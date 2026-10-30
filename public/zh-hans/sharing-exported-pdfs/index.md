# 把 PDF 交出去，不是把 Markdown 交出去。

代理写完一份文稿，你审阅、修改过后，公司里不写程序的人也要看——主管、客户，或另一个团队的人。他们不需要知道 `##` 或表格的竖线符号是什么意思。导出成 PDF，交给他们那份就好。

**把审阅过的文稿导出成 PDF，发那个文件就好。**它在任何地方都打得开，不需要懂 Markdown，也不用安装任何东西，看起来就跟你在预览里看到的一样——图表、表格、格式都在。

## 为什么不直接发 .md 文件

用纯文本编辑器打开 `.md` 文件，看到的是记号，不是排好版的页面：`#` 是标题，`**` 包住粗体文字，围住 Mermaid 图表的代码块没有画出图。不写 Markdown 的人看不出这些记号原本要呈现什么，而为了一份文稿就要对方先装一个查看器，也要求太多。

## 为什么不直接发截图

截图只能定格文稿的其中一个画面，文稿可能有好几页，内容不能搜索也不能选取，转发几次、被压缩后也会更难读。PDF 不管文稿多长，都能保留文字、图表和分页。

## PDF 能给你什么

- 对方已经有的东西就能打开——Preview、浏览器、Acrobat、手机都行，不需要任何 Markdown 工具。
- Mermaid 图表会画出来，不会留着代码原样；代码块保留语法上色。
- 分页位置经过安排，标题不会孤零零留在页尾，图表也不会被切成两半。
- 不管是从 MarsDawn app 还是免费的命令行导出，得到的都是同一份文件——完整步骤请看[Markdown 转 PDF](/zh-hans/markdown-to-pdf/)。

## 接下来

- 可以用哪些主题和布局导出：[预览主题与 PDF 导出](/zh-hans/themes/)。
- 从脚本或代理导出，而不是从 app：[给 AI 代理的 marsdawn 参考](/zh-hans/cli/agents/)。
- 为什么还是要先有人读过这份文稿：[审阅的理由](/zh-hans/reviewing-ai-output/)。
- 多代理交接常常就是要分享 PDF 的时候：[四种代理设计模式，各自会交给你什么文件](/zh-hans/agent-design-patterns/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、iPhone 和 iPad 上不能编辑、没有插件、不需要账户；可以换主题，但不能自定义 CSS。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [Mac 上怎么打开 md 文件](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [在 Mac 上预览 Mermaid](https://marsdawn.southern-light.dev/zh-hans/mermaid-preview-mac/index.md): 在 Mac 上预览 Mermaid 图表：源代码旁边实时画出来，快速查看和导出 PDF 也看得到。图表写错时，会显示错误信息和出错的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MarsDawn 对比：VS Code 预览、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [2026 Mac Markdown 查看器推荐](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM 代理把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI 代理的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI 代理与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给代理的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的代理把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个代理写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回代理的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [主题](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 内置四种预览主题，各有浅色与深色；在 Mac 版 MarsDawn 的设置里打开主题图库，还能安装更多。快速查看也会用你选的主题。
- [打造一个主题](https://marsdawn.southern-light.dev/zh-hans/themes/new/index.md): 挑选颜色和几个样式选项，实时看它们套用在范例文档上，再把主题送出成一个 GitHub issue。不用安装，也不用 git。
- [和代理一起做主题](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [主题图库](https://marsdawn.southern-light.dev/zh-hans/themes/gallery/index.md): 浏览 MarsDawn 的预览主题，每一个都经过开发者审核；可以按场景筛选，也可以举报有问题的主题。在浏览器里打造自己的主题，不用安装，也不用 git。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂代理交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI 代理把工作成果交成 Markdown：计划、规格、进度报告。做代理的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [代理的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造代理的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [审代理计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): 代理交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [代理设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种代理设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [路线图](https://marsdawn.southern-light.dev/zh-hans/roadmap/index.md): MarsDawn 在 Mac、iPhone 与 iPad 上正在做和接下来要做的功能，按版本列出。不写日期，未排期的项目另行标明。
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
- [English](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [日本語](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [Deutsch](https://marsdawn.southern-light.dev/de/sharing-exported-pdfs/index.md): Exportiere das Markdown eines Agenten als PDF und gib es einer Kollegin, die kein Markdown liest und nichts installieren wird. Zum Öffnen braucht es keine Syntax, keine App und keinen Account.
- [Français](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Español](https://marsdawn.southern-light.dev/es/sharing-exported-pdfs/index.md): Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.
- [한국어](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
