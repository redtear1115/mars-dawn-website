"""Reads the fields of theme.json out of the kit's own Swift, for /themes/agents/ (plan
PLAN-web-theme-tuning W3, Rev 3.7-3.9).

The three files scripts/sync_theme_kit.py vendors beside ThemeNumbers.swift -- ThemeDocument.swift,
ThemeStyle.swift and PaletteRole.swift -- decode every object of a theme.json in one of two ways,
and this reads both:

* **A keyed object**: an `init(from:)` that starts with `rejectUnknownKeys(decoder, keyedBy:
  CodingKeys.self)`. Its fields are that type's `CodingKeys`. A field is required when it is read
  with `.decode(` and optional when it is read with `.decodeIfPresent(`; its type is the type
  argument of that call (`Int`, `String`, `PaletteRole`, `[PaletteRole]`, `H1`, ...).
* **A discriminated object** (`extension ThemeStyle.X: Codable` with a `Kind` enum): its `type`
  values are the `Kind` cases, and the fields of each kind are the `allowed: [...]` array in that
  kind's `case .<kind>:` branch of the init, minus "type". Required or optional is `decode` versus
  `decodeIfPresent` in the same branch. The shared `Key` enum is not a source.

Anything this does not recognise raises `SwiftShapeError`, loudly, the way
sync_theme_kit.parse_scalar_options does with ThemeNumbers.swift: a kit change to the shape of these
files breaks the build here instead of producing a page that quietly stops matching. The one
object it is told to skip is `LocalizedText`, whose own `init` is a plain `[String: String]` map
(ThemeDocument.swift `LocalizedText`); the page says its shape in prose.

Value sets come from `enum NAME: String` declarations (`PaletteRole`, `ThemeScenario`,
`ThemeFontDesign`, `Align`): the raw value of a case is its name, or its `= "..."` literal.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
SWIFT_FILES = ["ThemeDocument.swift", "ThemeStyle.swift", "PaletteRole.swift"]

# Types whose init(from:) is not a keyed or a discriminated object, and what the page says of them.
OPAQUE_TYPES = {"LocalizedText"}
# The enums whose cases are value sets of some field.
ENUM_NAMES = ["PaletteRole", "ThemeScenario", "ThemeFontDesign", "Align"]
# The five discriminated extensions, as written after `extension ThemeStyle.`.
DISCRIMINATED = ["H1Decoration", "H2Decoration", "BlockquoteStyle", "HrStyle", "TableHeader"]


class SwiftShapeError(RuntimeError):
    """The Swift is not in a shape this reader knows. Carries the file and the type."""


def vendor_dir() -> Path:
    root = ROOT / "vendor" / "kit-themes"
    dirs = sorted(p for p in root.iterdir() if p.is_dir()) if root.is_dir() else []
    if len(dirs) != 1:
        raise SwiftShapeError(f"expected exactly one vendor/kit-themes/<sha>/, found {[d.name for d in dirs]}")
    return dirs[0]


def _strip_comments(text: str) -> str:
    return "\n".join(line.split("//", 1)[0] for line in text.splitlines())


def _block(text: str, open_index: int) -> str:
    """The text between the `{` at open_index and its matching `}`."""
    assert text[open_index] == "{"
    depth = 0
    for i in range(open_index, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[open_index + 1:i]
    raise SwiftShapeError("unbalanced braces")


def _enum_cases(body: str, where: str) -> list:
    """The case names (or raw-value literals) of an enum whose text after its `{` is `body`.
    Reads the leading `case` lines only: a `var` or a `func` ends the declarations."""
    cases = []
    for line in body.splitlines():
        line = line.strip()
        if line.endswith("}"):
            line = line[:-1].strip()
        if not line:
            continue
        if not line.startswith("case "):
            break
        for part in line[len("case "):].split(","):
            part = part.strip()
            if not part:
                continue
            m = re.match(r'^([A-Za-z0-9_]+)(?:\s*=\s*"([^"]*)")?$', part)
            if not m:
                raise SwiftShapeError(f"{where}: unreadable enum case {part!r}")
            cases.append(m.group(2) if m.group(2) is not None else m.group(1))
    if not cases:
        raise SwiftShapeError(f"{where}: no enum cases read")
    return cases


def _enum_named(text: str, name: str, where: str) -> list:
    m = re.search(rf"enum\s+{re.escape(name)}\b[^{{]*\{{", text)
    if not m:
        raise SwiftShapeError(f"{where}: no `enum {name}` found")
    return _enum_cases(text[m.end():], f"{where} enum {name}")


INIT = re.compile(r"init\(from decoder: Decoder\) throws \{")
_DECODE = re.compile(r"\.(decode|decodeIfPresent)\(\s*(\[?[A-Za-z0-9_]+\]?)\.self\s*,\s*forKey:\s*\.([A-Za-z0-9_]+)\s*\)")


_DECL = re.compile(r"\b(?:struct|enum|extension)\s+([A-Za-z0-9_.]+)[^{;]*\{")


def _enclosing(text: str, pos: int):
    """(name, block start, block text) of the innermost struct, enum or extension whose braces
    contain `pos`."""
    best = None
    for m in _DECL.finditer(text):
        if m.end() > pos:
            break
        body = _block(text, m.end() - 1)
        if m.end() + len(body) >= pos and (best is None or len(body) < len(best[2])):
            best = (m.group(1), m.end(), body)
    if best is None:
        raise SwiftShapeError("an init(from:) outside any type")
    return best


def _coding_keys(body: str, where: str) -> list:
    """The cases of the first `enum CodingKeys` in a type's body."""
    m = re.compile(r"enum\s+CodingKeys\b[^{]*\{").search(body)
    if not m:
        raise SwiftShapeError(f"{where}: no CodingKeys")
    return _enum_cases(body[m.end():], f"{where} CodingKeys")


def parse_keyed(text: str) -> dict:
    """{type name: [{"name", "type", "required"} ...]} for every keyed object in `text` (comments
    stripped by the caller)."""
    out = {}
    for m in INIT.finditer(text):
        type_name, _, type_body = _enclosing(text, m.start())
        body = _block(text, m.end() - 1)
        if "rejectUnknownKeys(decoder, keyedBy: CodingKeys.self)" not in body:
            continue  # discriminated objects and opaque ones are read elsewhere
        keys = _coding_keys(type_body, type_name)
        fields = []
        for dm in _DECODE.finditer(body):
            fields.append({"name": dm.group(3), "type": dm.group(2), "required": dm.group(1) == "decode"})
        if [f["name"] for f in fields] != keys:
            raise SwiftShapeError(
                f"{type_name}: the decode calls {[f['name'] for f in fields]} are not its CodingKeys {keys}")
        if type_name in out:
            raise SwiftShapeError(f"{type_name}: declared twice")
        out[type_name] = fields
    return out


def parse_discriminated(text: str) -> dict:
    """{type name: {kind: [{"name", "type", "required"} ...]}} for the five `type`-tagged objects."""
    out = {}
    for name in DISCRIMINATED:
        m = re.search(rf"extension\s+ThemeStyle\.{name}\s*:\s*Codable\s*\{{", text)
        if not m:
            raise SwiftShapeError(f"{name}: no `extension ThemeStyle.{name}: Codable`")
        ext = _block(text, m.end() - 1)
        kinds = _enum_named(ext, "Kind", name)
        im = re.search(r"init\(from decoder: Decoder\) throws \{", ext)
        if not im:
            raise SwiftShapeError(f"{name}: no init(from:)")
        body = _block(ext, im.end() - 1)
        branches = list(re.finditer(r"^\s*case\s+\.([A-Za-z0-9_]+)\s*:", body, re.M))
        if [b.group(1) for b in branches] != kinds:
            raise SwiftShapeError(f"{name}: switch branches {[b.group(1) for b in branches]} are not the Kind cases {kinds}")
        by_kind = {}
        for i, b in enumerate(branches):
            end = branches[i + 1].start() if i + 1 < len(branches) else len(body)
            branch = body[b.end():end]
            am = re.search(r"rejectUnknownKeys\(decoder, allowed:\s*\[([^\]]*)\]\)", branch)
            if not am:
                raise SwiftShapeError(f"{name}.{b.group(1)}: no `rejectUnknownKeys(decoder, allowed: [...])`")
            allowed = re.findall(r'"([^"]*)"', am.group(1))
            if not allowed or allowed[0] != "type":
                raise SwiftShapeError(f"{name}.{b.group(1)}: `allowed` does not start with \"type\": {allowed}")
            decodes = {dm.group(3): (dm.group(2), dm.group(1) == "decode") for dm in _DECODE.finditer(branch)}
            fields = []
            for field in allowed[1:]:
                if field not in decodes:
                    raise SwiftShapeError(f"{name}.{b.group(1)}: `{field}` is allowed but never decoded")
                ftype, required = decodes[field]
                fields.append({"name": field, "type": ftype, "required": required})
            if set(decodes) - set(allowed[1:]):
                raise SwiftShapeError(f"{name}.{b.group(1)}: decodes {sorted(set(decodes) - set(allowed[1:]))} that `allowed` omits")
            by_kind[b.group(1)] = fields
        out[name] = by_kind
    return out


def parse(vendor: Path = None) -> dict:
    """Everything the page's tables are made of:
    {"keyed": {type: [fields]}, "kinds": {type: {kind: [fields]}}, "enums": {name: [values]}}.
    Raises SwiftShapeError on anything it does not recognise."""
    vendor = vendor or vendor_dir()
    texts = {}
    for name in SWIFT_FILES:
        path = vendor / name
        if not path.is_file():
            raise SwiftShapeError(f"{name}: not vendored in {vendor.name}/ (run scripts/sync_theme_kit.py)")
        texts[name] = _strip_comments(path.read_text(encoding="utf-8"))
    whole = "\n".join(texts.values())

    keyed = {}
    for name in ("ThemeDocument.swift", "ThemeStyle.swift"):
        for type_name, fields in parse_keyed(texts[name]).items():
            if type_name in keyed:
                raise SwiftShapeError(f"{type_name}: declared in two files")
            keyed[type_name] = fields
    # Every init(from:) must be one of: keyed, discriminated (an extension), or opaque.
    for name in ("ThemeDocument.swift", "ThemeStyle.swift"):
        for m in INIT.finditer(texts[name]):
            owner = _enclosing(texts[name], m.start())[0]
            if not (owner in keyed or owner in OPAQUE_TYPES or owner.startswith("ThemeStyle.")):
                raise SwiftShapeError(f"{owner}: an init(from:) that is neither keyed, discriminated nor opaque")
    kinds = parse_discriminated(texts["ThemeStyle.swift"])
    enums = {}
    for name in ENUM_NAMES:
        enums[name] = _enum_named(whole, name, name)
    return {"keyed": keyed, "kinds": kinds, "enums": enums}


if __name__ == "__main__":
    import json
    print(json.dumps(parse(), indent=2))
