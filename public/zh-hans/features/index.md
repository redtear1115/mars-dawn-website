# MarsDawn 能做的事，一页看完。

MarsDawn 是为 Mac 做的 Markdown 编辑器。一边写，一边读排版后的页面，图表、数学公式和代码都画在里面。它没有自己的 AI 模型：做它是为了读代理写的东西，也让你写自己的。工作换到会议桌或档案柜上时，它也能打印、导出干净的页面。

下面每一节说明 app 做了什么，并链接到讲得更细的页面。

![MarsDawn 的并排布局：左边是 Markdown 源代码，右边是排版后的页面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

这张截图里：

1. 原生的 Mac 窗口。
2. Mac 原生的文本编辑器，附 Markdown 语法高亮。
3. ⌘1 源代码、⌘2 并排、⌘3 预览。
4. 页面会随着打字更新。

## 读代理写的 Markdown

### 源代码和预览并排

打开 Markdown 文件，排版后的页面就在源代码旁边（⌘2）；也可以只看源代码（⌘1）或只看预览（⌘3）。两边一起滚动，页面会随着输入更新。

[为 Mac 而做](/zh-hans/native/)

### 大纲和文件边栏

边栏的“大纲”列出文稿的标题，点按一下就跳到该处。打开文件夹后，“文件”标签列出里面的文件；代理正在写入时，新文件会自动出现。如果文件夹是 git 检出，上方标题会写出是哪个分支或工作树。

[读懂代理交回来的 Markdown](/zh-hans/reading-agent-output/)

### 指出确切的那一行

“编辑 ▸ 拷贝引用”会把你的位置拷贝成路径加行号，例如 `docs/plan.md:42`。“拷贝给 AI”再附上所选的文字。粘贴到代理的对话里就行。

[读懂代理交回来的 Markdown](/zh-hans/reading-agent-output/)

### 跟着链接跳到另一个文件

在预览里点按一个指向另一个 Markdown 文件的链接，MarsDawn 会打开那个文件（已经开着就带到前面），并滚动到那个标题。

## 纸质文件在人与人之间的用处

不是所有的工作都在屏幕上做。MarsDawn 打印和导出的页面，就是你在屏幕上读的那几页，所以人们聚在一起、读东西、留记录的地方都用得上。

### 开会讨论

把页面打印出来，或把同一份 PDF 发给每个人，大家就是看同一份文稿，不用挤在一个屏幕前。拿到同一个文件的人，分页位置都一样，所以“第 3 页那张表”指的是同一个东西。接着由人把决议写下来，写在打印出来的纸上，或写成笔记。会议记录模板把决议放在最前面，每个行动项都有负责人。

[导出 PDF](/zh-hans/pdf/) · [会议记录模板](/zh-hans/templates/meeting-notes/)

### 拿笔边读边写

有些人习惯用笔读东西：画线、在页边写几个字，才记得住。把文稿打印出来，就可以在纸上这样做。MarsDawn 本身没有批注功能；想直接在 PDF 上标记的话，用你原本就有的 PDF app 就好。

[导出 PDF](/zh-hans/pdf/)

### 纸质存档

有些行业还是要把纸质文件存起来，会计就是一个例子。MarsDawn 没有任何归档或合规的声明。它做的是打印和导出干净、分好页的页面：图表画进去，短的代码块不被切开，用主题的浅色配色。纸质文件还是正式记录的地方，就可以用这些页面。

[导出 PDF](/zh-hans/pdf/)

### 交给不写 Markdown 的人

PDF 在任何地方都能打开，也不需要懂 Markdown，所以也适合发给主管或客户。

[分享导出的 PDF](/zh-hans/sharing-exported-pdfs/)

## 写作和版面

### 纯 Markdown，附语法着色

粗体、斜体、删除线、行内代码、链接、引文和待办清单都照常使用。编辑器会给 Markdown 语法着色，颜色和预览主题一致。

[为 Mac 而做](/zh-hans/native/)

### 缩放、行号和状态栏

源代码和预览可以一起缩放，范围 50% 到 300%。源代码旁有行号栏；状态栏显示光标所在的行与列，以及整份文稿或所选文字的字数、字符数和阅读时间。

### 图像

先存储文稿，再把图像拖入或粘贴到编辑器。MarsDawn 会把图像拷贝到文稿旁的 assets 文件夹，并写好链接。网络图像在你点按“载入图像”之前都不会载入，所以打开文稿不会让任何服务器知道你读了它。

[你写的内容留在你的 Mac 上](/zh-hans/yours/)

### Front matter 不碍事

文件开头的 front matter 区块，在预览和快速查看里会收成可展开的“文稿信息”，导出 PDF 时则不会印出。

### 八种语言

App 界面有英文、繁体中文、简体中文、日文、德文、法文、西班牙文和韩文。

[为 Mac 而做](/zh-hans/native/)

## 图表、代码和数学公式

### Mermaid 图表

标记为 `mermaid` 的代码块会画成图表。图表写错时，预览会显示它的源代码，下方附上错误信息；点按信息，就跳到编辑器里那一行。

[在 Mac 上预览 Mermaid](/zh-hans/mermaid-preview-mac/)

### 代码着色

常见的编程语言都会语法着色，在开头的 ````` 后面写上语言名称就好。

### 数学公式

用 KaTeX 语法写的数学公式，会在预览和快速查看里画出来，导出的 PDF 里也有。

[为什么 AI 写的东西还是需要人读过](/zh-hans/reviewing-ai-output/)

## 主题、PDF 和打印

### 四种主题，各有浅色和深色

黎明、典雅、流行、活泼各有浅色和深色版本。MarsDawn 会跟着 Mac 的外观切换，也可以在设置中固定一种。从“显示 ▸ 预览主题”或工具栏的调色板按钮选择。

[预览主题与 PDF 导出](/zh-hans/themes/)

### 更多主题

“设置 ▸ 外观 ▸ 获取更多主题…”会打开额外预览主题的主题图库。装上一个，它就出现在“显示 ▸ 预览主题”里；点按“移除”就拿掉。主题图库只在打开的时候连上网络。

[主题图库](/zh-hans/themes/gallery/) · [打造一个主题](/zh-hans/themes/new/)

### 导出 PDF，或打印

“文件 ▸ 导出为 PDF…”会存成自动分页的 PDF，“文件 ▸ 打印…”打印相同的页面。Mermaid 图表直接画进去，代码保留语法着色，分页时会尽量不让标题落在页尾，也不切开短的代码块和图表。PDF 一律用主题的浅色配色，就算你是在深色下读的也一样。

[导出 PDF](/zh-hans/pdf/)

![用 MarsDawn 导出的 PDF，在内置的 PDF 查看器中打开，旁边有页面缩略图。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

这张截图里：

1. Mermaid 图表直接画进 PDF。
2. 代码保留语法高亮。

## 文件、标签页和快速查看

### 窗口和标签页

每份文稿默认在自己的窗口打开。用“窗口 ▸ 合并所有窗口”，可以把开着的窗口收成同一个窗口里的标签页。输入时会自动存储。

[为 Mac 而做](/zh-hans/native/)

### 在访达用快速查看

在访达选取 Markdown 文件并按空格键，就能看到排版后的样子，图表也会显示。快速查看会用你在 MarsDawn 选的主题，也跟着 MarsDawn 的外观设置。

[为 Mac 而做](/zh-hans/native/)

### 其他文件

MarsDawn 也能打开纯文本文件（`.txt`、`.log`、代码文件）和 PDF。UTF-8 纯文本文件打开就能直接编辑，只显示源代码。PDF 则在有页面缩略图、缩放和搜索的查看器中打开。

### 你的文件留在你手上

不需要账户，没有同步，也没有云端。文稿留在你存储的位置，MarsDawn 不收集任何关于你的数据。

[你写的内容留在你的 Mac 上](/zh-hans/yours/)

## 给代理和脚本

### 免费的命令行工具

免费的 `marsdawn` 工具另外用 Homebrew 安装。`marsdawn export` 把 Markdown 文件导出成 PDF，排版和 MarsDawn 的预览一样，不需要 app；可以用 `--theme` 选主题，纸张选 A4 或 Letter。`marsdawn open` 在 app 里打开文件让你审阅，还可以指定行号，这个需要先装 app。

[命令行工具](/zh-hans/cli/)

### 脚本读得懂的输出

加上 `--json`，两个命令都会返回代理或脚本能解析的结果。

[给 AI 代理的 marsdawn 参考](/zh-hans/cli/agents/)

### Skill 和 MCP 服务器

一个代理技能文件，教写代码的代理把自己写的东西在 MarsDawn 里打开给你审阅。没有 shell 的客户端，则可以用另外的 MCP 服务器执行同一个 export。

[给代理的 skill](/zh-hans/cli/skill/) · [MCP 服务器](/zh-hans/cli/mcp/)

### 里面没有 AI

MarsDawn 没有自己的 AI 模型。它不会帮你摘要或评分代理写的东西，只是让一份又长又一直在改的文件保持好读，读的人是你。

[MarsDawn 做不到的事](/zh-hans/limits/)

## Siri 和快捷指令

在“快捷指令”App 中搜索 MarsDawn，可以找到三个操作：“新建 Markdown 文稿”（可选模板）、“添加笔记到收件箱”和“打开最近使用的文稿”。笔记会添加到你在“MarsDawn ▸ 设置… ▸ 笔记文件夹”选的文件夹中的 `Inbox.md`。

[为 Mac 而做](/zh-hans/native/)

## 页面打印出来之后

大家围着打印出来的页面开会，有人拿笔在页边写字，纸质记录收进档案。

[MarsDawn 影片，88 秒](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## 在你的 Mac 上试试

MarsDawn 可以免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。需要 macOS 26 以上。

[立即下载试用](https://apps.apple.com/app/id6812925073)

试用怎么运作：[免费试用，买一次就好](/zh-hans/pay-once/)。刻意不做的事：[MarsDawn 做不到的事](/zh-hans/limits/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
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
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
