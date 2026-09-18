# Command Line

The free `marsdawn` command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.

**marsdawn is free and distributed separately from the Mac App Store.** Install it with Homebrew, which builds it from source on your Mac. `export` works on its own; `open` needs the MarsDawn app.

Calling marsdawn from an AI agent or a script? See [marsdawn for agents](/cli/agents/) for the JSON output, its schemas and every exit code.

## Install

With [Homebrew](https://brew.sh):

```
brew tap redtear1115/tap && brew install marsdawn
```

Homebrew compiles marsdawn from source, which takes a few minutes. The tool runs on macOS 15 or later, and building it needs Xcode 26 or later (Swift 6.2).

Or build it from [the source](https://github.com/redtear1115/mars-dawn-kit) with Swift Package Manager:

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

Check which version you have with `marsdawn --version`.

## Commands

### marsdawn open

Opens one or more Markdown files in MarsDawn for review. Needs MarsDawn installed.

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
```

- `path:line`: asks MarsDawn to land on that line. A column after it, as in `notes.md:120:8`, is ignored. If a file with the whole name exists, the argument is that file.
- `--line <n>`: the same for a single file, and the way to ask for a line on a path that itself ends in a colon and digits. Needs exactly one file.
- Lines run from 1 to 999999999.
- MarsDawn 1.0 opens the file but doesn't jump to the line yet.
- `--json`: print a JSON result instead of text.

Lines were added in marsdawn 0.3.0.

### marsdawn export

Renders a Markdown file to a paginated PDF, with the same exporter MarsDawn's own PDF export uses. It doesn't need the MarsDawn app. Relative images resolve against the input file's folder.

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`: where to write the PDF. Defaults to the input path with a `.pdf` extension.
- `--theme <dawn|classic|modern|vivid>`: the preview theme's light palette. Defaults to `$MARSDAWN_THEME`, then `dawn`.
- `--paper <a4|letter>`: paper size. Defaults to `a4`.
- `--allow-remote-images`: load images from the web while rendering. Off by default.
- `--force`: replace the output file if it already exists.
- `--json`: print a JSON result instead of text.

## The $MARSDAWN_THEME variable

When `--theme` isn't passed, `export` reads the `$MARSDAWN_THEME` environment variable. Its value must be one of `dawn`, `classic`, `modern` or `vivid`; anything else falls back to `dawn`. The CLI doesn't read the app's own theme setting, because reading another app's container can trigger a macOS privacy prompt.

## Overwriting files

`export` refuses to replace an existing output file unless you pass `--force`.

## Exit codes

- `0`: success.
- `2`: input not found.
- `3`: MarsDawn is not installed (`open` only).
- `4`: output exists (pass `--force`).
- `5`: export failed.
- `64`: usage error, including a line out of range or `--line` with more than one file.

## --json output

On success, `marsdawn open --json` prints `ok`, `opened` (a list with each file's `path`, plus `line` when one was asked for) and `app` (the app path). `marsdawn export --json` prints `ok`, `output`, `pages`, `theme`, `paper` and `diagramErrors`. On failure, both print `ok`, `error` and `message`.

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): MarsDawn is a native Markdown editor for the Mac with live preview, Mermaid diagrams and PDF export.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your documents stay on your Mac.
- [Pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn costs USD 4.99, once. No subscription, no account, no paid tier.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export as PDF or print, with Mermaid diagrams, highlighted code and careful page breaks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): Native windows and tabs, autosave, version history, Quick Look, and a text editor that behaves like the rest of your Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。
