# 隐私政策

macOS 的 Markdown 编辑器 MarsDawn 如何处理你的信息。

最后更新：2026-09-19

**MarsDawn 不收集任何关于你的数据。**没有账户、没有分析、没有广告，也不追踪。你的文稿与设置都留在你的 Mac 上。

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

MarsDawn 不向任何人收集数据，包括儿童。

## 购买

MarsDawn 将通过 Mac App Store 销售，付款会由 Apple 依其条款处理，开发者不会取得你的付款信息。

## 政策变更

如果 MarsDawn 未来处理数据的方式有所改变，本页会在该版本推出前更新，页面顶部的日期也会一并更改。

## 联系我们

隐私相关问题：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他页面

- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
