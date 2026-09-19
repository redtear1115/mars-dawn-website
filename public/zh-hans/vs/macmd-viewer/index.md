# MacMD Viewer 对比 MarsDawn。

两者都是给 Mac 用的 app，都能把 Markdown 排版出来读。MacMD Viewer 打开 `.md` 文件，显示排好版的页面，但不能编辑它。MarsDawn 则是在同样的预览旁边放了编辑器，让你在同一个窗口里写和读。以下逐项比较两者的差异。

## 如果你只需要读，不需要编辑

如果你的工作就是读别人写好的 Markdown，完全不用碰源代码，MacMD Viewer 是合理的选择：它就是为这件事做的，现在就能买，也能在比较旧的 macOS 上跑。当阅读不是全部的工作时，MarsDawn 才值得，因为 agent 写的 Markdown 通常还要再改一轮。

## 各自能做什么

- **编辑：**MacMD Viewer 设计上就是只读。MarsDawn 边编辑源代码边在旁边排版，打字的同时就看得到改动。
- **预览主题：**MacMD Viewer 内置 12 种文档主题。MarsDawn 有四种：Dawn、Classic、Modern 和 Vivid，各有浅色与深色。
- **图表与数学公式：**两者都能画出 Mermaid 图表、也都有代码高亮。MarsDawn 还能排版 KaTeX 数学公式；MacMD Viewer 自己的介绍页没有提到数学公式排版。
- **Finder 集成：**两者都有 Finder 的快速查看扩展功能，对 `.md` 文件按空格键就能看到排好版的页面。
- **PDF 与打印：**两者都能把排好版的页面输出或打印成 PDF。
- **系统需求：**MacMD Viewer 需要 macOS 14（Sonoma）以上。MarsDawn 需要 macOS 26（Tahoe）以上。
- **语言：**MarsDawn 的界面有英文、繁体中文、简体中文和日文。MacMD Viewer 自己的资料没有写出界面语言，这页就不比较这一项。

## 价格与购买方式

- **从哪里买：**MacMD Viewer 从自己的网站直接下载，也上架 Homebrew 和 Setapp，但不在 Mac App Store 上；MarsDawn 只在 Mac App Store 上架。
- **价格：**MacMD Viewer 一台 Mac 一次 USD 19.99（三台的组合包和批量授权更贵）。MarsDawn 免费下载，之后以 USD 4.99 一次解锁。
- **先试用：**MacMD Viewer 没有免费试用，直接购买改用 14 天内可退款的保证。MarsDawn 在你付费之前，先给你 14 天的试用。
- **退款与更新：**MacMD Viewer 的退款和更新都在它自己的网站上处理。MarsDawn 通过 Apple 购买，退款和更新都走 Apple 的标准流程。
- **账户：**两者都不需要账户就能使用。

## 现在就能免费试试看

MarsDawn 即将在 Mac App Store 上架，现在还没开卖。在那之前，免费的 `marsdawn` 命令行工具今天就能把任何 Markdown 文件转成 PDF，Mermaid 图表和代码高亮都在，而且不需要安装其他东西：

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 接下来

- 完整步骤：[Markdown 转 PDF](/zh-hans/markdown-to-pdf/)。
- MarsDawn 做不到的事：[这份清单](/zh-hans/limits/)。
- 命令行工具的所有选项：[命令行工具](/zh-hans/cli/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 原生的 Mac Markdown 编辑器，有实时预览、Mermaid 图表和 PDF 输出，为读 AI agent 写的 Markdown 而做。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在 Finder 用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
