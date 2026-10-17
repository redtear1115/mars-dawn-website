#!/usr/bin/env python3
"""Ingestion for /best-markdown-viewer-mac/ (website #228, milestone 1.3.0).

Every string the page carries comes from a pinned Grok/owner comment on issue #228 and is carried here
by program, never typed. The pins (id, created_at, updated_at, sha256, chars) are in sources.json; a
comment whose sha256 or updated_at differs stops the run (exit 2).

- C1 6235379596: en, zh-Hant and ja (`### en` ...).
- C2 6235458623: the Typora row of each of those three (live reload -> not documented) and the anchor
  tables (app slugs, column ids).
- C4 6237326931: zh-Hans, ko, de, fr and es (`### zh-Hans` ...), the Typora and MarkEdit decisions
  already applied.
- C3 6235638140: the owner's decision record, provenance only (nothing is read from it).

The only transformations are the allowed ones: Markdown inline syntax to HTML ([text](url) -> <a>,
`x` -> <code>, **x** -> <strong>, *x* -> <em>, \\| -> |), HTML escaping, and removing Grok's framing
(code fences, the "(35)" character counts after a label). Non-breaking spaces in the French copy stay
as delivered. The Typora row of en, zh-Hant and ja is replaced by C2's row after asserting that the
original exists once and differs from it only in the live-reload cell.

Outputs: scripts/best228/data.py (what the build reads) and scripts/best228/slots.json (one row per
shipped string: locale x field -> source).

    python3 -I -B scripts/best228/ingest.py --record   # first time only: write sources.json from the live comments
    python3 -I -B scripts/best228/ingest.py            # fetch, verify, write data.py and slots.json
    python3 -I -B scripts/best228/ingest.py --check    # fetch, verify, fail if data.py or slots.json differ
Exit codes: 0 ok, 1 --check differs or a parse assertion failed, 2 a pinned source differs.
"""
import hashlib
import html
import json
import pprint
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "redtear1115/mars-dawn-website"
PINNED = {"C1": 6235379596, "C2": 6235458623, "C3": 6235638140, "C4": 6237326931}
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
FIRST = {"en": "en", "zh-hant": "zh-Hant", "ja": "ja"}     # C1 (+ C2's Typora row)
SECOND = {"zh-hans": "zh-Hans", "ko": "ko", "de": "de", "fr": "fr", "es": "es"}   # C4
N_APPS, N_COLS = 8, 8


class Stop(SystemExit):
    def __init__(self, message, code=2):
        print(message, file=sys.stderr)
        super().__init__(code)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_one(cid: int) -> dict:
    out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{cid}"], capture_output=True, text=True)
    if out.returncode:
        raise Stop(f"gh api failed for comment {cid}: {out.stderr.strip()}", 1)
    return json.loads(out.stdout)


def record() -> int:
    path = HERE / "sources.json"
    if path.exists():
        raise Stop("sources.json exists: a pin is never re-recorded by this script", 1)
    pins = {}
    for name, cid in PINNED.items():
        got = fetch_one(cid)
        pins[name] = {"id": cid, "issue": 228, "created_at": got["created_at"], "updated_at": got["updated_at"],
                      "sha256": sha256(got["body"]), "chars": len(got["body"])}
    path.write_text(json.dumps({"issue": 228, "comments": pins}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("recorded", {k: v["sha256"][:12] for k, v in pins.items()})
    return 0


def load_sources() -> dict:
    return json.loads((HERE / "sources.json").read_text(encoding="utf-8"))["comments"]


def fetch(sources: dict) -> dict:
    bodies = {}
    for name, pin in sources.items():
        got = fetch_one(pin["id"])
        digest = sha256(got["body"])
        if digest != pin["sha256"] or got["updated_at"] != pin["updated_at"]:
            raise Stop(f"comment {pin['id']} ({name}) differs from the pinned source: sha256 {digest} vs {pin['sha256']}, "
                       f"updated_at {got['updated_at']} vs {pin['updated_at']}")
        bodies[name] = got["body"]
        print(f"verified comment {pin['id']} ({name}): sha256 {digest[:12]} updated_at {got['updated_at']}")
    return bodies


# ---- the allowed transformations --------------------------------------------------------------

def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline(text: str) -> str:
    """Markdown inline syntax to HTML; everything else is HTML-escaped and otherwise untouched."""
    text = text.replace("\\|", "|")
    out, pos = [], 0
    token = re.compile(r"\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*|(?<![\w*])\*([^*\n]+)\*(?![\w*])")
    for m in token.finditer(text):
        out.append(esc(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f'<a href="{html.escape(m.group(2), quote=True)}">{esc(m.group(1))}</a>')
        elif m.group(3) is not None:
            out.append(f"<code>{esc(m.group(3))}</code>")
        elif m.group(4) is not None:
            out.append(f"<strong>{esc(m.group(4))}</strong>")
        else:
            out.append(f"<em>{esc(m.group(5))}</em>")
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def plain_line(text: str) -> str:
    """A title or meta description: the fenced line itself, unescaped (the build escapes it)."""
    return text.strip()


# ---- readers -----------------------------------------------------------------------------------

def need(cond, message):
    if not cond:
        raise Stop("parse: " + message, 1)


def locale_block(body: str, heading: str) -> str:
    m = re.search(rf"^### {re.escape(heading)}\n(.*?)(?=^### |^## |\Z)", body, re.M | re.S)
    need(m, f"no '### {heading}' block")
    return m.group(1)


def fenced_after(block: str, label: str) -> str:
    m = re.search(rf"^\*\*{re.escape(label)}[^\n]*\*\*[^\n]*\n```\n(.*?)\n```", block, re.M | re.S)
    need(m, f"no fenced value after {label!r}")
    return m.group(1)


def split_row(line: str) -> list:
    line = line.strip()
    need(line.startswith("|") and line.endswith("|"), f"table row {line!r}")
    return [c.strip() for c in line[1:-1].split("|")]


def parse_locale(block: str) -> dict:
    title = fenced_after(block, "title / og:title / twitter:title")
    desc = fenced_after(block, "meta description")
    h1 = fenced_after(block, "h1")
    need(title == h1, "title differs from h1")
    after = block[block.index("```", block.index("**h1**") + 10) + 3:]       # after the h1 fence
    lines = after.strip("\n").split("\n")
    if "---" in lines:                                          # the separator Grok puts between locales
        lines = lines[:lines.index("---")]
    # bold-only lines in order: intro label, eight apps, comparison, not-for, FAQ
    bold = [i for i, l in enumerate(lines) if re.fullmatch(r"\*\*[^*]+\*\*", l)]
    need(len(bold) == 1 + N_APPS + 3, f"{len(bold)} bold labels, want {1 + N_APPS + 3}")
    def label(i): return lines[bold[i]][2:-2]
    def region(i): return [l for l in lines[bold[i] + 1:bold[i + 1] if i + 1 < len(bold) else len(lines)] if l.strip()]
    intro = region(0)
    need(len(intro) == 1, "intro is not one paragraph")
    apps = []
    for i in range(1, 1 + N_APPS):
        r = region(i)
        need(len(r) == 4 and not r[0].startswith("- ") and all(l.startswith("- ") for l in r[1:]), f"app {label(i)!r}: want a paragraph and three bullets")
        apps.append({"name": label(i), "para": r[0], "bullets": [l[2:] for l in r[1:]]})
    cmp_r = region(1 + N_APPS)
    need(all(l.startswith("|") for l in cmp_r), "comparison region is not a table")
    rows = [split_row(l) for l in cmp_r if not set(l.replace("|", "").strip()) <= set("-: ")]
    need(len(rows) == 1 + N_APPS and all(len(r) == 1 + N_COLS for r in rows), "table is not 1 head + 8 rows x 9 cells")
    notfor = region(2 + N_APPS)
    need(len(notfor) == 4 and all(l.startswith("- ") for l in notfor), "not-for is not four bullets")
    fr = region(3 + N_APPS)
    need(len(fr) == 8, f"FAQ region has {len(fr)} lines, want 4 Q + 4 A")
    faq = []
    for q, a in zip(fr[0::2], fr[1::2]):
        need(re.fullmatch(r"\*[^*].*[^*]\*", q), f"FAQ question {q!r}")
        faq.append((q[1:-1], a))
    return {"title": title, "description": desc, "h1": h1, "intro": intro[0], "apps": apps,
            "cmp_h": label(1 + N_APPS), "head": rows[0], "rows": rows[1:],
            "notfor_h": label(2 + N_APPS), "notfor": [l[2:] for l in notfor],
            "faq_h": label(3 + N_APPS), "faq": faq}


def parse_anchors(c2: str) -> tuple:
    """(slugs, [(col id, {locale: label})]) from C2's two anchor tables."""
    slugs, cols = [], []
    for line in c2.split("\n"):
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if len(cells) == 3 and re.fullmatch(r"`#cmp-[a-z0-9-]+`", cells[2]):
            sec, row = cells[1].strip("`"), cells[2].strip("`")
            need(sec.startswith("#") and row == "#cmp-" + sec[1:], f"anchor row {cells}")
            slugs.append((cells[0], sec[1:]))
        elif len(cells) == 5 and re.fullmatch(r"`#col-[a-z0-9-]+`", cells[4]):
            cols.append((cells[4].strip("`")[5:], {"en": cells[1], "zh-hant": cells[2], "ja": cells[3]}))
    need(len(slugs) == N_APPS and len(cols) == N_COLS, f"C2 anchors: {len(slugs)} apps, {len(cols)} columns")
    return slugs, cols


def typora_rows(c2: str) -> dict:
    """C2's replacement Typora row per first-round locale, from the fences in its section 1."""
    sec = c2[c2.index("### 1."):c2.index("### 2.")]
    out = {}
    for loc, heading in FIRST.items():
        m = re.search(rf"- \[ \] {re.escape(heading)}\n```\n(\| Typora [^\n]*)\n```", sec)
        need(m, f"C2 has no Typora row for {heading}")
        out[loc] = split_row(m.group(1))
    return out


def build(bodies: dict) -> tuple:
    c1, c2, c4 = bodies["C1"], bodies["C2"], bodies["C4"]
    slugs, cols = parse_anchors(c2)
    new_typora = typora_rows(c2)
    src = {}
    data = {}
    for loc in LOCALES:
        if loc in FIRST:
            data[loc] = parse_locale(locale_block(c1, FIRST[loc])); src[loc] = "C1"
        else:
            data[loc] = parse_locale(locale_block(c4, SECOND[loc])); src[loc] = "C4"
    replaced = {}
    for loc in LOCALES:
        d = data[loc]
        names = [r[0] for r in d["rows"]]
        # app order: the table's rows, the section headings and C2's slugs agree (en names are the brand names)
        for i, ((c2name, _), row_name, app) in enumerate(zip(slugs, names, d["apps"])):
            need(row_name.startswith(c2name) and c2name.lower().replace(" ", "") in app["name"].lower().replace("-", "").replace(" ", ""),
                 f"{loc}: app {i} is {row_name!r}/{app['name']!r}, C2 says {c2name!r}")
        if loc in FIRST:
            need(d["head"][1:] == [c[1][loc] for c in cols], f"{loc}: column labels differ from C2's")
            ti = names.index("Typora"); old = d["rows"][ti]; new = new_typora[loc]
            need(sum(1 for n in names if n == "Typora") == 1 and len(new) == len(old), f"{loc}: Typora row shape")
            diff = [j for j in range(len(old)) if old[j] != new[j]]
            need(diff == [5] and old[5] != new[5], f"{loc}: C2's Typora row differs from C1's in {diff}, want only the live-reload cell [5]")
            d["rows"][ti] = new; replaced[loc] = (ti, 5)
        else:
            ti = names.index("Typora")
            doc = d["rows"][0][6]                                  # MacDown 3000's CLI-at-line cell: the locale's "not documented"
            need(d["rows"][ti][5] == doc and d["rows"][ti][6] == doc, f"{loc}: Typora live reload {d['rows'][ti][5]!r} is not the locale's not-documented wording {doc!r}")
        mi = names.index("MarkEdit"); native = d["rows"][0][8]
        need(d["rows"][mi][8].startswith(native) and re.search(r"web view|Web-View|웹 뷰|Webビュー", d["rows"][mi][8], re.I),
             f"{loc}: MarkEdit build cell {d['rows'][mi][8]!r} is not the native (web view) wording")
    out = {}
    slots = []
    for loc in LOCALES:
        d = data[loc]
        def slot(field, text, html_ready, source=None):
            slots.append({"locale": loc, "field": field, "source": source or src[loc], "text": text, "html": html_ready})
        slot("title", d["title"], False); slot("description", d["description"], False); slot("h1", d["h1"], False)
        e = {"title": plain_line(d["title"]), "description": plain_line(d["description"]), "h1": d["h1"], "intro": inline(d["intro"]),
             "apps": [], "head": [], "rows": []}
        slot("intro", e["intro"], True)
        for i, app in enumerate(d["apps"]):
            slug = slugs[i][1]
            ea = {"slug": slug, "name": inline(app["name"]), "para": inline(app["para"]), "bullets": [inline(b) for b in app["bullets"]]}
            slot(f"app.{slug}.name", ea["name"], True); slot(f"app.{slug}.para", ea["para"], True)
            for k, b in enumerate(ea["bullets"]):
                slot(f"app.{slug}.bullet{k + 1}", b, True)
            e["apps"].append(ea)
        e["cmp_h"] = inline(d["cmp_h"]); slot("comparison.h", e["cmp_h"], True)
        for j, cell in enumerate(d["head"]):
            e["head"].append(inline(cell)); slot(f"comparison.head{j}", e["head"][-1], True)
        e["cols"] = [c[0] for c in cols]
        for i, row in enumerate(d["rows"]):
            cells = []
            for j, cell in enumerate(row):
                cells.append(inline(cell))
                via = "C2" if replaced.get(loc) == (i, j) else None
                slot(f"comparison.{slugs[i][1]}.c{j}", cells[-1], True, via)
            e["rows"].append(cells)
        e["notfor_h"] = inline(d["notfor_h"]); slot("notfor.h", e["notfor_h"], True)
        e["notfor"] = [inline(x) for x in d["notfor"]]
        for k, x in enumerate(e["notfor"]):
            slot(f"notfor.{k + 1}", x, True)
        e["faq_h"] = inline(d["faq_h"]); slot("faq.h", e["faq_h"], True)
        e["faq"] = [(inline(q), inline(a)) for q, a in d["faq"]]
        for k, (q, a) in enumerate(e["faq"]):
            slot(f"faq.q{k + 1}", q, True); slot(f"faq.a{k + 1}", a, True)
        out[loc] = e
    out["slugs"] = [s[1] for s in slugs]
    return out, slots


HEADER = '''"""The strings /best-markdown-viewer-mac/ puts on the site (website #228). Generated by
scripts/best228/ingest.py from the pinned comments in sources.json; do not edit by hand (`ingest.py
--check` fails on a hand edit). HTML-ready text except title and description, which the build escapes."""

DATA = '''


def render(data: dict, slots: list, sources: dict) -> tuple:
    return (HEADER + pprint.pformat(data, width=140, sort_dicts=False) + "\n",
            json.dumps({"sources": sources, "slots": slots}, ensure_ascii=False, indent=1) + "\n")


def main() -> int:
    if "--record" in sys.argv:
        return record()
    sources = load_sources()
    bodies = fetch(sources)
    data, slots = build(bodies)
    py, js = render(data, slots, sources)
    if "--check" in sys.argv:
        ok = (HERE / "data.py").read_text(encoding="utf-8") == py and (HERE / "slots.json").read_text(encoding="utf-8") == js
        print("best228 --check:", "data.py and slots.json match the pinned sources" if ok else "DIFFER from the pinned sources")
        return 0 if ok else 1
    (HERE / "data.py").write_text(py, encoding="utf-8")
    (HERE / "slots.json").write_text(js, encoding="utf-8")
    print(f"wrote {len(slots)} slots")
    return 0


if __name__ == "__main__":
    sys.exit(main())
