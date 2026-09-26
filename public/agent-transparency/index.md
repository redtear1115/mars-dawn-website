# Anthropic says agents should be transparent — so who reads what they lay out?

In December 2024 Anthropic published “Building Effective Agents,” a guide for people who build AI agents. Its summary lists three principles, and one of them is transparency. This post is about the other end of that principle: once an agent lays out its steps, somebody has to read them.

**Transparency is something the agent does. Reading is something you do. Anthropic asks builders to show an agent's planning steps; for most people driving a coding agent, those steps arrive as a Markdown file that someone has to read at the right moment.**

## What the guide says

Erik S. and Barry Zhang sum up their advice like this:

> “When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.”

These are design principles for people who build agents, not instructions for the person using one. The principle asks for the steps to be shown. It doesn't say who reads them.

The same post describes what an agent does once it has a task: “Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.” And: “Agents can then pause for human feedback at checkpoints or when encountering blockers.” Look at the verbs, *potentially* and *can*. Checkpoints are described as something an agent can have, not something it must.

## Most of the checking isn't done by you

It's easy to overstate this, so here's what the guide actually puts first. The agent checks itself against the world: “During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.” In that sentence, ground truth means test results and tool output. It doesn't mean a person.

The guide is also direct about the risk: “The autonomous nature of agents means higher costs, and the potential for compounding errors.” Its answer is extensive testing in sandboxed environments, with guardrails. It doesn't say “read more carefully”.

A person does come in later, in the appendix on coding agents: “However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.” That sentence is about code. The gap it points at is familiar from any agent, though: a test can tell you something works, not that it's what you meant.

## Where the steps end up

**From here on this is our reading, not Anthropic's.**

If you use a coding agent day to day, its planning steps usually don't show up in a dashboard. They show up as files: `plan.md`, a task list with checkboxes, a progress file the agent keeps rewriting, a summary at the end. Transparency, from your side, means more to read.

Showing the steps is the agent's half of the deal. The other half is a person reading them when it matters: before the migration runs, before the branch merges, before “done” is accepted. An agent that lays everything out in a 600-line file nobody opens is transparent on paper and unsupervised in practice.

Harrison Chase made a related point in 2024, writing about how agent frameworks should work rather than about documents: “You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.” He was talking about tooling for the people building agents. If you're the one driving the agent, the plain file it keeps writing is often the part you can watch.

None of these authors mention MarsDawn, and none of them endorse it or any other Markdown tool.

## Why that read is harder than it looks

The file is long, and what matters is rarely near the top. The diagram that explains the change is Mermaid source, not a picture (seeing it drawn is covered in [How to view a Markdown file on a Mac](/view-markdown-on-mac/)). The agent may rewrite the file while you're halfway down. There's often more than one file, sometimes on different branches or worktrees. And when you do spot a problem, “the cache part looks off” leaves the agent guessing. The longer version of this is on [Reading what your agent hands back](/reading-agent-output/).

## Where MarsDawn fits, and where it doesn't

MarsDawn is a Mac app for this read. It doesn't make an agent more transparent, and it has no AI model inside: it won't summarize the plan or tell you whether it's right. What it does:

- **Long files:** View ▸ Show Sidebar (⌃⌘S) opens the Outline tab, which lists the headings. Click one to jump there.
- **Diagrams and math:** the source and the rendered page sit side by side (⌘2) and scroll together, with Mermaid and KaTeX drawn out. If a diagram is broken, the preview shows its source with the error underneath.
- **Rewritten while you read:** when the agent rewrites the file, MarsDawn reloads it and keeps your place, as long as you have no unsaved edits of your own.
- **Several files:** open the agent's folder with File ▸ Open Folder… (⇧⌘O). New files show up in the Files tab within about a second, and for a git checkout the header names the branch or worktree.
- **Pointing at a line:** Edit ▸ Copy Reference (⌥⌘C) copies your place as `docs/plan.md:42`, and Copy for AI (⌃⌥⌘C) adds the selected text under it, ready to paste into the agent's chat.

You still do the reading. MarsDawn keeps a long, changing file readable while you do.

## Try it

MarsDawn is coming soon to the Mac App Store. The free `marsdawn` command-line tool works today:

```
brew install redtear1115/tap/marsdawn
```

It exports Markdown to PDF without the app.

[Command Line](/cli/) · Know before you buy: [What MarsDawn doesn't do](/limits/)

## Next

- Why agent output is hard to read, and a checklist for it: [Reading what your agent hands back](/reading-agent-output/).
- The checklist, step by step with an example: [Reviewing an agent plan in five minutes](/reviewing-agent-plans/).
- Which documents different kinds of agents hand you: [Four agent design patterns and the documents each one hands you](/agent-design-patterns/).
- The short case for reading AI output at all: [Why AI output still needs a human reader](/reviewing-ai-output/).

## Sources

- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (quoted from the version online on 2026-09-26; the post now notes that much of the tooling it describes has changed since December 2024).
- Harrison Chase, “What is an agent?,” LangChain, June 28, 2024, archived copy: [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (the original address now shows a different 2026 article).

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
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
