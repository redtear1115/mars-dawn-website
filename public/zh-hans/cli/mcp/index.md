# 调用 marsdawn 的三种方式。

MarsDawn 没有自己的 AI 模型：它是为了审阅 Markdown 而做的，不是用来写的，所以是哪个 agent 或模型写出这份 Markdown 并不重要。agent 或脚本调用 `marsdawn` 有三种方式，最后都会运行同一个 `export`。

**挑你的工具支持的那一种：免费的 `marsdawn` CLI、纯 Markdown 的 skill 文件，或是 [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) 这个 MCP 服务器。**三者都调用同一个 `marsdawn export`，返回一样的 JSON 结果。

## CLI

`marsdawn export notes.md --json` 可以被任何能运行 shell 命令的 agent 或脚本调用，因为是命令行工具，天生就跟模型无关。它返回的每个字段都写在[给 AI agent 的 marsdawn 参考](/zh-hans/cli/agents/)里，那一页是 JSON schema 的权威来源，下面另外两种方式都会连回去。

## Skill 文件

如果你的 agent 读的是纯 Markdown 指令，而不是直接运行 shell——目前是 Claude Code——[marsdawn skill](/zh-hans/cli/skill/) 就是一个文件，教它安装 marsdawn、运行 `export`、读懂结果。因为它就是纯 Markdown，其他会读指令文件的 agent 也能用同一个文件。

## MCP 服务器

[marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) 是另一个独立、公开、Apache-2.0 授权的 repository。它是一个只有一个工具的 MCP 服务器，`export_markdown_to_pdf`，包住 `marsdawn export --json`：把 MCP 客户端指向它，工具调用返回的 JSON 和 CLI 一样。

- **获取方式：**以 MCP Bundle（`marsdawn.mcpb`）的形式附在[GitHub release](https://github.com/redtear1115/marsdawn-mcp/releases) 上，或从源代码以 stdio 运行服务器。
- **Registry：**还没上架 MCP Registry（目前版本：0.1.0）。要靠 registry 搜索找到它之前，请先到 repository 确认目前状态。
- **托管：**只能自架，没有代管服务。服务器跑在你自己的机器上，就在 marsdawn 旁边。
- **系统要求：**macOS、marsdawn 0.5.0 以上，以及运行服务器需要的 Node.js 20 以上。

## 同一个 export，三扇门

不管从哪个界面调用，底层行为都一样：同一套输出程序、同样的主题和纸张大小，Mermaid 图表画不出来时也是同样的 `diagramErrors`。这页不重复那份规格——[给 AI agent 的 marsdawn 参考](/zh-hans/cli/agents/)里有完整内容。

## 接下来

- 完整 JSON schema 和所有退出代码：[给 AI agent 的 marsdawn 参考](/zh-hans/cli/agents/)。
- 给 Claude Code 等 agent 用的一个文件：[marsdawn skill](/zh-hans/cli/skill/)。
- 精简的 JSON 结果为什么对 agent 自己的 context 很重要：[节省 token 的审阅方式](/zh-hans/token-efficient-review/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 原生的 Mac Markdown 编辑器，有实时预览、Mermaid 图表和 PDF 输出，为读 AI agent 写的 Markdown 而做。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [English](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
