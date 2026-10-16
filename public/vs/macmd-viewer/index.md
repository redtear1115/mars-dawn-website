# MacMD Viewer vs. MarsDawn.

Both are Mac apps for reading Markdown as a finished page. MacMD Viewer opens a `.md` file and shows it; it is read-only by design and never saves changes to your file. MarsDawn puts an editor next to the same kind of rendered preview, so you write and review in one window. This page sets the two side by side, row by row, with a source for every fact about MacMD Viewer, and says when MacMD Viewer is the better choice.

Checked against MacMD Viewer's own site and repository on 15 October 2026 (version 1.7.0, released 10 October 2026). If something here is out of date, tell us at the address on the [support page](/support/).

## What it is and what it does

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| What it is | A viewer: "read-only and never saves changes to your source file" [[S1](#s1), [S9](#s9)] | An editor with a live preview: Markdown on the left, the rendered page on the right, in three layouts (source, split, preview) |
| Editing | No [[S1](#s1), [S7](#s7), [S9](#s9)] | Yes. The rendered page itself isn't editable; you edit the source beside it |
| Live preview | Renders the file; reloads when the file is saved by another editor [[S9](#s9)] | Updates as you type. When another app changes the file, MarsDawn reloads it and keeps your place, as long as you have no unsaved edits of your own. |
| Mermaid | Yes: flowcharts, sequence, state and Gantt diagrams, pie charts and more, offline [[S1](#s1), [S3](#s3), [S7](#s7)] | Yes |
| Math | No: its README says it "does not render math (LaTeX/KaTeX)" [[S7](#s7)] | Yes, KaTeX |
| Code highlighting | Yes [[S1](#s1), [S9](#s9)] | Yes |
| Themes | 12 document themes [[S1](#s1), [S7](#s7)] | 4 built in (Dawn, Classic, Modern, Vivid), each with a light and a dark palette, plus more in the theme gallery |
| Tabs | Yes, optional and off by default (since 1.6.0) [[S5](#s5), [S8](#s8)] | Yes |
| PDF export | Yes, one continuous page, in the current theme, no watermark [[S3](#s3), [S9](#s9)] | Yes, paginated pages in the theme's light palette; page breaks avoid splitting short code blocks |
| Print | Yes, through the macOS print dialog [[S3](#s3), [S9](#s9)] | Yes |
| Quick Look in Finder | Yes, included; you enable it in System Settings; uses your theme [[S4](#s4)] | Yes, works with or without the trial; uses your theme |
| Mermaid and math in Quick Look | Mermaid: yes [[S4](#s4)]. Math: no, it doesn't render math [[S7](#s7)] | Yes, both are drawn |
| Command line | No standalone command-line tool is described. It has a `markdownviewer://` URL scheme and a Claude Code plugin and hooks that open files in the viewer [[S6](#s6)] | The free `marsdawn` tool: `marsdawn export` renders a PDF without the app, `marsdawn open` opens a file at a line |
| Interface languages | Not stated in its own materials [[S1](#s1), [S3](#s3), [S7](#s7)] | English, Traditional Chinese, Simplified Chinese, Japanese, German, French, Spanish and Korean |
| Requires | macOS 14 (Sonoma) or later; Apple Silicon and Intel [[S1](#s1), [S7](#s7)] | macOS 26 (Tahoe) or later |
| Other platforms | Mac only [[S1](#s1)] | Mac only. No iPhone or iPad app |

## Price and how you buy it

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Where you buy it | Its own site, Homebrew or Setapp; no Mac App Store listing [[S2](#s2), [S7](#s7)] | The Mac App Store only |
| Price | USD 19.99 once, for one active Mac (movable to another Mac); Family Pack USD 39.99 for 3; 10 keys USD 129 [[S2](#s2)] | Free download, then USD 4.99 once |
| Trying it first | No trial or free tier; 14-day full refund on direct purchase [[S2](#s2)] | 14-day free trial with everything on |
| Refunds | Through its own support, within 14 days [[S2](#s2)] | Through Apple |
| Updates | Updates within the current major version are free [[S2](#s2)]; the direct download updates itself with Sparkle [[S7](#s7)] | Through the Mac App Store |
| Account needed | No [[S2](#s2)] | No |
| Subscription | No [[S1](#s1), [S2](#s2)] | No |

## What changes if you stop paying or trying

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| After the trial or purchase window | No trial; keeps working once bought | If you don't unlock after 14 days, documents open with their content covered; your files are untouched, Quick Look and the free `marsdawn` export keep working |

## Sources

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## Which one to pick

**Pick MacMD Viewer if** you only read Markdown and you want that to be guaranteed: it never saves changes to your file [[S1](#s1)]. It also fits better if your Mac runs macOS 14 or 15, since MarsDawn needs macOS 26 [[S1](#s1), [S7](#s7)]; if you would rather buy from a developer's own site, Homebrew or Setapp than the Mac App Store [[S2](#s2), [S7](#s7)]; if you want files an agent edits to open in the viewer automatically, which it does through hooks for Claude Code, Cursor and Windsurf [[S6](#s6)]; or if you want a single continuous-page PDF rather than paginated pages [[S9](#s9)]. It has no trial, but it has a 14-day refund [[S2](#s2)].

**Pick MarsDawn if** the Markdown comes back for another pass. An agent's plan, README or spec usually needs a fix, a reworded line or a new section, and in MarsDawn you do that in the window where you are already reading. It also covers math (KaTeX), which MacMD Viewer says it doesn't render [[S7](#s7)]; it ships in eight interface languages; it has a free `marsdawn` command line that exports a PDF without the app; and its price is USD 4.99 after a 14-day trial in which everything works.

**Either works if** you read Markdown on a recent Mac, want Mermaid diagrams drawn properly and want Quick Look in Finder. Both do those.

**And you can use both.** They aren't exclusive: nothing stops you from keeping a read-only viewer for what you only read and an editor for what you write.

## Questions

### Does MacMD Viewer edit files?

No. It is read-only and, in its own words, never saves changes to your source file [[S1](#s1), [S9](#s9)]. It can open the file in your text editor (File menu, ⇧⌘E, since 1.7.0), which hands the file to another app [[S5](#s5)].

### Is MacMD Viewer on the Mac App Store?

Its own pages list its site, Homebrew and Setapp, and don't mention the Mac App Store [[S2](#s2), [S7](#s7)]. MarsDawn is on the Mac App Store only.

### Can MarsDawn open the same files?

Yes. It opens `.md` files, and also plain text files and PDFs: text opens ready to edit as UTF-8, and PDFs open in a viewer.

### What if I'm on macOS 14 or 15?

MacMD Viewer runs on macOS 14 or later [[S1](#s1)]. MarsDawn needs macOS 26 or later, and the free `marsdawn` command-line tool can still export a PDF.

### Why is one USD 19.99 and the other USD 4.99?

They differ in what you get and how you pay. MacMD Viewer is a one-time purchase with a 14-day refund and no trial [[S2](#s2)]. MarsDawn is a free download with a 14-day trial, then a one-time unlock. Neither is a subscription.

## Try it today, free

MarsDawn is on the Mac App Store. The free `marsdawn` command-line tool also renders any Markdown file to a PDF, with Mermaid diagrams and highlighted code, and needs nothing else installed:

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## Next

- The full walk-through: [Markdown to PDF](/markdown-to-pdf/).
- What MarsDawn doesn't do: [the list](/limits/).
- Every option of the command-line tool: [Command Line](/cli/).
- Compared with reading Markdown in VS Code, a browser or Claude Desktop instead: [how they compare](/vs/markdown-preview-tools/).
- All of MarsDawn's features on one page: [Features](/features/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. On the Mac App Store.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes, more in the gallery. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [How to open .md files on Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. Build your own theme in the browser, and browse the community gallery.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Make a theme with your agent](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes the community submitted for MarsDawn, filter them by scenario, and report a problem with one. Build your own in the browser, no install, no git.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Editor's reading notes](https://marsdawn.southern-light.dev/reading-notes/index.md): Six short notes on what the people building AI agents actually argue — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain and Andrew Ng — and what each one means for the person who has to read what such an agent hands back.
- [Reading notes: Anthropic](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [Reading notes: Chip Huyen](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [Reading notes: Lilian Weng](https://marsdawn.southern-light.dev/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng's widely cited 2023 survey describes an LLM agent as a brain plus planning, memory and tool use. What each part tends to leave behind for you to read, and the limitation she names in plans that don't adjust to surprises.
- [Reading notes: Harrison Chase](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [Reading notes: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [Reading notes: Andrew Ng](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
