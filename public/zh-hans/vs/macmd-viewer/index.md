# MacMD Viewer 对比 MarsDawn。

两者都是给 Mac 用的 app，都能把 Markdown 排版成完整的页面来读。MacMD Viewer 打开 `.md` 文件并显示出来；它设计上就是只读，不会保存对文件的任何改动。MarsDawn 则是在同样的预览旁边放了编辑器，让你在同一个窗口里写和读。这一页把两者逐项并排，MacMD Viewer 的每一项事实都附上来源，也会说明什么情况下 MacMD Viewer 是比较好的选择。

以上依 2026 年 10 月 15 日 MacMD Viewer 自己的网站和 repo 核对（版本 1.7.0，2026 年 10 月 10 日发布）。如果有哪里过时了，请照[支持页](/zh-hans/support/)上的联系方式告诉我们。

## 它是什么、能做什么

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 是什么 | 查看器：“只读，不会保存对源文件的改动”[[S1](#s1), [S9](#s9)] | 有实时预览的编辑器：左边写 Markdown，右边看排版后的页面，三种版面（源代码、并排、预览） |
| 编辑 | 不能 [[S1](#s1), [S7](#s7), [S9](#s9)] | 可以。排版后的页面本身不能直接编辑，要编辑旁边的源代码 |
| 实时预览 | 显示文件；别的编辑器保存文件后会自动重新载入 [[S9](#s9)] | 打字时就更新。别的 app 改了文件，MarsDawn 会重新载入并保留你的位置，前提是你自己没有未保存的修改。 |
| Mermaid | 有：流程图、时序图、状态图、甘特图、饼图等，离线可用 [[S1](#s1), [S3](#s3), [S7](#s7)] | 有 |
| 数学公式 | 没有：它的 README 写明“不显示数学公式（LaTeX／KaTeX）”[[S7](#s7)] | 有，KaTeX |
| 代码高亮 | 有 [[S1](#s1), [S9](#s9)] | 有 |
| 主题 | 12 种文档主题 [[S1](#s1), [S7](#s7)] | 内置 4 种（黎明、典雅、流行、活泼），各有浅色与深色，主题图库还有更多 |
| 标签页 | 有，可选，默认关闭（1.6.0 起）[[S5](#s5), [S8](#s8)] | 有 |
| PDF 导出 | 有，单一连续页面，用当前的主题，无水印 [[S3](#s3), [S9](#s9)] | 有，分页输出，用主题的浅色配色；分页时尽量不切开短的代码 |
| 打印 | 有，走 macOS 的打印对话框 [[S3](#s3), [S9](#s9)] | 有 |
| 访达的快速查看 | 有，已包含；要在系统设置里启用；使用你选的主题 [[S4](#s4)] | 有，不论有没有试用都能用；使用你选的主题 |
| 快速查看里的 Mermaid 与数学公式 | Mermaid：有 [[S4](#s4)]。数学公式：没有，它不显示数学公式 [[S7](#s7)] | 有，两者都会画出来 |
| 命令行 | 没有描述独立的命令行工具。它有 `markdownviewer://` URL scheme，以及用来打开文件的 Claude Code 插件和 hook [[S6](#s6)] | 免费的 `marsdawn` 工具：`marsdawn export` 不需要 app 就能导出 PDF，`marsdawn open` 能在指定行打开文件 |
| 界面语言 | 自己的资料没有写明 [[S1](#s1), [S3](#s3), [S7](#s7)] | 英文、繁体中文、简体中文、日文、德文、法文、西班牙文和韩文 |
| 系统要求 | macOS 14（Sonoma）或更高版本；Apple 芯片与 Intel [[S1](#s1), [S7](#s7)] | macOS 26（Tahoe）或更高版本 |
| 其他平台 | 只有 Mac [[S1](#s1)] | Mac；iPhone 和 iPad 上只能阅读 |

## 价格与购买方式

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 从哪里买 | 自己的网站、Homebrew 或 Setapp；没有在 Mac App Store 上架 [[S2](#s2), [S7](#s7)] | 只在 Mac App Store |
| 价格 | 一台正在使用的 Mac 一次 USD 19.99（可以移到另一台 Mac）；Family Pack 3 把 USD 39.99；10 把 USD 129 [[S2](#s2)] | 免费下载，之后一次 USD 4.99 |
| 先试用 | 没有试用，也没有免费版；直接购买 14 天内全额退款 [[S2](#s2)] | 14 天免费试用，所有功能都能用 |
| 退款 | 14 天内，通过它自己的支持邮箱 [[S2](#s2)] | 通过 Apple |
| 更新 | 同一主版本内的更新免费 [[S2](#s2)]；直接下载的版本用 Sparkle 自动更新 [[S7](#s7)] | 通过 Mac App Store |
| 需要账号 | 不需要 [[S2](#s2)] | 不需要 |
| 订阅 | 没有 [[S1](#s1), [S2](#s2)] | 没有 |

## 试用或购买之后

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 状态 | 没有试用；买了就一直能用 | 14 天后没有解锁，文稿仍会打开但内容被遮住；文件不会有任何改变，快速查看和免费的 `marsdawn` 导出都照常 |

## 来源

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## 该选哪一个

**选 MacMD Viewer，如果**你只读 Markdown，而且希望“不会改到文件”这件事是保证的：它不会保存对文件的任何改动 [[S1](#s1)]。这些情况它也比较合适：你的 Mac 跑的是 macOS 14 或 15（MarsDawn 需要 macOS 26）[[S1](#s1), [S7](#s7)]；你比较想从开发者自己的网站、Homebrew 或 Setapp 买，而不是 Mac App Store [[S2](#s2), [S7](#s7)]；你想让代理改过的文件自动在查看器里打开，它用 Claude Code、Cursor 和 Windsurf 的 hook 做到 [[S6](#s6)]；或者你想要单一连续页面的 PDF，而不是分页的 PDF [[S9](#s9)]。它没有试用，但有 14 天退款 [[S2](#s2)]。

**选 MarsDawn，如果** Markdown 读完还要再改一轮。代理写的计划、README 或规格，通常要修一个地方、改一句话或加一段，在 MarsDawn 里就在你正在读的那个窗口里改。它也支持数学公式（KaTeX），MacMD Viewer 自己说不显示 [[S7](#s7)]；界面有八种语言；有免费的 `marsdawn` 命令行工具，不需要 app 就能导出 PDF；价格是 14 天全功能试用后 USD 4.99。

**两个都可以，如果**你在较新的 Mac 上读 Markdown，想把 Mermaid 图表画好，也想在访达用快速查看。两者都做得到。

**也可以两个都用。**两者不互斥：只读的文件用只读查看器，要写的文件用编辑器，并不冲突。

## 常见问题

### MacMD Viewer 能编辑文件吗？

不能。它是只读的，照它自己的说法，不会保存对源文件的改动 [[S1](#s1), [S9](#s9)]。它可以把文件交给你的文本编辑器打开（“文件”菜单，⇧⌘E，1.7.0 起）[[S5](#s5)]。

### MacMD Viewer 在 Mac App Store 上吗？

它自己的页面列出的是官网、Homebrew 和 Setapp，没有提到 Mac App Store [[S2](#s2), [S7](#s7)]。MarsDawn 只在 Mac App Store。

### MarsDawn 能打开同样的文件吗？

可以。它打开 `.md` 文件，也能打开纯文本文件和 PDF：UTF-8 的文本文件可直接编辑，PDF 以查看器打开。

### 我的 Mac 是 macOS 14 或 15 呢？

MacMD Viewer 在 macOS 14 以上都能跑 [[S1](#s1)]。MarsDawn 需要 macOS 26 以上，不过免费的 `marsdawn` 命令行工具仍然可以导出 PDF。

### 为什么一个是 USD 19.99，一个是 USD 4.99？

两者拿到的东西和付费方式不同。MacMD Viewer 是一次买断，有 14 天退款，没有试用 [[S2](#s2)]。MarsDawn 免费下载，有 14 天试用，之后一次解锁。两者都不是订阅。

## 现在就能免费试试看

MarsDawn 已在 Mac App Store 上架。免费的 `marsdawn` 命令行工具也能把任何 Markdown 文件转成 PDF，Mermaid 图表和代码高亮都在，而且不需要安装其他东西：

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 接下来

- 完整步骤：[Markdown 转 PDF](/zh-hans/markdown-to-pdf/)。
- MarsDawn 做不到的事：[这份清单](/zh-hans/limits/)。
- 命令行工具的所有选项：[命令行工具](/zh-hans/cli/)。
- MarsDawn 的全部功能，一页看完：[功能一览](/zh-hans/features/)。

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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
