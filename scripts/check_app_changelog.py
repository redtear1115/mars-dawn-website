#!/usr/bin/env python3
"""Checks /changelog/'s app section (website #273) against its vendored sources.

Usage:
    python3 scripts/check_app_changelog.py [--root public] [--self-test]

The expected page is computed from vendor/app-release-notes/whats-new.json (each app version's What's
New on the Mac App Store, vendored from the app repo's approved release notes by
scripts/tmde130/ingest.py) and scripts/tmde130/data.py (the page copy, from the pinned comments on
#273), never from the build's own code. In every locale's /changelog/index.html and its index.md twin:

  A1  whats-new.json's sha256 is the one in manifest.json.
  A2  A version the App Store has in the locale's language with a What's New: every bullet, verbatim
      (escaped in the HTML), under that version's heading.
  A3  A version whose What's New is empty there (1.0.0, the first release): the "first release" line
      under its heading.
  A4  A version the App Store doesn't have in that language: no heading for it.
  A5  The "earlier versions are in English only" line is there if and only if the locale misses a
      version, as the App section's last paragraph.
  A6  The page copy: meta description, intro, both section headings in order (app, then CLI), the
      CLI line.
  A7  The CLI entries are h3 under the CLI heading, each with its old anchor (#marsdawn-0-6-3, ...),
      the same versions in every locale.

--self-test plants one break per rule in a copy of the built pages and of the vendored file, and
fails unless each plant is reported by its own rule's message and nothing else, and the clean copy
passes. A2 also gets a plant that changes the last character of a bullet in the HTML and one in the
.md twin, each of which must be reported as a missing bullet: a dropped bullet alone would still be
caught by the bullet count if the text comparison stopped comparing text (#292). Then it checks the
real tree.
"""
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
        app_at = main.find(f'<h2 id="marsdawn-app">{c["app_h"]}</h2>')
        cli_at = main.find(f'<h2 id="marsdawn-command-line-tool">{c["cli_h"]}</h2>')
        if app_at < 0 or cli_at < 0 or app_at > cli_at:
            problems.append(f"A6 {where}: the app heading and then the CLI heading are not both there in order")
        app_part = main[app_at:cli_at] if 0 <= app_at < cli_at else ""
        omitted = False
        for entry in notes["versions"]:
            v, anchor = entry["version"], "app-" + entry["version"].replace(".", "-")
            text = entry["whatsNew"].get(to_store[locale])
            body, md_body = section(app_part, anchor), md_section(md, f"MarsDawn {v}")
            if text is None:
                omitted = True
                if f'id="{anchor}"' in main or f"### MarsDawn {v}\n" in md:
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
        shown = [line is not None and app_part.rstrip().endswith(f"<p>{line}</p>"), line is not None and plain(line) in md]
        if omitted and not all(shown):
            problems.append(f"A5 {where}: the English-only line is missing")
        elif not omitted and any(shown):
            problems.append(f"A5 {where}: the English-only line is there, but no version is missing")
        if f'<meta name="description" content="{html.escape(c["description"])}">' not in page:
            problems.append(f"A6 {where}: the meta description is not the pinned one")
        intro = re.search(r'<section class="intro">\s*<h1>[^<]*</h1>\s*<p>(.*?)</p>', main, re.S)
        if not intro or intro.group(1) != c["intro"] or plain(c["intro"]) not in md:
            problems.append(f"A6 {where}: the intro is not the pinned one")
        if cli_at < 0 or not main[cli_at:].split("</h2>", 1)[1].lstrip().startswith(f'<p>{c["cli_line"]}</p>'):
            problems.append(f"A6 {where}: the CLI line is not under the CLI heading")
        cli_part = main[cli_at:] if cli_at >= 0 else ""
        heads = re.findall(r'<h3 id="([^"]*)">marsdawn ([0-9.]+)</h3>', cli_part)
        if not heads or any(anchor != "marsdawn-" + v.replace(".", "-") for anchor, v in heads) \
                or re.search(r"<h2[^>]*>marsdawn [0-9]", main):
            problems.append(f"A7 {where}: a CLI entry is not an h3 with its old anchor")
        cli_sets[locale] = [v for _, v in heads]
    if len({tuple(s) for s in cli_sets.values()}) > 1:
        problems.append(f"A7 the CLI versions differ between locales: {cli_sets}")
    return problems


def self_test() -> bool:
    copy = load_copy()
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        def fresh():
            for name in ("public", "vendor"):
                shutil.rmtree(base / name, ignore_errors=True)
            for locale in LOCALES:
                dst = page_dir(base / "public", locale)
                shutil.copytree(page_dir(ROOT / "public", locale), dst)
            shutil.copytree(VENDOR, base / "vendor")
            return base / "public", base / "vendor"

        def edit(path: Path, old: str, new: str, count: int = 1):
            text = path.read_text(encoding="utf-8")
            assert old in text, f"self-test plant has nothing to replace in {path}: {old[:60]!r}"
            path.write_text(text.replace(old, new, count), encoding="utf-8")

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
        plants = [
            ("A1", lambda p, v: edit(v / "whats-new.json", '"dates_read": "2026', '"dates_read": "2025')),
            ("A2", lambda p, v: edit(p / "changelog" / "index.html", f"  <li>{first_html}</li>\n", "")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.html", f"<li>{first_html}</li>",
                                      f"<li>{first_html[:-1]}{'#' if first_html[-1] != '#' else '%'}</li>")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.md", f"\n- {twin(first_bullet)}\n",
                                      f"\n- {twin(first_bullet)[:-1]}{'#' if first_bullet[-1] != '#' else '%'}\n")),
            ("A3", lambda p, v: edit(p / "zh-hant" / "changelog" / "index.html", f'<p>{copy["zh-hant"]["first_release"]}</p>', "")),
            ("A4", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'<h2 id="marsdawn-app">{copy["de"]["app_h"]}</h2>\n',
                                     f'<h2 id="marsdawn-app">{copy["de"]["app_h"]}</h2>\n'
                                     f'<h3 id="app-{first_v.replace(".", "-")}">MarsDawn {first_v}</h3>\n')),
            ("A5", lambda p, v: edit(p / "ko" / "changelog" / "index.html", f'<p>{copy["ko"]["earlier"]}</p>', "")),
            ("A5", lambda p, v: edit(p / "changelog" / "index.html", '\n\n<h2 id="marsdawn-command-line-tool">',
                                     f'\n<p>{copy["en"]["earlier"]}</p>\n\n<h2 id="marsdawn-command-line-tool">')),
            ("A6", lambda p, v: edit(p / "ja" / "changelog" / "index.html", copy["ja"]["intro"], copy["ja"]["intro"][:-1])),
            ("A7", lambda p, v: edit(p / "fr" / "changelog" / "index.html", '<h3 id="marsdawn-0-5-4">', '<h3 id="marsdawn-054">')),
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
    return ok


def main() -> int:
    args = sys.argv[1:]
    public = ROOT / "public"
    if "--root" in args:
        public = Path(args[args.index("--root") + 1])
    if "--self-test" in args and not self_test():
        print("check_app_changelog: self-test FAILED")
        return 1
    problems = check(public, VENDOR, load_copy())
    for p in problems:
        print(p)
    if problems:
        return 1
    print(f"check_app_changelog: ok ({len(LOCALES)} locales)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
