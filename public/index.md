Frontier tools for builders

# Claim the map. Read the dawn.

Markdown for humans who steer agentic work.

MarsDawn is a native Mac app for reading and reviewing Markdown, with live split preview, Mermaid diagrams, KaTeX math, Quick Look and PDF export, free to try for 14 days and USD 4.99 once to unlock.

The page shows a working MarsDawn window over part of the app's Welcome guide. Its palette menu picks an appearance (System, Light, Dark) and a preview theme for light and for dark from four (Dawn, Classic, Modern, Vivid), and its toolbar one of three layouts (Source, Split, Preview).

## Read what your agent wrote.

1. **The agent writes.** Your coding agent or writing assistant drafts the Markdown: a README, a spec, a set of notes.
2. **You review in MarsDawn.** Open the file and read it rendered, with [Mermaid diagrams](/mermaid-preview-mac/) and highlighted code, next to the source.
3. **The agent revises.** Ask for changes. Open the revised file and read it the same way.

[How to review what your agent hands back](/reading-agent-output/) · [How to open a .md file on a Mac](/view-markdown-on-mac/)

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
- [Features](/features/): Everything MarsDawn does, on one page.

Know before you buy. [What MarsDawn doesn't do](/limits/)

Choosing between MarsDawn, VS Code's preview, Obsidian, QLMarkdown and LynxOffice? The comparison lists what each vendor states, what MarsDawn lacks, and when you don't need it. [Compare](/vs/)

## Your documents stay on your Mac

On your Mac. Reading, editing, rendering, PDF export and the marsdawn command line all run here, offline; the app never uploads your documents.

More: [Privacy Policy](/privacy/#what-stays-on-your-mac)

Off the network by default. Web images load only when you click Load Images or turn on Load remote images automatically in Settings, and an HTML document opens static, with its code not run.

More: [Privacy Policy](/privacy/#when-marsdawn-uses-the-internet)

Leaves only when you choose. Copy for AI puts text on your clipboard for you to paste; a theme download, a document you run with View › Run This Document, and the agent you let read a file go out only on your say.

More: [Privacy Policy](/privacy/#when-marsdawn-uses-the-internet)

## Questions and answers

### What is MarsDawn?

MarsDawn is a native Mac app for reading and reviewing the Markdown your agent wrote, with the source beside a live preview. It draws Mermaid and KaTeX, previews .md files in Quick Look and exports PDF, and you can edit the source too.

### Is MarsDawn a subscription?

No. MarsDawn is a free download with a 14-day trial of every feature. After that, a single in-app purchase of USD 4.99 unlocks it for good. Nothing renews, and there is no account.

### Does MarsDawn work on iPhone or iPad?

No. MarsDawn is a Mac app and needs macOS 26 or later. There is no iPhone or iPad app.

### Can Claude Code open files in MarsDawn?

Yes. The free marsdawn command-line tool has an open command that opens a Markdown file in MarsDawn, so Claude Code, or any agent that can run a shell command, can call it. An opt-in Claude Code hook can open each Markdown file Claude writes or edits.

### Does MarsDawn upload my documents?

No. The app never uploads your documents, collects no data about you and has no account; your documents and settings stay on your Mac. If a document refers to the web and you load that content, your Mac fetches it from the servers that host it, and MarsDawn's developer receives none of it.

More: [Privacy Policy](/privacy/#when-marsdawn-uses-the-internet)

### With MCP or the skill, who can see my files?

MarsDawn itself sends nothing. The skill is a text file of instructions, and the marsdawn CLI and the MCP server run on your Mac; the MCP server works only in folders you allow. The one reading your files is your agent, and what it and its model provider do with them is that agent's policy, which MarsDawn neither controls nor describes.

### Is it safe to open HTML someone sent me?

By default it opens static: its code doesn't run and nothing loads from the web. If you choose View › Run This Document, that document runs, and it can send data over the network and read images, stylesheets, fonts and media in its folder. The choice is never remembered, so it opens static again next time.

More: [Privacy Policy](/privacy/#when-marsdawn-uses-the-internet)

### Is the site's analytics cookie related to the app?

No. The app and this website are separate: the app collects nothing, and a visit can be recorded only on marsdawn.southern-light.dev. The site's Google Analytics starts denied and sets cookies only after you choose Accept; Cookie settings in the footer changes that. The app's requests for theme files under /themes/ are skipped.

More: [Privacy Policy](/privacy/#the-website)

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

- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes, more in the gallery. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [How to open .md files on Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): MarsDawn's Quick Look renders Markdown in Finder when you press Space, with Mermaid, KaTeX and highlighted code. It keeps working after the trial ends.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MarsDawn compared: VS Code preview, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. Build your own theme in the browser, and browse the community gallery.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Make a theme with your agent](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 讀懂、檢查 agent 寫的 Markdown 的 Mac 原生 app：分割即時預覽、Mermaid、KaTeX、快速查看、PDF 輸出。可免費試用，之後一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown を読んで確かめる Mac ネイティブアプリ。分割ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、解除は一度だけ USD 4.99。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
