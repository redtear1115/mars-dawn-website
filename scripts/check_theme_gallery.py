#!/usr/bin/env python3
"""Checks the community theme gallery (mars-dawn-website #145, plan-website-104 W4): the card and
filter HTML that scripts/build_pages.py builds from public/themes/v1/index.json at build time.

This is a --self-test-only script (like several others in this repo, e.g. check_redirects.py):
there is nothing in the committed public/themes/v1/index.json to check against yet (it's empty,
issue #77), so this plants fixtures of its own instead of reading the real tree.

Usage:
    python3 scripts/check_theme_gallery.py --self-test

What it proves:

- **Escaping.** A hostile theme (name/summary containing `"<>&'`, `</script>` and `javascript:`)
  never reaches the page unescaped: build_pages.community_gallery_html() runs every index-derived
  string through html.escape(quote=True) before it's written into HTML, so the raw hostile
  substrings never appear literally in the output, only their escaped form does.
- **Nothing display-derived lands in an href.** Every href="..." in the card HTML is collected and
  checked against the hostile name/summary substrings: none of them appear there, because only a
  theme's own id and version (not its name or summary) ever go into an href.
- **The report link and mailto decode to exactly id + version.** theme_report_url() and
  theme_report_mailto() are built with urllib.parse.quote; this parses the resulting query strings
  back with urllib.parse.parse_qs and requires them to hold exactly the id and version that went
  in, byte for byte, for values that themselves contain characters a naive encoder could mangle
  (spaces, `&`, `=`, `#`, non-ASCII).
- **The empty state.** An index with no themes renders the empty-state message and no card list.
- **The scenario filter.** Only scenarios actually present among the fixture's themes get a
  filter button, in SCENARIOS order, plus "All"; a scenario id outside the closed SCENARIOS list
  is dropped from both the card's badges and the filter, the way an older app would drop an
  unknown id.
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import build_pages as bp  # noqa: E402

HOSTILE_RAW = [
    '"<>&\'',
    "</script>",
    "javascript:",
]
# Of the substrings above, only the HTML metacharacters ever need escaping to appear safely as
# text; "javascript:" is inert as plain page text (harmful only as the scheme of a live href, and
# that's what check_hrefs proves it never becomes) and would still read as "javascript:" after
# html.escape(), so it isn't part of the "never appears unescaped" assertion below.
HOSTILE_MUST_ESCAPE = ['"<>&\'', "</script>"]

HREF_RE = re.compile(r'href="([^"]*)"')


def _fixture_theme(theme_id="hostile-theme", version="1.0.0", scenarios=None, name=None, summary=None):
    return {
        "id": theme_id,
        "version": version,
        "name": {"en": name if name is not None else 'Hostile "<>&\' Theme'},
        "summary": {"en": summary if summary is not None else "Bad </script> and javascript:alert(1) summary"},
        "author": {"name": "Author \"<>&' Name"},
        "minAppVersion": "1.1.0",
        "scenarios": scenarios if scenarios is not None else ["agent-review"],
        "files": {"theme.json": {"path": f"{theme_id}/{version}/theme.json", "sha256": "a" * 64}},
        "previews": {
            "light": f"{theme_id}/{version}/preview-light.png",
            "dark": f"{theme_id}/{version}/preview-dark.png",
        },
    }


def _hrefs(fragment: str) -> list:
    return HREF_RE.findall(fragment)


def check_escaping_and_hrefs() -> list:
    problems = []
    entry = _fixture_theme()
    card = bp._theme_card_html("en", entry)

    for raw in HOSTILE_MUST_ESCAPE:
        if raw in card:
            problems.append(f"escaping: the raw hostile substring {raw!r} appears literally in the card HTML")

    escaped_name = html.escape('Hostile "<>&\' Theme', quote=True)
    escaped_summary = html.escape("Bad </script> and javascript:alert(1) summary", quote=True)
    if escaped_name not in card:
        problems.append("escaping: the escaped theme name is missing from the card HTML")
    if escaped_summary not in card:
        problems.append("escaping: the escaped theme summary is missing from the card HTML")

    for href in _hrefs(card):
        decoded = unquote(html.unescape(href))
        for raw in HOSTILE_RAW:
            if raw in decoded:
                problems.append(f"href: a display-derived hostile substring {raw!r} reached href={href!r}")

    return problems


def check_report_link_roundtrip() -> list:
    problems = []
    cases = [
        ("olympus-dusk", "1.0.0"),
        ("weird id/with space", "1.0.0&extra=1"),
        ("héllo", "1.0.0#frag"),
    ]
    for theme_id, version in cases:
        url = bp.theme_report_url(theme_id, version)
        parsed = urlparse(url)
        query = parse_qs(parsed.query, keep_blank_values=True)
        if query.get("theme_id") != [theme_id] or query.get("theme_version") != [version]:
            problems.append(
                f"report url: {theme_id!r}/{version!r} round-tripped to "
                f"{query.get('theme_id')!r}/{query.get('theme_version')!r}"
            )
        if query.get("template") != ["theme-report.yml"]:
            problems.append(f"report url: template param missing or wrong: {query.get('template')!r}")

        mailto = bp.theme_report_mailto(theme_id, version)
        mail_parsed = urlparse(mailto)
        if mail_parsed.scheme != "mailto" or mail_parsed.path != bp.EMAIL:
            problems.append(f"mailto: wrong address or scheme: {mailto!r}")
        mail_query = parse_qs(mail_parsed.query)
        want_subject = f"Theme report: {theme_id} {version}"
        if mail_query.get("subject") != [want_subject]:
            problems.append(f"mailto: subject round-tripped to {mail_query.get('subject')!r}, wanted {[want_subject]!r}")
    return problems


def check_empty_state() -> list:
    problems = []
    original = bp.read_theme_index
    bp.read_theme_index = lambda: {"schemaVersion": 1, "generatedAt": "x", "themes": [], "revoked": []}
    try:
        html_out = bp.community_gallery_html("en")
    finally:
        bp.read_theme_index = original
    if bp.GALLERY_EMPTY["en"] not in html_out:
        problems.append("empty state: the empty-state message is missing when there are no themes")
    if "theme-gallery-cards" in html_out:
        problems.append("empty state: a card list was rendered even though the index has no themes")
    return problems


def check_scenario_filter() -> list:
    problems = []
    themes = [
        _fixture_theme("theme-a", "1.0.0", scenarios=["formal-output"]),
        _fixture_theme("theme-b", "1.0.0", scenarios=["agent-review", "not-a-real-scenario"]),
    ]
    original = bp.read_theme_index
    bp.read_theme_index = lambda: {"schemaVersion": 1, "generatedAt": "x", "themes": themes, "revoked": []}
    try:
        html_out = bp.community_gallery_html("en")
    finally:
        bp.read_theme_index = original

    for present in ("agent-review", "formal-output"):
        if f'data-scenario="{present}"' not in html_out:
            problems.append(f"filter: expected a button for present scenario {present!r}")
    for absent in ("technical-docs", "notes-sharing"):
        if f'data-scenario="{absent}"' in html_out:
            problems.append(f"filter: an absent scenario {absent!r} got a filter button anyway")
    if "not-a-real-scenario" in html_out:
        problems.append("filter: an unknown scenario id from the index leaked into the page")
    if 'data-scenario="all"' not in html_out:
        problems.append("filter: missing the 'all' button")
    return problems


def self_test() -> int:
    checks = [
        ("escaping and hrefs", check_escaping_and_hrefs),
        ("report link / mailto round-trip", check_report_link_roundtrip),
        ("empty state", check_empty_state),
        ("scenario filter", check_scenario_filter),
    ]
    failures = 0
    for name, check in checks:
        problems = check()
        if problems:
            failures += len(problems)
            print(f"self-test: {name}: FAILED")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"self-test: {name}: ok")
    print(f"self-test: {len(checks)} checks, {failures} failures")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    print("usage: check_theme_gallery.py --self-test")
    return 1


if __name__ == "__main__":
    sys.exit(main())
