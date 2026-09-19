# 在别处看 Markdown，对比 MarsDawn。

如果你手边刚好开着 VS Code、浏览器或 Claude Desktop，用它们顺手看一眼 Markdown 文件也合理。以下是它们各自实际排版出什么、要花多少功夫才能看到，和在 MarsDawn 里打开同一份文件的比较。

## 一眼看完

|  | VS Code 预览 | 浏览器扩展 | Claude Desktop | MarsDawn |
|---|---|---|---|---|
| 打开磁盘上的 Markdown 文件 | 可以 | 可以，但要先允许访问文件 | 不行：Markdown 不在可上传的类型里 | 可以 |
| 打开第一个文件之前 | 安装 VS Code，一整套开发环境 | 安装扩展，再打开“允许访问文件网址” | 无法浏览磁盘上的文件 | 安装 MarsDawn |
| 为什么而做 | 写代码；预览只是众多面板之一 | 浏览网页 | 和 Claude 对话 | 阅读与编辑 Markdown |
| 用什么画出页面 | Electron：内含 Chromium 和 Node.js | 一整个浏览器 | Claude Desktop 本身 | 原生的 AppKit app，页面由 WebKit 绘制 |

## VS Code 内置的预览

在 VS Code 按 `⌘⇧V`，就会用内置的预览窗格排版出 Markdown 文件，免费，不用另外安装。从 VS Code 1.121（2026 年 5 月）开始，这个预览也能原生画出 Mermaid 图表——微软把一个 Mermaid 扩展并进了 VS Code 本体，以前需要另外装扩展，现在不用了。它做不到的：这是编辑器里的一个预览窗格，不是为了阅读而做的编辑器——窗格旁边还有文件树、终端和 VS Code 能显示的其他所有面板，而 VS Code 本身是 Electron app，你装的是一整套开发环境，不是一个用来读文件的工具。

## 看本机文件的浏览器扩展

看本机 `.md` 文件，没有哪一个浏览器扩展是主流：Local Markdown Viewer、Markdown Viewer、MarkView 等等做的事都差不多，没有哪一个是默认会装的。每一个都要先做同一件事才能打开任何文件：把该扩展的“允许访问文件网址”打开，因为浏览器默认不让扩展读取 `file://` 开头的页面。这个权限每个扩展只要开一次，但也很容易忘记自己开过，或忘记为什么要开。开了之后，文件会显示在浏览器标签页里——也就是说，看一个文件要开一整个浏览器。

## Claude Desktop 的文件预览

Claude Desktop 显示的是已经在 Project 或对话里的文件。它不是为了浏览磁盘上任意文件而做的——你能看的是对话里已经有的东西，不是一个可以一直开在旁边的笔记文件夹。Anthropic 自己列出[可以上传的文件类型](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)是 PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON 和 XLSX，里面没有 Markdown。

## 为了读一份文件，背后跑着一整套浏览器引擎

VS Code 是 Electron app：内置一套 Chromium 和 Node.js 运行环境，不是原生的 Mac app。走浏览器扩展这条路，则是真的在浏览器里运行。不管哪一种，看一份 Markdown 文件都要有一整套浏览器引擎在背后跑。MarsDawn 是原生的 AppKit app：没有内置的浏览器运行环境、直接打开任何本地文件，不用装扩展，也不用记得开过哪个权限。

## 接下来

- MarsDawn 也做不到的事：[这份清单](/zh-hans/limits/)。
- 今天就能免费把任何 Markdown 文件转成 PDF：[Markdown 转 PDF](/zh-hans/markdown-to-pdf/)。
- 和一个 Mac 原生的查看器比较：[MacMD Viewer 对比 MarsDawn](/zh-hans/vs/macmd-viewer/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。已在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [English](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
