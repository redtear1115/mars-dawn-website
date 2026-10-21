# Changelog

Black Friday: the one-time unlock is half price, USD 2.49 instead of USD 4.99, through 30 November. It returns to USD 4.99 on 1 December. <!-- sale-line -->

What changed in each version of the MarsDawn app on the Mac App Store and the free marsdawn command-line tool. App dates are the day the version appeared on the Mac App Store.

## MarsDawn app

### MarsDawn 1.1.1

15 October 2026

- In German, Japanese, Spanish and French, Settings > Appearance > Get More Themes... now shows the scenario filter as a pop-up menu labelled Scenario, so the five choices fit. English, Korean and Chinese still use the segmented control.
- When a theme leaves the gallery, the notice in Get More Themes... now shows the theme's name (for example Inkwell Ivory) instead of its internal id.
- Collapsible details sections written the GitHub way now start collapsed with their summary shown in the preview and in Quick Look, and open on click. PDF export still prints every section's content.
- Documents you open from Finder, the Dock, File > Open... or the marsdawn open command now open as tabs in the front window, and so do new documents. To keep the previous behaviour, choose Follow System Setting in Settings > Appearance.

### MarsDawn 1.1.0

9 October 2026

- Settings > Appearance has a new Get More Themes... button. It opens a gallery of extra preview themes. Install one and it shows up under View > Preview Theme; Remove takes it away again. The gallery only goes online while it is open.
- Quick Look previews in Finder now use the theme you picked, instead of always Dawn.
- Quick Look also follows the Appearance setting in MarsDawn: Light and Dark stay as chosen even when your Mac is set the other way, and System follows your Mac.
- The git marker in the window title now shows "+" for a file that is staged but not yet committed. Before, it looked clean.
- Clicking a link to another Markdown file in the preview, such as [notes](notes.md#plan), now opens that file, or brings it forward if it is already open, and scrolls to the heading. If the file is outside your sidebar folders, MarsDawn offers to add its folder to the sidebar. Then click the link again.

### MarsDawn 1.0.2

7 October 2026

- Fixed: the editor no longer shifts up slightly the first time you switch layouts or show or hide the sidebar.
- When a Mermaid diagram can't be drawn, its full error message now appears. If the line is known, clicking the message jumps to that line in the editor.

### MarsDawn 1.0.0

5 October 2026

First release.

## marsdawn command-line tool

Versions before 0.5.1 are not listed.

### marsdawn 0.7.2

20 October 2026. The Handbook layout, callouts and Japanese fonts.

- The manual layout is now called Handbook: `marsdawn export --layout handbook`. `--layout manual` still works, but is deprecated.
- Callouts render, in the preview and in exported PDFs: GitHub alerts such as `> [!NOTE]` and `> [!WARNING]`, and HackMD containers such as `:::info` and `:::warning`. `:::spoiler` makes a collapsible section.
- A Japanese document uses Japanese fonts for its kana and kanji. marsdawn takes the language from `lang: ja` in the front matter, or from how much kana the text has.
- After a successful `export` or `open` in a terminal, marsdawn shows a one-time tip on stderr when the agent skill is missing or out of date. Output on stdout and with `--json` doesn't change. Set `MARSDAWN_NO_SKILL_HINT=1` to turn the tip off.

### marsdawn 0.7.1

20 October 2026. The Handbook layout, and a size limit.

- `marsdawn export --layout manual` prints the Handbook layout: wider margins, a 25 mm binding side and each top-level heading on a new page, plus a cover from the front matter's title, subtitle, version, date, author and logo, a table of contents of the level 1 and 2 headings with page numbers, `n / N` page numbers and PDF bookmarks. `--toc-title` sets the title of the contents page. `--layout document` is still the default.
- `<!--BREAK-->` on a line of its own starts a new page, in either layout.
- `marsdawn export` refuses a file over 16 MiB: it exits 5, reports `input_too_large` with `--json`, and writes nothing.
- The preview page drops script and noscript elements; a Mermaid redraw keeps its own SVG.
- A character reference that decodes to `=` or `^`, such as `&#61;`, no longer pairs with a HackMD mark.

### marsdawn 0.7.0

18 October 2026. HackMD Markdown, line breaks and limits for very large documents.

- HackMD's inline marks render: `==mark==`, `^sup^` and `~sub~`. A `[TOC]` paragraph on its own becomes a table of contents, HackMD image sizes apply, embed tags become plain https links, and a code fence's language is read before HackMD options such as `js=`.
- `marsdawn export --breaks` turns every newline inside a paragraph into a line break, as HackMD does. Without it, a newline between two Chinese or Japanese characters is dropped, so the lines read as one sentence. Korean keeps its space, because it spaces its words.
- Very large documents have limits, in the preview and in exported PDFs. A code block over 128K characters isn't highlighted, and highlighting stops after 256K characters in all. Up to 100 Mermaid diagrams and 1,000 math expressions are rendered per update; the other diagrams show their source, with a note, even if they were drawn before.
- In a sequence diagram, a message label inside a `rect` block gets a halo in the block's color.
- A footnote reference just above a table no longer crashes `marsdawn export`.
- `marsdawn skill --install` exits 7 (`skill_install_failed`) when it can't create the folder or write the file, and leaves an existing SKILL.md as it was.

### marsdawn 0.6.4

13 October 2026. Collapsible `<details>` blocks.

- A GitHub-style `<details>` block with blank lines inside renders as one collapsible element, in the preview and in exported PDFs. Before, it broke apart at the first blank line.
- PDF export opens every `<details>` block before printing, except front matter.
- The preview keeps its scroll position when you open or close a `<details>` block.

### marsdawn 0.6.3

6 October 2026. MarsDawn is on the Mac App Store.

- When the app isn't installed, `marsdawn open` points to MarsDawn on the Mac App Store.
- The README and the agent skill teach `marsdawn open .` and `--folder`: MarsDawn 1.0.0 shows the folder in the window's sidebar.

### marsdawn 0.6.1

29 September 2026. Checking a theme.

- `marsdawn theme validate` checks a `theme.json` against the rules the app uses. It exits 0 when the theme is valid and 1 when it isn't, with each problem listed. `--require-complete` also asks for the syntax and diagram colors.
- `marsdawn theme css` prints the CSS the preview uses for a valid theme, and `marsdawn theme preview` renders a sample document with it to a PNG, light or dark.

### marsdawn 0.5.4

26 September 2026. Mermaid fixes, diagram error lines and installing the skill.

- In a sequence diagram, a message label that crosses other participants' lifelines stays readable, in the preview and in exported PDFs.
- `marsdawn export` copes with documents full of Mermaid diagrams. One with 50 diagrams, which used to fail with exit 5, now exports.
- `marsdawn export --json` adds `diagramErrorDetails`, with line numbers for each diagram error: where the diagram starts in your document and, when Mermaid names one, the line of the error itself.
- `marsdawn skill --install` installs the agent skill for Claude Code at `~/.claude/skills/marsdawn/SKILL.md`, or in another folder with `--dir`. It leaves an identical file alone and replaces a different one only with `--force`. Otherwise it exits 64 (`skill_differs`) and changes nothing.

### marsdawn 0.5.3

25 September 2026. Folder status, full Mermaid errors and smaller fixes.

- `marsdawn open --folder` can say what happened to the folder. With an app that reports back, it waits up to `--wait` seconds (2 by default), and `--json` gives a status such as `attached` or `needsUser`.
- A Mermaid diagram that doesn't parse shows Mermaid's whole error message instead of only its first line, with the line number counted from the top of your document.
- The search for the end of a front-matter block stops after 1,000 lines, so an unclosed block no longer means scanning the rest of a large document.
- An app can give the footnote back-link a translated label for PDF export and printing. The label isn't printed on the page, and `marsdawn export` keeps the English one.
- The bundled highlight.js is now pinned by version, source and SHA-256, like KaTeX and Mermaid.

### marsdawn 0.5.2

24 September 2026. Footnotes, contrast and folders.

- Footnotes render in exported PDFs: numbered references, with the notes after the body.
- Every theme meets WCAG AA contrast, light and dark. Classic is now black and white.
- `marsdawn skill` prints the agent skill that matches the installed marsdawn.
- `marsdawn open` exits 6 (`app_cannot_open_folders`) when the MarsDawn it finds can't show a folder, instead of reporting success.
- The placeholders drawn into exported pages are also in German, French, Spanish and Korean.
- An image placeholder no longer shows the absolute path behind a very long relative path.
- `MARSDAWN_APP_PATH` is used only when it points at a MarsDawn app.

### marsdawn 0.5.1

19 September 2026. PDF export, and opening a file from the command line.

- The text layer of an exported PDF is repaired for Chinese, Japanese and Korean.
- `marsdawn open --background` opens a file without bringing MarsDawn to the front.
- `marsdawn open` can be given a folder, and MarsDawn shows it in the window's sidebar (MarsDawn 1.0.0 and later).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 2.49 once.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 2.49. No subscription, no account.
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
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 2.49 once.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
