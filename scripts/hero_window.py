"""The homepage's interactive MarsDawn window: four preview themes and three layouts, no script.

Everything the window shows about the app comes from scripts/hero_sources.json, which
sync_hero_sources.py copies from the kit and the app: theme colours, fonts and names, the
control labels, and an excerpt of the Welcome guide with the kit renderer's own HTML.
This module only arranges it.

The controls are radio groups: the layout, and in the palette menu the appearance and a
theme for each appearance, as the app's StyleMenu.combinedMenu() lays them out. The CSS
reads the checked radios with :has(), so the window changes with no script and no inline
style, and the radios keep the browser's own keyboard handling: Tab into a group, arrow
keys to choose.

Colours follow the window's own color-scheme through light-dark(): each appearance reads the
palette of the theme picked for it. What isn't a colour (a theme's font and shapes) follows
the theme that is showing, which depends on the appearance, so window_css() writes those
rules once per way the window can be in that appearance.
"""
import html
import json
import re
from pathlib import Path

SOURCES = json.loads((Path(__file__).resolve().parent / "hero_sources.json").read_text(encoding="utf-8"))
THEMES = SOURCES["themes"]
LAYOUTS = [("source", "1"), ("split", "2"), ("preview", "3")]
APPEARANCES = ["system", "light", "dark"]
DEFAULT_THEME, DEFAULT_LAYOUT, DEFAULT_APPEARANCE = "dawn", "split", "system"

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
    appearances = "\n".join(
        f'        <input type="radio" name="mdw-appearance" id="mdw-{mode}" value="{mode}"{" checked" if mode == DEFAULT_APPEARANCE else ""}>'
        f'<label for="mdw-{mode}">{ICONS["check"]}{labels[mode]}</label>'
        for mode in APPEARANCES
    )

    def themes(scheme: str) -> str:
        return "\n".join(
            f'          <input type="radio" name="mdw-{scheme}-theme" id="mdw-{scheme}-{t["id"]}" value="{t["id"]}"{" checked" if t["id"] == DEFAULT_THEME else ""}>'
            f'<label for="mdw-{scheme}-{t["id"]}" title="{t["summaries"][locale]}">{ICONS["check"]}{t["names"][locale]}</label>'
            for t in THEMES
        )
    return f"""<div class="mdw" role="group" aria-label="{WINDOW_LABEL[locale]}">
  <div class="mdw-bar">
    <span class="mdw-lights" aria-hidden="true"><span></span><span></span><span></span></span>
    <span class="mdw-title">{labels["title"]}</span>
    <details class="mdw-themes">
      <summary title="{labels["theme_tip"]}"><span class="mdw-sr">{labels["theme"]}</span>{ICONS["palette"]}{ICONS["chevron"]}</summary>
      <div class="mdw-menu">
      <fieldset>
        <legend>{labels["appearance"]}</legend>
{appearances}
      </fieldset>
      <hr>
      <fieldset>
        <legend>{labels["preview_theme"]}</legend>
        <fieldset class="mdw-pick-light">
          <legend>{labels["light"]}</legend>
{themes("light")}
        </fieldset>
        <hr>
        <fieldset class="mdw-pick-dark">
          <legend>{labels["dark"]}</legend>
{themes("dark")}
        </fieldset>
      </fieldset>
      <hr>
      <span class="mdw-settings" aria-hidden="true">{labels["settings"]}</span>
      </div>
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


# Each theme's shapes, as the kit's preview.css draws them. `&` stands for the window while that
# theme is the one showing; window_css() expands it. Dawn is the window's default and has none.
SHAPES = {
    "classic": """
& { --heading-weight: 600; --body-size: 16px; --line-height: 1.75; --radius: 4px; }
&:has(#mdw-preview:checked) .mdw-preview > * { max-width: 720px; }
& .md-h1 { text-align: center; font-size: 2.2em; letter-spacing: 0.01em; border-bottom: 0; padding-bottom: 0; }
& .md-h1::after { content: ""; display: block; width: 48px; height: 1px; margin: 0.5em auto 0; background: var(--accent); }
& .md-h2 { font-style: italic; }
& .mdw-preview blockquote { border-left-width: 2px; font-style: italic; }
& .mdw-preview th { background: transparent; border-bottom: 2px solid var(--accent); }
& .mdw-preview :is(th, td) { border-left: 0; border-right: 0; }
""",
    "modern": """
& { --heading-weight: 700; --radius: 6px; }
& :is(.md-h1, .md-h2) { letter-spacing: -0.015em; }
& .mdw-preview blockquote { border-left-width: 4px; }
& .mdw-preview li::marker { color: var(--muted); }
""",
    "vivid": """
& { --heading-weight: 800; --radius: 14px; }
& .md-h1 { border-bottom: 0; padding-bottom: 0.15em; background: linear-gradient(90deg, var(--accent), var(--heading)) left bottom / 64px 4px no-repeat; }
& .md-h2 { border-bottom: 0; padding-bottom: 0; }
& .md-h2::before { content: ""; display: inline-block; width: 0.5em; height: 0.5em; margin-right: 0.45em; border-radius: 50%; background: var(--accent); vertical-align: 0.12em; }
& .mdw-preview blockquote { border-left: 0; padding: 0.6em 1em; background: var(--surface); border-radius: var(--radius); color: var(--fg); }
& .mdw-preview code { color: var(--keyword); }
& .mdw-preview th { background: var(--heading); color: var(--bg); border-color: var(--heading); }
""",
}


def showing(theme_id: str) -> dict:
    """The selectors under which `theme_id` is the theme on show, by the media query they need:
    picked for Light with Light chosen, or for Dark with Dark chosen, in any case; picked for
    Light with System chosen while the Mac is light; picked for Dark with System while it's dark."""
    return {
        "": [f".mdw:has(#mdw-light:checked):has(#mdw-light-{theme_id}:checked)",
             f".mdw:has(#mdw-dark:checked):has(#mdw-dark-{theme_id}:checked)"],
        "not all and (prefers-color-scheme: dark)": [f".mdw:has(#mdw-system:checked):has(#mdw-light-{theme_id}:checked)"],
        "(prefers-color-scheme: dark)": [f".mdw:has(#mdw-system:checked):has(#mdw-dark-{theme_id}:checked)"],
    }


def window_css() -> str:
    """Each theme's light and dark palette and body font, straight from the kit, as custom
    properties on the window, and each theme's shapes. Every colour is light-dark() of the
    theme picked for Light (--l-*) and the one picked for Dark (--d-*); the appearance radios
    set the window's color-scheme. Fonts and shapes follow the theme on show (showing())."""
    def decls(palette: dict, prefix: str) -> list:
        return [f"  --{prefix}{PALETTE_VARS[key]}: {value};" for key, value in palette.items()]

    kit = SOURCES["kit"]
    dawn = next(t for t in THEMES if t["id"] == DEFAULT_THEME)
    base = [".mdw {", "  color-scheme: light dark;",
            *[f"  --{var}: light-dark(var(--l-{var}), var(--d-{var}));" for var in PALETTE_VARS.values()],
            *decls(dawn["light"], "l-"), *decls(dawn["dark"], "d-"),
            f"  --font-body: {dawn['font_stack']};", "}",
            ".mdw:has(#mdw-light:checked) { color-scheme: light; }",
            ".mdw:has(#mdw-dark:checked) { color-scheme: dark; }"]
    picks = []
    for t in THEMES:
        if t["id"] == DEFAULT_THEME:
            continue
        for scheme, prefix in (("light", "l-"), ("dark", "d-")):
            picks += [f".mdw:has(#mdw-{scheme}-{t['id']}:checked) {{", *decls(t[scheme], prefix), "}"]
    shapes = {query: [] for query in showing("x")}
    for t in THEMES:
        if t["id"] == DEFAULT_THEME:
            continue
        rules = [("&", f"--font-body: {t['font_stack']};")] + [
            (sel.strip(), body.strip()) for sel, body in re.findall(r"^(&[^{]*)\{ (.*) \}$", SHAPES[t["id"]], re.M)]
        for query, selectors in showing(t["id"]).items():
            for sel, body in rules:
                targets = ",\n".join(sel.replace("&", s) for s in selectors)
                shapes[query].append(f"{targets} {{ {body} }}")
    editor = SOURCES["editor"]
    field_var = {field: var for field, var in PALETTE_VARS.items()}
    roles = ".mdw-source {\n" + "\n".join(
        f"  --ed-{role}: var(--{field_var[editor[role]]});" for role in EDITOR_ROLES) + "\n}"
    out = [
        "/* Generated by scripts/build_pages.py from scripts/hero_sources.json: the preview themes",
        f"   of mars-dawn-kit {kit['tag']} ({kit['commit'][:7]}), PreviewTheme.swift. Don't edit by hand. */",
        *base,
        "/* The theme picked for each appearance: its palette. */",
        *picks,
        "/* The theme on show: its font and shapes (hero_window.SHAPES). */",
        *shapes[""],
    ]
    for query in list(shapes)[1:]:
        out += [f"@media {query} {{", *shapes[query], "}"]
    out += ["/* The source editor's colour roles, from the app's EditorTheme(lightTheme:darkTheme:). */", roles]
    return "\n".join(out) + "\n"


def window_markdown(locale: str) -> str:
    """The window in words, for the page's Markdown twin."""
    labels = SOURCES["labels"][locale]
    names = [t["names"][locale] for t in THEMES]
    modes = [labels[mode] for mode, _ in LAYOUTS]
    looks = [labels[mode] for mode in APPEARANCES]
    return {
        "en": f"The page shows a working MarsDawn window over part of the app's Welcome guide. Its palette menu picks an appearance ({', '.join(looks)}) and a preview theme for light and for dark from four ({', '.join(names)}), and its toolbar one of three layouts ({', '.join(modes)}).",
        "zh-hant": f"頁面上有一個可以操作的 MarsDawn 視窗，內容是 App 內建歡迎指南的一段。調色盤選單可以選外觀（{'、'.join(looks)}），並分別替淺色和深色從四個預覽主題（{'、'.join(names)}）裡選一個；工具列可以選三種版面（{'、'.join(modes)}）。",
        "zh-hans": f"页面上有一个可以操作的 MarsDawn 窗口，内容是 App 内置欢迎指南的一段。调色板菜单可以选外观（{'、'.join(looks)}），并分别为浅色和深色从四个预览主题（{'、'.join(names)}）里选一个；工具栏可以选三种布局（{'、'.join(modes)}）。",
        "ja": f"ページには操作できる MarsDawn のウインドウがあり、アプリ内蔵のようこそガイドの一部を表示しています。パレットのメニューで外観モード（{'、'.join(looks)}）を選び、ライトとダークそれぞれに 4 つのプレビューテーマ（{'、'.join(names)}）から 1 つを選べます。ツールバーでは 3 つのレイアウト（{'、'.join(modes)}）から選べます。",
    }[locale]
