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



LOC_LABEL = {"en": "en", "zh-Hant": "zh-hant", "ja": "ja"}


def r1_items(text: str) -> list:
    """Round-1 item lines for en, zh-Hant and ja: '- [ ] **en A（49）**：`...`' (a checked item) or
    '- en（56）：`...`' (a version listed without a box). Returns [(locale, tag, value)] in order; the tag is
    the word after the language ('A', 'description', ...) or ''."""
    out = []
    pat = re.compile(r"^\s*-\s*(?:\[[ x]\]\s*)?(?:\*\*)?(en|zh-Hant|ja)(?:\s+([A-Za-z]+))?\s*(?:（\d+）)?(?:\*\*)?[：:]\s*(.+?)\s*$", re.M)
    for m in pat.finditer(text):
        out.append((LOC_LABEL[m.group(1)], m.group(2) or "", unwrap(m.group(3))))
    return out


def r2_table(body: str, locale: str) -> dict:
    """Round 2's two-column table for a language: {item label without its count: cell text}."""
    heading = {"zh-hans": "zh-Hans", "ko": "ko", "de": "de", "fr": "fr", "es": "es"}[locale]
    return table_rows(section(body, f"### {heading}"))


def by_loc(items: list, tag: str = "") -> dict:
    return {loc: value for loc, t, value in items if t == tag}



def nested(text: str) -> dict:
    """'- [ ] **en**' lines followed by indented '- key：`value`' lines -> {locale: {key: value}}."""
    out, cur = {}, None
    for line in text.split("\n"):
        head = re.match(r"^- \[[ x]\] \*\*(en|zh-Hant|ja)\*\*\s*$", line)
        if head:
            cur = LOC_LABEL[head.group(1)]
            out[cur] = {}
            continue
        item = re.match(r"^\s+- ([^：:`]+)[：:]\s*(.+?)\s*$", line)
        if item and cur:
            out[cur][item.group(1).strip()] = unwrap(item.group(2))
            continue
        bare = re.match(r"^\s+- (`.+`)\s*$", line)
        if bare and cur:
            out[cur].setdefault("_list", []).append(unwrap(bare.group(1)))
        elif re.match(r"^- \[[ x]\]", line) or re.match(r"^#", line):
            cur = None
    return out


def fenced_by_locale(text: str) -> dict:
    """'- [ ] **en**' followed by a fenced block -> {locale: [lines]}."""
    out = {}
    for m in re.finditer(r"^- \[[ x]\] \*\*(en|zh-Hant|ja)\*\*\s*\n```\n(.*?)\n```", text, re.M | re.S):
        out[LOC_LABEL[m.group(1)]] = m.group(2).split("\n")
    return out


def locale_chunk(text: str, name: str) -> str:
    """The text after a bold '**name**' line, up to the next bold line."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == f"**{name}**":
            end = len(lines)
            for j in range(i + 1, len(lines)):
                if re.match(r"^\*\*[^*]+\*\*\s*$", lines[j].strip()):
                    end = j
                    break
            return "\n".join(lines[i + 1:end])
    raise Stop(f"no bold line {name!r}")


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



# ---- #244: titles without "editor", the home description and definition ------------------------

def ingest_244() -> None:
    c1, b1 = comment(244, 1)
    c2, b2 = comment(244, 2)
    # (a) the home page: version B; (b) /features/, (c) /yours/, (d) /vs/macmd-viewer/: version A.
    spec = [("index", "(a)", "### (a)", "B", "title"), ("features", "(b)", "### (b)", "A", "title"),
            ("yours", "(c)", "### (c)", "A", "title"), ("vs/macmd-viewer", "(d)", "### (d)", "A", "title")]
    r2_key = {"index": "(a) 首頁 `/` title／og:title", "features": "(b) `/features/`", "yours": "(c) `/yours/`",
              "vs/macmd-viewer": "(d) `/vs/macmd-viewer/`"}
    for slug, label, heading, version, _ in spec:
        sec = section(b1, heading)
        if version == "B":
            sec = sec[sec.index("版本 B"):]
            got = by_loc(r1_items(sec))
        else:
            got = by_loc(r1_items(sec), "A")
        assert set(got) == set(FIRST), (slug, got)
        for loc in FIRST:
            put(("titles", loc, slug), esc(got[loc]), slot={
                "locale": loc, "page": slug, "field": "title", "source": comment_source(c1, 1, f"{heading} version {version}, {loc}"),
                "item": f"#244{label}", "version": version})
        for loc in MACHINE:
            cell = r2_table(b2, loc)[r2_key[slug]]
            put(("titles", loc, slug), esc(cell), slot={
                "locale": loc, "page": slug, "field": "title", "source": comment_source(c2, 2, f"### {loc} table, {r2_key[slug]}"),
                "item": f"#244{label}", "version": "R2"})
    sec = section(b1, "### (f)")
    items = r1_items(sec)
    for loc in FIRST:
        for tag, key, label in (("description", "description", "(f) description"), ("definition", "definition", "(f) definition")):
            value = by_loc(items, tag)[loc]
            put(("home", loc, key), esc(value), slot={
                "locale": loc, "page": "index", "field": key, "source": comment_source(c1, 1, f"### (f), {loc} {tag}"),
                "item": f"#244{label}", "version": "R1"})
    for loc in MACHINE:
        table = r2_table(b2, loc)
        for key, row, label in (("description", "(f) 首頁 meta description（og:description、llms.txt）", "(f) description"),
                                ("definition", "(f) headline 下的定義句", "(f) definition")):
            put(("home", loc, key), esc(table[row]), slot={
                "locale": loc, "page": "index", "field": key, "source": comment_source(c2, 2, f"### {loc} table, {row}"),
                "item": f"#244{label}", "version": "R2"})
    # the definition sentence is also /native/'s (plan: "/native/ takes #244(f)'s definition")
    for loc in LOCALES:
        SLOTS.append(dict([s for s in SLOTS if s["path"] == ["home", loc, "definition"]][0], page="native", path=["home", loc, "definition"]))



# ---- #246: an invitation line under "Write to us" on /support/ ----------------------------------

def ingest_246() -> None:
    from urllib.parse import unquote, urlsplit, parse_qs
    c1, b1 = comment(246, 1)
    c2, b2 = comment(246, 2)
    sec_a = section(b1, "### (a)")
    sec_a = sec_a[:sec_a.index("**版本 B**")]            # version A only
    para = by_loc(r1_items(sec_a))
    subj = by_loc(r1_items(section(b1, "### (b)")))
    for loc in LOCALES:
        if loc in FIRST:
            text, subject = para[loc], subj[loc]
            src_p, src_s, ver = (comment_source(c1, 1, f"### (a) version A, {loc}"), comment_source(c1, 1, f"### (b), {loc}"), "A")
        else:
            table = r2_table(b2, loc)
            text, subject = table["文案（接在地址段落之後）"], table["mailto 主旨"]
            src_p, src_s, ver = (comment_source(c2, 2, f"### {loc} table, 文案（接在地址段落之後）"),
                                 comment_source(c2, 2, f"### {loc} table, mailto 主旨"), "R2")
        # the paragraph is Markdown; the kit's renderer turns it into HTML. Its mailto subject must be the item's.
        link = re.search(r"\]\((mailto:[^)]+)\)", text)
        assert link, (loc, text)
        decoded = parse_qs(urlsplit(link.group(1)).query)["subject"][0]
        assert decoded == subject, (loc, decoded, subject)
        put(("support", loc, "p_md"), text, slot={"locale": loc, "page": "support", "field": "p", "source": src_p,
                                                  "item": "#246(a)", "version": ver})
        put(("support", loc, "subject"), subject, slot={"locale": loc, "page": "support", "field": "mailto_subject", "source": src_s,
                                                        "item": "#246(b)", "version": ver})



# ---- #242: the /vs/ page, and its short version on the home page --------------------------------

def ingest_242() -> None:
    c1, b1 = comment(242, 1)
    c2, b2 = comment(242, 2)
    a = nested(section(b1, "### (a)"))
    notes = bullets(section(b1, "### (b)(c)"))
    lacks_a = by_loc(r1_items(section(b1, "### (d)")), "A")
    dont = fenced_by_locale(section(b1, "### (e)"))
    short = by_loc(r1_items(section(b1, "### (f)")))
    links = nested(section(b1, "### (g)"))

    def r2_nested(label: str) -> dict:
        """The round-2 correction '- [ ] **label**' with indented '- en：`...`' lines -> {locale: value}."""
        m = re.search(r"^- \[[ x]\] \*\*" + re.escape(label) + r"\*\*[^\n]*\n((?:  - .*\n?)+)", b2, re.M)
        assert m, label
        return {LOC_LABEL[k]: unwrap(v.strip()) for k, v in re.findall(r"^\s+- (en|zh-Hant|ja)[：:]\s*(.+)$", m.group(1), re.M)}
    vscode_cell = r2_nested("VS Code 格")
    lacks_extra = r2_nested("lacks 加的句子")
    dont_vscode = r2_nested("When you don't need 的 VS Code 那條")
    # the bracketed command in the VS Code cell is code, as in the round-1 table and in the other languages' cells
    for loc in vscode_cell:
        vscode_cell[loc] = vscode_cell[loc].replace("code -g file:line", "`code -g file:line`")
    anchor = {"en": "Its PDFs have no page numbers.", "zh-hant": "輸出的 PDF 沒有頁碼。", "ja": "PDF にページ番号は入りません。"}
    joiner = {"en": " ", "zh-hant": "", "ja": ""}

    def src1(where):
        return comment_source(c1, 1, where)

    def src2(where):
        return comment_source(c2, 2, where)

    for loc in LOCALES:
        if loc in FIRST:
            ln = {"en": "en", "zh-hant": "zh-Hant", "ja": "ja"}[loc]
            table = data_tables(locale_chunk(section(b1, "### (b)(c)"), ln))[0]
            fields = {"title": a[loc]["title"], "h1": a[loc]["h1"], "intro": a[loc]["引言"],
                      "note": notes[f"表下註記（{ln}）"], "short": short[loc]}
            where = {"title": src1(f"### (a), {loc} title"), "h1": src1(f"### (a), {loc} h1"), "intro": src1(f"### (a), {loc} 引言"),
                     "note": src1(f"### (b)(c), 表下註記（{ln}）"), "short": src1(f"### (f), {loc}")}
            lacks = lacks_a[loc]
            assert lacks.count(anchor[loc]) == 1, loc
            lacks_full = lacks.replace(anchor[loc], anchor[loc] + joiner[loc] + lacks_extra[loc])
            lacks_src = [src1(f"### (d) version A, {loc}"), src2(f"lacks 加的句子, {loc}, spliced after {anchor[loc]!r}")]
            ver = "R1+R2"
            items = list(dont[loc])
            heading, bullets_ = items[0], [i[2:] if i.startswith("- ") else i for i in items[1:]]
            assert len(bullets_) == 6
            assert "VS Code" in bullets_[0] and "VS Code" in dont_vscode[loc]
            bullets_[0] = dont_vscode[loc]
            dont_src = [src1(f"### (e), {loc} heading")] + [src1(f"### (e), {loc} bullet {i + 1}") for i in range(6)]
            dont_src[1] = src2(f"When you don't need 的 VS Code 那條, {loc}")
            head_row, rows = table[0], [list(r) for r in table[1:]]
            assert len(rows) == 8 and "VS Code" in head_row[2]
            rows[3][2] = vscode_cell[loc]
            cell_src = lambda r, c: src2(f"VS Code 格, {loc}") if (r, c) == (3, 2) else src1(f"### (b)(c) table {ln}, row {r + 1} col {c + 1}")
            l1 = links[loc]["_list"]
        else:
            t2 = r2_table(b2, loc)
            tables = data_tables(section(b2, "### " + {"zh-hans": "zh-Hans"}.get(loc, loc)))
            head_row, rows = tables[1][0], [list(r) for r in tables[1][1:]]
            assert len(rows) == 8
            fields = {"title": t2["title"], "h1": t2["h1"], "intro": t2["引言"], "note": t2["表下註記"], "short": t2["首頁短版"]}
            where = {k: src2(f"### {loc} table, {v}") for k, v in (("title", "title"), ("h1", "h1"), ("intro", "引言"), ("note", "表下註記"), ("short", "首頁短版"))}
            lacks_full = t2["What MarsDawn lacks"]
            lacks_src = [src2(f"### {loc} table, What MarsDawn lacks")]
            ver = "R2"
            heading = t2["When you don't need：標題"]
            bullets_ = [t2[f"When you don't need：第 {i} 條"] for i in range(1, 7)]
            dont_src = [src2(f"### {loc} table, When you don't need：標題")] + [src2(f"### {loc} table, When you don't need：第 {i} 條") for i in range(1, 7)]
            cell_src = lambda r, c: src2(f"### {loc} data table, row {r + 1} col {c + 1}")
            l1 = [t2["比較頁介紹 1"], t2["比較頁介紹 2"]]
        assert len(head_row) == 6 and all(len(r) == 6 for r in rows)
        for key, field, item in (("title", "title", "(a) title"), ("h1", "h1", "(a) h1"), ("intro", "p", "(a) 引言")):
            put(("vs", loc, key), esc(fields[key]) if key == "title" else inline(fields[key]),
                slot={"locale": loc, "page": "vs", "field": field, "source": where[key], "item": f"#242{item}", "version": ver})
        put(("vs", loc, "note"), inline(fields["note"]), slot={"locale": loc, "page": "vs", "field": "p", "source": where["note"],
                                                                "item": "#242(b)(c) 表下註記", "version": ver})
        put(("vs", loc, "lacks"), inline(lacks_full), slot={"locale": loc, "page": "vs", "field": "p", "source": lacks_src,
                                                             "item": "#242(d) What MarsDawn lacks (A)", "version": ver})
        put(("vs", loc, "dont_h"), inline(heading), slot={"locale": loc, "page": "vs", "field": "h2", "source": dont_src[0],
                                                           "item": "#242(e) heading", "version": ver})
        DATA["vs"][loc]["dont"] = []
        for i, b in enumerate(bullets_):
            DATA["vs"][loc]["dont"].append(inline(b))
            SLOTS.append({"locale": loc, "page": "vs", "field": "li", "source": dont_src[i + 1], "item": f"#242(e) bullet {i + 1}",
                          "version": ver, "path": ["vs", loc, "dont", i]})
        DATA["vs"][loc]["links"] = []
        for i, l in enumerate(l1):
            DATA["vs"][loc]["links"].append(inline(l))
            SLOTS.append({"locale": loc, "page": "vs", "field": "li", "source": src1(f"### (g), {loc} item {i + 1}") if loc in FIRST else src2(f"### {loc} table, 比較頁介紹 {i + 1}"),
                          "item": f"#242(g) item {i + 1}", "version": ver, "path": ["vs", loc, "links", i]})
        DATA["vs"][loc]["head"] = [inline(c) for c in head_row]
        for c, cell in enumerate(head_row):
            if cell:
                SLOTS.append({"locale": loc, "page": "vs", "field": "th", "source": src1(f"### (b)(c) table, header col {c + 1}") if loc in FIRST else src2(f"### {loc} data table, header col {c + 1}"),
                              "item": f"#242(b)(c) header {c + 1}", "version": ver, "path": ["vs", loc, "head", c]})
        DATA["vs"][loc]["rows"] = []
        for r, row in enumerate(rows):
            DATA["vs"][loc]["rows"].append([inline(c) for c in row])
            for c, cell in enumerate(row):
                SLOTS.append({"locale": loc, "page": "vs", "field": "th" if c == 0 else "td", "source": cell_src(r, c),
                              "item": f"#242(b)(c) row {r + 1} col {c + 1}", "version": ver, "path": ["vs", loc, "rows", r, c]})
        # the home page's short version
        put(("home", loc, "vs_short"), inline(fields["short"]), slot={"locale": loc, "page": "index", "field": "p", "source": where["short"],
                                                                      "item": "#242(f)", "version": ver})



# ---- #240: "Your documents stay on your Mac": three layers, and the privacy questions ----------

def ingest_240() -> None:
    c1, b1 = comment(240, 1)
    c2, b2 = comment(240, 2)
    title = by_loc(r1_items(section(b1, "### (a)")), "A")
    sec_b = section(b1, "### (b)")
    parts = re.split(r"\*\*第[一二三]層\*\*", sec_b)[1:]
    assert len(parts) == 3
    layer = {i: by_loc(r1_items(parts[i])) for i in range(3)}
    layer2_r2 = by_loc(r1_items(section(b2, "## 結論")))                # the corrected second layer: round 2 text under 結論
    faq_r1 = section(b1, "### (c)")
    heads = {m.group(1): m.group(2).strip() for m in re.finditer(r"^\*\*([QP]\d)\s+(.+?)\*\*", faq_r1, re.M)}
    chunks = re.split(r"^\*\*[QP]\d\b.*$", faq_r1, flags=re.M)[1:]
    keys = [m.group(1) for m in re.finditer(r"^\*\*([QP]\d)\b", faq_r1, re.M)]
    answers_r1 = {k: by_loc(r1_items(c)) for k, c in zip(keys, chunks) if k in ("Q1", "P1", "P2", "P3", "P4")}
    q1_heading = heads["Q1"]
    q1_heading = re.sub(r"（.*$", "", q1_heading).strip()
    # round 1's link row: one sentence per language, with the anchor of each place from its anchor table
    sec_d = section(b1, "### (d)")
    bar = by_loc(r1_items(sec_d.split("錨點對應")[0]))
    anchors = {"t1": "what-stays-on-your-mac", "t2": "when-marsdawn-uses-the-internet", "t3": "when-marsdawn-uses-the-internet",
               "P1": "when-marsdawn-uses-the-internet", "P3": "when-marsdawn-uses-the-internet", "P4": "the-website"}
    seo = ns_seo()
    for loc in LOCALES:
        if loc in FIRST:
            ttl = title[loc]
            layers = [layer[0][loc], layer2_r2[loc], layer[2][loc]]
            lsrc = [comment_source(c1, 1, f"### (b) 第一層, {loc}"), comment_source(c2, 2, f"## 結論 (corrected second layer), {loc}"),
                    comment_source(c1, 1, f"### (b) 第三層, {loc}")]
            tsrc = comment_source(c1, 1, f"### (a) A, {loc}")
            ver = "R1+R2"

            def link(anchor, loc=loc):
                return re.sub(r"#what-stays-on-your-mac", "#" + anchor, bar[loc])
            more = [link(anchors["t1"]), link(anchors["t2"]), link(anchors["t3"])]
            msrc = [comment_source(c1, 1, f"### (d) link row + anchor table, {loc}, {k}") for k in ("tier 1", "tier 2", "tier 3")]
            items = {}
            q1_q = seo[loc]["home_faq"][0][0] if loc != "en" else q1_heading
            items["Q1"] = (q1_q, answers_r1["Q1"][loc], None, comment_source(c1, 1, f"### (c) Q1, {loc}"), None)
            if loc == "en":
                for k in ("P1", "P2", "P3", "P4"):
                    q = re.sub(r"（.*$", "", heads[k]).strip()
                    mk = None if k == "P2" else link(anchors[k])
                    items[k] = (q, answers_r1[k][loc], mk, comment_source(c1, 1, f"### (c) {k}, en"),
                                comment_source(c1, 1, f"### (d) link row + anchor table, en, {k}") if mk else None)
        else:
            t = r2_table(b2, loc)
            ttl = t["標題"]
            layers = [t["第一層"], t["第二層"], t["第三層"]]
            lsrc = [comment_source(c2, 2, f"### {loc} table, {k}") for k in ("第一層", "第二層", "第三層")]
            tsrc = comment_source(c2, 2, f"### {loc} table, 標題")
            ver = "R2"
            more = [t["連結列（第一層）"], t["連結列（第二層）"], t["連結列（第三層）"]]
            msrc = [comment_source(c2, 2, f"### {loc} table, 連結列（{k}）") for k in ("第一層", "第二層", "第三層")]
            items = {"Q1": (t["Q1 問"], t["Q1 答"], None, comment_source(c2, 2, f"### {loc} table, Q1 問/答"), None)}
            for k in ("P1", "P2", "P3", "P4"):
                items[k] = (t[f"{k} 問"], t[f"{k} 答"], t[f"連結列（{k}）"], comment_source(c2, 2, f"### {loc} table, {k} 問/答"),
                            comment_source(c2, 2, f"### {loc} table, 連結列（{k}）"))
        put(("stays", loc, "h"), esc(ttl), slot={"locale": loc, "page": "index", "field": "h2", "source": tsrc, "item": "#240(a)", "version": "A" if loc in FIRST else "R2"})
        DATA["stays"][loc]["layers"] = []
        DATA["stays"][loc]["more"] = []
        for i in range(3):
            DATA["stays"][loc]["layers"].append(inline(layers[i]))
            SLOTS.append({"locale": loc, "page": "index", "field": "p", "source": lsrc[i], "item": f"#240(b) layer {i + 1}",
                          "version": ver, "path": ["stays", loc, "layers", i]})
            DATA["stays"][loc]["more"].append(inline(more[i]))
            SLOTS.append({"locale": loc, "page": "index", "field": "p", "source": msrc[i], "item": f"#240(d) link row, layer {i + 1}",
                          "version": ver, "path": ["stays", loc, "more", i]})
        DATA["stays"][loc]["faq"] = {}
        for k, (q, a, mk, asrc, msrc_) in items.items():
            DATA["stays"][loc]["faq"][k] = [esc(q), esc(a), inline(mk) if mk else None]
            SLOTS.append({"locale": loc, "page": "index", "field": "faq_q", "source": asrc, "item": f"#240(c) {k} question", "version": ver,
                          "path": ["stays", loc, "faq", k, 0]})
            SLOTS.append({"locale": loc, "page": "index", "field": "faq_a", "source": asrc, "item": f"#240(c) {k} answer", "version": ver,
                          "path": ["stays", loc, "faq", k, 1]})
            if mk:
                SLOTS.append({"locale": loc, "page": "index", "field": "p", "source": msrc_, "item": f"#240(d) link row, {k}", "version": ver,
                              "path": ["stays", loc, "faq", k, 2]})


def ns_seo() -> dict:
    ns = {}
    exec(compile(seo_source(), "seo_copy.py", "exec"), ns)
    return ns["COPY"]


# ---- main -------------------------------------------------------------------------------------

INGESTERS = {189: ingest_189, 244: ingest_244, 246: ingest_246, 242: ingest_242, 240: ingest_240}


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
