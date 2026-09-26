# Anthropic 说 agent 要透明，那摊开的东西谁来读？

Anthropic 在 2024 年 12 月发表了〈Building Effective Agents〉，写给打造 AI agent 的人。文章的总结列出三个原则，其中一个是透明。这篇要谈的是这个原则的另一端：agent 把步骤摊开之后，总得有人去读。

**透明是 agent 要做到的事，读是你要做的事。Anthropic 要求开发者把 agent 的规划步骤摊开；对大多数在驱动 coding agent 的人来说，这些步骤最后会变成一份 Markdown 文件，要有人在对的时间点读它。**

## 指南里写了什么

Erik S. 与 Barry Zhang 在总结里这样写：

> “When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.”

（实作 agent 时，我们尽量遵守三个核心原则：让 agent 的设计保持简单；优先重视透明度，明确展示 agent 的规划步骤；通过完整的工具文件与测试，仔细打造 agent 与电脑之间的接口（ACI）。）

这些是写给开发 agent 的人的设计原则，不是给使用者的操作指示。原则要求把步骤摊开，但没有说谁来读。

同一篇也描述了 agent 拿到任务之后会做什么：“Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.”（任务明确之后，agent 会自己规划、独立运作，必要时回头找人类要更多信息或判断。）还有：“Agents can then pause for human feedback at checkpoints or when encountering blockers.”（Agent 可以在检查点或遇到阻碍时暂停，等待人类反馈。）注意用词：*potentially*（必要时）和 *can*（可以）。检查点是 agent 可以有的设计，不是一定要有。

## 大部分的检查，不是你在做

这里很容易讲过头，所以先看指南真正放在前面的是什么。agent 会拿外界的结果来检查自己：“During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.”（执行过程中，agent 必须在每一步从环境取得“ground truth”，例如工具呼叫的结果或程序执行的结果，用来评估自己的进度。）这句话里的 ground truth 指的是测试结果和工具输出，不是人。

指南对风险也讲得很直接：“The autonomous nature of agents means higher costs, and the potential for compounding errors.”（Agent 的自主性意味着更高的成本，以及错误不断累积的可能。）它给的解方是在沙盒环境里大量测试、加上适当的防护，并没有说“要读得更仔细”。

人真正出场，是在附录谈 coding agent 的段落：“However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.”（然而，自动化测试虽然有助于验证功能，但要确保解法符合更广泛的系统需求，人工审阅仍然至关重要。）这句讲的是代码。不过它点出的落差，用过 agent 的人都不陌生：测试能告诉你东西能动，不能告诉你那是不是你要的。

## 摊开的步骤，最后去了哪里

**以下是我们的解读，不是 Anthropic 的主张。**

如果你每天都在用 coding agent，它的规划步骤通常不会出现在什么仪表板上，而是变成文件：`plan.md`、一份有勾选框的待办清单、一个 agent 一直在改写的进度档，最后再来一份总结。从你这边看，透明的意思就是要读的东西变多了。

把步骤摊开，是 agent 那一半的责任。另一半，是有人在关键时刻读它：数据库迁移执行之前、分支合并之前、接受“做完了”之前。一个 agent 把所有东西都写进一份 600 行、没人打开的文件，纸面上很透明，实际上没人在看。

Harrison Chase 在 2024 年也讲过类似的话，不过他谈的是 agent 框架该怎么设计，不是文件：“You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”（你会希望能观察系统内部发生了什么，因为它实际采取的步骤事先可能无法得知。）他讲的是给开发 agent 的人用的工具。如果你是驱动 agent 的那个人，它一直在写的那份纯文字档，常常就是你看得到的部分。

以上几位作者都没有提到 MarsDawn，也没有推荐 MarsDawn 或任何 Markdown 工具。

## 比看起来难读

文件很长，重要的地方很少在最上面。说明这次改动的那张图，是一段 Mermaid 原始码，不是图（想在 Mac 上看到排好的样子，可以先看[在 Mac 上怎么看 Markdown 文件](/zh-hans/view-markdown-on-mac/)）。你读到一半，agent 可能正在改写它。文件常常不只一份，有时还分散在不同的分支或 worktree。等你真的找到问题，说“缓存那段怪怪的”，agent 只能用猜的。完整的说明在[读懂 agent 交回来的 Markdown](/zh-hans/reading-agent-output/)。

## MarsDawn 帮得上、帮不上的地方

MarsDawn 是为这种阅读做的 Mac app。它不会让 agent 变得更透明，里面也没有 AI 模型：它不会帮你摘要计划，也不会告诉你计划对不对。它做的是：

- **文件很长：**“显示方式 ▸ 显示侧边栏”（⌃⌘S）打开“大纲”标签页，列出所有标题，点一下就跳过去。
- **图表和数学式：**原始码和排好的页面并排（⌘2），两边一起卷动，Mermaid 和 KaTeX 直接画出来。图表写错时，预览会显示它的原始码，下方附上错误信息。
- **读到一半被改写：**agent 改写文件时，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。
- **好几个文件：**用“文件 ▸ 打开文件夹⋯”（⇧⌘O）打开 agent 工作的文件夹，新文件大约一秒内就会出现在“文件”标签页；如果是 git 检出，清单上方会标出分支或工作树。
- **指出是哪一行：**“编辑 ▸ 拷贝引用”（⌥⌘C）把目前位置拷贝成 `docs/plan.md:42`，“拷贝给 AI”（⌃⌥⌘C）会在下面附上你选取的文字，直接贴给 agent 就好。

读的人还是你。MarsDawn 负责让一份又长又会变的文件，在你读的时候保持好读。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 输出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- agent 的产出为什么难读，以及一份检查清单：[读懂 agent 交回来的 Markdown](/zh-hans/reading-agent-output/)。
- 那份清单一步一步来，附实际例子：[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)。
- 不同类型的 agent 会交给你什么文件：[四种 agent 设计模式，各自会交给你什么文件](/zh-hans/agent-design-patterns/)。
- 为什么 AI 写的东西需要人读，短一点的版本：[为什么 AI 写的东西还是需要人读过](/zh-hans/reviewing-ai-output/)。

## 资料来源

- Erik S. 与 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) （引文依 2026-09-26 的线上版本；该文现已注明，文中提到的工具生态自 2024 年 12 月以来已有很多改变）
- Harrison Chase，〈What is an agent?〉，LangChain，2024 年 6 月 28 日，存档版本：[http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) （原网址现在显示的是 2026 年的另一篇文章）

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂 agent 交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [审 agent 计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [agent 设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能输出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
