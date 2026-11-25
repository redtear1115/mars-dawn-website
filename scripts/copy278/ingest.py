#!/usr/bin/env python3
"""The /from-hackmd/ copy (website #278), carried by program from Aria's comments, never retyped.

source/ holds the two comments as posted: 6684344469 (en, zh-Hant, Ray approved in 6685109512) and
6685163599 (the other six; Aria checks ja, Ray's decision in 6685212059). data.py is generated from them:

    python3 -I -B scripts/copy278/ingest.py          # write data.py
    python3 -I -B scripts/copy278/ingest.py --check  # fail if data.py isn't what the sources give

The `:::` sentence (Ray approved it on 2026-11-18, "#278 ::: ok", decision comment 6965143868) is put in by
build(): the other two source files hold its words (6964983008 section 1 for en and zh-Hant, 6965344647 for the
other six) and where it goes. In every locale the 【待定，#300】 line of 6684344469 / 6685163599 is taken out and
the sentence stands as its own paragraph just before the "A few things look different" line. The "now" string
the comment gives must be found exactly once in the locale's copy, and so must that line, or this stops.
Nothing else of 6964983008 changes the approved copy (its section 2 corrects Aria's notes, not the page text),
and its optional rows (section 3) are not applied.
"""
import html
import pprint
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SOURCES = {"6684344469-en-zh-hant.md": {"en": "en", "zh-Hant": "zh-hant"},
           "6685163599-six.md": {name: name for name in ("zh-hans", "ja", "ko", "de", "fr", "es")}}
COLON_EN = "6964983008-colon-en-zh-hant.md"
COLON_SIX = "6965344647-colon-six.md"


def block(text: str, heading: str) -> str:
    """The ```md block under `## heading`; the fence that ends it is the first one at column 0."""
    match = re.search(rf"^## {re.escape(heading)}\n+```md\n(.*?)^```$", text, re.S | re.M)
    if not match:
        raise SystemExit(f"no copy for {heading}")
    return match.group(1)


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline(text: str) -> str:
    """Markdown inline syntax to HTML; everything else is HTML-escaped and otherwise untouched."""
    out, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*", text):
        out.append(esc(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f'<a href="{html.escape(m.group(2), quote=True)}">{esc(m.group(1))}</a>')
        elif m.group(3) is not None:
            out.append(f"<code>{esc(m.group(3))}</code>")
        else:
            out.append(f"<strong>{inline(m.group(4))}</strong>")   # a bold phrase can hold a code span
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def cells(line: str) -> list:
    # strip(" ") and not strip(): fr and de copy carries U+00A0, which strip() would take off
    return [inline(cell.strip(" ")) for cell in line.strip(" ").removeprefix("|").removesuffix("|").split("|")]


def parse(md: str) -> dict:
    """Blocks, in order, as HTML-ready fields: ("h1"|"h2", text), ("p", html), ("ul", [html]), ("pre", text),
    ("table", head, rows), ("faq", heading, [(question, answer)]). The text of an h1 or h2 is plain, the rest is HTML (the FAQ's heading and questions are escaped)."""
    title = re.search(r"^Title: (.+)$", md, re.M).group(1)
    description = re.search(r"^Meta description: (.+)$", md, re.M).group(1)
    lines = md.split("\n")
    i = next(n for n, line in enumerate(lines) if line.startswith("# "))
    blocks = []
    while i < len(lines):
        line = lines[i]
        if not line.strip(" "):
            i += 1
        elif line.startswith("# "):
            blocks.append(("h1", line[2:]))
            i += 1
        elif line.startswith("### "):
            blocks.append(("h3", line[4:]))
            i += 1
        elif line.startswith("## "):
            blocks.append(("h2", line[3:]))
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            head, rule, *body = rows
            assert set(rule) <= set("|- "), rule
            blocks.append(("table", cells(head), [cells(row) for row in body]))
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(inline(lines[i][2:]))
                i += 1
            blocks.append(("ul", items))
        elif line.startswith("    "):
            code = []
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip(" ")):
                code.append(lines[i])
                i += 1
            while not code[-1].strip(" "):
                code.pop()
            blocks.append(("pre", "\n".join(row[4:] for row in code)))
        else:
            blocks.append(("p", inline(line)))
            i += 1
    # the last h2 and what follows it are the FAQ: its heading, then h3, one paragraph, h3, one paragraph
    k = max(n for n, b in enumerate(blocks) if b[0] == "h2")
    faq = blocks[k + 1:]
    if len(faq) % 2 or any(b[0] != ("h3", "p")[n % 2] for n, b in enumerate(faq)):
        raise SystemExit(f"{title}: the questions aren't h3 and paragraph pairs")
    blocks[k:] = [("faq", esc(blocks[k][1]), [(esc(q[1]), a[1]) for q, a in zip(faq[::2], faq[1::2])])]
    return {"title": title, "description": description, "blocks": blocks}


def colon_copy() -> dict:
    """Per locale (page key): the line to take out, the line to put the sentence before, the sentence. All read
    from the two comments' text: the table cells "現在" and 「…」 in section 1 and the md code blocks."""
    en_text = (HERE / "source" / COLON_EN).read_text(encoding="utf-8")
    six_text = (HERE / "source" / COLON_SIX).read_text(encoding="utf-8")
    out = {}
    anchors = re.search(r"改放在「(.+?)」（zh-Hant 是「(.+?)」）之前", en_text)
    en_md = re.findall(r"^```md\n(.*?)\n```$", en_text.split("給 Dev 複製的原文", 1)[1], re.S | re.M)[:2]
    for n, (key, label) in enumerate((("en", "en"), ("zh-hant", "zh-Hant"))):
        row = re.search(rf"^\| {label} 第 \d+ 行[^|]*\| (.+?) \| .+ \|$", en_text, re.M)
        out[key] = {"now": row.group(1), "before": anchors.group(n + 1), "sentence": en_md[n]}
    for locale in ("zh-hans", "ja", "ko", "de", "fr", "es"):
        row = re.search(rf"^\| `## {locale}` 第 \d+ 行[^|]*\| ``(.+?)`` \|.*?在「(.+?)」（同則", six_text, re.M)
        out[locale] = {"now": row.group(1), "before": row.group(2), "sentence": block(six_text, locale).rstrip("\n")}
    return out


def put_colon(md: str, locale: str, colon: dict) -> str:
    """md with the 【待定，#300】 line out and the sentence in as its own paragraph before the "A few things" line."""
    if md.count(colon["now"]) != 1:
        raise SystemExit(f"{locale}: the 'now' string is found {md.count(colon['now'])} times, not once")
    lines = md.split("\n")
    gone = [n for n, line in enumerate(lines) if line == colon["now"]]
    # the comment names the line to go before with an ordinary space where fr's page line has U+00A0: locate it ignoring that
    before = [n for n, line in enumerate(lines) if line.replace("\u00a0", " ") == colon["before"]]
    if len(gone) != 1 or len(before) != 1:
        raise SystemExit(f"{locale}: the 'now' line is found {len(gone)} times and {colon['before']!r} {len(before)} times, not once each")
    if before[0] > gone[0]:
        raise SystemExit(f"{locale}: {colon['before']!r} comes after the 'now' line")
    del lines[gone[0]]
    lines[before[0]:before[0]] = [colon["sentence"], ""]
    return "\n".join(lines)


def build() -> dict:
    colon = colon_copy()
    data = {}
    for name, locales in SOURCES.items():
        text = (HERE / "source" / name).read_text(encoding="utf-8")
        for heading, locale in locales.items():
            data[locale] = parse(put_colon(block(text, heading), locale, colon[locale]))
    if any("【待定" in repr(copy) for copy in data.values()):
        raise SystemExit("【待定 is still in the copy")
    return data


def main() -> int:
    source = ('"""Generated by ingest.py from source/. Do not edit: change the source and regenerate."""\n\nDATA = '
              + pprint.pformat(build(), width=120, sort_dicts=False) + "\n")
    target = HERE / "data.py"
    if "--check" in sys.argv:
        if target.read_text(encoding="utf-8") != source:
            print("data.py doesn't match source/")
            return 1
        print("data.py matches source/")
        return 0
    target.write_text(source, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
