# Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看

**2024 年 6 月，LangChain 的 Harrison Chase 用一个看似简单的问题——“什么是 agent？”——开启了一个新系列，给出一个技术定义，还有一条“agentic”程度的光谱。他主张：系统在这条光谱上愈往自主那端走，就愈需要能在它运作时看得到里面发生了什么。**

## 这篇文章主张什么

Chase 自己给的定义，还先承认这比大部分人的定义更技术性、涵盖的范围也更广：

> “An agent is a system that uses an LLM to decide the control flow of an application.”

（Agent 是用 LLM 来决定应用程序控制流程的系统。“控制流程”指的就是程序接下来要跑哪一步。）

他马上承认这个定义并不完美——一个只是让 LLM 在两条路径之间做选择的简单系统，照他的定义算是 agent，但不太符合大部分人对“agent”的直觉想象。与其去争谁才是“真正的”agent，他采用了 Andrew Ng 的说法——他引用 Ng 的一则推文，并注明出自 Ng：“rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic”（与其去争该把哪些工作算进“真正的”agent、哪些不算，不如承认系统可以有不同程度的 agentic）。Chase 自己的回应是：“I really agree with this viewpoint and I think Andrew expressed it nicely”（我很认同这个看法，觉得 Andrew 讲得很好）。从这里出发：系统愈由 LLM 决定该怎么运作，就愈“agentic”，从固定的路由器，到状态机，一路到能自己建立并记住工具的完全自主 agent。他从这条光谱出发，提出一个实际的主张：系统愈 agentic，某些基础设施就愈重要，其中最重要的是可观测性：

> “You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”

（你会希望能观察系统内部发生了什么，因为它实际采取的步骤事先可能无法得知。）

他还进一步主张不只要看，还要能介入：你也会希望能在某个时间点，修改一个正在运作的 agent 的状态或指示，如果它偏离了原本设定的路径，就把它拉回来。Chase 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。

## 以下是我们的解读，不是 Chase 的

Chase 谈的是给打造 agent 框架的人用的工具——他点名了 LangGraph 和 LangSmith——不是给读一份完成文件的人看的。但他这条光谱，给了一个很实用的方式，让你在开始读之前先估量一下手上这份东西：产出它的系统愈 agentic，你就愈不该预期它的步骤从最初的 prompt 就能猜得到，手上这份文件也就愈值得当成“实际发生了什么”的记录来读，而不是“原本该发生什么”的记录。他说的“观察系统内部”，讲的是一个正在运作的系统的内部状态——trace（一次执行过程中，agent 做过的所有事的记录）、中间步骤、工具调用——不是事后读一份 Markdown 计划。但他给的理由——步骤事先无法得知——用在 agent 做完之后交给你的那份文件上，一样说得通：如果一开始步骤就无法预测，那份做完之后的报告，就是唯一还能检查它们的地方。

## MarsDawn 帮得上、帮不上的地方

MarsDawn 不会去观察一个正在运作的 agent 的内部——它里面没有 AI 模型，也没有连到产生这份文件的任何框架，所以没办法告诉你某个 agent 在 Chase 的光谱上落在哪里。它处理的是事后落到你手上的那份文件：侧边栏（“显示 ▸ 显示边栏”，⌃⌘S）的“大纲”标签页让你看清楚一份长报告的架构；原始码和排好的预览并排（⌘2），处理图表和数学式；agent 改写文件时会重新加载，停在你原本读到的位置，前提是你自己没有未保存的修改——这就是“盯着还在动的东西”的文件版本。“编辑 ▸ 拷贝引用”（⌥⌘C）和“拷贝给 AI”（⌃⌥⌘C）让你精准指出哪一步走偏了，等于是文件版的“把跑偏的 agent 拉回正轨”。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 输出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- 这个系列对透明和检查点更完整的讨论：《[Anthropic 说 agent 要透明，那摊开的东西谁来读？](/zh-hans/agent-transparency/)》
- LangChain 2026 年在这篇文章原本的网址上发表的新文章，定义几乎一模一样：《[Jess Ou 的评测流程，里面还留给你的那一步](/zh-hans/reading-notes/langchain-what-is-an-agent/)》
- 回到系列索引：《[编者的阅读笔记](/zh-hans/reading-notes/)》

## 资料来源

- Harrison Chase，《What is an agent?》，LangChain，2024 年 6 月 28 日，存档版本：[http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) （通过 Wayback Machine 于 2026-09-26 读取并引用；原网址现在显示的是 Jess Ou 在 2026 年写的另一篇文章）

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
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
