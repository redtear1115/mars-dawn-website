# 命令行工具

免费的 `marsdawn` 命令行工具：从终端或 LLM agent 把 Markdown 导出成 PDF；装了 MarsDawn app 的话，也能用它打开文件。

**marsdawn 免费、另外发布，不通过 Mac App Store。**用 Homebrew 安装，在 Apple 芯片的 Mac 上装好就能直接使用。`export` 可以单独使用；`open` 需要 MarsDawn app。

要从 AI agent 或脚本调用 marsdawn？请看[给 AI agent 的 marsdawn 参考](/zh-hans/cli/agents/)，里面有 JSON 输出、Schema 和所有退出代码。

## 安装

使用 [Homebrew](https://brew.sh)：

```
brew tap redtear1115/tap && brew install marsdawn
```

在用写程序的 agent 吗？[加上 marsdawn skill](/zh-hans/cli/skill/)：一个文件，教它把自己写的文稿在 MarsDawn 里打开给你检阅，也能导出 PDF。

在 Apple 芯片的 Mac 上，Homebrew 会直接安装预先构建好的版本，几秒就完成，不需要另外安装任何东西。在 Intel Mac 上则会从源代码构建，需要几分钟，也需要 Xcode 26 以上（Swift 6.2）。这个工具需要 macOS 15 以上。

也可以从[源代码](https://github.com/redtear1115/mars-dawn-kit)用 Swift Package Manager 构建：

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

用 `marsdawn --version` 查看安装的版本。

## 命令

### marsdawn open

在 MarsDawn app 中打开一个或多个 Markdown 文件，方便审阅。需要先安装这个 app：没有安装时，`marsdawn open` 会以代码 3 结束，并说明没有安装 MarsDawn。`export` 不需要这个 app。

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
```

- `path:line`：请 MarsDawn 定位到那一行。后面再接列号，例如 `notes.md:120:8`，会被忽略。如果有文件的完整名称就是这个参数，则视为那个文件。
- `--line <n>`：同样的功能，只用于单一文件，也可以用在文件名本身以冒号加数字结尾的情况。只能搭配一个文件。
- 行号范围是 1 到 999999999。
- MarsDawn 1.0 会打开文件，但还不会跳到指定的行。
- `--json`：输出 JSON 结果，而不是文本。

行号功能从 marsdawn 0.3.0 开始提供。

### marsdawn export

把 Markdown 文件输出成分页的 PDF，使用和 MarsDawn 输出 PDF 相同的组件。不需要安装 MarsDawn app。相对路径的图片，会以输入文件所在的文件夹为准。

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`：PDF 的输出位置，默认是把输入文件的扩展名换成 `.pdf`。
- `--theme <dawn|classic|modern|vivid>`：预览主题的浅色版本，默认读取 `$MARSDAWN_THEME`，否则用 `dawn`。
- `--paper <a4|letter>`：纸张大小，默认 `a4`。
- `--allow-remote-images`：输出时加载网络图片，默认关闭。
- `--force`：如果输出文件已存在就直接覆盖。
- `--json`：输出 JSON 结果，而不是文本。

## $MARSDAWN_THEME 环境变量

没有传入 `--theme` 时，`export` 会读取 `$MARSDAWN_THEME` 环境变量，值必须是 `dawn`、`classic`、`modern` 或 `vivid` 其中之一，其他值都会改用 `dawn`。这个工具不会读取 App 本身的主题设置，因为读取其他 App 的容器可能触发 macOS 隐私提示。

## 覆盖文件的规则

`export` 默认不会覆盖已存在的输出文件，除非加上 `--force`。

## 退出代码

| 代码 | 意思 | 怎么处理 |
|---|---|---|
| `0` | 成功。 | 加了 `--json` 时，读 stdout 上的那一行 JSON |
| `2` | 找不到输入文件。 | 检查路径和文件名 |
| `3` | 尚未安装 MarsDawn（只有 `open` 会用到）。 | 安装 app，或改用不需要 app 的 `export` |
| `4` | 输出文件已存在（可加上 `--force`）。 | 加上 `--force` 覆盖，或用 `-o` 写到别处 |
| `5` | 输出失败。 | 读 JSON 结果里的 `message` |
| `64` | 使用方式错误，包括行号超出范围，或 `--line` 搭配了多个文件。 | 修正选项或值；这种错误以文本输出到 stderr，即使加了 `--json` 也一样 |

## --json 输出

成功时，`marsdawn open --json` 会输出 `ok`、`opened`（每个文件的 `path`，有指定行号时另含 `line`）与 `app`（App 路径）；`marsdawn export --json` 会输出 `ok`、`output`、`pages`、`theme`、`paper` 与 `diagramErrors`。失败时两者都会输出 `ok`、`error` 与 `message`。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。即将在 Mac App Store 上架。
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
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你检阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
