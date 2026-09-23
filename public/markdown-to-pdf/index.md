# Markdown to PDF on a Mac, from the command line.

The free `marsdawn` tool turns a Markdown file into a PDF with one command. Tables, math, Mermaid diagrams and highlighted code come out the way they read in the source, and it needs nothing else installed, not even the MarsDawn app.

## Install it

```
brew install redtear1115/tap/marsdawn
marsdawn --version
```

On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds. On an Intel Mac it builds from source instead, which takes a few minutes and needs Xcode 26 or later. It runs on macOS 15 or later, and `marsdawn --version` prints the version you got.

## Save a document

Paste this into a file named `plan.md`:

````
# Plan: faster exports

An agent wrote this plan. You review it, then turn it into a PDF.

## Steps

| Step | Owner | Status |
|------|-------|--------|
| Measure the slow pages | Agent | Done |
| Cache rendered diagrams | Agent | In review |

The target is $t < 2\,\text{s}$ for a 50-page document:

$$
t_{\text{total}} = \sum_{i=1}^{n} t_i
$$

```mermaid
graph LR
  Draft --> Review --> Ship
```

```swift
let pdf = try export("plan.md")
```
````

## Export it

```
marsdawn export plan.md
```

It writes `plan.pdf` next to the source and prints where it went:

```
Exported /Users/you/plan.pdf (1 page)
```

This is that page, captured from a real run of `marsdawn` 0.5.0:

![The exported PDF: the heading, a table of steps, an inline and a displayed formula, a Draft, Review, Ship diagram, and a highlighted line of Swift.](/assets/cli/plan-en.png)

## Choose a theme, paper size and file name

```
marsdawn export plan.md --theme classic --paper letter -o handout.pdf
```

- `--theme`: dawn, classic, modern or vivid, in the theme's light colors. Without it, `export` uses `$MARSDAWN_THEME`, then dawn.
- `--paper`: a4 or letter. The default is a4.
- `-o`: where to write the PDF, instead of next to the source.
- `--allow-remote-images`: load images from the web while rendering. They stay off unless you pass it.

## If it doesn't work

- `A full installation of Xcode.app 26.0 is required to compile this software.` Homebrew is building `marsdawn` from source, as it does on an Intel Mac. Install Xcode 26 or later from the App Store, then run the install again.
- `marsdawn: No such file: …` The path doesn't point at a file. Check the name, or run the command from the folder the file is in.
- `… already exists. Pass --force to replace it.` A PDF with that name is already there. Add `--force` to replace it, or `-o` to write it somewhere else.
- `Error: The value '…' is invalid for '--theme <theme>'.` The theme or paper size isn't one it knows. The themes are dawn, classic, modern and vivid; the paper is a4 or letter.

## Next

- Every option and the JSON it prints: [Command Line](/cli/).
- To have a coding agent do this for you: [the marsdawn agent skill](/cli/skill/).
- All four preview themes, and where PDF export is headed: [preview themes and PDF export](/themes/).
- Handing the PDF to someone who doesn't use Markdown: [sharing a PDF](/sharing-exported-pdfs/).

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
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [日本語](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
