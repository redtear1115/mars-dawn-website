"""The /themes/agents/ page (plan PLAN-web-theme-tuning W3): a reference an agent can read to make a
MarsDawn theme without running any script.

Two halves, kept apart on purpose:

* `model()` is what the kit says: every field of theme.json with its type, whether it is required,
  its value set and its range, read by scripts/theme_kit_swift.py from the three Swift files and
  ThemeNumbers.swift that scripts/sync_theme_kit.py vendors. scripts/check_theme_agents.py asks it
  the same question and compares the answer with the built pages.
* `render_body()` / `page()` lay that model out as HTML tables around a locale's prose (`copy`, a
  flat dict of strings written in build_pages.py for en and zh-hant, in scripts/copy_<l>.py for
  the rest). Names of fields, rule ids, types and commands are never translated.

A field the kit has and the page cannot describe (a `String` with no note, a `Double` with no
entry in ThemeNumbers.swift, a type this file has not heard of) raises, so the build fails instead
of publishing a table with a hole in it.
"""
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import sync_theme_kit as sync  # noqa: E402
import theme_kit_swift as swift  # noqa: E402

BASE_URL = "https://marsdawn.southern-light.dev"
ISSUE_FORM_URL = "https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml"
CONTRIBUTING_URL = "https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md"
BUILT_INS = ["dawn", "classic", "modern", "vivid"]

# The commands the page gives, in the order of `marsdawn theme validate --help`'s usage line.
CLI_LINES = [
    "marsdawn theme validate theme.json --require-complete --json",
    "marsdawn theme css theme.json --json",
    "marsdawn theme preview theme.json --appearance light -o light.png",
    "marsdawn theme preview theme.json --appearance dark -o dark.png",
]
# The hand-off link, in one line that works in zsh and bash on macOS and Linux (GNU base64 wraps
# its output, BSD's does not: `tr -d '\n='` takes both).
RECIPE = ("printf '{origin}{root}themes/new/#theme=%s\\n' "
          "\"$(base64 < theme.json | tr -d '\\n=' | tr '+/' '-_')\"")
MAX_FILE_BYTES = 16384

# Tables of keyed objects, in page order: (table id, Swift type, label the page shows).
FIELD_TABLES = [
    ("root", "ThemeDocument", "theme.json"),
    ("author", "ThemeAuthor", "author"),
    ("palette", "ThemeColors", "light, dark"),
    ("syntax-colors", "ThemeSyntaxColors", "syntax"),
    ("diagram-colors", "ThemeDiagramColors", "diagram"),
    ("style", "ThemeStyle", "style"),
    ("style-h1", "H1", "style.h1"),
    ("style-h2", "H2", "style.h2"),
    ("style-blockquote", "Blockquote", "style.blockquote"),
    ("style-hr", "Hr", "style.hr"),
    ("style-table", "Table", "style.table"),
    ("style-link", "LinkOptions", "style.link"),
    ("style-syntax", "SyntaxOptions", "style.syntax"),
]
# The five `type`-tagged objects: Swift type -> the option's path in theme.json.
KIND_OPTIONS = {
    "H1Decoration": "style.h1.decoration",
    "H2Decoration": "style.h2.decoration",
    "BlockquoteStyle": "style.blockquote.style",
    "HrStyle": "style.hr.style",
    "TableHeader": "style.table.header",
}
KINDS_LABEL = "type"
# Where a Double field's ThemeNumber path starts, per table.
NUMBER_PREFIX = {"style": "", "style-h1": "h1.", "style-h2": "h2."}
# The two palette groups that are optional to the parser but required to publish.
PUBLISH_FIELDS = {("palette", "syntax"), ("palette", "diagram")}
# Fields that need a sentence the Swift cannot give (its format, its limit), as copy keys n_<key>.
NOTE_FOR = {
    ("root", "schemaVersion"): "schemaVersion",
    ("root", "id"): "id",
    ("root", "version"): "version",
    ("root", "name"): "name",
    ("root", "summary"): "summary",
    ("root", "scenarios"): "scenarios",
    ("root", "license"): "license",
    ("author", "name"): "author_name",
    ("author", "github"): "author_github",
    ("style", "inlineCode"): "inline_code",
    ("kinds", "colors"): "gradient",
}
HEX_TABLES = {"palette", "syntax-colors", "diagram-colors"}  # their String fields are colours
# Swift type -> the type token the page prints.
SCALARS = {"String": "string", "Int": "integer", "Double": "number", "Bool": "boolean", "PaletteRole": "role",
           "[PaletteRole]": "role[]", "LocalizedText": "map", "ThemeFontDesign": "enum", "Align": "enum",
           "[ThemeScenario]": "enum[]"}
PUBLISH_MARK = "--require-complete"
NONE_CELL = "—"  # a kind that takes no fields


class PageError(RuntimeError):
    """The kit has something this page does not know how to show."""


def _token(swift_type: str, parsed: dict) -> str:
    if swift_type in SCALARS:
        return SCALARS[swift_type]
    if swift_type in parsed["keyed"] or swift_type in parsed["kinds"]:
        return "object"
    raise PageError(f"no type token for the Swift type {swift_type!r}")


def _enum_values(swift_type: str, parsed: dict):
    name = swift_type.strip("[]")
    return parsed["enums"][name] if name in parsed["enums"] and name != "PaletteRole" else None


def _object_table(swift_type: str):
    for table_id, type_name, _ in FIELD_TABLES:
        if type_name == swift_type:
            return table_id
    if swift_type in KIND_OPTIONS:
        return "kinds"
    raise PageError(f"no table for the object type {swift_type!r}")


def model(vendor: Path = None) -> dict:
    """What the kit says, in the shape the page and its check share:
    {"tables": [{"id", "label", "rows": [...]}], "kinds": [rows], "numbers": [(path, lo, hi, step)],
     "roles": [...]}. Raises swift.SwiftShapeError or PageError on anything unknown."""
    vendor = vendor or swift.vendor_dir()
    parsed = swift.parse(vendor)
    scalar = sync.parse_scalar_options((vendor / "ThemeNumbers.swift").read_text(encoding="utf-8"))
    numbers = [(f"style.{path}", lo, hi, step) for path, lo, hi, step in scalar.values()]
    number_paths = {n[0] for n in numbers}

    shown = {type_name for _, type_name, _ in FIELD_TABLES}
    if set(parsed["keyed"]) != shown:
        raise PageError(f"the kit has keyed objects {sorted(set(parsed['keyed']) ^ shown)} the page does not show")
    if set(parsed["kinds"]) != set(KIND_OPTIONS):
        raise PageError(f"the kit has type-tagged objects {sorted(set(parsed['kinds']) ^ set(KIND_OPTIONS))} the page does not show")

    used_numbers = set()
    tables = []
    for table_id, type_name, label in FIELD_TABLES:
        rows = []
        for f in parsed["keyed"][type_name]:
            token = _token(f["type"], parsed)
            row = {"field": f["name"], "type": token, "required": f["required"],
                   "enum": _enum_values(f["type"], parsed), "number": None,
                   "object": _object_table(f["type"]) if token == "object" else None,
                   "publish": (table_id, f["name"]) in PUBLISH_FIELDS}
            if token == "number":
                path = "style." + NUMBER_PREFIX.get(table_id, "\0") + f["name"]
                if path not in number_paths:
                    raise PageError(f"{table_id}.{f['name']} is a number with no entry in ThemeNumbers.swift ({path})")
                row["number"] = path
                used_numbers.add(path)
            rows.append(row)
        tables.append({"id": table_id, "label": label, "rows": rows})

    kind_rows = []
    for type_name, option in KIND_OPTIONS.items():
        for kind, fields in parsed["kinds"][type_name].items():
            if not fields:
                kind_rows.append({"option": option, "kind": kind, "field": None, "type": None, "required": None, "number": None})
            for f in fields:
                token = _token(f["type"], parsed)
                row = {"option": option, "kind": kind, "field": f["name"], "type": token, "required": f["required"], "number": None}
                if token == "number":
                    path = f"{option}.{f['name']}"
                    if path not in number_paths:
                        raise PageError(f"{option} {kind}.{f['name']} is a number with no entry in ThemeNumbers.swift ({path})")
                    row["number"] = path
                    used_numbers.add(path)
                elif token not in ("role", "role[]"):
                    raise PageError(f"{option} {kind}.{f['name']}: a {token} the page does not show")
                kind_rows.append(row)
    if used_numbers != number_paths:
        raise PageError(f"ThemeNumbers.swift has numbers no field uses: {sorted(number_paths - used_numbers)}")
    return {"tables": tables, "kinds": kind_rows, "numbers": numbers, "roles": parsed["enums"]["PaletteRole"]}


# --- Layout -----------------------------------------------------------------------------------

def _e(text: str) -> str:
    return html.escape(text, quote=False)


def _code(text: str) -> str:
    return f"<code>{_e(text)}</code>"


def _codes(values: list) -> str:
    return ", ".join(_code(v) for v in values)


def _note(copy: dict, table_id: str, field: str):
    key = NOTE_FOR.get((table_id, field))
    return copy["n_" + key] if key else None


def _values_cell(copy: dict, table_id: str, row: dict) -> str:
    parts = []
    note = _note(copy, table_id, row["field"])
    if row["enum"]:
        parts.append(_codes(row["enum"]))
    elif row["type"] in ("role", "role[]"):
        parts.append(f'<a href="#roles">{copy["see_roles"]}</a>')
    elif row["type"] == "number":
        parts.append(f'<a href="#t-numbers">{copy["see_ranges"]}</a>')
    elif row["type"] == "boolean":
        parts.append(_codes(["true", "false"]))
    elif row["type"] == "object":
        target = row["object"]
        label = KINDS_LABEL if target == "kinds" else next(l for i, _, l in FIELD_TABLES if i == target)
        parts.append(f'<a href="#t-{target}">{_code(label)}</a>')
    elif row["type"] == "string" and table_id in HEX_TABLES:
        note = copy["n_hex"]
    if note:
        parts.append(note)
    if not parts:
        raise PageError(f"{table_id}.{row['field']} ({row['type']}) has nothing to say about its values: add a note")
    return " &#8212; ".join(parts)


def _presence_cell(copy: dict, row: dict) -> str:
    cell = _code("required" if row["required"] else "optional")
    if row.get("publish"):
        cell += " " + copy["publish_note"]
    return cell


def _table(table_id: str, heads: list, rows: list) -> str:
    head = "".join(f'<th scope="col">{h}</th>' for h in heads)
    return (f'<div class="table-scroll"><table class="compare compare-wide" data-theme-table="{table_id}">\n'
            f"<thead><tr>{head}</tr></thead>\n<tbody>\n" + "\n".join(rows) + "\n</tbody>\n</table></div>")


def _row(first: str, cells: list, heads: list) -> str:
    tds = "".join(f'<td data-label="{_e(h)}">{c}</td>' for h, c in zip(heads[1:], cells))
    return f'  <tr><th scope="row">{first}</th>{tds}</tr>'


def _field_table(copy: dict, table: dict) -> str:
    heads = [copy["c_field"], copy["c_type"], copy["c_presence"], copy["c_values"]]
    rows = [_row(_code(r["field"]), [_code(r["type"]), _presence_cell(copy, r), _values_cell(copy, table["id"], r)], heads)
            for r in table["rows"]]
    return (f'<h3 id="t-{table["id"]}">{_code(table["label"])}</h3>\n' + _table(table["id"], heads, rows))


def _kinds_table(copy: dict, kind_rows: list) -> str:
    heads = [copy["c_option"], copy["c_kind"], copy["c_field"], copy["c_presence"], copy["c_type"]]
    rows = []
    for r in kind_rows:
        if r["field"] is None:
            cells = [_code(r["kind"]), NONE_CELL, NONE_CELL, NONE_CELL]
        else:
            type_cell = _code(r["type"])
            if r["number"]:
                type_cell += f' <a href="#t-numbers">{copy["see_ranges"]}</a>'
            note = _note(copy, "kinds", r["field"])
            if note and r["type"] == "role[]":
                type_cell += " " + note
            cells = [_code(r["kind"]), _code(r["field"]), _code("required" if r["required"] else "optional"), type_cell]
        rows.append(_row(_code(r["option"]), cells, heads))
    return f'<h3 id="t-kinds">{copy["h_kinds"]}</h3>\n<p>{copy["kinds_intro"]}</p>\n' + _table("kinds", heads, rows)


def _numbers_table(copy: dict, numbers: list) -> str:
    heads = [copy["c_field"], copy["c_min"], copy["c_max"], copy["c_step"]]
    rows = [_row(_code(path), [_code(str(lo)), _code(str(hi)), _code(str(step))], heads) for path, lo, hi, step in numbers]
    return f'<h3 id="t-numbers">{copy["h_numbers"]}</h3>\n<p>{copy["numbers_intro"]}</p>\n' + _table("numbers", heads, rows)


def dawn_text() -> str:
    return (swift.vendor_dir() / "Themes" / "dawn" / "theme.json").read_text(encoding="utf-8").strip("\n")


def recipe(root: str) -> str:
    return RECIPE.format(origin=BASE_URL, root=root)


def render_body(root: str, copy: dict) -> str:
    """The page body for the locale whose URL root is `root` ("/" or "/zh-hant/"), from the kit's
    model and that locale's prose."""
    m = model()
    pre = lambda text: f"<pre><code>{_e(text)}</code></pre>"  # noqa: E731
    built_ins = "\n".join(
        f'  <li><a href="/assets/theme-sim/kit/themes/{b}.json"><code>/assets/theme-sim/kit/themes/{b}.json</code></a>: {copy["start_" + b]}</li>'
        for b in BUILT_INS)
    li = lambda items: "\n".join(f"  <li>{i}</li>" for i in items)  # noqa: E731
    return f"""
<section class="intro">
  <h1>{copy["h1"]}</h1>
  <p>{copy["lede"]}</p>
</section>

<div class="summary"><p>{copy["summary"]}</p></div>

<h2>{copy["what_h"]}</h2>
<ul>
{li(copy["what_items"])}
</ul>
<p>{copy["what_note"]}</p>

<h2>{copy["loop_h"]}</h2>
<p>{copy["loop_intro"]}</p>
{pre(chr(10).join(CLI_LINES))}
<ul>
{li(copy["loop_items"])}
</ul>

<h2>{copy["start_h"]}</h2>
<p>{copy["start_intro"]}</p>
<ul>
{built_ins}
</ul>
<h3 id="example-dawn">{copy["ex_h"]}</h3>
<p>{copy["ex_intro"]}</p>
{pre(dawn_text())}

<h2>{copy["fields_h"]}</h2>
<p>{copy["fields_intro"]}</p>
<p>{copy["types_note"]}</p>
{chr(10).join(_field_table(copy, t) for t in m["tables"])}
{_kinds_table(copy, m["kinds"])}
<h3 id="roles">{copy["h_roles"]}</h3>
<p>{copy["roles_intro"]}</p>
<p data-theme-values="role">{_codes(m["roles"])}</p>
{_numbers_table(copy, m["numbers"])}

<h2>{copy["rules_h"]}</h2>
<ul>
{li(copy["rules_items"])}
</ul>

<h2>{copy["link_h"]}</h2>
<p>{copy["link_intro"]}</p>
{pre(recipe(root))}
<p>{copy["link_note"]}</p>

<h2>{copy["submit_h"]}</h2>
<p>{copy["submit_intro"]}</p>
<ul>
{li([copy["submit_issue"].replace("{issue_url}", ISSUE_FORM_URL), copy["submit_pr"].replace("{contributing_url}", CONTRIBUTING_URL)])}
</ul>
<p>{copy["submit_note"]}</p>

<h2>{copy["gallery_h"]}</h2>
<p>{copy["gallery_p"]}</p>
"""


def localise_links(body: str, root: str) -> str:
    """The prose is written with site-absolute links for the English page; a locale's own pages
    live under its root."""
    if root == "/":
        return body
    for path in ("/themes/new/", "/themes/gallery/", "/cli/agents/", "/cli/skill/"):
        body = body.replace(f'href="{path}"', f'href="{root}{path[1:]}"')
    return body


def page(root: str, copy: dict) -> dict:
    return {"title": copy["title"], "description": copy["description"],
            "body": localise_links(render_body(root, copy), root)}
