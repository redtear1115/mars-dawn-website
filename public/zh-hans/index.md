给建造者的前线工具

# 拿稳地图。读过黎明。

给要掌舵 agentic 开发的人用的 Markdown。

MarsDawn 是 macOS 原生的 Markdown 编辑器，有实时分栏预览、Mermaid 图表、KaTeX 数学公式、快速查看与 PDF 导出，可免费试用 14 天，之后只要一次 USD 4.99 解锁。

页面上有一个可以操作的 MarsDawn 窗口，内容是 App 内置欢迎指南的一段。调色板菜单可以选外观（系统、浅色、深色），并分别为浅色和深色从四个预览主题（黎明、典雅、流行、活泼）里选一个；工具栏可以选三种布局（源代码、并排、预览）。

## 读 agent 写的 Markdown。

1. **Agent 动笔。**你的代码助手或写作 agent 先写出 Markdown：README、规格文档，或一份笔记。
2. **你在 MarsDawn 里读。**打开文件，看排版后的页面，Mermaid 图表和代码高亮都在，旁边就是源代码。
3. **Agent 修改。**提出修改意见，agent 改好之后，再打开来读一次。

[如何审阅 agent 交回来的东西](/zh-hans/reading-agent-output/)。

## 现在就能做的事

免费的 `marsdawn` 命令行工具现在就能用。用 Homebrew 安装：

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` 把 Markdown 文件导出成 PDF，排版和 MarsDawn 的预览一样，不需要 app。
- `marsdawn open` 在 MarsDawn app 里打开文件，让你审阅。
- `--json` 返回脚本和 agent 能解析的结果。

[命令行工具](/zh-hans/cli/) · [给 AI agent 的 marsdawn 参考](/zh-hans/cli/agents/) · [给 agent 的 skill](/zh-hans/cli/skill/) · [MCP 服务器](/zh-hans/cli/mcp/)

## MarsDawn 是什么样的 app

- [为 Mac 而做](/zh-hans/native/)：原生窗口、标签页、自动保存、快速查看。
- [你写的内容留在你的 Mac 上](/zh-hans/yours/)：不需要账户，没有同步，也没有云端。
- [免费试用，买一次就好](/zh-hans/pay-once/)：免费试用 14 天，之后 USD 4.99 买一次，没有订阅。

购买前先知道。 [MarsDawn 做不到的事](/zh-hans/limits/)

## 常见问题

### MarsDawn 是什么？

MarsDawn 是 Mac 上原生的 Markdown 编辑器。源码旁边有实时预览，能画出 Mermaid 图表和 KaTeX 数学公式，在访达用快速查看预览 Markdown 文件，也能导出 PDF。

### MarsDawn 要订阅吗？

不用。MarsDawn 免费下载，14 天内所有功能都能试用；之后一次 USD 4.99 的 App 内购买就能永久解锁。没有任何续订，也不需要账户。

### MarsDawn 有 iPhone 或 iPad 版吗？

没有。MarsDawn 是 Mac app，需要 macOS 26 或更新版本，没有 iPhone 或 iPad 版。

### Claude Code 可以用 MarsDawn 打开文件吗？

可以。免费的 marsdawn 命令行工具有 open 命令，能用 MarsDawn 打开 Markdown 文件，所以 Claude Code，或任何能执行 shell 命令的 agent，都能调用它。另有一个需要自行启用的 Claude Code hook，可以在 Claude 写入或编辑 Markdown 文件时自动打开。

### 试用结束后，快速查看还能用吗？

能。不论试用是否进行中，访达里的快速查看都会继续显示你的 Markdown 文件。试用结束、尚未解锁时，在 MarsDawn 里打开的文档内容会被遮住。

## App 实际的样子

### [为 Mac 而做](/zh-hans/native/)

![MarsDawn 的并排布局：左边是 Markdown 源代码，右边是排版后的页面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

这张截图里：

1. 原生的 Mac 窗口。
2. Mac 原生的文本编辑器，附 Markdown 语法高亮。
3. ⌘1 源代码、⌘2 并排、⌘3 预览。
4. 页面会随着打字更新。

### [导出 PDF](/zh-hans/pdf/)

![用 MarsDawn 导出的 PDF，在内置的 PDF 查看器中打开，旁边有页面缩略图。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

这张截图里：

1. Mermaid 图表直接画进 PDF。
2. 代码保留语法高亮。

## 其他页面

- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。在浏览器里打造自己的主题，也可以逛逛社区主题库。
- [打造一个主题](https://marsdawn.southern-light.dev/zh-hans/themes/new/index.md): 挑选颜色和几个样式选项，实时看它们套用在范例文档上，再把主题送出成一个 GitHub issue。不用安装，也不用 git。
- [主题库](https://marsdawn.southern-light.dev/zh-hans/themes/gallery/index.md): 浏览社区投稿的 MarsDawn 预览主题，按场景筛选，也可以举报有问题的主题。在浏览器里打造一个自己的主题，不用安装，也不用 git。
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
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/index.md): MarsDawn is a native Markdown editor for Mac with live split preview, Mermaid, KaTeX, Quick Look and PDF export. Free to try, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是 Mac 原生 Markdown 編輯器：即時分割預覽、Mermaid、KaTeX、快速查看、PDF 輸出。免費試用，之後一次 USD 4.99 解鎖。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): MarsDawn は Mac 向けのネイティブ Markdown エディタです。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): MarsDawn ist ein nativer Markdown-Editor für Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): MarsDawn est un éditeur Markdown natif pour Mac : aperçu en direct côte à côte, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): MarsDawn es un editor Markdown nativo para Mac: vista previa en vivo, Mermaid, KaTeX, Vista rápida, exportación PDF. Pruébalo gratis; luego, 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): MarsDawn은 Mac용 네이티브 Markdown 편집기입니다. 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번만 USD 4.99.
