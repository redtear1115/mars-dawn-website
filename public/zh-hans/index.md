给建造者的前线工具

# 拿稳地图。读过黎明。

给要掌舵 agentic 开发的人用的 Markdown。

页面上有一个可以操作的 MarsDawn 窗口，内容是 App 内置欢迎指南的一段。可以从四个预览主题（黎明、典雅、流行、活泼）和三种布局（源代码、并排、预览）里选。

## 读 agent 写的 Markdown。

1. **Agent 动笔。**你的代码助手或写作 agent 先写出 Markdown：README、规格文档，或一份笔记。
2. **你在 MarsDawn 里读。**打开文件，看排版后的页面，Mermaid 图表和代码高亮都在，旁边就是源代码。
3. **Agent 修改。**提出修改意见，agent 改好之后，再打开来读一次。

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

## App 实际的样子

### [为 Mac 而做](/zh-hans/native/)

![MarsDawn 的并排布局：左边是 Markdown 源代码，右边是排版后的页面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

这张截图里：

1. 原生的 Mac 窗口。
2. Mac 原生的文本编辑器，附 Markdown 语法高亮。
3. ⌘1 源代码、⌘2 并排、⌘3 预览。
4. 页面会随着打字更新。

### [输出 PDF](/zh-hans/pdf/)

![用 MarsDawn 输出的 PDF，在内置的 PDF 查看器中打开，旁边有页面缩略图。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

这张截图里：

1. Mermaid 图表直接画进 PDF。
2. 代码保留语法高亮。

## 其他页面

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
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [English](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. On the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で配信中です。
