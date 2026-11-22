#!/usr/bin/env python3
"""Ingestion for website #363: the site's old iOS claims ("iPhone and iPad don't open JSON or YAML",
"doesn't export PDFs") are corrected in 8 locales.

Every string this slice puts on the site comes from a pinned issue comment and is carried here by
program, never typed. Each comment is fetched by id with `gh api` and held to the sha256 and
`updated_at` in sources.json; a comment that changed stops the run.

- A, #363 6800152890 (Aria, 2026-11-11): 6 keys per locale in 8 locales, as the one ```json block under
  the heading that starts "## 8 語全文". en and zh-Hant were approved by the owner on 2026-11-12
  ("decision", #363 6801523231); the other six locales are Aria's, under the standing machine-locale OK.
- "decision" is only verified, not read.
- "sentence", #371 6835867929 (Aria, 2026-11-12; a comment on the draft PR, not on #363): one new sentence per
  locale, the table under the one heading that starts "## 加的那一句" (columns 語系 and 新增句). It goes into
  limits_ios only, immediately before the one sentence that names iCloud, with the sentence rule of
  build_pages.py's _COPY363_SENTENCE_END. The checks that stop the run are in parse_sentence() and
  insert_sentence(): the table, the locales, the zh-Hant junction taken from the heading's 「…」 anchors, the en
  line the comment gives for the result, and U+00A0.
- "date", #363 (the id in sources.json; Ray's go-ahead of 2026-11-16 is #363 6908334791): roadmap_updated per locale as
  the one ```json block under the heading that starts "## 決定（資料）". It replaces A's roadmap_updated, which
  names the estimated launch day; parse_date() holds it to the same rules as A.

Writes scripts/copy363/data.py, which scripts/build_pages.py reads as copy363_data.

    python3 -I -B scripts/copy363/ingest.py           # verify the comments, write data.py
    python3 -I -B scripts/copy363/ingest.py --check   # verify, compare with data.py, write nothing

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
KEYS = ["features_other_last", "limits_ios", "limits_other", "vs_lacks_ios", "payonce_ios", "roadmap_updated"]
# U+00A0 per key in fr; every other locale has none.
NBSP_FR = {"features_other_last": 0, "limits_ios": 2, "limits_other": 2, "vs_lacks_ios": 1, "payonce_ios": 1,
           "roadmap_updated": 1}
BULLET = re.compile(r"- \*\*[^*\n]+\*\*[^\n]+")   # limits_ios and limits_other: '- **Label:** rest', one line
# The table's locale column, as the comment writes it; each is one of LOCALES in lower case.
TABLE_LOCALES = ["en", "zh-Hant", "zh-Hans", "ja", "ko", "de", "fr", "es"]
# Must stay the rule of build_pages.py's _COPY363_SENTENCE_END; sentence_rule_is_build_pages() checks the file.
SENTENCE_END_PATTERN = r"(?<=[.!?])(?= )|(?<=[。！？])"
SENTENCE_END = re.compile(SENTENCE_END_PATTERN)


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
    kind = pinned.get("kind", "issues")   # a comment on a pull request has /pull/N# in its html_url, not /issues/N#
    if kind not in ("issues", "pull"):
        raise Stop(f"comment {pinned['id']}: pinned kind {kind!r}, expected issues or pull")
    if f"/{kind}/{pinned['issue']}#" not in got["html_url"]:
        raise Stop(f"comment {pinned['id']} is not on #{pinned['issue']}: {got['html_url']}")
    print(f"verified #{pinned['issue']} comment {pinned['id']}: sha256 {digest[:12]} updated_at {got['updated_at']}")
    return got["body"]


def json_block(body: str) -> str:
    """The one ```json block in the section whose heading starts "## 8 語全文" (up to the next ## heading)."""
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
            want = NBSP_FR[key] if locale == "fr" else 0
            if value.count(" ") != want:
                raise Stop(f"A {locale} {key}: {value.count(chr(0xa0))} U+00A0, expected {want}")
        for key in ("limits_ios", "limits_other"):
            if not BULLET.fullmatch(d[key]):
                raise Stop(f"A {locale} {key}: not a one-line '- **Label:** rest' bullet: {d[key]!r}")
    return data


def parse_date(body: str, data: dict) -> dict:
    """data with roadmap_updated of each locale replaced by the "## 決定（資料）" JSON block's string."""
    sections = [part for part in re.split(r"(?m)^(?=## )", body) if part.startswith("## 決定（資料）")]
    if len(sections) != 1:
        raise Stop(f'date: {len(sections)} "## 決定（資料）" sections, expected 1')
    found = re.findall(r"(?ms)^```json\n(.*?)\n```$", sections[0])
    if len(found) != 1:
        raise Stop(f'date: {len(found)} json blocks under "## 決定（資料）", expected 1')
    got = json.loads(found[0])
    if sorted(got) != sorted(LOCALES):
        raise Stop(f"date: locales {sorted(got)}")
    out = {locale: dict(d) for locale, d in data.items()}
    for locale in LOCALES:
        if list(got[locale]) != ["roadmap_updated"]:
            raise Stop(f"date {locale}: keys {sorted(got[locale])}, expected only roadmap_updated")
        value = got[locale]["roadmap_updated"]
        want = NBSP_FR["roadmap_updated"] if locale == "fr" else 0
        if not isinstance(value, str) or "\r" in value or value.count("\xa0") != want:
            raise Stop(f"date {locale}: not a one-line string with {want} U+00A0: {value!r}")
        out[locale]["roadmap_updated"] = value
    return out


def sentence_rule_is_build_pages() -> None:
    src = (HERE.parent / "build_pages.py").read_text(encoding="utf-8")
    want = f'_COPY363_SENTENCE_END = re.compile(r"{SENTENCE_END_PATTERN}")\n'
    if src.count(want) != 1:
        raise Stop("sentence rule: build_pages.py's _COPY363_SENTENCE_END is not the rule used here")


def sentences_of(text: str) -> list:
    """The pieces of text by the sentence rule, as build_pages._copy363_sentences gives them."""
    pieces = SENTENCE_END.split(text)
    if pieces and pieces[-1] == "":
        pieces.pop()
    if "".join(pieces) != text:
        raise Stop(f"sentence rule: the pieces do not join back to {text!r}")
    return pieces


def parse_sentence(body: str) -> dict:
    """The new sentence per locale, the zh-Hant anchors and the en line, from the one "## 加的那一句" section."""
    sections = [part for part in re.split(r"(?m)^(?=## )", body) if part.startswith("## 加的那一句")]
    if len(sections) != 1:
        raise Stop(f'sentence: {len(sections)} "## 加的那一句" sections, expected 1')
    lines = re.split(r"\r?\n", sections[0])
    anchors = re.findall(r"「([^」]*)」", lines[0])
    if len(anchors) != 2 or not anchors[0].startswith("…") or not anchors[1].endswith("…"):
        raise Stop(f"sentence: the heading's 「…」 anchors are not 「…before」 and 「after…」: {anchors!r}")
    before, after = anchors[0][1:], anchors[1][:-1]
    if not before or not after:
        raise Stop(f"sentence: an empty anchor in the heading: {anchors!r}")

    blocks, current = [], []
    for line in lines[1:]:
        if line.startswith("|"):
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    if len(blocks) != 1:
        raise Stop(f'sentence: {len(blocks)} tables under "## 加的那一句", expected 1')
    rows = []
    for line in blocks[0]:
        if not line.endswith("|"):
            raise Stop(f"sentence: a table line does not end with |: {line!r}")
        rows.append([cell.strip() for cell in line[1:-1].split("|")])
    if any(len(row) != 2 for row in rows) or len(rows) < 2:
        raise Stop(f"sentence: the table is not 2 columns: {rows!r}")
    if rows[0] != ["語系", "新增句"] or not all(re.fullmatch(r":?-+:?", cell) for cell in rows[1]):
        raise Stop(f"sentence: the table header is not 語系 | 新增句 over a divider row: {rows[:2]!r}")
    if sorted(row[0] for row in rows[2:]) != sorted(TABLE_LOCALES):
        raise Stop(f"sentence: table locales {[row[0] for row in rows[2:]]!r}, expected each of {TABLE_LOCALES} once")
    sentences = {}
    for locale, text in rows[2:]:
        if not text:
            raise Stop(f"sentence {locale}: empty cell")
        sentences[locale.lower()] = text
    if sorted(sentences) != sorted(LOCALES):
        raise Stop(f"sentence: locales {sorted(sentences)}")

    marks = [i for i, line in enumerate(lines) if line.startswith("改完的 en 整點")]
    quotes = [line for line in lines if line.startswith(">")]
    if len(marks) != 1 or len(quotes) != 1:
        raise Stop(f"sentence: {len(marks)} '改完的 en 整點' lines and {len(quotes)} blockquote lines, expected 1 and 1")
    if next((line for line in lines[marks[0] + 1:] if line.strip()), None) != quotes[0] or not quotes[0].startswith("> "):
        raise Stop("sentence: the blockquote line is not the line under '改完的 en 整點', or does not start with '> '")
    return {"sentences": sentences, "before": before, "after": after, "en_line": quotes[0][2:]}


def insert_sentence(data: dict, got: dict) -> dict:
    """data with each locale's limits_ios holding its new sentence immediately before the iCloud sentence."""
    sentence_rule_is_build_pages()
    out = {locale: dict(d) for locale, d in data.items()}
    for locale in LOCALES:
        sentence = got["sentences"][locale]
        if "\n" in sentence or "\r" in sentence:
            raise Stop(f"sentence {locale}: has a line break")
        if sentence.count("\xa0"):
            raise Stop(f"sentence {locale}: the new sentence has {sentence.count(chr(0xa0))} U+00A0, expected 0")
        old = data[locale]["limits_ios"]
        if sentence in old:
            raise Stop(f"sentence {locale}: limits_ios already holds the new sentence")
        pieces = sentences_of(old)
        hits = [i for i, piece in enumerate(pieces) if "iCloud" in piece]
        if len(hits) != 1 or hits[0] != len(pieces) - 1:
            raise Stop(f"sentence {locale}: {len(hits)} sentences name iCloud (at {hits}) of {len(pieces)}; "
                       "expected one, the last")
        head, tail = "".join(pieces[:-1]), pieces[-1]
        if locale == "zh-hant":
            if old.count(got["before"]) != 1 or not head.endswith(got["before"]):
                raise Stop(f"sentence zh-hant: the heading's 「…{got['before']}」 is not once, ending where the "
                           f"sentence goes: {old.count(got['before'])} times")
            if not tail.startswith(got["after"]):
                raise Stop(f"sentence zh-hant: the sentence after the insertion does not start with 「{got['after']}…」")
        joint = " " if tail.startswith(" ") else ""
        new = head + joint + sentence + tail
        if new.count(sentence) != 1:
            raise Stop(f"sentence {locale}: the new sentence is in limits_ios {new.count(sentence)} times, expected 1")
        if not BULLET.fullmatch(new):
            raise Stop(f"sentence {locale}: not a one-line '- **Label:** rest' bullet: {new!r}")
        want = NBSP_FR["limits_ios"] if locale == "fr" else 0
        if new.count("\xa0") != want:
            raise Stop(f"sentence {locale}: limits_ios has {new.count(chr(0xa0))} U+00A0, expected {want}")
        if locale == "en":
            if not new.startswith("- ") or new[2:] != got["en_line"]:
                raise Stop(f"sentence en: limits_ios differs from the en line in the comment:\n  {new[2:]!r}\n"
                           f"  {got['en_line']!r}")
        out[locale]["limits_ios"] = new
    return out


def build() -> dict:
    c = SOURCES["comments"]
    fetch(c["decision"])
    data = parse_a(fetch(c["A"]))
    data = insert_sentence(data, parse_sentence(fetch(c["sentence"])))
    data = parse_date(fetch(c["date"]), data)
    return {locale: {k: data[locale][k] for k in KEYS} for locale in LOCALES}


def render(data: dict) -> str:
    pins = {k: {f: v[f] for f in ("issue", "kind", "id", "sha256", "updated_at") if f in v}
            for k, v in SOURCES["comments"].items()}
    return ('"""Generated by scripts/copy363/ingest.py from the pinned comments in sources.json. Do not edit by hand."""\n\n'
            f"SOURCES = {pprint.pformat(pins, width=110, sort_dicts=True)}\n\n"
            f"DATA = {pprint.pformat(data, width=110, sort_dicts=True)}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = render(build())
    target = HERE / "data.py"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("data.py differs from what the pinned comments give", file=sys.stderr)
            return 1
        print("data.py matches the pinned comments")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target.relative_to(HERE.parent.parent)}: {', '.join(LOCALES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
