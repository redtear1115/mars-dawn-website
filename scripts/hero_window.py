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
                "heading": "heading", "accent": "accent", "link": "link", "quote": "quote", "keyword": "keyword",
                "function": "function", "string": "string", "comment": "comment"}
# The editor's colour roles, which EditorTheme takes from these palette fields (snapshot "editor").
EDITOR_ROLES = ["text", "heading", "marker", "emphasis", "code", "codeFence", "link", "muted", "quote"]


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


# The editor's highlighting is the app's MarkdownHighlighter, read into the snapshot: its
# patterns, the order styleProse runs them in, the capture group each one styles, and each
# attribute set's colour role and font traits. Code blocks take the "code" set, with their
# fence lines in "fence". Later passes win, as attributes added later do in the app.
HIGHLIGHT = SOURCES["highlighter"]
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def _style(name: str) -> dict:
    attrs = HIGHLIGHT["attrs"][name]
    return {key: value for key, value in attrs.items() if value}


def source_runs(markdown: str) -> list:
    """(text, style) runs for the editor pane, styled as the app's editor styles them."""
    styles = [{} for _ in markdown]
    pos, open_fence, gap_start, gaps = 0, None, 0, []
    for line in markdown.split("\n"):
        end = pos + len(line)
        fence = FENCE.match(line)
        if open_fence is None and fence:
            gaps.append((gap_start, pos))
            open_fence, block_start = fence[1], pos
            for i in range(pos, end):
                styles[i] = _style("fence")
        elif open_fence is not None:
            closes = fence and fence[1][0] == open_fence[0] and len(fence[1]) >= len(open_fence) and not line[fence.end():].strip()
            for i in range(pos, end):
                styles[i] = _style("fence") if closes else _style("code")
            if closes:
                open_fence, gap_start = None, end + 1
        pos = end + 1
    if open_fence is None:
        gaps.append((gap_start, len(markdown)))
    for rule in HIGHLIGHT["rules"]:
        pattern, group, attrs = re.compile(rule["pattern"], re.M), rule["group"], _style(rule["attrs"])
        for start, stop in gaps:
            for m in pattern.finditer(markdown, start, stop):
                if m.start(group) < 0:
                    continue
                for i in range(m.start(group), m.end(group)):
                    styles[i] = {**styles[i], **attrs}
    runs, i = [], 0
    while i < len(markdown):
        if markdown[i] == "\n":
            runs.append(("\n", {}))
            i += 1
            continue
        j = i
        while j < len(markdown) and styles[j] == styles[i] and markdown[j] != "\n":
            j += 1
        runs.append((markdown[i:j], styles[i]))
        i = j
    return runs


def source_html(locale: str) -> str:
    out = []
    for text, style in source_runs(SOURCES["sample"][locale]["markdown"].rstrip("\n")):
        classes = ([f'ed-{style["color"]}'] if "color" in style else []) + [
            f"ed-{flag}" for flag in ("bold", "italic", "strike") if style.get(flag)]
        body = html.escape(text, quote=False)
        out.append(f'<span class="{" ".join(classes)}">{body}</span>' if classes else body)
    return "".join(out)


# Icons for the toolbar, drawn for this page in the spirit of the app's (not Apple's glyphs).
ICONS = {
    "source": '<svg viewBox="0 0 20 16" aria-hidden="true" focusable="false"><path d="M6.5 3.5 2 8l4.5 4.5M13.5 3.5 18 8l-4.5 4.5M11.4 2.5 8.6 13.5"/></svg>',
    "split": '<svg viewBox="0 0 20 16" aria-hidden="true" focusable="false"><rect x="2" y="2.5" width="16" height="11" rx="2.5"/><path d="M10 2.5v11"/></svg>',
    "preview": '<svg viewBox="0 0 20 16" aria-hidden="true" focusable="false"><path d="M1.8 8C4 4.4 6.8 2.8 10 2.8S16 4.4 18.2 8C16 11.6 13.2 13.2 10 13.2S4 11.6 1.8 8Z"/><circle cx="10" cy="8" r="3.1"/><circle class="pupil" cx="10" cy="8" r="1.3"/></svg>',
    "palette": '<svg viewBox="0 0 20 18" aria-hidden="true" focusable="false"><path d="M10 2C5.3 2 1.8 5.2 1.8 9.2c0 3.6 2.9 6.6 6.6 6.6 1.3 0 1.9-.8 1.9-1.6 0-.9-.7-1.3-.7-2.1 0-.9.7-1.5 1.6-1.5h2c2.8 0 5-1.9 5-4.5C18.2 4.6 14.6 2 10 2Z"/><circle cx="6" cy="8.6" r="1.1"/><circle cx="8.6" cy="5.6" r="1.1"/><circle cx="12.4" cy="5.6" r="1.1"/><circle cx="14.6" cy="8.4" r="1.1"/></svg>',
    "chevron": '<svg class="chev" viewBox="0 0 10 10" aria-hidden="true" focusable="false"><path d="M2.5 3.8 5 6.3l2.5-2.5"/></svg>',
    "check": '<svg class="tick" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2.5 6.4 5 8.8l4.6-5.6"/></svg>',
}


def window_html(locale: str) -> str:
    labels = SOURCES["labels"][locale]
    layouts = "\n".join(
        f'      <input type="radio" name="mdw-layout" id="mdw-{mode}" value="{mode}"{" checked" if mode == DEFAULT_LAYOUT else ""}>'
        f'<label for="mdw-{mode}" title="{labels[mode + "_title"]} (⌘{key})">{ICONS[mode]}<span class="mdw-sr">{labels[mode]}</span></label>'
        for mode, key in LAYOUTS
    )
    themes = "\n".join(
        f'        <input type="radio" name="mdw-theme" id="mdw-{t["id"]}" value="{t["id"]}"{" checked" if t["id"] == DEFAULT_THEME else ""}>'
        f'<label for="mdw-{t["id"]}">{ICONS["check"]}<span class="swatch sw-{t["id"]}" aria-hidden="true"></span>{t["names"][locale]}</label>'
        for t in THEMES
    )
    return f"""<div class="mdw" role="group" aria-label="{WINDOW_LABEL[locale]}">
  <div class="mdw-bar">
    <span class="mdw-lights" aria-hidden="true"><span></span><span></span><span></span></span>
    <span class="mdw-title">{labels["title"]}</span>
    <details class="mdw-themes">
      <summary title="{labels["preview_theme"]}"><span class="mdw-sr">{labels["theme"]}</span>{ICONS["palette"]}{ICONS["chevron"]}</summary>
      <fieldset class="mdw-menu">
        <legend>{labels["preview_theme"]}</legend>
{themes}
      </fieldset>
    </details>
    <fieldset class="mdw-layouts">
      <legend>{labels["layout"]}</legend>
{layouts}
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
    editor = SOURCES["editor"]
    field_var = {field: var for field, var in PALETTE_VARS.items()}
    roles = ".mdw-source {\n" + "\n".join(
        f"  --ed-{role}: var(--{field_var[editor[role]]});" for role in EDITOR_ROLES) + "\n}"
    return "\n".join([
        "/* Generated by scripts/build_pages.py from scripts/hero_sources.json: the preview themes",
        f"   of mars-dawn-kit {kit['tag']} ({kit['commit'][:7]}), PreviewTheme.swift. Don't edit by hand. */",
        *light,
        *swatches,
        "@media (prefers-color-scheme: dark) {",
        *dark,
        *dark_swatches,
        "}",
        "/* The source editor's colour roles, from the app's EditorTheme(lightTheme:darkTheme:). */",
        roles,
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
