# Move from HackMD to your Mac

Your notes are already Markdown, so there's nothing to convert. Pick a route below by how much you're moving. Images need their own step, so read that section before you delete anything on HackMD.

We tested this on a free HackMD account in November 2026. HackMD can change, and we didn't test paid plans or team workspaces.

| You want to | Take this route |
|---|---|
| Move all your notes | Download all notes |
| Move notes that are already on GitHub | Clone the repo |
| Move one or two notes | Download one note |

## Download all notes

HackMD's note settings have Download all notes, for personal and team workspaces. You get one .zip with a .md file for each note, named after its title.

- Folders aren't kept. Every note lands at the top level.
- Images aren't included. The .md files still point to them by URL.
- The option to include title and tags is on by default and adds a front matter block to each note. Turn it off to get each note exactly as written.

Unzip it, then choose File ▸ Open Folder… in MarsDawn to open that folder.

## Clone the repo

HackMD's GitHub sync links one note to one file, so a note you've pushed is already in the repo. Clone it and open the folder with File ▸ Open Folder…. The sidebar shows the repo and its branch.

If your notes aren't on GitHub yet, you don't need to start for this move. Each note has to be linked on its own, and the free plan allows 20 pushes a month. On a free personal account we found no way to push a whole workspace at once.

After the move, treat the repo as the original. A push from HackMD replaces what's on GitHub, even if GitHub has newer content, and it doesn't warn you.

## Download one note

The note menu downloads a note as .md or .html. Choose .md and open the file in MarsDawn.

## Images

Images you uploaded to HackMD live at `https://hackmd.io/_uploads/...`. Who can see them follows the note's permission.

| Your note is | What happens on your Mac | What to do |
|---|---|---|
| Public | The image loads from HackMD | Click Load Images in the preview, or turn on Settings ▸ Images ▸ Load remote images automatically |
| Private | The image returns an error, because MarsDawn isn't signed in to HackMD | Save the image from a signed-in browser, put it next to the .md file and change the path. Or make the note public, if everyone may read it |

- **Older notes** may use `i.imgur.com` addresses instead.
- **Deleting a note deletes its images.** Their addresses stop working, so move the images first.

If MarsDawn can't reach an image next to your file, use the button in the preview to give it access to the folder.

## How your notes will look

Most of HackMD's syntax reads the same: `==highlight==`, `^superscript^`, `~subscript~`, `[TOC]`, image sizes such as `=300x200`, Mermaid and KaTeX. `{%youtube %}` shows as a link. To keep every line break as HackMD does, turn on Settings ▸ Appearance ▸ Keep single line breaks.

`:::` blocks work too. `:::info`, `:::success`, `:::warning` and `:::danger` show as blocks with a colored bar and a heading (Note, Tip, Warning or Caution), or your own heading if you write one after the name. `:::spoiler` shows as a collapsible section that opens when you click it. A `:::` block with any other name, or without its closing `:::`, shows as you typed it.

A few things look different:

- `++inserted++` and emoji codes such as `:sparkles:` show as you typed them.
- `{%hackmd id %}` isn't expanded.
- `<i class="fa ...">` icons don't appear.

## For scripts: hackmd-cli

`hackmd-cli` has no command that exports everything at once. It exports one note and prints it, so you list your notes first and loop over them. You need Node.js, `jq` and an API token from your HackMD settings. If you don't need a script, Download all notes is simpler.

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<your token>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **Folders don't come across.** The note list doesn't say which folder a note is in, so every file lands in one place.
- **Images stay as `hackmd.io` links.** Handle them as in the Images section above.
- **File names are note IDs,** not titles.
- **The free plan allows 400 API calls every 30 days.** This uses one call for the list and one for each note.

We tried this on an account with only a few notes, so we don't know how a very long list behaves. Delete the token in your HackMD settings when you're done.

## Writing together

MarsDawn has no shared editing. If you need to write together live, keep using HackMD. If your team keeps documents in git, each person can open the same repo in their own MarsDawn and finish the document together. See Review documents as a team, with git.

## Questions

### Can I download all my HackMD notes at once?

Yes. Download all notes gives you one .zip of .md files. It doesn't keep folders or include images.

### Why are my images missing in MarsDawn?

MarsDawn holds back web images until you click Load Images. If the note is private, the image can't load at all, so save it next to your file.

### Do I have to leave HackMD?

No. HackMD stays the better choice for writing together. MarsDawn is for reading and reviewing on your Mac.

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review your agent's Markdown, JSON and YAML natively on Mac: live preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac editor for Markdown, JSON and YAML: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings and records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [Print & PDF](https://marsdawn.southern-light.dev/pdf/index.md): Preview your Markdown, then print it or save it as a PDF on your Mac, in Document, Handbook or Handout layout, with diagrams and code colors intact.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no editing on iPhone or iPad, no plugins, no accounts. Themes, but no custom CSS. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [How to open .md files on Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): MarsDawn's Quick Look renders Markdown in Finder when you press Space, with Mermaid, KaTeX and highlighted code. It keeps working after the trial ends.
- [Copy for AI](https://marsdawn.southern-light.dev/copy-for-ai/index.md): Copy selected text with its file path and line numbers, then paste it into Claude Code or any agent. MarsDawn does this on your Mac, with no IDE or plugin.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MarsDawn compared: VS Code preview, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026, except MarsDawn's PDF cell, updated on 7 November 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [Best Markdown viewer for Mac (2026)](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Themes](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Make a theme with your agent](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes for MarsDawn, each reviewed by the developer, filter them by scenario, and report a problem with one. Build your own in the browser.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [Roadmap](https://marsdawn.southern-light.dev/roadmap/index.md): What's in progress and what's next for MarsDawn on Mac, iPhone and iPad, by version. No dates, and unscheduled ideas are marked.
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
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/from-hackmd/index.md): Lade deine HackMD-Notizen als .md herunter und lies sie in MarsDawn auf dem Mac. Alle Notizen herunterladen, ein GitHub-Repository nutzen und Bilder retten.
- [Français](https://marsdawn.southern-light.dev/fr/from-hackmd/index.md): Téléchargez vos notes HackMD en .md et lisez-les dans MarsDawn sur votre Mac. Comment tout télécharger, partir d’un dépôt GitHub et garder vos images.
- [Español](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
- [한국어](https://marsdawn.southern-light.dev/ko/from-hackmd/index.md): HackMD 노트를 .md로 내려받아 Mac의 MarsDawn에서 읽는 방법입니다. 모든 노트 다운로드, GitHub 저장소에서 옮기기, 이미지 처리 방법을 정리했습니다.
