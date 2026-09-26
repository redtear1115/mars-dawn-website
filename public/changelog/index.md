# Changelog

What changed in the free marsdawn command-line tool. A Mac App Store build of MarsDawn is mentioned here only when it has a line of its own. Versions before 0.5.1 are not listed.

## marsdawn 0.6.0

1 October 2026. MarsDawn is on the Mac App Store.

- When the app isn't installed, `marsdawn open` points to MarsDawn on the Mac App Store.
- The README and the agent skill teach `marsdawn open .` and `--folder`: MarsDawn 1.0.0 shows the folder in the window's sidebar.

## marsdawn 0.5.4

26 September 2026. Mermaid fixes, diagram error lines and installing the skill.

- In a sequence diagram, a message label that crosses other participants' lifelines stays readable, in the preview and in exported PDFs.
- `marsdawn export` copes with documents full of Mermaid diagrams. One with 50 diagrams, which used to fail with exit 5, now exports.
- `marsdawn export --json` adds `diagramErrorDetails`, with line numbers for each diagram error: where the diagram starts in your document and, when Mermaid names one, the line of the error itself.
- `marsdawn skill --install` installs the agent skill for Claude Code at `~/.claude/skills/marsdawn/SKILL.md`, or in another folder with `--dir`. It leaves an identical file alone and replaces a different one only with `--force`. Otherwise it exits 64 (`skill_differs`) and changes nothing.

## marsdawn 0.5.3

25 September 2026. Folder status, full Mermaid errors and smaller fixes.

- `marsdawn open --folder` can say what happened to the folder. With an app that reports back, it waits up to `--wait` seconds (2 by default), and `--json` gives a status such as `attached` or `needsUser`.
- A Mermaid diagram that doesn't parse shows Mermaid's whole error message instead of only its first line, with the line number counted from the top of your document.
- The search for the end of a front-matter block stops after 1,000 lines, so an unclosed block no longer means scanning the rest of a large document.
- An app can give the footnote back-link a translated label for PDF export and printing. The label isn't printed on the page, and `marsdawn export` keeps the English one.
- The bundled highlight.js is now pinned by version, source and SHA-256, like KaTeX and Mermaid.

## marsdawn 0.5.2

24 September 2026. Footnotes, contrast and folders.

- Footnotes render in exported PDFs: numbered references, with the notes after the body.
- Every theme meets WCAG AA contrast, light and dark. Classic is now black and white.
- `marsdawn skill` prints the agent skill that matches the installed marsdawn.
- `marsdawn open` exits 6 (`app_cannot_open_folders`) when the MarsDawn it finds can't show a folder, instead of reporting success.
- The placeholders drawn into exported pages are also in German, French, Spanish and Korean.
- An image placeholder no longer shows the absolute path behind a very long relative path.
- `MARSDAWN_APP_PATH` is used only when it points at a MarsDawn app.

## marsdawn 0.5.1

19 September 2026. PDF export, and opening a file from the command line.

- The text layer of an exported PDF is repaired for Chinese, Japanese and Korean.
- `marsdawn open --background` opens a file without bringing MarsDawn to the front.
- `marsdawn open` can be given a folder, and MarsDawn shows it in the window's sidebar (MarsDawn 1.0.0 and later).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. On the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, on the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
