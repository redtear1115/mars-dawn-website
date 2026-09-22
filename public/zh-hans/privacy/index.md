# 隐私政策

macOS 的 Markdown 编辑器 MarsDawn 如何处理你的信息。

最后更新：2026-09-23

**MarsDawn app 不收集任何关于你的数据。**没有账户、没有广告，也不追踪。你的文稿与设置都留在你的 Mac 上。

## 这个网站

App 和这个网站是两件事。App 不收集数据。会记下访问的，只有 marsdawn.southern-light.dev。

**目前还没有开启。**这个网站今天不会把任何东西送到分析服务。下面是开启之后会记录的内容，先写在这里，让第一笔记录出现之前，说明就已经公开。开启的那天，删掉这一段，其余留下。

开启之后：

- **页面浏览。**服务器会记录某个页面被请求，以及浏览器有送来源网址时的那个网址。
- **经由本站转出去的点击。**经由本站跳转才离开的点击会被记录，例如前往 Mac App Store 的链接。目的地是固定网址，跳转不会附加追踪参数。
- **不会记录的。**没有 cookie，也不使用浏览器的本地存储，页面里没有分析脚本。没有账户，因为这个网站不需要账户。没有你的文稿，也没有你打的字。没有跨站广告，也不会建立你的个人档案。App 向 `/themes/` 索取主题文件的请求会被跳过，不会送出。
- **一次访问只是一次浏览。**每个请求配一组只用一次的随机编号，用完即弃。网站无法在你下次来时认出你。
- **数据去哪里。**这些事件由网站自己的服务器送给 PostHog（美国区）。你的浏览器不会连到 PostHog。PostHog 会将这些事件保留 12 个月。完整的 IP 地址不会转发过去。
- **主机。**网站放在 Cloudflare 上。和任何主机一样，它在响应请求时会看到你的 IP 地址。那是主机自己的日志，不是上面的分析。

## 留在你 Mac 上的东西

- **你的文稿。**MarsDawn 只读写你打开、保存或选择的文件与文件夹，App 不会把它们上传到任何地方。
- **你的设置。**外观、预览主题、窗口布局和图片偏好，都存在 App 自己的偏好设置里。
- **你授权的文件夹。**当你让 MarsDawn 显示某个文件夹里的图片或网页文件，或选择笔记文件夹时，App 会保存 macOS 书签，以便之后再次打开。你在侧边栏打开的文件夹，MarsDawn 会保持可读写，直到你在设置中移除为止，而不只是在那个窗口开着的时候。你随时可以到 MarsDawn › 设置… 移除。

## MarsDawn 什么时候会连上网络

MarsDawn 可以完全离线使用，只有在**你自己选择时**，才会为引用网络内容的文稿连网：

- **Markdown 文稿。**网络图片默认不加载，只有在你按下预览中的“载入图像”，或在设置中打开“自动载入网络图像”后才会加载。Markdown 文稿引用的其他网络内容一律不加载。
- **HTML 文稿。**HTML 文稿打开时是静态的：它的代码不会运行，也不会从网络加载任何东西。如果文稿含有可以运行的代码，你可以针对这份文稿选择“显示 › 运行这份文稿”。之后它自己的代码会一直运行，直到你停止它、文稿重新加载，或关闭窗口为止。这个选择不会被记住，也不是一项设置。运行期间，这份文稿可以通过网络发送数据，并读取它所在文件夹及其子文件夹中的图片、样式表、字体与媒体文件。从网络下载的代码一律不会运行。

MarsDawn 只通过 https 加载网络内容。http 地址一律不会加载，任何设置都无法打开，MarsDawn 也不会自动改写成 https。在 Markdown 文稿中，预览会以占位图标代替。

加载网络内容时，你的 Mac 会直接向存放内容的服务器发出请求。和所有网络请求一样，这些服务器会看到你的 IP 地址与请求的内容。MarsDawn 的开发者不会收到任何这类信息。

在预览中点击的链接会用你的默认浏览器打开，适用该浏览器的隐私做法。音频与视频不会自动播放。

## Siri、快捷指令和 Spotlight

MarsDawn 提供 Siri、快捷指令 App 和 Spotlight 可用的动作，例如添加文稿或加入笔记。使用时，你提供的文本会交给你 Mac 上的 MarsDawn，并只存到动作指定的位置（新文稿，或你所选笔记文件夹中的 `Inbox.md`）。对 Siri 说的话由 Apple 依 [Apple 隐私政策](https://www.apple.com/legal/privacy/) 处理。

## 输出 PDF 和打印

输出 PDF 和打印都在你的 Mac 上完成。PDF 存在你选择的位置，打印则通过 macOS 送到你选的打印机。

## marsdawn 命令行工具

另外发布、可自由选用的 `marsdawn` 命令行工具，同样完全在你的 Mac 上运行：只读取你指定的 Markdown 文件，并写出你要求的 PDF。只有在加上 `--allow-remote-images` 时才会加载网络图片。

## 儿童

MarsDawn app 不向任何人收集数据，包括儿童。网站上记下的访问不是账户，也不用来辨认任何人。

## 购买

MarsDawn 将通过 Mac App Store 销售，付款会由 Apple 依其条款处理，开发者不会取得你的付款信息。

## 政策变更

如果 MarsDawn 未来处理数据的方式有所改变，本页会在该版本推出前更新，页面顶部的日期也会一并更改。

## 联系我们

隐私相关问题：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
