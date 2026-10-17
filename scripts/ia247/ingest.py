#!/usr/bin/env python3
"""Ingestion for the site-architecture slice (website #247, milestone 1.3.0): the header, language
switch and footer strings.

Every string the new header and footer carry comes from four pinned Grok comments on issue #247,
fetched by id with `gh api` and held to the sha256 and `updated_at` recorded in sources.json. A
source that differs stops the run (exit 2). Nothing is typed here. Where two comments disagree the
later owner-approved one wins (the plan's copy table):

- 6218899916  version A: the five header items (en, zh-Hant, ja), the More label (all eight), the
              320 px language short names, the footer's six groups and their 31 pages, and
              zh-Hant's menu / wordmark / navigation names (read from its markup sketch);
- 6220575437  zh-Hans, de, fr, es, ko: the same strings;
- 6221114188  the layout revision: the header's second item is a short label (replaces A's and B's);
- 6221155465  en and ja: the menu label and the four accessible names.

Outputs: scripts/ia247/data.py (what the build reads) and scripts/ia247/slots.json (one row per
shipped string: slot x locale -> source comment, item label, value).

    python3 -B scripts/ia247/ingest.py           # fetch, verify, write
    python3 -B scripts/ia247/ingest.py --check   # fetch, verify, and fail if data.py or slots.json differ
"""
import hashlib
import json
import pprint
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))["issues"]["247"]
REPO = "redtear1115/mars-dawn-website"
A, B, C, D = (s["id"] for s in SOURCES)
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
FIRST = {"en": "en", "zh-Hant": "zh-hant", "ja": "ja"}   # the first-round languages, by column heading
B_HEADING = {"zh-hans": "zh-Hans", "de": "de", "fr": "fr", "es": "es", "ko": "ko"}
PRIMARY = ["en", "zh-hant", "ja", "zh-hans"]            # the order A lists the switch in


class Stop(SystemExit):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch() -> dict:
    """{comment id: body}, each held to its pinned sha256 and updated_at."""
    bodies = {}
    for pinned in SOURCES:
        cid = pinned["id"]
        out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{cid}"], capture_output=True, text=True)
        if out.returncode:
            raise Stop(f"gh api failed for comment {cid}: {out.stderr.strip()}")
        got = json.loads(out.stdout)
        digest = sha256(got["body"])
        if digest != pinned["sha256"] or got["updated_at"] != pinned["updated_at"]:
            raise Stop(f"comment {cid} (#247) differs from the pinned source: sha256 {digest} vs {pinned['sha256']}, "
                       f"updated_at {got['updated_at']} vs {pinned['updated_at']}")
        bodies[cid] = got["body"]
        print(f"verified comment {cid} (#247): sha256 {digest[:12]} updated_at {got['updated_at']}")
    return bodies


def split_row(line: str) -> list:
    line = line.strip()
    assert line.startswith("|") and line.endswith("|"), line
    return [c.strip() for c in line[1:-1].split("|")]


def tables(text: str) -> list:
    """Every pipe table in the text as a list of rows (cells), the separator row dropped."""
    found, cur = [], []
    for line in text.split("\n") + [""]:
        if line.startswith("|"):
            cells = split_row(line)
            if not all(set(c) <= set("-: ") for c in cells):
                cur.append(cells)
        elif cur:
            found.append(cur)
            cur = []
    return found


def section(body: str, heading: str) -> str:
    """The text under the heading line that starts with `heading`, up to the next heading of the same or a higher level."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.startswith(heading):
            level = len(line) - len(line.lstrip("#"))
            end = len(lines)
            for j in range(i + 1, len(lines)):
                m = re.match(r"(#+) ", lines[j])
                if m and len(m.group(1)) <= level:
                    end = j
                    break
            return "\n".join(lines[i + 1:end])
    raise Stop(f"no heading starting with {heading!r}")


def code(cell: str) -> list:
    return re.findall(r"`([^`]+)`", cell)


def one(pattern: str, text: str) -> str:
    found = re.findall(pattern, text)
    if len(found) != 1:
        raise Stop(f"expected exactly one match of {pattern!r}, got {found}")
    return found[0]


def parse(bodies: dict) -> tuple:
    """(DATA, SLOTS) from the four verified bodies."""
    slots = []   # {"slot", "locale", "source", "item", "value"}

    def put(data, slot, locale, source, item, value):
        data[locale][slot] = value
        slots.append({"slot": slot, "locale": locale, "source": source, "item": item, "value": value})

    data = {loc: {"nav": [None] * 5, "footer": [None] * 6} for loc in LOCALES}
    a = bodies[A]

    # -- A (a): the header's five items (en, zh-Hant, ja) and where they go --------------------------
    rows = tables(section(a, "## (a)"))[0]
    assert rows[0][2:] == ["en", "zh-Hant", "ja"], rows[0]
    hrefs = []
    for row in rows[1:]:
        n = int(row[0])
        hrefs.append(one(r"`(/[a-z/]*/)`", row[1]))
        for col, name in enumerate(rows[0][2:], start=2):
            loc = FIRST[name]
            data[loc]["nav"][n - 1] = row[col]
            slots.append({"slot": f"nav.{n}", "locale": loc, "source": A, "item": f"(a) {n} {name}", "value": row[col]})
    assert len(hrefs) == 5, hrefs

    # -- A (b): the More label, all eight --------------------------------------------------------------
    more = tables(section(a, "## (b)"))[0]
    assert more[0] == ["locale", "More 標籤"], more[0]
    for loc_name, label in more[1:]:
        loc = loc_name.lower()
        put(data, "more", loc, A, f"(b) More {loc_name}", label)

    # -- A (b): the 320 px short names, in the order the switch lists them ------------------------------
    shorts = one(r"summary 顯示目前語系的簡稱（([^）]+)）", a).split("／")
    assert len(shorts) == 8, shorts
    for loc, short in zip(PRIMARY + ["de", "fr", "es", "ko"], shorts):
        put(data, "abbr", loc, A, "(b) 320 px short name", short)

    # -- A (c): the footer's six groups -----------------------------------------------------------------
    rows = tables(section(a, "## (c)"))[0]
    assert rows[0][1:4] == ["en", "zh-Hant", "ja"], rows[0]
    pages = []
    for n, row in enumerate(rows[1:], start=1):
        pages.append(code(row[4]))
        for col, name in enumerate(rows[0][1:4], start=1):
            loc = FIRST[name]
            data[loc]["footer"][n - 1] = row[col]
            slots.append({"slot": f"footer.{n}", "locale": loc, "source": A, "item": f"(c) group {n} {name}", "value": row[col]})
    assert len(pages) == 6 and sum(len(p) for p in pages) == 31 - 0, [len(p) for p in pages]

    # -- A's markup sketch: zh-Hant's menu label and three accessible names (the wordmark's and the
    #    two navigation names; the footer's comes from the sketch below it) -----------------------------
    sketch = section(a, "### Header markup 草圖")
    put(data, "wordmark", "zh-hant", A, "header markup sketch: wordmark aria-label", one(r'class="wordmark"[^>]*aria-label="([^"]+)"', sketch))
    put(data, "nav_label", "zh-hant", A, "header markup sketch: main nav aria-label", one(r'<nav aria-label="([^"]+)">\s*<details class="nav-menu">', sketch))
    put(data, "lang_label", "zh-hant", A, "header markup sketch: language nav aria-label", one(r'<nav aria-label="([^"]+)" class="lang">', sketch))
    put(data, "menu", "zh-hant", A, "header markup sketch: menu summary", one(r"<summary>([^<]+)</summary>\s*<ul>", sketch))
    foot = section(a, "### Footer markup 草圖")
    put(data, "site_label", "zh-hant", A, "footer markup sketch: nav aria-label", one(r'<nav aria-label="([^"]+)">', foot))

    # -- B: zh-Hans, de, fr, es, ko ---------------------------------------------------------------------
    for loc, heading in B_HEADING.items():
        rows = tables(section(bodies[B], f"## {heading}"))[0]
        assert rows[0] == ["用途", "標籤"], rows[0]
        footer_n = 0
        for use, label in rows[1:]:
            m = re.match(r"Header (\d)", use)
            if m:
                n = int(m.group(1))
                data[loc]["nav"][n - 1] = label
                slots.append({"slot": f"nav.{n}", "locale": loc, "source": B, "item": use, "value": label})
            elif use.startswith("Footer "):
                footer_n += 1
                data[loc]["footer"][footer_n - 1] = label
                slots.append({"slot": f"footer.{footer_n}", "locale": loc, "source": B, "item": use, "value": label})
            elif use.startswith("320 px"):
                put(data, "menu", loc, B, use, label)
            elif use.startswith("字標"):
                put(data, "wordmark", loc, B, use, label)
            elif use.startswith("主要導覽"):
                put(data, "nav_label", loc, B, use, label)
            elif use.startswith("語言"):
                put(data, "lang_label", loc, B, use, label)
            elif use.startswith("網站導覽"):
                put(data, "site_label", loc, B, use, label)
            else:
                raise Stop(f"{loc}: unread row {use!r}")
        assert footer_n == 6, (loc, footer_n)
    # B confirms the short names: EN、繁中、日本語、简中、DE、FR、ES、KO, "不改".
    assert re.search(r"EN、繁中、日本語、简中、DE、FR、ES、KO", bodies[B]), "B no longer confirms the 320 px short names"

    # -- C: the header's second item is a short label, in all eight (replaces A's and B's) ---------------
    rows = tables(bodies[C])[0]
    assert rows[0][:2] == ["locale", "Header"], rows[0]
    footer2 = {}
    for row in rows[1:]:
        loc = row[0].lower()
        data[loc]["nav"][1] = row[1]
        slots = [s for s in slots if not (s["slot"] == "nav.2" and s["locale"] == loc)]
        slots.append({"slot": "nav.2", "locale": loc, "source": C, "item": f"header item 2 {row[0]}", "value": row[1]})
        footer2[loc] = row[2]
    assert len(footer2) == 8
    for loc, label in footer2.items():   # C restates the footer's second group: it must equal A's and B's
        assert data[loc]["footer"][1] == label, (loc, data[loc]["footer"][1], label)

    # -- D: en and ja, the menu label and the four accessible names ---------------------------------------
    rows = tables(bodies[D])[0]
    assert rows[0] == ["用途", "en", "ja"], rows[0]
    keys = {"320 px 選單": "menu", "字標 aria-label": "wordmark", "主要導覽 aria-label": "nav_label",
            "語言 aria-label": "lang_label", "網站導覽 aria-label": "site_label"}
    for row in rows[1:]:
        put(data, keys[row[0]], "en", D, row[0] + " en", row[1])
        put(data, keys[row[0]], "ja", D, row[0] + " ja", row[2])

    # every locale has every slot
    for loc in LOCALES:
        assert all(data[loc]["nav"]) and all(data[loc]["footer"]), loc
        for key in ("more", "abbr", "menu", "wordmark", "nav_label", "lang_label", "site_label"):
            assert data[loc].get(key), (loc, key)
    return {"nav_hrefs": hrefs, "footer_pages": pages, "locales": data}, slots


HEADER = '''"""The strings the #247 header, language switch and footer put on the site. Generated by
scripts/ia247/ingest.py from the pinned comments in sources.json; do not edit by hand (`ingest.py
--check` fails on a hand edit). Plain text: the build escapes it."""

DATA = '''


def render(data: dict, slots: list) -> tuple:
    return (HEADER + pprint.pformat(data, width=140, sort_dicts=False) + "\n",
            json.dumps({"sources": SOURCES, "slots": slots}, ensure_ascii=False, indent=1) + "\n")


def main() -> int:
    bodies = fetch()
    data, slots = parse(bodies)
    py, js = render(data, slots)
    if "--check" in sys.argv:
        ok = (HERE / "data.py").read_text(encoding="utf-8") == py and (HERE / "slots.json").read_text(encoding="utf-8") == js
        print("ia247 --check:", "data.py and slots.json match the pinned sources" if ok else "DIFFER from the pinned sources")
        return 0 if ok else 1
    (HERE / "data.py").write_text(py, encoding="utf-8")
    (HERE / "slots.json").write_text(js, encoding="utf-8")
    print(f"wrote {len(slots)} slots")
    return 0


if __name__ == "__main__":
    sys.exit(main())
