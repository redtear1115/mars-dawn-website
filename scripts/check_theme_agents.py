#!/usr/bin/env python3
"""Holds /themes/agents/ to the kit (plan PLAN-web-theme-tuning W3, Rev 3.7-3.9).

The page is a reference an agent reads instead of the kit's Swift, so a field that is missing,
extra, or wrong there makes the agent write a theme the validator refuses. scripts/theme_agents.py
lays the page out from the vendored Swift; this reads the *generated* pages back (every served
locale's themes/agents/index.html, and the English index.md) and compares what is printed there with
what the Swift says, so a hand edit of build_pages.py, a copy module or a stale public/ is caught
too. It asks the Swift through theme_agents.model(), not through the generator's layout code.

  page.missing     a served locale has no themes/agents/index.html
  fields.missing   a field the Swift decodes is not in its table
  fields.extra     a table row for a field the Swift does not decode
  fields.presence  required/optional differs from `.decode` / `.decodeIfPresent`
  fields.type      the type token differs from the Swift type
  fields.values    an enum field lists other values than the Swift enum
  publish.mark     "required to publish (--require-complete)" is not on exactly `syntax` and `diagram`
  kinds.missing    a `type` value (or one of its fields) the Swift allows is not in the options table
  kinds.extra      a row for a `type` value or field the Swift does not allow
  kinds.presence   a kind's field is marked required/optional the other way round
  kinds.type       a kind's field has another type token
  roles.set        the palette roles listed differ from PaletteRole
  numbers.missing  a number in ThemeNumbers.swift has no row
  numbers.extra    a number row ThemeNumbers.swift does not have
  numbers.range    a number's min, max or step differs from ThemeNumbers.swift
  example.drift    the Dawn example is not byte-equal to the vendored dawn theme.json
  recipe.drift     the hand-off command differs from the one the generator defines for that locale
  recipe.broken    run in bash against dawn.json and against bytes whose standard base64 holds + / and =,
                   the command does not give <locale>/themes/new/#theme= followed by the base64url of the
                   file's bytes
  md.twin          the English index.md does not carry the recipe and the example

Usage:
    python3 scripts/check_theme_agents.py [--root public]
    python3 scripts/check_theme_agents.py --self-test

--self-test plants one break of each rule in an in-memory copy of the real pages and fails unless
each is reported by its own rule, naming the thing it broke (and the unplanted copy is clean).
"""
import argparse
import base64
import html as htmllib
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import locales  # noqa: E402
import theme_agents as ta  # noqa: E402

PAGE = "themes/agents/index.html"
# dawn.json's base64 holds no '+', no '/' and no '=', so on its own it cannot tell a command that
# forgot the URL-safe alphabet or the padding from one that did not. These bytes encode to
# "Pj4+Pz8/Li4u" plus padding in standard base64: all three characters, asserted below.
ALPHABET_FIXTURE = b'{"x":">>>???..."}'
_std = base64.b64encode(ALPHABET_FIXTURE).decode()
assert "+" in _std and "/" in _std and "=" in _std, _std
MD = "themes/agents/index.md"


class Tables(HTMLParser):
    """Every <table data-theme-table="id">: {id: [row]}, a row being [cell], a cell
    {"text": str, "codes": [str]}. The first cell of a row is its <th scope="row">."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = {}
        self._id = None
        self._row = None
        self._cell = None
        self._code = False
        self._head = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table" and "data-theme-table" in a:
            self._id = a["data-theme-table"]
            self.tables[self._id] = []
        elif self._id is not None:
            if tag == "thead":
                self._head = True
            elif tag == "tr" and not self._head:
                self._row = []
            elif tag in ("td", "th") and self._row is not None:
                self._cell = {"text": "", "codes": [], "head": False}
            elif tag == "code" and self._cell is not None:
                self._code = True
                self._cell["codes"].append("")

    def handle_endtag(self, tag):
        if self._id is None:
            return
        if tag == "table":
            self._id = None
        elif tag == "thead":
            self._head = False
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.tables[self._id].append(self._row)
            self._row = None
        elif tag in ("td", "th") and self._cell is not None:
            self._cell["text"] = " ".join(self._cell["text"].split())
            self._row.append(self._cell)
            self._cell = None
        elif tag == "code":
            self._code = False

    def handle_data(self, data):
        if self._cell is not None:
            self._cell["text"] += data
            if self._code:
                self._cell["codes"][-1] += data


def read_tables(page_html: str) -> dict:
    p = Tables()
    p.feed(page_html)
    return p.tables


def first_code(cell: dict) -> str:
    return cell["codes"][0] if cell["codes"] else cell["text"]


def check_fields(loc: str, tables: dict, model: dict) -> list:
    found = []
    for t in model["tables"]:
        rows = tables.get(t["id"])
        if rows is None:
            found.append(("fields.missing", loc, f"table {t['id']} is not on the page"))
            continue
        got = {}
        for r in rows:
            if len(r) != 4:
                found.append(("fields.missing", loc, f"{t['id']}: a row with {len(r)} cells, not 4"))
                continue
            got[first_code(r[0])] = r
        want = {r["field"]: r for r in t["rows"]}
        for f in want:
            if f not in got:
                found.append(("fields.missing", loc, f"{t['label']}: `{f}` is decoded by the kit but not listed"))
        for f in got:
            if f not in want:
                found.append(("fields.extra", loc, f"{t['label']}: `{f}` is listed but the kit does not decode it"))
        for f, w in want.items():
            r = got.get(f)
            if r is None:
                continue
            presence = first_code(r[2])
            if presence != ("required" if w["required"] else "optional"):
                found.append(("fields.presence", loc, f"{t['label']}.{f}: listed {presence}, the kit has "
                              f"{'required' if w['required'] else 'optional'}"))
            if first_code(r[1]) != w["type"]:
                found.append(("fields.type", loc, f"{t['label']}.{f}: listed {first_code(r[1])}, the kit has {w['type']}"))
            if w["enum"] and r[3]["codes"] != w["enum"]:
                found.append(("fields.values", loc, f"{t['label']}.{f}: lists {r[3]['codes']}, "
                              f"the kit has {w['enum']}"))
            marked = ta.PUBLISH_MARK in " ".join(r[2]["codes"])
            if marked != bool(w["publish"]):
                found.append(("publish.mark", loc, f"{t['label']}.{f}: {'marked' if marked else 'not marked'} "
                              f"required to publish, the page defines {bool(w['publish'])}"))
    return found


def check_kinds(loc: str, tables: dict, model: dict) -> list:
    found = []
    rows = tables.get("kinds")
    if rows is None:
        return [("kinds.missing", loc, "the options-with-a-type table is not on the page")]
    got = {}
    for r in rows:
        if len(r) != 5:
            found.append(("kinds.missing", loc, f"kinds: a row with {len(r)} cells, not 5"))
            continue
        field = None if r[2]["text"] == ta.NONE_CELL else first_code(r[2])
        got[(first_code(r[0]), first_code(r[1]), field)] = r
    want = {(w["option"], w["kind"], w["field"]): w for w in model["kinds"]}
    show = lambda k: f"{k[0]} type {k[1]}" + (f" field `{k[2]}`" if k[2] else "")  # noqa: E731
    for k in want:
        if k not in got:
            found.append(("kinds.missing", loc, f"{show(k)} is allowed by the kit but not listed"))
    for k in got:
        if k not in want:
            found.append(("kinds.extra", loc, f"{show(k)} is listed but the kit does not allow it"))
    for k, w in want.items():
        r = got.get(k)
        if r is None or k[2] is None:
            continue
        presence = first_code(r[3])
        if presence != ("required" if w["required"] else "optional"):
            found.append(("kinds.presence", loc, f"{show(k)}: listed {presence}, the kit has "
                          f"{'required' if w['required'] else 'optional'}"))
        if first_code(r[4]) != w["type"]:
            found.append(("kinds.type", loc, f"{show(k)}: listed {first_code(r[4])}, the kit has {w['type']}"))
    return found


def check_numbers(loc: str, tables: dict, model: dict) -> list:
    found = []
    rows = tables.get("numbers")
    if rows is None:
        return [("numbers.missing", loc, "the numbers table is not on the page")]
    got = {first_code(r[0]): [first_code(c) for c in r[1:]] for r in rows if len(r) == 4}
    want = {p: [str(lo), str(hi), str(step)] for p, lo, hi, step in model["numbers"]}
    for p in want:
        if p not in got:
            found.append(("numbers.missing", loc, f"`{p}` is in ThemeNumbers.swift but not listed"))
    for p in got:
        if p not in want:
            found.append(("numbers.extra", loc, f"`{p}` is listed but ThemeNumbers.swift does not have it"))
    for p, w in want.items():
        if p in got and got[p] != w:
            found.append(("numbers.range", loc, f"`{p}`: listed min/max/step {got[p]}, ThemeNumbers.swift has {w}"))
    return found


def check_roles(loc: str, page_html: str, model: dict) -> list:
    m = re.search(r'<p data-theme-values="role">(.*?)</p>', page_html, re.S)
    return roles_found(loc, re.findall(r"<code>(.*?)</code>", m.group(1)) if m else None, model)


def roles_found(loc: str, got, model: dict) -> list:
    if got != model["roles"]:
        return [("roles.set", loc, f"lists {got}, PaletteRole has {model['roles']}")]
    return []


def pre_blocks(page_html: str) -> list:
    # A block wide enough to scroll is focusable and may be a labelled region (<pre tabindex="0" ...>, #271).
    return [htmllib.unescape(b) for b in re.findall(r"<pre(?: [^>]*)?><code>(.*?)</code></pre>", page_html, re.S)]


def run_recipe(command: str, file_bytes: bytes):
    """The payload the command prints after '#theme=' and the text before it, run by bash in a
    scratch folder holding theme.json."""
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "theme.json").write_bytes(file_bytes)
        out = subprocess.run(["bash", "-c", command], cwd=d, capture_output=True, text=True, timeout=30)
    return out.stdout


def check_example_and_recipe(loc: str, root: str, page_html: str) -> list:
    found = []
    dawn = ta.dawn_text()
    blocks = pre_blocks(page_html)
    if dawn not in blocks:
        found.append(("example.drift", loc, "no code block on the page is byte-equal to the vendored dawn theme.json"))
    command = ta.recipe(root)
    recipes = [b for b in blocks if b.startswith("printf ")]
    if len(recipes) != 1:
        return found + [("recipe.drift", loc, f"{len(recipes)} hand-off commands on the page, expected 1")]
    if recipes[0] != command:
        found.append(("recipe.drift", loc, f"the page's hand-off command is {recipes[0]!r}, the generator defines {command!r}"))
    dawn_bytes = (ta.swift.vendor_dir() / "Themes" / "dawn" / "theme.json").read_bytes()
    prefix = f"{ta.BASE_URL}{root}themes/new/#theme="
    for label, file_bytes in (("dawn.json", dawn_bytes), ("the alphabet fixture", ALPHABET_FIXTURE)):
        out = run_recipe(recipes[0], file_bytes)
        ok = out.startswith(prefix) and out.endswith("\n") and out.count("\n") == 1
        if ok:
            payload = out[len(prefix):-1]
            try:
                ok = (re.fullmatch(r"[A-Za-z0-9_-]+", payload) is not None
                      and base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)) == file_bytes)
            except Exception:
                ok = False
        if not ok:
            found.append(("recipe.broken", loc, f"run in bash on {label} it printed {out[:120]!r}, "
                          f"not {prefix}<base64url of the file>"))
    return found


MD_LABEL = "en/index.md"


def _md_cells(line: str) -> list:
    parts = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
    return [{"text": c, "codes": re.findall(r"`([^`]*)`", c)} for c in parts]


def read_md_tables(md: str) -> list:
    """Every pipe table of the Markdown twin, in order, as a list of rows of cells shaped like the
    HTML reader's ({"text", "codes"}); header and separator rows are left out."""
    tables, cur = [], None
    for line in md.splitlines():
        if line.startswith("|"):
            if cur is None:
                cur = []
                tables.append(cur)
            cur.append(line)
        else:
            cur = None
    out = []
    for lines in tables:
        out.append([_md_cells(l) for l in lines[2:]])  # [0] header, [1] |---|
    return out


def md_tables_by_id(md: str, model: dict) -> dict:
    """The twin's tables carry no ids; they are in the page's order: the model's field tables, then
    the options table, then the numbers table."""
    ids = [t["id"] for t in model["tables"]] + ["kinds", "numbers"]
    tables = read_md_tables(md)
    if len(tables) != len(ids):
        return {"__count__": len(tables)}
    return dict(zip(ids, tables))


def check_md(md: str, root: str = "/") -> list:
    found = []
    if ta.recipe(root) not in md:
        found.append(("md.twin", "en", "index.md does not carry the hand-off command"))
    if ta.dawn_text() not in md:
        found.append(("md.twin", "en", "index.md does not carry the Dawn example"))
    model = ta.model()
    tables = md_tables_by_id(md, model)
    if "__count__" in tables:
        return found + [("fields.missing", MD_LABEL, f"{tables['__count__']} tables, expected {len(model['tables']) + 2}")]
    found += check_fields(MD_LABEL, tables, model)
    found += check_kinds(MD_LABEL, tables, model)
    found += check_numbers(MD_LABEL, tables, model)
    m = re.search(r"A palette role is one of these names:\n\n(.*?)\n\n", md, re.S)
    found += roles_found(MD_LABEL, re.findall(r"`([^`]*)`", m.group(1)) if m else None, model)
    return found


def problems(pages: dict, md: str, served: list) -> list:
    """`pages` maps a locale to its themes/agents/index.html; `md` is the English index.md.
    Returns (rule, locale, detail)."""
    model = ta.model()
    found = []
    for loc in served:
        page_html = pages.get(loc)
        if page_html is None:
            found.append(("page.missing", loc, f"{PAGE} was not generated"))
            continue
        root = "/" if loc == "en" else f"/{loc}/"
        tables = read_tables(page_html)
        found += check_fields(loc, tables, model)
        found += check_kinds(loc, tables, model)
        found += check_numbers(loc, tables, model)
        found += check_roles(loc, page_html, model)
        found += check_example_and_recipe(loc, root, page_html)
    return found + check_md(md)


def load(root: Path):
    served = locales.enabled()
    pages = {}
    for loc in served:
        prefix = "" if loc == "en" else f"{loc}/"
        p = root / prefix / PAGE
        if p.is_file():
            pages[loc] = p.read_text(encoding="utf-8")
    md = (root / MD).read_text(encoding="utf-8") if (root / MD).is_file() else ""
    return pages, md, served


# --- Self-test --------------------------------------------------------------------------------

def _sub(html: str, old: str, new: str, count: int = 1) -> str:
    assert html.count(old) >= 1, f"plant anchor not found: {old[:80]!r}"
    return html.replace(old, new, count)


def _drop_row(html: str, table: str, first_cell: str, second: str = None) -> str:
    """Remove the first <tr> of `table` whose row header is `first_cell` (and, for the options table,
    whose second cell is `second`)."""
    start = html.index(f'data-theme-table="{table}"')
    end = html.index("</table>", start)
    chunk = html[start:end]
    for m in re.finditer(r'  <tr><th scope="row"><code>' + re.escape(first_cell) + r"</code></th>.*?</tr>", chunk):
        if second is None or f"<code>{second}</code>" in m.group(0):
            return html[:start] + chunk[:m.start()] + chunk[m.end():].lstrip("\n") + html[end:]
    raise AssertionError(f"plant anchor not found: row {first_cell} {second} in {table}")


def _row_html(html: str, table: str, first_cell: str, second: str = None) -> str:
    start = html.index(f'data-theme-table="{table}"')
    end = html.index("</table>", start)
    for m in re.finditer(r'  <tr><th scope="row"><code>' + re.escape(first_cell) + r"</code></th>.*?</tr>", html[start:end]):
        if second is None or f"<code>{second}</code>" in m.group(0):
            return m.group(0)
    raise AssertionError(f"plant anchor not found: row {first_cell} {second} in {table}")


def _replace_row(html: str, table: str, first_cell: str, new_row: str, second: str = None) -> str:
    old = _row_html(html, table, first_cell, second)
    return html.replace(old, new_row, 1)


def self_test(root: Path) -> int:
    pages, md, served = load(root)
    if "en" not in pages:
        print("self-test: no English page to plant into (run scripts/build_pages.py first)", file=sys.stderr)
        return 1
    en = pages["en"]
    clean = problems(pages, md, served)
    failures = []
    if clean:
        failures.append(f"the unplanted copy is not clean: {clean[:3]}")

    plants = []

    def plant(name, rule, needle, mutate, in_md=False):  # in_md: `mutate` takes the Markdown, not the en HTML
        plants.append((name, rule, needle, mutate, in_md))

    h2_row = _row_html(en, "style-h2", "letterSpacing")
    plant("an extra field", "fields.extra", "bogusKey",
          lambda h: _sub(h, h2_row, h2_row + h2_row.replace("letterSpacing", "bogusKey")))
    plant("a field dropped from style.h2", "fields.missing", "letterSpacing",
          lambda h: _drop_row(h, "style-h2", "letterSpacing"))
    plant("summary dropped from the root", "fields.missing", "summary", lambda h: _drop_row(h, "root", "summary"))
    plant("inlineCode dropped from style", "fields.missing", "inlineCode", lambda h: _drop_row(h, "style", "inlineCode"))
    plant("a required field marked optional", "fields.presence", "schemaVersion",
          lambda h: _replace_row(h, "root", "schemaVersion",
                                 _row_html(h, "root", "schemaVersion").replace("<code>required</code>", "<code>optional</code>")))
    plant("a wrong type token", "fields.type", "bodySize",
          lambda h: _replace_row(h, "style", "bodySize",
                                 _row_html(h, "style", "bodySize").replace("<code>number</code>", "<code>integer</code>")))
    plant("a font design dropped from the enum", "fields.values", "fontDesign",
          lambda h: _replace_row(h, "root", "fontDesign",
                                 _row_html(h, "root", "fontDesign").replace("<code>sans</code>, ", "")))
    plant("the publish mark removed from syntax", "publish.mark", "syntax",
          lambda h: _sub(h, " " + re.search(r"<code>optional</code> ((?:\(|（).*?(?:\)|）))", _row_html(h, "palette", "syntax")).group(1), ""))
    plant("hr 'line' without its kind", "kinds.missing", "type line",
          lambda h: _drop_row(_drop_row(h, "kinds", "style.hr.style", "line"), "kinds", "style.hr.style", "line"))
    plant("h1 decoration 'rule' dropped", "kinds.missing", "style.h1.decoration type rule",
          lambda h: _drop_row(h, "kinds", "style.h1.decoration", "rule"))
    plant("a `color` added to h1 decoration 'rule'", "kinds.extra", "field `color`",
          lambda h: _replace_row(h, "kinds", "style.h1.decoration",
                                 _row_html(h, "kinds", "style.h1.decoration", "rule").replace(ta.NONE_CELL + "</td>", "<code>color</code></td>", 1),
                                 "rule"))
    plant("table header 'filled' border marked required", "kinds.presence", "border", _border_required)
    plant("a wrong kind type token", "kinds.type", "color",
          lambda h: _replace_row(h, "kinds", "style.h1.decoration",
                                 _row_html(h, "kinds", "style.h1.decoration", "shortRule").replace("<code>role</code>", "<code>string</code>"),
                                 "shortRule"))
    plant("a role dropped", "roles.set", "quote",
          lambda h: _sub(h, "<code>quote</code>, ", ""))
    plant("a wrong range", "numbers.range", "style.bodySize",
          lambda h: _replace_row(h, "numbers", "style.bodySize",
                                 _row_html(h, "numbers", "style.bodySize").replace("<code>14</code>", "<code>13</code>")))
    plant("a wrong step", "numbers.range", "style.lineHeight",
          lambda h: _replace_row(h, "numbers", "style.lineHeight",
                                 _row_html(h, "numbers", "style.lineHeight").replace("<code>0.05</code>", "<code>0.1</code>")))
    plant("a number dropped", "numbers.missing", "style.radius", lambda h: _drop_row(h, "numbers", "style.radius"))
    plant("a number added", "numbers.extra", "style.bogus",
          lambda h: _sub(h, _row_html(h, "numbers", "style.radius"),
                         _row_html(h, "numbers", "style.radius") + _row_html(h, "numbers", "style.radius").replace("style.radius", "style.bogus")))
    plant("the Dawn example altered", "example.drift", "dawn",
          lambda h: _sub(h, '"id": "dawn"', '"id": "dawm"'))
    plant("the hand-off command's alphabet swapped", "recipe.broken", "the alphabet fixture",
          lambda h: _sub(h, "tr '+/' '-_'", "tr '+/' '_-'"))
    plant("the hand-off command's padding kept", "recipe.broken", "base64url",
          lambda h: _sub(h, "tr -d '\\n='", "tr -d '\\n'"))
    plant("the hand-off command pointing at another page", "recipe.drift", "generator defines",
          lambda h: _sub(h, "themes/new/#theme=", "themes/gallery/#theme="))
    plant("the Markdown twin without the command", "md.twin", "hand-off command",
          lambda m: _sub(m, ta.recipe("/"), "printf nothing"), in_md=True)

    def md_row(m, first):
        return next(l for l in m.splitlines() if l.startswith(f"| `{first}` |"))
    # F1: the Markdown twin's tables are held to the Swift too (reported under en/index.md)
    plant("md: the license row dropped", "fields.missing", "license",
          lambda m: m.replace(md_row(m, "license") + "\n", "", 1), in_md=True)
    plant("md: fontDesign flipped to optional", "fields.presence", "fontDesign",
          lambda m: m.replace(md_row(m, "fontDesign"), md_row(m, "fontDesign").replace("`required`", "`optional`"), 1), in_md=True)
    plant("md: an extra row", "fields.extra", "bogusKey",
          lambda m: m.replace(md_row(m, "license"), md_row(m, "license") + "\n" + md_row(m, "license").replace("license", "bogusKey"), 1), in_md=True)
    plant("md: a wrong type token", "fields.type", "fontDesign",
          lambda m: m.replace(md_row(m, "fontDesign"), md_row(m, "fontDesign").replace("`enum`", "`string`", 1), 1), in_md=True)
    plant("md: a role dropped", "roles.set", "quote", lambda m: _sub(m, "`quote`, `keyword`", "`keyword`"), in_md=True)
    plant("md: a number range changed", "numbers.range", "style.bodySize",
          lambda m: m.replace(md_row(m, "style.bodySize"), md_row(m, "style.bodySize").replace("`14`", "`13`", 1), 1), in_md=True)
    # F2: an extra enum value is as wrong as a missing one
    plant("an extra font design listed", "fields.values", "fontDesign",
          lambda h: _replace_row(h, "root", "fontDesign",
                                 _row_html(h, "root", "fontDesign").replace("<code>rounded</code>", "<code>rounded</code>, <code>mono</code>")))
    plant("an extra scenario listed", "fields.values", "scenarios",
          lambda h: _replace_row(h, "root", "scenarios",
                                 _row_html(h, "root", "scenarios").replace("<code>notes-sharing</code>", "<code>notes-sharing</code>, <code>poetry</code>")))
    plant("an extra align value listed", "fields.values", "align",
          lambda h: _replace_row(h, "style-h1", "align",
                                 re.sub(r"(<code>center</code>)", r"\1, <code>right</code>", _row_html(h, "style-h1", "align"), 1)))

    for name, rule, needle, mutate, in_md in plants:
        planted = dict(pages)
        planted_md = md
        if in_md:
            planted_md = mutate(md)
            assert planted_md != md, f"plant {name!r} changed nothing"
        else:
            planted["en"] = mutate(en)
            assert planted["en"] != en, f"plant {name!r} changed nothing"
        found = problems(planted, planted_md, served)
        want_loc = MD_LABEL if name.startswith("md:") else None  # an md plant must be reported under the md's label
        hit = [f for f in found if f[0] == rule and needle in f[2] and (want_loc is None or f[1] == want_loc)]
        if not hit:
            failures.append(f"plant {name!r}: expected {rule} naming {needle!r}, got {[(f[0], f[2][:70]) for f in found] or 'nothing'}")
        else:
            print(f"  planted: {name} -> {hit[0][0]}: {hit[0][2][:90]}")

    # A locale page that is not there at all.
    gone = dict(pages)
    gone.pop(served[-1])
    found = problems(gone, md, served)
    if not any(f[0] == "page.missing" and f[1] == served[-1] for f in found):
        failures.append(f"a missing {served[-1]} page: expected page.missing, got {found[:2]}")
    else:
        print(f"  planted: no {served[-1]} page -> page.missing")

    # A page whose Swift has a shape the parser does not know must fail loudly, not pass.
    import theme_kit_swift as sw
    saved = ta.swift.parse
    try:
        def shaky(vendor=None):
            raise sw.SwiftShapeError("planted: an init(from:) the reader does not know")
        ta.swift.parse = shaky
        try:
            ta.model()
            failures.append("an unreadable Swift shape did not raise")
        except sw.SwiftShapeError as e:
            print(f"  planted: unreadable Swift -> SwiftShapeError: {e}")
    finally:
        ta.swift.parse = saved

    for f in failures:
        print(f"SELF-TEST FAIL: {f}", file=sys.stderr)
    if failures:
        return 1
    print(f"self-test: the unplanted copy is clean; {len(plants) + 2} plants each reported by their own rule")
    return 0


def _border_required(html: str) -> str:
    # the 'filled' rows are one per field; the border row is the one that names it
    start = html.index('data-theme-table="kinds"')
    end = html.index("</table>", start)
    for m in re.finditer(r'  <tr><th scope="row"><code>style\.table\.header</code></th>.*?</tr>', html[start:end]):
        if "<code>filled</code>" in m.group(0) and "<code>border</code>" in m.group(0):
            return html.replace(m.group(0), m.group(0).replace("<code>optional</code>", "<code>required</code>"), 1)
    raise AssertionError("plant anchor not found: filled.border")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default="public")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    if not root.is_absolute():
        root = ROOT / root
    if args.self_test:
        return self_test(root)
    pages, md, served = load(root)
    found = problems(pages, md, served)
    for rule, loc, detail in found:
        print(f"{rule}: [{loc}] {detail}", file=sys.stderr)
    if found:
        print(f"{len(found)} problem(s) in /themes/agents/", file=sys.stderr)
        return 1
    print(f"/themes/agents/ matches the kit in {len(served)} locale(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
