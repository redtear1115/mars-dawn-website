# Jess Ou 的评测流程，里面还留给你的那一步

**2026 年 7 月，LangChain 在 Harrison Chase 2024 年那篇《What is an agent?》原本的网址上，发表了一篇新的《What is an AI agent?》——这次是 Jess Ou 写的，定义几乎和他当年那句一字不差。她这篇大部分在谈他那篇没谈到的东西：一整套自动评测 agent 的流程。她的文章很坦白地讲清楚，这套流程哪里还需要人，哪里已经不需要了。**

## 这篇文章主张什么

Ou 的定义几乎就是 Chase 那句话的回声：

> “An AI agent is a system that uses a large language model to decide the control flow of an application.”

（AI agent 是用大型语言模型来决定应用程序控制流程的系统。“控制流程”一样是指接下来要跑哪一步。）

接下来她描述了 LangChain 的 Agent Development Lifecycle：build、test、deploy、monitor 四个阶段，以及一套不靠人读每一次执行记录就能检查 agent 表现的分层做法：online evals 对正式流量的 trace（一次执行的记录）取样，抓退步；offline evals 跑在整理好的数据集上，在变更上线前先抓出问题；“LLM-as-a-judge”则是用一个人事先定好的标准，去替一次执行的输出打分数，而且规模是人工审阅做不到的。她也直接讲清楚人在这套流程里还该站在哪里：

> “For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.”

（对于敏感或不可逆的动作，我们建议用 human-in-the-loop 的控制机制，暂停 agent，等待核准、修改、拒绝或澄清。）

她也有一句话讲的是不管流程多完善都省不掉的判断：“Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.”（无法评估的判断，就不要外包出去。如果你自己认不出正确答案，agent 也认不出来。）《[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)》已经拿这句话建过讨论，这篇不重复。Ou 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。她也从来没提过 Chase 这个人；把这两篇文章连在一起的，是 LangChain 在 2026 年把她这篇发表在 Chase 2024 年那篇文章原本的网址上，而且定义几乎一模一样——这是我们自己的观察，不是她的主张。

## 以下是我们的解读，不是 Ou 的

Ou 讲的 human-in-the-loop，是在特定动作执行前先拦下来——暂停一个 write 动作、等人核准，跟 Chip Huyen 那个 read-only／write action 的分法，其实是同一件事的不同角度——不是读一份已经完成的报告。仔细看她整套流程，大部分设计是要把人从例行检查里拿掉，而不是加进去：online evals、offline evals 和 LLM-as-a-judge，存在的目的就是让团队不用手动看每一次的执行记录。这不是在批评这篇文章——这本来就是她讲明的目标，在正式营运的规模下也很合理。但这代表你亲自动手做的审阅——直接读一份 agent 交给你的计划或报告——正好就是她这套流程想要减少、而不是取代的那种检查。她自己那句判断的话，替这种减少画了一条底线：你自己读了都认不出对错的地方，还是得自己读过。

## MarsDawn 帮得上、帮不上的地方

MarsDawn 不是评测流程，里面也没有 AI 模型——它不会替一次执行记录打分数，不会跑 LLM-as-a-judge，也不会替你决定哪些动作敏感到要先暂停。它做的，正是她这套流程还留给人的那个时刻：直接把东西读过一遍。侧边栏（“显示 ▸ 显示边栏”，⌃⌘S）的“大纲”标签页列出一份长报告的所有标题；源代码和排好的预览并排（⌘2），Mermaid 和 KaTeX 都直接画出来；“编辑 ▸ 拷贝引用”（⌥⌘C）搭配“拷贝给 AI”（⌃⌥⌘C），让你把一次抽查变成 agent 看得懂、改得动的反馈。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 导出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- 部分建立在她这句“别外包判断”上的完整检查清单：《[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)》
- 这个定义最早在 2024 年是怎么写的：《[Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看](/zh-hans/reading-notes/harrison-chase-what-is-an-agent/)》
- 回到系列索引：《[编者的阅读笔记](/zh-hans/reading-notes/)》

## 资料来源

- Jess Ou，《What is an AI agent?》，LangChain，2026 年 7 月 31 日：[https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent) （2026-09-26 读取并引用）

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
- [阅读笔记：Chip Huyen](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把 agent 的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM agent 描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
