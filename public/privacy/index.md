# Privacy Policy

How MarsDawn, the Markdown editor for macOS, handles your information.

Last updated 2026-09-23

**The MarsDawn app does not collect any data about you.** There is no account, no advertising and no tracking. Your documents and settings stay on your Mac.

## The website

The app and this website are two different things. The app collects nothing. A visit can be recorded only here, on marsdawn.southern-light.dev.

This site uses **Google Analytics 4**, loaded through **Google Tag Manager**. Every visitor starts with analytics denied: Google's Consent Mode sends only a cookieless ping with no analytics cookie and no persistent identifier, until you choose *Accept* in the banner. Choosing *Decline*, or making no choice at all, keeps it that way, and choosing *Decline* after a prior *Accept* turns analytics back off immediately and removes the cookies below. Change your choice at any time with the "Cookie settings" link in the footer of every page. The choice itself is stored only in your browser's local storage, never in a cookie of ours.

Once you accept, Google Analytics sets its own cookies (`_ga` and `_ga_<measurement id>`) and records:

- **Page views and referrer.** Which page was viewed, and the referring address when the browser sends one.
- **Approximate location, device and browser.** A coarse location derived from your IP address (city level at most), your device type, operating system and browser — none of it precise enough to identify you.
- **Outbound clicks and scroll depth.** Google Analytics' enhanced measurement records clicks that leave the site, such as the link to the Mac App Store, and how far you scroll down a page.
- **IP addresses.** Google Analytics 4 does not log or store IP addresses.
- **What is not recorded.** No account, because the site has none. No document, and nothing you type. No cross-site advertising, and no profile of you. Requests the app makes for theme files under `/themes/` are skipped, and are not sent on.
- **Retention.** Google keeps this data for 14 months, then deletes it.
- **Where it's processed.** Google Tag Manager and Google Analytics are operated by Google; your data may be processed in the United States as well as other countries where Google operates.
- **The host.** Cloudflare hosts the site and, like any host, sees your IP address while it answers the request. That log belongs to the host. It is not the analytics above.

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

The MarsDawn app does not collect data from anyone, including children. A visit recorded on the website is not an account, and it is not used to identify anyone.

## Purchases

MarsDawn will be sold through the Mac App Store. Apple will process the purchase under its own terms, and the developer never receives your payment details.

## Changes to this policy

If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.

## Contact

Questions about privacy: [support@southern-light.dev](mailto:support@southern-light.dev)

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
