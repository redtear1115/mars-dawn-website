#!/usr/bin/env python3
"""One-shot application of #383's Print & Export panel copy from the pinned TABLE_A.

Checks all eight old /pdf/ figure alts before writing. Adds a separate figure so /features/
can keep using the PDF viewer. Stops if any of the new figure entries already exist.

    python3 -I -B scripts/copy383/apply_panel.py --dry-run   # check every match, write nothing
    python3 -I -B scripts/copy383/apply_panel.py             # write
"""
import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from copy383.apply import Stop, exactly_once, lit  # noqa: E402
from copy383.data import TABLE_A  # noqa: E402

BUILT_IN = {"en": "en", "zh-Hant": "zh-hant"}
CALLOUTS = ("co1", "co2", "co3")


def proposed(locale: str, key: str, quote: str) -> str:
    return lit(TABLE_A[locale][key][1], quote)


def built_in_entry() -> str:
    quote = '"'

    def labels(key, sep=", "):
        return sep.join(f'"{lang}": {proposed(locale, key, quote)}' for locale, lang in BUILT_IN.items())

    alt = labels("fig_alt", ",\n            ")
    return f"""    "print-export": {{
        "image": "06-print-export",
        "alt": {{
            {alt},
        }},
        "callouts": [
            (20.83, 48.89, "l", {{{labels("co1")}}}),
            (78.19, 33.56, "r", {{{labels("co2")}}}),
            (71.60, 78.00, "r", {{{labels("co3")}}}),
        ],
    }},"""


def locale_entry(locale: str) -> str:
    quote = "'"
    alt = proposed(locale, "fig_alt", quote)
    callouts = ", ".join(proposed(locale, key, quote) for key in CALLOUTS)
    return f"""        'print-export': {{
            "alt": {alt},
            "callouts": [{callouts}],
        }},"""


def add_figure(path: str, name: str, indent: str, locales: dict, entry: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    start = exactly_once(text, f"{indent}{name} = {{\n", path)
    lineno = text.count("\n", 0, start) + 1
    table = next((node.value for node in ast.walk(ast.parse(text, filename=path))
                  if isinstance(node, ast.Assign) and node.lineno == lineno), None)
    if not isinstance(table, ast.Dict):
        raise Stop(f"{path}: expected a literal {name} dictionary")
    keys = [key.value if isinstance(key, ast.Constant) else None for key in table.keys]
    if "print-export" in keys:
        raise Stop(f"{path}: print-export already exists in {name}")
    if keys.count("pdf") != 1:
        raise Stop(f"{path}: found {keys.count('pdf')} pdf entries in {name}, expected exactly once")
    pdf = table.values[keys.index("pdf")]
    old_alt = ast.literal_eval(pdf)["alt"]
    for locale, lang in locales.items():
        exactly_once(old_alt[lang] if lang else old_alt, TABLE_A[locale]["fig_alt"][0], f"{path} {locale} pdf alt")
        print(f"{locale}: old pdf alt matched once")
    # Keep the existing figure bytes and place each translated entry directly after pdf.
    lines = text.split("\n")
    lines.insert(table.end_lineno - 1 if name == "FIGURES" else pdf.end_lineno, entry)
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    path = "scripts/build_pages.py"
    files = {path: add_figure(path, "FIGURES", "", BUILT_IN, built_in_entry())}
    for locale in TABLE_A:
        if locale not in BUILT_IN:
            path = f"scripts/copy_{locale.lower().replace('-', '_')}.py"
            files[path] = add_figure(path, "figures", "    ", {locale: None}, locale_entry(locale))
    print(f"prepared {len(TABLE_A)} locales x {1 + len(CALLOUTS)} panel cells in {len(files)} files")
    if args.dry_run:
        print("dry run: nothing written")
        return 0
    for path, text in files.items():
        (ROOT / path).write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
