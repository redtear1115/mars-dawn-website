#!/usr/bin/env python3
"""Checks that the built /features/, /limits/, /vs/, /pay-once/ and /roadmap/ carry website #363's copy, verbatim.

scripts/copy363/data.py holds Aria's corrections of the old iOS claims: DATA[locale] has 6 pieces.
scripts/copy363/old.json holds what they replace (written by the caller from the #370 head): the 5 old
strings, the deleted Callouts bullet of Mac 1.2.2, the Plans bullet that stays, the four h3 titles of
/roadmap/ and the old "Last updated" line. This reads the built public/ files, not build_pages.py, and fails
unless every locale's pages and their Markdown twins (index.md) hold each piece in full and in its place:

- /features/: the paragraph right after the h3 whose paragraph lists .log ends with features_other_last;
- /limits/: one list item equals limits_ios and one limits_other, each starting with its bold label;
- /vs/: one paragraph holds vs_lacks_ios; /pay-once/: one list item ends with payonce_ios;
- /roadmap/: one paragraph equals roadmap_updated, the only bullet under "Mac 1.2.2" is the kept one, the
  Callouts bullet is gone, the four headings are there once each and in order;
- every piece once on its page (in <main>, and in the twin);
- fr's U+00A0 (limits_ios 2, limits_other 2, vs_lacks_ios 1, payonce_ios 1, roadmap_updated 1) on the pages
  as the character itself, not &nbsp; or a space; none in any other locale;
- no old string, Callouts bullet or old "Last updated" line on any file under public/ (.html, .md, .txt,
  .json), even with tags, non-breaking spaces or &nbsp; between its words;
- the home page's third FAQ answer still #369's (scripts/copy369/data.py) as visible text, as the FAQPage
  JSON-LD's mainEntity[2] answer, in the twin and in llms-full.txt, once each; and the old iPhone-or-iPad
  answers (scripts/promo130/data.py) on no file under public/;
- with --against REF_DIR (or --base-dir DIR, the same): native/ and vs/macmd-viewer/ (index.html and
  index.md, every locale) byte for byte as in REF_DIR, a second public tree such as the #370 head's.

Pieces are compared as visible text: tags stripped, entities decoded, runs of ASCII whitespace collapsed
(U+00A0 kept as it is), against the copy with only its Markdown marks and list marker removed. Never
against the build's own rendering, which would share any mistake the build makes.

--self-test reads the built pages into memory and, on copies, changes one character of each piece, empties
and duplicates each piece, puts the Callouts bullet back, removes the Plans bullet, swaps two headings,
brings the old "Last updated" line back, turns fr's U+00A0 into spaces and into &nbsp;, plants each old
string (whole, NBSP-spaced, &nbsp;-spaced, tag-wrapped) into a copy of /features/ and llms-full.txt, and
changes and duplicates the home FAQ answer; it fails unless the unplanted copies are clean and every change
is caught. Nothing is written to public/.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from copy363 import data  # noqa: E402
from copy369 import data as data369  # noqa: E402
from promo130 import data as promo_data  # noqa: E402

SITE = HERE.parent / "public"
OLD_JSON = HERE / "copy363" / "old.json"
ROOTS = {"en": "", "zh-hant": "zh-hant/", "zh-hans": "zh-hans/", "ja": "ja/", "ko": "ko/", "de": "de/",
         "fr": "fr/", "es": "es/"}
PAGES = {"home": "", "features": "features/", "limits": "limits/", "vs": "vs/", "pay-once": "pay-once/",
         "roadmap": "roadmap/"}
KEYS = ["features_other_last", "limits_ios", "limits_other", "vs_lacks_ios", "payonce_ios", "roadmap_updated"]
ON_PAGE = {"features": ["features_other_last"], "limits": ["limits_ios", "limits_other"], "vs": ["vs_lacks_ios"],
           "pay-once": ["payonce_ios"], "roadmap": ["roadmap_updated"]}
NBSP = " "
NBSP_WANT = {"fr": {"features_other_last": 0, "limits_ios": 2, "limits_other": 2, "vs_lacks_ios": 1,
                    "payonce_ios": 1, "roadmap_updated": 1}}
NBSP_ENTITY = re.compile(r"&(?:nbsp|#0*160|#[xX]0*[aA]0);")
ENT_MARK = "\x01"   # where an &nbsp; entity stood, in strict()
SCAN_SUFFIXES = {".html", ".md", ".txt", ".json"}
UNTOUCHED = ["native/", "vs/macmd-viewer/"]


def ws(s: str) -> str:
    """Runs of ASCII whitespace to one space, trimmed. U+00A0 is not whitespace here."""
    return re.sub(r"[ \t\r\n]+", " ", s).strip(" \t\r\n")


def vis(fragment: str) -> str:
    return ws(html.unescape(re.sub(r"<[^>]+>", "", fragment)))


def strict(fragment: str) -> str:
    """Like vis(), but an &nbsp; entity becomes ENT_MARK, not U+00A0, so it can be told from the character."""
    return ws(html.unescape(NBSP_ENTITY.sub(ENT_MARK, re.sub(r"<[^>]+>", "", fragment))))


def plain_inline(md: str) -> str:
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"\*\*(.+?)\*\*", r"\1", md)
    return md.replace("`", "")


def plain(md: str) -> str:
    """The copy's own text: list marker and Markdown marks removed."""
    return ws(plain_inline(re.sub(r"^(?:- |\d+\. )", "", md)))


def label(md: str) -> str:
    m = re.search(r"\*\*(.+?)\*\*", md)
    return m.group(1) if m else ""


def elements(fragment: str, tag: str, attrs: str = "") -> list:
    """Match objects for each <tag ...attrs...>inner</tag> (non-nested), inner as group 1."""
    return list(re.finditer(rf"<{tag}\b{attrs}[^>]*>(.*?)</{tag}>", fragment, re.S))


def main_of(page: str) -> tuple:
    """(offset, text) of the page's <main> element; (0, "") if there is none."""
    m = re.search(r"<main\b.*?</main>", page, re.S)
    return (m.start(), m.group(0)) if m else (0, "")


def md_lines(md: str) -> list:
    """(offset, line) for each line of a Markdown file."""
    out, at = [], 0
    for line in md.split("\n"):
        out.append((at, line))
        at += len(line) + 1
    return out


def rel(loc: str, page: str, ext: str) -> str:
    return f"{ROOTS[loc]}{PAGES[page]}index.{ext}"


def where(loc: str, page: str, ext: str) -> str:
    return f"{loc} /{PAGES[page]} {rel(loc, page, ext)}"


def load_old() -> dict:
    return json.loads(OLD_JSON.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the pieces, per page
# Each check returns its problems and records, in `holders`, where each piece sits:
# holders[(page, ext, key)] = (outer_start, outer_end, inner_start, inner_end), offsets in the page's text,
# the outer span being the whole element (html) or line (md), the inner span its content. --self-test plants
# its changes there, and the U+00A0 count reads the inner span.

def hold(holders: dict, page: str, ext: str, key: str, off: int, m) -> None:
    holders[(page, ext, key)] = (off + m.start(), off + m.end(), off + m.start(1), off + m.end(1))


def hold_line(holders: dict, page: str, ext: str, key: str, at: int, line: str) -> None:
    holders[(page, ext, key)] = (at, at + len(line), at, at + len(line))


def once_html(out: list, w: str, main: str, key: str, piece: str) -> None:
    n = vis(main).count(plain(piece))
    if n != 1:
        out.append(f"{w}: {key} is on the page {n} times, want 1")


def once_md(out: list, w: str, md: str, key: str, piece: str) -> None:
    n = ws(plain_inline(md)).count(plain(piece))
    if n != 1:
        out.append(f"{w}: {key} is in the twin {n} times, want 1")


def features_problems(loc: str, d: dict, old: dict, h: str, md: str, holders: dict) -> list:
    out, key = [], "features_other_last"
    want = plain(d[key])
    if h is None:
        out.append(f"{where(loc, 'features', 'html')}: missing")
    else:
        w = where(loc, "features", "html")
        off, main = main_of(h)
        hits = [m for m in re.finditer(r"<h3\b[^>]*>.*?</h3>\s*<p>(.*?)</p>", main, re.S)
                if "<code>.log</code>" in m.group(1)]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} paragraphs right after an h3 list <code>.log</code>, want 1")
        else:
            m = re.search(r"<p>(.*?)</p>$", hits[0].group(0), re.S)
            hold(holders, "features", "html", key, off + hits[0].start(), m)
            if not vis(m.group(1)).endswith(want):
                out.append(f"{w}: the \"Other files\" paragraph does not end with {key}")
        once_html(out, w, main, key, d[key])
    if md is None:
        out.append(f"{where(loc, 'features', 'md')}: missing")
    else:
        w = where(loc, "features", "md")
        lines = md_lines(md)
        hits = [lines[i + 2] for i in range(len(lines) - 2)
                if lines[i][1].startswith("### ") and lines[i + 1][1] == "" and "`.log`" in lines[i + 2][1]]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} paragraphs right after a ### heading list `.log`, want 1")
        else:
            hold_line(holders, "features", "md", key, *hits[0])
            if not plain(hits[0][1]).endswith(want):
                out.append(f"{w}: the \"Other files\" paragraph does not end with {key}")
        once_md(out, w, md, key, d[key])
    return out


def limits_problems(loc: str, d: dict, old: dict, h: str, md: str, holders: dict) -> list:
    out = []
    if h is None:
        out.append(f"{where(loc, 'limits', 'html')}: missing")
    else:
        w = where(loc, "limits", "html")
        off, main = main_of(h)
        lis = elements(main, "li")
        for key in ("limits_ios", "limits_other"):
            hits = [m for m in lis if vis(m.group(1)) == plain(d[key])]
            if len(hits) != 1:
                out.append(f"{w}: {len(hits)} list items equal {key}, want 1")
                continue
            hold(holders, "limits", "html", key, off, hits[0])
            strong = re.match(r"\s*<strong>(.*?)</strong>", hits[0].group(1), re.S)
            if not strong or vis(strong.group(1)) != ws(label(d[key])):
                out.append(f"{w}: the {key} item does not start with its bold label")
    if md is None:
        out.append(f"{where(loc, 'limits', 'md')}: missing")
    else:
        w = where(loc, "limits", "md")
        for key in ("limits_ios", "limits_other"):
            hits = [(at, line) for at, line in md_lines(md) if line.startswith("- ") and plain(line) == plain(d[key])]
            if len(hits) != 1:
                out.append(f"{w}: {len(hits)} list lines equal {key}, want 1")
                continue
            hold_line(holders, "limits", "md", key, *hits[0])
            if not hits[0][1].startswith(f"- **{label(d[key])}**"):
                out.append(f"{w}: the {key} line does not start with its bold label")
    return out


def vs_problems(loc: str, d: dict, old: dict, h: str, md: str, holders: dict) -> list:
    out, key = [], "vs_lacks_ios"
    want = plain(d[key])
    if h is None:
        out.append(f"{where(loc, 'vs', 'html')}: missing")
    else:
        w = where(loc, "vs", "html")
        off, main = main_of(h)
        hits = [m for m in elements(main, "p") if want in vis(m.group(1))]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} paragraphs hold {key}, want 1")
        else:
            hold(holders, "vs", "html", key, off, hits[0])
        once_html(out, w, main, key, d[key])
    if md is None:
        out.append(f"{where(loc, 'vs', 'md')}: missing")
    else:
        w = where(loc, "vs", "md")
        hits = [(at, line) for at, line in md_lines(md) if want in plain(line)]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} lines hold {key}, want 1")
        else:
            hold_line(holders, "vs", "md", key, *hits[0])
        once_md(out, w, md, key, d[key])
    return out


def payonce_problems(loc: str, d: dict, old: dict, h: str, md: str, holders: dict) -> list:
    out, key = [], "payonce_ios"
    want = plain(d[key])
    if h is None:
        out.append(f"{where(loc, 'pay-once', 'html')}: missing")
    else:
        w = where(loc, "pay-once", "html")
        off, main = main_of(h)
        hits = [m for m in elements(main, "li") if vis(m.group(1)).endswith(want)]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} list items end with {key}, want 1")
        else:
            hold(holders, "pay-once", "html", key, off, hits[0])
        once_html(out, w, main, key, d[key])
    if md is None:
        out.append(f"{where(loc, 'pay-once', 'md')}: missing")
    else:
        w = where(loc, "pay-once", "md")
        hits = [(at, line) for at, line in md_lines(md) if line.startswith("- ") and plain(line).endswith(want)]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} list lines end with {key}, want 1")
        else:
            hold_line(holders, "pay-once", "md", key, *hits[0])
        once_md(out, w, md, key, d[key])
    return out


def roadmap_problems(loc: str, d: dict, old: dict, h: str, md: str, holders: dict) -> list:
    out, key = [], "roadmap_updated"
    heads = old["headings"][loc]
    kept, callouts = old["kept"][loc], old["callouts"][loc]
    if h is None:
        out.append(f"{where(loc, 'roadmap', 'html')}: missing")
    else:
        w = where(loc, "roadmap", "html")
        off, main = main_of(h)
        hits = [m for m in elements(main, "p") if vis(m.group(1)) == plain(d[key])]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} paragraphs equal {key}, want 1")
        else:
            hold(holders, "roadmap", "html", key, off, hits[0])
        h3s = elements(main, "h3")
        texts = [vis(m.group(1)) for m in h3s]
        at = []
        for t in heads:
            n = texts.count(t)
            if n != 1:
                out.append(f"{w}: the heading {t!r} is there {n} times, want 1")
            else:
                at.append(texts.index(t))
        if len(at) == len(heads) and at != sorted(at):
            out.append(f"{w}: the four headings are not in order: {[texts[i] for i in sorted(at)]!r}")
        if texts.count(heads[0]) == 1:
            h3 = h3s[texts.index(heads[0])]
            ul = re.match(r"\s*<ul>(.*?)</ul>", main[h3.end():], re.S)
            items = [vis(m.group(1)) for m in elements(ul.group(1), "li")] if ul else None
            if items != [plain(kept)]:
                out.append(f"{w}: under {heads[0]!r} the bullets are {items!r}, want only the kept one")
        if plain(callouts) in vis(main):
            out.append(f"{w}: the Callouts bullet is on the page")
    if md is None:
        out.append(f"{where(loc, 'roadmap', 'md')}: missing")
    else:
        w = where(loc, "roadmap", "md")
        lines = md_lines(md)
        hits = [(a, line) for a, line in lines if plain(line) == plain(d[key])]
        if len(hits) != 1:
            out.append(f"{w}: {len(hits)} lines equal {key}, want 1")
        else:
            hold_line(holders, "roadmap", "md", key, *hits[0])
        texts = [line for _, line in lines]
        at = []
        for t in heads:
            n = texts.count("### " + t)
            if n != 1:
                out.append(f"{w}: the heading '### {t}' is there {n} times, want 1")
            else:
                at.append(texts.index("### " + t))
        if len(at) == len(heads) and at != sorted(at):
            out.append(f"{w}: the four headings are not in order")
        if texts.count("### " + heads[0]) == 1:
            i = texts.index("### " + heads[0]) + 1
            while i < len(texts) and texts[i] == "":
                i += 1
            items = []
            while i < len(texts) and texts[i].startswith("- "):
                items.append(texts[i])
                i += 1
            if items != [kept]:
                out.append(f"{w}: under '### {heads[0]}' the bullets are {items!r}, want only the kept one")
        if callouts in texts or plain(callouts) in ws(plain_inline(md)):
            out.append(f"{w}: the Callouts bullet is in the twin")
    return out


CHECKS = {"features": features_problems, "limits": limits_problems, "vs": vs_problems,
          "pay-once": payonce_problems, "roadmap": roadmap_problems}


def nbsp_problems(loc: str, d: dict, pages: dict, holders: dict) -> list:
    """Each piece's U+00A0, counted in the element or line that holds it: the character, not &nbsp; nor a space."""
    out = []
    for page, keys in ON_PAGE.items():
        for key in keys:
            want = plain(d[key])
            rx = "".join(f"([{NBSP}{ENT_MARK} ])" if c == NBSP else re.escape(c) for c in want)
            for ext in ("html", "md"):
                span = holders.get((page, ext, key))
                if span is None:
                    continue   # already reported: the piece is not where it belongs
                raw = pages[f"{page}.{ext}"][span[2]:span[3]]
                text = strict(raw) if ext == "html" else ws(plain_inline(NBSP_ENTITY.sub(ENT_MARK, raw)))
                w = where(loc, page, ext)
                m = re.search(rx, text)
                if not m:
                    if ENT_MARK in text or (loc in NBSP_WANT and NBSP_WANT[loc][key]):
                        out.append(f"{w}: {key} is not there with its U+00A0 as the character itself")
                    continue
                got = [m.group(i) for i in range(1, (m.lastindex or 0) + 1)]
                if got.count(ENT_MARK):
                    out.append(f"{w}: {key} has {got.count(ENT_MARK)} U+00A0 written as &nbsp;, want the character")
                if got.count(" "):
                    out.append(f"{w}: {key} has {got.count(' ')} plain spaces where the copy has U+00A0")
                if loc not in NBSP_WANT and (NBSP in m.group(0) or ENT_MARK in m.group(0)):
                    out.append(f"{w}: {key} carries a U+00A0, none expected in {loc}")
    return out


def data_problems(old: dict) -> list:
    out = []
    if set(data.DATA) != set(ROOTS):
        out.append(f"data: locales {sorted(data.DATA)} != {sorted(ROOTS)}")
    for loc in ROOTS:
        d = data.DATA.get(loc)
        if d is None:
            continue
        if sorted(d) != sorted(KEYS):
            out.append(f"{loc}: data keys {sorted(d)} != {sorted(KEYS)}")
        for key in KEYS:
            v = d.get(key)
            if not isinstance(v, str) or not v.strip():
                out.append(f"{loc}: data {key} is empty or not a string")
                continue
            want = NBSP_WANT.get(loc, {}).get(key, 0)
            if v.count(NBSP) != want:
                out.append(f"{loc}: data {key} has {v.count(NBSP)} U+00A0, want {want}")
    for part, size in (("old", 5), ("headings", 4)):
        for loc in ROOTS:
            v = old.get(part, {}).get(loc)
            if not isinstance(v, list) or len(v) != size or not all(isinstance(s, str) and s.strip() for s in v):
                out.append(f"old.json {part}/{loc}: want {size} non-empty strings")
    for part in ("callouts", "kept", "last_updated_before"):
        for loc in ROOTS:
            v = old.get(part, {}).get(loc)
            if not isinstance(v, str) or not v.strip():
                out.append(f"old.json {part}/{loc}: empty or missing")
    return out


def problems_for(loc: str, pages: dict, old: dict) -> list:
    d, out, holders = data.DATA[loc], [], {}
    for page, fn in CHECKS.items():
        out += fn(loc, d, old, pages.get(f"{page}.html"), pages.get(f"{page}.md"), holders)
    return out + nbsp_problems(loc, d, pages, holders) + faq_problems(loc, pages)


# ---------------------------------------------------------------- the home FAQ (#369's answer 3)

def faq_problems(loc: str, pages: dict) -> list:
    out, want = [], data369.DATA[loc]["faq"]
    h, md = pages.get("home.html"), pages.get("home.md")
    if h is None:
        out.append(f"{where(loc, 'home', 'html')}: missing")
    else:
        w = where(loc, "home", "html")
        sec = re.search(r'<section\b[^>]*class="faq"[^>]*>(.*?)</section>', h, re.S)
        h3s = elements(sec.group(1), "h3") if sec else []
        if len(h3s) < 3:
            out.append(f"{w}: the FAQ has fewer than 3 questions")
        else:
            pm = re.match(r"<p>(.*?)</p>", sec.group(1)[h3s[2].end():].lstrip(" \t\r\n"), re.S)
            if not pm or vis(pm.group(1)) != plain(want):
                out.append(f"{w}: FAQ answer 3 (visible) is not #369's")
            n = vis(sec.group(1)).count(plain(want))
            if n != 1:
                out.append(f"{w}: #369's FAQ answer is in the FAQ {n} times, want 1")
        entity = None
        for m in elements(h, "script", r'[^>]*type="application/ld\+json"'):
            if "FAQPage" in m.group(1):
                try:
                    entity = json.loads(m.group(1))["mainEntity"]
                except (ValueError, KeyError, TypeError) as e:
                    out.append(f"{w}: FAQPage JSON-LD unreadable: {e}")
                break
        else:
            out.append(f"{w}: no FAQPage JSON-LD")
        if entity is not None:
            try:
                answers = [q["acceptedAnswer"]["text"] for q in entity]
            except (KeyError, TypeError) as e:
                answers = []
                out.append(f"{w}: FAQPage JSON-LD has no answers: {e}")
            if answers[2:3] != [want]:
                out.append(f"{w}: FAQPage JSON-LD mainEntity[2] answer is not #369's")
            if answers.count(want) != 1:
                out.append(f"{w}: #369's FAQ answer is in the JSON-LD {answers.count(want)} times, want 1")
    if md is None:
        out.append(f"{where(loc, 'home', 'md')}: missing")
    else:
        n = sum(plain(line) == plain(want) for line in md.split("\n"))
        if n != 1:
            out.append(f"{where(loc, 'home', 'md')}: {n} lines equal #369's FAQ answer, want 1")
    return out


def llms_faq_problems(llms: str) -> list:
    if llms is None:
        return ["llms-full.txt: missing"]
    lines = [plain(line) for line in llms.split("\n")]
    return [f"{loc} llms-full.txt: {lines.count(plain(d['faq']))} lines equal #369's FAQ answer, want 1"
            for loc, d in data369.DATA.items() if lines.count(plain(d["faq"])) != 1]


def old_faq_answers() -> list:
    """(locale, answer) for each old iPhone-or-iPad home FAQ answer, HTML stripped."""
    out = []
    for loc in ROOTS:
        for q, a in promo_data.DATA["seo"][loc]["home_faq"]:
            if "iPhone" in q and "iPad" in q:
                out.append((loc, a))
        out.append((loc, promo_data.DATA["faq275"][loc]["q3"]))
    return [(loc, vis(a)) for loc, a in out]


# ---------------------------------------------------------------- old strings, anywhere under public/

def hay(s: str) -> str:
    return re.sub(r"[ \t\r\n]+", " ", NBSP_ENTITY.sub(" ", s).replace(NBSP, " "))


def json_strings(obj) -> list:
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, dict):
        return [s for v in obj.values() for s in json_strings(v)]
    if isinstance(obj, list):
        return [s for v in obj for s in json_strings(v)]
    return []


def needles(old: dict) -> list:
    out = []
    for loc in ROOTS:
        named = [(f"old[{i}]", s) for i, s in enumerate(old["old"][loc])]
        named += [("callouts", old["callouts"][loc]), ("last_updated_before", old["last_updated_before"][loc])]
        for name, s in named:
            for n in (hay(plain(s)).strip(" "), hay(re.sub(r"^- ", "", s)).strip(" ")):
                if n and (loc, name, n) not in out:
                    out.append((loc, name, n))
    for loc, a in old_faq_answers():
        n = hay(a).strip(" ")
        if n and (loc, "old FAQ answer", n) not in out:
            out.append((loc, "old FAQ answer", n))
    return out


def file_hays(name: str, text: str) -> list:
    stripped = html.unescape(re.sub(r"<[^>]+>", "", text))
    hays = [hay(text), hay(stripped), hay(plain_inline(stripped))]
    blobs = [text] if name.endswith(".json") else [m.group(1) for m in elements(text, "script", r'[^>]*type="application/ld\+json"')]
    for blob in blobs:
        try:
            hays.append(hay(" \n ".join(json_strings(json.loads(blob)))))
        except ValueError:
            pass
    return hays


def old_problems(old: dict, files: dict) -> list:
    """files: {name: text}. One line per file and old string found on it."""
    out, ns = [], needles(old)
    for name, text in files.items():
        hays = file_hays(name, text)
        seen = set()
        for loc, what, n in ns:
            if (loc, what) not in seen and any(n in h for h in hays):
                seen.add((loc, what))
                out.append(f"{name}: the old {loc} {what} is on it: {n[:60]!r}")
    return out


def site_files() -> dict:
    return {str(f.relative_to(SITE)): f.read_text(encoding="utf-8", errors="replace")
            for f in sorted(SITE.rglob("*")) if f.is_file() and f.suffix in SCAN_SUFFIXES}


# ---------------------------------------------------------------- pages not to be touched

def untouched_files() -> list:
    return [f"{ROOTS[loc]}{sub}index.{ext}" for loc in ROOTS for sub in UNTOUCHED for ext in ("html", "md")]


def read_bytes(root: Path) -> dict:
    """{name: bytes or None} for each file that must not change, under root."""
    return {name: (root / name).read_bytes() if (root / name).is_file() else None for name in untouched_files()}


def against_problems(site: dict, ref: dict, ref_name: str) -> list:
    out = []
    for name in untouched_files():
        a, b = site.get(name), ref.get(name)
        if a is None or b is None:
            out.append(f"{name}: missing in {'public/' if a is None else ref_name}")
        elif a != b:
            out.append(f"{name}: differs from the same file in {ref_name}")
    return out


# ---------------------------------------------------------------- run

def read_pages(loc: str) -> dict:
    out = {}
    for page in PAGES:
        for ext in ("html", "md"):
            f = SITE / rel(loc, page, ext)
            out[f"{page}.{ext}"] = f.read_text(encoding="utf-8") if f.is_file() else None
    return out


def read_llms() -> str:
    f = SITE / "llms-full.txt"
    return f.read_text(encoding="utf-8") if f.is_file() else None


def check(against: Path = None) -> list:
    old = load_old()
    out = data_problems(old)
    if out:
        return out
    for loc in ROOTS:
        out += problems_for(loc, read_pages(loc), old)
    out += llms_faq_problems(read_llms())
    out += old_problems(old, site_files())
    if against is not None:
        out += against_problems(read_bytes(SITE), read_bytes(against), str(against))
    return out


ESCAPABLE = set("&<>'\"")


def segments(piece: str) -> list:
    """The piece's runs of text between Markdown marks (so none straddles a tag on the page)."""
    raw = re.sub(r"^(?:- |\d+\. )", "", piece)
    return [s for s in re.split(r"\*\*|`|\[|\]\([^)]*\)", raw) if s.strip()]


def piece_spans(text: str, start: int, end: int, piece: str) -> list:
    """Where each of the piece's segments sits in text[start:end], in order; None if one is not there raw."""
    out, at = [], start
    for seg in segments(piece):
        i = text.find(seg.strip(" "), at, end)
        if i < 0:
            return None
        out.append((i, i + len(seg.strip(" "))))
        at = out[-1][1]
    return out


def self_test() -> int:
    old = load_old()
    caught = missed = 0
    if data_problems(old):
        print("self-test: baseline not clean: " + "; ".join(data_problems(old)))
        return 1
    all_pages = {loc: read_pages(loc) for loc in ROOTS}
    feats = all_pages["en"]["features.html"] or ""
    llms = read_llms() or ""
    base = {"features/index.html": feats, "llms-full.txt": llms}
    baseline = [p for loc in ROOTS for p in problems_for(loc, all_pages[loc], old)]
    baseline += llms_faq_problems(read_llms()) + old_problems(old, base)
    if baseline:
        print(f"self-test: baseline not clean: {len(baseline)} problems on the unplanted copies, so no plant is tried:")
        for p in baseline:
            print("  " + p)
        return 1

    def expect(what: str, problems: list) -> None:
        nonlocal caught, missed
        if problems:
            caught += 1
        else:
            print(f"self-test: {what} was NOT caught")
            missed += 1

    def cant(what: str) -> None:
        nonlocal missed
        print(f"self-test: {what}: the plant can't be made")
        missed += 1

    for loc in ROOTS:
        pages, d = all_pages[loc], data.DATA[loc]
        holders = {}
        for page, fn in CHECKS.items():
            fn(loc, d, old, pages[f"{page}.html"], pages[f"{page}.md"], holders)

        def run(page: str, ext: str, text: str) -> list:
            return problems_for(loc, {**pages, f"{page}.{ext}": text}, old)

        for page, keys in ON_PAGE.items():
            for key in keys:
                for ext in ("html", "md"):
                    text, span = pages[f"{page}.{ext}"], holders.get((page, ext, key))
                    spans = piece_spans(text, span[2], span[3], d[key]) if span else None
                    w = f"{loc}/{page}.{ext} {key}"
                    if not spans:
                        cant(w)
                        continue
                    # one character changed, in the middle of the piece's longest run of text
                    s, e = max(spans, key=lambda x: x[1] - x[0])
                    mid = (s + e) // 2
                    while text[mid] in ESCAPABLE | {NBSP, " "} and mid + 1 < e:
                        mid += 1
                    expect(f"{w}: one character changed",
                           run(page, ext, text[:mid] + ("X" if text[mid] != "X" else "Y") + text[mid + 1:]))
                    # emptied: every run of the piece removed
                    emptied = text
                    for a, b in reversed(spans):
                        emptied = emptied[:a] + emptied[b:]
                    expect(f"{w}: emptied", run(page, ext, emptied))
                    # duplicated: the element or line that holds it, twice
                    o1 = span[1]
                    expect(f"{w}: duplicated", run(page, ext, text[:o1] + "\n" + text[span[0]:o1] + text[o1:]))
                    # fr's U+00A0 as a space and as &nbsp;
                    n = sum(text[a:b].count(NBSP) for a, b in spans)
                    if NBSP_WANT.get(loc, {}).get(key):
                        if n != NBSP_WANT[loc][key]:
                            cant(f"{w}: U+00A0 ({n} found)")
                            continue
                        for name, repl in (("a plain space", " "), ("&nbsp;", "&nbsp;")):
                            planted = text
                            for a, b in reversed(spans):
                                planted = planted[:a] + planted[a:b].replace(NBSP, repl) + planted[b:]
                            expect(f"{w}: U+00A0 as {name}", run(page, ext, planted))
                            a, b = spans[[i for i, (x, y) in enumerate(spans) if NBSP in text[x:y]][0]]
                            i = text.index(NBSP, a, b)
                            expect(f"{w}: one U+00A0 as {name}", run(page, ext, text[:i] + repl + text[i + 1:]))

        # /roadmap/: the Callouts bullet back, the Plans bullet removed, two headings swapped, old date back
        heads, kept, callouts = old["headings"][loc], old["kept"][loc], old["callouts"][loc]
        rh, rm = pages["roadmap.html"], pages["roadmap.md"]
        callouts_li = "  <li>" + html.escape(callouts[2:], quote=False).replace("**", "") + "</li>\n"
        callouts_li = re.sub(r"`([^`]+)`", r"<code>\1</code>", callouts_li)
        opening = f"<h3>{html.escape(heads[0], quote=False)}</h3>\n<ul>\n"
        if opening in rh:
            expect(f"{loc}/roadmap.html: Callouts bullet back", run("roadmap", "html", rh.replace(opening, opening + callouts_li, 1)))
        else:
            cant(f"{loc}/roadmap.html: Callouts bullet back")
        md_opening = f"### {heads[0]}\n\n"
        if md_opening in rm:
            expect(f"{loc}/roadmap.md: Callouts bullet back", run("roadmap", "md", rm.replace(md_opening, md_opening + callouts + "\n", 1)))
        else:
            cant(f"{loc}/roadmap.md: Callouts bullet back")
        kept_li = next((m.group(0) for m in elements(rh, "li") if vis(m.group(1)) == plain(kept)), None)
        if kept_li:
            expect(f"{loc}/roadmap.html: Plans bullet removed", run("roadmap", "html", rh.replace(kept_li, "", 1)))
        else:
            cant(f"{loc}/roadmap.html: Plans bullet removed")
        if kept + "\n" in rm:
            expect(f"{loc}/roadmap.md: Plans bullet removed", run("roadmap", "md", rm.replace(kept + "\n", "", 1)))
        else:
            cant(f"{loc}/roadmap.md: Plans bullet removed")
        for ext, fmt in (("html", "<h3>{}</h3>"), ("md", "### {}\n")):
            text = pages[f"roadmap.{ext}"]
            a, b = fmt.format(html.escape(heads[1], quote=False) if ext == "html" else heads[1]), \
                fmt.format(html.escape(heads[2], quote=False) if ext == "html" else heads[2])
            if a in text and b in text:
                expect(f"{loc}/roadmap.{ext}: headings 2 and 3 swapped",
                       run("roadmap", ext, text.replace(a, "\0", 1).replace(b, a, 1).replace("\0", b, 1)))
            else:
                cant(f"{loc}/roadmap.{ext}: headings swapped")
            span = holders.get(("roadmap", ext, "roadmap_updated"))
            if span:
                back = text[:span[2]] + html.escape(old["last_updated_before"][loc], quote=False) + text[span[3]:]
                expect(f"{loc}/roadmap.{ext}: old Last-updated line back", run("roadmap", ext, back))
                expect(f"{loc}/roadmap.{ext}: old Last-updated line back, site-wide search",
                       old_problems(old, {rel(loc, "roadmap", ext): back}))
            else:
                cant(f"{loc}/roadmap.{ext}: old Last-updated line back")

        # the home FAQ answer: changed (visible, JSON-LD, twin) and duplicated
        want = data369.DATA[loc]["faq"]
        hh, hm = pages["home.html"], pages["home.md"]
        sec = re.search(r'<section\b[^>]*class="faq"[^>]*>.*?</section>', hh, re.S)
        vis_at = hh.find(want[:30], sec.start(), sec.end()) if sec else -1
        script = hh.find('"FAQPage"')
        json_at = hh.find(json.dumps(want, ensure_ascii=False)[1:31], script) if script >= 0 else -1
        for what, at in (("visible", vis_at), ("JSON-LD", json_at)):
            if at < 0:
                cant(f"{loc}/home.html: FAQ answer {what} changed")
                continue
            i = at + 15
            expect(f"{loc}/home.html: FAQ answer {what} changed",
                   run("home", "html", hh[:i] + ("X" if hh[i] != "X" else "Y") + hh[i + 1:]))
        pm = re.search(r"<p>[^<]*" + re.escape(want[:30]) + r".*?</p>", sec.group(0), re.S) if sec else None
        if pm:
            i = sec.start() + pm.end()
            expect(f"{loc}/home.html: FAQ answer duplicated", run("home", "html", hh[:i] + "\n" + pm.group(0) + hh[i:]))
        else:
            cant(f"{loc}/home.html: FAQ answer duplicated")
        line = next((x for x in hm.split("\n") if plain(x) == plain(want)), None)
        if line:
            i = len(line) // 2
            expect(f"{loc}/home.md: FAQ answer changed", run("home", "md", hm.replace(line, line[:i] + "X" + line[i + 1:], 1)))
            expect(f"{loc}/home.md: FAQ answer duplicated", run("home", "md", hm.replace(line, line + "\n\n" + line, 1)))
        else:
            cant(f"{loc}/home.md: FAQ answer")
        line = next((x for x in llms.split("\n") if plain(x) == plain(want)), None)
        if line:
            expect(f"llms-full.txt: {loc} FAQ answer changed", llms_faq_problems(llms.replace(line, line[:-3] + "X" + line[-2:], 1)))
            expect(f"llms-full.txt: {loc} FAQ answer duplicated", llms_faq_problems(llms.replace(line, line + "\n" + line, 1)))
        else:
            cant(f"llms-full.txt: {loc} FAQ answer")

    # old strings planted into copies of en /features/ and llms-full.txt
    plants = [(loc, f"old[{i}]", s) for loc in ROOTS for i, s in enumerate(old["old"][loc])]
    plants += [(loc, k, old[k][loc]) for loc in ROOTS for k in ("callouts", "last_updated_before")]
    plants += [(loc, "old FAQ answer", a) for loc, a in old_faq_answers()]
    for loc, what, s in plants:
        p = plain(s)
        words = p.replace(NBSP, " ").split(" ")
        wrapped = " ".join(words[:2] + [f"<strong>{words[2]}</strong>"] + words[3:]) if len(words) > 3 \
            else f"<em>{p[:len(p) // 2]}</em>{p[len(p) // 2:]}"
        variants = {"whole": s, "NBSP-spaced": " ".join(words).replace(" ", NBSP),
                    "&nbsp;-spaced": " ".join(words).replace(" ", "&nbsp;"), "tag-wrapped": wrapped}
        for vname, v in variants.items():
            for fname, text in base.items():
                planted = text.replace("</main>", f"<p>{v}</p></main>", 1) if fname.endswith(".html") else text + "\n" + v + "\n"
                if planted == text:
                    cant(f"{fname}: {loc} {what}")
                    continue
                expect(f"{loc} {what} ({vname}) in {fname}", old_problems(old, {**base, fname: planted}))

    # --against: public/'s own bytes against a copy of them, clean, then with one byte changed or a file gone
    mine = read_bytes(SITE)
    if any(b is None for b in mine.values()):
        cant("--against: a file that must not change is missing in public/")
    else:
        same = against_problems(mine, dict(mine), "the copy")
        if same:
            print("self-test: --against: public/ against its own copy: " + "; ".join(same))
            missed += 1
        for name in (untouched_files()[0], untouched_files()[-1]):
            b = mine[name]
            expect(f"{name}: a byte changed (--against)",
                   against_problems(mine, {**mine, name: b[:-1] + bytes([b[-1] ^ 1])}, "the copy"))
            expect(f"{name}: missing in the reference (--against)", against_problems(mine, {**mine, name: None}, "the copy"))
    print(f"self-test: unplanted copies clean; {caught} plants caught, {missed} missed")
    return 1 if missed or not caught else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--against", "--base-dir", dest="against", metavar="REF_DIR", type=Path,
                    help="a second public tree; native/ and vs/macmd-viewer/ must equal it byte for byte")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.against is not None and not args.against.is_dir():
        print(f"--against: {args.against} is not a folder")
        return 1
    problems = check(args.against)
    for p in problems:
        print(p)
    if problems:
        print(f"{len(problems)} problems")
        return 1
    print(f"ok: #363 copy present and verbatim in {len(ROOTS)} locales (6 pieces each, html and md); "
          f"no old string on any file under public/; #369's FAQ answer in place"
          + ("; native/ and vs/macmd-viewer/ unchanged" if args.against else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
