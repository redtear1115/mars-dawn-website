# Andrew Ng 自己帮四种设计模式的可预测程度排序

**2024 年初，Andrew Ng 在 The Batch 用五篇文章介绍了四种 agentic 设计模式——reflection（反思）、tool use（使用工具）、planning（规划）、multi-agent collaboration（多 agent 协作）——而且很少见地直接告诉读者，这四种里他觉得哪两种比较可靠、哪两种难以预测。**

## 这几篇文章主张什么

《[四种 agent 设计模式，各自会交给你什么文件](/zh-hans/agent-design-patterns/)》已经完整谈过这四种模式各自是什么、当成我们自己的推论各自通常会交给你什么文件，还有 Ng 自己对 planning 的评语，引自 Part 4：“while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do”（Reflection 和 Tool Use 这两种设计模式我都能让它们稳定运作、提升应用程序的表现，但 Planning 还是比较不成熟的技术，我很难事先预测它会怎么做）。这篇要补的，是那篇没用到的另外两封信里同一个排序：Part 3，写在 Part 4 之前一周，先讲出了这个排序；Part 5，把排序延伸到 Part 4 没提到的那一种模式——multi-agent collaboration。在介绍 tool use 的 Part 3 里，他写道：

> “In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.”

（在接下来的信里，我会介绍 Planning 和 Multi-agent collaboration 这两种设计模式。它们能让 AI agent 做到更多事，但也是比较不成熟、比较难预测的技术——虽然非常令人兴奋。）

两周后，他在系列最后一篇谈 multi-agent collaboration 时，从另一个角度确认了同样的排序：

> “Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.”

（就像 Planning 这个设计模式一样，我发现 multi-agent collaboration 的输出质量很难预测，尤其是让 agent 之间自由互动、又给它们多种工具的时候。比较成熟的 Reflection 和 Tool Use 模式则可靠得多。）

他讲的是这几种模式对他自己应用程序表现的提升效果，不是在谈应该多仔细审阅它们的产出——这个系列完全没有主张要人工审阅，也没有提到 MarsDawn 或推荐任何 Markdown 工具。

## 以下是我们的解读，不是 Ng 的

Ng 的排序谈的是开发者视角下的输出质量和可预测性，但大致对应到每种模式留下的记录，从你的角度该花多少心力去查。他觉得比较可靠的 reflection 和 tool use，通常会交给你描述“已经做完的事”的东西——一份改过的草稿、一份跑了什么的报告——所以拿里面一个宣称去对照真正的输出，通常就能覆盖大部分风险。他觉得难以预测的 planning 和 multi-agent collaboration，通常会交给你“事情发生之前”写好的东西，或是分散在好几个 agent 手上的好几份文件：一份还在等你点头的计划，或是还没被实际执行验证过的 agent 交接。照他自己的说法，这两种正是“写下来的东西”和“实际会发生的事”落差最大的地方——这也正是《五分钟审完一份 agent 计划》从 Chip Huyen 那篇文章里引出的道理，在“为什么要在执行前审”那一段：在事情跑之前抓到问题，是最便宜的时机。

## MarsDawn 帮得上、帮不上的地方

MarsDawn 不知道一份文件是 Ng 四种模式里哪一种做出来的，也不会替任何东西按可预测程度排序，里面也没有 AI 模型——他排序背后暗示值得做的那些检查，它不会替你做。它做的是让文件在你自己检查的时候保持好读：侧边栏（“显示 ▸ 显示边栏”，⌃⌘S）的“大纲”标签页看得出一份长计划的架构；原始码和排好的预览并排（⌘2）；multi-agent 交接的情况下，用“文件 ▸ 打开文件夹…”（⇧⌘O）打开共用的文件夹，不同 agent 写出新文件时，大约一秒内就会出现在“文件”标签页，清单上方也会标出 git 分支或工作树，两份不同 agent 写的同名文件就不会搞混。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 输出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- 每种模式完整会交给你什么文件：《[四种 agent 设计模式，各自会交给你什么文件](/zh-hans/agent-design-patterns/)》
- 执行前五分钟审完一份计划的方法：《[五分钟审完一份 agent 计划](/zh-hans/reviewing-agent-plans/)》
- 回到系列索引：《[编者的阅读笔记](/zh-hans/reading-notes/)》

## 资料来源

- Andrew Ng，《Agentic Design Patterns Part 1》，The Batch，2024 年 3 月 20 日：[https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng，《Agentic Design Patterns Part 3: Tool Use》，The Batch，2024 年 4 月 3 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/) （2026-09-26 读取并引用）
- Andrew Ng，《Agentic Design Patterns Part 4: Planning》，The Batch，2024 年 4 月 10 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/) （引文原封不动沿用自 `design/inbox/276-agent-blog-series.md`，该引文已用在 `/zh-hans/agent-design-patterns/`）
- Andrew Ng，《Agentic Design Patterns Part 5, Multi-Agent Collaboration》，The Batch，2024 年 4 月 17 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/) （2026-09-26 读取并引用）

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
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
