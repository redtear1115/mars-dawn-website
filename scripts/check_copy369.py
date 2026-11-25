#!/usr/bin/env python3
"""Checks that the built home, /features/, /pdf/ and /markdown-to-pdf/ carry website #369's copy, verbatim.

scripts/copy369/data.py holds Aria's copy about the new iOS and print features: DATA[locale] has the 11
pieces that ship, HELD[locale] the 2 that must not. This reads the built public/ files, not build_pages.py,
and fails unless every locale's pages hold each shipped piece in full and in its place:

- home: the three #iphone-steps steps and the limit line under them, and the FAQ's third answer, both
  as visible text and as the FAQPage JSON-LD's mainEntity[2] answer;
- /features/: the fold heading and paragraph as the page's third <h3>, the export paragraph followed by
  its /pdf/ link and the figure, devices steps 2 and 3 with their bold labels, and the devnote;
- /pdf/: the last bullet of the page's first list;
- /markdown-to-pdf/: the --layout bullet right after --paper, and the first bullet under the last h2;
- each page's Markdown twin (index.md) with the same lines, in the same order;
- the HELD pieces on no file under public/ (.html, .md, .txt, .json), whole or by their first sentence,
  even with tags or non-breaking spaces in between;
- de and fr's U+00A0 (5 and 15 over the 13 values, shipped and held, as copy369/ingest.py counts them;
  none elsewhere) still on the pages that carry the shipped ones.

Pieces are compared as visible text: tags stripped, entities decoded, runs of ASCII whitespace collapsed
(U+00A0 kept as it is), against the copy with only its Markdown marks and list marker removed. Never
against the build's own rendering, which would share any mistake the build makes.

--self-test changes one character of each piece in a copy of each built page and its twin, swaps the
--layout and --paper bullets and two home steps, plants HELD strings (whole, first sentence, NBSP-spaced,
tag-wrapped) into a copy of /features/ and llms-full.txt, empties a HELD string, and turns de and fr's
U+00A0 into spaces, and fails unless every change is caught.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from copy369 import data  # noqa: E402

SITE = HERE.parent / "public"
ROOTS = {"en": "", "zh-hant": "zh-hant/", "zh-hans": "zh-hans/", "ja": "ja/", "de": "de/", "fr": "fr/",
         "es": "es/", "ko": "ko/"}
PAGES = {"home": "", "features": "features/", "pdf": "pdf/", "markdown-to-pdf": "markdown-to-pdf/"}
KEYS = ["home_ios", "faq", "fold_h", "fold", "export", "ios_s2", "ios_s3", "devnote", "pdf", "layout", "next"]
ON_PAGE = {"home": ["home_ios", "faq"], "features": ["fold_h", "fold", "export", "ios_s2", "ios_s3", "devnote"],
           "pdf": ["pdf"], "markdown-to-pdf": ["layout", "next"]}
HELD_KEYS = {"plan4", "outline_plus"}
NBSP = " "
NBSP_WANT = {"de": 5, "fr": 15}
HELD_SUFFIXES = {".html", ".md", ".txt", ".json"}


def ws(s: str) -> str:
    """Runs of ASCII whitespace to one space, trimmed. U+00A0 is not whitespace here."""
    return re.sub(r"[ \t\r\n]+", " ", s).strip(" \t\r\n")


def vis(fragment: str) -> str:
    return ws(html.unescape(re.sub(r"<[^>]+>", "", fragment)))


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


def home_steps(d: dict) -> tuple:
    steps, _, limit = d["home_ios"].partition("\n\n")
    return steps.split("\n"), limit.strip()


def elements(fragment: str, tag: str, attrs: str = "") -> list:
    """Match objects for each <tag ...attrs...>inner</tag> (non-nested), inner as group 1."""
    return list(re.finditer(rf"<{tag}\b{attrs}[^>]*>(.*?)</{tag}>", fragment, re.S))


def after(page: str, m) -> str:
    return page[m.end():].lstrip(" \t\r\n")


def main_of(page: str) -> str:
    m = re.search(r"<main\b.*?</main>", page, re.S)
    return m.group(0) if m else ""


# ---------------------------------------------------------------- shipped pieces, per page

def home_problems(loc: str, d: dict, h: str, md: str) -> list:
    out, p = [], f"{loc}/home"
    steps, limit = home_steps(d)
    want = [plain(s) for s in steps]
    if h is None:
        out.append(f"{p}: index.html missing")
    else:
        sec = re.search(r'<section\b[^>]*\bid="iphone-steps"[^>]*>(.*?)</section>', h, re.S)
        if not sec:
            out.append(f"{p}: no section#iphone-steps")
        else:
            ol = elements(sec.group(1), "ol")
            got = [vis(m.group(1)) for m in elements(ol[0].group(1), "li")] if ol else []
            if got != want:
                out.append(f"{p}: #iphone-steps steps differ: {got!r}")
            lim = elements(sec.group(1), "p", r'[^>]*class="iphone-steps-limit"')
            if len(lim) != 1 or vis(lim[0].group(1)) != plain(limit):
                out.append(f"{p}: #iphone-steps limit line differs or is missing")
        faq_sec = re.search(r'<section\b[^>]*class="faq"[^>]*>(.*?)</section>', h, re.S)
        h3s = elements(faq_sec.group(1), "h3") if faq_sec else []
        seen = None
        if len(h3s) < 3:
            out.append(f"{p}: FAQ has fewer than 3 questions")
        else:
            nxt = after(faq_sec.group(1), h3s[2])
            pm = re.match(r"<p>(.*?)</p>", nxt, re.S)
            seen = vis(pm.group(1)) if pm else None
            if seen != plain(d["faq"]):
                out.append(f"{p}: FAQ answer 3 (visible) differs")
        jtext = None
        for m in elements(h, "script", r'[^>]*type="application/ld\+json"'):
            if "FAQPage" not in m.group(1):
                continue
            try:
                jtext = json.loads(m.group(1))["mainEntity"][2]["acceptedAnswer"]["text"]
            except (ValueError, KeyError, IndexError, TypeError) as e:
                out.append(f"{p}: FAQPage JSON-LD unreadable: {e}")
            break
        else:
            out.append(f"{p}: no FAQPage JSON-LD")
        if jtext is not None and jtext != d["faq"]:
            out.append(f"{p}: FAQPage JSON-LD answer 3 differs")
        if seen is not None and jtext is not None and seen != ws(jtext):
            out.append(f"{p}: FAQ answer 3 visible text and JSON-LD disagree")
    if md is None:
        out.append(f"{p}: index.md missing")
    else:
        lines = md.split("\n")
        ok = False
        for i in range(len(lines) - 4):
            if all(lines[i + k].startswith(f"{k + 1}. ") and plain(lines[i + k]) == want[k] for k in range(3)):
                ok = lines[i + 3] == "" and plain(lines[i + 4]) == plain(limit)
                break
        if not ok:
            out.append(f"{p}/md: the three steps and the limit line are not there, in order")
        if not any(plain(line) == plain(d["faq"]) for line in lines):
            out.append(f"{p}/md: FAQ answer 3 missing")
    return out


def features_problems(loc: str, d: dict, h: str, md: str) -> list:
    out, p = [], f"{loc}/features"
    if h is None:
        out.append(f"{p}: index.html missing")
    else:
        h3s = elements(h, "h3")
        if len(h3s) < 3 or vis(h3s[2].group(1)) != plain(d["fold_h"]):
            out.append(f"{p}: the fold heading is not the page's 3rd <h3>")
        else:
            pm = re.match(r"<p>(.*?)</p>", after(h, h3s[2]), re.S)
            if not pm or vis(pm.group(1)) != plain(d["fold"]):
                out.append(f"{p}: the fold paragraph is not right after its heading, or differs")
        exp = [m for m in elements(h, "p") if m.group(0).startswith("<p>") and vis(m.group(1)) == plain(d["export"])]
        if len(exp) != 1:
            out.append(f"{p}: {len(exp)} paragraphs equal the export copy, want 1")
        else:
            rest = after(h, exp[0])
            more = re.match(r'<p class="more">(.*?)</p>', rest, re.S)
            hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"', more.group(1)) if more else []
            if not more or not any(x.endswith("/pdf/") for x in hrefs):
                out.append(f"{p}: the export paragraph is not followed by its /pdf/ link")
            elif not after(rest, more).startswith("<figure"):
                out.append(f"{p}: the export paragraph's link is not followed by the figure")
        ol = elements(h, "ol", r'[^>]*class="devsteps"')
        lis = elements(ol[0].group(1), "li") if ol else []
        for n, key in ((1, "ios_s2"), (2, "ios_s3")):
            li = lis[n].group(1) if len(lis) > n else None
            strong = re.match(r"\s*<strong>(.*?)</strong>", li or "", re.S)
            if li is None or vis(li) != plain(d[key]):
                out.append(f"{p}: devices step {n + 1} differs or is missing")
            elif not strong or vis(strong.group(1)) != ws(label(d[key])):
                out.append(f"{p}: devices step {n + 1} does not start with its bold label")
        dn = elements(h, "p", r'[^>]*class="devnote"')
        if len(dn) != 1 or vis(dn[0].group(1)) != plain(d["devnote"]):
            out.append(f"{p}: devnote differs or is missing")
    if md is None:
        out.append(f"{p}: index.md missing")
    else:
        lines = md.split("\n")
        i = next((i for i, line in enumerate(lines) if line == "### " + d["fold_h"]), None)
        if i is None or lines[i + 1:i + 2] != [""] or plain(lines[i + 2] if i + 2 < len(lines) else "") != plain(d["fold"]):
            out.append(f"{p}/md: the fold heading and its paragraph are not there")
        for key, num in (("export", None), ("ios_s2", "2. "), ("ios_s3", "3. "), ("devnote", None)):
            want = plain(d[key])
            hit = [line for line in lines if plain(line) == want and (num is None or line.startswith(num))]
            if num and hit and f"**{label(d[key])}**" not in hit[0]:
                hit = []
            if not hit:
                out.append(f"{p}/md: {key} line missing")
    return out


def pdf_problems(loc: str, d: dict, h: str, md: str) -> list:
    out, p = [], f"{loc}/pdf"
    if h is None:
        out.append(f"{p}: index.html missing")
    else:
        ul = elements(main_of(h), "ul")
        lis = elements(ul[0].group(1), "li") if ul else []
        if not lis or vis(lis[-1].group(1)) != plain(d["pdf"]):
            out.append(f"{p}: the last bullet of the first list differs")
    if md is None:
        out.append(f"{p}: index.md missing")
    else:
        lines, run = md.split("\n"), []
        for line in lines:
            if line.startswith("- "):
                run.append(line)
            elif run:
                break
        if not run or plain(run[-1]) != plain(d["pdf"]):
            out.append(f"{p}/md: the last bullet of the first list differs")
    return out


def m2p_problems(loc: str, d: dict, h: str, md: str) -> list:
    out, p = [], f"{loc}/markdown-to-pdf"
    url = re.search(r"\]\(([^)]+)\)", d["next"])
    h2_text = None
    if h is None:
        out.append(f"{p}: index.html missing")
    else:
        main = main_of(h)
        paper = next((m for m in elements(main, "li") if m.group(1).startswith("<code>--paper</code>")), None)
        nxt = re.match(r"<li>(.*?)</li>", after(main, paper), re.S) if paper else None
        if not nxt or vis(nxt.group(1)) != plain(d["layout"]) or "<code>--layout</code>" not in nxt.group(1):
            out.append(f"{p}: the bullet right after --paper is not the --layout copy")
        h2s = elements(main, "h2")
        if not h2s:
            out.append(f"{p}: no <h2> in <main>")
        else:
            h2_text = vis(h2s[-1].group(1))
            ul = re.search(r"<ul>(.*?)</ul>", main[h2s[-1].end():], re.S)
            first = elements(ul.group(1), "li")[:1] if ul else []
            if not first or vis(first[0].group(1)) != plain(d["next"]):
                out.append(f"{p}: the first bullet under the last h2 differs")
            elif not url or url.group(1) not in [html.unescape(x) for x in re.findall(r'href="([^"]*)"', first[0].group(1))]:
                out.append(f"{p}: the first bullet under the last h2 does not link to the copy's URL")
    if md is None:
        out.append(f"{p}: index.md missing")
    else:
        lines = md.split("\n")
        i = next((i for i, line in enumerate(lines) if line.startswith("- `--paper`")), None)
        if i is None or i + 1 >= len(lines) or not lines[i + 1].startswith("- ") or plain(lines[i + 1]) != plain(d["layout"]):
            out.append(f"{p}/md: the line right after --paper is not the --layout copy")
        # The twin ends in a site-wide "## Plus" link list, so the section is found by the html's last h2.
        j = next((j for j, line in enumerate(lines) if h2_text and line == "## " + h2_text), None)
        first = next((line for line in lines[j + 1:] if line.startswith("- ")), None) if j is not None else None
        if first is None or plain(first) != plain(d["next"]) or (url and f"]({url.group(1)})" not in first):
            out.append(f"{p}/md: the first bullet under '## {h2_text}' differs")
    return out


CHECKS = {"home": home_problems, "features": features_problems, "pdf": pdf_problems, "markdown-to-pdf": m2p_problems}


def nbsp_problems(loc: str, d: dict, pages: dict) -> list:
    out = []
    for page, keys in ON_PAGE.items():
        need = sum(d[k].count(NBSP) for k in keys)
        if loc not in NBSP_WANT:
            continue
        for ext in ("html", "md"):
            text = pages.get(f"{page}.{ext}")
            if text is None:
                continue
            have = html.unescape(text).count(NBSP) if ext == "html" else text.count(NBSP)
            if have < need:
                out.append(f"{loc}/{page}{'/md' if ext == 'md' else ''}: {have} U+00A0 on the page, the copy on it carries {need}")
    return out


def data_problems() -> list:
    out = []
    for loc in ROOTS:
        d = data.DATA.get(loc)
        if d is None:
            out.append(f"{loc}: no #369 copy in scripts/copy369/data.py")
            continue
        missing = [k for k in KEYS if not isinstance(d.get(k), str) or not d[k].strip()]
        if missing:
            out.append(f"{loc}: data lacks {missing}")
    return out


def problems_for(loc: str, pages: dict) -> list:
    d, out = data.DATA[loc], []
    for page, fn in CHECKS.items():
        out += fn(loc, d, pages.get(f"{page}.html"), pages.get(f"{page}.md"))
    return out + nbsp_problems(loc, d, pages)


# ---------------------------------------------------------------- HELD

def hay(s: str) -> str:
    return re.sub(r"[ \t\r\n]+", " ", s.replace("&nbsp;", " ").replace(NBSP, " "))


def first_sentence(s: str) -> str:
    for m in re.finditer(r"\.(?=\s|$)|。", s):
        if m.end() >= 20:
            return s[:m.end()]
    return s[:40]


def held_needles(s: str) -> list:
    out = []
    for n in (s, plain(s), first_sentence(plain(s)), first_sentence(s)):
        n = hay(n).strip(" ")
        if n and n not in out:
            out.append(n)
    return out


def held_problems(held: dict, files: dict) -> list:
    """files: {name: text}. HELD must name the 8 locales, each with exactly plan4 and outline_plus, non-empty."""
    out = []
    if set(held) != set(ROOTS):
        out.append(f"HELD: locales {sorted(held)} != {sorted(ROOTS)}")
    needles = []
    for loc, pieces in held.items():
        if set(pieces) != HELD_KEYS:
            out.append(f"HELD/{loc}: keys {sorted(pieces)} != {sorted(HELD_KEYS)}")
        for key, s in pieces.items():
            if not isinstance(s, str) or not s.strip():
                out.append(f"HELD/{loc}/{key}: empty, so the search would find nothing")
                continue
            needles += [(loc, key, n) for n in held_needles(s)]
    # The data's own rule (copy369/ingest.py NBSP) counts U+00A0 over all 13 values, shipped and held.
    for loc in ROOTS:
        n = sum(v.count(NBSP) for v in list(data.DATA.get(loc, {}).values()) + list(held.get(loc, {}).values())
                if isinstance(v, str))
        if n != NBSP_WANT.get(loc, 0):
            out.append(f"{loc}: data has {n} U+00A0 over its 13 values, want {NBSP_WANT.get(loc, 0)}")
    for name, text in files.items():
        # Raw (JSON-LD, Markdown) and with tags stripped and entities decoded; Markdown and llms*.txt can
        # carry inline html too, so every suffix gets both.
        hays = [hay(text), hay(html.unescape(re.sub(r"<[^>]+>", "", text)))]
        for loc, key, n in needles:
            if any(n in h for h in hays):
                out.append(f"{name}: HELD {loc}/{key} is on it: {n[:50]!r}")
                break
    return out


def site_files() -> dict:
    return {str(f.relative_to(SITE)): f.read_text(encoding="utf-8", errors="replace")
            for f in sorted(SITE.rglob("*")) if f.is_file() and f.suffix in HELD_SUFFIXES}


# ---------------------------------------------------------------- run

def read_pages(loc: str) -> dict:
    out = {}
    for page, sub in PAGES.items():
        for ext in ("html", "md"):
            f = SITE / ROOTS[loc] / sub / f"index.{ext}"
            out[f"{page}.{ext}"] = f.read_text(encoding="utf-8") if f.is_file() else None
    return out


def check() -> list:
    out = data_problems()
    for loc in ROOTS:
        if loc in data.DATA and not any(p.startswith(f"{loc}: data lacks") for p in out):
            out += problems_for(loc, read_pages(loc))
    return out + held_problems(data.HELD, site_files())


ESCAPABLE = set("&<>'\"")


def segments(piece: str) -> list:
    """The piece's runs of text between Markdown marks (so none straddles a tag on the page)."""
    raw = re.sub(r"^(?:- |\d+\. )", "", piece)
    return [s for s in re.split(r"\*\*|`|\[|\]\([^)]*\)", raw) if s]


def window(seg: str, k: int, side: int) -> str:
    """seg[k] with up to `side` characters each side, stopping at characters html would escape."""
    a = b = k
    while a > 0 and k - a < side and seg[a - 1] not in ESCAPABLE:
        a -= 1
    while b + 1 < len(seg) and b - k < side and seg[b + 1] not in ESCAPABLE:
        b += 1
    return seg[a:b + 1]


def chunk(piece: str) -> str:
    """Up to 11 characters from the middle of the piece's longest unmarked run, none that html escapes."""
    seg = max(segments(piece), key=len)
    mid = len(seg) // 2
    while seg[mid] in ESCAPABLE | {NBSP} and mid + 1 < len(seg):
        mid += 1
    return window(seg, mid, 5)


def is_the_piece(text: str, s: int, ext: str, piece: str, key: str) -> bool:
    """Whether position s lies in the element (html) or line (md) that holds the piece itself, or, for the
    FAQ answer, in the FAQPage JSON-LD. Plants elsewhere (a heading's words in a menu) prove nothing."""
    if ext == "md":
        line = text[text.rfind("\n", 0, s) + 1:text.find("\n", s) if text.find("\n", s) >= 0 else len(text)]
        return plain(line.removeprefix("### ")) == plain(piece)
    script = text.rfind("<script", 0, s)
    if key == "faq" and script > text.rfind("</script>", 0, s) and "FAQPage" in text[script:s]:
        return True
    opens = list(re.finditer(r"<(p|li|h3)\b[^>]*>", text[:s]))
    if not opens:
        return False
    o = opens[-1]
    close = text.find(f"</{o.group(1)}>", s)
    return close >= 0 and vis(text[o.end():close]) == plain(piece)


def piece_spots(text: str, ext: str, piece: str, key: str, needle: str) -> list:
    return [m.start() for m in re.finditer(re.escape(needle), text or "") if is_the_piece(text, m.start(), ext, piece, key)]


def self_test() -> int:
    caught = missed = 0

    def expect(what: str, problems: list) -> None:
        nonlocal caught, missed
        if problems:
            caught += 1
        else:
            print(f"self-test: {what} was NOT caught")
            missed += 1

    for loc in data.DATA:
        pages, d = read_pages(loc), data.DATA[loc]
        if problems_for(loc, pages):
            print(f"self-test: {loc}: the built pages already have problems; plants there prove little")
        # (a) one character changed, at each place the piece itself sits (the FAQ answer: visible and JSON-LD)
        for page, keys in ON_PAGE.items():
            for key in keys:
                piece = home_steps(d)[0][0] if key == "home_ios" else d[key]
                for ext in ("html", "md"):
                    text = pages[f"{page}.{ext}"]
                    c = chunk(piece)
                    starts = piece_spots(text, ext, piece, key, c)
                    want = 2 if (key, ext) == ("faq", "html") else 1
                    if len(starts) < want:
                        print(f"self-test: {loc}/{page}.{ext}: {key}'s piece is on the page {len(starts)} times, want {want}")
                        missed += 1
                        continue
                    for s in starts:
                        mid = s + len(c) // 2
                        changed = text[:mid] + ("X" if text[mid] != "X" else "Y") + text[mid + 1:]
                        expect(f"{loc}/{page}.{ext}: a change in {key} at {s}",
                               problems_for(loc, {**pages, f"{page}.{ext}": changed}))
        # (b) swaps
        m2p, home = pages["markdown-to-pdf.html"], pages["home.html"]
        paper = re.search(r"<li><code>--paper</code>.*?</li>", m2p or "", re.S)
        layout = re.match(r"\s*<li>.*?</li>", m2p[paper.end():], re.S) if paper else None
        if layout:
            a, b = paper.group(0), layout.group(0).strip()
            expect(f"{loc}/markdown-to-pdf.html: --layout before --paper",
                   problems_for(loc, {**pages, "markdown-to-pdf.html": m2p.replace(a, "\0", 1).replace(b, a, 1).replace("\0", b, 1)}))
        else:
            print(f"self-test: {loc}/markdown-to-pdf.html: the swap plant can't be made")
            missed += 1
        mdl = (pages["markdown-to-pdf.md"] or "").split("\n")
        i = next((i for i, line in enumerate(mdl) if line.startswith("- `--paper`")), None)
        if i is not None:
            mdl[i], mdl[i + 1] = mdl[i + 1], mdl[i]
            expect(f"{loc}/markdown-to-pdf.md: --layout before --paper", problems_for(loc, {**pages, "markdown-to-pdf.md": "\n".join(mdl)}))
        else:
            print(f"self-test: {loc}/markdown-to-pdf.md: the swap plant can't be made")
            missed += 1
        sec = re.search(r'id="iphone-steps".*?</ol>', home or "", re.S)
        lis = re.findall(r"<li>.*?</li>", sec.group(0), re.S) if sec else []
        if len(lis) >= 2:
            s0, s1 = sec.span()
            swapped = sec.group(0).replace(lis[0], "\0", 1).replace(lis[1], lis[0], 1).replace("\0", lis[1], 1)
            expect(f"{loc}/home.html: steps 1 and 2 swapped", problems_for(loc, {**pages, "home.html": home[:s0] + swapped + home[s1:]}))
        else:
            print(f"self-test: {loc}/home.html: the swap plant can't be made")
            missed += 1
        steps, _ = home_steps(d)
        hm = pages["home.md"] or ""
        if steps[0] + "\n" + steps[1] in hm:
            expect(f"{loc}/home.md: steps 1 and 2 swapped",
                   problems_for(loc, {**pages, "home.md": hm.replace(steps[0] + "\n" + steps[1], steps[1] + "\n" + steps[0], 1)}))
        else:
            print(f"self-test: {loc}/home.md: the swap plant can't be made")
            missed += 1
        # (d) U+00A0 in each de and fr piece turned into a space, at every occurrence on its page
        if loc in NBSP_WANT:
            for page, keys in ON_PAGE.items():
                for key in keys:
                    pieces = home_steps(d)[0] if key == "home_ios" else [d[key]]
                    piece = next((p for p in pieces if NBSP in p), None)
                    if piece is None:
                        continue
                    seg = next(s for s in segments(piece) if NBSP in s)
                    around = window(seg, seg.index(NBSP), 6)
                    for ext in ("html", "md"):
                        text = pages[f"{page}.{ext}"] or ""
                        spots = piece_spots(text, ext, piece, key, around)
                        if not spots:
                            print(f"self-test: {loc}/{page}.{ext}: {key}'s U+00A0 is not on the page as text")
                            missed += 1
                            continue
                        for s in reversed(spots):
                            text = text[:s] + around.replace(NBSP, " ") + text[s + len(around):]
                        expect(f"{loc}/{page}.{ext}: {key}'s U+00A0 as a space", problems_for(loc, {**pages, f"{page}.{ext}": text}))
    # (c) HELD planted into copies of built files
    feats = read_pages("en")["features.html"] or ""
    llms_path = SITE / "llms-full.txt"
    llms = llms_path.read_text(encoding="utf-8") if llms_path.is_file() else ""
    base = {"features/index.html": feats, "llms-full.txt": llms}
    if held_problems(data.HELD, base):
        print("self-test: HELD: the unplanted files already have problems; plants there prove little")
    for loc, pieces in data.HELD.items():
        for key, s in pieces.items():
            p = plain(s)
            words = p.split(" ")
            wrapped = " ".join(words[:2] + [f"<strong>{words[2]}</strong>"] + words[3:]) if len(words) > 3 else f"<em>{p}</em>"
            variants = {"raw": s, "plain": p, "first sentence": first_sentence(p), "NBSP-spaced": p.replace(" ", NBSP),
                        "&nbsp;-spaced": p.replace(" ", "&nbsp;"), "tag-wrapped": wrapped}
            for vname, v in variants.items():
                for fname in base:
                    text = base[fname]
                    planted = text.replace("</main>", f"<p>{v}</p></main>", 1) if fname.endswith(".html") else text + "\n" + v + "\n"
                    expect(f"HELD {loc}/{key} ({vname}) in {fname}", held_problems(data.HELD, {**base, fname: planted}))
    for empty in ("", "   "):
        held = {loc: dict(pieces) for loc, pieces in data.HELD.items()}
        held["en"]["plan4"] = empty
        expect(f"HELD with an empty string {empty!r}", held_problems(held, base))
    held = {loc: dict(pieces) for loc, pieces in data.HELD.items()}
    held["de"].pop("outline_plus")
    expect("HELD missing a key", held_problems(held, base))
    print(f"self-test: {caught} plants caught, {missed} missed")
    return 1 if missed or not caught else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = check()
    for p in problems:
        print(p)
    if problems:
        print(f"{len(problems)} problems")
        return 1
    print(f"ok: #369 copy present and verbatim in {len(data.DATA)} locales (11 pieces each, html and md); "
          f"HELD pieces on no file under public/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
