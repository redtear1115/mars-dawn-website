# Where an agent's Markdown gets a careful read.

An AI agent writes the Markdown. You review it in MarsDawn, source and rendered page side by side, then send it back for changes.

Coming soon to the Mac App Store · Free 14-day trial, then USD 4.99 once · macOS 26 or later · [The free marsdawn CLI works today](/cli/)

![MarsDawn in split view: the Markdown source on the left, the rendered page on the right.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

## The loop

1. **The agent writes.** Claude Code, Cursor or your writing assistant drafts the Markdown: a README, a spec, a design note.
2. **You review in MarsDawn.** The agent runs `marsdawn open SPEC.md`, or you open the file yourself. Diagrams, math and code render next to the source.
3. **The agent revises.** Tell it what to change, then read the new version the same way.

## Try the agent side today

The [marsdawn CLI](/cli/) is free, and exporting needs no app. Install it, and your agent can turn its Markdown into a PDF and learn, from one line of JSON, whether every Mermaid diagram rendered.

```
brew tap redtear1115/tap
brew install marsdawn
marsdawn export SPEC.md --json
```

It answers with one line:

```
{"diagramErrors":[],"ok":true,"output":"/path/to/SPEC.pdf","pages":3,"paper":"a4","theme":"dawn"}
```

Every flag, exit code and JSON schema is in [marsdawn for agents](/cli/agents/).

**Read what your agent wrote.** MarsDawn is coming soon to the Mac App Store.

## More

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
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
