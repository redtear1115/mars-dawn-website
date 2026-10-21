# 2026 Mac Markdown 查看器推荐

哪款 Markdown 查看器最好，要看你读的是什么。如果是自己写的笔记，一款全能的笔记 App 就够了。如果是带图表和数学公式的长文稿，或是 AI 代理不断改写的文件，就要看各款怎么处理自动重新载入、Mermaid 和 PDF。以下按字母排序，每款都写出适合谁、一个坦白的缺点和价格。

## MacDown 3000

原版 MacDown 已停止维护。MacDown 3000 是社区接手的版本：免费开源（MIT）、原生，支持 Mermaid、MathJax、PDF 导出、自动重新载入与快速查看。

- 适合：想要免费原生左右分栏的人。
- 缺点：没有文档说明能从命令行打开到指定行。
- 价格：免费。

## Marked

Marked 3 是预览器，用来看你在其他 App 里写的 Markdown。文件一变就重新载入，支持 MathJax 与 KaTeX，能打印分页并带页码的 PDF。Marked 2 仍在销售。

- 适合：保留自己的写作工具、想要精致预览与打印的写作者。
- 缺点：快速查看要另买 Marked QL（USD 9.99）。
- 价格：Marked 3 免费下载，之后每月 USD 2.99、每年 USD 29.99 或终身 USD 69.99。Marked 2 官网 USD 14.99，Mac App Store USD 13.99。

## MarkEdit

轻巧免费的原生 App（在 web view 中使用 CodeMirror），支持快速查看。

- 适合：想要快速、有 Mac 手感的纯文本工具的人。
- 缺点：Mermaid 与数学公式要装官方扩展，PDF 要靠 Pandoc。
- 价格：免费。

## MarsDawn

原生 Mac App，源文本与实时预览左右并排，内置 Mermaid 与 KaTeX。AI 代理保存文件时，打开的窗口会把更改收成一步可撤销的“从磁盘更新”。`marsdawn open notes.md:120` 可打开到指定行，另有给代理用的代理技能与 MCP 服务器。无论是否在试用期，快速查看都能用。“拷贝给 AI”与“拷贝引用”能把文字交给代理。除非你选择，数据不会离开你的 Mac。

- 适合：审阅 AI 代理所写 Markdown 的人。
- 缺点：导出的 PDF 没有页码。
- 价格：免费下载，试用 14 天，之后一次性 USD 4.99。无需账户。仅在 Mac App Store 提供。

## Obsidian

以链接 Markdown 文件的 vault 为核心的笔记 App，支持 Mermaid、MathJax、PDF 导出与自动重新载入。

- 适合：搭建个人知识库的人。
- 缺点：是 Electron App，文件放在 vault 里才最顺手。
- 价格：免费，Sync 与 Publish 另行付费。

## QLMarkdown

快速查看扩展：在访达中选中 .md 文件按空格键即可。Mermaid 与 MathJax 需手动开启。

- 适合：只想在访达里瞄一眼文件的人。
- 缺点：不是用来阅读或编辑的 App，也没有文档说明 PDF 导出。
- 价格：免费（GPL-3.0）。

## Typora

预览即文稿的所见即所得式写作工具，支持 Mermaid、MathJax，PDF 导出可在页眉或页脚加页码。

- 适合：喜欢直接在排版画面中写作的人。
- 缺点：没有源文本与预览左右并排。
- 价格：一次性 USD 14.99，最多 3 台设备。

## VS Code 预览

内置 Markdown 预览，1.121 起内置 Mermaid，支持 KaTeX。`code -g file:line` 可打开到指定行。

- 适合：本来就整天用 VS Code 的开发者。
- 缺点：是 Electron App，没有内置 PDF 导出。
- 价格：免费。

## 比较表

| App | 价格 | Mermaid | 数学公式 | PDF | 自动重新载入 | 命令行打开到指定行 | 快速查看 | 架构 |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | 免费 | 有 | MathJax | 有 | 有 | 无文档 | 有 | 原生 |
| Marked 3 | 每月 USD 2.99 起 | 有 | MathJax、KaTeX | 有，带页码 | 有 | 无文档 | Marked QL，USD 9.99 | 原生 |
| MarkEdit | 免费 | 扩展 | KaTeX（扩展） | Pandoc | 无文档 | 无文档 | 有 | 原生（web view） |
| MarsDawn | 一次性 USD 4.99 | 有 | KaTeX | 有，无页码 | 有，可撤销 | 有 | 有 | 原生 |
| Obsidian | 免费 | 有 | MathJax | 有 | 有 | 无文档 | 无文档 | Electron |
| QLMarkdown | 免费 | 需开启 | MathJax（需开启） | 无文档 | 不适用 | 不适用 | 本身就是 | 原生 |
| Typora | 一次性 USD 14.99 | 有 | MathJax | 有，带页码 | 无文档 | 无文档 | 无文档 | 原生 |
| VS Code | 免费 | 有（1.121 起） | KaTeX | 无 | 无文档 | 有 | 无文档 | Electron |

## MarsDawn 不适合谁

- PDF 一定要有页码。Typora 与 Marked 3 能加，MarsDawn 不能。
- 你在维护互相链接的个人笔记库。Obsidian 就是为此打造的。
- 你从不离开 VS Code。内置预览免费，VS Code 也正在 Agents 窗口加入实验性的 Markdown 查看。
- 你只想在访达里预览。QLMarkdown 免费。

## 常见问题

### 哪些免费的 Mac Markdown 查看器支持 Mermaid？

MacDown 3000、Obsidian 与 VS Code（1.121 起）内置。QLMarkdown 可选择开启，MarkEdit 要通过扩展。

### 哪些能导出带页码的 PDF？

Typora 与 Marked 3。MarsDawn 导出的 PDF 没有页码。

### 哪些能从命令行打开到指定行？

MarsDawn（`marsdawn open notes.md:120`）与 VS Code（`code -g file:line`）。其他几款无文档说明。

### 哪些是原生 Mac App，而不是 Electron？

除了 Obsidian 与 VS Code 都是。MarkEdit 是原生 App，编辑区使用 web view。

[立即下载试用](https://apps.apple.com/app/id6812925073)

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户。内置四种主题，主题图库还有更多。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [Mac 上怎么打开 md 文件](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [在 Mac 上预览 Mermaid](https://marsdawn.southern-light.dev/zh-hans/mermaid-preview-mac/index.md): 在 Mac 上预览 Mermaid 图表：源代码旁边实时画出来，快速查看和导出 PDF 也看得到。图表写错时，会显示错误信息和出错的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MarsDawn 对比：VS Code 预览、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM 代理把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI 代理的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI 代理与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给代理的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的代理把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个代理写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回代理的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。在浏览器里打造自己的主题，也可以逛逛社区主题图库。
- [打造一个主题](https://marsdawn.southern-light.dev/zh-hans/themes/new/index.md): 挑选颜色和几个样式选项，实时看它们套用在范例文档上，再把主题送出成一个 GitHub issue。不用安装，也不用 git。
- [和代理一起做主题](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [主题图库](https://marsdawn.southern-light.dev/zh-hans/themes/gallery/index.md): 浏览社区投稿的 MarsDawn 预览主题，按场景筛选，也可以举报有问题的主题。在浏览器里打造一个自己的主题，不用安装，也不用 git。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把代理写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂代理交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI 代理把工作成果交成 Markdown：计划、规格、进度报告。做代理的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [代理的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造代理的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [审代理计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): 代理交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [代理设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种代理设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [编者的阅读笔记](https://marsdawn.southern-light.dev/zh-hans/reading-notes/index.md): 六篇短笔记，谈打造 AI 代理的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读代理交回来的东西”的人分别意味着什么。
- [阅读笔记：Anthropic](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和代理分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [阅读笔记：Chip Huyen](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把代理的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM 代理描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对代理的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测代理的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给代理写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给代理的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。代理来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。代理来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
