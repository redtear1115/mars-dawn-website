#!/usr/bin/env python3
"""Checks that the built /native/ pages carry website #373's "Small and quiet" section, character for character.

DATA holds the approved copy from the ticket (mars-dawn-website#373, issue body, table "文案"): per locale a
heading, two list items and a small note. U+00A0 is written as the escape \\u00a0 so it cannot be lost by an
editor. This reads the built public/ files, never build_pages.py or the copy_*.py files, and compares EXACTLY:
no strip, no whitespace collapsing, no NBSP normalisation, no case folding.

Per locale, the section must sit in <main> of public/<prefix>native/index.html as the page's third <h3>
(after "Editing" and "The rest of the Mac"), once, as

    <h3>heading</h3> <ul> <li>li1</li> <li>li2</li> </ul> <p>note</p>

with each element's text (tags stripped, html.unescape applied) equal to DATA. The Markdown twin
(index.md) must hold the lines "### heading", "", "- li1", "- li2", "", "note" in a row, as the third "### ".

The twin is made by build_pages.py's _collapse(), which on main still turns U+00A0 into a plain space
(website #369 / PR #370 changes that). So by default the twin's expected lines have U+00A0 -> " ", and
--md-keep-nbsp expects them kept (use it once #370's _collapse change is on the branch). The HTML never
gets that leniency.

Exit codes: 0 all good, 1 a mismatch (first differing code point and its index are printed), 2 usage error
or a failed --self-test.

--self-test builds a synthetic site from DATA, asserts it passes (positive control), then applies mutations
in memory, each of which must be caught: double space, U+00A0 to space, U+00A0 dropped, one character
swapped, one character appended, heading/li/note missing, whole section removed (html and md), section
moved, a missing locale file, one locale's text replaced by another locale's, a repeated section. It never
writes to the repo.
"""
import argparse
import html
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "public"
PREFIX = {"en": "", "zh-hant": "zh-hant/", "zh-hans": "zh-hans/", "ja": "ja/", "ko": "ko/", "de": "de/",
          "fr": "fr/", "es": "es/"}
NBSP = "\u00a0"

DATA = {
    "en": {
        "h": "Small and quiet",
        "li1": "An 11.4 MB download from the Mac App Store.",
        "li2": "0% CPU when a document is open and nothing is changing.",
        "note": "Measured on version 1.2.1, November 2026.",
    },
    "zh-hant": {
        "h": "小而安靜",
        "li1": "從 Mac App Store 下載只要 11.4 MB。",
        "li2": "文件開著、沒有變動時，CPU 用量 0%。",
        "note": "以 1.2.1 版實測，2026 年 11 月。",
    },
    "zh-hans": {
        "h": "小而安静",
        "li1": "从 Mac App Store 下载只要 11.4 MB。",
        "li2": "文稿开着、没有变动时，CPU 占用 0%。",
        "note": "以 1.2.1 版实测，2026 年 11 月。",
    },
    "ja": {
        "h": "小さくて、静か",
        "li1": "Mac App Store からのダウンロードは 11.4 MB。",
        "li2": "書類を開いたまま変更がないとき、CPU 使用率は 0%。",
        "note": "バージョン 1.2.1 で計測（2026年11月）。",
    },
    "ko": {
        "h": "작고 조용하게",
        "li1": "Mac App Store에서 내려받는 크기는 11.4MB입니다.",
        "li2": "문서를 열어 둔 채 변경이 없으면 CPU 사용률은 0%입니다.",
        "note": "버전 1.2.1에서 측정(2026년 11월).",
    },
    "de": {
        "h": "Klein und leise",
        "li1": "11,4\u00a0MB Download aus dem Mac App Store.",
        "li2": "0\u00a0% CPU, wenn ein Dokument geöffnet ist und sich nichts ändert.",
        "note": "Gemessen mit Version 1.2.1, November 2026.",
    },
    "fr": {
        "h": "Petite et discrète",
        "li1": "11,4\u00a0Mo à télécharger sur le Mac App Store.",
        "li2": "0\u00a0% de CPU quand un document est ouvert et que rien ne change.",
        "note": "Mesuré avec la version 1.2.1, novembre 2026.",
    },
    "es": {
        "h": "Pequeña y silenciosa",
        "li1": "Una descarga de 11,4\u00a0MB desde el Mac App Store.",
        "li2": "0\u00a0% de CPU con un documento abierto y sin cambios.",
        "note": "Medido con la versión 1.2.1, noviembre de 2026.",
    },
}
assert list(DATA) == list(PREFIX)

FIELDS = ("h", "li1", "li2", "note")
HTML_SECTION = re.compile(
    r"<h3>(?P<h>[^<]*)</h3>\s*<ul>\s*<li>(?P<li1>(?:(?!</li>).)*)</li>\s*<li>(?P<li2>(?:(?!</li>).)*)</li>\s*</ul>\s*<p>(?P<note>(?:(?!</p>).)*)</p>",
    re.S)


def cp(ch: str) -> str:
    return f"U+{ord(ch):04X} {ch!r}"


def first_diff(want: str, got: str) -> str:
    """Where two strings first differ, as an index and the two code points."""
    for i, (a, b) in enumerate(zip(want, got)):
        if a != b:
            return f"index {i}: want {cp(a)}, got {cp(b)}"
    if len(want) == len(got):
        return "no difference"
    i = min(len(want), len(got))
    longer, who = (want, "want has") if len(want) > len(got) else (got, "got has")
    return f"index {i}: {who} extra {cp(longer[i])} (want {len(want)} chars, got {len(got)})"


def text_of(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment))


def md_expect(d: dict, keep_nbsp: bool) -> list:
    lines = [f"### {d['h']}", "", f"- {d['li1']}", f"- {d['li2']}", "", d["note"]]
    return lines if keep_nbsp else [x.replace(NBSP, " ") for x in lines]


def html_problems(loc: str, d: dict, page) -> list:
    p = f"{loc}/html"
    if page is None:
        return [f"{p}: index.html missing"]
    m = re.search(r"<main\b.*?</main>", page, re.S)
    main = m.group(0) if m else page
    h3s = re.findall(r"<h3>([^<]*)</h3>", main)
    if len(h3s) != 3:
        return [f"{p}: expected 3 <h3> in <main>, found {len(h3s)}"]
    secs = [s for s in HTML_SECTION.finditer(main) if s.group("h") == d["h"]]
    if len(secs) != 1:
        near = [h for h in h3s if h != d["h"]][-1:]
        return [f"{p}: section with the exact heading {d['h']!r} found {len(secs)} times "
                f"(h3s: {[text_of(h) for h in h3s]!r}; {first_diff(d['h'], text_of(h3s[2]))})"]
    out = []
    got = {k: text_of(secs[0].group(k)) for k in FIELDS}
    for k in FIELDS:
        if got[k] != d[k]:
            out.append(f"{p}: {k} differs at {first_diff(d[k], got[k])}")
    if h3s[2] != d["h"]:
        out.append(f"{p}: section is not the page's third <h3> (third is {h3s[2]!r})")
    return out


def md_problems(loc: str, d: dict, text, keep_nbsp: bool) -> list:
    p = f"{loc}/md"
    if text is None:
        return [f"{p}: index.md missing"]
    lines = text.split("\n")
    want = md_expect(d, keep_nbsp)
    heads = [i for i, ln in enumerate(lines) if ln.startswith("### ")]
    at = [i for i in heads if lines[i] == want[0]]
    if len(heads) < 3 or len(at) != 1:
        cand = lines[heads[2]] if len(heads) >= 3 else ""
        return [f"{p}: line {want[0]!r} found {len(at)} times among {len(heads)} '### ' lines "
                f"({first_diff(want[0], cand)})"]
    i = at[0]
    if heads.index(i) != 2:
        return [f"{p}: section is '### ' number {heads.index(i) + 1}, expected 3"]
    out = []
    for k, w in enumerate(want):
        g = lines[i + k] if i + k < len(lines) else ""
        if g != w:
            out.append(f"{p}: line {k} of the section differs at {first_diff(w, g)}")
    return out


def check(read, keep_nbsp: bool) -> list:
    """read(locale, 'html'|'md') -> file text or None. Returns the list of problems."""
    out = []
    for loc, d in DATA.items():
        out += html_problems(loc, d, read(loc, "html"))
        out += md_problems(loc, d, read(loc, "md"), keep_nbsp)
    return out


def real_reader(loc: str, kind: str):
    f = SITE / PREFIX[loc] / "native" / ("index.html" if kind == "html" else "index.md")
    return f.read_text(encoding="utf-8") if f.is_file() else None


# ---------------------------------------------------------------- self-test

def synth_html(d: dict) -> str:
    return ("<html><body><main>\n<h2>x</h2>\n<h3>A</h3>\n<ul>\n  <li>a</li>\n</ul>\n<h3>B</h3>\n<ul>\n  <li>b</li>\n</ul>\n"
            f"<h3>{d['h']}</h3>\n<ul>\n  <li>{d['li1']}</li>\n  <li>{d['li2']}</li>\n</ul>\n<p>{d['note']}</p>\n"
            "</main></body></html>\n")


def synth_md(d: dict, keep_nbsp: bool) -> str:
    pre = "## x\n\n### A\n\n- a\n\n### B\n\n- b\n\n"
    return pre + "\n".join(md_expect(d, keep_nbsp)) + "\n"


def self_test(keep_nbsp: bool) -> int:
    base = {}
    for loc, d in DATA.items():
        base[(loc, "html")] = synth_html(d)
        base[(loc, "md")] = synth_md(d, keep_nbsp)
    fails = []

    def run(files):
        return check(lambda loc, kind: files.get((loc, kind)), keep_nbsp)

    def case(name, mutants):
        """mutants: list of (label, files). Every mutant must produce at least one problem."""
        missed = [lab for lab, files in mutants if not run(files)]
        status = "PASS" if mutants and not missed else "FAIL"
        print(f"{status} {name}: {len(mutants) - len(missed)}/{len(mutants)} detected")
        if status == "FAIL":
            fails.append(name)
            for lab in missed[:5]:
                print(f"    not detected: {lab}")

    def sub(key, old, new):
        files = dict(base)
        assert old in files[key], (key, old)
        files[key] = files[key].replace(old, new, 1)
        return files

    pos = run(base)
    print(("PASS" if not pos else "FAIL") + f" positive control (unmutated, md_keep_nbsp={keep_nbsp}): {len(pos)} problems")
    if pos:
        fails.append("positive control")
        for x in pos[:5]:
            print("    " + x)

    def field_mutants(fn, need):
        """fn(text) -> mutated text or None (not applicable). Applied to each field, in html and in md."""
        out = []
        for loc, d in DATA.items():
            for k in FIELDS:
                new = fn(d[k])
                if new is None:
                    continue
                for kind in ("html", "md"):
                    shown = d[k] if kind == "html" or keep_nbsp else d[k].replace(NBSP, " ")
                    newshown = new if kind == "html" or keep_nbsp else new.replace(NBSP, " ")
                    if shown == newshown:
                        continue
                    pre = {"html": {"h": "<h3>", "li1": "<li>", "li2": "<li>", "note": "<p>"},
                           "md": {"h": "### ", "li1": "- ", "li2": "- ", "note": "\n\n"}}[kind][k]
                    out.append((f"{loc}/{kind}/{k}", sub((loc, kind), pre + shown, pre + newshown)))
        assert len(out) >= need, (len(out), need)
        return out

    def dbl(t):
        i = t.find(" ")
        return None if i < 0 else t[:i] + "  " + t[i + 1:]

    def nb2sp(t):
        return t.replace(NBSP, " ", 1) if NBSP in t else None

    def nb_drop(t):
        return t.replace(NBSP, "", 1) if NBSP in t else None

    def swap(t):
        i = len(t) // 2
        return t[:i] + ("x" if t[i] != "x" else "y") + t[i + 1:]

    def digit(t):
        m = re.search(r"\d", t)
        return None if not m else t[:m.start()] + str((int(m.group()) + 1) % 10) + t[m.end():]

    def append(t):
        return t + "."

    def lead(t):
        return " " + t

    case("double space", field_mutants(dbl, 40))
    case("NBSP -> space (de, fr, es)", field_mutants(nb2sp, 6))
    case("NBSP removed (de, fr, es)", field_mutants(nb_drop, 6))
    case("one character swapped", field_mutants(swap, 60))
    case("one digit changed (11.4, 0%, 1.2.1, 2026)", field_mutants(digit, 20))
    case("one character appended", field_mutants(append, 60))
    case("leading space", field_mutants(lead, 60))

    sect = {}
    for loc, d in DATA.items():
        sect[(loc, "html")] = synth_html(d)
    m = []
    for loc, d in DATA.items():
        for kind, a, b in (("html", f"<h3>{d['h']}</h3>", "</p>\n"),):
            files = dict(base)
            t = files[(loc, kind)]
            i, j = t.index(a), t.index(b, t.index(a)) + len(b)
            files[(loc, kind)] = t[:i] + t[j:]
            m.append((f"{loc}/{kind}", files))
        files = dict(base)
        t = files[(loc, "md")]
        i = t.index("### " + md_expect(d, keep_nbsp)[0][4:])
        files[(loc, "md")] = t[:i]
        m.append((f"{loc}/md", files))
    case("section removed (html and md, every locale)", m)

    m = []
    for loc, d in DATA.items():
        for kind in ("html", "md"):
            files = dict(base)
            files[(loc, kind)] = None
            m.append((f"{loc}/{kind}", files))
    case("locale file missing (html or md)", m)

    m = []
    locs = list(DATA)
    for n, loc in enumerate(locs):
        other = DATA[locs[(n + 1) % len(locs)]]
        files = dict(base)
        files[(loc, "html")] = synth_html(other)
        m.append((f"{loc}/html <- {locs[(n + 1) % len(locs)]}", files))
        files = dict(base)
        files[(loc, "md")] = synth_md(other, keep_nbsp)
        m.append((f"{loc}/md <- {locs[(n + 1) % len(locs)]}", files))
        # only the body text from another locale, heading kept
        files = dict(base)
        files[(loc, "html")] = base[(loc, "html")].replace(DATA[loc]["li1"], other["li1"], 1)
        m.append((f"{loc}/html li1 <- {locs[(n + 1) % len(locs)]}", files))
    case("one language's text replaced by another's", m)

    m = []
    for loc, d in DATA.items():
        files = dict(base)
        files[(loc, "html")] = files[(loc, "html")].replace("</main>", f"<h3>{d['h']}</h3>\n<ul>\n<li>{d['li1']}</li>\n<li>{d['li2']}</li>\n</ul>\n<p>{d['note']}</p>\n</main>")
        m.append((f"{loc}/html repeated", files))
        files = dict(base)
        files[(loc, "md")] = files[(loc, "md")] + "\n" + synth_md(d, keep_nbsp)
        m.append((f"{loc}/md repeated", files))
    case("section repeated", m)

    m = []
    for loc, d in DATA.items():
        files = dict(base)
        h = synth_html(d)
        sec = h[h.index(f"<h3>{d['h']}</h3>"):h.index("</main>")]
        files[(loc, "html")] = h.replace(sec, "").replace("<h3>A</h3>", sec + "<h3>A</h3>", 1)
        m.append((f"{loc}/html moved before A", files))
    case("section moved out of third place (html)", m)

    m = []
    for loc, d in DATA.items():
        files = dict(base)
        files[(loc, "md")] = base[(loc, "md")].replace("\n\n- " + d["li1"].replace(NBSP, " ") if not keep_nbsp else "\n\n- " + d["li1"], "\n- " + (d["li1"].replace(NBSP, " ") if not keep_nbsp else d["li1"]), 1)
        m.append((f"{loc}/md blank line after heading removed", files))
        files = dict(base)
        files[(loc, "md")] = base[(loc, "md")].rstrip("\n") + " \n"
        m.append((f"{loc}/md trailing space on the note", files))
    case("md layout changed (blank line, trailing space)", m)

    if fails:
        print("self-test FAILED: " + ", ".join(fails))
        return 2
    print("self-test ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--self-test", action="store_true", help="plant mutations in memory and require each to be caught")
    ap.add_argument("--md-keep-nbsp", action="store_true",
                    help="expect U+00A0 kept in the Markdown twins (after website #369's _collapse change)")
    try:
        a = ap.parse_args()
    except SystemExit as e:
        return 2 if e.code else 0
    if a.self_test:
        rc = self_test(False)
        return rc or self_test(True)
    problems = check(real_reader, a.md_keep_nbsp)
    for x in problems:
        print("MISMATCH " + x)
    if problems:
        return 1
    print(f"ok: {len(DATA)} locales x (html, md) carry #373's section verbatim (md_keep_nbsp={a.md_keep_nbsp})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
