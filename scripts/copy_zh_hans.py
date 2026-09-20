"""Simplified Chinese (zh-Hans) copy for the MarsDawn site, translated from the zh-hant copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': '隐私政策', 'support': '支持', 'cli': '命令行工具', 'agents': '给 AI agent 的 marsdawn 参考', 'using_cli': '使用 CLI', 'markdown-to-pdf': 'Markdown 转 PDF', 'skill': '给 agent 的 skill', 'view-markdown-on-mac': '在 Mac 上看 Markdown', 'vs-macmd-viewer': 'MacMD Viewer 对比 MarsDawn', 'updated': f"最后更新：{k.UPDATED}", 'tagline': '读 agent 写的 Markdown。', 'footer_store': 'MarsDawn 即将在 Mac App Store 上架。', 'more': '其他页面', 'yours': '你写的内容留在你的 Mac 上', 'pay-once': '免费试用，买一次就好', 'pdf': '输出 PDF', 'native': '为 Mac 而做', 'limits': 'MarsDawn 做不到的事', 'mcp': 'MCP 服务器', 'token-efficient-review': '节省 token 的审阅方式', 'vs-markdown-preview-tools': '在别处看 Markdown，对比 MarsDawn', 'themes': '预览主题与 PDF 导出', 'sharing-exported-pdfs': '分享导出的 PDF', 'reviewing-ai-output': '为什么 AI 写的东西还是需要人读过'}
    store_chip = '即将在 Mac App Store 上架'
    schema_notes = {'export': 'export 成功', 'open': 'open 成功，marsdawn 0.3.0 以后', 'error': '两个命令的失败结果', 'open_v1': 'open 成功，marsdawn 0.2.x，当时 <code>opened</code> 是路径清单'}
    example_plan = '# 计划：让输出更快\n\n这份计划由 agent 撰写，你审阅后再把它转成 PDF。\n\n## 步骤\n\n| 步骤 | 负责 | 状态 |\n|------|------|------|\n| 找出慢的页面 | Agent | 完成 |\n| 缓存算好的图表 | Agent | 审阅中 |\n\n目标是 50 页的文稿在 $t < 2\\,\\text{s}$ 内完成：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  草稿 --> 审阅 --> 发布\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'yours': ('你写的内容留在你的 Mac 上', '不需要账户，没有同步，也没有云端。'), 'pay-once': ('免费试用，买一次就好', '免费试用 14 天，之后 USD 4.99 买一次，没有订阅。'), 'pdf': ('输出 PDF', '图表、代码高亮、经过安排的分页。'), 'native': ('为 Mac 而做', '原生窗口、标签页、自动保存、快速查看。'), 'limits': ('MarsDawn 做不到的事', '购买前先知道。')}
    trait_nav_heading = 'MarsDawn 是什么样的 app'
    figure_list_label = '这张截图里'
    figures = {
        'index': {
            "alt": 'MarsDawn 的并排布局：左边是 Markdown 源代码，右边是排版后的页面。',
            "callouts": [],
        },
        'yours': {
            "alt": 'MarsDawn 以 Classic 主题显示文稿，预览占满整个窗口。',
            "callouts": ['你 Mac 上的一个文件，存在你选的地方。', '整条工具栏只有主题和布局，没有任何需要登录的地方。'],
        },
        'pay-once': {
            "alt": 'MarsDawn 使用 Vivid 主题，左边是 Markdown 源代码，右边是排版后的页面。',
            "callouts": ['编辑器的 Markdown 语法高亮，包含在内。', '所有主题和布局都包含在内。', 'Mermaid 图表，包含在内。', '代码高亮，包含在内。'],
        },
        'pdf': {
            "alt": '用 MarsDawn 输出的 PDF，在内置的 PDF 查看器中打开，旁边有页面缩略图。',
            "callouts": ['Mermaid 图表直接画进 PDF。', '代码保留语法高亮。'],
        },
        'native': {
            "alt": 'MarsDawn 的并排布局：左边是 Markdown 源代码，右边是排版后的页面。',
            "callouts": ['原生的 Mac 窗口。', 'Mac 原生的文本编辑器，附 Markdown 语法高亮。', '⌘1 源代码、⌘2 并排、⌘3 预览。', '页面会随着打字更新。'],
        },
        'limits': {
            "alt": 'MarsDawn 的深色模式，左边是 Markdown 源代码，右边是排版后的页面。',
            "callouts": ['一个窗口一份文稿，就在这台 Mac 上。', '你在这里写 Markdown。', '工具栏只有主题和布局，没有插件菜单。', '这一侧用来阅读，不能直接编辑。'],
        },
    }
    pages = {}
    pages['support'] = {
        "title": '支持 · MarsDawn',
        "description": 'MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。',
        "body": f"""
<section class="intro">
  <h1>支持</h1>
  <p>macOS Markdown 编辑器 MarsDawn 的使用说明。</p>
</section>

<section class="contact">
  <h2>写信给我们</h2>
  <a class="email" href="mailto:{k.EMAIL}?subject=MarsDawn%20support">{k.EMAIL}</a>
  <p>请附上你的 macOS 版本与 MarsDawn 版本（MarsDawn › 关于 MarsDawn）。如果画面看起来不对，附上截图或一份小的范例文稿会很有帮助。</p>
</section>

<section class="faq">
  <h2>常见问题</h2>

  <h3>MarsDawn 需要什么环境？</h3>
  <p>macOS 26 Tahoe 或更新版本的 Mac，Apple 芯片或 Intel 皆可。</p>

  <h3>怎么切换编辑器与预览？</h3>
  <p>按 <kbd>⌘1</kbd> 只看源代码、<kbd>⌘2</kbd> 左右并排、<kbd>⌘3</kbd> 只看预览。“显示”菜单和工具栏也有相同选项。</p>

  <h3>文稿里的图片没有显示。</h3>
  <ul>
    <li><strong>Mac 上的图片：</strong>先保存文稿，再按预览中的“授予文件夹访问权限…”，选择图片所在的文件夹。MarsDawn 会记住这个文件夹，你可以到 MarsDawn › 设置… › 文件夹访问查看。</li>
    <li><strong>网络上的图片：</strong>网络图片在你按下预览上方的“载入图像”之前不会加载。想要一律加载，可在设置中打开“自动载入网络图像”。</li>
  </ul>

  <h3>怎么加入图片？</h3>
  <p>把图片拖进编辑器，或直接粘贴。文稿需要先保存：MarsDawn 会把图片复制到文稿旁的 <code>assets</code> 文件夹，并帮你写好 Markdown 链接。</p>

  <h3>Mermaid 图表显示错误。</h3>
  <p>MarsDawn 会显示图表的源代码，下方附上 Mermaid 错误消息的第一行。请检查消息指出的那一行，例如箭头后面缺了目标，或括号没有闭合。</p>

  <h3>怎么产生 PDF？</h3>
  <p>选择“文件 › 导出为 PDF…”（<kbd>⌥⌘E</kbd>）。不论目前是哪种布局，PDF 都会使用预览主题的浅色版本并自动分页。“文件 › 打印…”会打印出相同的页面。</p>

  <h3>怎么搭配 Siri 或快捷指令使用？</h3>
  <p>打开“快捷指令”App 搜索 MarsDawn，就能找到“新建 Markdown 文稿”、“添加笔记到收件箱”与“打开最近使用的文稿”。要添加笔记之前，请先到 MarsDawn › 设置… › 笔记文件夹选择文件夹，笔记会加到该文件夹的 <code>Inbox.md</code>。</p>

  <h3>设置在哪里？</h3>
  <p>MarsDawn › 设置…（<kbd>⌘,</kbd>），包含外观、图片、笔记文件夹、文件夹访问与预览主题。</p>

  <h3>怎么申请退款？</h3>
  <p>购买由 Apple 处理，请到 <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> 申请退款。</p>
</section>
""",
    }
    pages['privacy'] = {
        "title": '隐私政策 · MarsDawn',
        "description": 'MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。',
        "body": f"""
<section class="intro">
  <h1>隐私政策</h1>
  <p>macOS 的 Markdown 编辑器 MarsDawn 如何处理你的信息。</p>
  <p class="updated">最后更新：{k.PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn 不收集任何关于你的数据。</strong>没有账户、没有分析、没有广告，也不追踪。你的文稿与设置都留在你的 Mac 上。</p></div>

<h2>留在你 Mac 上的东西</h2>
<ul>
  <li><strong>你的文稿。</strong>MarsDawn 只读写你打开、保存或选择的文件与文件夹，App 不会把它们上传到任何地方。</li>
  <li><strong>你的设置。</strong>外观、预览主题、窗口布局和图片偏好，都存在 App 自己的偏好设置里。</li>
  <li><strong>你授权的文件夹。</strong>当你让 MarsDawn 显示某个文件夹里的图片或网页文件，或选择笔记文件夹时，App 会保存 macOS 书签，以便之后再次打开。你在侧边栏打开的文件夹，MarsDawn 会保持可读写，直到你在设置中移除为止，而不只是在那个窗口开着的时候。你随时可以到 MarsDawn › 设置… 移除。</li>
</ul>

<h2>MarsDawn 什么时候会连上网络</h2>
<p>MarsDawn 可以完全离线使用，只有在<strong>你自己选择时</strong>，才会为引用网络内容的文稿连网：</p>
<ul>
  <li><strong>Markdown 文稿。</strong>网络图片默认不加载，只有在你按下预览中的“载入图像”，或在设置中打开“自动载入网络图像”后才会加载。Markdown 文稿引用的其他网络内容一律不加载。</li>
  <li><strong>HTML 文稿。</strong>HTML 文稿打开时是静态的：它的代码不会运行，也不会从网络加载任何东西。如果文稿含有可以运行的代码，你可以针对这份文稿选择“显示 › 运行这份文稿”。之后它自己的代码会一直运行，直到你停止它、文稿重新加载，或关闭窗口为止。这个选择不会被记住，也不是一项设置。运行期间，这份文稿可以通过网络发送数据，并读取它所在文件夹及其子文件夹中的图片、样式表、字体与媒体文件。从网络下载的代码一律不会运行。</li>
</ul>
<p>MarsDawn 只通过 https 加载网络内容。http 地址一律不会加载，任何设置都无法打开，MarsDawn 也不会自动改写成 https。在 Markdown 文稿中，预览会以占位图标代替。</p>
<p>加载网络内容时，你的 Mac 会直接向存放内容的服务器发出请求。和所有网络请求一样，这些服务器会看到你的 IP 地址与请求的内容。MarsDawn 的开发者不会收到任何这类信息。</p>
<p>在预览中点击的链接会用你的默认浏览器打开，适用该浏览器的隐私做法。音频与视频不会自动播放。</p>

<h2>Siri、快捷指令和 Spotlight</h2>
<p>MarsDawn 提供 Siri、快捷指令 App 和 Spotlight 可用的动作，例如添加文稿或加入笔记。使用时，你提供的文本会交给你 Mac 上的 MarsDawn，并只存到动作指定的位置（新文稿，或你所选笔记文件夹中的 <code>Inbox.md</code>）。对 Siri 说的话由 Apple 依 <a href="https://www.apple.com/legal/privacy/">Apple 隐私政策</a> 处理。</p>

<h2>输出 PDF 和打印</h2>
<p>输出 PDF 和打印都在你的 Mac 上完成。PDF 存在你选择的位置，打印则通过 macOS 送到你选的打印机。</p>

<h2>marsdawn 命令行工具</h2>
<p>另外发布、可自由选用的 <code>marsdawn</code> 命令行工具，同样完全在你的 Mac 上运行：只读取你指定的 Markdown 文件，并写出你要求的 PDF。只有在加上 <code>--allow-remote-images</code> 时才会加载网络图片。</p>

<h2>儿童</h2>
<p>MarsDawn 不向任何人收集数据，包括儿童。</p>

<h2>购买</h2>
<p>MarsDawn 将通过 Mac App Store 销售，付款会由 Apple 依其条款处理，开发者不会取得你的付款信息。</p>

<h2>政策变更</h2>
<p>如果 MarsDawn 未来处理数据的方式有所改变，本页会在该版本推出前更新，页面顶部的日期也会一并更改。</p>

<h2>联系我们</h2>
<p>隐私相关问题：<a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
""",
    }
    return {
        'ui': ui,
        'store_chip': store_chip,
        'schema_notes': schema_notes,
        'example_plan': example_plan,
        'trait_link': trait_link,
        'trait_nav_heading': trait_nav_heading,
        'figure_list_label': figure_list_label,
        'figures': figures,
        'pages': pages,
    }
