#!/usr/bin/env python3
"""Ingestion for website #369: the site's copy catches up with the new iOS and print features (plan A).

Every string this slice puts on the site comes from a pinned issue comment and is carried here by
program, never typed. Each comment is fetched by id with `gh api` and held to the sha256 and
`updated_at` in sources.json; a comment that changed stops the run.

- A, #369 6796812714 (Aria, 2026-11-11): 13 keys per locale in 8 locales, as the one ```json block under
  the heading "## 8 語全文". en and zh-Hant were approved by the owner on 2026-11-11 ("approval",
  #369 6796859928); the other six locales are Aria's, under the standing machine-locale OK.
- "scope" (#369 6773514660, Daphne's positions) and "plan_a" (#369 6796672544, the plan A decision) are
  only verified, not read.

Of the 13 keys, 11 ship (DATA). plan4 and outline_plus describe features that are not shipping yet; they
are kept apart in HELD, which scripts/build_pages.py must never read.

Writes scripts/copy369/data.py, which scripts/build_pages.py reads as copy369_data.

    python3 -I -B scripts/copy369/ingest.py           # verify the comments, write data.py
    python3 -I -B scripts/copy369/ingest.py --check   # verify, compare with data.py, write nothing

It needs gh, so it runs locally, never in CI.
"""
import argparse
import hashlib
import json
import pprint
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
REPO = "redtear1115/mars-dawn-website"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "ko", "de", "fr", "es"]
KEYS = ["home_ios", "faq", "plan4", "outline_plus", "fold_h", "fold", "export", "ios_s2", "ios_s3", "devnote",
        "pdf", "layout", "next"]
HELD_KEYS = ["plan4", "outline_plus"]
SHIP_KEYS = [k for k in KEYS if k not in HELD_KEYS]
NBSP = {"de": 5, "fr": 15}   # U+00A0 per locale, over all 13 values; every other locale has none
HOME_IOS = re.compile(r"1\. [^\n]+\n2\. [^\n]+\n3\. [^\n]+\n\n[^\n]+")


class Stop(SystemExit):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch(pinned: dict) -> str:
    out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{pinned['id']}"], capture_output=True, text=True)
    if out.returncode:
        raise Stop(f"gh api failed for comment {pinned['id']}: {out.stderr.strip()}")
    got = json.loads(out.stdout)
    digest = sha256(got["body"])
    if digest != pinned["sha256"] or got["updated_at"] != pinned["updated_at"]:
        raise Stop(f"comment {pinned['id']} differs from the pinned source: sha256 {digest} vs {pinned['sha256']}, "
                   f"updated_at {got['updated_at']} vs {pinned['updated_at']}")
    if f"/issues/{pinned['issue']}#" not in got["html_url"]:
        raise Stop(f"comment {pinned['id']} is not on #{pinned['issue']}: {got['html_url']}")
    print(f"verified #{pinned['issue']} comment {pinned['id']}: sha256 {digest[:12]} updated_at {got['updated_at']}")
    return got["body"]


def json_block(body: str) -> str:
    """The one ```json block in the "## 8 語全文" section (up to the next ## heading)."""
    sections = [part for part in re.split(r"(?m)^(?=## )", body) if part.startswith("## 8 語全文")]
    if len(sections) != 1:
        raise Stop(f'A: {len(sections)} "## 8 語全文" sections, expected 1')
    found = re.findall(r"(?ms)^```json\n(.*?)\n```$", sections[0])
    if len(found) != 1:
        raise Stop(f'A: {len(found)} json blocks under "## 8 語全文", expected 1')
    return found[0]


def parse_a(body: str) -> dict:
    data = json.loads(json_block(body))
    if sorted(data) != sorted(LOCALES):
        raise Stop(f"A: locales {sorted(data)}")
    for locale in LOCALES:
        d = data[locale]
        if sorted(d) != sorted(KEYS):
            raise Stop(f"A {locale}: keys {sorted(d)}")
        for key, value in d.items():
            if not isinstance(value, str):
                raise Stop(f"A {locale} {key}: not a string: {value!r}")
            if "\r" in value:
                raise Stop(f"A {locale} {key}: has \\r")
        nbsp = sum(value.count(" ") for value in d.values())
        if nbsp != NBSP.get(locale, 0):
            raise Stop(f"A {locale}: {nbsp} U+00A0, expected {NBSP.get(locale, 0)}")
        if not HOME_IOS.fullmatch(d["home_ios"]):
            raise Stop(f"A {locale}: home_ios is not three numbered lines and a limit line: {d['home_ios']!r}")
    return data


def build() -> tuple:
    c = SOURCES["comments"]
    for name in ("approval", "scope", "plan_a"):
        fetch(c[name])
    data = parse_a(fetch(c["A"]))
    ship = {locale: {k: data[locale][k] for k in SHIP_KEYS} for locale in LOCALES}
    held = {locale: {k: data[locale][k] for k in HELD_KEYS} for locale in LOCALES}
    return ship, held


def render(ship: dict, held: dict) -> str:
    pins = {k: {f: v[f] for f in ("issue", "id", "sha256", "updated_at")} for k, v in SOURCES["comments"].items()}
    return ('"""Generated by scripts/copy369/ingest.py from the pinned comments in sources.json. Do not edit by hand.\n\n'
            "DATA holds the keys that ship. HELD holds plan4 and outline_plus, which describe features that are not\n"
            'shipping yet: nothing that builds the site may read HELD."""\n\n'
            f"SOURCES = {pprint.pformat(pins, width=110, sort_dicts=True)}\n\n"
            f"DATA = {pprint.pformat(ship, width=110, sort_dicts=True)}\n\n"
            f"HELD = {pprint.pformat(held, width=110, sort_dicts=True)}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    ship, held = build()
    text = render(ship, held)
    target = HERE / "data.py"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("data.py differs from what the pinned comments give", file=sys.stderr)
            return 1
        print("data.py matches the pinned comments")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target.relative_to(HERE.parent.parent)}: {', '.join(sorted(ship))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
