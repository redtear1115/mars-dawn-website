# Best Markdown viewer for Mac (2026)

The best Markdown viewer depends on what you read. If it is notes you write yourself, an all-in-one editor is enough. If it is long documents with diagrams and math, or files an AI agent keeps rewriting, check how each app handles live reload, Mermaid and PDF. The apps below are in alphabetical order, and each one gets who it suits, one honest drawback and its price.

## MacDown 3000

The original MacDown is no longer maintained. MacDown 3000 is the community continuation: free and open source (MIT), native, with Mermaid, MathJax, PDF export, live reload and Quick Look.

- Suits: people who want a free native split view.
- Drawback: no documented way to open a file at a line from the command line.
- Price: free.

## Marked

Marked 3 is a previewer for Markdown you write in another app. It reloads whenever the file changes, has MathJax and KaTeX, and prints paginated PDFs with page numbers. Marked 2 is still sold.

- Suits: writers who keep their own editor and want a polished preview and print.
- Drawback: Quick Look is a separate app, Marked QL (USD 9.99).
- Price: Marked 3 is a free download, then USD 2.99/month, USD 29.99/year or USD 69.99 lifetime. Marked 2 is USD 14.99 direct or USD 13.99 on the Mac App Store.

## MarkEdit

A light, free native editor (CodeMirror in a web view) with Quick Look.

- Suits: people who want a fast plain-text editor that feels at home on the Mac.
- Drawback: Mermaid and math need the official extensions, and PDF export needs Pandoc.
- Price: free.

## MarsDawn

A native Mac app that shows the source and a live preview side by side, with Mermaid and KaTeX built in. When an agent saves the file, the open window takes the change as one undoable "Update from Disk". `marsdawn open notes.md:120` opens a file at a line, and there is a skill and an MCP server for agents. Quick Look works with or without the trial. Copy for AI and Copy Reference hand text to an agent. Nothing leaves your Mac unless you choose.

- Suits: people reviewing Markdown that AI agents write.
- Drawback: the PDF export has no page numbers.
- Price: free download with a 14-day trial, then USD 4.99 once. No account. Mac App Store only.

## Obsidian

A notes app built around a vault of linked Markdown files, with Mermaid, MathJax, PDF export and live reload.

- Suits: people building a knowledge base of their own notes.
- Drawback: it is an Electron app, and it works best with files inside a vault.
- Price: free. Sync and Publish are paid.

## QLMarkdown

A Quick Look extension: select a .md file in Finder and press Space. Mermaid and MathJax are opt-in.

- Suits: people who only want to glance at files in Finder.
- Drawback: it is not an app for reading or editing, and has no documented PDF export.
- Price: free (GPL-3.0).

## Typora

A seamless editor where the preview is the document, with Mermaid, MathJax and PDF export with page numbers in the header or footer.

- Suits: people who prefer to write in a WYSIWYG-style view.
- Drawback: no separate source and preview side by side.
- Price: USD 14.99 once, for up to 3 devices.

## VS Code preview

The built-in Markdown preview, with Mermaid built in since 1.121 and KaTeX. `code -g file:line` opens a file at a line.

- Suits: developers who already live in VS Code.
- Drawback: it is an Electron app, and has no built-in PDF export.
- Price: free.

## Comparison

| App | Price | Mermaid | Math | PDF | Live reload | CLI at line | Quick Look | Build |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | Free | Yes | MathJax | Yes | Yes | Not documented | Yes | Native |
| Marked 3 | From USD 2.99/mo | Yes | MathJax, KaTeX | Yes, page numbers | Yes | Not documented | Marked QL, USD 9.99 | Native |
| MarkEdit | Free | Extension | KaTeX (extension) | Pandoc | Not documented | Not documented | Yes | Native (web view) |
| MarsDawn | USD 4.99 once | Yes | KaTeX | Yes, no page numbers | Yes, undoable | Yes | Yes | Native |
| Obsidian | Free | Yes | MathJax | Yes | Yes | Not documented | Not documented | Electron |
| QLMarkdown | Free | Opt-in | MathJax (opt-in) | Not documented | n/a | n/a | It is one | Native |
| Typora | USD 14.99 once | Yes | MathJax | Yes, page numbers | Not documented | Not documented | Not documented | Native |
| VS Code | Free | Yes (1.121+) | KaTeX | No | Not documented | Yes | Not documented | Electron |

## Who MarsDawn is not for

- You need page numbers in your PDFs. Typora and Marked 3 add them, MarsDawn does not.
- You keep a linked knowledge base of your own notes. Obsidian is built for that.
- You never leave VS Code. Its built-in preview is free, and VS Code is adding an experimental Markdown view to its Agents window.
- You only want a preview in Finder. QLMarkdown is free.

## FAQ

### Which free Markdown viewers for Mac have Mermaid?

MacDown 3000, Obsidian and VS Code (1.121 and later) have it built in. QLMarkdown has it as an option, and MarkEdit through an extension.

### Which ones export PDF with page numbers?

Typora and Marked 3. MarsDawn exports PDF without page numbers.

### Which ones open a file at a specific line from the command line?

MarsDawn (`marsdawn open notes.md:120`) and VS Code (`code -g file:line`). For the others it is not documented.

### Which ones are native Mac apps rather than Electron?

All of them except Obsidian and VS Code. MarkEdit is native with its editor in a web view.

[Download and try it free](https://apps.apple.com/app/id6812925073)

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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
