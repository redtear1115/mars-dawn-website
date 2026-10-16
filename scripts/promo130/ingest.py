#!/usr/bin/env python3
"""Ingestion for the promo-130 content bundle (website milestone 1.3.0).

Every string the bundle puts on the site comes from a pinned source and is carried here by program,
never typed:

- a Grok comment on a website issue (#240 to #246, and #189's two review comments), fetched by id
  with `gh api` and held to the sha256 and `updated_at` recorded in sources.json, or
- scripts/seo_copy.py at commit 8de3664934e02a5bd2e1e4d6de8a7f0907b95fe6 (#189), read from the git
  object and held to its recorded sha256.

A source whose hash or `updated_at` differs from the pinned one stops the run (exit 2). The only
transformations applied are the allowed ones: Markdown inline syntax to HTML ([text](url) -> <a>,
`x` -> <code>, **x** -> <strong>, *x* -> <em>, \\| -> |), the reply's own framing removed (check boxes,
language labels, the code span wrapped around a whole item, character counts), commands and file
names in <code>, and, for #189's zh-Hans strings only, the owner's zh-Hans word map (agent -> 代理).

Outputs: scripts/promo130/data.py (the strings the build reads) and scripts/promo130/slots.json (one
row per shipped string: page x field x locale -> source, item label, version label).

    python3 -B scripts/promo130/ingest.py            # fetch, verify, write
    python3 -B scripts/promo130/ingest.py --through 189   # only the issues up to this one
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
ROOT = HERE.parent.parent
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
REPO = "redtear1115/mars-dawn-website"
SEO_COMMIT = "8de3664934e02a5bd2e1e4d6de8a7f0907b95fe6"
SEO_SHA256 = "abde71d1cd7f45fbc6bcb65f3bdca2955f1fa8f2c02148aecab6017cc6853ec6"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
FIRST = ["en", "zh-hant", "ja"]            # the first-round languages
MACHINE = ["zh-hans", "ko", "de", "fr", "es"]   # Grok's needs-i18n round

ORDER = [189, 244, 246, 242, 240, 241, 245, 243]


class Stop(SystemExit):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


_cache = {}


def comment(issue: int, round_: int) -> tuple:
    """(id, body) of the issue's pinned comment: round 1 or 2 (189: the two review comments)."""
    pinned = SOURCES["issues"][str(issue)][round_ - 1]
    cid = pinned["id"]
    if cid not in _cache:
        out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{cid}"], capture_output=True, text=True)
        if out.returncode:
            raise Stop(f"gh api failed for comment {cid}: {out.stderr.strip()}")
        got = json.loads(out.stdout)
        digest = sha256(got["body"])
        if digest != pinned["sha256"] or got["updated_at"] != pinned["updated_at"]:
            raise Stop(f"comment {cid} (#{issue}) differs from the pinned source: sha256 {digest} vs {pinned['sha256']}, "
                       f"updated_at {got['updated_at']} vs {pinned['updated_at']}")
        _cache[cid] = got["body"]
        print(f"verified comment {cid} (#{issue} round {round_}): sha256 {digest[:12]} updated_at {got['updated_at']}")
    return cid, _cache[cid]


def seo_source() -> str:
    out = subprocess.run(["git", "-C", str(ROOT), "show", f"{SEO_COMMIT}:scripts/seo_copy.py"], capture_output=True)
    if out.returncode:
        raise Stop(f"git show {SEO_COMMIT}:scripts/seo_copy.py failed: {out.stderr.decode()[:200]}")
    text = out.stdout.decode("utf-8")
    if sha256(text) != SEO_SHA256:
        raise Stop(f"seo_copy.py@{SEO_COMMIT[:7]} sha256 {sha256(text)} differs from the pinned {SEO_SHA256}")
    print(f"verified scripts/seo_copy.py@{SEO_COMMIT[:7]}: sha256 {SEO_SHA256[:12]}")
    return text


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


def strip_count(text: str) -> str:
    """Grok's trailing character count in a label: 'en A（49）' -> 'en A'."""
    return re.sub(r"[（(]\d+[）)]\s*$", "", text).strip()


# ---- readers for Grok's reply formats ---------------------------------------------------------

def section(body: str, heading: str) -> str:
    """The text under a heading line that starts with `heading`, up to the next heading of the same or
    a higher level."""
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


def bullets(text: str) -> dict:
    """'- [ ] **label**：`value`' lines -> {label: value}. The label loses its count; the value loses
    the code span wrapped around the whole item."""
    out = {}
    for m in re.finditer(r"^\s*- \[[ x]\] \*\*(.+?)\*\*[：:]\s*(.+)$", text, re.M):
        label, value = strip_count(m.group(1)), m.group(2).strip()
        value = unwrap(value)
        out[label] = value
    return out


def unwrap(value: str) -> str:
    """Remove the one pair of backticks Grok wraps around a whole item, and the versions note after it."""
    m = re.match(r"^`((?:[^`]|`(?!$))*?)`(?:（[^）]*）)?$", value)
    if m:
        return m.group(1)
    return value


def table_rows(text: str) -> dict:
    """The first two-column table in the text: {first cell: second cell}."""
    out = {}
    for line in text.split("\n"):
        if not line.startswith("|"):
            if out:
                break
            continue
        cells = split_row(line)
        if len(cells) < 2 or set(cells[0]) <= set("-: ") or cells[0] in ("項目",):
            continue
        out[strip_count(cells[0])] = cells[1]
    return out


def split_row(line: str) -> list:
    line = line.strip()
    assert line.startswith("|") and line.endswith("|"), line
    cells, cur, i = [], "", 1
    body = line[1:-1]
    while i <= len(body):
        ch = body[i - 1] if i - 1 < len(body) else ""
        if ch == "\\" and i < len(body) and body[i] == "|":
            cur += "\\|"
            i += 2
            continue
        if ch == "|":
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def data_tables(text: str) -> list:
    """Every pipe table in the text as a list of rows (cells), separator rows dropped."""
    tables, cur = [], []
    for line in text.split("\n") + [""]:
        if line.startswith("|"):
            cells = split_row(line)
            if not all(set(c) <= set("-: ") for c in cells):
                cur.append(cells)
        elif cur:
            tables.append(cur)
            cur = []
    return tables


# ---- collecting data and slots ----------------------------------------------------------------

DATA = {}
SLOTS = []


def put(path: tuple, value, *, slot: dict) -> None:
    """DATA[path...] = value; the slot row records where it ships and where it came from. A slot with
    `path` None only records a row (for a value kept under a parent path)."""
    node = DATA
    for part in path[:-1]:
        node = node.setdefault(part, {})
    node[path[-1]] = value
    SLOTS.append(dict(slot, path=list(path)))


def comment_source(cid: int, round_: int, locator: str) -> dict:
    return {"comment": cid, "round": f"R{round_}", "locator": locator}


# ---- #189: scripts/seo_copy.py@8de3664 --------------------------------------------------------

def ingest_189() -> None:
    cid2 = SOURCES["issues"]["240"][1]["id"]
    text = seo_source()
    ns = {}
    exec(compile(text, "seo_copy.py", "exec"), ns)
    copy = ns["COPY"]
    # #240 round 2 corrects one zh-Hans word in Q4; the owner's zh-Hans map is agent -> 代理.
    comment(240, 2)
    zh_q4_old, zh_q4_new = "或任何能执行 shell 命令的 agent", "或任何能执行 shell 命令的代理"
    for loc in LOCALES:
        c = copy[loc]
        src = {"file": f"scripts/seo_copy.py@{SEO_COMMIT[:7]}", "sha256": SEO_SHA256}

        def plain(key, value, page, field, item, subst=None):
            put(("seo", loc, key) if not isinstance(key, tuple) else ("seo", loc) + key, esc(value),
                slot={"locale": loc, "page": page, "field": field, "source": dict(src, **({"subst": subst} if subst else {})),
                      "item": item, "version": "#189"})
        plain("ql_title", c["ql_title"], "quicklook", "title", "ql_title")
        plain("ql_desc", c["ql_desc"], "quicklook", "description", "ql_desc")
        plain("ql_h1", c["ql_h1"], "quicklook", "h1", "ql_h1")
        plain("ql_lead", c["ql_lead"], "quicklook", "p", "ql_lead")
        plain("ql_shows_h", c["ql_shows_h"], "quicklook", "h2", "ql_shows_h")
        DATA["seo"][loc]["ql_shows"] = []
        for i, item in enumerate(c["ql_shows"]):
            DATA["seo"][loc]["ql_shows"].append(esc(item))
            SLOTS.append({"locale": loc, "page": "quicklook", "field": "li", "source": src, "item": f"ql_shows[{i}]",
                          "version": "#189", "path": ["seo", loc, "ql_shows", i]})
        plain("ql_how_name", c["ql_how_name"], "quicklook", "h2", "ql_how_name")
        DATA["seo"][loc]["ql_steps"] = []
        for i, (name, step) in enumerate(c["ql_steps"]):
            DATA["seo"][loc]["ql_steps"].append([esc(name), esc(step)])
            for j, (field, kind) in enumerate((("strong", "name"), ("li-text", "text"))):
                SLOTS.append({"locale": loc, "page": "quicklook", "field": field, "source": src, "item": f"ql_steps[{i}].{kind}",
                              "version": "#189", "path": ["seo", loc, "ql_steps", i, j]})
        plain("ql_trial_h", c["ql_trial_h"], "quicklook", "h2", "ql_trial_h")
        plain("ql_pay_link_text", c["ql_pay_link_text"], "quicklook", "a", "ql_pay_link_text")
        plain("ql_trial_p", c["ql_trial_p"], "quicklook", "p", "ql_trial_p")
        plain("ql_next_h", c["ql_next_h"], "quicklook", "h2", "ql_next_h")
        plain("ql_link", c["ql_link"], "native", "a", "ql_link")
        plain("ui", c["ui"], "quicklook", "breadcrumb", "ui")
        plain("faq_h", c["faq_h"], "quicklook", "h2", "faq_h")
        for key, page, items in (("ql_faq", "quicklook", c["ql_faq"]), ("pay_faq", "pay-once", c["pay_faq"]),
                                 ("home_faq", "index", c["home_faq"][1:4])):
            DATA["seo"][loc][key] = []
            base = 1 if key == "home_faq" else 0   # the home FAQ keeps #189's Q2 to Q4; Q1 and Q5 are superseded
            for i, (q, a) in enumerate(items):
                subst = None
                if loc == "zh-hans" and key == "home_faq" and i + base == 3:
                    assert a.count(zh_q4_old) == 1, "zh-Hans Q4 no longer holds the string #240 round 2 corrects"
                    a = a.replace(zh_q4_old, zh_q4_new)
                    subst = {"old": zh_q4_old, "new": zh_q4_new, "by": f"comment {cid2} (R2) and the owner's zh-Hans map"}
                DATA["seo"][loc][key].append([esc(q), esc(a)])
                for j, (field, kind) in enumerate((("faq_q", "q"), ("faq_a", "a"))):
                    row = {"locale": loc, "page": page, "field": field, "source": dict(src, **({"subst": subst} if subst and j == 1 else {})),
                           "item": f"{key}[{i + base}].{kind}", "version": "#189", "path": ["seo", loc, key, i, j]}
                    SLOTS.append(row)
    # the zh-Hans map is the only change #189's strings take: nothing else says 'agent'
    zh = json.dumps(DATA["seo"]["zh-hans"], ensure_ascii=False)
    assert not re.search("agent", zh, re.I), "zh-Hans seo strings still say agent"


# ---- main -------------------------------------------------------------------------------------

INGESTERS = {189: ingest_189}


def write() -> None:
    body = pprint.pformat(DATA, width=150, sort_dicts=False)
    (HERE / "data.py").write_text(
        '"""The strings the promo-130 bundle puts on the site. Generated by scripts/promo130/ingest.py from the\n'
        'pinned sources in sources.json; do not edit by hand (a hand edit is caught by the A2 comparison)."""\n\n'
        f"DATA = {body}\n", encoding="utf-8")
    (HERE / "slots.json").write_text(json.dumps({"sources": SOURCES, "slots": SLOTS}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    through = ORDER[-1]
    if "--through" in sys.argv:
        through = int(sys.argv[sys.argv.index("--through") + 1])
    for issue in ORDER[:ORDER.index(through) + 1]:
        INGESTERS[issue]()
    write()
    print(f"wrote {len(SLOTS)} slots")


if __name__ == "__main__":
    main()
