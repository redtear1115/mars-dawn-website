# Chip Huyen 的 read-only／write action 分类，核准前为什么要看它

**Chip Huyen 在 2025 年 1 月发表的《Agents》，从教科书式的定义出发，一路写到一个更具体的分类：agent 的动作分成“只是看世界”跟“会改变世界”两种。这个分类，正好可以用来判断你手上五分钟该花在计划里的哪几行。**

## 这篇文章主张什么

Huyen 开门见山：

> “An agent is anything that can perceive its environment and act upon that environment.”

（Agent 是任何能感知环境、并对环境采取行动的东西。）

从这里出发，她说明 agent 需要什么：一个可以行动的环境，还有一组决定它能做什么的工具——她称之为“tool inventory”。她点出一个分界：只是让 agent 能感知环境的动作是“read-only actions”，能让它对环境采取行动的动作是“write actions”。对于后者，她讲得很直接：

> “Write actions enable a system to do more.”

（Write action 能让系统做到更多事。）

但她也直接点出第二种动作带来的风险：“the prospect of giving AI the ability to automatically alter our lives is frightening”（让 AI 有能力自动改变我们的生活，这个念头令人不安），照她的说法：“you shouldn’t allow an unreliable AI to initiate bank transfers”（不该让一个不可靠的 AI 去发起银行转账）。她对 agent 最难搞定的那一块也讲得很坦白：

> “If you’ve ever been in any planning meeting, you know that planning is hard.”

（如果你参加过任何一场规划会议，就知道规划有多难。）

Huyen 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。《[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)》已经引用她这篇文章里三句话：执行前不监督的代价、以为自己做完其实没做完的 agent，还有第三步里她说系统遇到有风险的操作“可以在执行前要求人类明确核准”那一句。这篇不重复这些引文；还没看过那篇的话，下面有链接。

## 以下是我们的解读，不是 Huyen 的

Huyen 的 read-only／write action 分法，不是写给审阅用的建议，而是一种给工具分类的方式。但它是一个很好用的通用判断法，可以用来抓出《五分钟审完一份 agent 计划》第三步已经要你放慢脚步的那种有风险的操作：读一个文件、跑一次搜索、列一下目录，这些是 read-only，做错了顶多重跑一次；删数据、force push、合并分支、发信、扣款，这些是 write action——照她的说法，这种一旦做错就是“令人不安”的那种，而且等你读到 agent 的报告时，它可能已经做完了。她说连人坐在一起开会都觉得规划很难，这也提醒我们别对一份计划的精确度期待过高：计划读起来自信，不代表它是对的。

## MarsDawn 帮得上、帮不上的地方

MarsDawn 没办法帮你判断计划里哪一步是 read-only、哪一步是 write——这是文字没标出来的判断，app 里的任何东西都不会替你读出语义。它里面也没有 AI 模型：不会帮你标出风险高的那一行，不会替你跑“规划到底有多难”的检查，也不会给计划打分数。它做的是让文件在你自己做判断的时候保持好读：侧边栏（“显示 ▸ 显示边栏”，⌃⌘S）的“大纲”标签页让你先看过计划的架构，再逐行读；源代码和排好的页面并排（⌘2），步骤图就不会卡在 Mermaid 源代码那个阶段；“编辑 ▸ 拷贝引用”（⌥⌘C）把你的位置拷贝成 `plan.md:10`，你一发现顺序不对的 write 动作，马上就能贴出去当反馈。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 导出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- 用同一篇文章建出来的完整六步骤五分钟检查清单：《[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)》
- agent 的产出为什么普遍难读：《[读懂 agent 交回来的 Markdown](/zh-hans/reading-agent-output/)》
- 回到系列索引：《[编者的阅读笔记](/zh-hans/reading-notes/)》

## 资料来源

- Chip Huyen，《Agents》，2025 年 1 月 7 日：[https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html) （2026-09-26 读取并引用）

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 导出。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
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
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [审 agent 计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [agent 设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [编者的阅读笔记](https://marsdawn.southern-light.dev/zh-hans/reading-notes/index.md): 六篇短笔记，谈打造 AI agent 的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读 agent 交回来的东西”的人分别意味着什么。
- [阅读笔记：Anthropic](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和 agent 分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM agent 描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章裡，把 agent 的動作分成 read-only 和 write action 兩種。這個分法為什麼是核準計畫前，快速拓出該多看一眼的那一行的好方法。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
