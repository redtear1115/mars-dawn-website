#!/usr/bin/env python3
"""One-shot application of the #383 copy to the sources (website #383). Already applied; kept so a reviewer can see how.

Reads scripts/copy383/data.py (written by ingest.py from the pinned comments) and edits the sources:

1. SRC_ROWS (Table B): each "current" fragment must occur exactly once in its file, then it is replaced by the
   proposed fragment. Found 0 or more than 1 times: stop, change nothing in that file.
2. Table A: for each locale the /pdf/ page block (title, description, intro, body) is located, every old
   cell that is being replaced must occur exactly once in it, and the block is rewritten from the proposed cells.
   The cells the table leaves alone (b2, b3, the #369 sentence b369, card) are not typed here: b2 and b3 must occur
   exactly once in the old block and are carried over; b369 is appended by apply_copy369_pdf_pages as before.
   apply_panel.py applies fig_alt and co1-co3 to the Print & Export panel figure.

    python3 -I -B scripts/copy383/apply.py --dry-run   # check every match, write nothing
    python3 -I -B scripts/copy383/apply.py             # write
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from copy383.data import SRC_ROWS, TABLE_A  # noqa: E402
import rich_pages  # noqa: E402

LOCALE_BLOCK = {
    # locale: (file, start marker, end marker, quote used for the plain literals, kind)
    "en": ("scripts/build_pages.py", '    ("en", "pdf"): _trait_page(\n', "\n    ),\n", '"', "trait_page"),
    "zh-Hant": ("scripts/build_pages.py", '    ("zh-hant", "pdf"): _trait_page(\n', "\n    ),\n", '"', "trait_page"),
}
for _l, _f in (("zh-Hans", "copy_zh_hans"), ("ja", "copy_ja"), ("ko", "copy_ko"), ("de", "copy_de"), ("fr", "copy_fr"), ("es", "copy_es")):
    LOCALE_BLOCK[_l] = (f"scripts/{_f}.py", "    pages['pdf'] = {\n", "\n    }\n", "'", "pages")

IMAGES = {"doc": "layout-document.png", "hb": "layout-handbook-contents.png", "ho": "layout-handout.png"}
IMAGE_SIZE = (856, 1108)


class Stop(SystemExit):
    pass


def exactly_once(text: str, needle: str, where: str) -> int:
    n = text.count(needle)
    if n != 1:
        raise Stop(f"{where}: {needle[:70]!r} found {n} times, expected exactly once")
    return text.index(needle)


def edit_rows(files: dict) -> None:
    for row in SRC_ROWS:
        path = row["file"]
        if path == "scripts/copy369/data.py":
            continue   # generated: scripts/copy369/ingest.py applies these rows (rename_383) and writes data.py
        text = files.setdefault(path, (ROOT / path).read_text(encoding="utf-8"))
        old, new = row["current"].lstrip("…"), row["proposed"].lstrip("…")
        where = f'{row["id"]} ({path})'
        if row["id"] == "src.approved.zh-Hant.faq":
            # approved_copy.py splits this link text over two string literals: '…請看[輸出 ' and 'PDF](/zh-hant/pdf/)和…'.
            # The table's fragment spans the seam, so match the seam: only the part before the space changes.
            (old_head, tail), (new_head, new_tail) = (re.search(r"\[([^\]]+)\]", x).group(1).rsplit(" ", 1) for x in (old, new))
            if tail != new_tail:
                raise Stop(f"{where}: the link text after the seam changes ({tail!r} -> {new_tail!r})")
            seam = re.compile(r"\[" + re.escape(old_head) + r" '\n\s*'" + re.escape(tail) + r"\]\(/zh-hant/pdf/\)")
            found = seam.findall(text)
            if len(found) != 1:
                raise Stop(f"{where}: the split link text found {len(found)} times, expected exactly once")
            files[path] = seam.sub(lambda m: m.group(0).replace(f"[{old_head} '", f"[{new_head} '", 1), text)
            continue
        if text.count(old) == 0 and ")" in old and ")" in new:
            # the sentence continues in a second string literal (en faq: "... and [Markdown to '" 'PDF](...)'):
            # match up to the end of the renamed link, and require that the rest of the table's text is unchanged
            cut_old, cut_new = old.index(")") + 1, new.index(")") + 1
            if old[cut_old:] != new[cut_new:]:
                raise Stop(f"{where}: text after the link changes")
            old, new = old[:cut_old], new[:cut_new]
            print(f"  {row['id']}: matched up to the end of the link")
        at = exactly_once(text, old, where)
        files[path] = text[:at] + new + text[at + len(old):]


def lit(s: str, quote: str) -> str:
    """A Python string literal for s: backslash and NBSP escaped, the other quote used when s contains this one."""
    if quote in s and (other := "'" if quote == '"' else '"') not in s:
        quote = other
    body = s.replace("\\", "\\\\").replace("\xa0", "\\xa0").replace(quote, "\\" + quote)
    return quote + body + quote


def html_alt(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def md(s: str) -> str:
    return rich_pages.md_inline(s)


def new_parts(locale: str) -> dict:
    p = {k: v[1] for k, v in TABLE_A[locale].items()}
    w, h = IMAGE_SIZE
    figs = "\n".join(
        f'  <figure>\n    <img src="/assets/cli/{IMAGES[k]}" alt="{html_alt(p["alt_" + k])}" width="{w}" height="{h}">\n'
        f'    <figcaption>{md(p["cap_" + k])}</figcaption>\n  </figure>'
        for k in ("doc", "hb", "ho"))
    steps = "\n".join(f"  <li>{md(p[f'step{i}'])}</li>" for i in (1, 2, 3))
    intro = f'\n<section class="intro">\n  <h1>{md(p["h1"])}</h1>\n  <p>{md(p["lede"])}</p>\n</section>\n'
    body = (f'\n<h2>{md(p["h2_steps"])}</h2>\n<ol class="loop-steps">\n{steps}\n</ol>\n'
            f'<h2>{md(p["h2_layouts"])}</h2>\n<p>{md(p["opener"])}</p>\n<div class="layout-shots">\n{figs}\n</div>\n'
            f'<h2>{md(p["h2_bul"])}</h2>\n<ul>\n'
            f'  <li>{md(p["b1"])}</li>\n  <li>{md(p["b2"])}</li>\n  <li>{md(p["b3"])}</li>\n</ul>\n'
            f'<p>{md(p["ios"])}</p>\n<p>{md(p["close"])}</p>\n')
    return {"title": p["title"] + " · MarsDawn", "description": p["meta"], "intro": intro, "body": body}


def check_old_cells(locale: str, block: str) -> None:
    """Every cell the table replaces must be in the old block exactly once; the cells it keeps too."""
    norm = block.replace("\\xa0", "\xa0")
    a = {k: v[0] for k, v in TABLE_A[locale].items()}
    where = f"{locale} /pdf/ block"
    for key in ("meta", "h1", "lede", "h2_bul", "b1", "b_del", "close", "b2", "b3"):
        cell = a[key]
        needle = cell if key == "meta" else md(cell)
        if key == "close" and "<a " in cell:
            needle = md(cell)
        exactly_once(norm, needle, f"{where} {key}")
    exactly_once(norm, a["title"] + " · MarsDawn", f"{where} title")


def rewrite_block(locale: str, text: str) -> str:
    path, start, end, quote, kind = LOCALE_BLOCK[locale]
    i = exactly_once(text, start, f"{locale} block start in {path}") + len(start)
    j = text.index(end, i)
    block = text[i:j]
    check_old_cells(locale, block)
    n = new_parts(locale)
    t, d, intro, body = (lit(n["title"], quote), lit(n["description"], quote),
                         n["intro"].replace("\xa0", "\\xa0"), n["body"].replace("\xa0", "\\xa0"))
    if kind == "trait_page":
        new = f'        {t},\n        {d},\n        """{intro}""",\n        """{body}""",'
    else:
        # keep each field's own string prefix (f or plain): only the text changes
        fp = {k: re.search(rf'"{k}": (f?)"""', block).group(1) for k in ("intro", "body")}
        new = (f'        "title": {t},\n        "description": {d},\n'
               f'        "intro": {fp["intro"]}"""{intro}""",\n        "body": {fp["body"]}"""{body}""",')
    return text[:i] + new + text[j:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    files = {}
    # the page blocks first: table B edits change copy369/data.py, build_pages.py and the copy_<l>.py files too
    for locale in LOCALE_BLOCK:
        path = LOCALE_BLOCK[locale][0]
        text = files.setdefault(path, (ROOT / path).read_text(encoding="utf-8"))
        files[path] = rewrite_block(locale, text)
        print(f"page block {locale}: old cells matched once each, rewritten")
    edit_rows(files)
    print(f"{sum(r['file'] != 'scripts/copy369/data.py' for r in SRC_ROWS)} source rows matched once each (the 8 for copy369/data.py are applied by copy369/ingest.py)")
    if args.dry_run:
        print("dry run: nothing written")
        return 0
    for path, text in files.items():
        (ROOT / path).write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
