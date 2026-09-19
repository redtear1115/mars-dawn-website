# MacMD Viewer vs. MarsDawn.

Both are Mac apps for reading Markdown rendered. MacMD Viewer opens a `.md` file and shows the finished page; it doesn't edit it. MarsDawn puts an editor next to the same kind of rendered preview, so you write and review in one window. Here's how they differ, feature by feature.

## If you only need to read, not edit

If your job is strictly reading Markdown someone else wrote, and you never need to touch the source, MacMD Viewer is a reasonable fit: it's built for exactly that, is available now and works down to an older macOS. MarsDawn is worth it once reading isn't the whole job, because an agent's Markdown usually comes back for another pass.

## What each app does

- **Editing:** MacMD Viewer is read-only by design. MarsDawn edits the source and renders it side by side, so a change shows up as you type.
- **Preview themes:** MacMD Viewer ships 12 document themes. MarsDawn ships four, Dawn, Classic, Modern and Vivid, each with a light and a dark palette.
- **Diagrams and math:** both render Mermaid diagrams and highlight code. MarsDawn also renders KaTeX math; MacMD Viewer's own listing doesn't mention math rendering.
- **Finder integration:** both add a Quick Look extension, so pressing Space on a `.md` file in Finder shows the rendered page.
- **PDF and print:** both export or print a PDF of the rendered page.
- **System requirements:** MacMD Viewer needs macOS 14 (Sonoma) or later. MarsDawn needs macOS 26 (Tahoe) or later.
- **Languages:** MarsDawn's interface ships in 英語、繁体字中国語、簡体字中国語、日本語. MacMD Viewer's own materials don't state a UI language, so this page doesn't compare that.

## Pricing and how you buy it

- **Where you buy it:** MacMD Viewer is a direct download from its own site, also on Homebrew and Setapp; it isn't on the Mac App Store. MarsDawn is Mac App Store only.
- **Price:** MacMD Viewer is USD 19.99 once for one Mac (a 3-Mac pack and volume packs cost more). MarsDawn is a free download, then a USD 4.99 one-time unlock.
- **Trying it first:** MacMD Viewer has no free trial; direct purchases carry a 14-day money-back guarantee instead. MarsDawn gives you a 14-day trial before you pay anything.
- **Refunds and updates:** MacMD Viewer's refunds and updates run through its own site. MarsDawn's purchase goes through Apple, so refunds and updates use Apple's standard process.
- **Accounts:** neither app needs an account to use.

## Try it today, free

MarsDawn is coming soon to the Mac App Store, not on sale yet. Until then, the free `marsdawn` command-line tool renders any Markdown file to a PDF today, with Mermaid diagrams and highlighted code, and needs nothing else installed:

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## Next

- The full walk-through: [Markdown to PDF](/ja/markdown-to-pdf/).
- What MarsDawn doesn't do: [the list](/ja/limits/).
- Every option of the command-line tool: [Command Line](/ja/cli/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/ja/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.
- [A Mac app](https://marsdawn.southern-light.dev/ja/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/ja/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/ja/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [View Markdown on a Mac](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
- [Markdown to PDF](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [Command Line](https://marsdawn.southern-light.dev/ja/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
