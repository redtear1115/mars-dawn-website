# 更新记录

Mac App Store 上的 MarsDawn App，以及免费的 marsdawn 命令行工具，每个版本改了什么。App 的日期是该版本在 Mac App Store 上架的日子。

接下来要做的事列在[路线图](/zh-hans/roadmap/)。

## MarsDawn App

### MarsDawn 1.1.1

2026 年 10 月 15 日

- 在德语、日语、西班牙语和法语中，「设置 ▸ 外观 ▸ 获取更多主题…」的场景筛选改为标示为「场景」的弹出式菜单，五个选项才放得下。英语、韩语和中文仍使用分段控件。
- 主题从主题图库下架时，「获取更多主题…」中的提示现在会显示主题名称（例如 Inkwell Ivory），不再显示内部 id。
- 按 GitHub 写法编写的可折叠 details 区块，在预览和「快速查看」中会先折叠并显示摘要，点按后才展开。导出 PDF 时仍会打印每一部分的内容。
- 从访达、程序坞、「文件 ▸ 打开…」或 marsdawn open 命令打开的文稿，以及新建的文稿，现在都会成为最前面窗口的标签页。要保持以前的方式，可以在「设置 ▸ 外观」中选择「跟随系统设置」。

### MarsDawn 1.1.0

2026 年 10 月 9 日

- 「设置 ▸ 外观」新增「获取更多主题…」按钮，可打开主题图库，挑选更多预览主题。安装后，主题会出现在「显示 ▸ 预览主题」中，也可以随时移除。主题图库只在打开时才会联网。
- 在访达中用「快速查看」预览时，现在会使用你选的主题，不再一律使用黎明主题。
- 「快速查看」也会跟随 MarsDawn 的外观设置：选「浅色」或「深色」就固定使用该外观，即使 Mac 设为另一种；选「系统」则跟随 Mac。
- 窗口标题中的 git 标记，现在遇到已暂存但尚未提交的文件会显示「+」，以前看起来像是没有更改。
- 在预览中点按指向其他 Markdown 文件的链接，例如 [notes](notes.md#plan)，现在会打开该文件；如果已经打开就带到最前面，并滚动到对应的标题。文件若不在边栏的文件夹内，MarsDawn 会先请你将该文件夹添加到边栏，添加后再点按一次链接。

### MarsDawn 1.0.2

2026 年 10 月 7 日

- 修正：第一次切换布局，或显示、隐藏边栏时，编辑器不会再向上偏移一小段。
- 无法绘制的 Mermaid 图表现在会显示完整的错误信息；知道行号时，点按错误信息就会跳到编辑器中该图表所在的行。
- 繁体中文、简体中文和西班牙语的菜单用词，改为与 macOS 内置的翻译一致，例如「保存为…」。

### MarsDawn 1.0.0

2026 年 10 月 5 日

首次发布。

## marsdawn 命令行工具

0.5.1 以前的版本不列。

### marsdawn 0.7.2

2026 年 10 月 20 日。手册布局、提示块，以及日文字体。

- `--layout` 的值改为 `handbook`，与 app 的「手册」（Handbook）布局同名：`marsdawn export --layout handbook`。`--layout manual` 仍可使用，但已弃用。
- 预览和导出的 PDF 都会显示提示块：GitHub 的 alert（例如 `> [!NOTE]`、`> [!WARNING]`），以及 HackMD 的容器（例如 `:::info`、`:::warning`）。`:::spoiler` 会成为可折叠的区块。
- 日文文稿的假名和汉字会改用日文字体。语言取自 front matter 的 `lang: ja`；没有写时，按正文中假名的比例判断。
- 在终端中成功运行 `export` 或 `open` 之后，如果代理技能没有安装或已经过期，marsdawn 会在 stderr 显示一次提示。stdout 和 `--json` 的输出都不变。设置 `MARSDAWN_NO_SKILL_HINT=1` 就不再提示。

### marsdawn 0.7.1

2026 年 10 月 20 日。手册布局，以及文件大小上限。

- `marsdawn export --layout manual` 导出成手册：页边距更宽、装订边留 25 mm，每个一级标题从新的一页开始；另外有封面（取自 front matter 的 title、subtitle、version、date、author 和 logo）、列出一、二级标题并附页码的目录、`n / N` 页码，以及 PDF 书签。目录页的标题可以用 `--toc-title` 指定。默认仍是 `--layout document`。
- 单独一行的 `<!--BREAK-->` 会从新的一页开始，两种布局都适用。
- `marsdawn export` 不处理超过 16 MiB 的文件：以代码 5 结束，加上 `--json` 时报告 `input_too_large`，不写出任何文件。
- 预览页会移除 script 和 noscript 元素；Mermaid 重绘时保留图表自己的 SVG。
- 解码后是 `=` 或 `^` 的字符引用（例如 `&#61;`）不再和 HackMD 标记配对。

### marsdawn 0.7.0

2026 年 10 月 18 日。HackMD 语法、换行，以及超大文稿的上限。

- 支持 HackMD 的行内标记：`==mark==`、`^sup^` 和 `~sub~`。单独成段的 `[TOC]` 会变成目录；HackMD 写法的图片尺寸会生效；嵌入标签会变成普通的 https 链接；代码块的语言会先读出来，再处理 `js=` 这类 HackMD 选项。
- `marsdawn export --breaks` 会把段落内的每个换行都当作换行，和 HackMD 一样。不加时，两个中文或日文字符之间的换行会去掉，让前后两行连成一句；韩文的词与词之间本来就有空格，所以保留空格。
- 超大文稿在预览和导出的 PDF 中都有上限：单个代码块超过 128K 字符就不做语法高亮，整份累计超过 256K 字符后也不再高亮。每次更新最多绘制 100 个 Mermaid 图表、渲染 1,000 个数学公式；其余图表显示源代码并附上说明，即使之前绘制过也一样。
- 时序图中，`rect` 区块里的消息标签，描边底色改用该区块的颜色。
- 表格正上方有脚注引用时，`marsdawn export` 不再崩溃。
- `marsdawn skill --install` 无法创建文件夹或写入文件时，以代码 7（`skill_install_failed`）结束，原有的 SKILL.md 保持不变。

### marsdawn 0.6.4

2026 年 10 月 13 日。可折叠的 `<details>` 区块。

- GitHub 风格的 `<details>` 区块里有空行时，也会显示为一个可折叠的区块；预览和导出的 PDF 都一样。以前遇到第一个空行就会断开。
- 导出 PDF 时，会先把每个 `<details>` 区块展开再打印（front matter 除外）。
- 展开或折叠 `<details>` 区块时，预览会保持原来的滚动位置。

### marsdawn 0.6.3

2026 年 10 月 6 日。MarsDawn 在 Mac App Store 上架。

- 没有安装 app 时，`marsdawn open` 会指向 Mac App Store 上的 MarsDawn。
- README 和代理技能会教 `marsdawn open .` 与 `--folder`：MarsDawn 1.0.0 会把文件夹显示在窗口的侧边栏。

### marsdawn 0.6.1

2026 年 9 月 29 日。检查主题。

- `marsdawn theme validate` 会用 app 采用的规则检查 `theme.json`。主题有效时以代码 0 结束，无效时以代码 1 结束，并列出每个问题。加上 `--require-complete` 时，还会要求语法高亮和图表的颜色。
- `marsdawn theme css` 会输出预览为有效主题使用的 CSS；`marsdawn theme preview` 会用这个主题把一份示例文稿渲染成 PNG，浅色或深色都可以。

### marsdawn 0.5.4

2026 年 9 月 26 日。Mermaid 修复、图表错误的行号，以及安装 skill。

- 时序图中，消息标签跨过其他参与者的生命线时，文字仍清晰可读；预览和导出的 PDF 都是如此。
- `marsdawn export` 能处理包含大量 Mermaid 图表的文稿。一份有 50 张图表、以前会以代码 5 结束的文稿，现在可以顺利导出。
- `marsdawn export --json` 新增 `diagramErrorDetails`，用行号标出每个图表错误：图表在文稿中从第几行开始；Mermaid 指出行号时，也给出错误本身所在的行。
- `marsdawn skill --install` 会把代理技能安装到 `~/.claude/skills/marsdawn/SKILL.md`，供 Claude Code 使用；加上 `--dir` 可以改装到其他文件夹。已有相同的文件时不会改动它；内容不同时，只有加上 `--force` 才会替换，否则以代码 64（`skill_differs`）结束，不做任何改动。

### marsdawn 0.5.3

2026 年 9 月 25 日。文件夹状态、完整的 Mermaid 错误信息，以及其他小修复。

- `marsdawn open --folder` 可以报告文件夹最后的状态。配合会回报状态的 app，它最多等待 `--wait` 秒（默认 2 秒），`--json` 会给出 `attached`、`needsUser` 等状态。
- Mermaid 图表无法解析时，会显示 Mermaid 完整的错误信息，不再只有第一行；行号也改为从文稿开头算起。
- 查找 front matter 区块的结尾时，最多只查找 1,000 行；未闭合的区块，不再让大型文稿每次都被扫描到最后。
- app 可以在导出 PDF 和打印时，为脚注的返回链接提供翻译后的标签。这个标签不会打印在页面上，`marsdawn export` 仍使用英文。
- 内置的 highlight.js 现在和 KaTeX、Mermaid 一样，记录版本、来源与 SHA-256。

### marsdawn 0.5.2

2026 年 9 月 24 日。脚注、对比度与文件夹。

- 导出的 PDF 会呈现脚注：引用有编号，脚注内容接在正文之后。
- 所有主题的浅色与深色都符合 WCAG AA 对比度。Classic 改为黑白。
- `marsdawn skill` 会打印与已安装的 marsdawn 相符的代理技能。
- 找到的 MarsDawn 无法显示文件夹时，`marsdawn open` 会以代码 6（`app_cannot_open_folders`）结束，不再报告成功。
- 画进导出页面的占位文字，也有德文、法文、西班牙文和韩文。
- 相对路径很长时，图片占位文字不再显示它背后的绝对路径。
- `MARSDAWN_APP_PATH` 只有指向 MarsDawn app 时才会采用。

### marsdawn 0.5.1

2026 年 9 月 19 日。PDF 导出，以及从命令行打开文件。

- 导出的 PDF 中，中文、日文与韩文的文字层已修正。
- `marsdawn open --background` 会打开文件，但不会把 MarsDawn 带到最前面。
- `marsdawn open` 可以指定一个文件夹，MarsDawn 会把它显示在窗口的侧边栏（MarsDawn 1.0.0 起）。

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
- [2026 Mac Markdown 查看器推荐](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
