# 在 Mac 上读 Markdown：MarsDawn 和其他做法

写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到[支持](/zh-hans/support/)页上的地址。

|  | MarsDawn | VS Code 预览 | Obsidian | QLMarkdown | LynxOffice |
|---|---|---|---|---|---|
| 打开本地 .md | 可以，直接改原文件 [app 1.1.1] | 可以，⇧⌘V 打开预览 [[8](#v8)] | 厂商未说明 [[21](#v21)] | 只能预览: "for viewing Markdown files" [[22](#v22)] | "Markdown opens rendered and saves back verbatim." [[3](#v3)] |
| Mermaid | 内置 [[1](#v1)] | 内置 [[8](#v8)] | 内置，笔记语法 [[16](#v16)] | 内置，`mermaid` 区块 [[22](#v22)] | "diagram blocks are not rendered" [[3](#v3)] |
| 数学公式 | KaTeX，`$…$`、`$$…$$` [[kit](#kit)] | KaTeX [[8](#v8)] | MathJax [[16](#v16)] | MathJax [[22](#v22)] | "Footnotes, math, and diagram blocks are not rendered." [[3](#v3)] |
| 检查代理的计划／跳到某一行 | `marsdawn open file:line`；从磁盘更新；拷贝引用 [/cli/, /features/] | Markdown diff 预览，标出改动的行 [[8](#v8)]；`code -g file:line` [[14](#v14)] | `obsidian://open` 没有行号参数 [[20](#v20)] | 厂商未说明 | 有 CLI 和 MCP 服务器；未说明跳行 [[4](#v4), [5](#v5)] |
| PDF：分页、页码 | 分页不切开短代码块 [/pdf/]；没有页码 [实测] | 厂商未说明 [[8](#v8)] | 纸张大小、边距；分页与页码未说明 [[17](#v17)] | 厂商未说明 [[22](#v22)] | PDF "including tables"；分页与页码未说明 [[3](#v3)] |
| 价格 | 免费下载；解锁一次 USD 4.99；试用 14 天 [[1](#v1)] | 厂商未说明 [[12](#v12), [13](#v13)] | 个人："Free without limits"；商用授权非必需 [[15](#v15)] | 免费，GPL-3.0 [[22](#v22)] | "Free while in early release." [[2](#v2)] |
| 系统要求 | macOS 26.0 或更新版本 [[1](#v1)] | "the latest release and the two previous versions" [[9](#v9)] | 厂商未说明 [[18](#v18)] | macOS 12.0 或更新版本 [[23](#v23)] | macOS 13 或更新版本 [[2](#v2)] |
| 需要账户 | 不需要 [/privacy/] | 厂商未说明 | "No sign-up required" [[15](#v15)] | 厂商未说明 | 不需要 [[2](#v2)] |

每一格都在 2026 年 10 月 16 日对照括号里的来源核实（V 编号列在下方；[实测] 是我们用 marsdawn 0.6.4 实际导出的结果）。厂商原文照录。“厂商未说明”表示我们读到的页面没有提到，不代表没有这个功能。表格不为产品排名。MarsDawn 自己那一栏在 2026 年 10 月 29 日根据 iPhone 和 iPad 版更新。

## 来源

- 1 · [Mac App Store](https://apps.apple.com/app/id6812925073)
- 2 · [https://lynxoffice.com/](https://lynxoffice.com/)
- 3 · [https://lynxoffice.com/markdown/](https://lynxoffice.com/markdown/)
- 4 · [https://lynxoffice.com/cli/](https://lynxoffice.com/cli/)
- 5 · [https://lynxoffice.com/mcp/](https://lynxoffice.com/mcp/)
- 6 · [https://lynxoffice.com/release-notes/](https://lynxoffice.com/release-notes/)
- 8 · [https://code.visualstudio.com/docs/languages/markdown](https://code.visualstudio.com/docs/languages/markdown)
- 9 · [https://code.visualstudio.com/docs/supporting/requirements](https://code.visualstudio.com/docs/supporting/requirements)
- 11 · [https://code.visualstudio.com/updates/v1_142](https://code.visualstudio.com/updates/v1_142)
- 12 · [https://code.visualstudio.com/license](https://code.visualstudio.com/license)
- 13 · [https://code.visualstudio.com/](https://code.visualstudio.com/)
- 14 · [https://code.visualstudio.com/docs/configure/command-line](https://code.visualstudio.com/docs/configure/command-line)
- 15 · [https://obsidian.md/pricing](https://obsidian.md/pricing)
- 16 · [https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax](https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax)
- 17 · [https://obsidian.md/help/pdf](https://obsidian.md/help/pdf)
- 18 · [https://obsidian.md/download](https://obsidian.md/download)
- 19 · [https://obsidian.md/changelog/](https://obsidian.md/changelog/)
- 20 · [https://obsidian.md/help/uri](https://obsidian.md/help/uri)
- 21 · [https://obsidian.md/help/Getting+started/Create+a+vault](https://obsidian.md/help/Getting+started/Create+a+vault)
- 22 · [https://github.com/sbarex/QLMarkdown](https://github.com/sbarex/QLMarkdown)
- 23 · [https://github.com/sbarex/QLMarkdown/releases](https://github.com/sbarex/QLMarkdown/releases)
- 24 · [https://api.github.com/repos/sbarex/QLMarkdown/releases](https://api.github.com/repos/sbarex/QLMarkdown/releases)
- kit · [https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7](https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7)

MarsDawn 没有的东西。需要 macOS 26 或更新版本。在 iPhone 和 iPad 上只能阅读，不能编辑，也不能导出 PDF。不能共同编辑，不同步，也没有账户。预览本身不能改，要改旁边的 Markdown 源文本。不能导出 Word，也没有插件。导出的 PDF 没有页码。没有 diff 视图：代理保存更改后，打开的窗口会从磁盘更新，一步就能撤销，但不会标出改了哪里。14 天试用结束后，文稿打开时内容会被遮住，直到解锁。

## 什么时候用不到 MarsDawn

- 你整天待在 VS Code，预览窗格就够：它能画 Mermaid、排 KaTeX，有 Markdown diff 预览，也能用 code -g 跳到某一行。
- 你只想在访达里按空格键预览：QLMarkdown 是免费的 Markdown 快速查看扩展。
- 你的 Mac 系统比较旧：QLMarkdown 需要 12.0 或更新版本，LynxOffice 需要 13 或更新版本。免费的 marsdawn 工具只要 macOS 15，不打开 app 也能导出 PDF。
- 你用 vault 管理互相链接的笔记：Obsidian 就是为此而做。
- 你需要在 iPhone 或 iPad 上编辑、共同编辑，或导出 Word。
- 你想让代理处理电子表格、Word 和 PDF：LynxOffice 为它们提供了 MCP 服务器文档。

- [MacMD Viewer 对比 MarsDawn](/zh-hans/vs/macmd-viewer/)：只读查看器和 MarsDawn 逐格对照，并说明各自适合什么情况。
- [Markdown 预览工具](/zh-hans/vs/markdown-preview-tools/)：VS Code 预览、浏览器扩展和 Claude Desktop 的文件预览。
- [2026 Mac Markdown 查看器推荐](/zh-hans/best-markdown-viewer-mac/)

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 检查代理写的 Markdown、JSON、YAML：Mac 原生 app，实时预览、Mermaid、KaTeX、快速查看、PDF。免费试用，之后一次 USD 4.99。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown、JSON、YAML 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可拿去开会或存档。
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
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把代理写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
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
- [English](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [Français](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [Español](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
