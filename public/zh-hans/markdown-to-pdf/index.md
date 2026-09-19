# Markdown 转 PDF 工具：在 Mac 上用命令行转换。

免费的 `marsdawn` 工具只要一个命令，就能把 Markdown 文件转成 PDF。表格、数学公式、Mermaid 图表和代码高亮，都会照源文件的样子呈现，而且不需要安装其他东西，连 MarsDawn app 都不用。

## 安装

```
brew install redtear1115/tap/marsdawn
marsdawn --version
```

在 Apple 芯片的 Mac 上，Homebrew 会直接安装预先构建好的版本，几秒就完成。在 Intel Mac 上则会从源代码构建，需要几分钟，也需要 Xcode 26 以上。这个工具需要 macOS 15 以上，`marsdawn --version` 会输出你装到的版本。

## 存一份文稿

把下面的内容贴进一个叫 `plan.md` 的文件：

````
# 计划：让输出更快

这份计划由 agent 撰写，你审阅后再把它转成 PDF。

## 步骤

| 步骤 | 负责 | 状态 |
|------|------|------|
| 找出慢的页面 | Agent | 完成 |
| 缓存算好的图表 | Agent | 审阅中 |

目标是 50 页的文稿在 $t < 2\,\text{s}$ 内完成：

$$
t_{\text{total}} = \sum_{i=1}^{n} t_i
$$

```mermaid
graph LR
  草稿 --> 审阅 --> 发布
```

```swift
let pdf = try export("plan.md")
```
````

## 导出

```
marsdawn export plan.md
```

它会在源文件旁边写出 `plan.pdf`，并输出存放的位置：

```
Exported /Users/you/plan.pdf (1 page)
```

这是那一页，截取自 `marsdawn` 0.5.0 的实际运行结果：

![导出的 PDF：标题、步骤表格、行内与独立的数学公式、“草稿、审阅、发布”流程图，以及一行高亮的 Swift 代码。](/assets/cli/plan-zh-hans.png)

## 选主题、纸张大小和文件名

```
marsdawn export plan.md --theme classic --paper letter -o handout.pdf
```

- `--theme`：dawn、classic、modern 或 vivid，使用主题的浅色配色。没有指定时，`export` 会用 `$MARSDAWN_THEME`，再来才是 dawn。
- `--paper`：a4 或 letter，默认是 a4。
- `-o`：PDF 要写到哪里，而不是写在源文件旁边。
- `--allow-remote-images`：转换时加载网络上的图片。没加这个选项就不会加载。

## 如果没有成功

- `A full installation of Xcode.app 26.0 is required to compile this software.` 代表 Homebrew 正在从源代码构建 `marsdawn`，这在 Intel Mac 上会发生。从 App Store 安装 Xcode 26 以上，再重新安装一次。
- `marsdawn: No such file: …` 路径没有指到文件。确认文件名，或在文件所在的文件夹里运行命令。
- `… already exists. Pass --force to replace it.` 同名的 PDF 已经存在。加上 `--force` 覆盖它，或用 `-o` 写到别的地方。
- `Error: The value '…' is invalid for '--theme <theme>'.` 主题或纸张大小不是它认得的。主题有 dawn、classic、modern 和 vivid，纸张是 a4 或 letter。

## 接下来

- 所有选项和它输出的 JSON：[命令行工具](/zh-hans/cli/)。
- 让写程序的 agent 帮你做这件事：[marsdawn 的 agent skill](/zh-hans/cli/skill/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 原生的 Mac Markdown 编辑器，有实时预览、Mermaid 图表和 PDF 输出，为读 AI agent 写的 Markdown 而做。已在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你检阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [English](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [日本語](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
