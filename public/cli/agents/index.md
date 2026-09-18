# marsdawn for agents

A reference for AI agents and scripts that call the `marsdawn` command-line tool. Every example on this page was run against the tool built from the current source.

**To turn a Markdown file into a PDF, run `marsdawn export notes.md --json` and read one JSON object from stdout.** Mermaid diagrams and highlighted code are rendered the same way as in the MarsDawn app. The MarsDawn app must be installed.

## What it does

- `export` renders one Markdown file to a paginated PDF with the same exporter as the MarsDawn app. No window opens.
- `open` opens one or more Markdown files in the MarsDawn app, so a person can review them.

## What it does not do

- It doesn't read Markdown from stdin. Pass a file path.
- It doesn't write the PDF to stdout. The PDF always goes to a file; stdout carries only the result.
- It doesn't replace an existing file unless you pass `--force`.
- It doesn't load images from the web unless you pass `--allow-remote-images`, and then only over https.
- It doesn't work without the MarsDawn app installed. Both commands exit with code 3.
- It has no `--version` option; passing one is a usage error.
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
```

Success, exit code 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":["/path/to/notes.md"]}
```

- `opened`: absolute paths of the files that were opened.
- `app`: path of the MarsDawn app that opened them.

## Failures

With `--json`, a failure prints one JSON object on stdout and exits with its code:

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: the input doesn't exist, is a folder, or isn't UTF-8 text.
- `3`, `app_not_installed`: MarsDawn isn't installed.
- `4`, `output_exists`: the output file exists. Pass `--force`.
- `5`, `export_failed`: the export itself failed.
- `64`: usage error, such as an unknown option or an invalid value. This one is printed as text on stderr, even with `--json`.

## JSON Schemas

JSON Schema (draft 2020-12) for every `--json` result:

- [export.v1.json](/schemas/cli/export.v1.json): export success
- [open.v1.json](/schemas/cli/open.v1.json): open success
- [error.v1.json](/schemas/cli/error.v1.json): failure, both commands

## Environment variables

- `MARSDAWN_THEME`: the theme `export` uses when `--theme` isn't passed. An unknown value falls back to `dawn` without an error.

## Requirements

- The tool runs on macOS 15 or later. Building it needs Swift 6.2 or later, which comes with Xcode 26 or later.
- The MarsDawn app needs macOS 26 or later.

## Install

Build it from [the source](https://github.com/redtear1115/mars-dawn-kit). The first build fetches dependencies and compiles, which takes a few minutes.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): MarsDawn is a native Markdown editor for the Mac with live preview, Mermaid diagrams and PDF export.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
