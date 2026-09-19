# marsdawn for agents

A reference for AI agents and scripts that call the `marsdawn` command-line tool. Every example on this page was run against the tool built from the current source.

**To turn a Markdown file into a PDF, run `marsdawn export notes.md --json` and read one JSON object from stdout.** Mermaid diagrams and highlighted code are rendered the same way as in the MarsDawn app. `export` doesn't need the app; `open` does.

## What it does

- `export` renders one Markdown file to a paginated PDF with the same exporter as the MarsDawn app. No window opens.
- `open` opens one or more Markdown files in the MarsDawn app, so a person can review them, and can name the line each file should land on.

## What it does not do

- It doesn't read Markdown from stdin. Pass a file path.
- It doesn't write the PDF to stdout. The PDF always goes to a file; stdout carries only the result.
- It doesn't replace an existing file unless you pass `--force`.
- It doesn't load images from the web unless you pass `--allow-remote-images`, and then only over https.
- `open` doesn't work without the MarsDawn app installed; it exits with code 3. `export` doesn't need the app.
- MarsDawn 1.0 doesn't jump to the line `open` names yet. It opens the file at the top.
- It runs on macOS only.

## export

```
marsdawn export notes.md --json
```

Writes `notes.pdf` next to `notes.md`. Options:

- `-o, --output <path>`: where to write the PDF. Defaults to the input path with a `.pdf` extension.
- `--theme <dawn|classic|modern|vivid>`: the theme's light palette. Defaults to `$MARSDAWN_THEME`, then `dawn`.
- `--paper <a4|letter>`: paper size. Defaults to `a4`.
- `--allow-remote-images`: load https images from the web while rendering.
- `--force`: replace the output file if it exists.
- `--json`: print one JSON object on stdout instead of text.

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

Success, exit code 0:

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`: absolute path of the PDF that was written.
- `pages`: number of pages.
- `theme` and `paper`: the values used.
- `diagramErrors`: one message per Mermaid diagram that failed to render. The PDF is still written.

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
```

- `path:line` names the line to land on. A column after it, as in `notes.md:120:8`, is ignored. An argument that names a file which exists is always that whole filename, so a file called `weird:12` opens as itself.
- `--line <n>` names the line for a single file, including a path that itself ends in a colon and digits. It needs exactly one file.
- Lines run from 1 to 999999999. Anything else is a usage error.
- Lines were added in marsdawn 0.3.0. MarsDawn 1.0 opens the file but doesn't jump to the line yet.

Success, exit code 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`: one object per file, in the order given. `path` is the file's absolute path; `line` appears only when a line was asked for.
- `app`: path of the MarsDawn app that opened them.

marsdawn 0.2.x printed `opened` as a list of path strings. Check `marsdawn --version` if you need to handle both.

## Failures

With `--json`, a failure prints one JSON object on stdout and exits with its code:

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: the input doesn't exist, is a folder, or isn't UTF-8 text.
- `3`, `app_not_installed`: MarsDawn isn't installed. Only `open` returns this.
- `4`, `output_exists`: the output file exists. Pass `--force`.
- `5`, `export_failed`: the export itself failed.
- `64`: usage error, such as an unknown option, an invalid value, a line out of range or `--line` with more than one file. This one is printed as text on stderr, even with `--json`.

## JSON Schemas

JSON Schema (draft 2020-12) for every `--json` result:

- [export.v1.json](/schemas/cli/export.v1.json): export success
- [open.v2.json](/schemas/cli/open.v2.json): open success, marsdawn 0.3.0 and later
- [error.v1.json](/schemas/cli/error.v1.json): failure, both commands
- [open.v1.json](/schemas/cli/open.v1.json): open success, marsdawn 0.2.x, where `opened` was a list of paths

## Environment variables

- `MARSDAWN_THEME`: the theme `export` uses when `--theme` isn't passed. An unknown value falls back to `dawn` without an error.

## Requirements

- The tool runs on macOS 15 or later. On Apple silicon, Homebrew installs a prebuilt bottle and nothing else is needed. Building it yourself, on an Intel Mac or from the source, needs Swift 6.2 or later, which comes with Xcode 26 or later.
- The MarsDawn app needs macOS 26 or later.

## Install

With Homebrew. On Apple silicon it pours a prebuilt bottle in seconds, with no Xcode needed. On an Intel Mac it compiles marsdawn from source, which takes a few minutes and needs Xcode 26 or later.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

Or build it from [the source](https://github.com/redtear1115/mars-dawn-kit). The first build fetches dependencies and compiles, which also takes a few minutes.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` prints the version number, such as `0.3.0`, and exits with code 0.

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
