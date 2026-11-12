#!/usr/bin/env python3
"""Checks /changelog/'s app sections (website #273, #368) against their vendored sources.

Usage:
    python3 scripts/check_app_changelog.py [--root public] [--self-test] [--release]

The expected page is computed from vendor/app-release-notes/whats-new.json (each app version's What's
New on the App Store, vendored from the app repo's approved release notes by scripts/tmde130/ingest.py:
the Mac's under "versions", the iPhone and iPad app's under "ios") and scripts/tmde130/data.py (the page
copy, from the pinned comments on #273 and #368), never from the build's own code. The page has three
sections in this order: the Mac app (h2 #marsdawn-app), the iPhone and iPad app (h2 #marsdawn-ios), the
CLI (h2 #marsdawn-command-line-tool). In every locale's /changelog/index.html and its index.md twin:

  A1  whats-new.json's sha256 is the one in manifest.json.
  A2  A Mac version the App Store has in the locale's language with a What's New: every bullet, verbatim
      (escaped in the HTML), under that version's heading in the Mac section.
  A3  A version whose What's New is empty there (1.0.0, the first release): the "first release" line
      under its heading.
  A4  A Mac version the App Store doesn't have in that language: no heading for it in the Mac section.
  A5  The "earlier versions are in English only" line is there if and only if the locale misses a Mac
      version, as the Mac section's last paragraph.
  A6  The page copy: meta description, intro, the three section headings' text, the CLI line.
  A7  The CLI entries are h3 under the CLI heading, each with its old anchor (#marsdawn-0-6-3, ...),
      the same versions in every locale.
  A8  The Mac, iOS and CLI headings are all there, in that order (HTML and Markdown twin).
  A9  An iOS version's bullets: every one verbatim (escaped in the HTML) in the HTML and in the .md
      twin, and as many <li> as bullets. (Mac 1.0.2 and iOS 1.0.2 have the same title: the two are
      kept apart by section, the .md twin's Mac and iOS parts are cut at their ## headings first.)
  A10 An iOS version has its h3 with anchor ios-<version> (#ios-1-0-2) and the title MarsDawn <version>,
      and a "### MarsDawn <version>" in the .md twin's iOS part.
  A11 That h3 is inside the iOS section, and the iOS section has no other h3.
  A12 The iOS line ("versions before 1.0.2 are not listed") is the iOS section's last paragraph, in the
      HTML and in the .md twin.

--self-test plants one break per rule in a copy of the built pages and of the vendored file, and
fails unless each plant is reported by its own rule's message and nothing else, and the clean copy
passes. A2 and A9 also get plants that change the last character of a bullet in the HTML and one in the
.md twin, each of which must be reported as a missing bullet: a dropped bullet alone would still be
caught by the bullet count if the text comparison stopped comparing text (#292). Then it checks the
real tree (or --root's).

--release (not run in CI) fails while whats-new.json has a version marked "pending", Mac or iOS: a
version the App Store doesn't have yet is vendored from the app repo's release notes with a placeholder
date, and the site must not merge with that date. --self-test covers it too.
"""
import copy as copylib
import hashlib
import html
import importlib.util
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "vendor" / "app-release-notes"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
# The three sections, in page order: key, the id of its h2.
HEADS = (("app", "marsdawn-app"), ("ios", "marsdawn-ios"), ("cli", "marsdawn-command-line-tool"))


def load_copy() -> dict:
    spec = importlib.util.spec_from_file_location("tmde130_data", ROOT / "scripts" / "tmde130" / "data.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DATA


def page_dir(public: Path, locale: str) -> Path:
    return public / "changelog" if locale == "en" else public / locale / "changelog"


def plain(fragment: str) -> str:
    """Text of an HTML fragment as the .md twin writes it: links as [text](href), entities decoded."""
    text = re.sub(r'<a href="([^"]*)">(.*?)</a>', r"[\2](\1)", fragment)
    return twin(html.unescape(re.sub(r"<[^>]+>", "", text)))


def twin(text: str) -> str:
    """The site's HTML-to-Markdown converter writes a no-break space as a plain space (every twin does)."""
    return text.replace("\u00a0", " ")


def no_shy(text: str) -> str:
    return text.replace("&shy;", "").replace("­", "")


def section(page: str, anchor: str) -> str:
    """The HTML from the heading with this id to the next h2 or h3."""
    m = re.search(rf'<h3 id="{anchor}">.*?(?=<h[23][\s>]|$)', page, re.S)
    return m.group(0) if m else ""


def md_section(md: str, title: str) -> str:
    m = re.search(rf"^### {re.escape(title)}\n(.*?)(?=^##)", md + "\n##", re.S | re.M)
    return m.group(1) if m else ""


def html_heads(main: str) -> dict:
    """{key: (start, text)} of the h2 of each section that is there, found by its id."""
    out = {}
    for key, anchor in HEADS:
        m = re.search(rf'<h2 id="{anchor}">(.*?)</h2>', main, re.S)
        if m:
            out[key] = (m.start(), m.group(1))
    return out


def html_part(main: str, heads: dict, key: str) -> str:
    """The section's HTML: from its h2 to the next h2 of whichever section comes next (to the end for the
    last), so a section out of order still owns its own text."""
    if key not in heads:
        return ""
    start = heads[key][0]
    return main[start:min([s for s, _ in heads.values() if s > start] + [len(main)])]


def md_start(md: str, title: str) -> int:
    m = re.search(rf"^## {re.escape(title)}$", md, re.M)
    return m.start() if m else -1


def md_part(md: str, title: str) -> str:
    """The twin's text under the `## title` line, up to the next `## ` heading."""
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1) if m else ""


def last_paragraph(md_text: str) -> str:
    return md_text.rstrip().split("\n\n")[-1]


def release_problems(notes: dict) -> list:
    """--release: a version still marked pending (Mac or iOS) is not ready to merge."""
    pending = [f"{name} {e['version']}" for name, entries in (("Mac", notes["versions"]), ("iOS", notes["ios"]["versions"]))
               for e in entries if e.get("pending")]
    if not pending:
        return []
    return ["pending versions: " + ", ".join(pending) + " - set their dates from the App Store and run the ingester "
            "without `pending` before merging"]


def check(public: Path, vendor: Path, copy: dict) -> list:
    problems = []
    raw = (vendor / "whats-new.json").read_bytes()
    manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))
    if hashlib.sha256(raw).hexdigest() != manifest["whats-new.json"]:
        problems.append("A1 vendor/app-release-notes/whats-new.json does not match manifest.json's sha256")
    notes = json.loads(raw)
    to_store = {site: store for store, site in notes["locale_map"].items()}
    cli_sets = {}
    for locale in LOCALES:
        folder = page_dir(public, locale)
        page = no_shy((folder / "index.html").read_text(encoding="utf-8"))
        md = no_shy((folder / "index.md").read_text(encoding="utf-8"))
        c = copy[locale]
        where = f"{locale}/changelog"
        main = page[page.index('<main id="main">'):page.index("</main>")]
        heads = html_heads(main)
        titles = {key: twin(plain(c[f"{key}_h"])) for key, _ in HEADS}
        # A8: the three headings are there, Mac then iOS then CLI, in the HTML and in the twin.
        starts = [heads[key][0] if key in heads else -1 for key, _ in HEADS]
        md_starts = [md_start(md, titles[key]) for key, _ in HEADS]
        in_order = lambda xs: all(x >= 0 for x in xs) and xs == sorted(xs)  # noqa: E731
        if not in_order(starts) or not in_order(md_starts):
            problems.append(f"A8 {where}: the Mac, iOS and CLI headings are not all there, in that order")
        sound = all(x >= 0 for x in starts) and all(x >= 0 for x in md_starts)
        for key, _ in HEADS:
            if key in heads and heads[key][1] != c[f"{key}_h"]:
                problems.append(f"A6 {where}: the {key} heading is not the pinned one")
        app_part, ios_part = html_part(main, heads, "app"), html_part(main, heads, "ios")
        md_app, md_ios = md_part(md, titles["app"]), md_part(md, titles["ios"])
        omitted = False
        for entry in notes["versions"]:
            v, anchor = entry["version"], "app-" + entry["version"].replace(".", "-")
            text = entry["whatsNew"].get(to_store[locale])
            body, md_body = section(app_part, anchor), md_section(md_app, f"MarsDawn {v}")
            if text is None:
                omitted = True
                if f'id="{anchor}"' in main or f"### MarsDawn {v}\n" in md_app:
                    problems.append(f"A4 {where}: has a heading for {v}, which the App Store doesn't have in this language")
                continue
            if not body.startswith(f'<h3 id="{anchor}">MarsDawn {v}</h3>') or not md_body:
                problems.append(f"A2 {where}: no heading for {v}")
                continue
            if text:
                lacking = [line[2:] for line in text.split("\n")
                           if f"<li>{html.escape(line[2:], quote=False)}</li>" not in body
                           or f"\n- {twin(line[2:])}\n" not in "\n" + md_body + "\n"]
                for bullet in lacking:
                    problems.append(f"A2 {where}: {v} lacks the bullet {bullet[:40]!r}…")
                if not lacking and len(re.findall("<li>", body)) != len(text.split("\n")):
                    problems.append(f"A2 {where}: {v} has a different number of bullets from its What's New")
            elif f'<p>{c["first_release"]}</p>' not in body or plain(c["first_release"]) not in md_body:
                problems.append(f"A3 {where}: {v} lacks the first-release line")
        line = c.get("earlier")
        shown = [line is not None and app_part.rstrip().endswith(f"<p>{line}</p>"), line is not None and plain(line) in md_app]
        if omitted and not all(shown):
            problems.append(f"A5 {where}: the English-only line is missing")
        elif not omitted and any(shown):
            problems.append(f"A5 {where}: the English-only line is there, but no version is missing")
        # The iOS section (A9-A12). Skipped when a heading is missing or out of order: A8 has said so.
        ios_anchors = []
        if sound:
            for entry in notes["ios"]["versions"]:
                v, anchor = entry["version"], "ios-" + entry["version"].replace(".", "-")
                ios_anchors.append(anchor)
                text = entry["whatsNew"].get(to_store[locale])
                if not text:
                    problems.append(f"A9 {where}: iOS {v} has no What's New in this language in whats-new.json")
                    continue
                body, md_body = section(main, anchor), md_section(md_ios, f"MarsDawn {v}")
                if not body.startswith(f'<h3 id="{anchor}">MarsDawn {v}</h3>') or not md_body:
                    problems.append(f"A10 {where}: iOS {v} has no h3 with the anchor {anchor} and the title MarsDawn {v}, "
                                    f"or no ### heading in the .md twin's iOS part")
                    continue
                if f'<h3 id="{anchor}">' not in ios_part:
                    problems.append(f"A11 {where}: iOS {v} is not inside the iOS section")
                lacking = [line[2:] for line in text.split("\n")
                           if f"<li>{html.escape(line[2:], quote=False)}</li>" not in body
                           or f"\n- {twin(line[2:])}\n" not in "\n" + md_body + "\n"]
                for bullet in lacking:
                    problems.append(f"A9 {where}: iOS {v} lacks the bullet {bullet[:40]!r}…")
                if not lacking and len(re.findall("<li>", body)) != len(text.split("\n")):
                    problems.append(f"A9 {where}: iOS {v} has a different number of bullets from its What's New")
            # (An iOS h3 with a wrong anchor is A10's, not this one's.)
            foreign = [a for a in re.findall(r'<h3 id="([^"]*)"', ios_part) if not a.startswith("ios-")]
            if foreign:
                problems.append(f"A11 {where}: the iOS section has h3 that are not iOS versions: {foreign}")
            ios_line = c["ios_line"]
            if not ios_part.rstrip().endswith(f"<p>{ios_line}</p>") or last_paragraph(md_ios) != plain(ios_line):
                problems.append(f"A12 {where}: the iOS line is not the iOS section's last paragraph")
        if f'<meta name="description" content="{html.escape(c["description"])}">' not in page:
            problems.append(f"A6 {where}: the meta description is not the pinned one")
        intro = re.search(r'<section class="intro">\s*<h1>[^<]*</h1>\s*<p>(.*?)</p>', main, re.S)
        if not intro or intro.group(1) != c["intro"] or plain(c["intro"]) not in md:
            problems.append(f"A6 {where}: the intro is not the pinned one")
        cli_at = heads["cli"][0] if "cli" in heads else -1
        if cli_at < 0 or not main[cli_at:].split("</h2>", 1)[1].lstrip().startswith(f'<p>{c["cli_line"]}</p>'):
            problems.append(f"A6 {where}: the CLI line is not under the CLI heading")
        cli_part = main[cli_at:] if cli_at >= 0 else ""
        cli_heads = re.findall(r'<h3 id="([^"]*)">marsdawn ([0-9.]+)</h3>', cli_part)
        if not cli_heads or any(anchor != "marsdawn-" + v.replace(".", "-") for anchor, v in cli_heads) \
                or re.search(r"<h2[^>]*>marsdawn [0-9]", main):
            problems.append(f"A7 {where}: a CLI entry is not an h3 with its old anchor")
        cli_sets[locale] = [v for _, v in cli_heads]
    if len({tuple(s) for s in cli_sets.values()}) > 1:
        problems.append(f"A7 the CLI versions differ between locales: {cli_sets}")
    return problems


def self_test(source: Path) -> bool:
    copy = load_copy()
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        def fresh():
            for name in ("public", "vendor"):
                shutil.rmtree(base / name, ignore_errors=True)
            for locale in LOCALES:
                dst = page_dir(base / "public", locale)
                shutil.copytree(page_dir(source, locale), dst)
            shutil.copytree(VENDOR, base / "vendor")
            return base / "public", base / "vendor"

        def edit(path: Path, old: str, new: str, count: int = 1):
            text = path.read_text(encoding="utf-8")
            assert old in text, f"self-test plant has nothing to replace in {path}: {old[:60]!r}"
            path.write_text(text.replace(old, new, count), encoding="utf-8")

        def swap(path: Path, first: str, second: str, third: str):
            """Put the section that starts at `second` before the one that starts at `first`."""
            text = path.read_text(encoding="utf-8")
            a, b, z = text.index(first), text.index(second), text.index(third)
            assert a < b < z, f"self-test swap: the markers are not in order in {path}"
            path.write_text(text[:a] + text[b:z] + text[a:b] + text[z:], encoding="utf-8")

        def move_ios_entry(path: Path, anchor: str):
            """Cut an iOS version's h3 block out of the iOS section and put it first in the Mac section."""
            text = path.read_text(encoding="utf-8")
            start = text.index(f'<h3 id="{anchor}">')
            end = text.index("</ul>", start) + len("</ul>")
            block = text[start:end]
            text = text[:start] + text[end:]
            first_mac = text.index('<h3 id="app-')
            path.write_text(text[:first_mac] + block + "\n\n" + text[first_mac:], encoding="utf-8")

        public, vendor = fresh()
        clean = check(public, vendor, copy)
        if clean:
            print("self-test: the clean copy fails:\n  " + "\n  ".join(clean))
            return False
        notes = json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8"))
        first_bullet = notes["versions"][0]["whatsNew"]["en-US"].split("\n")[0][2:]
        first_v = notes["versions"][-1]["version"]
        first_html = html.escape(first_bullet, quote=False)
        lacks = f"A2 en/changelog: {notes['versions'][0]['version']} lacks the bullet "
        ios_v = notes["ios"]["versions"][0]["version"]
        ios_anchor = "ios-" + ios_v.replace(".", "-")
        ios_bullet = notes["ios"]["versions"][0]["whatsNew"]["en-US"].split("\n")[0][2:]
        ios_html = html.escape(ios_bullet, quote=False)
        ios_lacks = f"A9 en/changelog: iOS {ios_v} lacks the bullet "
        mac_h = '<h2 id="marsdawn-app">'
        ios_h = '<h2 id="marsdawn-ios">'
        cli_h = '<h2 id="marsdawn-command-line-tool">'
        wrong = lambda s: s[:-1] + ("#" if s[-1] != "#" else "%")  # noqa: E731
        plants = [
            ("A1", lambda p, v: edit(v / "whats-new.json", '"dates_read": "2026', '"dates_read": "2025')),
            ("A2", lambda p, v: edit(p / "changelog" / "index.html", f"  <li>{first_html}</li>\n", "")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.html", f"<li>{first_html}</li>", f"<li>{wrong(first_html)}</li>")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.md", f"\n- {twin(first_bullet)}\n", f"\n- {wrong(twin(first_bullet))}\n")),
            ("A3", lambda p, v: edit(p / "zh-hant" / "changelog" / "index.html", f'<p>{copy["zh-hant"]["first_release"]}</p>', "")),
            ("A4", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'{mac_h}{copy["de"]["app_h"]}</h2>\n',
                                     f'{mac_h}{copy["de"]["app_h"]}</h2>\n'
                                     f'<h3 id="app-{first_v.replace(".", "-")}">MarsDawn {first_v}</h3>\n')),
            ("A5", lambda p, v: edit(p / "ko" / "changelog" / "index.html", f'<p>{copy["ko"]["earlier"]}</p>', "")),
            ("A5", lambda p, v: edit(p / "changelog" / "index.html", f'\n\n{ios_h}',
                                     f'\n<p>{copy["en"]["earlier"]}</p>\n\n{ios_h}')),
            ("A6", lambda p, v: edit(p / "ja" / "changelog" / "index.html", copy["ja"]["intro"], copy["ja"]["intro"][:-1])),
            ("A6", lambda p, v: edit(p / "fr" / "changelog" / "index.html", f'{mac_h}{copy["fr"]["app_h"]}</h2>',
                                     f'{mac_h}{copy["fr"]["app_h"][:-1]}</h2>')),
            ("A6", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'{ios_h}{copy["de"]["ios_h"]}</h2>',
                                     f'{ios_h}{copy["de"]["ios_h"][:-1]}</h2>')),
            ("A7", lambda p, v: edit(p / "fr" / "changelog" / "index.html", '<h3 id="marsdawn-0-5-4">', '<h3 id="marsdawn-054">')),
            # A8: the Mac and iOS sections swapped, in the HTML and in the twin.
            ("A8", lambda p, v: swap(p / "ko" / "changelog" / "index.html", mac_h, ios_h, cli_h)),
            ("A8", lambda p, v: swap(p / "zh-hans" / "changelog" / "index.md",
                                     f"## {twin(plain(copy['zh-hans']['app_h']))}\n", f"## {twin(plain(copy['zh-hans']['ios_h']))}\n",
                                     f"## {twin(plain(copy['zh-hans']['cli_h']))}\n")),
            # A9: an iOS bullet gone, and one whose last character differs, in the HTML and in the twin.
            ("A9", lambda p, v: edit(p / "changelog" / "index.html", f"  <li>{ios_html}</li>\n", "")),
            (ios_lacks, lambda p, v: edit(p / "changelog" / "index.html", f"<li>{ios_html}</li>", f"<li>{wrong(ios_html)}</li>")),
            (ios_lacks, lambda p, v: edit(p / "changelog" / "index.md", f"\n- {twin(ios_bullet)}\n", f"\n- {wrong(twin(ios_bullet))}\n")),
            # A10: the iOS anchor is wrong.
            ("A10", lambda p, v: edit(p / "ja" / "changelog" / "index.html", f'<h3 id="{ios_anchor}">', '<h3 id="ios-102">')),
            # A11: the iOS entry sits in the Mac section.
            ("A11", lambda p, v: move_ios_entry(p / "fr" / "changelog" / "index.html", ios_anchor)),
            # A12: the iOS line is gone, from the HTML and from the twin.
            ("A12", lambda p, v: edit(p / "changelog" / "index.html", f'<p>{copy["en"]["ios_line"]}</p>', "")),
            ("A12", lambda p, v: edit(p / "es" / "changelog" / "index.md", plain(copy["es"]["ios_line"]), "")),
        ]
        for rule, plant in plants:
            public, vendor = fresh()
            plant(public, vendor)
            found = check(public, vendor, copy)
            if len(found) != 1 or not found[0].startswith(rule if rule.endswith(" ") else rule + " "):
                print(f"self-test: plant for {rule} reported {found}")
                ok = False
            else:
                print(f"self-test: {rule.split()[0]} caught: {found[0][:100]}")
        # --release: pending versions fail it, shipped ones pass.
        shipped = copylib.deepcopy(notes)
        for entry in shipped["versions"] + shipped["ios"]["versions"]:
            entry.pop("pending", None)
        both = copylib.deepcopy(shipped)
        both["versions"][0]["pending"] = both["ios"]["versions"][0]["pending"] = True
        mac_only = copylib.deepcopy(shipped)
        mac_only["versions"][0]["pending"] = True
        ios_only = copylib.deepcopy(shipped)
        ios_only["ios"]["versions"][0]["pending"] = True
        for label, data, want in (("none pending", shipped, 0), ("a Mac version pending", mac_only, 1),
                                  ("an iOS version pending", ios_only, 1), ("both pending", both, 1)):
            found = release_problems(data)
            if len(found) != want or (want and not found[0].startswith("pending versions: ")):
                print(f"self-test: --release with {label} reported {found}")
                ok = False
            else:
                print(f"self-test: --release with {label}: {found[0][:100] if found else 'passes'}")
        if "pending versions: Mac %s, iOS %s" % (both["versions"][0]["version"], both["ios"]["versions"][0]["version"]) \
                not in release_problems(both)[0]:
            print("self-test: --release does not name both versions")
            ok = False
    return ok


def main() -> int:
    args = sys.argv[1:]
    public = ROOT / "public"
    if "--root" in args:
        public = Path(args[args.index("--root") + 1])
    if "--self-test" in args and not self_test(public):
        print("check_app_changelog: self-test FAILED")
        return 1
    problems = check(public, VENDOR, load_copy())
    if "--release" in args:
        problems += release_problems(json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8")))
    for p in problems:
        print(p)
    if problems:
        return 1
    print(f"check_app_changelog: ok ({len(LOCALES)} locales)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
