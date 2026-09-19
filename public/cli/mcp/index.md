# Three ways to call marsdawn.

MarsDawn has no AI model of its own: it's built to review Markdown, not write it, so it doesn't matter which agent or model produced the file. There are three ways for an agent or a script to call `marsdawn`, and all three end up running the same `export`.

**Pick whichever your tooling supports: the free `marsdawn` CLI, a plain-Markdown skill file, or the [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) MCP server.** All three call the same `marsdawn export` and return the same JSON result.

## Which one to use

| If your agent | Use | Needs |
|---|---|---|
| Can run a shell command | [The CLI](/cli/agents/) | macOS 15 or later |
| Loads instruction files, like Claude Code | [The skill file](/cli/skill/) | The CLI, which the skill installs |
| Calls tools over MCP | [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) | marsdawn-mcp 0.2.1 or later, marsdawn 0.5.0 or later, and Node.js 20 or later |

## The CLI

`marsdawn export notes.md --json` is callable by any agent or script that can run a shell command, model-agnostic by construction. Every field it returns is documented at [marsdawn for agents](/cli/agents/), which is the source of truth for the JSON schema the other two surfaces below point back to.

## The skill file

For an agent that reads plain-Markdown instructions instead of calling a shell directly — Claude Code today — [the marsdawn skill](/cli/skill/) is one file that teaches it to install marsdawn, run `export` and read the result. It's plain Markdown, so other agents that load instruction files can use the same one.

## The MCP server

[marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) is a separate, public, Apache-2.0 repository. It's an MCP server with two tools, `export_markdown_to_pdf` and `open_in_marsdawn`, that wrap `marsdawn export --json` and `marsdawn open --json`: point an MCP client at it and a tool call returns the same JSON as the CLI.

- **Get it:** as an MCP Bundle, `marsdawn.mcpb`, attached to [its GitHub release](https://github.com/redtear1115/marsdawn-mcp/releases), or by running the server from source over stdio.
- **Registry:** not yet listed in the MCP Registry (current release: 0.2.1). Check the repository for the current status before relying on registry discovery.
- **Hosting:** self-hosted only. There is no hosted marsdawn-mcp service; the server runs on your own machine, next to marsdawn itself.
- **Requirements:** macOS, marsdawn 0.5.0 or later, and Node.js 20 or later to run the server.

## Confined to folders you allow

Both tools only reach inside folders you allow: the extension's **Allowed folders** setting, which starts empty with no preset, or the roots your MCP client offers instead. With neither set, every call is refused, and the refusal message says how to fix that. Every path has to be absolute, and `export_markdown_to_pdf` only ever writes a `.pdf` file, never through a symlink.

**Security:** update to [0.2.1](https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1) — 0.1.0 and 0.2.0 let a call write a PDF to any path your account could write, fixed as [GHSA-fqgj-hcxc-34qc](https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc).

## Same export, three doors

Whichever surface calls it, the underlying behavior doesn't change: the same exporter, the same themes and paper sizes, the same `diagramErrors` when a Mermaid diagram fails to render. This page doesn't repeat that contract — [marsdawn for agents](/cli/agents/) does, in full.

## Next

- The full JSON schema and every exit code: [marsdawn for agents](/cli/agents/).
- The one-file skill for Claude Code and similar agents: [the marsdawn skill](/cli/skill/).
- Why a compact JSON result matters to your agent's own context: [token-efficient review](/token-efficient-review/).

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
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
