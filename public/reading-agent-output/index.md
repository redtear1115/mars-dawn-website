# Your agent's work comes back as a Markdown file.

You ask a coding agent to plan a migration, write a spec or chase a bug. It works on its own for a while, then hands you a file: `plan.md`, `SPEC.md`, a progress report, a research summary. As far as you can check the work, that file is the work.

**Whether the agent got it right, you find out by reading what it hands back. MarsDawn is a Mac app for that read.**

## What people who build agents say

Quoted as written; our reading follows.

- Anthropic's “Building Effective Agents” (Erik S. and Barry Zhang, December 2024) gives three core principles for building agents. One is “Prioritize transparency by explicitly showing the agent’s planning steps.” It's written for people who build agents. From your side, that transparency is the plan you end up reading.
- The same post: “Agents can then pause for human feedback at checkpoints or when encountering blockers.” Note the verb: *can*.
- Chip Huyen, in “Agents” (January 2025), on why planning should be kept apart from execution: “Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.” She also describes a failure where “The agent is convinced that it’s accomplished a task when it hasn’t.” Asked to put 50 people in 30 hotel rooms, it places 40 and insists it's done.
- Andrew Ng, on the planning design pattern in The Batch (April 2024): “On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results.” That's a point about predictability, not a call for human review, and he expects planning to improve quickly.

**Our inference, not theirs:** if an agent lays out its plan and stops at checkpoints, somebody reads that plan at the checkpoint, and usually that's you. If an agent can think it's finished when it isn't, its “done” report needs a reader too. None of these authors mention MarsDawn or endorse it or any other Markdown tool.

## Why it's a harder read than it looks

The file is long, and the part that matters is rarely near the top. It has Mermaid diagrams and formulas that are hard to follow as source. The agent may still be rewriting it while you're halfway down. It's often one of several files, sometimes across branches or worktrees. And when you find a problem, “the cache part looks off” leaves the agent guessing; “`docs/plan.md:42` drops the old table before the backfill finishes” doesn't.

## Where MarsDawn helps

- **Long files:** the Outline tab in the sidebar (⌃⌘S) lists the headings. Click one and both panes jump there.
- **Diagrams and math:** Mermaid and KaTeX are drawn in the preview beside the source (⌘2), and the two panes scroll together.
- **Rewritten while you read:** when the agent rewrites the file, MarsDawn reloads it and keeps your place, as long as you have no unsaved edits of your own.
- **Several files:** open the agent's folder with File ▸ Open Folder… (⇧⌘O). New files show up in the Files tab within about a second, and for a git checkout the header names the branch or worktree.
- **Exact feedback:** Edit ▸ Copy Reference (⌥⌘C) copies your place as `docs/plan.md:42`. Copy for AI (⌃⌥⌘C) adds the selected text under it. Paste either into the agent's chat.

Two more for the loop: an agent can run `marsdawn open plan.md:42` to open the file in MarsDawn at line 42, the line it wants you to see first, and a reviewed file exports to PDF from the app or with the free `marsdawn export` command.

MarsDawn has no AI model inside. It won't summarize the plan, grade it or tell you what's wrong. You do the reading; it keeps a long, changing file readable and lets you point at the exact line.

## Review an agent's plan in five minutes

This works in any editor.

1. Read only the headings. Does the outline match what you asked for? A missing section usually means missing work.
2. Find every place that says something is done, passing or verified, and check one yourself: open the file, run the test, count the rows.
3. Look for steps that can't be undone: deleting data, migrations, force-pushes, anything that sends, pays or publishes. Those wait for your explicit yes.
4. Read the diagrams rendered, and check each arrow against the text.
5. List the files and systems the plan touches. Ask about anything you didn't request before it runs.
6. Write feedback as place, problem, fix: “`plan.md:88`: the backfill runs after the drop. Swap steps 4 and 5.” One problem per line.

Short on time? Do step 2. That's where an agent that thinks it's finished gets caught. The long version, with a worked example: [Reviewing an agent plan in five minutes](/reviewing-agent-plans/).

## Try it

MarsDawn is coming soon to the Mac App Store. The free `marsdawn` command-line tool works today:

```
brew install redtear1115/tap/marsdawn
```

It exports Markdown to PDF without the app. Once the app is out, `marsdawn open` lets your agent open files in it for you.

[Command Line](/cli/) · [marsdawn for agents](/cli/agents/) · Know before you buy: [What MarsDawn doesn't do](/limits/)

## Next

- The short case for reading AI output at all: [Why AI output still needs a human reader](/reviewing-ai-output/).
- Keeping the agent's context small while you review: [token-efficient review](/token-efficient-review/).
- Why agents lay their plans out at all: [Anthropic says agents should be transparent — so who reads what they lay out?](/agent-transparency/)
- The checklist above, step by step with an example: [Reviewing an agent plan in five minutes](/reviewing-agent-plans/).
- Which documents different kinds of agents hand you: [Four agent design patterns and the documents each one hands you](/agent-design-patterns/).

## Sources

- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (quoted from the version online on 2026-09-26; the post now notes that much of the tooling it describes has changed since December 2024).
- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

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
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
