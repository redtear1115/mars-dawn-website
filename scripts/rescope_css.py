"""The `.sim-preview` rescoping transform (plan-website-104 WA/W1, design
theme-ecosystem-design.md §3.4, rev-4 rule): the sync-time (Python) half.

Turns a stylesheet written for the kit's own preview page (`:root`, `html`, `body`, and rules
scoped by `[data-theme="…"]`) into one that can be adopted alongside the real page without ever
touching anything outside a wrapper element, `.sim-preview` by default:

    :root                        -> .sim-preview
    html                         -> .sim-preview
    body                         -> .sim-preview
    :root[data-theme="x"]        -> .sim-preview[data-theme="x"]
    [data-theme="x"] h1          -> .sim-preview[data-theme="x"] h1
    [data-theme="x"] .foo        -> .sim-preview[data-theme="x"] .foo
    [data-theme] .foo            -> .sim-preview[data-theme] .foo
    [data-theme="x"] h2::before  -> .sim-preview[data-theme="x"] h2::before
    .foo (anything else)         -> .sim-preview .foo

A selector's leading `[data-theme…]` compound (with or without `:root`) merges onto the wrapper
as ONE compound selector; only the remainder gets a descendant prefix. `@media
(prefers-color-scheme: dark) { … }` becomes the same rules under
`.sim-preview[data-appearance="dark"]` (dark-block `:root[data-theme="x"]` becomes
`.sim-preview[data-appearance="dark"][data-theme="x"]`).

This is a byte-for-byte port of public/assets/theme-sim/rescope.js (the runtime/JS half, kit
website #142). Both halves share scripts/theme_sim/rescope_fixture.json and must pass it, so
neither one can drift from the other or from this comment. Run this file directly to self-test:

    python3 scripts/rescope_css.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "scripts" / "theme_sim" / "rescope_fixture.json"

DEFAULT_WRAPPER = ".sim-preview"
DARK_WRAPPER = '.sim-preview[data-appearance="dark"]'
ROOT_LIKE = {":root", "html", "body"}
# A leading compound that is *only* `:root`, `:root[data-theme…]`, or `[data-theme…]` on its own,
# with nothing else attached (no other attribute, class or pseudo-class in the compound).
LEADING_ATTR = re.compile(r'^:root(\[data-theme(?:="[^"]*")?\])?$|^(\[data-theme(?:="[^"]*")?\])$')
DARK_MEDIA = re.compile(r'^@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)$')
ANY_MEDIA = re.compile(r'^@media\b')
COMMENT = re.compile(r'/\*.*?\*/', re.S)


def _top_level_space(selector: str) -> int:
    """The index of the first top-level whitespace in `selector` (not inside `[...]` or `(...)`),
    or -1."""
    depth = 0
    for i, c in enumerate(selector):
        if c in "[(":
            depth += 1
        elif c in "])":
            depth -= 1
        elif depth == 0 and c.isspace():
            return i
    return -1


def rescope_selector(selector: str, wrapper: str = DEFAULT_WRAPPER) -> str:
    """Rescopes one simple/compound selector (no commas). `wrapper` is the compound to merge onto
    or replace the leading `:root`/`html`/`body`/`[data-theme…]`, `.sim-preview` by default."""
    trimmed = selector.strip()
    idx = _top_level_space(trimmed)
    head = trimmed if idx == -1 else trimmed[:idx]
    rest = "" if idx == -1 else trimmed[idx:]  # includes its own leading whitespace/combinator

    if head in ROOT_LIKE:
        return wrapper + rest if rest else wrapper
    match = LEADING_ATTR.match(head)
    if match:
        attr = match.group(1) or match.group(2) or ""
        return wrapper + attr + rest
    return f"{wrapper} {trimmed}"


def rescope_selector_list(selector_list: str, wrapper: str = DEFAULT_WRAPPER) -> str:
    """Rescopes a comma-separated selector list."""
    return ", ".join(rescope_selector(part, wrapper) for part in selector_list.split(","))


def _split_top_level(css: str):
    """Splits `css` into top-level rules and `@media` blocks, tolerant of nested braces
    (declaration values in this kit's generated CSS never contain `{`/`}`, so a naive brace
    counter is enough). Yields (header, body) pairs."""
    blocks = []
    i, n = 0, len(css)
    while i < n:
        while i < n and css[i].isspace():
            i += 1
        if i >= n:
            break
        header_start = i
        depth = 0
        while i < n:
            c = css[i]
            if c == "{":
                if depth == 0:
                    header = css[header_start:i].strip()
                    body_start = i + 1
                    body_depth = 1
                    i = body_start
                    while i < n and body_depth > 0:
                        if css[i] == "{":
                            body_depth += 1
                        elif css[i] == "}":
                            body_depth -= 1
                        if body_depth > 0:
                            i += 1
                    blocks.append((header, css[body_start:i]))
                    i += 1  # consume the closing brace
                    break
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
    return blocks


def _merge_dark_attribute(wrapper: str) -> str:
    return wrapper if 'data-appearance="dark"' in wrapper else f'{wrapper}[data-appearance="dark"]'


def rescope_css(css: str, wrapper: str = DEFAULT_WRAPPER) -> str:
    """Rescopes a whole stylesheet: every top-level rule under `wrapper`, every rule inside
    `@media (prefers-color-scheme: dark) { … }` unwrapped under
    `.sim-preview[data-appearance="dark"]` (or `wrapper` with that attribute merged on, if
    `wrapper` already carries a leading compound).

    Comments are stripped first: a `/* ... */` between two rules has no `{`/`}` of its own, so
    without this a leading top-of-file comment (preview.css has exactly one, before its first
    rule) would otherwise be swallowed into the *next* rule's selector text -- turning `:root`
    into `/* comment */ :root`, a descendant selector that matches nothing, rather than the
    bare `:root` this transform means to rescope."""
    css = COMMENT.sub("", css)
    out = []
    for header, body in _split_top_level(css):
        if DARK_MEDIA.match(header):
            dark_wrapper = DARK_WRAPPER if wrapper == DEFAULT_WRAPPER else _merge_dark_attribute(wrapper)
            for inner_header, inner_body in _split_top_level(body):
                out.append(f"{rescope_selector_list(inner_header, dark_wrapper)} {{{inner_body}}}\n")
            continue
        if ANY_MEDIA.match(header):
            # Any other `@media` condition (preview.css also has `@media print`): the condition
            # itself names no element, so it is never a selector to rescope -- only the rules
            # nested inside it are. Recursing (rather than treating "@media print" as if it were
            # a compound selector, which would silently ship every inner selector un-rescoped,
            # outside `.sim-preview` entirely) keeps every declaration under the wrapper.
            inner = "".join(f"{rescope_selector_list(h, wrapper)} {{{b}}}\n" for h, b in _split_top_level(body))
            out.append(f"{header} {{\n{inner}}}\n")
            continue
        out.append(f"{rescope_selector_list(header, wrapper)} {{{body}}}\n")
    return "".join(out)


# Regression cases the kit's own preview.css exercises, but the shared fixture (deliberately
# byte-identical between this Python port and public/assets/theme-sim/rescope.js, the JS port)
# does not: a leading top-of-file comment before the first rule, and an `@media` condition other
# than `prefers-color-scheme: dark` (preview.css has `@media print`). Kept separate from the
# shared fixture rather than added to it, so this file's own copy doesn't drift from the JS
# module's -- see that file's own header for how the two are meant to stay in sync.
_REGRESSION_CASES = [
    ("leading top-of-file comment",
     "/* a comment */\n\n:root {\n  --x: 1;\n}\n",
     ".sim-preview {\n  --x: 1;\n}\n"),
    ("a non-dark @media condition",
     "@media print {\n  body { color: black; }\n}\n",
     '@media print {\n.sim-preview { color: black; }\n}\n'),
]


def self_test() -> list:
    """Runs the shared fixture (scripts/theme_sim/rescope_fixture.json) against this transform,
    plus this file's own regression cases (_REGRESSION_CASES). Returns the names of every case
    that didn't match, so a caller (this file, or scripts/check_theme_kit.py) can report each one
    and fail if the list isn't empty."""
    missed = []
    for name, css, expected in _REGRESSION_CASES:
        got = rescope_css(css)
        if got != expected:
            missed.append(f"regression {name}: got {got!r}, expected {expected!r}")
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    default_wrapper = fixture["wrapper"]
    for case in fixture["selectors"]:
        got = rescope_selector(case["selector"], case.get("wrapper", default_wrapper))
        if got != case["expected"]:
            missed.append(f"selector {case['name']}: got {got!r}, expected {case['expected']!r}")
    for sheet in fixture["stylesheets"]:
        rescoped = rescope_css(sheet["css"], default_wrapper)
        for expected_selector in sheet["expectedSelectors"]:
            if expected_selector not in rescoped:
                missed.append(f"stylesheet {sheet['name']}: missing selector {expected_selector!r}")
        for line in rescoped.split("\n"):
            brace = line.find("{")
            if brace == -1:
                continue
            selector_list = line[:brace].strip()
            if not selector_list:
                continue
            for sel in selector_list.split(","):
                if not sel.strip().startswith(".sim-preview"):
                    missed.append(f"stylesheet {sheet['name']}: scope escape {sel.strip()!r}")
    return missed


def main() -> int:
    missed = self_test()
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    total = (len(_REGRESSION_CASES) + len(fixture["selectors"])
              + sum(len(s["expectedSelectors"]) for s in fixture["stylesheets"]))
    if missed:
        for m in missed:
            print(f"::error::{m}")
        print(f"{len(missed)}/{total} case(s) failed.")
        return 1
    print(f"rescope_css: {total} fixture case(s), 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
