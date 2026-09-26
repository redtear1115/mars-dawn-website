# marsdawn for agents

A reference for AI agents and scripts that call the `marsdawn` command-line tool. Every example on this page was run against the tool built from the current source.

**To turn a Markdown file into a PDF, run `marsdawn export notes.md --json` and read one JSON object from stdout.** Mermaid diagrams and highlighted code are rendered the same way as in the MarsDawn app. `export` doesn't need the app; `open` does.

## What it does

- `export` renders one Markdown file to a paginated PDF with the same exporter as the MarsDawn app. No window opens.
- `open` opens one or more Markdown files in the MarsDawn app, so a person can review them, and can name the line each file should land on.
- `open --folder <path>` also asks MarsDawn to show a folder in the window's sidebar, alongside any files, and, from an app that reports back, waits to say what happened to it.

## What it does not do

- It doesn't read Markdown from stdin. Pass a file path.
- It doesn't write the PDF to stdout. The PDF always goes to a file; stdout carries only the result.
- It doesn't replace an existing file unless you pass `--force`.
- It doesn't load images from the web unless you pass `--allow-remote-images`, and then only over https.
- `open` doesn't work without the MarsDawn app installed; it exits with code 3. `export` doesn't need the app.
- MarsDawn 1.0 opens the file at the line `open` names.
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
- Lines were added in marsdawn 0.3.0. MarsDawn 1.0 opens the file at that line.

Success, exit code 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`: one object per file, in the order given. `path` is the file's absolute path; `line` appears only when a line was asked for.
- `app`: path of the MarsDawn app that opened them.

marsdawn 0.2.x printed `opened` as a list of path strings. Check `marsdawn --version` if you need to handle both.

## Showing a folder

```
marsdawn open . --folder . --json
```

`--folder <path>` (or a folder passed as one of the file arguments, as above) asks MarsDawn to show that folder in the window's sidebar too, alongside any files. A window's sidebar shows one folder, so naming two is a usage error. An app that can't show a folder refuses before opening anything, exit code 6 (`app_cannot_open_folders`); files on their own still open as usual.

Success, exit code 0:

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/notes","requested":true,"status":"attached"},"ok":true,"opened":[]}
```

- `folder.path`: absolute path of the folder.
- `folder.requested`: always `true` — `open` handed the folder to MarsDawn and returned.
- `folder.status`: present only from a MarsDawn that reports back (marsdawn 0.5.3 and later, paired with an app that declares it) and a `--wait` above 0. One of `attached`, `needsUser` (see `waitingFor`), `declined`, `failed`, `attachedDifferentFolder`, `full`, `unavailable`, or `unknown` (the app didn't answer before `--wait` ran out — try again with a longer `--wait`, or treat it as "don't know"). `needsUser` means the user has to act: don't retry, just tell them.
- `folder.waitingFor`: present only alongside `status: "needsUser"`: `confirmation` or `folderChoice`.
- `--wait <seconds>`: how long to wait for the app's report, 0–30, default 2. `--wait 0`, or an older MarsDawn that doesn't report back, skips waiting: `folder` only ever carries `path` and `requested: true`, the same as before this existed.
- A `--wait` value ArgumentParser can parse as a number but outside 0–30 is a usage error, exit 64, with `error: wait_out_of_range` in `--json`. Write a negative value as `--wait=-1`, not `--wait -1`: with a space, ArgumentParser reads it as another flag and gives its own plain usage error instead (still exit 64, but no `wait_out_of_range`).

## Failures

With `--json`, a failure prints one JSON object on stdout and exits with its code:

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: the input doesn't exist, is a folder, or isn't UTF-8 text.
- `3`, `app_not_installed`: MarsDawn isn't installed. Only `open` returns this.
- `4`, `output_exists`: the output file exists. Pass `--force`.
- `5`, `export_failed`: the export itself failed.
- `6`, `app_cannot_open_folders`: this MarsDawn can't show a folder, so nothing was opened. Only `open` returns this.
- `64`: usage error, such as an unknown option, an invalid value, a line out of range, `--line` with more than one file, or (only for `--folder`) `--wait` out of range. This one is printed as text on stderr, even with `--json` — except `wait_out_of_range`, which does print as JSON.

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

## Next

- A one-file skill for agents that read instructions instead of a shell: [the marsdawn skill](/cli/skill/).
- An MCP server that wraps this same `export`: [marsdawn-mcp](/cli/mcp/).
- Why this JSON result stays cheap for an agent's own context: [token-efficient review](/token-efficient-review/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. Coming soon to the Mac App Store.
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
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Editor's reading notes](https://marsdawn.southern-light.dev/reading-notes/index.md): Six short notes on what the people building AI agents actually argue — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain and Andrew Ng — and what each one means for the person who has to read what such an agent hands back.
- [Reading notes: Anthropic](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [Reading notes: Chip Huyen](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [Reading notes: Lilian Weng](https://marsdawn.southern-light.dev/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng's widely cited 2023 survey describes an LLM agent as a brain plus planning, memory and tool use. What each part tends to leave behind for you to read, and the limitation she names in plans that don't adjust to surprises.
- [Reading notes: Harrison Chase](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [Reading notes: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [Reading notes: Andrew Ng](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
