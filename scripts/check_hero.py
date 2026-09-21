#!/usr/bin/env python3
"""Checks that the homepage's MarsDawn window still shows what the app and the kit do.

The window's facts live in scripts/hero_sources.json, copied from the app and the kit by
sync_hero_sources.py. This script holds the built site to that snapshot:

- public/assets/hero.css has every theme's light and dark palette and font, value for value;
- each locale's home page names the themes and the controls as the app does, and shows
  the Welcome-guide excerpt exactly: the source pane its Markdown, the preview the kit
  renderer's text;

and, with --kit, holds the snapshot to the kit itself: PreviewTheme.swift and the theme
names at the pinned tag, fetched from GitHub (the kit is public). The app is private, so
its side is checked on a Mac with `sync_hero_sources.py --check`.

--self-test plants one drift of each kind in memory and fails unless every one is caught,
so a check that can't fail doesn't pass for one that works.
"""
import argparse
import json
import re
import sys
import urllib.request
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import sync_hero_sources as sync  # noqa: E402

PAGES = {"en": "index.html", "zh-hant": "zh-hant/index.html", "zh-hans": "zh-hans/index.html", "ja": "ja/index.html"}
KIT_RAW = "https://raw.githubusercontent.com/redtear1115/mars-dawn-kit/{tag}/{path}"
VARS = {"bg": "background", "surface": "surface", "fg": "text", "muted": "muted", "border": "border",
        "heading": "heading", "accent": "accent", "link": "link", "quote": "quote", "keyword": "keyword",
        "function": "function", "string": "string", "comment": "comment"}


def css_palettes(css: str) -> dict:
    """{(theme, scheme): {field: value}} and fonts, read back out of hero.css, plus each
    theme's swatch under (theme, scheme, "swatch")."""
    out = {}
    light, _, dark = css.partition("@media (prefers-color-scheme: dark)")
    for scheme, text in (("light", light), ("dark", dark)):
        for m in re.finditer(r"\.mdw(?::has\(#mdw-(\w+):checked\))? \{([^}]*)\}", text):
            out[(m[1] or "dawn", scheme)] = dict(re.findall(r"--([\w-]+): ([^;]+);", m[2]))
        for m in re.finditer(r"\.sw-(\w+) \{([^}]*)\}", text):
            out[(m[1], scheme, "swatch")] = dict(re.findall(r"--([\w-]+): ([^;]+);", m[2]))
    return out


class Text(HTMLParser):
    """Collects the text of the elements the check reads, by a simple class/for key."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.found = [], {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        key = None
        if tag == "label" and (a.get("for") or "").startswith("mdw-"):
            key = a["for"]
        elif tag == "legend":
            key = "legend"
        elif tag == "pre" and "mdw-source" in (a.get("class") or ""):
            key = "source"
        elif tag == "div" and "mdw-preview" in (a.get("class") or ""):
            key = "preview"
        elif tag == "kbd":
            key = "kbd"
        if tag in ("input", "br", "img", "meta", "link"):
            return
        self.stack.append(key)
        if key and key not in ("legend", "kbd"):
            self.found.setdefault(key, "")
        if key == "legend":
            self.found.setdefault("legends", []).append("")

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if "kbd" in self.stack:
            return
        for key in reversed(self.stack):
            if key == "legend":
                self.found["legends"][-1] += data
                return
            if key:
                self.found[key] += data
                return


def rendered_text(html: str) -> str:
    """The characters a reader sees, without whitespace: the page's markup differs from the
    renderer's between tags (a heading becomes a styled paragraph), never inside the text."""
    return re.sub(r"\s+", "", unescape(re.sub(r"<[^>]+>", "", html)))


def check_site(src: dict, css: str, pages: dict) -> list:
    problems = check_editor_roles(src, css)
    palettes = css_palettes(css)
    for theme in src["themes"]:
        for scheme in ("light", "dark"):
            got = palettes.get((theme["id"], scheme))
            if got is None:
                problems.append(f"hero.css: no {scheme} block for {theme['id']}")
                continue
            for var, field in VARS.items():
                if got.get(var, "").upper() != theme[scheme][field].upper():
                    problems.append(f"hero.css: {theme['id']} {scheme} --{var} is {got.get(var)}, kit says {theme[scheme][field]}")
            # The swatch on the theme's button: its page and accent colours.
            swatch = palettes.get((theme["id"], scheme, "swatch"), {})
            for var, field in (("sw-bg", "background"), ("sw-accent", "accent")):
                if swatch.get(var, "").upper() != theme[scheme][field].upper():
                    problems.append(f"hero.css: {theme['id']} {scheme} swatch --{var} is {swatch.get(var)}, kit says {theme[scheme][field]}")
        font = palettes.get((theme["id"], "light"), {}).get("font-body")
        if font != theme["font_stack"]:
            problems.append(f"hero.css: {theme['id']} font is {font}, kit says {theme['font_stack']}")
    for locale, html in pages.items():
        page = Text()
        page.feed(html)
        found, labels = page.found, src["labels"][locale]
        want = {f"mdw-{t['id']}": t["names"][locale] for t in src["themes"]}
        want.update({f"mdw-{mode}": labels[mode] for mode in ("source", "split", "preview")})
        for key, text in want.items():
            if found.get(key, "").strip() != text:
                problems.append(f"{locale}: control {key} reads {found.get(key, '').strip()!r}, the app says {text!r}")
        if [s.strip() for s in found.get("legends", [])] != [labels["preview_theme"], labels["layout"]]:
            problems.append(f"{locale}: group names {found.get('legends')} aren't the app's {[labels['preview_theme'], labels['layout']]}")
        problems += check_chrome(locale, html, src)
        if found.get("source", "") != src["sample"][locale]["markdown"].rstrip("\n"):
            problems.append(f"{locale}: the source pane isn't the Welcome.md excerpt")
        if rendered_text(found.get("preview", "")) != rendered_text(src["sample"][locale]["html"]):
            problems.append(f"{locale}: the preview's text isn't what the kit renderer made of the excerpt")
    return problems


# The themes page in each language lists the themes by name. The list must use that language's
# app names, in the kit's order, and nothing else beside them, such as another language's name
# in brackets (COPY-REVIEW §3.2, and the owner's calls of 2026-09-21).
THEME_LISTS = {"en": "themes/index.html", "zh-hant": "zh-hant/themes/index.html", "zh-hans": "zh-hans/themes/index.html", "ja": "ja/themes/index.html"}


def check_theme_lists(src: dict, pages: dict) -> list:
    problems = []
    for locale, html in pages.items():
        # The name, and anything set right after it before the punctuation that starts its
        # description, so a bracketed second name counts as part of the name.
        names = [(name + extra).strip() for name, extra in
                 re.findall(r"<li><strong>([^<]+)</strong>([^:：,，、<]*)", html)[:len(src["themes"])]]
        want = [t["names"][locale] for t in src["themes"]]
        if names != want:
            problems.append(f"{THEME_LISTS[locale]}: the theme list reads {names}, the app says {want}")
    return problems


def check_chrome(locale: str, html: str, src: dict) -> list:
    """The window's title bar and toolbar say and show what the app's do."""
    labels, problems = src["labels"][locale], []
    title = re.search(r'<span class="mdw-title">([^<]*)</span>', html)
    if not title or title[1] != labels["title"]:
        problems.append(f"{locale}: the window title is {title and title[1]!r}, the app titles its guide {labels['title']!r}")
    summary = re.search(r'<summary title="([^"]*)"><span class="mdw-sr">([^<]*)</span><svg', html)
    if not summary or summary.groups() != (labels["preview_theme"], labels["theme"]):
        problems.append(f"{locale}: the theme button's tooltip and name are {summary and summary.groups()}, "
                        f"the app's are {(labels['preview_theme'], labels['theme'])}")
    for mode, key in (("source", "1"), ("split", "2"), ("preview", "3")):
        tip = re.search(rf'<label for="mdw-{mode}" title="([^"]*)"><svg', html)
        want = f"{labels[mode + '_title']} (⌘{key})"
        if not tip or tip[1] != want:
            problems.append(f"{locale}: the {mode} button's tooltip is {tip and tip[1]!r}, the app's is {want!r}, with an icon")
    for theme in src["themes"]:
        if not re.search(rf'<label for="mdw-{theme["id"]}"><svg class="tick"', html):
            problems.append(f"{locale}: the {theme['id']} menu item has no checkmark")
    checked = re.findall(r'id="mdw-(\w+)" value="\w+" checked', html)
    if checked != ["dawn", "split"]:
        problems.append(f"{locale}: the window opens on {checked}, not Dawn in Split")
    return problems


def check_editor_roles(src: dict, css: str) -> list:
    """hero.css maps each editor colour role to the palette field the app's EditorTheme uses."""
    block = re.search(r"\.mdw-source \{([^}]*)\}", css)
    got = dict(re.findall(r"--ed-(\w+): var\(--(\w+)\);", block[1])) if block else {}
    var_of = {field: var for var, field in VARS.items()}
    return [f"hero.css: editor role {role} is --{got.get(role)}, the app's EditorTheme uses {field} (--{var_of.get(field)})"
            for role, field in src["editor"].items()
            if role in ("text", "heading", "marker", "emphasis", "code", "codeFence", "link", "muted", "quote")
            and got.get(role) != var_of.get(field)]


def kit_files(tag: str) -> dict:
    paths = ["Sources/MarsDawnKit/PreviewTheme.swift"] + [
        sync.KIT_STRINGS.format(lproj=lproj) for locale, lproj in sync.LOCALES.items() if locale != "en"]
    return {p: urllib.request.urlopen(KIT_RAW.format(tag=tag, path=p), timeout=30).read().decode("utf-8") for p in paths}


def check_kit(src: dict, files: dict) -> list:
    problems = []
    themes = sync.parse_themes(files["Sources/MarsDawnKit/PreviewTheme.swift"])
    for locale, lproj in sync.LOCALES.items():
        strings = sync.parse_strings(files[sync.KIT_STRINGS.format(lproj=lproj)]) if locale != "en" else {}
        for theme in themes:
            theme.setdefault("names", {})[locale] = strings.get(theme["name"], theme["name"])
    for theme in themes:
        del theme["name"]
    for path in sync.drift(src["themes"], themes, "themes"):
        problems.append(f"hero_sources.json differs from kit {src['kit']['tag']} at {path}")
    return problems


def self_test(src: dict, css: str, pages: dict, lists: dict, kit: dict) -> list:
    """Each plant must make its check fail; returns the ones that didn't."""
    dawn = src["themes"][0]
    en_label = dawn["names"]["en"]
    plants = {
        "a colour in hero.css": (lambda: check_site(src, css.replace(dawn["light"]["accent"], "#123456", 1), pages)),
        "a dark colour in hero.css": (lambda: check_site(src, css.replace(dawn["dark"]["background"], "#123456", 1), pages)),
        "a font in hero.css": (lambda: check_site(src, css.replace("ui-serif", "Georgia", 1), pages)),
        "a swatch colour in hero.css": (lambda: check_site(src, re.sub(r"(\.sw-dawn \{ --sw-bg: )#[0-9A-F]{6}", r"\1#00FF00", css, count=1), pages)),
        "a dark swatch colour in hero.css": (lambda: check_site(src, re.sub(r"(  \.sw-vivid \{ --sw-bg: #[0-9A-F]{6}; --sw-accent: )#[0-9A-F]{6}", r"\1#00FF00", css, count=1), pages)),
        "a theme name on a page": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace(f"</span>{en_label}</label>", "</span>Sunrise</label>", 1)})),
        "a layout label on a page": (lambda: check_site(src, css, {**pages, "ja": pages["ja"].replace(f'<span class="mdw-sr">{src["labels"]["ja"]["split"]}</span>', '<span class="mdw-sr">並べて</span>', 1)})),
        "a word in the source pane": (lambda: check_site(src, css, {**pages, "zh-hant": re.sub(r'(<pre class="mdw-source"[^>]*>.*?)MarsDawn', r"\1MarsDusk", pages["zh-hant"], count=1, flags=re.S)})),
        "the window title": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace('<span class="mdw-title">Welcome to MarsDawn</span>', '<span class="mdw-title">Welcome.md</span>', 1)})),
        "a layout tooltip": (lambda: check_site(src, css, {**pages, "zh-hant": pages["zh-hant"].replace("(⌘2)", "(⌘3)", 1)})),
        "a menu item without its checkmark": (lambda: check_site(src, css, {**pages, "ja": pages["ja"].replace('<label for="mdw-vivid"><svg class="tick"', '<label for="mdw-vivid"><svg class="x"', 1)})),
        "the theme button's name": (lambda: check_site(src, css, {**pages, "zh-hans": re.sub(r'(<summary title="[^"]*"><span class="mdw-sr">)[^<]*', r"\1Palette", pages["zh-hans"], count=1)})),
        "an editor colour role": (lambda: check_site(src, css.replace("--ed-code: var(--string);", "--ed-code: var(--keyword);", 1), pages)),
        "the default theme": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace('value="dawn" checked', 'value="dawn"', 1).replace('value="modern">', 'value="modern" checked>', 1)})),
        "a word in the preview": (lambda: check_site(src, css, {**pages, "zh-hans": re.sub(r"(<p class=\"md-h1\">[^<]*)MarsDawn", r"\1MarsDusk", pages["zh-hans"], count=1)})),
        "an English theme name in the ja theme list": (lambda: check_theme_lists(src, {"ja": lists["ja"].replace("<strong>クラシック</strong>", "<strong>Classic</strong>", 1)})),
        "an English theme name in the zh-Hant theme list": (lambda: check_theme_lists(src, {"zh-hant": lists["zh-hant"].replace("<strong>黎明</strong>", "<strong>Dawn</strong>", 1)})),
        "a bracketed Chinese name in the en theme list": (lambda: check_theme_lists(src, {"en": lists["en"].replace("<strong>Classic</strong>:", "<strong>Classic</strong> (典雅):", 1)})),
        "the zh-Hant name in the zh-Hans theme list": (lambda: check_theme_lists(src, {"zh-hans": lists["zh-hans"].replace("<strong>活泼</strong>", "<strong>活潑</strong>", 1)})),
    }
    if kit:
        swapped = json.loads(json.dumps(src))
        swapped["themes"][3]["dark"]["heading"] = "#000000"
        renamed = json.loads(json.dumps(src))
        renamed["themes"][1]["names"]["ja"] = "Classic（典雅）"
        plants["a colour in the snapshot vs the kit"] = lambda: check_kit(swapped, kit)
        plants["a ja theme name in the snapshot vs the kit"] = lambda: check_kit(renamed, kit)
    missed = []
    for name, run in plants.items():
        caught = run()
        print(f"  {'caught' if caught else 'MISSED'}: {name}" + (f" ({caught[0]})" if caught else ""))
        if not caught:
            missed.append(name)
    return missed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--kit", action="store_true", help="also compare the snapshot with the kit on GitHub")
    parser.add_argument("--self-test", action="store_true", help="plant drift and require every plant to be caught")
    args = parser.parse_args()
    src = json.loads((ROOT / "scripts" / "hero_sources.json").read_text(encoding="utf-8"))
    css = (ROOT / "public" / "assets" / "hero.css").read_text(encoding="utf-8")
    pages = {locale: (ROOT / "public" / path).read_text(encoding="utf-8") for locale, path in PAGES.items()}
    lists = {locale: (ROOT / "public" / path).read_text(encoding="utf-8") for locale, path in THEME_LISTS.items()}
    kit = kit_files(src["kit"]["tag"]) if args.kit else None
    problems = check_site(src, css, pages) + check_theme_lists(src, lists) + (check_kit(src, kit) if kit else [])
    for p in problems:
        print(f"::error::{p}")
    if problems:
        return 1
    print(f"The homepage window matches hero_sources.json" + (f" and kit {src['kit']['tag']}." if kit else "."))
    if args.self_test:
        print("Planted drift:")
        missed = self_test(src, css, pages, lists, kit)
        if missed:
            print(f"::error::The check missed planted drift: {', '.join(missed)}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
