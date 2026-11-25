#!/usr/bin/env python3
"""Checks that the built /pdf/ pages carry website #383's approved copy, character for character, and that every
cell is within Daphne's length limit.

The approved copy is not typed here. scripts/copy383/ingest.py reads it from the pinned issue comments (ids and
sha256 in scripts/copy383/sources.json) and writes scripts/copy383/data.py; this file reads that data (column
"建議", the proposed text) and compares it with the built public/ files. It never reads build_pages.py or the
copy_*.py files, and it compares EXACTLY: no strip, no whitespace collapsing, no NBSP normalisation, no case folding.

Per locale, per cell, one line:

    PASS|FAIL  <locale>  <cell>  chars=<n>  <where it was compared>   [limit <count>/<limit> <unit> ok|OVER]

A FAIL prints the first differing code point and its index. Check for a parse problem first (the structure of
the page, the cell's markup) before calling a FAIL a copy problem.

Compared places, per locale:
  /pdf/index.html  <title>, meta description, og:title, og:description, h1, lede, the three h2, the three steps
                   (label in <strong>, sentence), the opener, three figcaptions, three img alt, the four list
                   items (the last is the #369 sentence), the iPhone/iPad line, the closing line and its link.
                   The Print & Export figure's image, alt, markers, leaders and ordered caption.
  /pdf/index.md    the same cells as lines, in the same order.
  llms.txt         "- [name](.../pdf/index.md): meta".
  yours, pay-once, limits, native (html)   trait nav: <a>name</a><span>trait</span>.
  index.html       home card: <a>name</a><span>card</span>.
  /pdf/ and every page's footer: the page name.   JSON-LD BreadcrumbList on /pdf/: the page name.
Both formats must use the new panel image and omit the old PDF viewer image and alt. The HTML page must omit
the deleted cell (b_del) and the original "待圖" marker.

Limits are Daphne's structure table (issue #383, section 2). Words = str.split() on the visible text; chars = len().
For the panel alt and callouts, Aria's approved counts split on whitespace (including NBSP), then count tokens
with a word character. English also counts a standalone "&". The original cells retain their original counts.
The #369 sentence (b369) is locked by check_copy369.py and is reported as LOCKED when it is over, not as a FAIL.

Exit codes: 0 all good, 1 a mismatch, 2 usage error or a failed --self-test.

    python3 scripts/check_copy383.py                 # public/
    python3 scripts/check_copy383.py --site DIR      # another built tree
    python3 scripts/check_copy383.py --self-test     # positive control plus in-memory mutations; writes nothing
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from copy383.data import TABLE_A  # noqa: E402

ROOT = HERE.parent
BASE = "https://marsdawn.southern-light.dev"
LOCALES = ["en", "zh-Hant", "zh-Hans", "ja", "ko", "de", "fr", "es"]
PREFIX = {"en": "", "zh-Hant": "zh-hant/", "zh-Hans": "zh-hans/", "ja": "ja/", "ko": "ko/", "de": "de/",
          "fr": "fr/", "es": "es/"}
# The page names (issue #383, Aria's page-name table). Written out here so a wrong name in the sources is caught.
NAME = {"en": "Print & PDF", "zh-Hant": "列印與 PDF", "zh-Hans": "打印与 PDF", "ja": "プリントと PDF",
        "ko": "프린트 및 PDF", "de": "Drucken und PDF", "fr": "Imprimer et PDF", "es": "Imprimir y PDF"}
CALLOUTS = ("co1", "co2", "co3")
COPY_CELLS = ["title", "meta", "h1", "lede", "fig_alt", *CALLOUTS, "h2_steps", "step1", "step2", "step3",
              "h2_layouts", "opener", "cap_doc", "cap_hb", "cap_ho", "alt_doc", "alt_hb", "alt_ho",
              "h2_bul", "b1", "b2", "b3", "b_del", "b369", "ios", "close", "trait", "card"]
PANEL_SRC = "/assets/screens/06-print-export-868.png"
PANEL_CANDIDATES = ("/assets/screens/06-print-export-800.png 800w", f"{PANEL_SRC} 868w")
IMG = {"doc": "layout-document.png", "hb": "layout-handbook-contents.png", "ho": "layout-handout.png"}
TRAIT_PAGES = ["yours", "pay-once", "limits", "native"]

# Daphne's limits: (kind, limit) per column group. kind: "w" words, "c" chars. Columns: en, zh (Hant/Hans), ja, ko, latin (de/fr/es).
_COL = {"en": 0, "zh-Hant": 1, "zh-Hans": 1, "ja": 2, "ko": 3, "de": 4, "fr": 4, "es": 4}
LIMITS = {
    "title": [("c", 48), ("c", 30), ("c", 30), ("c", 30), ("c", 54)],
    "meta": [("c", 155), ("c", 90), ("c", 90), ("c", 90), ("c", 160)],
    "h1": [("w", 8), ("c", 16), ("c", 26), ("c", 24), ("w", 11)],
    "h1.chars": [("c", 45), None, None, None, ("c", 60)],
    "lede": [("w", 30), ("c", 55), ("c", 95), ("c", 95), ("w", 38)],
    "fig_alt": [("w", 25), ("c", 60), ("c", 60), ("c", 60), ("w", 30)],
    "co": [("w", 8), ("c", 16), ("c", 24), ("c", 22), ("w", 10)],
    "step.label": [("w", 3), ("c", 6), ("c", 10), ("c", 10), ("w", 4)],
    "step.text": [("w", 18), ("c", 36), ("c", 55), ("c", 55), ("w", 22)],
    "opener": [("w", 25), ("c", 50), ("c", 80), ("c", 80), ("w", 32)],
    "cap": [("w", 16), ("c", 32), ("c", 50), ("c", 50), ("w", 20)],
    "alt": [("w", 20), ("c", 45), ("c", 45), ("c", 45), ("w", 25)],
    "bullet": [("w", 20), ("c", 40), ("c", 65), ("c", 60), ("w", 26)],
    "ios": [("w", 20), ("c", 40), ("c", 65), ("c", 60), ("w", 26)],
    "close": [("w", 20), ("c", 40), ("c", 65), ("c", 60), ("w", 26)],
    "trait": [("w", 9), ("c", 22), ("c", 34), ("c", 32), ("w", 12)],
}


class Site:
    """Reads files under a built tree. `mutate(relpath, text)` lets --self-test change what the checks see."""

    def __init__(self, root: Path, mutate=None):
        self.root, self.mutate, self._cache = Path(root), mutate, {}

    def read(self, rel: str):
        if rel not in self._cache:
            p = self.root / rel
            text = p.read_text(encoding="utf-8") if p.is_file() else None
            if text is not None and self.mutate:
                text = self.mutate(rel, text)
            self._cache[rel] = text
        return self._cache[rel]


def plain(cell: str) -> str:
    """The visible text of a cell: **bold** and [text](url) lose their markup."""
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cell.replace("**", ""))


def tags_off(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment))


def first_diff(want: str, got: str) -> str:
    n = min(len(want), len(got))
    i = next((k for k in range(n) if want[k] != got[k]), n)
    w = f"U+{ord(want[i]):04X}" if i < len(want) else "end"
    g = f"U+{ord(got[i]):04X}" if i < len(got) else "end"
    return f"first difference at index {i}: want {w}, got {g}; want {want[max(0, i - 12):i + 12]!r}, got {got[max(0, i - 12):i + 12]!r}"


def words(text: str) -> int:
    return len(text.split())


def words_text(text: str, locale: str) -> int:
    return sum(bool(re.search(r"\w", token)) or (locale == "en" and token == "&") for token in text.split())


def limit_text(locale: str, cell: str, text: str, key: str = None) -> str:
    """'count/limit unit ok|OVER' for a cell, or '' when there is no limit for it."""
    key = key or ("co" if cell in CALLOUTS else cell)
    row = LIMITS.get(key)
    if row is None:
        return ""
    parts = []
    for r in (row, LIMITS.get(key + ".chars")):
        spec = r[_COL[locale]] if r else None
        if spec:
            if spec[0] == "c":
                n = len(text)
            else:
                n = words_text(text, locale) if key in ("fig_alt", "co") else words(text)
            parts.append(f"{n}/{spec[1]} {'words' if spec[0] == 'w' else 'chars'} {'ok' if n <= spec[1] else 'OVER'}")
    return "limit " + ", ".join(parts)


def over(limit: str) -> bool:
    return "OVER" in limit


def label_and_rest(cell: str):
    m = re.match(r"\*\*(.+?)\*\* ?(.*)$", cell, re.S)
    return (m.group(1), m.group(2)) if m else (None, cell)


def expected(locale: str) -> dict:
    return {k: v[1] for k, v in TABLE_A[locale].items()}


def collect_panel(body: str) -> dict:
    shot = re.search(r'<figure class="shot">(.*?)</figure>', body, re.S)
    figure = shot[1] if shot else ""
    image = re.search(r'<img\s([^>]*)>', figure)
    attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', image[1])) if image else {}
    alt = attrs.get("alt")
    out = {
        "fig_alt": (html.unescape(alt) if alt is not None else None, "html panel img alt"),
        "panel.src": (attrs.get("src"), "html panel img src"),
        "panel.srcset": (attrs.get("srcset"), "html panel img srcset"),
    }
    caption = re.search(r'<figcaption>[^<]*(?:<span[^>]*>[^<]*</span>\s*)?<ol>(.*?)</ol>', figure, re.S)
    items = re.findall(r'<li>(.*?)</li>', caption[1], re.S) if caption else []
    out["panel.caption"] = (len(items), "html panel figcaption li count")
    for i, cell in enumerate(CALLOUTS, 1):
        cls = rf'[^"]* co-print-export-{i}(?=\s|")[^"]*'
        leaders = re.findall(rf'<span class="leader {cls}"[^>]*><span>(.*?)</span></span>', figure, re.S)
        markers = re.findall(rf'<span class="marker {cls}"[^>]*>(.*?)</span>', figure, re.S)
        out[cell] = (tags_off(leaders[0]) if len(leaders) == 1 else None, f"html panel leader #{i}")
        out[cell + ".caption"] = (tags_off(items[i - 1]) if i <= len(items) else None, f"html panel figcaption li #{i}")
        out[cell + ".marker"] = (markers[0] if len(markers) == 1 else None, f"html panel marker #{i}")
    return out


def collect(site: Site, locale: str) -> dict:
    """What the built /pdf/ page of one locale says in each cell: {cell: (text, where)}, or an error string."""
    pre = PREFIX[locale]
    h = site.read(f"{pre}pdf/index.html")
    md = site.read(f"{pre}pdf/index.md")
    if h is None:
        return {"_missing": f"{pre}pdf/index.html is missing"}
    main = re.search(r"<main[^>]*>(.*?)</main>", h, re.S)
    if not main:
        return {"_missing": "no <main> in the page"}
    body = main.group(1)
    body = body.split('<nav class="traits"')[0]
    out = collect_panel(body)
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    out["title"] = (tags_off(t.group(1)).removesuffix(" · MarsDawn") if t else None, "html <title>")
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    out["meta"] = (html.unescape(m.group(1)) if m else None, "html meta description")
    for prop, key in (("og:title", "og_title"), ("og:description", "og_desc")):
        m = re.search(rf'<meta property="{prop}" content="([^"]*)"', h)
        out[key] = (html.unescape(m.group(1)) if m else None, prop)
    m = re.search(r"<h1>(.*?)</h1>\s*<p>(.*?)</p>", body, re.S)
    out["h1"] = (tags_off(m.group(1)) if m else None, "html h1")
    out["lede"] = (tags_off(m.group(2)) if m else None, "html lede")
    h2 = re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)
    for i, key in enumerate(("h2_steps", "h2_layouts", "h2_bul")):
        out[key] = (tags_off(h2[i]) if i < len(h2) else None, f"html h2 #{i + 1}")
    ol = re.search(r'<ol class="loop-steps">(.*?)</ol>', body, re.S)
    lis = re.findall(r"<li>(.*?)</li>", ol.group(1), re.S) if ol else []
    for i in range(3):
        li = lis[i] if i < len(lis) else None
        out[f"step{i + 1}"] = (tags_off(li) if li is not None else None, "html loop-steps li")
        sm = re.match(r"<strong>(.*?)</strong>", li or "")
        out[f"step{i + 1}.label"] = (tags_off(sm.group(1)) if sm else None, "html <strong>")
    m = re.search(r"<h2[^>]*>" + re.escape(h2[1] if len(h2) > 1 else "\0") + r"</h2>\s*<p>(.*?)</p>", body, re.S)
    out["opener"] = (tags_off(m.group(1)) if m else None, "html p after h2 #2")
    shots = re.search(r'<div class="layout-shots">(.*?)\n</div>', body, re.S)
    figs = re.findall(r"<figure>(.*?)</figure>", shots.group(1), re.S) if shots else []
    for i, k in enumerate(("doc", "hb", "ho")):
        f = figs[i] if i < len(figs) else ""
        c = re.search(r"<figcaption>(.*?)</figcaption>", f, re.S)
        a = re.search(r'<img src="([^"]*)" alt="([^"]*)"', f)
        out["cap_" + k] = (tags_off(c.group(1)) if c else None, "html figcaption")
        out["alt_" + k] = (html.unescape(a.group(2)) if a else None, "html img alt")
        out["src_" + k] = (a.group(1) if a else None, "html img src")
        cs = re.match(r"<strong>(.*?)</strong>", c.group(1) if c else "")
        out["cap_" + k + ".label"] = (tags_off(cs.group(1)) if cs else None, "html figcaption <strong>")
    ul = re.search(r"<h2[^>]*>" + re.escape(h2[2] if len(h2) > 2 else "\0") + r"</h2>\s*<ul>(.*?)</ul>(.*)$", body, re.S)
    bl = re.findall(r"<li>(.*?)</li>", ul.group(1), re.S) if ul else []
    for key, i in (("b1", 0), ("b2", 1), ("b3", 2), ("b369", 3)):
        out[key] = (tags_off(bl[i]) if i < len(bl) else None, f"html ul li #{i + 1}")
    out["_nbullets"] = (len(bl), "html")
    ps = re.findall(r"<p>(.*?)</p>", ul.group(2), re.S) if ul else []
    out["ios"] = (tags_off(ps[0]) if len(ps) > 0 else None, "html p after ul")
    out["close"] = (tags_off(ps[1]) if len(ps) > 1 else None, "html closing p")
    ln = re.search(r'<a href="([^"]*)">', ps[1]) if len(ps) > 1 else None
    out["close.href"] = (ln.group(1) if ln else None, "html closing link")
    out["_np_after_ul"] = (len(ps), "html")
    # the markdown twin
    lines = md.split("\n") if md is not None else None
    out["_md"] = lines
    return out


def md_expect(locale: str) -> list:
    """The twin's lines, in order, from the cells (as the twin writes them)."""
    e = expected(locale)
    lines = [("h1", "# " + e["h1"]), ("lede", e["lede"]), ("fig_alt", f"![{e['fig_alt']}]({BASE}{PANEL_SRC})")]
    lines += [(cell, f"{i}. {e[cell]}") for i, cell in enumerate(CALLOUTS, 1)]
    lines += [("h2_steps", "## " + e["h2_steps"]),
             ("step1", "1. " + e["step1"]), ("step2", "2. " + e["step2"]), ("step3", "3. " + e["step3"]),
             ("h2_layouts", "## " + e["h2_layouts"]), ("opener", e["opener"])]
    for k in ("doc", "hb", "ho"):
        lines.append(("alt_" + k, f"![{e['alt_' + k]}](/assets/cli/{IMG[k]})"))
        lines.append(("cap_" + k, e["cap_" + k]))
    lines += [("h2_bul", "## " + e["h2_bul"]), ("b1", "- " + e["b1"]), ("b2", "- " + e["b2"]), ("b3", "- " + e["b3"]),
              ("b369", "- " + e["b369"]), ("ios", e["ios"]), ("close", e["close"])]
    return lines


def run(site: Site, quiet: bool = False):
    """Returns (lines, failures). Each line is the printed result of one cell."""
    lines, fails = [], 0

    def emit(ok, locale, cell, chars, where, limit="", note=""):
        nonlocal fails
        if not ok:
            fails += 1
        lines.append(f"{'PASS' if ok else 'FAIL'}  {locale:8} {cell:11} chars={chars:<4} {where}"
                     + (f"  [{limit}]" if limit else "") + (f"  {note}" if note else ""))

    for locale in LOCALES:
        e = expected(locale)
        got = collect(site, locale)
        if "_missing" in got:
            emit(False, locale, "(page)", 0, got["_missing"])
            continue
        # html cells
        for cell in COPY_CELLS:
            if cell in ("b_del", "trait", "card"):
                continue
            want = plain(e[cell])
            text, where = got[cell]
            ok = text == want
            note = "" if ok else (f"{first_diff(want, text)}" if text is not None else "element not found")
            lim = ""
            if cell.startswith("step"):
                label, rest = label_and_rest(e[cell])
                lim = limit_text(locale, cell, plain(label), "step.label") + " | " + limit_text(locale, cell, plain(rest), "step.text")
            elif cell.startswith("cap_") and "bullet" not in cell:
                label, rest = label_and_rest(e[cell])
                lim = limit_text(locale, cell, want, "cap")
            elif cell.startswith("alt_"):
                lim = limit_text(locale, cell, want, "alt")
            elif cell in ("b1", "b2", "b3", "b369"):
                lim = limit_text(locale, cell, want, "bullet")
            elif cell.startswith("h2_"):
                lim = ""
            else:
                lim = limit_text(locale, cell, want)
            locked = cell == "b369" and over(lim)
            emit(ok, locale, cell, len(want), where, lim.replace("OVER", "OVER, locked by #369") if locked else lim, note)
        # The caption repeats each leader's copy, and every leader has a matching marker.
        for i, cell in enumerate(CALLOUTS, 1):
            want = e[cell]
            text, where = got[cell + ".caption"]
            emit(text == want, locale, cell + ".caption", len(want), where,
                 note="" if text == want else first_diff(want, text) if text is not None else "element not found")
            marker, where = got[cell + ".marker"]
            emit(marker == str(i), locale, cell + ".marker", 0, where, note="" if marker == str(i) else f"got {marker!r}")
        src, where = got["panel.src"]
        emit(src == PANEL_SRC, locale, "panel.src", len(PANEL_SRC), where, note="" if src == PANEL_SRC else f"got {src!r}")
        srcset, where = got["panel.srcset"]
        candidates = {part.strip() for part in (srcset or "").split(",")}
        srcset_ok = candidates.issuperset(PANEL_CANDIDATES)
        emit(srcset_ok, locale, "panel.srcset", 0, where, note="" if srcset_ok else f"got {srcset!r}")
        count, where = got["panel.caption"]
        emit(count == len(CALLOUTS), locale, "panel.caption", 0, where,
             note="" if count == len(CALLOUTS) else f"got {count}, want {len(CALLOUTS)}")
        # bold labels in <strong>
        for cell in ("step1", "step2", "step3", "cap_doc", "cap_hb", "cap_ho"):
            label, _ = label_and_rest(e[cell])
            text, where = got[cell + ".label"]
            ok = text == label
            emit(ok, locale, cell + ".label", len(label), where, "", "" if ok else (first_diff(label, text) if text else "no <strong>"))
        for k in ("doc", "hb", "ho"):
            src = got["src_" + k][0]
            emit(src == f"/assets/cli/{IMG[k]}", locale, "src_" + k, len(IMG[k]), "html img src", "", "" if src == f"/assets/cli/{IMG[k]}" else f"got {src!r}")
        want_href = f"/{PREFIX[locale]}cli/"
        emit(got["close.href"][0] == want_href, locale, "close.href", len(want_href), "html closing link",
             "", "" if got["close.href"][0] == want_href else f"got {got['close.href'][0]!r}")
        nb, npa = got["_nbullets"][0], got["_np_after_ul"][0]
        emit(nb == 4 and npa == 2, locale, "structure", 0, "html", "", f"{nb} list items (want 4), {npa} paragraphs after the list (want 2)" if not (nb == 4 and npa == 2) else "")
        # og: tags equal the title / description
        emit(got["og_title"][0] == e["title"] + " · MarsDawn", locale, "og_title", len(e["title"]) + 11, "og:title", "", "")
        emit(got["og_desc"][0] == e["meta"], locale, "og_desc", len(e["meta"]), "og:description", "", "")
        # the deleted cell and the retired PDF viewer figure
        h = site.read(f"{PREFIX[locale]}pdf/index.html") or ""
        old_b_del = TABLE_A[locale]["b_del"][0]
        emit(old_b_del not in h and "待圖" not in h, locale, "b_del", len(old_b_del), "old list item absent, no 待圖 marker")
        old_alt = TABLE_A[locale]["fig_alt"][0]
        for fmt, page in (("html", h), ("md", site.read(f"{PREFIX[locale]}pdf/index.md"))):
            if page is not None:
                old_fig = [label for label, needle in (("05-pdf", "05-pdf"), ("old alt", old_alt))
                           if needle in html.unescape(page)]
                emit(not old_fig, locale, f"{fmt}.old_fig", 0, fmt, note="found " + ", ".join(old_fig) if old_fig else "")
        # markdown twin
        md = got["_md"]
        if md is None:
            emit(False, locale, "(md)", 0, "pdf/index.md is missing")
        else:
            pos = -1
            for cell, want in md_expect(locale):
                idx = [i for i, l in enumerate(md) if l == want]
                ok = len(idx) == 1 and idx[0] > pos
                if idx and ok:
                    pos = idx[0]
                if not ok:
                    near = next((l for l in md if l[:6] == want[:6] and l != want), None)
                    note = (f"found {len(idx)} times" if len(idx) != 1 else "out of order") + (f"; {first_diff(want, near)}" if near and not idx else "")
                else:
                    note = ""
                emit(ok, locale, "md." + cell, len(want), "md line", "", note)
        # llms.txt
        llms = site.read("llms.txt") or ""
        want = f"- [{NAME[locale]}]({BASE}/{PREFIX[locale]}pdf/index.md): {e['meta']}"
        emit(want in llms.split("\n"), locale, "llms.txt", len(want), "llms.txt line")
        # footer and breadcrumb on the page itself
        foot = f'<li><a href="/{PREFIX[locale]}pdf/" aria-current="page">{html.escape(NAME[locale], quote=False)}</a></li>'
        emit(foot in h, locale, "footer", len(NAME[locale]), "footer link on /pdf/")
        cn = None
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            data = json.loads(block)
            if isinstance(data, dict) and data.get("@type") == "BreadcrumbList":
                cn = data["itemListElement"][-1]["name"]
        emit(cn == NAME[locale], locale, "breadcrumb", len(NAME[locale]), "JSON-LD BreadcrumbList name")
        # trait nav and home card
        trait_line = f'<li><a href="/{PREFIX[locale]}pdf/">{html.escape(NAME[locale], quote=False)}</a><span>{html.escape(e["trait"], quote=False)}</span></li>'
        trait_lim = limit_text(locale, "trait", e["trait"])
        for slug in TRAIT_PAGES:
            ph = site.read(f"{PREFIX[locale]}{slug}/index.html") or ""
            emit(trait_line in ph, locale, "trait@" + slug, len(e["trait"]), "html trait nav", trait_lim if slug == TRAIT_PAGES[0] else "")
        home = site.read(f"{PREFIX[locale]}index.html") or ""
        card = f'<a href="/{PREFIX[locale]}pdf/">{html.escape(NAME[locale], quote=False)}</a><span>{html.escape(e["card"], quote=False)}</span>'
        emit(card in home, locale, "card", len(e["card"]), "home page card")
    return lines, fails


def swap(rel_for, old_new):
    def mutate(rel, text):
        if rel in rel_for:
            old, new = old_new(text)
            return text.replace(old, new, 1)
        return text
    return mutate


def panel_self_test_cases():
    first_word, second_word = expected("en")["fig_alt"].split()[:2]
    ja_callout = expected("ja")["co1"]
    es_panel = f'src="{PANEL_SRC}" srcset="{", ".join(PANEL_CANDIDATES)}"'
    es_pdf = ('src="/assets/screens/05-pdf-980.png" '
              'srcset="/assets/screens/05-pdf-800.png 800w, /assets/screens/05-pdf-980.png 980w"')
    de_callout = f'3. {expected("de")["co3"]}\n'
    return [
        ("one word changed in the panel alt (en)",
         swap({"pdf/index.html"}, lambda t: (f'alt="{first_word} {second_word} ', f'alt="This {second_word} '))),
        ("panel leader changed (ja)",
         swap({"ja/pdf/index.html"}, lambda t: (f"><span>{ja_callout}</span></span>", f"><span>{ja_callout}!</span></span>"))),
        ("old 05-pdf image back (es)", swap({"es/pdf/index.html"}, lambda t: (es_panel, es_pdf))),
        ("panel callout missing from the twin (de)", swap({"de/pdf/index.md"}, lambda t: (de_callout, ""))),
    ]


def self_test() -> int:
    site = Site(ROOT / "public")
    lines, fails = run(site)
    if fails:
        print("self-test: the positive control fails on the real tree, so mutations prove nothing:")
        print("\n".join(l for l in lines if l.startswith("FAIL")))
        return 2
    pdf = {loc: f"{PREFIX[loc]}pdf/index.html" for loc in LOCALES}
    e = {loc: expected(loc) for loc in LOCALES}

    def first(loc, key):
        return plain(e[loc][key])

    cases = [
        ("double space in a step", swap({pdf["en"]}, lambda t: (first("en", "step2")[:5], first("en", "step2")[:5] + " "))),
        ("NBSP turned into a space (fr)", swap({pdf["fr"]}, lambda t: ("\xa0", " "))),
        ("NBSP dropped (de)", swap({pdf["de"]}, lambda t: ("\xa0", ""))),
        ("one character swapped (ja lede)", swap({pdf["ja"]}, lambda t: (first("ja", "lede"), first("ja", "lede")[:3] + "X" + first("ja", "lede")[4:]))),
        ("one character appended (ko h1)", swap({pdf["ko"]}, lambda t: ("</h1>", "!</h1>"))),
        ("title changed (es)", swap({pdf["es"]}, lambda t: ("<title>", "<title>x"))),
        ("an alt changed (zh-Hans)", swap({pdf["zh-Hans"]}, lambda t: ('alt="' + e["zh-Hans"]["alt_hb"][:4], 'alt="XXXX'))),
        ("a list item removed", swap({pdf["en"]}, lambda t: ("  <li>" + e["en"]["b2"], "  <li>"))),
        ("old page name in the footer (en)", swap({pdf["en"]}, lambda t: ('aria-current="page">Print &amp; PDF', 'aria-current="page">PDF export'))),
        ("a caption from another locale (zh-Hant gets en)", swap({pdf["zh-Hant"]}, lambda t: (label_and_rest(e["zh-Hant"]["cap_doc"])[1], label_and_rest(e["en"]["cap_doc"])[1]))),
        ("a 待圖 marker left in the page (en)", swap({pdf["en"]}, lambda t: ("</main>", "待圖</main>"))),
        ("trait line changed on /limits/ (es)", swap({"es/limits/index.html"}, lambda t: (e["es"]["trait"], e["es"]["trait"] + "."))),
        ("md twin line changed (ja)", swap({"ja/pdf/index.md"}, lambda t: (e["ja"]["opener"], e["ja"]["opener"] + " "))),
        ("llms.txt meta changed (de)", swap({"llms.txt"}, lambda t: (e["de"]["meta"], e["de"]["meta"][:-1]))),
    ] + panel_self_test_cases()
    bad = 0
    for name, mut in cases:
        _, f = run(Site(ROOT / "public", mut))
        print(f"  {'caught' if f else 'MISSED'}: {name} ({f} FAIL)")
        bad += 0 if f else 1
    gone = Site(ROOT / "public", lambda rel, text: None if rel == "ja/pdf/index.html" else text)
    _, f = run(gone)
    print(f"  {'caught' if f else 'MISSED'}: a missing locale file ({f} FAIL)")
    bad += 0 if f else 1
    print("self-test:", "FAILED" if bad else "ok (positive control passes, every mutation is caught)")
    return 2 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--site", default=str(ROOT / "public"))
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not Path(a.site).is_dir():
        print(f"no such directory: {a.site}", file=sys.stderr)
        return 2
    lines, fails = run(Site(Path(a.site)))
    print("\n".join(lines))
    print(f"\n{len(LOCALES)} locales, {len(lines)} comparisons: {len(lines) - fails} PASS, {fails} FAIL")
    over_n = [l for l in lines if "OVER" in l and "locked" not in l]
    print(f"length limits: {len(over_n)} cell(s) over the limit, "
          f"{sum(1 for l in lines if 'locked by #369' in l)} locked #369 sentence(s) over")
    for l in over_n:
        print("  OVER", l)
    compared = set()
    for line in lines:
        _, locale, field, _ = line.split(maxsplit=3)
        cell = field.split("@", 1)[0]
        if cell in COPY_CELLS:
            compared.add((locale, cell))
    pending = sum(len(TABLE_A[locale].keys() - set(COPY_CELLS)) for locale in LOCALES)
    print(f"copy cells: {len(compared)} ({len(LOCALES)} locales x {len(COPY_CELLS)}), PENDING {pending}")
    return 1 if fails or over_n else 0


if __name__ == "__main__":
    sys.exit(main())
