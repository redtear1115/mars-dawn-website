# Four agent design patterns and the documents each one hands you

In March 2024, Andrew Ng used his newsletter, The Batch, to describe four design patterns for AI agents: reflection, tool use, planning and multi-agent collaboration. They're usually discussed from the builder's side, as ways to get better results out of a model. This post looks from the other side. If you use an agent built on one of these patterns, what lands in your folder, and what should you read first?

**The four patterns are Andrew Ng's. Which documents each one tends to hand you, and what to check in them, is our own inference. He doesn't write about either, and he doesn't argue for human review in this series.**

## The four patterns, briefly

Ng describes them in “Agentic Design Patterns Part 1.” In short: with **reflection**, the model looks over its own work and improves it. With **tool use**, it can call tools such as web search or code execution. With **planning**, it comes up with a multistep plan and carries it out. With **multi-agent collaboration**, several agents split up the work and discuss it.

In Part 1 he shows the payoff with a coding benchmark, HumanEval, using results his team gathered from several research groups: “GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.” Those numbers are about one coding benchmark, and 95.1% is a best case (“up to”). They show agent workflows can improve output. They don't say anything about who checks it.

**From here on, the documents and the checks are our reading, not Ng's.** Real agents mix patterns, too. A coding agent may plan, run tools and review its own work in one session, so you'll often get all four kinds of file.

## 1. Reflection: a draft that has already reviewed itself

Ng's post on reflection frames it as automating the feedback a person would otherwise give: “What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?”

**What it tends to hand you:** a revised document, sometimes with a self-review section or lines like “double-checked the edge cases.”

**What to check:** the result against *your* request, not against the agent's own critique. Self-review can go wrong in its own way. Chip Huyen: “An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it’s accomplished a task when it hasn’t.” Lilian Weng, writing on her blog Lil’Log in June 2023 while at OpenAI, about models of that time: “The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.” (In the study she was describing, an LLM's evaluation of the results and human experts' evaluation didn't agree.) If it says “verified,” check one thing yourself.

## 2. Tool use: a report of what ran

**What it tends to hand you:** a summary of what the agent ran or searched and what came back. “Ran the test suite: all passing.” A results table. Links it found.

Anthropic's guide describes tool results as the agent's own check on itself: “During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.” That check happens inside the agent. What reaches you is the agent's retelling of it.

**What to check:** that each claim traces back to output you can see. Match one number in the summary to the real output. Open one of the links.

## 3. Planning: `plan.md`

**What it tends to hand you:** a plan, a spec, a task list with checkboxes the agent ticks as it goes.

Ng is candid about this pattern in Part 4:

> “On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.”

He's optimistic, too: “But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.”

**What to check:** the plan before it runs, using [the five-minute review](/reviewing-agent-plans/): shape, one claim, steps that can't be undone, diagrams, scope. If the agent rewrites the plan midway, compare it with the version you approved; if it's in git, `git diff plan.md` shows what changed. In MarsDawn, the Outline tab shows a long plan's shape, and a rewritten plan reloads without losing your place, as long as you have no unsaved edits of your own.

## 4. Multi-agent collaboration: several files, several authors

**What it tends to hand you:** a spec from one agent, implementation notes from another, a review from a third, and summaries passed between them. Sometimes each works in its own branch or worktree.

**What to check:** the handoffs. Where one agent summarizes another's work, look for a requirement that didn't make it across. Look for two files that disagree, and decide which one is the source of truth before anyone builds on the other. In MarsDawn, open the shared folder with File ▸ Open Folder… (⇧⌘O): new files show up in the Files tab within about a second as the agents write them, and for a git checkout the header names the branch or worktree, so two windows on the same file name from different branches don't look alike. When the result has to go to people who don't read Markdown, [Sharing exported PDFs](/sharing-exported-pdfs/) covers that step.

## At a glance

| Pattern (Ng) | What it tends to hand you (our inference) | Read first (our suggestion) |
|---|---|---|
| Reflection | A revised draft, maybe with a self-review | The result against your own request; check one “verified” |
| Tool use | A report of what ran and what came back | One claim traced to real output |
| Planning | `plan.md`, a spec, a task list | The five-minute review, before it runs |
| Multi-agent collaboration | Several files from several agents, maybe on several branches | The handoffs, and which file is the source of truth |

None of the authors quoted here mention MarsDawn, and none of them endorse it or any other Markdown tool. MarsDawn has no AI model inside: it doesn't know which pattern produced a file, and it won't do these checks for you. It keeps the files readable while you do.

## Try it

MarsDawn is coming soon to the Mac App Store. The free `marsdawn` command-line tool works today:

```
brew install redtear1115/tap/marsdawn
```

It exports Markdown to PDF without the app: see [Markdown to PDF](/markdown-to-pdf/).

[Command Line](/cli/) · Know before you buy: [What MarsDawn doesn't do](/limits/)

## Next

- Why agent output is hard to read, and a checklist for it: [Reading what your agent hands back](/reading-agent-output/).
- The planning check in full: [Reviewing an agent plan in five minutes](/reviewing-agent-plans/).
- What transparency does and doesn't ask of you: [Anthropic says agents should be transparent — so who reads what they lay out?](/agent-transparency/)

## Sources

- Andrew Ng, “Agentic Design Patterns Part 1,” The Batch, March 20, 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, “Agentic Design Patterns Part 2, Reflection,” The Batch, March 27, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, “LLM Powered Autonomous Agents,” Lil’Log, June 23, 2023: [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (quoted from the version online on 2026-09-26).

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
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
