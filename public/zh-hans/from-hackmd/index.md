# 从 HackMD 搬到 Mac

你的笔记本来就是 Markdown，不用转换。看你要搬多少，选一条路。图片要另外处理，删除 HackMD 上的内容之前，请先读“图片”那一段。

这一页是 2026 年 11 月用 HackMD 免费账户实测的。HackMD 可能会变，付费方案和团队工作区我们没有测。

| 你想要 | 走这条 |
|---|---|
| 搬全部笔记 | 下载所有笔记 |
| 搬已经在 GitHub 上的笔记 | clone 仓库 |
| 搬一两篇 | 下载单篇 |

## 下载所有笔记

HackMD 的笔记设置里有 Download all notes，个人和团队空间都有。下载下来是一个 .zip，一篇笔记一个 .md，文件名是笔记标题。

- 文件夹不会保留，所有笔记都在最上层。
- 图片不在里面，.md 里仍然是网址。
- 包含标题和标签的选项默认打开，会在每篇最前面加一段 front matter。关掉后就和笔记原文相同。

解压缩后，在 MarsDawn 选择“文件 ▸ 打开文件夹…”，打开那个文件夹。

## clone 仓库

HackMD 的 GitHub 同步是一篇笔记对一个文件，所以推送过的笔记已经在仓库里。clone 下来，用“文件 ▸ 打开文件夹…”打开，边栏会显示仓库和分支。

还没接 GitHub 的笔记，不用为了搬家特地接。每篇都要各自绑定，免费版每月可以推送 20 次。在免费个人账户上，我们没看到一次推送整个工作区的入口。

搬完之后，以仓库为准。从 HackMD 推送会直接覆盖 GitHub 上的内容，就算 GitHub 上的比较新也一样，而且不会警告。

## 下载单篇

笔记菜单可以下载 .md 或 .html。选择 .md，再用 MarsDawn 打开。

## 图片

上传到 HackMD 的图片，网址是 `https://hackmd.io/_uploads/...`。谁看得到，跟着笔记的权限走。

| 你的笔记是 | 搬到 Mac 后 | 怎么处理 |
|---|---|---|
| 公开 | 图片从 HackMD 载入 | 在预览中点按“载入图像”，或打开“设置 ▸ 图像 ▸ 自动载入网络图像” |
| 私人 | 图片会返回错误，因为 MarsDawn 没有登录 HackMD | 在已登录的浏览器里把图片存下来，放在 .md 旁边，再改路径。或者把笔记改成公开，前提是所有人都可以看 |

- **旧笔记** 的图片可能是 `i.imgur.com` 网址。
- **删除笔记，图片也会失效。** 网址之后打不开，所以先搬好图片再删除。

如果 MarsDawn 读不到文件旁边的图片，用预览里的按钮授权那个文件夹。

## 读起来的样子

HackMD 的语法大多照样能读：`==高亮==`、`^上标^`、`~下标~`、`[TOC]`、`=300x200` 这类图片尺寸、Mermaid 和 KaTeX。`{%youtube %}` 会显示成链接。想和 HackMD 一样保留每个换行，请打开“设置 ▸ 外观 ▸ 保留单个换行”。

`:::` 区块也看得到。`:::info`、`:::success`、`:::warning`、`:::danger` 会显示成有色条的区块，上面有标题，默认是附注、提示、警告、小心；在名称后面自己写标题的话，就用你写的。`:::spoiler` 会显示成点一下才展开的可折叠区块。其他名称的 `:::` 区块，或少了结尾 `:::` 的，会按原文显示。

有几个地方不一样：

- `++下划线++` 和 `:sparkles:` 这类 emoji 代码会按原文显示。
- `{%hackmd id %}` 不会展开。
- `<i class="fa ...">` 图标不会出现。

## 给脚本用：hackmd-cli

`hackmd-cli` 没有一次导出全部的命令。它一次导出一篇，内容打印在屏幕上，所以要先列出笔记，再逐篇跑循环。你需要 Node.js、`jq`，以及在 HackMD 设置页创建的 API token。不需要脚本的话，Download all notes 比较简单。

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<你的 token>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **文件夹带不过来。** 笔记列表没有写笔记在哪个文件夹，所以文件都会放在同一层。
- **图片仍是 `hackmd.io` 链接。** 请按上面“图片”那一段处理。
- **文件名是笔记 ID，** 不是标题。
- **免费版每 30 天可以调用 API 400 次。** 列表 1 次，每篇笔记再 1 次。

我们只在笔记很少的账户上试过，不知道列表很长时会怎样。用完请到 HackMD 设置页删除 token。

## 一起写的话

MarsDawn 没有多人同时编辑。需要共同编写的话，继续用 HackMD。团队把文稿放在 git 的话，每个人都能用自己的 MarsDawn 打开同一个仓库，一起完成同一份文稿。请看团队用 git 一起审文稿。

## 常见问题

### 可以一次下载全部 HackMD 笔记吗？

可以。Download all notes 会给你一个 .zip，里面都是 .md。文件夹不会保留，也不含图片。

### 为什么在 MarsDawn 看不到图片？

MarsDawn 默认不载入网络图片，要点按“载入图像”。如果是私人笔记，图片载入不了，请存到文件旁边。

### 一定要离开 HackMD 吗？

不用。要一起写，HackMD 还是比较好的选择。MarsDawn 是让你在 Mac 上读和审。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 检查代理写的 Markdown、JSON、YAML：Mac 原生 app，实时预览、Mermaid、KaTeX、快速查看、PDF。免费试用，之后一次 USD 4.99。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown、JSON、YAML 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可拿去开会或存档。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [打印与 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上先预览，再把 Markdown 打印或存储为 PDF；有文稿、手册、讲义三种布局，Mermaid 图表和代码高亮都会保留。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、iPhone 和 iPad 上不能编辑、没有插件、不需要账户；可以换主题，但不能自定义 CSS。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [Mac 上怎么打开 md 文件](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [在 Mac 上预览 Mermaid](https://marsdawn.southern-light.dev/zh-hans/mermaid-preview-mac/index.md): 在 Mac 上预览 Mermaid 图表：源代码旁边实时画出来，快速查看和导出 PDF 也看得到。图表写错时，会显示错误信息和出错的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [拷贝给 AI](https://marsdawn.southern-light.dev/zh-hans/copy-for-ai/index.md): 选中文本，连同文件路径和行号一起拷贝，粘贴到 Claude Code 或任何代理。在 Mac 上就能做，不用打开 IDE，也不用装插件。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MarsDawn 对比：VS Code 预览、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日（MarsDawn 的 PDF 格子更新于 2026 年 11 月 7 日）；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
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
- [English](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/from-hackmd/index.md): Lade deine HackMD-Notizen als .md herunter und lies sie in MarsDawn auf dem Mac. Alle Notizen herunterladen, ein GitHub-Repository nutzen und Bilder retten.
- [Français](https://marsdawn.southern-light.dev/fr/from-hackmd/index.md): Téléchargez vos notes HackMD en .md et lisez-les dans MarsDawn sur votre Mac. Comment tout télécharger, partir d’un dépôt GitHub et garder vos images.
- [Español](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
- [한국어](https://marsdawn.southern-light.dev/ko/from-hackmd/index.md): HackMD 노트를 .md로 내려받아 Mac의 MarsDawn에서 읽는 방법입니다. 모든 노트 다운로드, GitHub 저장소에서 옮기기, 이미지 처리 방법을 정리했습니다.
