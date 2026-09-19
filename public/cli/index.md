# Command Line

The free `marsdawn` command-line tool: export Markdown to PDF from a shell or an LLM agent, and, with the MarsDawn app installed, open files in it.

**marsdawn is free and distributed separately from the Mac App Store.** Install it with Homebrew: on an Apple silicon Mac it arrives ready to run. `export` works on its own; `open` needs the MarsDawn app.

Calling marsdawn from an AI agent or a script? See [marsdawn for agents](/cli/agents/) for the JSON output, its schemas and every exit code, or [the MCP server](/cli/mcp/) if your agent calls tools over MCP instead.

## Install

With [Homebrew](https://brew.sh):

```
brew tap redtear1115/tap && brew install marsdawn
```

Using a coding agent? [Add the marsdawn skill](/cli/skill/): one file that teaches it to open what it wrote in MarsDawn for your review, and to export PDFs.

On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds, with nothing else to install. On an Intel Mac it builds marsdawn from source instead, which takes a few minutes and needs Xcode 26 or later (Swift 6.2). The tool runs on macOS 15 or later.

Or build it from [the source](https://github.com/redtear1115/mars-dawn-kit) with Swift Package Manager:

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

Check which version you have with `marsdawn --version`.

## Commands

### marsdawn open

Opens one or more Markdown files in the MarsDawn app for review. It needs the app installed: without it, `marsdawn open` exits with code 3 and says MarsDawn isn't installed. `export` doesn't need the app.

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .
```

- `path:line`: asks MarsDawn to land on that line. A column after it, as in `notes.md:120:8`, is ignored. If a file with the whole name exists, the argument is that file.
- `--line <n>`: the same for a single file, and the way to ask for a line on a path that itself ends in a colon and digits. Needs exactly one file.
- Lines run from 1 to 999999999.
- A folder argument opens in the window's sidebar instead of as a document: `marsdawn open .` shows the current folder. `--folder <path>` does the same alongside files. A window's sidebar shows one folder, so naming two is a usage error.
- `--background`: open without bringing MarsDawn to the front.
- MarsDawn 1.0 opens the file but doesn't jump to the line yet.
- `--json`: print a JSON result instead of text.

Lines were added in marsdawn 0.3.0, and folders and `--background` in 0.5.1.

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

| Code | Means | What to do |
|---|---|---|
| `0` | success. | With `--json`, read the one JSON line on stdout |
| `2` | input not found. | Check the path and the file name |
| `3` | MarsDawn is not installed (`open` only). | Install the app, or use `export`, which doesn't need it |
| `4` | output exists (pass `--force`). | Pass `--force` to replace it, or `-o` to write elsewhere |
| `5` | export failed. | Read `message` in the JSON result |
| `64` | usage error, including a line out of range, `--line` with more than one file or with a folder, or more than one folder. | Fix the option or value; this error is text on stderr, even with `--json` |

## --json output

On success, `marsdawn open --json` prints `ok`, `opened` (a list with each file's `path`, plus `line` when one was asked for), `app` (the app path) and, when a folder was given, `folder`. `marsdawn export --json` prints `ok`, `output`, `pages`, `theme`, `paper` and `diagramErrors`. On failure, both print `ok`, `error` and `message`.

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
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
