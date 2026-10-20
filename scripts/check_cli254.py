#!/usr/bin/env python3
"""Checks that the built /cli/, /cli/agents/ and /changelog/ carry website #254's copy, verbatim.

scripts/cli254/data.py holds the copy, carried from the pinned issue comments by scripts/cli254/ingest.py
(which needs gh and runs locally). This reads the built pages, not build_pages.py, and fails unless every
locale's page holds each piece in full and in its place:

- /cli/: each `open` and `export` bullet as its own <li> in that command's list, the two version sentences
  as paragraphs, and the `marsdawn theme` section (heading, commands, bullets) between export and the
  next h2;
- /cli/agents/: the folder `status` bullet right after the `folder` item, and each schema note beside
  its schema file's link;
- /changelog/: every CLI entry with its heading, date line and bullets, newest first, among the others.

--self-test changes one character of one piece in a copy of each built page and fails unless every
change is caught.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rich_pages  # noqa: E402
from cli254 import data  # noqa: E402

SITE = HERE.parent / "public"
ROOTS = {"en": "", "zh-hant": "zh-hant/", "zh-hans": "zh-hans/", "ja": "ja/", "de": "de/", "fr": "fr/",
         "es": "es/", "ko": "ko/"}
SCHEMA_FILES = {"open_v4": "open.v4.json", "open": "open.v3.json", "error_v3": "error.v3.json", "error": "error.v2.json"}
ORDER = ["0.7.2", "0.7.1", "0.7.0", "0.6.4", "0.6.3", "0.6.1", "0.5.4"]


def li(md: str) -> str:
    return f"<li>{rich_pages.md_inline(md)}</li>"


def section(page: str, start: str) -> str:
    i = page.find(start)
    if i < 0:
        return ""
    m = re.compile(r"\n<h[23][ >]").search(page, i + len(start))
    return page[i:m.start() if m else len(page)]


def problems_for(locale: str, pages: dict) -> list:
    d, out = data.DATA[locale], []
    cli, agents, changelog = pages["cli"], pages["cli/agents"], pages["changelog"]
    open_sec = section(cli, "<h3>marsdawn open</h3>")
    for item in d["open_items"]:
        if li(item) not in open_sec:
            out.append(f"{locale}/cli: open item missing: {item[:50]!r}")
    if f"<p>{rich_pages.md_inline(d['open_since'])}</p>" not in open_sec:
        out.append(f"{locale}/cli: open's version sentence missing")
    export_sec = section(cli, "<h3>marsdawn export</h3>")
    for item in d["export_items"] + d["export_after_json"]:
        if li(item) not in export_sec:
            out.append(f"{locale}/cli: export item missing: {item[:50]!r}")
    if f"<p>{rich_pages.md_inline(d['export_since'])}</p>" not in export_sec:
        out.append(f"{locale}/cli: export's version sentence missing")
    theme_sec = section(cli, "<h3>marsdawn theme</h3>")
    if not theme_sec or cli.find("<h3>marsdawn theme</h3>") < cli.find("<h3>marsdawn export</h3>"):
        out.append(f"{locale}/cli: no marsdawn theme section after export")
    head, _, rest = d["theme_section"].partition("\n\n")
    intro, _, rest = rest.partition("\n\n")
    if f"<p>{rich_pages.md_inline(intro)}</p>" not in theme_sec or rich_pages.md_blocks(rest) not in theme_sec:
        out.append(f"{locale}/cli: the theme section's text differs")
    if rich_pages.escape(data.SHARED["theme_example"]) not in theme_sec:
        out.append(f"{locale}/cli: the theme section's commands differ")
    folder = re.search(r"<li><code>folder</code>.*?</li>\n  ", agents)
    for item in d["agents_folder_items"]:
        if not folder or not agents[folder.end():].startswith(li(item)):
            out.append(f"{locale}/cli/agents: the folder status item is not right after the folder item")
    for key, note in d["schema_notes"].items():
        name = SCHEMA_FILES[key]
        if f'<a href="/schemas/cli/{name}">{name}</a>: {note}</li>' not in agents:
            out.append(f"{locale}/cli/agents: schema note {key} missing")
    for v, md in d["changelog"].items():
        heading, _, rest = md.partition("\n\n")
        m = re.search(rf'<h3 id="marsdawn-{v.replace(".", "-")}">marsdawn {re.escape(v)}</h3>\n(.*?)\n\n', changelog + "\n\n", re.S)
        if not m or m.group(1) != rich_pages.md_blocks(rest):
            out.append(f"{locale}/changelog: {v} differs or is missing")
    seen = re.findall(r'<h3 id="marsdawn-[0-9-]+">marsdawn ([0-9.]+)</h3>', changelog)
    want = [v for v in ORDER if v in seen]
    if seen[:len(want)] != want:
        out.append(f"{locale}/changelog: CLI versions out of order: {seen}")
    return out


def read_pages(locale: str) -> dict:
    root = SITE / ROOTS[locale]
    return {slug: (root / slug / "index.html").read_text(encoding="utf-8") for slug in ("cli", "cli/agents", "changelog")}


def check() -> list:
    out = []
    for locale in ROOTS:
        if locale not in data.DATA:
            out.append(f"{locale}: no #254 copy in scripts/cli254/data.py")
            continue
        out += problems_for(locale, read_pages(locale))
    return out


def self_test() -> int:
    caught = missed = 0
    for locale in data.DATA:
        pages = read_pages(locale)
        d = data.DATA[locale]
        plants = [("cli", li(d["open_items"][0])), ("cli", li(d["export_items"][-1])),
                  ("cli", rich_pages.md_blocks(d["theme_section"].split("\n\n", 2)[2])),
                  ("cli/agents", li(d["agents_folder_items"][0])),
                  ("cli/agents", d["schema_notes"]["open_v4"]),
                  ("changelog", rich_pages.md_blocks(d["changelog"]["0.7.2"].partition("\n\n")[2]))]
        for slug, piece in plants:
            text = pages[slug]
            if piece not in text:
                print(f"self-test: {locale}/{slug}: the piece to plant in is not on the page")
                missed += 1
                continue
            mid = len(piece) // 2
            changed = piece[:mid] + ("X" if piece[mid] != "X" else "Y") + piece[mid + 1:]
            if problems_for(locale, {**pages, slug: text.replace(piece, changed, 1)}):
                caught += 1
            else:
                print(f"self-test: {locale}/{slug}: a one-character change was NOT caught")
                missed += 1
    print(f"self-test: {caught} plants caught, {missed} missed")
    return 1 if missed or not caught else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    problems = check()
    for p in problems:
        print(p)
    if problems:
        print(f"{len(problems)} problems")
        return 1
    print(f"#254 copy present and verbatim in {len(data.DATA)} locales")
    return self_test() if args.self_test else 0


if __name__ == "__main__":
    sys.exit(main())
