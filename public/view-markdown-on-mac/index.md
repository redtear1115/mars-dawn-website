# How to view a Markdown file on a Mac.

A `.md` file is plain text. The headings, bold words, tables and diagrams are written as marks: `#` for a heading, `**` around bold, pipes for a table, a `mermaid` code block for a diagram. Open it in a plain text editor and you read the marks. To read the page the way its author meant, something has to render it.

## Today, for free: turn it into a PDF

The free `marsdawn` command-line tool renders a Markdown file to a PDF, which any Mac can open. Tables, math, Mermaid diagrams and highlighted code come out rendered, and it needs nothing else installed, not even the MarsDawn app.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` writes `notes.pdf` next to the Markdown file, and `open` shows it in your PDF viewer. It needs macOS 15 or later. The walk-through, with a real exported page, is on [Markdown to PDF](/markdown-to-pdf/).

## Coming soon: read it in MarsDawn

MarsDawn is a Markdown editor for the Mac, coming soon to the Mac App Store. Open a `.md` file and read the rendered page next to the source:

- The preview updates as you type, and the two panes scroll together.
- Mermaid flowcharts and sequence diagrams are drawn in the preview, and code blocks are highlighted.
- In Finder, press Space on a Markdown file for a Quick Look preview, diagrams included.
- When you want to change something, the source is right there. MarsDawn is an editor, not only a viewer.

If an AI agent wrote the file, this is the loop MarsDawn is built for: the agent writes, you read it rendered, and it revises. See [the home page](/), and [marsdawn for agents](/cli/agents/) for letting an agent open files for you.

## Next

- Every option of the command-line tool: [Command Line](/cli/).
- What MarsDawn doesn't do: [the list](/limits/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): MarsDawn: a native Mac Markdown editor built for the AI workflow. An agent writes the Markdown, you review it with live preview, and it revises.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your documents stay on your Mac.
- [Pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn costs USD 4.99, once. No subscription, no account, no paid tier.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export as PDF or print, with Mermaid diagrams, highlighted code and careful page breaks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): Native windows and tabs, autosave, version history, Quick Look, and a text editor that behaves like the rest of your Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Turn a Markdown file into a PDF with the free marsdawn command-line tool. Install it with Homebrew, run one command, and get tables, math, Mermaid diagrams and highlighted code on the page.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool: export Markdown to PDF from a shell or an LLM agent, and, with the MarsDawn app installed, open files in it.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
