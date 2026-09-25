# Changelog

What changed in the free marsdawn command-line tool. A Mac App Store build of MarsDawn is mentioned here only when it has a line of its own. Versions before 0.5.1 are not listed.

## marsdawn 0.5.4

1 October 2026. MarsDawn is on the Mac App Store.

- When the app isn't installed, `marsdawn open` points to MarsDawn on the Mac App Store.
- The README and the agent skill teach `marsdawn open .` and `--folder`: MarsDawn 1.0.0 shows the folder in the window's sidebar.

## marsdawn 0.5.3

25 September 2026. Folder status, clearer diagram errors, and export fixes.

- `marsdawn open --folder` can report back what happened to the folder, with `--wait`: `attached`, `needsUser`, and more, from an app that opts in.
- A Mermaid diagram's parse error shows the full message, mapped to the document's line, instead of only its first line.
- Scanning for an unclosed front-matter block stops after 1000 lines, instead of scanning the rest of a large document on every edit.
- Exported PDFs can carry a localized label for the footnote back-link.
- The vendored highlight.js is now recorded by version, source and SHA-256, the way KaTeX and Mermaid already are.
- Reading a file iCloud has offloaded restores the thread's file-materialization policy correctly, even when the previous one couldn't be read.

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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
