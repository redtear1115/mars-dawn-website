Frontier tools for builders

# Claim the map. Read the dawn.

Markdown for humans who steer agentic work.

MarsDawn is a native macOS Markdown editor with live split preview, Mermaid diagrams, KaTeX math, Quick Look and PDF export, free to try for 14 days and USD 4.99 once to unlock.

The page shows a working MarsDawn window over part of the app's Welcome guide. Its palette menu picks an appearance (System, Light, Dark) and a preview theme for light and for dark from four (Dawn, Classic, Modern, Vivid), and its toolbar one of three layouts (Source, Split, Preview).

## Read what your agent wrote.

1. **The agent writes.** Your coding agent or writing assistant drafts the Markdown: a README, a spec, a set of notes.
2. **You review in MarsDawn.** Open the file and read it rendered, with Mermaid diagrams and highlighted code, next to the source.
3. **The agent revises.** Ask for changes. Open the revised file and read it the same way.

[How to review what your agent hands back](/reading-agent-output/).

## Do this now

The free `marsdawn` command-line tool is ready today. Install it with Homebrew:

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` turns a Markdown file into a PDF, rendered like MarsDawn's preview. It doesn't need the app.
- `marsdawn open` opens files in the MarsDawn app for you to review.
- `--json` gives scripts and agents results they can parse.

[Command Line](/cli/) · [marsdawn for agents](/cli/agents/) · [Agent skill](/cli/skill/) · [MCP server](/cli/mcp/)

## What to expect from MarsDawn

- [A Mac app](/native/): Native windows, tabs, autosave, Quick Look.
- [Your writing stays on your Mac](/yours/): No account, no sync, no cloud.
- [Try free, pay once](/pay-once/): Free for 14 days, then USD 4.99 once. No subscription.

Know before you buy. [What MarsDawn doesn't do](/limits/)

## Questions and answers

### What is MarsDawn?

MarsDawn is a native Markdown editor for the Mac. It shows a live preview next to the source, draws Mermaid diagrams and KaTeX math, previews Markdown files in Finder with Quick Look, and exports PDF.

### Is MarsDawn a subscription?

No. MarsDawn is a free download with a 14-day trial of every feature. After that, a single in-app purchase of USD 4.99 unlocks it for good. Nothing renews, and there is no account.

### Does MarsDawn work on iPhone or iPad?

No. MarsDawn is a Mac app and needs macOS 26 or later. There is no iPhone or iPad app.

### Can Claude Code open files in MarsDawn?

Yes. The free marsdawn command-line tool has an open command that opens a Markdown file in MarsDawn, so Claude Code, or any agent that can run a shell command, can call it. An opt-in Claude Code hook can open each Markdown file Claude writes or edits.

### Does Quick Look still work after the trial ends?

Yes. Quick Look in Finder keeps showing your Markdown files whether or not the trial is running. After the trial ends and until you unlock, documents open in MarsDawn with their content covered.

## The app, as it is

### [A Mac app](/native/)

![MarsDawn in split view: the Markdown source on the left, the rendered page on the right.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

In this screenshot:

1. A native Mac window.
2. The Mac's text editor, with Markdown highlighting.
3. ⌘1 source, ⌘2 split, ⌘3 preview.
4. The page updates as you type.

### [PDF export](/pdf/)

![A PDF exported from MarsDawn, open in its PDF viewer with page thumbnails.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

In this screenshot:

1. Mermaid diagrams, drawn into the PDF.
2. Code keeps its highlighting.

## More

- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, on the Mac App Store.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): Press Space on a Markdown file in Finder to read it rendered, with Mermaid diagrams, KaTeX math and highlighted code. MarsDawn's Quick Look is not locked by the trial.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. Build your own theme in the browser, and browse the community gallery.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes the community submitted for MarsDawn, filter them by scenario, and report a problem with one. Build your own in the browser, no install, no git.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): Mac 原生 Markdown 編輯器：即時分割預覽、Mermaid、KaTeX、快速查看、PDF 輸出。免費試用，只需買一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): Mac 原生 Markdown 编辑器：实时分栏预览、Mermaid、KaTeX、快速查看、PDF 导出。免费试用，只需买一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): Mac 向けネイティブ Markdown エディタ。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Éditeur Markdown natif pour Mac : aperçu en direct à côté de la source, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Editor de Markdown nativo para Mac: vista previa en vivo junto al código, Mermaid, KaTeX, Vista rápida, exportación a PDF. Pruébalo gratis, 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
