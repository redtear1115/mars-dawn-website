#!/usr/bin/env python3
"""Copies what the homepage's interactive window shows from the app and the kit into
scripts/hero_sources.json, so the site never types those facts by hand.

The window on the homepage is a working model of MarsDawn's: four preview themes and
three layouts, over an excerpt of the app's own Welcome guide. Each of those comes
from somewhere else:

- theme colours, fonts and names: the kit's PreviewTheme.swift and its Localizable.strings,
  at the kit tag the app ships (KIT_TAG);
- the layout and theme control labels: the app's Localizable String Catalog (or, before app
  #90, its per-language Localizable.strings);
- the sample: the app's Welcome.md in each language, rendered by the kit's own
  MarkdownRenderer (tools/hero-render, pinned to the same kit tag).

The app repository is private and CI can't read it, so this script runs on a Mac with
both checkouts, and CI checks the site against the snapshot it writes (check_hero.py).

    python3 scripts/sync_hero_sources.py --kit ../mars-dawn-kit --app ../mars-dawn          # rewrite
    python3 scripts/sync_hero_sources.py --kit ../mars-dawn-kit --app ../mars-dawn --check  # drift?

--check exits 1, and names what moved, if what the site shows no longer matches the
sources: a theme's colours, font or names, a control label, or the Welcome excerpt and
its rendering. Which app or kit commit was read is recorded but never compared, so an app
commit that changes none of those, like most, leaves the check green.
The app is read at --app-ref (default origin/main), the kit at KIT_TAG; neither
working tree is touched, so stale local branches don't matter.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "scripts" / "hero_sources.json"
RENDERER = ROOT / "tools" / "hero-render"

KIT_TAG = "0.5.2"
# The parts of the snapshot the site shows. The rest (which commits were read) is provenance.
SHOWN = ("themes", "labels", "editor", "highlighter", "sample")
LOCALES = {"en": "en", "zh-hant": "zh-Hant", "zh-hans": "zh-Hans", "ja": "ja"}
THEME_ORDER = ["dawn", "classic", "modern", "vivid"]
PALETTE_KEYS = ["background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote"]
# The syntax colours the site uses: code in the preview (keyword), and the editor's (EDITOR).
SYNTAX_KEYS = ["keyword", "function", "string", "comment"]
# The app's own strings for the two controls, keyed by what the site calls them.
# The layout names are ViewMode.shortTitle, the ones the toolbar's segmented control shows.
LABEL_KEYS = {"theme": "Theme", "layout": "Layout", "source": "Source", "split": "Split", "preview": "Preview",
              # The window's title for the guide (WelcomeGuide.title), the theme menu's header,
              # and ViewMode.title, which the layout buttons' tooltips show with their shortcut.
              "title": "Welcome to MarsDawn", "preview_theme": "Preview Theme",
              "source_title": "Source Only", "split_title": "Source and Preview", "preview_title": "Preview Only"}
APP_EDITOR = "MarsDawn/Editor/EditorTheme.swift"
APP_HIGHLIGHTER = "MarsDawn/Editor/MarkdownHighlighter.swift"
KIT_STRINGS = "Sources/MarsDawnKit/Resources/Localization/{lproj}.lproj/Localizable.strings"
APP_STRINGS = "MarsDawn/Resources/{lproj}.lproj/Localizable.strings"
# The app's String Catalog (app #90), which replaces the .strings tables above once it lands.
APP_CATALOG = "MarsDawn/Resources/Localizable.xcstrings"
APP_WELCOME = "MarsDawn/Resources/{lproj}.lproj/Welcome.md"


def git_show(repo: Path, ref: str, path: str) -> str:
    return subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{path}"],
                          check=True, capture_output=True, text=True).stdout


def git_has(repo: Path, ref: str, path: str) -> bool:
    return subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"{ref}:{path}"], capture_output=True).returncode == 0


def app_strings(app: Path, ref: str) -> dict:
    """{lproj: {key: value}} for the app's Localizable table, from its String Catalog when the
    ref has one, else from the per-language .strings files. English falls back to the key in
    both, as the app does when a string has no en value of its own."""
    if git_has(app, ref, APP_CATALOG):
        catalog = json.loads(git_show(app, ref, APP_CATALOG))
        tables = {lproj: {} for lproj in LOCALES.values()}
        for key, entry in catalog["strings"].items():
            for lproj in tables:
                unit = entry.get("localizations", {}).get(lproj, {}).get("stringUnit")
                if unit and unit.get("state") in ("translated", None):
                    tables[lproj][key] = unit["value"]
        return tables
    return {lproj: parse_strings(git_show(app, ref, APP_STRINGS.format(lproj=lproj))) for lproj in LOCALES.values()}


def git_commit(repo: Path, ref: str) -> str:
    return subprocess.run(["git", "-C", str(repo), "rev-parse", f"{ref}^{{commit}}"],
                          check=True, capture_output=True, text=True).stdout.strip()


def parse_strings(text: str) -> dict:
    return {k: v for k, v in re.findall(r'^"((?:[^"\\]|\\.)*)"\s*=\s*"((?:[^"\\]|\\.)*)";', text, re.M)}


def parse_themes(swift: str) -> list:
    themes = {}
    for match in re.finditer(r"static let (\w+) = PreviewTheme\((.*?)\n    \)\n", swift, re.S):
        body = match.group(2)
        theme_id = re.search(r'id: "(\w+)"', body).group(1)
        palettes = {}
        for scheme in ("light", "dark"):
            block = re.search(scheme + r": Palette\((.*?)\n        \)", body, re.S).group(1)
            top = block.split("syntax:")[0]
            colours = dict(re.findall(r'(\w+): "(#[0-9A-Fa-f]{6})"', top))
            syntax = dict(re.findall(r'(\w+): "(#[0-9A-Fa-f]{6})"', re.search(r"Syntax\((.*?)\)", block).group(1)))
            palettes[scheme] = {key: colours[key].upper() for key in PALETTE_KEYS}
            for key in SYNTAX_KEYS:
                palettes[scheme][key] = syntax[key].upper()
        themes[theme_id] = {
            "id": theme_id,
            "name": re.search(r'name: String\(localized: "([^"]+)"', body).group(1),
            "font": re.search(r"fontDesign: \.(\w+)", body).group(1),
            **palettes,
        }
    stacks = dict(re.findall(r'case \.(\w+): #"(.*?)"#', swift))
    for theme in themes.values():
        theme["font_stack"] = stacks[theme["font"]]
    order = re.search(r"static var all: \[PreviewTheme\] \{ \[(.*?)\] \}", swift).group(1)
    ids = [name.strip() for name in order.split(",")]
    assert ids == THEME_ORDER, f"the kit's theme list changed: {ids}"
    return [themes[i] for i in ids]


def parse_editor(swift: str) -> dict:
    """The source editor's colour roles, as EditorTheme(lightTheme:darkTheme:) takes them from a
    preview theme: {role: palette field}, e.g. "code": "string" (syntax.string)."""
    body = swift[swift.index("init(lightTheme: PreviewTheme, darkTheme: PreviewTheme)"):]
    body = body[:body.index("\n    }\n")]
    roles = {role: path.split(".")[-1] for role, path in re.findall(r"(\w+) = color\(\\\.([\w.]+)\)", body)}
    assert {"text", "heading", "marker", "code", "codeFence"} <= set(roles), f"EditorTheme changed shape: {roles}"
    return roles


def parse_highlighter(swift: str) -> dict:
    """The editor's Markdown highlighting, read from MarkdownHighlighter.swift:
    - rules: styleProse's passes in order, each {pattern, group, attrs}: the regex (the app's
      raw-string literal), which capture group it styles (0 = the whole match) and which
      attribute set it adds;
    - attrs: each attribute set as {color: EditorTheme role, bold, italic, strike}."""
    patterns = dict(re.findall(r'static let (\w+) = make\(#"(.*?)"#\)', swift))
    prose = swift[swift.index("private func styleProse"):swift.index("// MARK: - Attribute sets")]
    rules = []
    for name, body in re.findall(r"each\(Patterns\.(\w+)\) \{(.*?)\n?\s*\}\n", prose, re.S):
        for attrs, group in re.findall(r"addAttributes\(attrs\.(\w+), range: \$0\.range(?:\(at: (\d+)\))?\)", body):
            rules.append({"pattern": patterns[name], "group": int(group or 0), "attrs": attrs})
    init = swift[swift.index("init(theme: EditorTheme)"):]
    init = init[:init.index("\n    }\n")]
    sets = {}
    for name, body in re.findall(r"(\w+) = \[(.*?)\]$", init, re.M):
        color = re.search(r"\.foregroundColor: theme\.(\w+)", body)
        sets[name] = {"color": color[1] if color else None, "bold": "boldFont" in body,
                      "italic": "italicFont" in body, "strike": "strikethroughStyle" in body}
    assert rules and {"code", "fence", "heading", "marker"} <= set(sets), "MarkdownHighlighter changed shape"
    assert all(rule["attrs"] in sets for rule in rules)
    return {"rules": rules, "attrs": sets}


def welcome_excerpt(markdown: str) -> str:
    """The title and its paragraph, the Layouts heading and its table, and the whole
    Writing section: the third ## section. Every language's guide has the same shape,
    which the asserts hold it to, so the excerpt is the same part of it in each."""
    lines = markdown.split("\n")
    starts = [i for i, line in enumerate(lines) if line.startswith("## ")]
    head = lines[:starts[0]]
    layouts = lines[starts[0]:starts[1]]
    table_end = next(i for i, line in enumerate(layouts) if i > 2 and line.startswith("|") and not layouts[i + 1].startswith("|"))
    writing = lines[starts[2]:starts[3]]
    assert head[0].startswith("# ") and layouts[2].startswith("|"), "Welcome.md's opening changed shape"
    assert any(line.startswith("- [x]") for line in writing), "Welcome.md's third section is no longer Writing"
    return "\n".join(head + layouts[:table_end + 1] + [""] + writing).rstrip("\n") + "\n"


def render(markdown: str) -> str:
    subprocess.run(["swift", "build", "-c", "release", "--package-path", str(RENDERER)],
                   check=True, capture_output=True)
    binary = RENDERER / ".build" / "release" / "hero-render"
    return subprocess.run([str(binary)], input=markdown, check=True, capture_output=True, text=True).stdout


def collect(kit: Path, app: Path, app_ref: str) -> dict:
    themes = parse_themes(git_show(kit, KIT_TAG, "Sources/MarsDawnKit/PreviewTheme.swift"))
    labels, sample = {}, {}
    app_tables = app_strings(app, app_ref)
    for locale, lproj in LOCALES.items():
        kit_strings = parse_strings(git_show(kit, KIT_TAG, KIT_STRINGS.format(lproj=lproj))) if locale != "en" else {}
        table = app_tables[lproj]
        for theme in themes:
            theme.setdefault("names", {})[locale] = kit_strings.get(theme["name"], theme["name"])
        # An English string missing from en.lproj falls back to its key, as it does in the app.
        labels[locale] = {site: table.get(key, key) if locale == "en" else table[key]
                          for site, key in LABEL_KEYS.items()}
        excerpt = welcome_excerpt(git_show(app, app_ref, APP_WELCOME.format(lproj=lproj)))
        sample[locale] = {"markdown": excerpt, "html": render(excerpt)}
    for theme in themes:
        del theme["name"]
    return {
        "_generated_by": "scripts/sync_hero_sources.py; edit the sources, not this file",
        "kit": {"tag": KIT_TAG, "commit": git_commit(kit, KIT_TAG)},
        "app": {"ref": app_ref, "commit": git_commit(app, app_ref)},
        "themes": themes,
        "labels": labels,
        "editor": parse_editor(git_show(app, app_ref, APP_EDITOR)),
        "highlighter": parse_highlighter(git_show(app, app_ref, APP_HIGHLIGHTER)),
        "sample": sample,
    }


def drift(old: dict, new: dict, path: str = "") -> list:
    if isinstance(old, dict) and isinstance(new, dict):
        return [d for key in sorted(set(old) | set(new)) for d in drift(old.get(key), new.get(key), f"{path}.{key}".lstrip("."))]
    if isinstance(old, list) and isinstance(new, list) and len(old) == len(new):
        return [d for i, (a, b) in enumerate(zip(old, new)) for d in drift(a, b, f"{path}[{i}]")]
    return [] if old == new else [path]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--kit", type=Path, required=True, help="a clone of mars-dawn-kit (any branch)")
    parser.add_argument("--app", type=Path, required=True, help="a clone of mars-dawn (any branch)")
    parser.add_argument("--app-ref", default="origin/main")
    parser.add_argument("--check", action="store_true", help="compare with the snapshot instead of writing it")
    parser.add_argument("--snapshot", type=Path, default=SNAPSHOT)
    args = parser.parse_args()
    new = collect(args.kit, args.app, args.app_ref)
    if args.check:
        old = json.loads(args.snapshot.read_text(encoding="utf-8"))
        moved = drift({key: old.get(key) for key in SHOWN}, {key: new[key] for key in SHOWN})
        if moved:
            print(f"{args.snapshot.name} no longer matches the app ({args.app_ref}) and kit {KIT_TAG}:", file=sys.stderr)
            for path in moved:
                print(f"  {path}", file=sys.stderr)
            print("Run without --check, rebuild the pages and review the difference.", file=sys.stderr)
            return 1
        print(f"{args.snapshot.name} matches app {new['app']['commit'][:7]} and kit {KIT_TAG} ({new['kit']['commit'][:7]}).")
        return 0
    args.snapshot.write_text(json.dumps(new, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {args.snapshot.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
