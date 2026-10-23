# MarsDawn and other ways to read Markdown on a Mac

For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on [Support](/support/).

|  | MarsDawn | VS Code preview | Obsidian | QLMarkdown | LynxOffice |
|---|---|---|---|---|---|
| Open a local .md | Yes; edits the file in place [app 1.1.1] | Yes; preview with ⇧⌘V [[8](#v8)] | Not stated by the vendor [[21](#v21)] | Preview only: "for viewing Markdown files" [[22](#v22)] | "Markdown opens rendered and saves back verbatim." [[3](#v3)] |
| Mermaid | Built in [[1](#v1)] | Built in [[8](#v8)] | Built in, note syntax [[16](#v16)] | Built in, `mermaid` fences [[22](#v22)] | "diagram blocks are not rendered" [[3](#v3)] |
| Math | KaTeX, `$…$` and `$$…$$` [[kit](#kit)] | KaTeX [[8](#v8)] | MathJax [[16](#v16)] | MathJax [[22](#v22)] | "Footnotes, math, and diagram blocks are not rendered." [[3](#v3)] |
| Review an agent's plan / jump to a line | `marsdawn open file:line`; updates from disk; Copy Reference [/cli/, /features/] | Markdown diff preview, changed lines highlighted [[8](#v8)]; `code -g file:line` [[14](#v14)] | No line parameter in `obsidian://open` [[20](#v20)] | Not stated by the vendor | CLI and MCP server; no line jump stated [[4](#v4), [5](#v5)] |
| PDF: page breaks, page numbers | Breaks avoid splitting short code blocks [/pdf/]; no page numbers [check] | Not stated by the vendor [[8](#v8)] | Paper size, margins; breaks and numbers not stated [[17](#v17)] | Not stated by the vendor [[22](#v22)] | PDF "including tables"; breaks and numbers not stated [[3](#v3)] |
| Price | Free download; Unlock USD 4.99 once; 14-day trial [[1](#v1)] | Not stated by the vendor [[12](#v12), [13](#v13)] | Personal: "Free without limits"; commercial licence optional [[15](#v15)] | Free, GPL-3.0 [[22](#v22)] | "Free while in early release." [[2](#v2)] |
| System requirements | macOS 26.0 or later [[1](#v1)] | "the latest release and the two previous versions" [[9](#v9)] | Not stated by the vendor [[18](#v18)] | macOS 12.0 or later [[23](#v23)] | macOS 13 or later [[2](#v2)] |
| Account needed | No [/privacy/] | Not stated by the vendor | "No sign-up required" [[15](#v15)] | Not stated by the vendor | No [[2](#v2)] |

Every cell was checked on 16 October 2026 against the source in brackets (V-ids are listed below; [check] is our own export with marsdawn 0.6.4). Vendor quotes stay as written. "Not stated by the vendor" means the pages we read were silent, not that the feature is missing. No cell ranks the products.

## Sources

- 1 · [Mac App Store](https://apps.apple.com/app/id6812925073)
- 2 · [https://lynxoffice.com/](https://lynxoffice.com/)
- 3 · [https://lynxoffice.com/markdown/](https://lynxoffice.com/markdown/)
- 4 · [https://lynxoffice.com/cli/](https://lynxoffice.com/cli/)
- 5 · [https://lynxoffice.com/mcp/](https://lynxoffice.com/mcp/)
- 6 · [https://lynxoffice.com/release-notes/](https://lynxoffice.com/release-notes/)
- 8 · [https://code.visualstudio.com/docs/languages/markdown](https://code.visualstudio.com/docs/languages/markdown)
- 9 · [https://code.visualstudio.com/docs/supporting/requirements](https://code.visualstudio.com/docs/supporting/requirements)
- 11 · [https://code.visualstudio.com/updates/v1_142](https://code.visualstudio.com/updates/v1_142)
- 12 · [https://code.visualstudio.com/license](https://code.visualstudio.com/license)
- 13 · [https://code.visualstudio.com/](https://code.visualstudio.com/)
- 14 · [https://code.visualstudio.com/docs/configure/command-line](https://code.visualstudio.com/docs/configure/command-line)
- 15 · [https://obsidian.md/pricing](https://obsidian.md/pricing)
- 16 · [https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax](https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax)
- 17 · [https://obsidian.md/help/pdf](https://obsidian.md/help/pdf)
- 18 · [https://obsidian.md/download](https://obsidian.md/download)
- 19 · [https://obsidian.md/changelog/](https://obsidian.md/changelog/)
- 20 · [https://obsidian.md/help/uri](https://obsidian.md/help/uri)
- 21 · [https://obsidian.md/help/Getting+started/Create+a+vault](https://obsidian.md/help/Getting+started/Create+a+vault)
- 22 · [https://github.com/sbarex/QLMarkdown](https://github.com/sbarex/QLMarkdown)
- 23 · [https://github.com/sbarex/QLMarkdown/releases](https://github.com/sbarex/QLMarkdown/releases)
- 24 · [https://api.github.com/repos/sbarex/QLMarkdown/releases](https://api.github.com/repos/sbarex/QLMarkdown/releases)
- kit · [https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7](https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7)

What MarsDawn lacks. It needs macOS 26 or later. There is no iPhone or iPad app; MarsDawn is for the Mac. There's no shared editing, no sync and no account. The preview can't be edited; you edit the Markdown source beside it. It doesn't export Word files and has no plugins. Its PDFs have no page numbers. There's no diff view: when an agent saves a change, the open window updates from disk in one step you can undo, but it doesn't highlight what changed. After the 14-day trial, documents open with their content covered until you unlock it.

## When you don't need MarsDawn

- You live in VS Code and a preview pane is enough: it renders Mermaid and KaTeX, shows Markdown diff previews and jumps to a line with code -g.
- You only want a space-bar preview in Finder: QLMarkdown is a free Quick Look extension for Markdown.
- Your Mac runs an older macOS: QLMarkdown needs 12.0 or later and LynxOffice 13 or later. The free marsdawn tool needs macOS 15 and exports PDF without the app.
- You keep a vault of linked notes: that is what Obsidian is built for.
- You need an iPhone or iPad app, shared editing or Word export.
- You want an agent to handle spreadsheets, Word files and PDFs: LynxOffice documents an MCP server for them.

- [MacMD Viewer vs. MarsDawn](/vs/macmd-viewer/): a read-only viewer next to MarsDawn, cell by cell, with when to pick each.
- [Markdown preview tools](/vs/markdown-preview-tools/): VS Code's preview, a browser extension and Claude Desktop's file preview.
- [Best Markdown viewer for Mac (2026)](/best-markdown-viewer-mac/)

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
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
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [Best Markdown viewer for Mac (2026)](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [Français](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [Español](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
