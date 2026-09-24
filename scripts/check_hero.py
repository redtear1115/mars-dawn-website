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
    """{(theme, scheme): {field: value}} read back out of hero.css: Dawn's from the .mdw block's
    --l-* and --d-*, every other theme's from the block its Light or Dark radio sets; each
    theme's font under (theme, "font"), from the rule for the theme on show; and the
    colour mapping under "map": {var: what .mdw sets it to}."""
    out = {}
    base = re.search(r"^\.mdw \{([^}]*)\}", css, re.M)
    body = dict(re.findall(r"--([\w-]+): ([^;]+);", base[1])) if base else {}
    out["map"] = {k: v for k, v in body.items() if not k.startswith(("l-", "d-")) and k != "font-body"}
    out[("dawn", "light")] = {k[2:]: v for k, v in body.items() if k.startswith("l-")}
    out[("dawn", "dark")] = {k[2:]: v for k, v in body.items() if k.startswith("d-")}
    out[("dawn", "font")] = body.get("font-body")
    for m in re.finditer(r"^\.mdw:has\(#mdw-(light|dark)-(\w+):checked\) \{([^}]*)\}", css, re.M):
        out[(m[2], m[1])] = {k[2:]: v for k, v in re.findall(r"--([\w-]+): ([^;]+);", m[3])}
    for m in re.finditer(r"^\.mdw:has\(#mdw-light:checked\):has\(#mdw-light-(\w+):checked\),\n"
                         r"\.mdw:has\(#mdw-dark:checked\):has\(#mdw-dark-\1:checked\) \{ --font-body: ([^;]+); \}", css, re.M):
        out[(m[1], "font")] = m[2]
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
    for var in VARS:
        want = f"light-dark(var(--l-{var}), var(--d-{var}))"
        if palettes["map"].get(var) != want:
            problems.append(f"hero.css: --{var} is {palettes['map'].get(var)}, not {want}")
    for theme in src["themes"]:
        for scheme in ("light", "dark"):
            got = palettes.get((theme["id"], scheme))
            if not got:
                problems.append(f"hero.css: no {scheme} block for {theme['id']}")
                continue
            for var, field in VARS.items():
                if got.get(var, "").upper() != theme[scheme][field].upper():
                    problems.append(f"hero.css: {theme['id']} {scheme} --{var} is {got.get(var)}, kit says {theme[scheme][field]}")
        font = palettes.get((theme["id"], "font"))
        if font != theme["font_stack"]:
            problems.append(f"hero.css: {theme['id']} font is {font}, kit says {theme['font_stack']}")
    for locale, html in pages.items():
        page = Text()
        page.feed(html)
        found, labels = page.found, src["labels"][locale]
        want = {f"mdw-{scheme}-{t['id']}": t["names"][locale] for t in src["themes"] for scheme in ("light", "dark")}
        want.update({f"mdw-{mode}": labels[mode] for mode in ("source", "split", "preview", "system", "light", "dark")})
        for key, text in want.items():
            if found.get(key, "").strip() != text:
                problems.append(f"{locale}: control {key} reads {found.get(key, '').strip()!r}, the app says {text!r}")
        # The menu's section headers in StyleMenu.combinedMenu()'s order, then the layout group.
        groups = [labels[k] for k in ("appearance", "preview_theme", "light", "dark", "layout")]
        if [s.strip() for s in found.get("legends", [])] != groups:
            problems.append(f"{locale}: group names {found.get('legends')} aren't the app's {groups}")
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
    if not summary or summary.groups() != (labels["theme_tip"], labels["theme"]):
        problems.append(f"{locale}: the theme button's tooltip and name are {summary and summary.groups()}, "
                        f"the app's are {(labels['theme_tip'], labels['theme'])}")
    settings = re.search(r'<span class="mdw-settings"[^>]*>([^<]*)</span>\s*</div>\s*</details>', html)
    if not settings or settings[1] != labels["settings"]:
        problems.append(f"{locale}: the menu doesn't end on {labels['settings']!r}")
    for mode, key in (("source", "1"), ("split", "2"), ("preview", "3")):
        tip = re.search(rf'<label for="mdw-{mode}" title="([^"]*)"><svg', html)
        want = f"{labels[mode + '_title']} (⌘{key})"
        if not tip or tip[1] != want:
            problems.append(f"{locale}: the {mode} button's tooltip is {tip and tip[1]!r}, the app's is {want!r}, with an icon")
    for mode in ("system", "light", "dark"):
        if not re.search(rf'<label for="mdw-{mode}"><svg class="tick"', html):
            problems.append(f"{locale}: the {mode} menu item has no checkmark")
    for theme in src["themes"]:
        for scheme in ("light", "dark"):
            tip = theme["summaries"][locale]
            if not re.search(rf'<label for="mdw-{scheme}-{theme["id"]}" title="{re.escape(tip)}"><svg class="tick"', html):
                problems.append(f"{locale}: the {scheme} {theme['id']} menu item lacks its checkmark or the kit's summary {tip!r}")
    checked = re.findall(r'id="mdw-([\w-]+)" value="\w+" checked', html)
    if checked != ["system", "light-dawn", "dark-dawn", "split"]:
        problems.append(f"{locale}: the window opens on {checked}, not System, Dawn for both, in Split")
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
        sync.localize_themes(themes, locale, strings)
    sync.finish_themes(themes)
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
        "a dark colour for a picked theme": (lambda: check_site(src, css.replace(src["themes"][3]["dark"]["accent"], "#123456", 1), pages)),
        "a colour mapped to one scheme": (lambda: check_site(src, css.replace("--fg: light-dark(var(--l-fg), var(--d-fg));", "--fg: var(--l-fg);", 1), pages)),
        "a theme summary on a page": (lambda: check_site(src, css, {**pages, "zh-hant": pages["zh-hant"].replace(src["themes"][2]["summaries"]["zh-hant"], "現代", 1)})),
        "an appearance label": (lambda: check_site(src, css, {**pages, "ja": pages["ja"].replace(f'</svg>{src["labels"]["ja"]["system"]}</label>', "</svg>自動</label>", 1)})),
        "Settings… missing": (lambda: check_site(src, css, {**pages, "en": re.sub(r'<span class="mdw-settings"[^>]*>[^<]*</span>', "", pages["en"], count=1)})),
        "a theme name on a page": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace(f"</svg>{en_label}</label>", "</svg>Sunrise</label>", 1)})),
        "a layout label on a page": (lambda: check_site(src, css, {**pages, "ja": pages["ja"].replace(f'<span class="mdw-sr">{src["labels"]["ja"]["split"]}</span>', '<span class="mdw-sr">並べて</span>', 1)})),
        "a word in the source pane": (lambda: check_site(src, css, {**pages, "zh-hant": re.sub(r'(<pre class="mdw-source"[^>]*>.*?)MarsDawn', r"\1MarsDusk", pages["zh-hant"], count=1, flags=re.S)})),
        "the window title": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace('<span class="mdw-title">Welcome to MarsDawn</span>', '<span class="mdw-title">Welcome.md</span>', 1)})),
        "a layout tooltip": (lambda: check_site(src, css, {**pages, "zh-hant": pages["zh-hant"].replace("(⌘2)", "(⌘3)", 1)})),
        "a menu item without its checkmark": (lambda: check_site(src, css, {**pages, "ja": re.sub(r'(<label for="mdw-dark-vivid"[^>]*><svg class=")tick', r"\1x", pages["ja"], count=1)})),
        "the theme button's name": (lambda: check_site(src, css, {**pages, "zh-hans": re.sub(r'(<summary title="[^"]*"><span class="mdw-sr">)[^<]*', r"\1Palette", pages["zh-hans"], count=1)})),
        "an editor colour role": (lambda: check_site(src, css.replace("--ed-code: var(--string);", "--ed-code: var(--keyword);", 1), pages)),
        "the default theme": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace('value="dawn" checked', 'value="dawn"', 1).replace('value="modern">', 'value="modern" checked>', 1)})),
        "the default appearance": (lambda: check_site(src, css, {**pages, "en": pages["en"].replace('value="system" checked', 'value="system"', 1).replace('value="dark">', 'value="dark" checked>', 1)})),
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
