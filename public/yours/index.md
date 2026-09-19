# Your writing stays on your Mac.

MarsDawn has no account, no sync and no cloud. It opens a file, you write, and it saves the file where you choose.

![MarsDawn showing a document in the Classic theme, with the preview filling the window.](https://marsdawn.southern-light.dev/assets/screens/02-classic-1180.png)

In this screenshot:

1. The window title is the file's name: a plain .md file on your Mac.
2. The toolbar holds themes and layouts. There's no account button and no sign-in.

**MarsDawn does not collect any data about you.** The app never uploads your documents, and its developer receives nothing when your Mac loads something from the web.

## No account, no cloud, no tracking

- **No account.** There is nothing to sign up for or sign in to.
- **No sync.** Your documents stay where you save them, so to use one on another Mac, keep it in a folder you already sync. More in [what MarsDawn doesn't do](/limits/).
- **No analytics, advertising or tracking.** Its App Store privacy label will say "Data Not Collected".
- **Only what you open.** MarsDawn reads the files and folders you open or choose. A folder you open in the sidebar stays readable and writable until you remove it in MarsDawn › Settings. See [what stays on your Mac](/privacy/#on-your-mac).

## The only times it goes online

MarsDawn works fully offline. It connects only when you choose to:

- **Web images in Markdown** load when you click *Load Images*, or always if you turn on *Load remote images automatically* in Settings. Until then, opening a document tells no server you read it. When they load, your Mac asks the hosting server directly, so that server sees your IP address; MarsDawn's developer receives none of it.
- **HTML documents** open static: nothing loads and their code doesn't run unless you choose *View › Run This Document* for that one document. While it runs, that document can send data over the network. The choice is never remembered.
- **Links** you click open in your default browser, under its own privacy practices.
- **The free [marsdawn CLI](/cli/)** runs entirely on your Mac and loads web images only when you pass `--allow-remote-images`.

Web content loads over https only: a plain http address is never loaded, in any setting. Siri dictation and App Store purchases are handled by Apple, under Apple's terms.

Every detail is in the [privacy policy](/privacy/#internet). Questions about privacy: [support@southern-light.dev](mailto:support@southern-light.dev)

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
