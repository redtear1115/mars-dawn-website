# How to open .md files on Mac.

Double-click it. If your Mac opens it in a text editor and you see `#` and `**` instead of headings and bold, the file is fine: a `.md` file is plain text, and that editor is showing the text as it is. Open it in an app that renders Markdown, such as MarsDawn, and make that app the default so every `.md` file opens there.

A `.md` file is plain text. The headings, bold words, tables and diagrams are written as marks: `#` for a heading, `**` around bold, pipes for a table, a `mermaid` code block for a diagram. Open it in a plain text editor and you read the marks. To read the page the way its author meant, something has to render it.

## Open a .md file on your Mac

1. **Double-click the file.** It opens in the app your Mac has set for `.md` files. With no Markdown app, that is often a plain text editor, which shows the marks instead of the page.
2. **Pick the app yourself.** Control-click the file and choose Open With, then the app. Or choose File ▸ Get Info (⌘I), pick an app under "Open with:", and click "Change All…" so every file of this type opens there. MarsDawn opens `.md`, `.markdown`, `.mdown`, `.mkd` and `.mkdn` files.
3. **Preview without opening it.** Select the file in Finder and press Space. With MarsDawn installed, Quick Look shows the rendered page, diagrams included.

## Read it in MarsDawn

MarsDawn is a Markdown editor for the Mac. It is free to download from the Mac App Store: try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account. It needs macOS 26 or later.

[Download MarsDawn free on the Mac App Store](https://apps.apple.com/app/id6812925073)

Open a `.md` file and read the rendered page next to the source:

- The preview updates as you type, and the two panes scroll together.
- [Mermaid](/mermaid-preview-mac/) flowcharts and sequence diagrams are drawn in the preview, and code blocks are highlighted.
- When you want to change something, the source is right there. MarsDawn is an editor, not only a viewer.

If an AI agent wrote the file, this is the loop MarsDawn is built for: the agent writes, you read it rendered, and it revises. See [the home page](/), and [marsdawn for agents](/cli/agents/) for letting an agent open files for you. For why that reading matters and how to review a plan, see [Reading what your agent hands back](/reading-agent-output/) and [Reviewing an agent plan in five minutes](/reviewing-agent-plans/).

## Without the app: turn it into a PDF

The free `marsdawn` command-line tool renders a Markdown file to a PDF, which any Mac can open. Tables, math, Mermaid diagrams and highlighted code come out rendered, and it needs nothing else installed, not even the MarsDawn app.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` writes `notes.pdf` next to the Markdown file, and `open` shows it in your PDF viewer. It needs macOS 15 or later. The walk-through, with a real exported page, is on [Markdown to PDF](/markdown-to-pdf/).

## Questions

### What is a .md file?

A `.md` file is a plain text file written in Markdown, a way of marking up text with simple characters: `#` for a heading, `**` around bold, a pipe for a table cell. The extensions `.markdown`, `.mdown`, `.mkd` and `.mkdn` mean the same thing. Developers use it for READMEs and docs, and AI agents often hand back their plans and reports as `.md` files.

### Why does my .md file open as plain text, with # and ** marks in it?

Because it is plain text, and a plain text editor shows it as it is. Nothing is wrong with the file. To see headings, bold, tables and diagrams, open it in an app that renders Markdown. In MarsDawn the rendered page sits next to the source.

### Why does it open with garbled characters?

Garbled characters usually mean the file was saved in a text encoding other than UTF-8, and the app that opened it guessed wrong. The fix is to save a UTF-8 copy. MarsDawn opens a plain text file that isn't UTF-8 read-only, names the encoding it read it as in a bar at the top of the window, and offers Save As UTF-8… there, or File ▸ Save As… (⌥⇧⌘S), to write a UTF-8 copy you can edit.

### Can I turn a .md file into a PDF?

Yes. In MarsDawn, choose File ▸ Export as PDF… (⌥⌘E) or File ▸ Print…; the pages are paginated, with diagrams drawn in and code highlighted, in the theme's light colors. Without the app, the free `marsdawn export` command-line tool makes the same PDF: `marsdawn export notes.md`. See [PDF export](/pdf/) and [Markdown to PDF](/markdown-to-pdf/).

### Can I open the .md files my AI agent wrote?

Yes, that is what MarsDawn is built for. Open the file and read the rendered page next to its source; when the agent revises it, open it again. An agent can also run `marsdawn open plan.md` to open the file in MarsDawn for you. See [Reading what your agent hands back](/reading-agent-output/).

## Next

- Every option of the command-line tool: [Command Line](/cli/).
- What MarsDawn doesn't do: [the list](/limits/).
- Reading Markdown in VS Code, a browser or Claude Desktop instead: [how they compare](/vs/markdown-preview-tools/).
- Diagrams in a Markdown file: [Mermaid preview on Mac](/mermaid-preview-mac/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review your agent's Markdown, JSON and YAML natively on Mac: live preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac editor for Markdown, JSON and YAML: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings and records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no editing on iPhone or iPad, no plugins, no accounts. Themes, but no custom CSS. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): MarsDawn's Quick Look renders Markdown in Finder when you press Space, with Mermaid, KaTeX and highlighted code. It keeps working after the trial ends.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MarsDawn compared: VS Code preview, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [Best Markdown viewer for Mac (2026)](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Themes](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Make a theme with your agent](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes for MarsDawn, each reviewed by the developer, filter them by scenario, and report a problem with one. Build your own in the browser.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [Roadmap](https://marsdawn.southern-light.dev/roadmap/index.md): What's in progress and what's next for MarsDawn on Mac, iPhone and iPad, by version. No dates, and unscheduled ideas are marked.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [日本語](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Français](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Español](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [한국어](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
