#!/usr/bin/env python3
"""Ingestion for website #254: /cli/, /cli/agents/ and /changelog/ catch up with marsdawn 0.7.2.

Every string this slice puts on the site comes from a pinned issue comment and is carried here by
program, never typed. Each comment is fetched by id with `gh api` and held to the sha256 and
`updated_at` in sources.json; a comment that changed stops the run.

- A, #254 6233038202 (Grok, 2026-10-17): /cli/'s `open --wait` bullets and version sentence,
  /cli/agents/'s folder `status` bullet, the 0.6.4 changelog entry.
- B, #254 6294978172 (Grok, 2026-10-20): the 0.7.2 and 0.6.1 changelog entries, /cli/'s export
  bullets and version sentence, the `marsdawn theme` section, /cli/agents/'s schema notes.
- C, #286 6280485104 (Grok, 2026-10-20): the 0.7.1 and 0.7.0 changelog entries (its 0.6.4 is void, #286
  6294982770), with Grok's edits in #286 6280891336 section 6c applied by program (each old text must
  occur exactly once), and the ja layout name ハンドブック (#254 6295059627) in place of マニュアル in ja 0.7.1.
- The owner approved A and B for en, zh-Hant and ja on 2026-10-20 (#254 6295102211), and C with those
  edits on 2026-10-21 (#254 6295263711); both are pinned.
- The other five locales: Grok's needs-i18n comment(s), listed in sources.json under "i18n", under
  the standing machine-locale OK.

Writes scripts/cli254/data.py, which scripts/build_pages.py reads (apply_cli254). The text is the
comments' Markdown; the build turns it into HTML with rich_pages.md_inline. Schema notes are HTML in
the source and stay HTML.

    python3 -I -B scripts/cli254/ingest.py           # verify the comments, write data.py
    python3 -I -B scripts/cli254/ingest.py --check   # verify, compare with data.py, write nothing

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
LABELS = {"en": "en", "zh-Hant": "zh-hant", "zh-Hans": "zh-hans", "ja": "ja", "ko": "ko", "de": "de",
          "fr": "fr", "es": "es"}
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
SCHEMA_KEYS = ["open_v4", "open", "error_v3", "error"]


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


def label(line: str):
    """The locale a line names on its own (**en**, **zh-Hant**, ### ja ...), or None."""
    m = re.fullmatch(r"(?:\*\*|#+ )([A-Za-z-]+)(?:\*\*)?\s*", line)
    return LABELS.get(m.group(1)) if m else None


def blocks(body: str):
    """(section, locale, text) for every fenced block, in order. section is the last ###/#### heading
    outside a fence (its number, such as "2a."); locale is the last locale label, reset by a heading."""
    section, locale, fence, out = "", None, None, []
    for line in body.replace("\r\n", "\n").split("\n"):
        if fence is not None:
            if line.strip() == "```":
                out.append((section, locale, "\n".join(fence)))
                fence = None
            else:
                fence.append(line)
            continue
        if line.startswith("```"):
            fence = []
            continue
        loc = label(line)
        if loc:
            locale = loc
        elif re.match(r"#{2,4} ", line):
            section, locale = line.lstrip("#").strip().split(" ")[0], None
    if fence is not None:
        raise Stop("an unclosed fence")
    return out


def table_rows(body: str, section: str):
    """The rows of the Markdown table under the heading that starts with section."""
    lines = body.replace("\r\n", "\n").split("\n")
    start = next(i for i, line in enumerate(lines) if re.match(rf"#{{2,4}} {re.escape(section)}", line))
    rows = []
    for line in lines[start + 1:]:
        if re.match(r"#{2,4} ", line):
            break
        if line.startswith("|"):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def bullets(text: str) -> list:
    lines = text.split("\n")
    if not lines or not all(line.startswith("- ") for line in lines):
        raise Stop(f"not a bullet list: {text!r}")
    return [line[2:] for line in lines]


def one_line(text: str) -> str:
    if "\n" in text or not text.strip():
        raise Stop(f"not one line: {text!r}")
    return text


def entry(text: str, version: str) -> str:
    if not text.startswith(f"## marsdawn {version}\n\n"):
        raise Stop(f"not the {version} entry: {text[:40]!r}")
    return text


def take(found: list, section: str, locale, count: int) -> list:
    got = [text for sec, loc, text in found if sec == section and loc == locale]
    if len(got) != count:
        raise Stop(f"section {section} {locale}: {len(got)} blocks, expected {count}")
    return got


def parse_a(body: str, locales: list, data: dict) -> None:
    found = blocks(body)
    for loc in locales:
        d = data[loc]
        o1, o2, o3, since = take(found, "1.", loc, 4)
        d["open_items"] = [b for t in (o1, o2, o3) for b in bullets(t)]
        d["open_since"] = one_line(since)
        (folder,) = take(found, "2.", loc, 1)
        d["agents_folder_items"] = bullets(folder)
        (cl,) = take(found, "3.", loc, 1)
        d["changelog"]["0.6.4"] = entry(cl, "0.6.4")


def parse_b(body: str, locales: list, data: dict, shared: dict) -> None:
    found = blocks(body)
    (example,) = take(found, "2b.", None, 1)
    shared["theme_example"] = example
    for loc in locales:
        d = data[loc]
        c072, c061 = take(found, "1.", loc, 2)
        d["changelog"]["0.7.2"] = entry(c072, "0.7.2")
        d["changelog"]["0.6.1"] = entry(c061, "0.6.1")
        items, after_json, since = take(found, "2a.", loc, 3)
        d["export_items"] = bullets(items)
        d["export_after_json"] = bullets(after_json)
        d["export_since"] = one_line(since)
        (theme,) = take(found, "2b.", loc, 1)
        if not theme.startswith("### marsdawn theme\n\n"):
            raise Stop(f"{loc}: the theme section has no heading")
        d["theme_section"] = theme
    rows = table_rows(body, "3.")
    head, rows = rows[0], [r for r in rows[2:]]
    cols = {LABELS[h]: i for i, h in enumerate(head) if h in LABELS}
    for loc in locales:
        notes = {}
        for row in rows:
            key = re.match(r"`(\w+)`", row[0]).group(1)
            notes[key] = row[cols[loc]]
        if sorted(notes) != sorted(SCHEMA_KEYS):
            raise Stop(f"{loc}: schema note keys {sorted(notes)}")
        data[loc]["schema_notes"] = notes


EDIT = re.compile(r"(`+) ?(.+?) ?\1 → (`+) ?(.+?) ?\3")


def parse_c(body: str, edits: str, locales: list, data: dict) -> None:
    found = blocks(body)
    lines = edits.replace("\r\n", "\n").split("\n")
    start = lines.index(next(line for line in lines if line.startswith("### 6c.")))
    todo = {}
    for line in lines[start + 1:]:
        if line.startswith("#"):
            break
        m = re.match(r"- \[ \] (\S+) (0\.7\.[01])：(.*)$", line)
        if m:
            pairs = [(e.group(2), e.group(4)) for e in EDIT.finditer(m.group(3))]
            if not pairs:
                raise Stop(f"6c: no edit in {line!r}")
            todo[(LABELS[m.group(1)], m.group(2))] = pairs
    if sorted(todo) != [("en", "0.7.1"), ("ja", "0.7.1"), ("zh-hant", "0.7.0")]:
        raise Stop(f"6c: unexpected edits {sorted(todo)}")
    todo[("ja", "0.7.1")].append(("マニュアル", "ハンドブック"))
    for loc in locales:
        (text,) = take(found, "2.", loc, 1)
        parts = re.split(r"(?m)^(?=## marsdawn )", text)
        got = {re.match(r"## marsdawn (\S+)", part).group(1): part.rstrip("\n") for part in parts if part.strip()}
        if sorted(got) != ["0.6.4", "0.7.0", "0.7.1"]:
            raise Stop(f"C {loc}: versions {sorted(got)}")
        for v in ("0.7.1", "0.7.0"):
            entry_text = entry(got[v], v)
            for old, new in todo.get((loc, v), []):
                if old.endswith("…") and new.endswith("…"):
                    old, new = old[:-1], new[:-1]
                n = entry_text.count(old)
                if n != 1 and not (old == "マニュアル" and n >= 1):
                    raise Stop(f"C {loc} {v}: {old!r} found {n} times")
                entry_text = entry_text.replace(old, new)
            data[loc]["changelog"][v] = entry_text


def build() -> tuple:
    c = SOURCES["comments"]
    fetch(c["approval"])
    fetch(c["approval_c"])
    fetch(c["ja_name"])
    approved = ["en", "zh-hant", "ja"]
    data = {loc: {"changelog": {}} for loc in approved}
    shared = {}
    parse_a(fetch(c["A"]), approved, data)
    parse_b(fetch(c["B"]), approved, data, shared)
    parse_c(fetch(c["C"]), fetch(c["C_edits"]), approved, data)
    for key, pinned in SOURCES.get("i18n", {}).items():
        raise Stop(f"i18n source {key}: no parser yet")
    return data, shared


def render(data: dict, shared: dict) -> str:
    pins = {k: {f: v[f] for f in ("issue", "id", "sha256")} for k, v in SOURCES["comments"].items()}
    return ('"""Generated by scripts/cli254/ingest.py from the pinned comments in sources.json. Do not edit by hand."""\n\n'
            f"SOURCES = {pprint.pformat(pins, width=110, sort_dicts=True)}\n\n"
            f"SHARED = {pprint.pformat(shared, width=110, sort_dicts=True)}\n\n"
            f"DATA = {pprint.pformat(data, width=110, sort_dicts=True)}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    data, shared = build()
    text = render(data, shared)
    target = HERE / "data.py"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("data.py differs from what the pinned comments give", file=sys.stderr)
            return 1
        print("data.py matches the pinned comments")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target.relative_to(HERE.parent.parent)}: {', '.join(sorted(data))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
