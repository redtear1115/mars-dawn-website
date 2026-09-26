# Reviewing an agent plan in five minutes

Your agent has written a plan and is waiting for a go-ahead. You have five minutes, not an hour. Here's a way to use them that works in any editor, even a plain text one. MarsDawn helps with some of the steps, and we'll say which. It doesn't help with the most important one.

**Don't read the plan top to bottom. Check its shape, check one claim, find what can't be undone, look at the diagrams and the scope, then write feedback the agent can act on. Six steps, about five minutes.**

## Why bother before it runs

Chip Huyen, explaining why planning should be kept apart from execution, puts the cost plainly: “Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.” Our addition: a plan is the cheapest place to catch a mistake. Fixing a line in `plan.md` costs a sentence. Fixing what the agent did after it ran costs an afternoon.

## The example

You asked an agent to move user avatars to object storage without breaking existing links. It hands back this:

```
# Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. ✅ done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.
```

It reads fine. It would also delete every avatar before copying any of them.

## The six steps

**1. Read only the headings.** *(about a minute)* Does the outline match what you asked for? A missing section usually means missing work. Here: Goal, Steps, Status. You asked for existing links to keep working, and there's no heading about old links or about undoing the change. That's your first comment.

From a terminal, `grep -n '^#' plan.md` prints just the headings, and most editors can show an outline too. In MarsDawn, the Outline tab in the sidebar (View ▸ Show Sidebar, ⌃⌘S) lists them, and clicking one jumps there.

**2. Find every place that says something is done, passing or verified, and check one yourself.** *(about a minute)* Open the file, run the test, count the rows. Chip Huyen describes a failure where “The agent is convinced that it’s accomplished a task when it hasn’t.” In her example, an agent asked to put 50 people in 30 hotel rooms places 40 and insists it's finished.

```
grep -n -i -E 'done|pass|verified|✅' plan.md
```

Here that finds “✅ done” and “All tests pass.” Which tests? Do any of them touch avatars? Run them, or ask. MarsDawn can't do this step for you. Nothing can but you.

**3. Look for steps that can't be undone.** *(about a minute)* Deleting data, migrations, force-pushes, anything that sends, pays or publishes. Those wait for your explicit yes. Chip Huyen describes the same idea from the system's side: “If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.” Here, step 4 deletes the originals, and it comes before step 5, the copy.

**4. Read the diagrams rendered, and check each arrow against the text.** A flowchart that says “copy → verify → delete” while the steps say otherwise is a finding. This plan has no diagram, so skip it today. When there is one, look at the picture, not the Mermaid source: many editors have a preview, and [How to view a Markdown file on a Mac](/view-markdown-on-mac/) and [Viewing Markdown elsewhere](/vs/markdown-preview-tools/) cover the options. In MarsDawn the rendered diagram sits beside its source (⌘2), and a broken diagram shows its source with the error underneath, which is worth a comment of its own.

**5. List the files and systems the plan touches, and ask about anything you didn't request.** *(steps 4 and 5 together, about a minute)* Here: the storage config, the templates, a folder on the server, a bucket. Who can read the bucket? You didn't say it should be public. If you opened the agent's working folder in MarsDawn (File ▸ Open Folder…, ⇧⌘O), new files it writes show up in the Files tab within about a second, and the header names the git branch or worktree, so you know which checkout you're reviewing.

**6. Write feedback as place, problem, fix, one problem per line.** *(the last minute)*

```
plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.
```

Any editor with line numbers will do. In MarsDawn, Edit ▸ Copy Reference (⌥⌘C) copies your place as `plan.md:10`, and Copy for AI (⌃⌥⌘C) adds the selected text under it.

## If you have one minute

Do step 2. That's where an agent that thinks it's finished gets caught.

## When five minutes isn't enough

Sometimes you can't tell whether a step is right, because it's outside what you know. Jess Ou, in LangChain's 2026 explainer on agents, puts it in two sentences: “Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.” Our takeaway: if you can't judge a step, that isn't a reason to approve it faster. It's a reason to ask someone who can.

## What MarsDawn does here, and what it doesn't

MarsDawn has no AI model inside. It won't find the problems in this plan, and it doesn't do steps 2 or 3. It keeps the file readable while you work: the outline for step 1, rendered diagrams for step 4, the Files tab for step 5, line references for step 6. And if the agent revises the plan while you're reading, MarsDawn reloads it and keeps your place, as long as you have no unsaved edits of your own.

Once the plan is settled and someone else needs to see it, [Sharing exported PDFs](/sharing-exported-pdfs/) and [Markdown to PDF](/markdown-to-pdf/) cover handing it over as a PDF.

## Try it

MarsDawn is coming soon to the Mac App Store. The free `marsdawn` command-line tool works today:

```
brew install redtear1115/tap/marsdawn
```

It exports Markdown to PDF without the app.

[Command Line](/cli/) · Know before you buy: [What MarsDawn doesn't do](/limits/)

## Next

- Why agent output is hard to read in the first place: [Reading what your agent hands back](/reading-agent-output/).
- Why agents lay their plans out at all: [Anthropic says agents should be transparent — so who reads what they lay out?](/agent-transparency/)
- Plans aren't the only thing agents hand back: [Four agent design patterns and the documents each one hands you](/agent-design-patterns/).

## Sources

- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou, “What is an AI agent?,” LangChain, July 31, 2026: [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

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
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Preview themes and PDF export](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
