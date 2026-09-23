# Inbox: the loop as one video, in English

**For Claude.** One recorded video of the whole loop for the homepage: the agent writes, you read and edit in MarsDawn, the agent makes the rest agree, you read again and export. There is one English cut, and every locale uses it. This folder does not wire it into the page. Do not merge it as the live change.

**Do not put it on the site yet.** The video shows the Outline sidebar, and Outline is not in the App Store version (1.0.1 shipped with the Files tab only). The owner decided on 2026-09-24 that the video waits for the version with Outline. Check the iTunes lookup before placing it.

| File | |
|------|--|
| `launch-note-loop-en.mp4` | 51.6 s, 1600×900, 60 fps, H.264, silent, faststart, 2.9 MB |
| `launch-note-loop-en-poster.png` | Poster frame: "Who does what" after the agent's edit |
| `fixtures/` | The note in its three states. Every word on screen comes from these files |
| `rig/` | The recording, cutting and checking scripts |

## What happens

| Shot | Seconds | What you see |
|------|---------|--------------|
| 1 | 0–3.8 | Terminal. `› Write a launch note for the new sign-in page. Save it as launch-note.md.` |
| 2 | 3.8–8.4 | The reply, then `› marsdawn open launch-note.md` |
| 3 | 8.4–12.9 | MarsDawn opens it side by side, Dawn theme; slow push in |
| 4 | 12.9–19.1 | View → Show Sidebar; Outline; click "When it ships", both panes jump |
| 5 | 19.1–24.5 | Double-click `Wednesday`, type `Friday`, save; push in |
| 6 | 24.5–29.8 | Terminal. `› I edited "When it ships". Make the other sections agree. Don't add sections.` |
| 7 | 29.8–37.2 | The reply; back in MarsDawn the file has reloaded, now Friday throughout |
| 8 | 37.2–42.4 | Outline: "What changed", then "Who does what" |
| 9 | 42.4–51.6 | File → Export as PDF…, Save; the PDF opens in MarsDawn, Friday everywhere |

The note starts with the launch on Wednesday. The reader moves it to Friday in one section; the agent changes the other two sections to match, and leaves Design's Tuesday deadline and Rollback alone. The PDF is the edited version.

## How it was made

- Everything is a real screen recording of a Mac (1920×1080 at 1x), one continuous take. There are hard cuts between shots. The push-ins are deterministic crop and zoom keyframes (`rig/render.py`). No generative model touched any frame, so no glyph was redrawn.
- The app is a Release build of mars-dawn `main` at `d891882` (it has Outline), with the paywall flag off, as for the store screenshots. It ran as a throwaway copy under its own bundle id. The installed app was not touched.
- The terminal is Terminal.app with the built-in Basic profile and a dark background, and the prompt is `›`. The title bar is cropped out, because it carries local paths. The "agent" is `rig/replay.sh`. It types the user's lines, prints the replies, and writes the file with `cp`. `marsdawn open` is the real CLI, 0.5.1.
- The pointer and the typing are scripted (`rig/take.sh`, `rig/vidax.swift`). Some segments are played 1.25–1.3× faster to fit about 50 seconds. The table above uses cut time.
- The status items at the right of the menu bar that fall inside the crop (the recording indicator and its neighbours) are covered with an empty stretch of the same menu bar.
- The banner "Another app/agent changed this file. Your previous text was kept. Undo · Browse All Versions…" is the app's real behavior when the agent overwrites the file. It was left in.

## What was checked

`rig/verify.py` reads key frames with Vision OCR and compares them word for word with the fixtures and with `replay.sh`. The comparisons cover the ask, the reply and the command; v1 in the preview; the Wednesday section after the jump; the user's "Friday" edit; all three terminal lines intact; the agent's reply; v3 after reload; "Who does what" on Friday; and the exported PDF. They also check that "Wednesday" appears nowhere after the agent's edit. 19 of 19 pass on this encode. The check can fail: on an earlier take it failed on `launch-fote.md`, where the pointer covered the "n", and that take was re-recorded.

It was also checked during the take itself:

- the file on disk after the user's save is byte-identical to `fixtures/launch-note.v2-user.md`;
- after the agent's write, the source pane holds exactly `fixtures/launch-note.v3-agent.md`;
- the PDF was written next to the note.

## How to place it

Use it where the page explains the loop, not in the three narrow columns: it is 16:9. Show the poster first. Play the video muted, inline, once, and only when the reader has not asked for reduced motion. It ends on the PDF, so looping jumps back to an empty terminal.

```html
<video src="…/launch-note-loop-en.mp4" poster="…/launch-note-loop-en-poster.png"
       muted playsinline preload="none" width="1600" height="900"></video>
```

## Alt text

en: A terminal asks an agent for a launch note. MarsDawn opens it side by side. The reader moves the launch from Wednesday to Friday, the agent updates the other sections to match, and the note is exported as a PDF.

zh-Hant：在終端機請 agent 寫一份上線公告，MarsDawn 並排打開它。讀者把上線日從週三改成週五，agent 把其他段落改成一致，最後匯出成 PDF。

zh-Hans：在终端请 agent 写一份上线公告，MarsDawn 并排打开它。读者把上线日从周三改成周五，agent 把其他段落改成一致，最后导出为 PDF。

ja：ターミナルでエージェントにリリースノートを頼み、MarsDawn が左右に開く。読み手が公開日を水曜から金曜に直し、エージェントが他の節を合わせ、最後に PDF に書き出す。

The zh-Hans and ja lines are drafts and need a native reviewer. The video itself stays English on every page, and a WebVTT caption track can be added later if wanted.

## Re-making it

`rig/take.sh` records a take. Take the screen lock (`SCREEN.md`) yourself first; the script does not. It needs the paywall-off Release build, Terminal.app not running, and the display awake. The paths in it, and in `render.py` and `verify.py`, are the recording machine's. `rig/render.py` cuts it, and `rig/verify.py` checks the result.
