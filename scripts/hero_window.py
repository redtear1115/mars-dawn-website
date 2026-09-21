"""The homepage's interactive MarsDawn window: four preview themes and three layouts, no script.

Everything the window shows about the app comes from scripts/hero_sources.json, which
sync_hero_sources.py copies from the kit and the app: theme colours, fonts and names, the
control labels, and an excerpt of the Welcome guide with the kit renderer's own HTML.
This module only arranges it.

The controls are two radio groups. site.css reads the checked radio with :has(), so the
window changes theme and layout with no script and no inline style, and the radios keep
the browser's own keyboard handling: Tab into a group, arrow keys to choose.
"""
import html
import json
import re
from pathlib import Path

SOURCES = json.loads((Path(__file__).resolve().parent / "hero_sources.json").read_text(encoding="utf-8"))
THEMES = SOURCES["themes"]
LAYOUTS = [("source", "1"), ("split", "2"), ("preview", "3")]
DEFAULT_THEME, DEFAULT_LAYOUT = "dawn", "split"

# The window's accessible name: the one piece of copy here that isn't the app's own.
WINDOW_LABEL = {
    "en": "A working MarsDawn window: choose a theme and a layout",
    "zh-hant": "可以操作的 MarsDawn 視窗：選一個主題和版面",
    "zh-hans": "可以操作的 MarsDawn 窗口：选一个主题和布局",
    "ja": "操作できる MarsDawn のウインドウ：テーマとレイアウトを選べます",
}

# The kit's palette fields, as the custom properties site.css reads inside the window.
PALETTE_VARS = {"background": "bg", "surface": "surface", "text": "fg", "muted": "muted", "border": "border",
                "heading": "heading", "accent": "accent", "link": "link", "quote": "quote", "keyword": "keyword"}


def preview_html(locale: str) -> str:
    """The kit renderer's HTML, adapted to sit inside a page without changing what it shows:
    line anchors and heading ids go, table alignment becomes a class (the CSP allows no
    inline style), headings become styled paragraphs so the page keeps one h1, and the
    link becomes text so the window adds no tab stop of its own."""
    out = SOURCES["sample"][locale]["html"]
    out = re.sub(r' (data-line|id)="[^"]*"', "", out)
    out = re.sub(r' style="text-align:(left|center|right)"', r' class="align-\1"', out)
    out = re.sub(r"<h([12])>(.*?)</h\1>", r'<p class="md-h\1">\2</p>', out)
    out = re.sub(r'<a href="[^"]*">(.*?)</a>', r'<span class="md-a">\1</span>', out)
    assert "<a " not in out and "style=" not in out and "<h" not in out, "the renderer's output changed shape"
    return out.strip()


def source_html(locale: str) -> str:
    """The Markdown, marked the way the editor colours it: syntax in muted, headings in the heading colour."""
    lines = []
    for raw in SOURCES["sample"][locale]["markdown"].rstrip("\n").split("\n"):
        line = html.escape(raw, quote=False)
        if m := re.match(r"(#{1,6} )(.*)", line):
            line = f'<span class="mk">{m[1]}</span><span class="hd">{m[2]}</span>'
        else:
            line = re.sub(r"^(\s*)(&gt; |- \[[ x]\] |- )", r'\1<span class="mk">\2</span>', line)
            line = re.sub(r"(\*\*)(.+?)(\*\*)", r'<span class="mk">\1</span><b>\2</b><span class="mk">\3</span>', line)
            line = re.sub(r"(?<![*\w])(\*)([^*]+?)(\*)(?!\*)", r'<span class="mk">\1</span><i>\2</i><span class="mk">\3</span>', line)
            line = re.sub(r"(~~)(.+?)(~~)", r'<span class="mk">\1</span><s>\2</s><span class="mk">\3</span>', line)
            line = re.sub(r"(`)([^`]+)(`)", r'<span class="mk">\1</span><span class="cd">\2</span><span class="mk">\3</span>', line)
            line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<span class="mk">[</span>\1<span class="mk">](</span><span class="ln">\2</span><span class="mk">)</span>', line)
            if line.startswith("|"):
                line = re.sub(r"(\||:?-{3,}:?)", r'<span class="mk">\1</span>', line)
        lines.append(line)
    return "\n".join(lines)


def window_html(locale: str) -> str:
    labels = SOURCES["labels"][locale]
    layouts = "\n".join(
        f'      <input type="radio" name="mdw-layout" id="mdw-{mode}" value="{mode}"{" checked" if mode == DEFAULT_LAYOUT else ""}>'
        f'<label for="mdw-{mode}">{labels[mode]}<kbd aria-hidden="true">⌘{key}</kbd></label>'
        for mode, key in LAYOUTS
    )
    themes = "\n".join(
        f'      <input type="radio" name="mdw-theme" id="mdw-{t["id"]}" value="{t["id"]}"{" checked" if t["id"] == DEFAULT_THEME else ""}>'
        f'<label for="mdw-{t["id"]}"><span class="swatch sw-{t["id"]}" aria-hidden="true"></span>{t["names"][locale]}</label>'
        for t in THEMES
    )
    return f"""<div class="mdw" role="group" aria-label="{WINDOW_LABEL[locale]}">
  <div class="mdw-bar">
    <span class="mdw-lights" aria-hidden="true"><span></span><span></span><span></span></span>
    <fieldset class="mdw-layouts">
      <legend>{labels["layout"]}</legend>
{layouts}
    </fieldset>
    <fieldset class="mdw-themes">
      <legend>{labels["theme"]}</legend>
{themes}
    </fieldset>
  </div>
  <div class="mdw-panes">
    <pre class="mdw-source" aria-label="{labels["source"]}">{source_html(locale)}</pre>
    <div class="mdw-preview" aria-label="{labels["preview"]}" role="region">
{preview_html(locale)}
    </div>
  </div>
</div>"""


def window_css() -> str:
    """Each theme's light and dark palette and body font, straight from the kit, as custom
    properties on the window. The default theme sits on .mdw itself; the others apply when
    their radio is checked. site.css holds the window's layout and the themes' shapes."""
    def block(selector: str, palette: dict, font, indent: str = "") -> str:
        decls = [f"{indent}  --{PALETTE_VARS[key]}: {value};" for key, value in palette.items()]
        if font:
            decls.append(f"{indent}  --font-body: {font};")
        return f"{indent}{selector} {{\n" + "\n".join(decls) + f"\n{indent}}}"

    def selector(theme_id: str) -> str:
        return ".mdw" if theme_id == DEFAULT_THEME else f".mdw:has(#mdw-{theme_id}:checked)"

    kit = SOURCES["kit"]
    light = [block(selector(t["id"]), t["light"], t["font_stack"]) for t in THEMES]
    dark = [block(selector(t["id"]), t["dark"], None, "  ") for t in THEMES]
    swatches = [f".sw-{t['id']} {{ --sw-bg: {t['light']['background']}; --sw-accent: {t['light']['accent']}; }}" for t in THEMES]
    dark_swatches = [f"  .sw-{t['id']} {{ --sw-bg: {t['dark']['background']}; --sw-accent: {t['dark']['accent']}; }}" for t in THEMES]
    return "\n".join([
        "/* Generated by scripts/build_pages.py from scripts/hero_sources.json: the preview themes",
        f"   of mars-dawn-kit {kit['tag']} ({kit['commit'][:7]}), PreviewTheme.swift. Don't edit by hand. */",
        *light,
        *swatches,
        "@media (prefers-color-scheme: dark) {",
        *dark,
        *dark_swatches,
        "}",
    ]) + "\n"


def window_markdown(locale: str) -> str:
    """The window in words, for the page's Markdown twin."""
    labels = SOURCES["labels"][locale]
    names = [t["names"][locale] for t in THEMES]
    modes = [labels[mode] for mode, _ in LAYOUTS]
    return {
        "en": f"The page shows a working MarsDawn window over part of the app's Welcome guide. Pick one of four preview themes ({', '.join(names)}) and one of three layouts ({', '.join(modes)}).",
        "zh-hant": f"頁面上有一個可以操作的 MarsDawn 視窗，內容是 App 內建歡迎指南的一段。可以從四個預覽主題（{'、'.join(names)}）和三種版面（{'、'.join(modes)}）裡選。",
        "zh-hans": f"页面上有一个可以操作的 MarsDawn 窗口，内容是 App 内置欢迎指南的一段。可以从四个预览主题（{'、'.join(names)}）和三种布局（{'、'.join(modes)}）里选。",
        "ja": f"ページには操作できる MarsDawn のウインドウがあり、アプリ内蔵のようこそガイドの一部を表示しています。4 つのプレビューテーマ（{'、'.join(names)}）と 3 つのレイアウト（{'、'.join(modes)}）から選べます。",
    }[locale]
