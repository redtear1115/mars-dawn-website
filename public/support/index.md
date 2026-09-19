# Support

Help with MarsDawn, the Markdown editor for macOS.

## Write to us

[support@southern-light.dev](mailto:support@southern-light.dev?subject=MarsDawn%20support)

Please include your macOS version and your MarsDawn version (MarsDawn › About MarsDawn). If something looks wrong, a screenshot or a small sample document helps a lot.

## Common questions

### What do I need to run MarsDawn?

A Mac with macOS 26 Tahoe or later, on Apple silicon or Intel.

### How do I switch between the editor and the preview?

Press `⌘1` for the source only, `⌘2` for side by side, and `⌘3` for the preview only. The same choices are in the View menu and the toolbar.

### An image in my document doesn't show.

- **Image on your Mac:** save the document first, then click *Grant Folder Access…* in the preview and choose the folder that holds the image. MarsDawn remembers the folder. You can review granted folders in MarsDawn › Settings › Folder Access.
- **Image from the web:** web images are blocked until you click *Load Images* at the top of the preview. To always load them, turn on *Load remote images automatically* in Settings.

### How do I add an image?

Drag it into the editor, or paste it. The document must be saved first: MarsDawn copies the image into an `assets` folder next to the document and writes the Markdown link for you.

### A Mermaid diagram shows an error.

MarsDawn shows the diagram's source with the first line of Mermaid's error message underneath. Check the line it names, for example for an arrow with nothing after it or a bracket that isn't closed.

### How do I make a PDF?

Choose File › Export as PDF… (`⌥⌘E`). The PDF uses the light version of your preview theme and is split into pages, whichever layout you are in. File › Print… prints the same pages.

### How do I use MarsDawn with Siri or Shortcuts?

Open the Shortcuts app and search for MarsDawn to find *New Markdown Document*, *Add Note to Inbox* and *Open Recent Document*. Before adding notes, choose a notes folder in MarsDawn › Settings › Notes Folder. Notes are added to `Inbox.md` in that folder.

### Where are my settings?

MarsDawn › Settings (`⌘,`) has appearance, images, the notes folder, folder access and the preview theme.

### How do I get a refund?

Purchases are handled by Apple. Request a refund at [reportaproblem.apple.com](https://reportaproblem.apple.com).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
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
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [日本語](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
