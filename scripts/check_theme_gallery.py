#!/usr/bin/env python3
"""Checks the community theme gallery (mars-dawn-website #145, plan-website-104 W4): the card and
filter HTML that scripts/build_pages.py builds from public/themes/v1/index.json at build time, and
the report/mailto URLs that public/assets/theme-gallery.js builds and opens.

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
- **No href ever carries a theme's id/version, anywhere in a gallery page** (round 2 review, #151):
  GA4's enhanced measurement records an outbound click by the clicked <a>'s own href (`link_url`),
  so a real `<a href>` carrying `theme_id`/`theme_version` -- even to the report form -- would
  report that theme to analytics on every click, contradicting the privacy policy. Report and
  Report-by-email are real `<button>`s with only `data-theme-id`/`data-theme-version` (never a
  URL); the URL itself is built and opened by public/assets/theme-gallery.js's reportUrl()/mailUrl()
  at click time via window.open(), the same pattern as the simulator's own Submit button. This is
  checked three ways: no href in a built card contains a hostile display string; a dedicated
  scanner (`_href_leak_problems`) is proven to catch a planted `<a href="...issues/new?theme_id=...">`
  by feeding it one directly; and that same scanner is run against every real, built
  `themes/gallery/index.html` on disk, in every locale.
- **The report link and mailto decode to exactly id + version.** theme-gallery.js's reportUrl() and
  mailUrl() are run for real under plain `node` (no npm; the module guards its DOM-touching code
  behind `typeof document !== "undefined"`, the same way scripts/check_theme_sim.mjs imports the
  simulator's own pure-logic modules) and their output is parsed with urllib.parse.parse_qs,
  requiring it to hold exactly the id and version that went in, byte for byte, for values that
  themselves contain characters a naive encoder could mangle (spaces, `&`, `=`, `#`, non-ASCII).
- **The empty state.** An index with no themes renders the empty-state message and no card list.
- **The scenario filter.** Only scenarios actually present among the fixture's themes get a
  filter button, in SCENARIOS order, plus "All"; a scenario id outside the closed SCENARIOS list
  is dropped from both the card's badges and the filter, the way an older app would drop an
  unknown id.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parent
sys.path.insert(0, str(ROOT))
import build_pages as bp  # noqa: E402

HOSTILE_RAW = [
    '"<>&\'',
    "</script>",
    "javascript:",
]
# Of the substrings above, only the HTML metacharacters ever need escaping to appear safely as
# text; "javascript:" is inert as plain page text (harmful only as the scheme of a live href, and
# that's what the href-leak checks below prove it never becomes) and would still read as
# "javascript:" after html.escape(), so it isn't part of the "never appears unescaped" assertion.
HOSTILE_MUST_ESCAPE = ['"<>&\'', "</script>"]

HREF_RE = re.compile(r'href="([^"]*)"')
# Any of these inside a decoded href means a theme's report data reached a real link.
FORBIDDEN_HREF_SUBSTRINGS = ("issues/new", "theme_id=", "theme_version=")

THEME_GALLERY_JS = REPO_ROOT / "public" / "assets" / "theme-gallery.js"


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


def _href_leak_problems(fragment: str, where: str, extra_substrings=()) -> list:
    """Every href="..." in `fragment` that carries a theme-report pattern or one of
    `extra_substrings` (typically a specific theme's id/version), decoded first so neither HTML
    entities nor percent-encoding can hide it."""
    problems = []
    for href in _hrefs(fragment):
        decoded = unquote(html.unescape(href))
        for pattern in FORBIDDEN_HREF_SUBSTRINGS:
            if pattern in decoded:
                problems.append(f"{where}: href leaks {pattern!r}: {href!r}")
        for extra in extra_substrings:
            if extra and extra in decoded:
                problems.append(f"{where}: href leaks {extra!r}: {href!r}")
    return problems


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

    # No href at all should exist on the report/mail buttons any more -- they're <button>s.
    problems += _href_leak_problems(card, "fixture card", extra_substrings=("hostile-theme",))
    return problems


def check_href_leak_scanner_catches_a_plant() -> list:
    """Proves the scanner used above and below actually works, by feeding it a regression the way
    it used to look (a real <a href> to the issue form with theme_id/theme_version in the query) --
    the "plant -> red" the coordinator asked for."""
    problems = []
    planted = (
        '<li class="theme-card">'
        '<a href="https://github.com/redtear1115/mars-dawn-website/issues/new?'
        'theme_id=hostile-theme&amp;theme_version=1.0.0">Report</a>'
        "</li>"
    )
    found = _href_leak_problems(planted, "plant", extra_substrings=("hostile-theme",))
    if not found:
        problems.append("href-leak scanner: a planted <a href=\"...issues/new?theme_id=...\"> went uncaught")
    return problems


def check_built_gallery_pages_have_no_leaking_hrefs() -> list:
    """The same scanner, run over every real, built themes/gallery/index.html this repo ships (all
    4 locales) -- not just the in-memory fixture above."""
    problems = []
    site = REPO_ROOT / "public"
    pages = sorted(site.rglob("themes/gallery/index.html"))
    if not pages:
        problems.append("built pages: found no themes/gallery/index.html under public/ -- run scripts/build_pages.py")
    for path in pages:
        text = path.read_text(encoding="utf-8")
        problems += _href_leak_problems(text, str(path.relative_to(REPO_ROOT)))
    return problems


def _run_theme_gallery_js(theme_id: str, version: str) -> dict:
    code = (
        f"import {{ reportUrl, mailUrl }} from {json.dumps(THEME_GALLERY_JS.resolve().as_uri())};\n"
        f"console.log(JSON.stringify({{\n"
        f"  r: reportUrl({json.dumps(theme_id)}, {json.dumps(version)}),\n"
        f"  m: mailUrl({json.dumps(theme_id)}, {json.dumps(version)}),\n"
        f"}}));\n"
    )
    result = subprocess.run(["node", "--input-type=module", "-e", code], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"node failed for {theme_id!r}/{version!r}: {result.stderr.strip()}")
    return json.loads(result.stdout)


def check_report_link_roundtrip() -> list:
    problems = []
    cases = [
        ("olympus-dusk", "1.0.0"),
        ("weird id/with space", "1.0.0&extra=1"),
        ("héllo", "1.0.0#frag"),
    ]
    for theme_id, version in cases:
        try:
            urls = _run_theme_gallery_js(theme_id, version)
        except RuntimeError as error:
            problems.append(str(error))
            continue

        report_parsed = urlparse(urls["r"])
        report_query = parse_qs(report_parsed.query, keep_blank_values=True)
        if report_query.get("theme_id") != [theme_id] or report_query.get("theme_version") != [version]:
            problems.append(
                f"report url: {theme_id!r}/{version!r} round-tripped to "
                f"{report_query.get('theme_id')!r}/{report_query.get('theme_version')!r}"
            )
        if report_query.get("template") != ["theme-report.yml"]:
            problems.append(f"report url: template param missing or wrong: {report_query.get('template')!r}")
        if not urls["r"].startswith("https://github.com/redtear1115/mars-dawn-website/issues/new?"):
            problems.append(f"report url: unexpected base: {urls['r']!r}")

        mail_parsed = urlparse(urls["m"])
        if mail_parsed.scheme != "mailto" or mail_parsed.path != bp.EMAIL:
            problems.append(f"mailto: wrong address or scheme: {urls['m']!r}")
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
        ("href-leak scanner catches a plant", check_href_leak_scanner_catches_a_plant),
        ("built gallery pages have no leaking hrefs", check_built_gallery_pages_have_no_leaking_hrefs),
        ("report link / mailto round-trip (theme-gallery.js under node)", check_report_link_roundtrip),
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
