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
        "pause": "Pause the animation", "pause_short": "Pause", "play_short": "Play",
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
        "pause": "暫停動畫", "pause_short": "暫停", "play_short": "播放",
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
        "pause": "暂停动画", "pause_short": "暂停", "play_short": "播放",
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
        "pause": "アニメーションを一時停止", "pause_short": "一時停止", "play_short": "再生",
    },
}

LANG_CLASS = {"en": "", "zh-hant": " loop-hant", "zh-hans": " loop-hans", "ja": " loop-ja"}

_esc = html.escape


def _day(copy: dict, which: str, caret: bool) -> str:
    steps = len(copy["new"])
    out = (f'<span class="loop-day loop-d-{which} a"><span class="loop-old a">{_esc(copy["old"])}</span>'
           f'<span class="loop-new loop-n{steps} a">{_esc(copy["new"])}</span></span>')
    if caret:
        out += '<span class="loop-ecaret a"></span>'
    return out


def _fill(text: str, copy: dict, source: bool) -> str:
    return re.sub(r"\{([aub])\}", lambda m: _day(copy, m.group(1), source and m.group(1) == "u"), _esc(text))


def loop_html(locale: str) -> str:
    copy = COPY[locale]
    rows = f'<div class="loop-h1row">{_esc(copy["title"])}</div>' + "".join(
        f'<div class="loop-sub{" loop-row-u a" if i == 1 else ""}">{_esc(h)}</div>'
        for i, (h, _) in enumerate(copy["sections"]))
    source = f'<span class="loop-h"><span class="loop-mk">#</span> {_esc(copy["title"])}</span>\n' + "".join(
        f'\n<span class="loop-h"><span class="loop-mk">##</span> {_esc(h)}</span>\n{_fill(p, copy, True)}\n'
        for h, p in copy["sections"])
    preview = f'<h3>{_esc(copy["title"])}</h3>' + "".join(
        f'<h4>{_esc(h)}</h4><p>{_fill(p, copy, False)}</p>' for h, p in copy["sections"])
    return f"""<div class="loop-anim{LANG_CLASS[locale]}">
<div class="loop-frame" role="img" aria-label="{_esc(copy["alt"])}">
<div class="loop-stage">
<div class="loop-win a">
<div class="loop-bar"><div class="loop-lights"><i></i><i></i><i></i></div><div class="loop-wtitle">{FILE_NAME}</div><div class="loop-tools"><i></i><i class="on"></i><i></i></div></div>
<div class="loop-body">
<div class="loop-side"><div class="loop-tabs"><span class="on">{_esc(copy["outline"])}</span><span>{_esc(copy["files"])}</span></div><div class="loop-rows">{rows}</div></div>
<div class="loop-src">{source}</div>
<div class="loop-pre">{preview}</div>
</div>
</div>
<div class="loop-term a">
<div class="loop-tbar"><div class="loop-lights"><i></i><i></i><i></i></div></div>
<div class="loop-tbody">
<div><span class="loop-p">›</span> <span class="loop-cmd a">{COMMAND}</span><span class="loop-caret a"></span></div>
<div class="loop-l2 a"><span class="loop-p">›</span> {_esc(copy["ask"])}</div>
<div class="loop-l3 a">{_esc(copy["reply"])}</div>
</div>
</div>
<svg class="loop-ptr a" viewBox="0 0 30 40" aria-hidden="true"><path d="M3 2v30l8-7.5 5.2 11.8 5.6-2.4-5.2-11.6H28Z" fill="#fff" stroke="#111" stroke-width="2" stroke-linejoin="round"/></svg>
</div>
</div>
<label class="loop-pause"><input type="checkbox" id="loop-pause" aria-label="{_esc(copy["pause"])}"><span class="loop-pause-on" aria-hidden="true">{_esc(copy["pause_short"])}</span><span class="loop-pause-off" aria-hidden="true">{_esc(copy["play_short"])}</span></label>
</div>"""


# Lengths in the stage are written as `<number>u`; loop_css() turns them into calc() on --u.
_CSS = r"""/* The homepage loop. Generated by scripts/loop_anim.py; edit it there. */
.loop-anim {
  --shot-width: max(100%, min(76rem, 100vw - 48px));
  width: var(--shot-width);
  margin: 8px calc((100% - var(--shot-width)) / 2) 0;
  display: grid;
  gap: 10px;
  justify-items: end;
}
.loop-frame {
  width: 100%;
  aspect-ratio: 16 / 9;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  background: var(--sand);
  container-type: inline-size;
}
.loop-stage {
  --u: calc(100cqw / 1600);
  --t: 0s;
  position: absolute; inset: 0;
  color: #26211F;
  font-family: var(--font);
  line-height: 1.5;
}
.loop-hans .loop-stage { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", sans-serif; }
.loop-ja .loop-stage { font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Hiragino Kaku Gothic ProN", sans-serif; }
.loop-stage .a {
  animation-duration: 10s; animation-iteration-count: infinite; animation-timing-function: linear;
  animation-fill-mode: both; animation-delay: calc(var(--d, 0s) - var(--t));
}
.loop-anim:has(#loop-pause:checked) .a { animation-play-state: paused; }

/* The MarsDawn window, in the Dawn theme in both colour schemes, like the screenshots. */
.loop-win {
  position: absolute; left: 400u; top: 50u; width: 1150u; height: 800u;
  border-radius: 14u; overflow: hidden; background: #FFFDFB;
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
  background: #fff; border-bottom: 1u solid #E6E6E6; }
.loop-lights { display: flex; gap: 8u; position: relative; z-index: 1; }
.loop-lights i { width: 13u; height: 13u; border-radius: 50%; display: block; }
.loop-lights i:nth-child(1) { background: #FA5C5F; }
.loop-lights i:nth-child(2) { background: #FAC800; }
.loop-lights i:nth-child(3) { background: #34C758; }
.loop-wtitle { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
  font-size: 18u; font-weight: 600; }
.loop-tools { margin-left: auto; display: flex; gap: 4u; padding: 4u; border-radius: 18u; background: #fff;
  box-shadow: 0 0 0 1u rgba(0,0,0,.08); position: relative; z-index: 1; }
.loop-tools i { width: 40u; height: 28u; border-radius: 14u; display: block; background: #F2F2F2; }
.loop-tools i.on { background: #DCDCDC; }
.loop-body { display: grid; grid-template-columns: 230u 1fr 1fr; height: calc(100% - 56u); }
.loop-side { background: #F4EEEA; border-right: 1u solid #E6DDD6; padding: 14u 12u; }
.loop-tabs { display: grid; grid-template-columns: 1fr 1fr; gap: 4u; margin-bottom: 14u; }
.loop-tabs span { text-align: center; font-size: 15u; line-height: 1.2; padding: 6u 0; border-radius: 7u; background: #E9E1DB; }
.loop-tabs span.on { background: #C8471B; color: #fff; font-weight: 600; }
.loop-rows { display: grid; gap: 2u; font-size: 16u; line-height: 1.25; }
.loop-rows div { padding: 8u 12u; border-radius: 7u; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.loop-h1row { font-weight: 600; }
.loop-rows .loop-sub { padding-left: 26u; }
.loop-row-u { animation-name: loop-row; }
@keyframes loop-row {
  0%, 29% { background: transparent; color: #26211F; }
  30%, 90% { background: #C8471B; color: #fff; }
  92%, 100% { background: transparent; color: #26211F; }
}
.loop-src { padding: 26u; border-right: 1u solid #ECE6E1; font: 20u/1.6 var(--mono); white-space: pre-wrap; overflow: hidden; }
.loop-h { font-weight: 700; }
.loop-mk { color: #C8471B; }
.loop-pre { padding: 30u 36u; overflow: hidden; }
.loop-pre h3 { margin: 0 0 22u; padding-bottom: 10u; border-bottom: 1u solid #EADFD8; font-size: 40u; font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; color: inherit; }
.loop-pre h4 { margin: 22u 0 8u; font-size: 25u; font-weight: 700; letter-spacing: -0.01em; line-height: 1.3; color: inherit; }
.loop-pre p { margin: 0; font-size: 20u; line-height: 1.55; }

/* A day that changes: both words share one grid cell and have the same width. */
.loop-day { display: inline-grid; border-radius: 4u; font-variant-numeric: tabular-nums; }
.loop-day > span { grid-area: 1 / 1; white-space: nowrap; }
.loop-new { clip-path: inset(0 100% 0 0); }

/* The reader's own edit, in the source: select the day, then type the new one. */
.loop-src .loop-d-u .loop-old { animation-name: loop-u-old; }
.loop-src .loop-d-u .loop-new { animation-name: loop-u-new; }
.loop-src .loop-d-u .loop-new.loop-n2 { animation-timing-function: steps(2, end); }
.loop-src .loop-d-u .loop-new.loop-n5 { animation-timing-function: steps(5, end); }
@keyframes loop-u-old {
  0%, 35% { opacity: 1; background: transparent; }
  36%, 40.9% { opacity: 1; background: #F2C6B3; }
  41%, 94.9% { opacity: 0; background: transparent; }
  95%, 100% { opacity: 1; background: transparent; }
}
@keyframes loop-u-new {
  0%, 41% { clip-path: inset(0 100% 0 0); }
  46%, 94.9% { clip-path: inset(0 0 0 0); }
  95%, 100% { clip-path: inset(0 100% 0 0); }
}
.loop-ecaret { display: inline-block; width: 2u; height: 1.05em; background: #C8471B; vertical-align: -0.15em; margin-left: 1u; opacity: 0; animation-name: loop-ecaret; }
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
  0%, 59.9% { background: rgba(200,71,27,0); }
  60% { background: rgba(200,71,27,.28); }
  78%, 100% { background: rgba(200,71,27,0); }
}

/* The terminal starts centred and large, then steps aside for the window. */
.loop-term {
  position: absolute; left: 40u; top: 520u; width: 620u; height: 330u; border-radius: 12u; overflow: hidden;
  background: #211C1A; color: #EDE6E1; z-index: 3;
  box-shadow: 0 0 0 1u rgba(0,0,0,.35), 0 26u 44u -22u rgba(0,0,0,.55);
  animation-name: loop-term;
}
@keyframes loop-term {
  0%, 13.5% { transform: translate(450u, -235u) scale(1.3); animation-timing-function: cubic-bezier(.5,0,.2,1); }
  22% { transform: none; }
  86% { transform: none; animation-timing-function: cubic-bezier(.5,0,.2,1); }
  96%, 100% { transform: translate(450u, -235u) scale(1.3); }
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
.loop-pause-off { display: none; }
.loop-pause:has(input:checked) .loop-pause-on { display: none; }
.loop-pause:has(input:checked) .loop-pause-off { display: inline; }

/* Reduced motion: the edited note, still, and nothing to pause. */
@media (prefers-reduced-motion: reduce) {
  .loop-stage { --t: 7.2s; }
  .loop-stage .a { animation-play-state: paused; }
  .loop-pause { display: none; }
}
"""


def loop_css() -> str:
    return re.sub(r"(-?\d+(?:\.\d+)?)u\b", r"calc(\1 * var(--u))", _CSS)
