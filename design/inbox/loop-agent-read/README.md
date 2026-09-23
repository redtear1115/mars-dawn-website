# Inbox: 讀 agent 寫的 Markdown — three plates

**For Claude.** These are the three pictures, and the three silent clips, for the homepage loop. This PR does not wire them into the page. Do not merge it as the live change.

The plates are drawn for the Traditional Chinese page. The strings are in `plate.html`; the other three locales are listed there and need their own render before the same pictures can ship in en, zh-Hans or ja.

## What each one shows

The loop on the homepage is three sentences. Each plate is one sentence.

| File | Step | What you see |
|------|------|----------------|
| `01-write.png` / `.mp4` | Agent 動筆 | `README.md` being written, with `notes.md` and `SPEC.md` beside it |
| `02-read.png` / `.mp4` | 你在 MarsDawn 裡讀 | `SPEC.md` open side by side: source, then the rendered heading, flowchart and highlighted command |
| `03-revise.png` / `.mp4` | Agent 修改 | A note, 短一點。, sits **outside** the window. The flowchart loses its last step, and the source changes to match |

The still is the last frame of its clip. The clip is 5 seconds, 12 fps, 1600×900, silent H.264, about the same size as the still.

## How to place them

The loop is three narrow columns. These plates are 16:9 and will not read there. Stack them under the loop's heading, one after another, the way the screenshots break out of the column. The sentence already under each step is the caption. Keep the real screenshots in「App 實際的樣子」; these do not replace them.

Use the still. Play the clip only when the reader has not asked for reduced motion, muted, and once — the clip starts empty and ends on the still, so looping jumps. The page can do that without a script (`<video muted playsinline poster="…">` is not a loop). If a script would be needed to start it on scroll, ship the still and leave the clip in the repo.

Suggested public paths, if they ship:

- `public/assets/loop/01-write.png`
- `public/assets/loop/02-read.png`
- `public/assets/loop/03-revise.png`
- and the `.mp4` next to each still

## Alt text

zh-Hant

1. Agent 寫出三份 Markdown：最前面是 README.md，旁邊是 notes.md 和 SPEC.md。
2. MarsDawn 並排打開 SPEC.md：左邊是原始碼，右邊是排好的頁面，有流程圖，也有上色的程式碼。
3. 視窗外面有一張寫著「短一點。」的筆記，SPEC.md 的流程圖少了最後一步。

en

1. The agent drafts three Markdown files: README.md in front, notes.md and SPEC.md beside it.
2. MarsDawn opens SPEC.md side by side: the source on the left, and on the right the rendered page, with a flowchart and highlighted code.
3. A note reading "Shorter." sits outside the window, and the flowchart in SPEC.md has lost its last step.

zh-Hans

1. Agent 写出三份 Markdown：最前面是 README.md，旁边是 notes.md 和 SPEC.md。
2. MarsDawn 并排打开 SPEC.md：左边是源代码，右边是排好的页面，有流程图，也有着色的代码。
3. 窗口外面有一张写着「短一点。」的笔记，SPEC.md 的流程图少了最后一步。

ja

1. エージェントが Markdown を三つ書く。手前が README.md、隣が notes.md と SPEC.md。
2. MarsDawn が SPEC.md を左右に開く。左がソース、右が組版されたページで、フローチャートと色の付いたコードがある。
3. ウィンドウの外に「短く。」と書いたメモがあり、SPEC.md のフローチャートは最後の一歩が消えている。

The en, zh-Hans and ja lines describe a re-render. They do not describe the pictures in this folder, which are zh-Hant.

## What is drawn, and what is not

The window uses the hero's measured title-bar colours and the Dawn palette from `hero.css` (heading, keyword, the purple for `marsdawn`, the green for the file name). The flowchart is a schematic of the rendered Mermaid in the Telemetry Pipeline screenshot: peach boxes, a rust stroke. It is not a capture of Mermaid, and it is not a new control in the app.

The note is a piece of paper outside the window. The app does not annotate a preview. The revision is the file changing, then being opened again.

Regenerate with `python3 render_plates.py` from this directory. It needs Google Chrome and ffmpeg. Proof frames, nine of them, come from `--proof`.

Co-authored-by: Grok <grok@southern-light.dev>
