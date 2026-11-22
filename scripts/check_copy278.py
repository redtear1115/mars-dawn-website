#!/usr/bin/env python3
"""Checks that the built /from-hackmd/ pages carry the `:::` sentence (website #278), character for character.

The sentence per locale is read from the approved comments kept in scripts/copy278/source/ (6964983008 for en
and zh-Hant, 6965344647 for the other six; Ray's "#278 ::: ok" is comment 6965143868), through the same reader
ingest.py uses, never from data.py or build_pages.py. This reads the built public/ files and compares EXACTLY:
no strip, no whitespace collapsing, no NBSP normalisation, no case folding.

Per locale, in <main> of public/<prefix>from-hackmd/index.html:
  - one <p> whose text (tags stripped, html.unescape applied) is the sentence with its backticks removed,
    and whose <code> texts are the backticked spans in order;
  - the next <p> is the "A few things look different" paragraph (fr: its U+00A0 read as a space);
  - no 【待定 anywhere in <main>.
In index.md (the twin): the sentence is one line, exactly as in the comment, followed by an empty line and the
"A few things" line, and the sentence occurs once.

Prints one line per locale: how many times found in the HTML and the twin, its position (the number of the
<p> in <main>, the line number in the twin), and whether each matches. Exit codes: 0 all good, 1 a mismatch
(first differing code point and its index are printed), 2 usage error or a failed --self-test.

--self-test builds a synthetic site from the sentences, asserts it passes (positive control), then applies
mutations in memory, each of which must be caught: double space, U+00A0, one character swapped or appended,
a <code> span lost, the sentence missing or repeated, moved after the "A few things" paragraph, another
locale's sentence, a 【待定 line left in, a missing file (html and md). It never writes to the repo.
"""
import argparse
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from copy278 import ingest  # noqa: E402

SITE = HERE.parent / "public"
PREFIX = {"en": "", "zh-hant": "zh-hant/", "zh-hans": "zh-hans/", "ja": "ja/", "ko": "ko/", "de": "de/",
          "fr": "fr/", "es": "es/"}
NBSP = " "
PENDING = "【待定"


def cp(ch: str) -> str:
    return f"U+{ord(ch):04X} {ch!r}"


def first_diff(want: str, got: str) -> str:
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


def sentences() -> dict:
    """locale -> (sentence as written in the comment, the "A few things" line as the comment names it)."""
    return {loc: (c["sentence"], c["before"]) for loc, c in ingest.colon_copy().items()}


def code_spans(sentence: str) -> list:
    return re.findall(r"`([^`]+)`", sentence)


def paragraphs(page: str):
    m = re.search(r"<main\b.*?</main>", page, re.S)
    main = m.group(0) if m else page
    return main, re.findall(r"<p>(.*?)</p>", main, re.S)


def html_report(loc: str, sentence: str, before: str, page):
    """(found, position, problems)."""
    if page is None:
        return 0, None, [f"{loc}/html: index.html missing"]
    main, paras = paragraphs(page)
    want = sentence.replace("`", "")
    at = [i for i, p in enumerate(paras) if text_of(p) == want]
    out = []
    if PENDING in main:
        out.append(f"{loc}/html: {PENDING} is still in <main>")
    if len(at) != 1:
        near = next((p for p in paras if text_of(p).startswith(want[:6])), "")
        return len(at), None, out + [f"{loc}/html: sentence found {len(at)} times ({first_diff(want, text_of(near))})"]
    i = at[0]
    if re.findall(r"<code>(.*?)</code>", paras[i], re.S) != [html.escape(c, quote=False) for c in code_spans(sentence)]:
        out.append(f"{loc}/html: the <code> spans differ from the comment's backticked spans")
    nxt = text_of(paras[i + 1]) if i + 1 < len(paras) else ""
    if nxt.replace(NBSP, " ") != before:
        out.append(f"{loc}/html: the paragraph after the sentence is not {before!r} ({first_diff(before, nxt)})")
    return 1, i + 1, out


def md_report(loc: str, sentence: str, before: str, text):
    if text is None:
        return 0, None, [f"{loc}/md: index.md missing"]
    lines = text.split("\n")
    at = [n for n, line in enumerate(lines) if line == sentence]
    out = []
    if PENDING in text:
        out.append(f"{loc}/md: {PENDING} is still in the twin")
    if len(at) != 1:
        near = next((line for line in lines if line.startswith(sentence[:6])), "")
        return len(at), None, out + [f"{loc}/md: sentence found {len(at)} times ({first_diff(sentence, near)})"]
    n = at[0]
    after = lines[n + 2] if n + 2 < len(lines) else ""
    if lines[n + 1:n + 2] != [""] or after.replace(NBSP, " ") != before:
        out.append(f"{loc}/md: the sentence is not followed by an empty line and {before!r} ({first_diff(before, after)})")
    return 1, n + 1, out


def check(read, data: dict):
    """read(locale, 'html'|'md') -> text or None. Returns (rows, problems)."""
    rows, problems = [], []
    for loc, (sentence, before) in data.items():
        hf, hp, hproblems = html_report(loc, sentence, before, read(loc, "html"))
        mf, mp, mproblems = md_report(loc, sentence, before, read(loc, "md"))
        rows.append((loc, hf, hp, not hproblems, mf, mp, not mproblems))
        problems += hproblems + mproblems
    return rows, problems


def real_reader(loc: str, kind: str):
    f = SITE / PREFIX[loc] / "from-hackmd" / ("index.html" if kind == "html" else "index.md")
    return f.read_text(encoding="utf-8") if f.is_file() else None


# ---------------------------------------------------------------- self-test

def synth_html(sentence: str, before: str, pending: bool = False) -> str:
    code = re.sub(r"`([^`]+)`", lambda m: f"<code>{html.escape(m.group(1), quote=False)}</code>", html.escape(sentence.replace("`", "\0"), quote=False).replace("\0", "`"))
    return ("<html><body><main>\n<h1>x</h1>\n<p>intro</p>\n<p>before</p>\n"
            f"<p>{code}</p>\n<p>{before}</p>\n<ul><li>a</li></ul>\n" + (f"<p>{PENDING}，#300】</p>\n" if pending else "")
            + "</main></body></html>\n")


def synth_md(sentence: str, before: str, pending: bool = False) -> str:
    return "# x\n\nintro\n\nbefore\n\n" + sentence + "\n\n" + before + "\n\n- a\n" + (f"\n{PENDING}，#300】\n" if pending else "")


def self_test() -> int:
    data = sentences()
    assert list(data) == list(PREFIX), list(data)
    base = {}
    for loc, (s, b) in data.items():
        base[(loc, "html")] = synth_html(s, b)
        base[(loc, "md")] = synth_md(s, b)
    fails = []

    def run(files):
        return check(lambda loc, kind: files.get((loc, kind)), data)[1]

    def case(name, mutants):
        missed = [lab for lab, files in mutants if not run(files)]
        status = "PASS" if mutants and not missed else "FAIL"
        print(f"{status} {name}: {len(mutants) - len(missed)}/{len(mutants)} detected")
        if status == "FAIL":
            fails.append(name)
            for lab in missed[:5]:
                print(f"    not detected: {lab}")

    pos = run(base)
    print(("PASS" if not pos else "FAIL") + f" positive control (unmutated): {len(pos)} problems")
    if pos:
        fails.append("positive control")
        for x in pos[:5]:
            print("    " + x)

    def edit(fn, need):
        """fn(sentence) -> changed sentence or None; applied to the sentence inside the html and the md."""
        out = []
        for loc, (s, b) in data.items():
            new = fn(s)
            if new is None or new == s:
                continue
            out.append((f"{loc}/html", {**base, (loc, "html"): synth_html(new, b)}))
            out.append((f"{loc}/md", {**base, (loc, "md"): synth_md(new, b)}))
        assert len(out) >= need, (len(out), need)
        return out

    def dbl(s):
        i = s.find(" ")
        return None if i < 0 else s[:i] + "  " + s[i + 1:]

    def swap(s):
        i = len(s) // 2
        return s[:i] + ("x" if s[i] != "x" else "y") + s[i + 1:]

    case("double space", edit(dbl, 14))
    case("a space turned into U+00A0", edit(lambda s: s.replace(" ", NBSP, 1), 14))
    case("one character swapped", edit(swap, 14))
    case("one character appended", edit(lambda s: s + ".", 14))
    case("last backtick span lost", edit(lambda s: re.sub(r"`([^`]+)`(?!.*`)", r"\1", s), 14))

    m = []
    for loc, (s, b) in data.items():
        m.append((f"{loc}/html", {**base, (loc, "html"): synth_html("", b).replace("<p></p>\n", "")}))
        m.append((f"{loc}/md", {**base, (loc, "md"): synth_md("", b).replace("\n\n\n\n", "\n\n")}))
    case("sentence missing", m)

    m = []
    for loc, (s, b) in data.items():
        m.append((f"{loc}/html", {**base, (loc, "html"): base[(loc, "html")].replace("</main>", synth_html(s, b).split("<main>")[1])}))
        m.append((f"{loc}/md", {**base, (loc, "md"): base[(loc, "md")] + "\n" + s + "\n"}))
    case("sentence repeated", m)

    m = []
    for loc, (s, b) in data.items():
        h = base[(loc, "html")]
        rows = h.split("\n")
        rows[4], rows[5] = rows[5], rows[4]   # the sentence's <p> and the "A few things" <p> trade places
        m.append((f"{loc}/html", {**base, (loc, "html"): "\n".join(rows)}))
        t = base[(loc, "md")]
        m.append((f"{loc}/md", {**base, (loc, "md"): t.replace(s + "\n\n" + b + "\n", b + "\n\n" + s + "\n")}))
    case("sentence moved after the 'A few things' paragraph", m)

    m = []
    locs = list(data)
    for n, loc in enumerate(locs):
        other = data[locs[(n + 1) % len(locs)]][0]
        b = data[loc][1]
        m.append((f"{loc}/html <- {locs[(n + 1) % len(locs)]}", {**base, (loc, "html"): synth_html(other, b)}))
        m.append((f"{loc}/md <- {locs[(n + 1) % len(locs)]}", {**base, (loc, "md"): synth_md(other, b)}))
    case("another locale's sentence", m)

    m = []
    for loc, (s, b) in data.items():
        m.append((f"{loc}/html", {**base, (loc, "html"): synth_html(s, b, True)}))
        m.append((f"{loc}/md", {**base, (loc, "md"): synth_md(s, b, True)}))
    case("a 【待定 line left in", m)

    m = [(f"{loc}/{kind}", {**base, (loc, kind): None}) for loc in data for kind in ("html", "md")]
    case("locale file missing", m)

    if fails:
        print("self-test FAILED: " + ", ".join(fails))
        return 2
    print("self-test ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--self-test", action="store_true", help="plant mutations in memory and require each to be caught")
    try:
        a = ap.parse_args()
    except SystemExit as e:
        return 2 if e.code else 0
    if a.self_test:
        return self_test()
    rows, problems = check(real_reader, sentences())
    print("locale   html: found  <p> no.  match | md: found  line no.  match")
    for loc, hf, hp, hok, mf, mp, mok in rows:
        print(f"{loc:8} {hf:>11}  {hp if hp else '-':>7}  {'yes' if hok else 'NO':>5} | {mf:>9}  {mp if mp else '-':>8}  {'yes' if mok else 'NO':>5}")
    for x in problems:
        print("MISMATCH " + x)
    if problems:
        return 1
    print(f"ok: {len(rows)} locales carry the ::: sentence verbatim in html and md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
