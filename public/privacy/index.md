# Privacy Policy

How MarsDawn, the Markdown editor for macOS, handles your information.

Last updated 2026-09-17

**MarsDawn does not collect any data about you.** There is no account, no analytics, no advertising and no tracking. Your documents and settings stay on your Mac.

## What stays on your Mac

- **Your documents.** MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.
- **Your settings.** Appearance, preview theme, window layout, and your choices about web images and web content are stored in the app's own preferences on your Mac.
- **Folder access you grant.** When you let MarsDawn show images or page files from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. A folder you open in the sidebar stays readable and writable by MarsDawn until you remove it in Settings, not just while its window is open. You can remove folders at any time in MarsDawn › Settings.

## When MarsDawn uses the internet

MarsDawn works fully offline. It connects to the internet only **when you choose to load web content** that a document refers to:

- **Markdown documents.** Web images are blocked by default. They load only after you click *Load Images* in the preview, or if you turn on *Load remote images automatically* in Settings. Nothing else a Markdown document refers to is loaded from the web.
- **HTML pages.** MarsDawn shows HTML files read-only. Web content a page refers to (images, stylesheets, fonts, audio/video) loads only when you choose, and this has its own setting, which is off by default. Page scripts never run.

MarsDawn loads web content over https only. A document that refers to a plain http address is never loaded, in any setting, and MarsDawn does not rewrite it to https. The preview shows a placeholder in its place.

When web content loads, your Mac requests it directly from the servers that host it. Like any web request, this lets those servers see your IP address and what was requested. MarsDawn's developer receives none of this information.

If you allow web content for an HTML page, that page's layout could let those servers learn whether files the page itself refers to exist in the folder you gave MarsDawn access to, and roughly how large they are. The page can't read your files or send their contents, and this can't happen while web content is blocked.

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

MarsDawn is sold through the Mac App Store. Apple processes the purchase under its own terms, and the developer does not receive your payment details.

## Changes to this policy

If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.

## Contact

Questions about privacy: [support@southern-light.dev](mailto:support@southern-light.dev)

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): MarsDawn is a native Markdown editor for the Mac with live preview, Mermaid diagrams and PDF export.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
