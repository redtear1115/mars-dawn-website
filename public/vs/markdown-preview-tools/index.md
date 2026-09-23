# Viewing Markdown elsewhere, vs. MarsDawn.

If you already have VS Code, a browser or Claude Desktop open, reaching for one of them to glance at a Markdown file is reasonable. Here's what each one actually renders, and what it costs to get there, compared with opening the same file in MarsDawn.

## At a glance

|  | VS Code preview | Browser extension | Claude Desktop | MarsDawn |
|---|---|---|---|---|
| Opens a Markdown file from disk | Yes | Yes, once file access is allowed | No: Markdown isn't on its upload list | Yes |
| Before the first file | Install VS Code, a whole development environment | Install an extension, then turn on “Allow access to file URLs” | It can't browse files on disk | Install MarsDawn |
| Built for | Writing code; the preview is one pane among many | Browsing the web | Conversations with Claude | Reading and editing Markdown |
| Draws the page with | Electron: a bundled Chromium and Node.js | A full browser | The Claude Desktop app | A native AppKit app; WebKit draws the page |

## VS Code's built-in preview

Press `⌘⇧V` in VS Code and it renders the Markdown file in a built-in preview pane, free, with nothing to install. As of VS Code 1.121 (May 2026), that preview also renders Mermaid diagrams natively — Microsoft folded a Mermaid extension into VS Code itself, so this used to need a separate extension and no longer does. What it doesn't do: it's a preview pane inside an editor, not an editor built for reading — the pane sits next to a file tree, a terminal and every other panel VS Code can show, and VS Code itself is an Electron app you install as a whole development environment, not something you open to read one file.

## A browser extension for local files

No single browser extension dominates for reading a local `.md` file: Local Markdown Viewer, Markdown Viewer, MarkView and others all do roughly the same thing, and none is a default. Every one of them needs the same extra step before it can open anything: turning on "Allow access to file URLs" for that extension, because browsers block extensions from reading `file://` pages by default. That's a permission you grant once per extension, and it's easy to forget you did it, or why. Once it's on, the file renders in a browser tab, which means running a full browser to look at one file.

## Claude Desktop's file preview

Claude Desktop shows a file that's already in a Project or a conversation. What it isn't built for is browsing arbitrary files on disk — what you can look at is what the conversation already holds, not a folder of notes you keep open beside your work. Anthropic's own list of [the document types you can upload](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai) is PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON and XLSX: Markdown isn't on it.

## A browser engine to read one file

VS Code is an Electron app: a bundled Chromium and Node.js runtime, not a native Mac app. The browser-extension route runs inside an actual browser. Either way, viewing one Markdown file means a full browser engine is running to show it. MarsDawn is a native AppKit app: no bundled browser runtime, it opens any local file directly, with no extension to install or permission flag to remember.

## Next

- What MarsDawn doesn't do either: [the list](/limits/).
- Turn any Markdown file into a PDF today, free: [Markdown to PDF](/markdown-to-pdf/).
- Compared with a Mac-native viewer instead: [MacMD Viewer vs. MarsDawn](/vs/macmd-viewer/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
