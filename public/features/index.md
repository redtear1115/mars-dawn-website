# Everything MarsDawn does, on one page.

MarsDawn is a Markdown editor for the Mac. You write on one side and read the rendered page on the other, with diagrams, math and code drawn in. It has no AI model of its own: it is built for reading what an agent wrote, and for writing your own. And when the work moves to a table, a meeting or a filing cabinet, it prints and exports clean pages.

Each section below says what the app does and links to the page that goes deeper.

![MarsDawn in split view: the Markdown source on the left, the rendered page on the right.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

In this screenshot:

1. A native Mac window.
2. The Mac's text editor, with Markdown highlighting.
3. ⌘1 source, ⌘2 split, ⌘3 preview.
4. The page updates as you type.

## Read what your agent wrote

### Source and preview, side by side

Open a Markdown file and read the rendered page next to its source (⌘2), or switch to source only (⌘1) or preview only (⌘3). The two panes scroll together, and the page updates as you type.

[A Mac app](/native/)

### Outline and Files sidebar

The sidebar's Outline tab lists a document's headings; click one to jump there. Open a folder and the Files tab lists what is in it, and new files appear on their own while an agent is writing into it. If the folder is a git checkout, the header names the branch or worktree.

[Reading what your agent hands back](/reading-agent-output/)

### Point at the exact line

Edit ▸ Copy Reference copies your place as a path and line, like `docs/plan.md:42`. Copy for AI adds the selected text under it. Paste either into the agent's chat.

[Reading what your agent hands back](/reading-agent-output/)

### Follow links between files

Click a link to another Markdown file in the preview and MarsDawn opens it, or brings it forward if it is already open, and scrolls to the heading.

## On paper, among people

Not all of the work happens on a screen. The pages MarsDawn prints and exports are the ones you read on screen, so they work where people meet, read and keep records.

### In the meeting

Print the pages, or send everyone the same PDF, and the whole table works from the same document instead of one shared screen. Everyone holding the same file has the same page breaks, so "the table on page 3" points at one thing. Then the people write the decisions down, on the printout or in notes. The meeting-notes template starts with decisions and gives each action item an owner.

[PDF export](/pdf/) · [Meeting notes template](/templates/meeting-notes/)

### Reading with a pen

Some people take things in better with a pen: underlining, writing in the margin, so it sticks. Print the document and do that on paper. MarsDawn has no annotation tool of its own, so if you would rather mark up the PDF, use the PDF app you already have.

[PDF export](/pdf/)

### Paper records

Some fields still file paper, accounting among them. MarsDawn makes no archival or compliance claim. What it does is print and export clean, paginated pages: diagrams drawn in, short code blocks kept whole, the theme's light colors. Use them wherever paper is still the record.

[PDF export](/pdf/)

### Handing it to someone who doesn't use Markdown

A PDF opens in anything and needs no Markdown knowledge, so it is also the one to send a manager or a client.

[Sharing exported PDFs](/sharing-exported-pdfs/)

## Write and lay out

### Plain Markdown, highlighted

Bold, italic, strikethrough, inline code, links, block quotes and task lists all work. The editor colors Markdown syntax, and the colors match your preview theme.

[A Mac app](/native/)

### Zoom, line numbers and a status bar

Zoom the source and preview together from 50% to 300%. A line-number gutter runs beside the source, and the status bar shows your line and column, plus word and character counts and reading time for the document or your selection.

### Images

Save the document, then drop or paste an image into the editor. MarsDawn copies it into an assets folder next to the document and writes the link. Images from the web stay hidden until you click Load Images, so opening a document never tells a server you read it.

[Your writing stays on your Mac](/yours/)

### Front matter stays out of the way

A front matter block at the top of a file shows as a collapsed Document info section in the preview and Quick Look, and is left out of the PDF.

### Eight languages

The app is in English, Traditional Chinese, Simplified Chinese, Japanese, German, French, Spanish and Korean.

[A Mac app](/native/)

## Diagrams, code and math

### Mermaid diagrams

A fenced code block marked `mermaid` is drawn as a diagram. If the diagram has a mistake, the preview shows its source with the error underneath, and clicking the message jumps to that line.

[Mermaid preview on Mac](/mermaid-preview-mac/)

### Highlighted code

Code blocks are highlighted for most common languages. Name the language after the opening fence.

### Math

Math written in KaTeX syntax is drawn in the preview and in Quick Look, and comes through in the exported PDF.

[Why AI output still needs a human reader](/reviewing-ai-output/)

## Themes, PDF and print

### Four themes, light and dark

Dawn, Classic, Modern and Vivid each come in a light and a dark version, and MarsDawn follows your Mac's appearance unless you pick one in Settings. Choose from View ▸ Preview Theme or the palette button in the toolbar.

[Preview themes and PDF export](/themes/)

### More themes

Settings ▸ Appearance ▸ Get More Themes… opens a gallery of extra preview themes. Install one and it shows up under View ▸ Preview Theme; Remove takes it away again. The gallery only goes online while it is open.

[Theme gallery](/themes/gallery/) · [Build a theme](/themes/new/)

### Export as PDF, or print

File ▸ Export as PDF… saves a paginated PDF, and File ▸ Print… prints the same pages. Mermaid diagrams are drawn in, code keeps its highlighting, and page breaks avoid splitting a heading from its section or cutting a short code block or diagram in half. The PDF always uses the theme's light colors, even if you were reading in dark.

[PDF export](/pdf/)

![A PDF exported from MarsDawn, open in its PDF viewer with page thumbnails.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

In this screenshot:

1. Mermaid diagrams, drawn into the PDF.
2. Code keeps its highlighting.

## Files, tabs and Quick Look

### Windows and tabs

Each document opens in its own window. Choose Window ▸ Merge All Windows to gather open windows as tabs of one. Autosave runs as you type.

[A Mac app](/native/)

### Quick Look in Finder

Select a Markdown file in Finder and press Space to read it rendered, diagrams included. Quick Look uses the theme you picked in MarsDawn and follows its Appearance setting.

[A Mac app](/native/)

### Other files

MarsDawn also opens plain text files (`.txt`, `.log`, source code) and PDFs. UTF-8 text opens ready to edit, as source only. PDFs open in a viewer with page thumbnails, zoom and search.

### Your files stay yours

There is no account, no sync and no cloud. Documents stay where you save them, and MarsDawn collects no data about you.

[Your writing stays on your Mac](/yours/)

## For agents and scripts

### A free command-line tool

The free `marsdawn` tool is installed separately with Homebrew. `marsdawn export` turns a Markdown file into a PDF, rendered like MarsDawn's preview; it does not need the app. Choose a theme with `--theme` and paper size A4 or Letter. `marsdawn open` opens files in the app for you to review, optionally at a line, and does need the app installed.

[Command Line](/cli/)

### Output a script can read

Add `--json` and both commands return a result an agent or script can parse.

[marsdawn for agents](/cli/agents/)

### Skill and MCP server

An agent skill file teaches a coding agent to open what it wrote in MarsDawn for your review. For clients without a shell, a separate MCP server runs the same export.

[Agent skill](/cli/skill/) · [MCP server](/cli/mcp/)

### No AI inside

MarsDawn has no AI model of its own. It won't summarize or grade what an agent wrote; it keeps a long, changing file readable so you can do the reading.

[What MarsDawn doesn't do](/limits/)

## Siri and Shortcuts

Search for MarsDawn in the Shortcuts app to find three actions: New Markdown Document (from a template), Add Note to Inbox and Open Recent Document. Notes go to `Inbox.md` in the folder you choose in MarsDawn ▸ Settings… ▸ Notes Folder.

[A Mac app](/native/)

## After the page is printed

A meeting around printed pages, a pen in the margin, a paper record on file.

[MarsDawn film, 88 seconds](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## Try it on your Mac

MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account. It needs macOS 26 or later.

[Download and try it free](https://apps.apple.com/app/id6812925073)

How the trial works: [Try free, pay once](/pay-once/). What is left out on purpose: [What MarsDawn doesn't do](/limits/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
