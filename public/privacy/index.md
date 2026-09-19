# Privacy Policy

How MarsDawn, the Markdown editor for macOS, handles your information.

Last updated 2026-09-19

**MarsDawn does not collect any data about you.** There is no account, no analytics, no advertising and no tracking. Your documents and settings stay on your Mac.

## What stays on your Mac

- **Your documents.** MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.
- **Your settings.** Appearance, preview theme, window layout and the image preference are stored in the app's own preferences on your Mac.
- **Folder access you grant.** When you let MarsDawn show images or page files from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. A folder you open in the sidebar stays readable and writable by MarsDawn until you remove it in Settings, not just while its window is open. You can remove folders at any time in MarsDawn › Settings.

## When MarsDawn uses the internet

MarsDawn works fully offline. It connects to the internet only **when you choose to**, for a document that refers to the web:

- **Markdown documents.** Web images are blocked by default. They load only after you click *Load Images* in the preview, or if you turn on *Load remote images automatically* in Settings. Nothing else a Markdown document refers to is loaded from the web.
- **HTML documents.** An HTML document opens static: its code doesn't run and nothing is loaded from the web. If a document contains code that could run, you can choose *View › Run This Document* for that document. Its own code then runs until you stop it, the document reloads or you close the window. That choice is never remembered, and it isn't a setting. While it runs, the document can send data over the network, and read images, style sheets, fonts and media in its folder and the folders inside it. Code downloaded from the web never runs.

MarsDawn loads web content over https only. A plain http address is never loaded, in any setting, and MarsDawn does not rewrite it to https. In a Markdown document, the preview shows a placeholder in its place.

When web content loads, your Mac requests it directly from the servers that host it. Like any web request, this lets those servers see your IP address and what was requested. MarsDawn's developer receives none of this information.

Links you click in the preview open in your default web browser, under that browser's own privacy practices. Audio and video never play by themselves.

## Siri, Shortcuts and Spotlight

MarsDawn offers actions for Siri, the Shortcuts app and Spotlight, such as creating a document or adding a note. When you use them, the text you provide is passed to MarsDawn on your Mac and saved only where the action says (a new document, or the `Inbox.md` file in the notes folder you chose). Speech you dictate to Siri is handled by Apple under [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

## Exporting and printing

PDF export and printing happen on your Mac. The PDF is saved where you choose. Printing goes through macOS to the printer you pick.

## The marsdawn command-line tool

The optional `marsdawn` command-line tool, distributed separately, also runs entirely on your Mac. It reads the Markdown file you name and writes the PDF you ask for. It loads web images only when you pass `--allow-remote-images`.

## Children

MarsDawn does not collect data from anyone, including children.

## Purchases

MarsDawn will be sold through the Mac App Store. Apple will process the purchase under its own terms, and the developer never receives your payment details.

## Changes to this policy

If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.

## Contact

Questions about privacy: [support@southern-light.dev](mailto:support@southern-light.dev)

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
