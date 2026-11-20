#!/usr/bin/env python3
"""Checks that the built /zh-hant/best-markdown-viewer-mac/ carries Aria's #336 copy, and says where it differs.

Usage:
    python3 scripts/check_copy336.py [--root public]
    python3 scripts/check_copy336.py --self-test

scripts/copy336/approved.md is Aria's comment on #336 (pinned in sources.json). This reads it, and the built
public/zh-hant/best-markdown-viewer-mac/index.html and index.md, and fails unless the page holds, in its place:

  1 verbatim      every line of Aria's fenced copy, except the ones REPLACED and REMOVED (opening, scenarios, the two new tools, not-for list, FAQ),
                  title, h1 and description, as the text of one <h1>, <h2>, <h3>, <p> or <li>;
  2 filled        every {{placeholder}} filled the way scripts/copy336/data.py FILLS says, and no {{ left;
  3 cells         the two new table columns, cell by cell against Aria's table; a cell in CELLS_DIFFER has its
                  new value and not Aria's old one;
  4 removed       the sentences in REMOVED (now R3 only) are not on the page, and the rest of their line is (or
                  the whole line is gone when drop_line says so);
  4b replaced     the lines in REPLACED (R1, R2 with its opening-answer line, R4, R5: what Ray approved in another
                  wording) are on the page word for word, in place, in html, md and the zh-hant part of
                  llms-full.txt, and Aria's old line is in none of them (R4's old line also belongs to ColaMD, so
                  it is held to the Chrome section only);
  and: the held FAQ question (iPhone, waits for #337) and its link are not on the page; the two new tools
  link to their official pages and the Chrome extension's Web Store ID is stated; the eight old tools'
  paragraphs, bullets and table cells are the ones scripts/best228/data.py has, apart from the MarsDawn price
  bullet (Aria's new one) and
  5 corrections the old-text facts of CORRECTIONS in copy336/data.py (Marked 3's limited-time price, in its
                  bullet and its table cell; QLMarkdown's price as 開源 in its bullet and its table cell; C5, the
                  FAQ answer about native Mac apps, which also has to be in the page's FAQPage JSON-LD and in
                  llms-full.txt): each has its new text on the page, in html and md, and its old text nowhere, and
                  QLMarkdown's section, row and not-for line (R5) do not say 免費.
  MarkEdit's 只讀 cell is data.MARKEDIT_READ_ONLY (cell check 3, in html and md), not Aria's 無 and not the first
  pass's 未記載，官方稱是編輯器 (an official-repo fact, see data.MARKEDIT_READ_ONLY_SOURCES).
  Every other locale's page does not carry any of this ticket's words.

Text is compared as visible text (tags stripped, entities decoded, whitespace collapsed) against the copy with
its Markdown marks removed. Never against the build's own rendering, which would share a mistake the build makes.
sources.json's sha256 pins approved.md, so a hand edit of it fails too.

--self-test plants one break of each kind in copies of the built page and its twin and fails unless each is caught.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
from best228 import data as best  # noqa: E402
from copy336 import data  # noqa: E402

SITE = HERE.parent / "public"
PAGE = "zh-hant/best-markdown-viewer-mac"
OTHER_LOCALES = ["", "zh-hans", "ja", "de", "fr", "es", "ko"]
NEW_COLS = {"iPhone／iPad": "iphone-ipad", "只讀（不會誤改）": "read-only"}
CHROME_ID = "medapdbncneneejhbgcjceippjlfkmkg"


def ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def vis(fragment: str) -> str:
    return ws(html.unescape(re.sub(r"<[^>]+>", "", fragment)))


def plain_inline(md: str) -> str:
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"\*\*(.+?)\*\*", r"\1", md)
    return md.replace("`", "")


def plain(md: str) -> str:
    return ws(plain_inline(re.sub(r"^(?:#{1,6} |- )", "", md.strip())))


def main_of(page: str) -> str:
    m = re.search(r"<main\b.*?</main>", page, re.S)
    return m.group(0) if m else ""


# ---------------------------------------------------------------- Aria's copy

def approved_text() -> str:
    return (HERE / "copy336" / "approved.md").read_text(encoding="utf-8")


def pin_problems(text: str) -> list:
    pin = json.loads((HERE / "copy336" / "sources.json").read_text(encoding="utf-8"))["comments"]["A"]
    got = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return [] if got == pin["vendored_sha256"] else [f"approved.md: sha256 {got} is not the pinned {pin['vendored_sha256']}"]


def fenced_blocks(text: str) -> list:
    """The ~~~markdown blocks of approved.md, each as a list of non-empty lines, in order."""
    return [[ln for ln in blk.split("\n") if ln.strip()] for blk in re.findall(r"~~~markdown\n(.*?)\n~~~", text, re.S)]


def aria_meta(text: str) -> dict:
    return {
        "title": re.search(r"- `<title>`：(.+)", text).group(1).strip(),
        "h1": re.search(r"- `<h1>`：(.+)", text).group(1).strip(),
        "description": re.search(r"### description\n\n> (.+)", text).group(1).strip(),
        "price": re.search(r"價格改成「(.+?)」", text).group(1),
    }


def aria_table(text: str) -> tuple:
    block = re.search(r"\| App \|.*?\n\n", text, re.S).group(0)
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in block.strip().split("\n")]
    return rows[0], [r for r in rows[2:]]


def fill(line: str) -> str:
    def one(m):
        key = m.group(1)
        if key not in data.FILLS:
            raise KeyError(f"placeholder {{{{{key}}}}} has no entry in copy336/data.py FILLS")
        return data.FILLS[key]
    return re.sub(r"\{\{(.+?)\}\}", one, line)


def expected_lines(text: str) -> tuple:
    """(lines that must be elements of the page, in order; plain texts that must not be on it)."""
    want, absent = [], []
    blocks = fenced_blocks(text)
    assert len(blocks) == 5, f"approved.md has {len(blocks)} fenced blocks, want 5 (opening, scenarios, tools, not-for, faq)"
    held_faq = False
    for block in blocks:
        h2 = ""
        for ln in block:
            if ln.startswith("## "):
                h2 = plain(ln)
            if ln.startswith("### ") and plain(ln) in ("iPhone 怎麼看 .md 檔？",):
                held_faq = True
                absent.append(plain(ln))
                continue
            if ln.startswith("### "):
                held_faq = False
            if held_faq:
                continue
            line = plain(fill(ln))
            dropped = False
            for rep_ in data.REPLACED:
                only = rep_.get("only_after")
                if (not only or h2 == only) and plain(ln) == rep_["old"]:
                    line = rep_["new"]
                    if not only:
                        absent.append(rep_["old"])
            for rem in data.REMOVED:
                sent = plain(rem["sentence"])
                only = rem.get("only_after")
                if only and h2 != only:
                    continue
                if sent in plain(ln) or sent == plain(ln):
                    if not only:  # a rule for one section is held to that section below
                        absent.append(sent)
                    if rem["drop_line"]:
                        dropped = True
                    else:
                        line = ws(plain(fill(ln)).replace(sent, ""))
            if not dropped:
                want.append(line)
    return want, absent


# ---------------------------------------------------------------- the page

def table_of(h: str) -> tuple:
    head = [vis(c) for c in re.findall(r"<th scope=\"col\"[^>]*>(.*?)</th>", h, re.S)]
    ids = re.findall(r"<th scope=\"col\" id=\"(col-[^\"]+)\"", h)
    rows = {}
    for m in re.finditer(r"<tr id=\"cmp-[^\"]+\"><th scope=\"row\">(.*?)</th>(.*?)</tr>", h, re.S):
        rows[vis(m.group(1))] = [vis(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", m.group(2), re.S)]
    return head, ids, rows


def md_table_of(md: str) -> tuple:
    lines = [ln for ln in md.split("\n") if ln.startswith("| ")]
    cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    return cells[0], {r[0]: r[1:] for r in cells[1:]}


def sections(main: str) -> dict:
    parts = re.split(r"(?=<h2\b)", main)
    out = {}
    for part in parts:
        m = re.match(r"<h2\b[^>]*>(.*?)</h2>", part, re.S)
        if m:
            out[vis(m.group(1))] = part
    return out


def jsonld_answers(h: str) -> list:
    """(question, answer text) of every FAQPage in the page's JSON-LD."""
    out = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            blob = json.loads(m.group(1))
        except ValueError:
            continue
        for node in (blob if isinstance(blob, list) else [blob]):
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                out += [(q.get("name", ""), vis(q.get("acceptedAnswer", {}).get("text", ""))) for q in node.get("mainEntity", [])]
    return out


def zh_hant_llms(llms: str) -> str:
    """The zh-hant best page's part of llms-full.txt: from its "Source:" line to the next page's "---" rule."""
    i = llms.find("\nSource: https://marsdawn.southern-light.dev/" + PAGE + "/\n")
    if i < 0:
        return ""
    j = llms.find("\n---\n", i)
    return llms[i:j if j > 0 else len(llms)]


def page_problems(h: str, md: str, text: str, absent_extra=(), llms: str = "") -> list:
    out = []
    main = main_of(h)
    meta = aria_meta(text)
    want, absent = expected_lines(text)

    # 1-2 verbatim and filled: each line is the text of one element, in order
    els = [(m.start(), vis(m.group(2))) for m in re.finditer(r"<(h[1-3]|p|li)\b[^>]*>(.*?)</\1>", main, re.S)]
    pos = 0
    for line in want:
        if re.match(r"\| ", line):
            continue
        hit = next((i for i in range(pos, len(els)) if els[i][1] == line), None)
        if hit is None:
            anywhere = any(t == line for _, t in els)
            out.append(f"html: {'out of order' if anywhere else 'missing'}: {line[:70]}")
        else:
            pos = hit + 1
    md_plain = ws(" ".join(plain_inline(ln) for ln in md.split("\n")))
    pos = 0
    for line in want:
        i = md_plain.find(line, pos)
        if i < 0:
            out.append(f"md: {'out of order' if line in md_plain else 'missing'}: {line[:70]}")
        else:
            pos = i + len(line)

    # title, h1, description, MarsDawn's price bullet
    for key, pat in (("title", r"<title>(.*?)</title>"), ("description", r'<meta name="description" content="([^"]*)"')):
        m = re.search(pat, h, re.S)
        if not m or html.unescape(m.group(1)).strip() != meta[key]:
            out.append(f"html: {key} is not Aria's: {m.group(1) if m else None}")
    m = re.search(r"<h1\b[^>]*>(.*?)</h1>", main, re.S)
    if not m or vis(m.group(1)) != meta["h1"]:
        out.append(f"html: h1 is not Aria's: {vis(m.group(1)) if m else None}")
    if not md.startswith("# " + meta["h1"] + "\n"):
        out.append("md: first line is not Aria's h1")
    price = "價格：" + meta["price"]
    if not any(t == price for _, t in els):
        out.append("html: MarsDawn's price bullet is not Aria's")
    for need, where in (("Markdown 閱讀器推薦", meta["title"]), ("iPhone", meta["title"]),
                        ("Markdown 閱讀器推薦", meta["h1"]), ("iPhone", meta["h1"])):
        if need not in where:
            out.append(f"copy: {need} is not in {where}")
    first = meta["description"].split("。")[0]
    if "閱讀器" not in first or "推薦" not in first:
        out.append("copy: description's first sentence lacks 閱讀器 or 推薦")

    # 4 removed, and held
    htext, mtext = vis(main), md_plain
    for a in list(absent) + list(data.ABSENT) + list(absent_extra):
        if a and (a in htext or a in mtext or a in main or a in md):
            out.append(f"held/removed text is on the page: {a[:60]}")
    secs = sections(main)
    chrome = secs.get("Chrome 的 Markdown Reader 擴充功能", "")
    if "價格：免費。" in [vis(m.group(1)) for m in re.finditer(r"<li\b[^>]*>(.*?)</li>", chrome, re.S)] or "iPhone 上的 Chrome" in vis(chrome):
        out.append("html: a removed or replaced sentence is back in the Chrome section")

    # 3 cells
    head, ids, rows = table_of(h)
    arow_head, arows = aria_table(text)
    old_head = best.DATA["zh-hant"]["head"]
    for col, cid in NEW_COLS.items():
        if col not in head:
            out.append(f"html: column {col} missing")
        if f"col-{cid}" not in ids:
            out.append(f"html: column id col-{cid} missing")
    if [c for c in head if c not in NEW_COLS] != old_head:
        out.append("html: the old columns are not the eight-tool page's, in order")
    differ = {(r, c): (old, new) for r, c, old, new in data.CELLS_DIFFER}
    for arow in arows:
        name = arow[0]
        cells = rows.get(name)
        if cells is None:
            out.append(f"html: table row {name} missing")
            continue
        for k, col in enumerate(arow_head[1:], start=1):
            want_cell = fill(arow[k])
            if (name, col) in differ:
                old, new = differ[(name, col)]
                if old != arow[k]:
                    out.append(f"copy336 CELLS_DIFFER: {name}/{col} old value is not Aria's ({arow[k]!r})")
                want_cell = new
            got = cells[head.index(col) - 1] if col in head else None
            if got != want_cell:
                out.append(f"html: cell {name}/{col} is {got!r}, want {want_cell!r}")
            if (name, col) in differ and got == arow[k]:
                out.append(f"html: cell {name}/{col} still has Aria's value")
    mhead, mrows = md_table_of(md)
    if mhead != head:
        out.append("md: table head is not the page's")
    for name, cells in rows.items():
        if mrows.get(name) != cells:
            out.append(f"md: table row {name} is not the page's")
    if rows.get("MarsDawn", [""] * 9)[head.index("自動重新載入") - 1:][:1] != ["有，可撤銷"]:
        out.append("html: MarsDawn's 自動重新載入 is not 有，可撤銷")

    # the eight old tools stay as best228 has them
    old = best.DATA["zh-hant"]
    fix_bullet = {c["old"]: c["new"] for c in data.CORRECTIONS if c["where"] == "app bullet"}
    fix_cell = {c["key"]: c for c in data.CORRECTIONS if c["where"] == "table cell 價格"}
    for app in old["apps"]:
        sec = secs.get(app["name"])
        if sec is None:
            out.append(f"html: old tool {app['name']} lost its section")
            continue
        ts = [vis(m.group(2)) for m in re.finditer(r"<(p|li)\b[^>]*>(.*?)</\1>", sec, re.S)]
        for t in [vis(app["para"])] + [vis(fix_bullet.get(b, b)) for b in app["bullets"] if not (app["slug"] == "marsdawn" and b.startswith("價格："))]:
            if t not in ts:
                out.append(f"html: old text of {app['name']} changed: {t[:50]}")
    for row in old["rows"]:
        got = rows.get(row[0])
        want_cells = [vis(c) for c in row[1:]]
        if row[0] in fix_cell:
            want_cells[0] = fix_cell[row[0]]["new"]
        if got is None:
            out.append(f"html: old row {row[0]} lost")
        elif [c for col, c in zip(head[1:], got) if col not in NEW_COLS] != want_cells:
            out.append(f"html: old cells of {row[0]} changed")

    faq = re.search(r'<section class="faq">(.*?)</section>', h, re.S)
    # 5 corrections of old text: new text in html and md, old text gone, and no 免費 left for QLMarkdown
    for c in data.CORRECTIONS:
        if c["where"] == "app bullet":
            sec = secs.get({"marked": "Marked", "qlmarkdown": "QLMarkdown"}[c["key"]], "")
            if c["new"] not in [vis(m.group(1)) for m in re.finditer(r"<li\b[^>]*>(.*?)</li>", sec, re.S)]:
                out.append(f"html: correction {c['id']} ({c['app']}) is not on the page: {c['new'][:50]}")
            if c["old"] in vis(sec):
                out.append(f"html: correction {c['id']} ({c['app']}) still has the old text: {c['old'][:50]}")
            if c["new"] not in md_plain:
                out.append(f"md: correction {c['id']} ({c['app']}) is not in the twin: {c['new'][:50]}")
            if c["old"] in md_plain:
                out.append(f"md: correction {c['id']} ({c['app']}) still has the old text: {c['old'][:50]}")
        elif c["where"] == "faq answer":
            # html FAQ section, the FAQPage JSON-LD, the md twin and llms-full.txt: new text in each, old text in none
            html_ans = [vis(m.group(2)) for m in re.finditer(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", faq.group(1), re.S) if vis(m.group(1)) == c["key"]] if faq else []
            ld_ans = [a for q, a in jsonld_answers(h) if q == c["key"]]
            zl = ws(zh_hant_llms(llms))
            for where, ok, anywhere in (("html", c["new"] in html_ans, c["old"] in vis(main)),
                                        ("JSON-LD", c["new"] in ld_ans, any(c["old"] in a for _, a in jsonld_answers(h)) or c["old"] in h),
                                        ("md", c["new"] in md_plain, c["old"] in md_plain),
                                        ("llms-full.txt", c["new"] in zl, c["old"] in ws(llms))):
                if not ok:
                    out.append(f"{where}: correction {c['id']} ({c['key']}) answer is not on the page: {c['new'][:50]}")
                if anywhere:
                    out.append(f"{where}: correction {c['id']} ({c['key']}) still has the old answer: {c['old'][:50]}")
        else:
            cells = rows.get(c["key"])
            if cells is None or cells[0] != c["new"]:
                out.append(f"html: correction {c['id']} ({c['app']}) price cell is {cells[0] if cells else None!r}, want {c['new']!r}")
            if mrows.get(c["key"], [None])[0] != c["new"]:
                out.append(f"md: correction {c['id']} ({c['app']}) price cell is not {c['new']!r}")
    ql_sec, ql_row = vis(secs.get("QLMarkdown", "")), rows.get("QLMarkdown", [""])[0]
    if "免費" in ql_sec or "免費" in ql_row:
        out.append("html: QLMarkdown's section or price cell still says 免費 (the official page states no price)")
    # 4b replaced: the new line in all three outputs, Aria's old line in none (R4's only in the Chrome section)
    zl = ws(plain_inline(zh_hant_llms(llms)))
    md_chrome = md_plain[md_plain.find("Chrome 的 Markdown Reader 擴充功能"):md_plain.find("ColaMD")] if "ColaMD" in md_plain else md_plain
    for r in data.REPLACED:
        if not any(t == r["new"] for _, t in els):
            out.append(f"html: replaced line {r['id']} is not on the page: {r['new'][:50]}")
        if r["new"] not in md_plain:
            out.append(f"md: replaced line {r['id']} is not in the twin: {r['new'][:50]}")
        if r["new"] not in zl:
            out.append(f"llms-full.txt: replaced line {r['id']} is not in the zh-hant part: {r['new'][:50]}")
        if r.get("only_after"):
            if r["old"] in vis(chrome):
                out.append(f"html: Aria's line {r['id']} is back in the {r['only_after']} section: {r['old']}")
            if r["old"] in md_chrome:
                out.append(f"md: Aria's line {r['id']} is back in the {r['only_after']} section: {r['old']}")
        else:
            for where, body in (("html", vis(main)), ("md", md_plain), ("llms-full.txt", zl)):
                if r["old"] in body:
                    out.append(f"{where}: Aria's line {r['id']} is still there: {r['old'][:50]}")
    faq_h3 = [vis(x) for x in re.findall(r"<h3>(.*?)</h3>", faq.group(1), re.S)] if faq else []
    if faq_h3 != ["Mac 預設能開 .md 嗎？"] + [q for q, _ in old["faq"]]:
        out.append(f"html: FAQ questions are {faq_h3}")

    # sources of the two new tools
    colamd = secs.get("ColaMD", "")
    if CHROME_ID not in vis(chrome) or f"chromewebstore.google.com/detail/md-reader/{CHROME_ID}" not in chrome:
        out.append("html: the Chrome section does not name the extension's ID and Web Store page")
    if "https://github.com/marswaveai/ColaMD" not in colamd or "https://colamd.com/" not in colamd:
        out.append("html: the ColaMD section lacks its official links")
    if vis(main).count(data.CHECK_DATE) < 3:
        out.append(f"html: the check date {data.CHECK_DATE} is not in the opening and both new tools' sections")
    return out


def site_problems(root: Path) -> list:
    text = approved_text()
    out = pin_problems(text)
    page = root / PAGE
    if not (page / "index.html").is_file() or not (page / "index.md").is_file():
        return out + [f"{PAGE}: index.html or index.md is not built"]
    llms = root / "llms-full.txt"
    if not llms.is_file():
        out.append("llms-full.txt: missing")
    out += page_problems((page / "index.html").read_text(encoding="utf-8"), (page / "index.md").read_text(encoding="utf-8"), text,
                         llms=llms.read_text(encoding="utf-8") if llms.is_file() else "")
    for loc in OTHER_LOCALES:
        f = root / loc / "best-markdown-viewer-mac" / "index.html"
        if not f.is_file():
            out.append(f"{f.relative_to(root)}: missing")
            continue
        body = f.read_text(encoding="utf-8")
        for needle in ("Markdown 閱讀器推薦", "ColaMD", CHROME_ID):
            if needle in body:
                out.append(f"{f.relative_to(root)}: carries {needle!r}, which belongs to zh-hant only")
    return out


# ---------------------------------------------------------------- self-test

def self_test(root: Path) -> int:
    text = approved_text()
    page = root / PAGE
    h = (page / "index.html").read_text(encoding="utf-8")
    md = (page / "index.md").read_text(encoding="utf-8")
    llms = (root / "llms-full.txt").read_text(encoding="utf-8")
    if page_problems(h, md, text, llms=llms):
        print("self-test: the built page already has problems; plants prove little")
        return 1
    caught = missed = 0

    def plant(what, hh=None, mm=None, tt=None, extra=(), ll=None):
        nonlocal caught, missed
        if page_problems(hh if hh is not None else h, mm if mm is not None else md,
                         tt if tt is not None else text, extra, ll if ll is not None else llms):
            caught += 1
        else:
            print(f"self-test: {what} was NOT caught")
            missed += 1

    def sub(s, old, new):
        assert old in s, f"self-test: cannot plant, {old!r} is not there"
        return s.replace(old, new, 1)

    plant("a verbatim line changed (html)", hh=sub(h, "看三件事", "看兩件事"))
    plant("a verbatim line changed (md)", mm=sub(md, "看三件事", "看兩件事"))
    plant("a placeholder left in", hh=sub(h, "查證日期是 " + data.CHECK_DATE, "查證日期是 {{查證日期}}"))
    plant("a filled value changed", hh=sub(h, "Mermaid 圖表和數學式（KaTeX）都內建。", "Mermaid 圖表和數學式都內建。"))
    plant("a removed sentence back (R1)", hh=sub(h, "<li><strong>Marked 3</strong>：專門用來預覽和列印，PDF 有分頁和頁碼。</li>",
                                                    "<li><strong>Marked 3</strong>：專門用來預覽和列印，PDF 有分頁和頁碼。</li>\n<p>MarsDawn 也能輸出 PDF，但沒有頁碼。</p>"))
    plant("a removed sentence back (R3)", hh=sub(h, "才能讀本機檔案。", "才能讀本機檔案。iPhone 上的 Chrome 不能裝擴充功能。"))
    plant("a differing cell has Aria's value", hh=sub(h, "<td data-col=\"read-only\">未記載，官方稱是編輯器</td>", "<td data-col=\"read-only\">無，原始碼可以直接改</td>"))
    plant("a cell of the two new columns changed", hh=sub(h, "<td data-col=\"iphone-ipad\">有，只能讀</td>", "<td data-col=\"iphone-ipad\">有</td>"))
    plant("an old cell changed", hh=sub(h, "<td data-col=\"price\">一次 USD 4.99</td>", "<td data-col=\"price\">一次 USD 5.99</td>"))
    plant("an old paragraph changed", hh=sub(h, "快速查看擴充功能：在 Finder", "快速查看擴充功能：在 Finder 裡"))
    plant("the held iPhone FAQ is on the page", hh=sub(h, "<h3>Mac 預設能開 .md 嗎？</h3>", "<h3>iPhone 怎麼看 .md 檔？</h3>\n<p>x</p>\n<h3>Mac 預設能開 .md 嗎？</h3>"))
    plant("a link to the #337 page", mm=md + "\n[x](/zh-hant/view-markdown-on-iphone/)\n")
    plant("the Chrome ID is gone", hh=h.replace(CHROME_ID, "xxxx"))
    plant("the ColaMD link is gone", hh=h.replace("https://github.com/marswaveai/ColaMD", "https://example.com"))
    plant("MarsDawn's price is the old one", hh=sub(h, "價格：免費下載，試用 14 天，之後 USD 4.99 一次買斷。", "價格：免費下載，試用 14 天，之後一次 USD 4.99。"))
    plant("the title lost iPhone", hh=sub(h, "Mac、iPhone 只看不改", "Mac 只看不改"))
    # fifth kind: the old-text corrections
    plant("C1 old price wording is back (免費下載)", hh=sub(h, "Marked 3 免費試用", "Marked 3 免費下載"))
    plant("C1 original price is wrong by one digit", hh=sub(h, "每年 USD 49.99", "每年 USD 49.98"))
    plant("C1 lost its limited-time note (md)", mm=sub(md, "（限時優惠價，原價", "（原價"))
    plant("C2 table cell is the old one", hh=sub(h, "<td data-col=\"price\">優惠價每月 USD 2.99 起</td>", "<td data-col=\"price\">每月 USD 2.99 起</td>"))
    plant("C2 table cell changed (md)", mm=sub(md, "| 優惠價每月 USD 2.99 起 |", "| 優惠價每月 USD 2.98 起 |"))
    plant("C3 bullet says 免費 again", hh=sub(h, "價格：開源（GPL-3.0）。", "價格：免費（GPL-3.0）。"))
    plant("C3 bullet says 免費 again (md)", mm=sub(md, "價格：開源（GPL-3.0）。", "價格：免費（GPL-3.0）。"))
    plant("C4 table cell says 免費 again", hh=sub(h, "<td data-col=\"price\">開源（GPL-3.0）</td>", "<td data-col=\"price\">免費</td>"))
    plant("C4 table cell changed (md)", mm=sub(md, "| QLMarkdown | 開源（GPL-3.0） |", "| QLMarkdown | 開源 |"))
    # REPLACED (R1, R2, R2-opening, R4, R5): the new line missing from one output, Aria's old line back, a word changed
    llms_marker = "\nSource: https://marsdawn.southern-light.dev/" + PAGE + "/\n"

    def probe(r, body):
        """The part of r's new line that is plain text in `body` (the opening's bold lead-in has marks around it)."""
        return r["new"] if r["new"] in body else r["new"].split("：", 1)[1]

    for r in data.REPLACED:
        rid, new_, old_ = r["id"], r["new"], r["old"]
        for what, body in (("html", h), ("md", md), ("llms-full.txt", llms)):
            pr = probe(r, body)
            kw = {"html": "hh", "md": "mm", "llms-full.txt": "ll"}[what]
            plant(f"{rid} new line missing ({what})", **{kw: sub(body, pr, "x")})
            plant(f"{rid} new line has a changed word ({what})", **{kw: sub(body, pr, pr[:-3] + "xx。")})
            if r.get("only_after"):
                plant(f"{rid} Aria's old line is back ({what})", **{kw: sub(body, new_, old_)})
            elif what == "html":
                plant(f"{rid} Aria's old line is back ({what})", hh=sub(h, "</main>", f"<p>{old_}</p></main>"))
            elif what == "md":
                plant(f"{rid} Aria's old line is back ({what})", mm=md + "\n- " + old_ + "\n")
            else:
                plant(f"{rid} Aria's old line is back ({what})", ll=sub(llms, llms_marker, llms_marker + "- " + old_ + "\n"))
    # MarkEdit's 只讀 cell (P2-1)
    ro, old_ro = data.MARKEDIT_READ_ONLY, "未記載，官方稱是編輯器"
    me = "| MarkEdit | 免費 | 無 | " + ro + " |"
    plant("MarkEdit 只讀 cell is the first pass's (html)", hh=sub(h, f'<td data-col="read-only">{ro}</td>', f'<td data-col="read-only">{old_ro}</td>'))
    plant("MarkEdit 只讀 cell is the first pass's (md)", mm=sub(md, me, me.replace(ro, old_ro)))
    plant("MarkEdit 只讀 cell is Aria's 無 (html)", hh=sub(h, f'<td data-col="read-only">{ro}</td>', '<td data-col="read-only">無</td>'))
    plant("MarkEdit 只讀 cell is another string (html)", hh=sub(h, f'<td data-col="read-only">{ro}</td>', '<td data-col="read-only">有，唯讀模式</td>'))
    plant("MarkEdit 只讀 cell is another string (md)", mm=sub(md, me, me.replace(ro, "有")))
    # C5: the native-app FAQ answer, in html, JSON-LD, md and llms-full.txt
    c5 = next(c for c in data.CORRECTIONS if c["id"] == "C5")
    old5, new5 = c5["old"], c5["new"]

    def in_jsonld(page, old, new):
        """Swap text inside the FAQPage JSON-LD only."""
        m = re.search(r'<script type="application/ld\+json">(?:(?!</script>).)*?' + re.escape(old) + r'.*?</script>', page, re.S)
        assert m, f"self-test: {old[:30]!r} is not in a JSON-LD block"
        return page[:m.start()] + m.group(0).replace(old, new, 1) + page[m.end():]

    plant("C5 old answer is back (html only)", hh=sub(h, "<p>" + new5 + "</p>", "<p>" + old5 + "</p>"))
    plant("C5 old answer is back (JSON-LD only)", hh=in_jsonld(h, new5, old5))
    plant("C5 old answer is back (md)", mm=sub(md, new5, old5))
    plant("C5 old answer is back (llms-full.txt)", ll=sub(llms, new5, old5))
    plant("C5 new answer is missing (html only)", hh=sub(h, "<p>" + new5 + "</p>", "<p>x</p>"))
    plant("C5 new answer is missing (JSON-LD only)", hh=in_jsonld(h, new5, "x"))
    plant("C5 new answer is missing (md)", mm=sub(md, new5, "x"))
    plant("C5 new answer is missing (llms-full.txt)", ll=sub(llms, new5, "x"))
    # the pin: a changed approved.md text is the pin's problem, not the page's
    if not pin_problems(text + "x\n"):
        print("self-test: a changed approved.md was NOT caught by the pin")
        missed += 1
    else:
        caught += 1
    print(f"self-test: {caught} caught, {missed} missed")
    return 1 if missed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(SITE))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    if args.self_test:
        return self_test(root)
    problems = site_problems(root)
    for p in problems:
        print(p)
    if problems:
        print(f"{len(problems)} problems")
        return 1
    print("ok: #336 copy on /zh-hant/best-markdown-viewer-mac/ (html and md): verbatim lines, filled placeholders, "
          f"{len(data.CELLS_DIFFER)} table cells that differ from Aria's, {len(data.REMOVED)} removed sentence(s), "
          f"{len(data.REPLACED)} replaced lines (R1, R2, R4, R5), "
          f"{len(data.CORRECTIONS)} old-text corrections (kind 5), other old text unchanged, held iPhone FAQ absent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
