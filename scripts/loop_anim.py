"""The homepage loop, drawn in HTML and CSS: the agent writes, you read and change one day in
MarsDawn, the agent makes the rest agree, and it starts over. Owner decision, 2026-09-24.

No script and no inline style, the same as the hero window. The drawing is a 1600×900 stage
whose lengths are written in `u`, one sixteen-hundredth of the frame's width (a container
query unit), so it scales without measuring anything. Every word is text in the page, so each
locale is its own copy below. The two days that trade places have the same width in every
locale (Oct 7/Oct 9 with tabular digits; 週三/週五, 周三/周五, 水曜/金曜 are two characters), so
they are stacked in one grid cell and nothing has to be measured.

The pause control is a checkbox that loop.css reads with :has(). Visitors who ask for reduced
motion get the edited note, still, and no control.
"""
import html
import re

# The command and the file name stay English in every locale, as they are in the app.
COMMAND = "marsdawn open launch-note.md"
FILE_NAME = "launch-note.md"

COPY = {
    "en": {
        "outline": "Outline", "files": "Files",
        "title": "Launch note",
        "sections": [("What changed", "The sign-in page leads with the email. It ships on {a}."),
                     ("When it ships", "{u} at noon."),
                     ("Who does what", "Engineering turns on the flag on {b}.")],
        "old": "Oct 7", "new": "Oct 9",
        "ask": "I moved the launch. Make the other sections agree.",
        "reply": "Done. Both sections now say Oct 9.",
        "alt": "A terminal opens launch-note.md in MarsDawn. The reader changes the launch day "
               "from October 7 to October 9, the agent updates the other two sections to match, and "
               "the loop starts again.",
        "pause": "Pause the animation", "pause_short": "Pause",
    },
    "zh-hant": {
        "outline": "大綱", "files": "檔案",
        "title": "上線說明",
        "sections": [("改了什麼", "登入頁先問 email，{a}上線。"),
                     ("什麼時候上線", "{u}中午。"),
                     ("誰做什麼", "工程在{b}打開開關。")],
        "old": "週三", "new": "週五",
        "ask": "我改了上線日，其他段落也改成一致。",
        "reply": "好了，另外兩段也改成週五。",
        "alt": "終端機用 MarsDawn 打開 launch-note.md。讀者把上線日從週三改成週五，agent 把另外兩段也改成一致，接著重頭再來一次。",
        "pause": "暫停動畫", "pause_short": "暫停",
    },
    "zh-hans": {
        "outline": "大纲", "files": "文件",
        "title": "上线说明",
        "sections": [("改了什么", "登录页先问 email，{a}上线。"),
                     ("什么时候上线", "{u}中午。"),
                     ("谁做什么", "工程在{b}打开开关。")],
        "old": "周三", "new": "周五",
        "ask": "我改了上线日，其他段落也改成一致。",
        "reply": "好了，另外两段也改成周五。",
        "alt": "终端用 MarsDawn 打开 launch-note.md。读者把上线日从周三改成周五，agent 把另外两段也改成一致，然后从头再来一次。",
        "pause": "暂停动画", "pause_short": "暂停",
    },
    "ja": {
        "outline": "アウトライン", "files": "ファイル",
        "title": "ローンチメモ",
        "sections": [("変更点", "サインイン画面はメールから始まる。{a}に公開。"),
                     ("公開日", "{u}の正午。"),
                     ("担当", "{b}にエンジニアがフラグを有効にする。")],
        "old": "水曜", "new": "金曜",
        "ask": "公開日を変えた。ほかの節も合わせて。",
        "reply": "完了。ほかの 2 節も金曜にした。",
        "alt": "ターミナルが MarsDawn で launch-note.md を開く。読み手が公開日を水曜から金曜に変え、エージェントが残りの 2 節を合わせ、最初に戻る。",
        "pause": "アニメーションを一時停止", "pause_short": "一時停止",
    },
}

LANG_CLASS = {"en": "", "zh-hant": " loop-hant", "zh-hans": " loop-hans", "ja": " loop-ja"}

_esc = html.escape

# A scene is data: the file, its source lines, its preview blocks, and what changes. Two kinds of
# change, both keyed by a one-letter id: a swap (old text stacked on new text of the same width,
# `{id}` inside a line) and a removal (a whole line, block or diagram step, given as `rm=id`).
# `u` is the reader's edit (select, then type or delete, 36–46%); `a`, `b`, `c` … are the agent's,
# a beat apart from 60%. The home page is one scene (home_scene); the /templates/ pages are others.
AGENT_IDS = "abcdefg"


def _swap(old: str, new: str, which: str, caret: bool) -> str:
    steps = len(new)
    caret_html = f'<span class="loop-ecaret loop-n{steps} a"></span>' if caret else ""
    return (f'<span class="loop-day loop-d-{which} a"><span class="loop-old a">{_esc(old)}</span>'
            f'<span class="loop-new loop-n{steps} a">{_esc(new)}</span>{caret_html}</span>')


def _fill(text: str, swaps: dict, source: bool) -> str:
    return re.sub(r"\{([a-gu])\}", lambda m: _swap(*swaps[m.group(1)], m.group(1), source and m.group(1) == "u"),
                  _esc(text))


def _source_html(items: list, swaps: dict) -> str:
    out = []
    for item in items:
        kind, text, rm = item[0], item[1], (item[2] if len(item) > 2 else None)
        if kind == "h1":
            piece = f'<span class="loop-h"><span class="loop-mk">#</span> {_esc(text)}</span>\n'
        elif kind == "h2":
            piece = f'\n<span class="loop-h"><span class="loop-mk">##</span> {_esc(text)}</span>\n'
        elif kind == "li":
            piece = f'<span class="loop-mk">-</span> {_fill(text, swaps, True)}\n'
        elif kind == "task":
            piece = f'<span class="loop-mk">- [ ]</span> {_fill(text, swaps, True)}\n'
        elif kind == "code":
            piece = f'<span class="loop-code">{_fill(text, swaps, True)}</span>\n'
        elif kind == "blank":
            piece = "\n"
        else:
            piece = f'{_fill(text, swaps, True)}\n'
        if rm:
            # A removable line is its own block, so it can collapse; the block ends the line.
            piece = f'<span class="loop-rl loop-r-{rm} a">{piece[:-1]}</span>'
        out.append(piece)
    return "".join(out)


def _preview_html(items: list, swaps: dict) -> str:
    out, list_open = [], False
    for item in items:
        kind, body, rm = item[0], item[1], (item[2] if len(item) > 2 else None)
        rmc = f' class="loop-rl loop-r-{rm} a"' if rm else ""
        if kind in ("li", "task") and not list_open:
            out.append("<ul>")
            list_open = True
        if kind not in ("li", "task") and list_open:
            out.append("</ul>")
            list_open = False
        if kind == "h3":
            out.append(f"<h3>{_esc(body)}</h3>")
        elif kind == "h4":
            out.append(f"<h4>{_esc(body)}</h4>")
        elif kind == "li":
            out.append(f"<li{rmc}>{_fill(body, swaps, False)}</li>")
        elif kind == "task":
            cls = f"loop-task loop-rl loop-r-{rm} a" if rm else "loop-task"
            out.append(f'<li class="{cls}">{_fill(body, swaps, False)}</li>')
        elif kind == "flow":
            nodes = []
            for i, node in enumerate(body):
                text, nrm = (node, None) if isinstance(node, str) else node
                cell = f'<span class="loop-node">{_esc(text)}</span>'
                if i:
                    seg = f'<span class="loop-arrow">→</span>{cell}'
                    cls = f"loop-fseg loop-rn loop-r-{nrm} a" if nrm else "loop-fseg"
                    cell = f'<span class="{cls}">{seg}</span>'
                nodes.append(cell)
            out.append(f'<div class="loop-flow">{"".join(nodes)}</div>')
        else:
            out.append(f"<p{rmc}>{_fill(body, swaps, False)}</p>")
    if list_open:
        out.append("</ul>")
    return "".join(out)


def scene_html(scene: dict, locale: str) -> str:
    """One loop: a terminal opens `scene["file"]` in MarsDawn, the reader makes change `u`, the
    agent makes the others, and the window folds back into the terminal."""
    ui = COPY[locale]
    swaps = scene.get("swaps", {})
    headings = [(it[0], it[1]) for it in scene["source"] if it[0] in ("h1", "h2")]
    active = headings.index(("h2", scene["active"]))
    rows = "".join(
        f'<div class="loop-h1row">{_esc(t)}</div>' if k == "h1" else
        f'<div class="loop-sub{" loop-row-u a" if i == active else ""}">{_esc(t)}</div>'
        for i, (k, t) in enumerate(headings))
    command = f"marsdawn open {scene['file']}"
    cmd_cls = "loop-cmd a" if len(command) == 28 else f"loop-cmd loop-cmd-{len(command)} a"
    ptr_cls = "loop-ptr a" if active == 2 else f"loop-ptr loop-ptr-r{active} a"
    long_cls = " loop-long" if scene.get("long") else ""
    return f"""<div class="loop-anim{LANG_CLASS[locale]}{long_cls}">
<div class="loop-frame" role="img" aria-label="{_esc(scene["alt"])}">
<div class="loop-stage" aria-hidden="true">
<div class="loop-win a">
<div class="loop-bar"><div class="loop-lights"><i></i><i></i><i></i></div><div class="loop-wtitle">{scene["file"]}</div><div class="loop-tools"><i></i><i class="on"></i><i></i></div></div>
<div class="loop-body">
<div class="loop-side"><div class="loop-tabs"><span class="on">{_esc(ui["outline"])}</span><span>{_esc(ui["files"])}</span></div><div class="loop-rows">{rows}</div></div>
<div class="loop-src">{_source_html(scene["source"], swaps)}</div>
<div class="loop-pre">{_preview_html(scene["preview"], swaps)}</div>
</div>
</div>
<div class="loop-term a">
<div class="loop-tbar"><div class="loop-lights"><i></i><i></i><i></i></div></div>
<div class="loop-tbody">
<div><span class="loop-p">›</span> <span class="{cmd_cls}">{command}</span><span class="loop-caret a"></span></div>
<div class="loop-l2 a"><span class="loop-p">›</span> {_esc(scene["ask"])}</div>
<div class="loop-l3 a">{_esc(scene["reply"])}</div>
</div>
</div>
<svg class="{ptr_cls}" viewBox="0 0 30 40" aria-hidden="true"><path d="M3 2v30l8-7.5 5.2 11.8 5.6-2.4-5.2-11.6H28Z" fill="#fff" stroke="#111" stroke-width="2" stroke-linejoin="round"/></svg>
</div>
</div>
<label class="loop-pause"><input type="checkbox" id="loop-pause" aria-label="{_esc(ui["pause"])}"><span aria-hidden="true">{_esc(ui["pause_short"])}</span></label>
</div>"""


def home_scene(locale: str) -> dict:
    copy = COPY[locale]
    source = [("h1", copy["title"])]
    preview = [("h3", copy["title"])]
    for h, p in copy["sections"]:
        source += [("h2", h), ("text", p)]
        preview += [("h4", h), ("p", p)]
    return {"file": FILE_NAME, "source": source, "preview": preview, "active": copy["sections"][1][0],
            "swaps": {k: (copy["old"], copy["new"]) for k in "aub"},
            "ask": copy["ask"], "reply": copy["reply"], "alt": copy["alt"]}


def loop_html(locale: str) -> str:
    return scene_html(home_scene(locale), locale)


# Lengths in the stage are written as `<number>u`; loop_css() turns them into calc() on --u.
_CSS = r"""/* The homepage loop. Generated by scripts/loop_anim.py; edit it there. */
/* --w-media (site.css): the same edges as the hero window and the screenshot plates. */
.loop-anim {
  --loop-width: max(100%, var(--w-media));
  width: var(--loop-width);
  margin: 8px calc((100% - var(--loop-width)) / 2) 0;
  display: grid;
  gap: 10px;
  justify-items: end;
}
.loop-frame {
  width: 100%;
  aspect-ratio: 16 / 9;
  position: relative;
  overflow: hidden;
  border-radius: var(--r-plate);
  background: var(--sand);
  container-type: inline-size;
}
/* The window follows the Mac's appearance, as the hero window does: the Dawn theme's light
   palette, or its night one (hero.css, from the kit). The terminal is dark in both. --t starts
   the loop with the window already open, so the frame never arrives empty. */
.loop-stage {
  --u: calc(100cqw / 1600);
  --t: 2.4s;
  --lw-bg: #FFFDFB; --lw-fg: #26211F; --lw-bar: #FFFFFF; --lw-bar-rule: #E6E6E6;
  --lw-pill: #FFFFFF; --lw-pill-edge: rgba(0,0,0,.08); --lw-seg: #F2F2F2; --lw-seg-on: #DCDCDC;
  --lw-side: #F4EEEA; --lw-side-rule: #E6DDD6; --lw-tab: #E9E1DB; --lw-rule: #EADFD8;
  --lw-accent: #C8471B; --lw-on-accent: #FFFFFF; --lw-select: #F2C6B3;
  --lw-glow: rgba(200,71,27,.28); --lw-glow-0: rgba(200,71,27,0);
  position: absolute; inset: 0;
  color: var(--lw-fg);
  font-family: var(--font);
  line-height: 1.5;
}
.loop-hans .loop-stage { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", sans-serif; }
.loop-ja .loop-stage { font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Hiragino Kaku Gothic ProN", sans-serif; }
.loop-stage .a {
  animation-duration: 10s; animation-iteration-count: infinite; animation-timing-function: linear;
  animation-fill-mode: both; animation-delay: calc(var(--d, 0s) - var(--t));
}
@media (prefers-color-scheme: dark) {
  .loop-stage {
    --lw-bg: #1C1A1F; --lw-fg: #EBE4DF; --lw-bar: #242B2F; --lw-bar-rule: #232323;
    --lw-pill: #273136; --lw-pill-edge: #3E5058; --lw-seg: #2F3A40; --lw-seg-on: #4D555A;
    --lw-side: #262229; --lw-side-rule: #3A343A; --lw-tab: #332E36; --lw-rule: #3A343A;
    --lw-accent: #FF8A50; --lw-on-accent: #1C1A1F; --lw-select: #6B3A2A;
    --lw-glow: rgba(255,138,80,.3); --lw-glow-0: rgba(255,138,80,0);
  }
}
.loop-anim:has(#loop-pause:checked) .a { animation-play-state: paused; }

/* The MarsDawn window in the Dawn theme. */
.loop-win {
  position: absolute; left: 400u; top: 50u; width: 1150u; height: 800u;
  border-radius: 14u; overflow: hidden; background: var(--lw-bg);
  box-shadow: 0 0 0 1u rgba(0,0,0,.18), 0 30u 50u -26u rgba(0,0,0,.45);
  transform-origin: -4% 79%; animation-name: loop-win;
}
@keyframes loop-win {
  0%, 15% { opacity: 0; transform: scale(.25); animation-timing-function: cubic-bezier(.3,.8,.2,1); }
  24% { opacity: 1; transform: none; }
  84% { opacity: 1; transform: none; animation-timing-function: cubic-bezier(.6,0,.8,.4); }
  92%, 100% { opacity: 0; transform: scale(.25); }
}
.loop-bar { position: relative; height: 56u; display: flex; align-items: center; padding: 0 18u;
  background: var(--lw-bar); border-bottom: 1u solid var(--lw-bar-rule); }
.loop-lights { display: flex; gap: 8u; position: relative; z-index: 1; }
.loop-lights i { width: 13u; height: 13u; border-radius: 50%; display: block; }
.loop-lights i:nth-child(1) { background: #FA5C5F; }
.loop-lights i:nth-child(2) { background: #FAC800; }
.loop-lights i:nth-child(3) { background: #34C758; }
.loop-wtitle { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
  font-size: 18u; font-weight: 600; }
.loop-tools { margin-left: auto; display: flex; gap: 4u; padding: 4u; border-radius: 18u; background: var(--lw-pill);
  box-shadow: 0 0 0 1u var(--lw-pill-edge); position: relative; z-index: 1; }
.loop-tools i { width: 40u; height: 28u; border-radius: 14u; display: block; background: var(--lw-seg); }
.loop-tools i.on { background: var(--lw-seg-on); }
.loop-body { display: grid; grid-template-columns: 230u 1fr 1fr; height: calc(100% - 56u); }
.loop-side { background: var(--lw-side); border-right: 1u solid var(--lw-side-rule); padding: 14u 12u; }
.loop-tabs { display: grid; grid-template-columns: 1fr 1fr; gap: 4u; margin-bottom: 14u; }
.loop-tabs span { text-align: center; font-size: 15u; line-height: 1.2; padding: 6u 0; border-radius: 7u; background: var(--lw-tab); }
.loop-tabs span.on { background: var(--lw-accent); color: var(--lw-on-accent); font-weight: 600; }
.loop-rows { display: grid; gap: 2u; font-size: 16u; line-height: 1.25; }
.loop-rows div { padding: 8u 12u; border-radius: 7u; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.loop-h1row { font-weight: 600; }
.loop-rows .loop-sub { padding-left: 26u; }
.loop-row-u { animation-name: loop-row; }
@keyframes loop-row {
  0%, 29% { background: transparent; color: var(--lw-fg); }
  30%, 90% { background: var(--lw-accent); color: var(--lw-on-accent); }
  92%, 100% { background: transparent; color: var(--lw-fg); }
}
.loop-src { padding: 26u; border-right: 1u solid var(--lw-rule); font: 20u/1.6 var(--mono); white-space: pre-wrap; overflow: hidden; }
.loop-h { font-weight: 700; }
.loop-mk { color: var(--lw-accent); }
.loop-pre { padding: 30u 36u; overflow: hidden; }
.loop-pre h3 { margin: 0 0 22u; padding-bottom: 10u; border-bottom: 1u solid var(--lw-rule); font-size: 40u; font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; color: inherit; }
.loop-pre h4 { margin: 22u 0 8u; font-size: 25u; font-weight: 700; letter-spacing: -0.01em; line-height: 1.3; color: inherit; }
.loop-pre p { margin: 0; font-size: 20u; line-height: 1.55; }

/* A day that changes: both words share one grid cell and have the same width. */
.loop-day { position: relative; display: inline-grid; border-radius: 4u; font-variant-numeric: tabular-nums; }
.loop-day > span { grid-area: 1 / 1; white-space: nowrap; }
.loop-new { clip-path: inset(0 100% 0 0); }

/* The reader's own edit, in the source: select the day, then type the new one. */
.loop-src .loop-d-u .loop-old { animation-name: loop-u-old; }
.loop-src .loop-d-u .loop-new { animation-name: loop-u-new; }
.loop-src .loop-d-u .loop-new.loop-n2 { animation-timing-function: steps(2, end); }
.loop-src .loop-d-u .loop-new.loop-n5 { animation-timing-function: steps(5, end); }
@keyframes loop-u-old {
  0%, 35% { opacity: 1; background: transparent; }
  36%, 40.9% { opacity: 1; background: var(--lw-select); }
  41%, 94.9% { opacity: 0; background: transparent; }
  95%, 100% { opacity: 1; background: transparent; }
}
@keyframes loop-u-new {
  0%, 41% { clip-path: inset(0 100% 0 0); }
  46%, 94.9% { clip-path: inset(0 0 0 0); }
  95%, 100% { clip-path: inset(0 100% 0 0); }
}
.loop-ecaret {
  position: absolute; top: 0.2em; left: 0; width: 2u; height: 1.1em; background: var(--lw-accent); opacity: 0;
  animation-name: loop-ecaret, loop-ecaret-x;
}
/* The caret follows the typed characters: the same steps as the reveal. */
.loop-ecaret.loop-n2 { animation-timing-function: linear, steps(2, end); }
.loop-ecaret.loop-n5 { animation-timing-function: linear, steps(5, end); }
@keyframes loop-ecaret-x { 0%, 41% { left: 0; } 46%, 100% { left: 100%; } }
@keyframes loop-ecaret {
  0%, 40.9% { opacity: 0; }
  41%, 43%, 45%, 47%, 49%, 51% { opacity: 1; }
  44%, 48%, 52%, 100% { opacity: 0; }
}

/* The preview follows the reader's save. */
.loop-pre .loop-d-u .loop-old { animation-name: loop-pu-old; }
.loop-pre .loop-d-u .loop-new { animation-name: loop-pu-new; }
@keyframes loop-pu-old { 0%, 46.9% { opacity: 1; } 47%, 94.9% { opacity: 0; } 95%, 100% { opacity: 1; } }
@keyframes loop-pu-new { 0%, 46.9% { clip-path: inset(0 100% 0 0); } 47%, 94.9% { clip-path: inset(0 0 0 0); } 95%, 100% { clip-path: inset(0 100% 0 0); } }

/* The agent's edits: the other two sections, a beat apart. */
.loop-d-a { --d: 0s; }
.loop-d-b { --d: .45s; }
.loop-d-a .loop-old, .loop-d-b .loop-old { animation-name: loop-a-old; }
.loop-d-a .loop-new, .loop-d-b .loop-new { animation-name: loop-a-new; }
.loop-d-a, .loop-d-b { animation-name: loop-a-glow; }
@keyframes loop-a-old { 0%, 59.9% { opacity: 1; } 60%, 94.9% { opacity: 0; } 95%, 100% { opacity: 1; } }
@keyframes loop-a-new { 0%, 59.9% { clip-path: inset(0 100% 0 0); } 60%, 94.9% { clip-path: inset(0 0 0 0); } 95%, 100% { clip-path: inset(0 100% 0 0); } }
@keyframes loop-a-glow {
  0%, 59.9% { background: var(--lw-glow-0); }
  60% { background: var(--lw-glow); }
  78%, 100% { background: var(--lw-glow-0); }
}

/* The terminal starts centred and large, then steps aside for the window. */
.loop-term {
  position: absolute; left: 40u; top: 520u; width: 620u; height: 330u; border-radius: 12u; overflow: hidden;
  background: #211C1A; color: #EDE6E1; z-index: 3;
  box-shadow: 0 0 0 1u rgba(0,0,0,.35), 0 26u 44u -22u rgba(0,0,0,.55);
  --term-x: 450u; --term-y: -235u;
  animation-name: loop-term;
}
@keyframes loop-term {
  0%, 13.5% { transform: translate(var(--term-x), var(--term-y)) scale(1.3); animation-timing-function: cubic-bezier(.5,0,.2,1); }
  22% { transform: none; }
  86% { transform: none; animation-timing-function: cubic-bezier(.5,0,.2,1); }
  96%, 100% { transform: translate(var(--term-x), var(--term-y)) scale(1.3); }
}
.loop-tbar { height: 34u; display: flex; align-items: center; padding: 0 14u; background: #2B2522; }
.loop-tbar .loop-lights i { width: 11u; height: 11u; background: #4A413C; }
.loop-tbody { padding: 18u 22u; font: 19u/1.6 var(--mono); display: grid; gap: 6u; }
.loop-p { color: #E0875E; }
.loop-cmd { display: inline-block; vertical-align: bottom; overflow: hidden; white-space: nowrap; width: 0; animation-name: loop-type; }
@keyframes loop-type {
  0%, 3% { width: 0; animation-timing-function: steps(28, end); }
  12.5%, 90% { width: 28ch; }
  92%, 100% { width: 0; }
}
.loop-caret { display: inline-block; width: 10u; height: 1.1em; background: #EDE6E1; vertical-align: -0.2em; animation-name: loop-tcaret; }
@keyframes loop-tcaret {
  0%, 1.5%, 3%, 13.5%, 90% { opacity: 1; }
  0.8%, 2.2%, 14%, 89.9% { opacity: 0; }
  91%, 93%, 95%, 97%, 99% { opacity: 1; }
  92%, 94%, 96%, 98% { opacity: 0; }
}
.loop-l2 { animation-name: loop-l2; }
.loop-l3 { animation-name: loop-l3; color: #9FCBB1; }
@keyframes loop-l2 { 0%, 48% { opacity: 0; transform: translateY(8u); } 51%, 88% { opacity: 1; transform: none; } 91%, 100% { opacity: 0; transform: none; } }
@keyframes loop-l3 { 0%, 55% { opacity: 0; transform: translateY(8u); } 58%, 88% { opacity: 1; transform: none; } 91%, 100% { opacity: 0; transform: none; } }

/* The pointer clicks one outline row, then leaves. */
.loop-ptr { position: absolute; left: 0; top: 0; width: 30u; height: 40u; z-index: 4; animation-name: loop-ptr; }
@keyframes loop-ptr {
  0%, 22% { opacity: 0; transform: translate(760u, 520u); }
  23% { opacity: 1; transform: translate(760u, 520u); animation-timing-function: cubic-bezier(.4,0,.2,1); }
  28.5% { transform: translate(468u, 238u) scale(1); }
  29.3% { transform: translate(468u, 238u) scale(.86); }
  30.2% { opacity: 1; transform: translate(468u, 238u) scale(1); animation-timing-function: cubic-bezier(.4,0,.2,1); }
  36% { opacity: 1; }
  38%, 100% { opacity: 0; transform: translate(520u, 360u); }
}

/* Pause and play. A checkbox, so it works with the keyboard and without a script. */
.loop-pause {
  position: relative;
  display: inline-flex; align-items: center; min-height: 28px; padding: 3px 12px;
  border: 1px solid var(--hairline); border-radius: 999px;
  color: var(--dust); font-size: 0.82rem; cursor: pointer;
}
.loop-pause input { position: absolute; inset: 0; margin: 0; opacity: 0; cursor: pointer; }
.loop-pause:has(input:focus-visible) { outline: 2px solid var(--ember); outline-offset: 2px; }
.loop-pause:hover { color: var(--ink); }
.loop-pause:has(input:checked) { color: var(--paper); background: var(--ink); border-color: var(--ink); }

/* Phones: the whole stage at 358px wide sets its text at about 4px. Show the part that carries
   the story instead, the source and the preview (x 630 to 1550 of the stage), at a larger scale,
   with the terminal docked along their foot. The outline pane and the pointer fall outside. */
@media (max-width: 560px) {
  .loop-frame { aspect-ratio: 920 / 860; }
  .loop-stage { --u: calc(100cqw / 920); inset: auto; left: -630u; top: -50u; width: 1600u; height: 900u; }
  .loop-term { left: 650u; top: 580u; --term-x: 130u; --term-y: -265u; }
  .loop-ptr { display: none; }
}

/* Reduced motion: the edited note, still, and nothing to pause. */
@media (prefers-reduced-motion: reduce) {
  .loop-stage { --t: 7.2s; }
  .loop-stage .a { animation-play-state: paused; }
  .loop-pause { display: none; }
}
"""


def _scene_css() -> str:
    """Rules only the /templates/ scenes use, appended after the home page's: removals, a flow
    diagram, task lists, commands of other lengths, the pointer on other rows, a third agent edit."""
    parts = [r"""
/* ---- Scenes beyond the home page (/templates/). Appended; the rules above are the home page's. ---- */
.loop-d-c { --d: .9s; }
.loop-d-c .loop-old { animation-name: loop-a-old; }
.loop-d-c .loop-new { animation-name: loop-a-new; }
.loop-d-c { animation-name: loop-a-glow; }
/* Scene colours, light and night, from the kit's Dawn theme (hero_sources.json): code is the
   theme's string colour, a flow node sits on its surface. The rest reuse the --lw-* palette. */
.loop-stage { --lw-code: #2F6F5E; --lw-node: #FFF7F4; --lw-node-edge: #D66A4D; --lw-muted: #6F6660; }
@media (prefers-color-scheme: dark) {
  .loop-stage { --lw-code: #7FD1B9; --lw-node: #262229; --lw-node-edge: #A15D3F; --lw-muted: #A39992; }
}
.loop-code { color: var(--lw-code); }

/* A scene with a longer document: the terminal stops short of the source pane (the window's
   sidebar ends at 630u), so no line of source is hidden behind it. */
.loop-long .loop-term { width: 575u; }

/* A line, block or list item that goes away. */
.loop-rl { overflow: hidden; }
.loop-src .loop-rl { display: block; }
.loop-src .loop-r-u { animation-name: loop-u-rl; }
.loop-pre .loop-r-u { animation-name: loop-pu-rl; }
.loop-r-a { --d: 0s; }
.loop-r-b { --d: .45s; }
.loop-r-c { --d: .9s; }
.loop-rl.loop-r-a, .loop-rl.loop-r-b, .loop-rl.loop-r-c { animation-name: loop-a-rl; }
@keyframes loop-u-rl {
  0%, 35% { max-height: 5em; opacity: 1; background: transparent; }
  36%, 40.9% { max-height: 5em; opacity: 1; background: var(--lw-select); }
  41% { max-height: 5em; opacity: 1; background: var(--lw-select); }
  44%, 94.9% { max-height: 0; opacity: 0; background: transparent; }
  95%, 100% { max-height: 5em; opacity: 1; background: transparent; }
}
@keyframes loop-pu-rl {
  0%, 46.9% { max-height: 5em; opacity: 1; }
  49%, 94.9% { max-height: 0; opacity: 0; }
  95%, 100% { max-height: 5em; opacity: 1; }
}
@keyframes loop-a-rl {
  0%, 57% { max-height: 5em; opacity: 1; background: var(--lw-glow-0); }
  59.5% { max-height: 5em; opacity: 1; background: var(--lw-glow); }
  63%, 94.9% { max-height: 0; opacity: 0; background: var(--lw-glow-0); }
  95%, 100% { max-height: 5em; opacity: 1; background: var(--lw-glow-0); }
}

/* A flow diagram, as the preview draws a Mermaid flowchart; a step can go away. */
.loop-flow { display: flex; align-items: center; margin: 12u 0 20u; }
.loop-flow > * { flex-shrink: 0; }
.loop-node { display: inline-flex; align-items: center; height: 40u; padding: 0 9u; border-radius: 7u;
  background: var(--lw-node); border: 1.5u solid var(--lw-node-edge); color: var(--lw-fg); font-size: 14u; font-weight: 650; white-space: nowrap; }
.loop-fseg { display: inline-flex; align-items: center; overflow: hidden; white-space: nowrap; max-width: 30em; }
.loop-arrow { padding: 0 5u; color: var(--lw-accent); font-size: 15u; }
.loop-pre .loop-rn.loop-r-u { animation-name: loop-pu-rn; }
.loop-rn.loop-r-a, .loop-rn.loop-r-b, .loop-rn.loop-r-c { animation-name: loop-a-rn; }
@keyframes loop-pu-rn {
  0%, 46.9% { max-width: 30em; opacity: 1; }
  49%, 94.9% { max-width: 0; opacity: 0; }
  95%, 100% { max-width: 30em; opacity: 1; }
}
@keyframes loop-a-rn {
  0%, 59.9% { max-width: 30em; opacity: 1; }
  63%, 94.9% { max-width: 0; opacity: 0; }
  95%, 100% { max-width: 30em; opacity: 1; }
}

/* Lists and task lists in the preview. */
.loop-pre ul { margin: 0 0 4u; padding-left: 26u; font-size: 20u; line-height: 1.55; }
.loop-pre li { margin: 0; }
.loop-pre li.loop-task { list-style: none; margin-left: -26u; }
.loop-task::before { content: ""; display: inline-block; width: 0.75em; height: 0.75em; margin-right: 0.45em;
  border: 1.5u solid var(--lw-muted); border-radius: 3u; vertical-align: -0.05em; }
"""]
    # The typed-in new text, and the caret after it, step one character at a time.
    for n in range(1, 13):
        if n in (2, 5):
            continue
        parts.append(f".loop-src .loop-d-u .loop-new.loop-n{n} {{ animation-timing-function: steps({n}, end); }}\n"
                     f".loop-ecaret.loop-n{n} {{ animation-timing-function: linear, steps({n}, end); }}\n")
    # `marsdawn open <file>` for other file names: the same typing, at that length.
    for n in range(18, 41):
        if n == 28:
            continue
        parts.append(f".loop-cmd-{n} {{ animation-name: loop-type-{n}; }}\n"
                     f"@keyframes loop-type-{n} {{\n"
                     f"  0%, 3% {{ width: 0; animation-timing-function: steps({n}, end); }}\n"
                     f"  12.5%, 90% {{ width: {n}ch; }}\n"
                     f"  92%, 100% {{ width: 0; }}\n}}\n")
    # The pointer on outline row r (0 is the document's title), clicking it like the home page's.
    for r in range(1, 9):
        if r == 2:
            continue
        y = 162 + 38 * r
        parts.append(f".loop-ptr-r{r} {{ animation-name: loop-ptr-r{r}; }}\n"
                     f"@keyframes loop-ptr-r{r} {{\n"
                     f"  0%, 22% {{ opacity: 0; transform: translate(760u, 520u); }}\n"
                     f"  23% {{ opacity: 1; transform: translate(760u, 520u); animation-timing-function: cubic-bezier(.4,0,.2,1); }}\n"
                     f"  28.5% {{ transform: translate(468u, {y}u) scale(1); }}\n"
                     f"  29.3% {{ transform: translate(468u, {y}u) scale(.86); }}\n"
                     f"  30.2% {{ opacity: 1; transform: translate(468u, {y}u) scale(1); animation-timing-function: cubic-bezier(.4,0,.2,1); }}\n"
                     f"  36% {{ opacity: 1; }}\n"
                     f"  38%, 100% {{ opacity: 0; transform: translate(520u, {y + 110}u); }}\n}}\n")
    return "".join(parts)


def loop_css() -> str:
    return re.sub(r"(-?\d+(?:\.\d+)?)u\b", r"calc(\1 * var(--u))", _CSS + _scene_css())
