# Let your agent make the PDF.

This skill is one Markdown file. It teaches a coding agent to install `marsdawn`, check that it works, export a document to PDF and read the result, so the agent that wrote the Markdown can hand you the PDF as well.

## Install it in Claude Code

```
mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md
```

Claude Code loads it when a task calls for a PDF, and you can run it yourself as `/marsdawn`. It's [one short file](/cli/skill/SKILL.md), so read it before you install it.

Other agents can use the same file. It's plain Markdown, instructions and commands, so point yours at the URL or paste it in.

## What it teaches

- Install `marsdawn` with Homebrew if it's missing, then check it with `marsdawn --version` instead of assuming a version.
- Export with `marsdawn export … --json`, and read the result: where the PDF went, how many pages it has, and any Mermaid diagram that didn't render.
- Tell the failures apart by exit code: no such file, a PDF already there, a failed export, a bad option.
- Use `open` only when the MarsDawn app is installed, and never to make a PDF.

## What it doesn't do

- It doesn't give itself permission to run anything. Your agent still asks before it installs `marsdawn` or runs it, as it would for any other command.
- It doesn't send your documents anywhere. `marsdawn` renders on your Mac, and it leaves out images from the web unless you pass `--allow-remote-images`.

The whole contract, every field and every code, is in [marsdawn for agents](/cli/agents/).

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
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
