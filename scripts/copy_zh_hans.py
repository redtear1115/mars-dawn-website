"""Simplified Chinese (zh-Hans) copy for the MarsDawn site, translated from the zh-hant copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': '隐私政策', 'support': '支持', 'cli': '命令行工具', 'agents': '给 AI agent 的 marsdawn 参考', 'using_cli': '使用 CLI', 'markdown-to-pdf': 'Markdown 转 PDF', 'skill': '给 agent 的 skill', 'view-markdown-on-mac': '在 Mac 上看 Markdown', 'vs-macmd-viewer': 'MacMD Viewer 对比 MarsDawn', 'updated': f"最后更新：{k.UPDATED}", 'tagline': '读 agent 写的 Markdown。', 'footer_store': 'MarsDawn 即将在 Mac App Store 上架。', 'more': '其他页面', 'yours': '你写的内容留在你的 Mac 上', 'pay-once': '免费试用，买一次就好', 'pdf': '输出 PDF', 'native': '为 Mac 而做', 'limits': 'MarsDawn 做不到的事'}
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
    pages['index'] = {
        "title": 'MarsDawn：Mac 上的 Markdown 编辑器，实时预览',
        "description": '原生的 Mac Markdown 编辑器，有实时预览、Mermaid 图表和 PDF 输出，为读 AI agent 写的 Markdown 而做。即将在 Mac App Store 上架。',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">为 AI 工作流程而生</p>
  <h1>让 agent 写的 Markdown，被好好读过一遍。</h1>
  <p>AI agent 写 Markdown，你在 MarsDawn 里读，源代码和排版后的页面并排显示，再把修改意见交回去。</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">整个循环</h2>
<ol class="loop-steps">
  <li><strong>Agent 动笔。</strong>你的代码助手或写作 agent 先写出 Markdown：README、规格文档，或一份笔记。</li>
  <li><strong>你在 MarsDawn 里读。</strong>打开文件，看排版后的页面，Mermaid 图表和代码高亮都在，旁边就是源代码。</li>
  <li><strong>Agent 修改。</strong>提出修改意见，agent 改好之后，再打开来读一次。</li>
</ol>
<p>Agent 也能直接操作 MarsDawn：免费的 <a href="/zh-hans/cli/">marsdawn</a> 命令行工具能打开文件供你检阅，也能输出 PDF，并提供给脚本使用的 JSON 输出。细节请看<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。</p>
""",
    }
    pages['yours'] = {
        "title": '不用账户、不上云端的 Mac Markdown 编辑器 · MarsDawn',
        "description": 'MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。',
        "intro": f"""
<section class="intro">
  <h1>你写的内容，留在你的 Mac 上。</h1>
  <p>MarsDawn 不需要账户，没有同步，也没有云端。它打开文件、让你写，再存回你选的位置。</p>
</section>
""",
        "body": f"""
<h2>这代表什么</h2>
<ul>
  <li>不需要账户，不用注册，也不用登录。</li>
  <li>不会同步到云端，文稿存在哪里就留在哪里。</li>
  <li>不追踪任何行为。MarsDawn 不收集任何关于你的数据，App Store 隐私标签为“未收集数据”。</li>
  <li>网络图片在你选择加载之前一律不加载，打开文稿不会让任何服务器知道你读了它。选择加载时，也只走 https。</li>
  <li>本地图片在你授权文件夹访问后，就会显示在预览中。</li>
</ul>
<p>完整说明请看<a href="/zh-hans/privacy/">隐私政策</a>。</p>
""",
    }
    pages['pay-once'] = {
        "title": '免费试用，买一次就好 · MarsDawn',
        "description": 'MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。',
        "intro": f"""
<section class="intro">
  <h1>先全部试用，再买一次。</h1>
  <p>MarsDawn 可以免费下载。开始 14 天试用后，所有功能都能使用；试用结束后想继续使用，花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。</p>
</section>
""",
        "body": f"""
<h2>怎么运作</h2>
<ul>
  <li>在 Mac App Store 免费下载 MarsDawn。</li>
  <li>开始试用后，14 天内所有功能都能使用：所有主题与布局、PDF 输出与打印、快速查看，以及 Siri 和快捷指令操作。</li>
  <li>试用结束后想继续使用，花 USD 4.99 解锁一次就好。这是 App 内购买，不是订阅，不会自动续费，之后也不会再扣款。</li>
  <li>试用本身也不会扣款。试用结束时，除非你选择解锁，否则不会购买任何东西。</li>
  <li>不需要账户，MarsDawn 从不要求你创建账户。</li>
</ul>
<h2>如果没有解锁</h2>
<ul>
  <li>14 天后，在你解锁之前，无法在 MarsDawn 中阅读、编辑、输出或打印文稿。文稿仍会打开，但内容会被遮住。</li>
  <li>你的文件不会有任何改变。它们就是你 Mac 上的一般文件，在访达中用“快速查看”依然看得到。</li>
  <li>免费的 <a href="/zh-hans/cli/"><code>marsdawn</code> 命令行工具</a>不受试用影响，依然能把它们导出成 PDF。</li>
  <li>如果试用结束时有文稿正开在 MarsDawn 里，你输入的文本不会遗失，可以用“文件”▸“存储为…”保存。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": '在 Mac 把 Markdown 输出成 PDF，图表也在 · MarsDawn',
        "description": '在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。',
        "intro": f"""
<section class="intro">
  <h1>PDF 看起来就是你写的那一页。</h1>
  <p>输出成 PDF 或打印，使用主题的浅色配色。图表和代码高亮都会保留，分页位置也经过安排。</p>
</section>
""",
        "body": f"""
<h2>这代表什么</h2>
<ul>
  <li>Mermaid 图表直接画进 PDF。</li>
  <li>代码块保留语法高亮。</li>
  <li>分页时会尽量不让标题落在页面底部，也不切开代码、表格和图表。</li>
  <li>任何布局都能输出，只显示源代码时也可以。</li>
</ul>
<p>免费的 <a href="/zh-hans/cli/">marsdawn 命令行工具</a>使用同一套输出程序，所以脚本或 AI agent 也能得到一样的 PDF。</p>
""",
    }
    pages['native'] = {
        "title": '原生的 Mac Markdown app：标签页、快速查看 · MarsDawn',
        "description": '真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。',
        "intro": f"""
<section class="intro">
  <h1>用 Mac 原生的组件做的。</h1>
  <p>窗口、标签页、菜单和文本编辑器都是 Mac 原生的。排版后的页面由 Safari 使用的 WebKit 引擎绘制。</p>
</section>
""",
        "body": f"""
<h2>这代表什么</h2>
<ul>
  <li>源代码、并排、预览三种布局，一个快捷键切换（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>两侧同步滚动，正在编辑的段落一直在眼前。</li>
  <li>编辑器内置 Markdown 语法高亮，颜色与预览主题一致。</li>
  <li>原生窗口、标签页、自动保存和版本记录。</li>
  <li>快速查看：在访达选取 Markdown 文件按空格键就能预览，图表也会显示。</li>
  <li>Siri 和快捷指令：用模板添加文稿、在笔记收件箱加上一行，或重新打开最近的文稿。</li>
  <li>支持{k.APP_UI_LANGUAGES}。</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'MarsDawn 做不到的事 · MarsDawn',
        "description": '没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。',
        "intro": f"""
<section class="intro">
  <h1>MarsDawn 做不到的事。</h1>
  <p>有些功能是刻意不做的。如果你需要其中一项，现在知道总比买了之后才发现好。</p>
</section>
""",
        "body": f"""
<h2>刻意不做的</h2>
<ul>
  <li><strong>同步：</strong>MarsDawn 不会同步文稿，文稿存在哪里就留在哪里；要在另一台 Mac 上使用，请放在你原本就会同步的文件夹。</li>
  <li><strong>iPhone 和 iPad：</strong>没有这两个平台的版本，MarsDawn 只给 Mac。</li>
  <li><strong>插件：</strong>MarsDawn 没有插件或扩展功能。</li>
  <li><strong>分享：</strong>没有账户，也不能共同编辑，因为 MarsDawn 是给一个人在自己的 Mac 上用的。</li>
  <li><strong>编辑：</strong>你在左边写 Markdown，在右边阅读排版后的页面；页面本身不能直接编辑。</li>
  <li><strong>格式：</strong>MarsDawn 能输出 PDF 和打印，不能输出 Word 文件。</li>
  <li><strong>主题：</strong>内置 Dawn、Classic、Modern 和 Vivid，每种都有浅色与深色，无法安装其他主题。</li>
  <li><strong>其他文件：</strong>纯文本文件和 PDF 以只读方式打开。</li>
  <li><strong>试用结束后：</strong>如果 14 天试用结束后没有解锁，就无法在 MarsDawn 中阅读和编辑文稿：文稿会打开，但内容会被遮住。你的文件维持原样，“快速查看”依然看得到，免费的命令行工具也依然能导出它们。</li>
  <li><strong>系统：</strong>MarsDawn 需要 macOS 26 以上。</li>
</ul>
""",
    }
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
    pages['view-markdown-on-mac'] = {
        "title": '在 Mac 上怎么看 Markdown 文件 · MarsDawn',
        "description": 'md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。',
        "body": f"""
<section class="intro">
  <h1>在 Mac 上，怎么看 Markdown 文件。</h1>
  <p><code>.md</code> 文件是纯文本。标题、粗体、表格和图表，都是用记号写成的：<code>#</code> 代表标题，<code>**</code> 包住粗体，直线符号画出表格，<code>mermaid</code> 代码块则是一张图。用纯文本编辑器打开，看到的就是这些记号。想照作者的意思读到排好的页面，就需要有东西把它排版出来。</p>
</section>
<h2>现在就能用，而且免费：转成 PDF</h2>
<p>免费的 <code>marsdawn</code> 命令行工具，能把 Markdown 文件排版成 PDF，任何一台 Mac 都打得开。表格、数学公式、Mermaid 图表和代码高亮都会排好，而且不需要安装其他东西，连 MarsDawn app 都不用。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> 会在 Markdown 文件旁边写出 <code>notes.pdf</code>，<code>open</code> 会用你的 PDF 查看器打开它。这个工具需要 macOS 15 以上。完整步骤和一页实际导出的结果，请看<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF</a>。</p>
<h2>即将推出：在 MarsDawn 里读</h2>
<p>MarsDawn 是为 Mac 做的 Markdown 编辑器，即将在 Mac App Store 上架。打开 <code>.md</code> 文件，排好的页面就在源代码旁边：</p>
<ul>
  <li>预览会随着你打字实时更新，两边的窗格一起滚动。</li>
  <li>Mermaid 流程图和时序图直接画在预览里，代码块也会高亮。</li>
  <li>在访达里对 Markdown 文件按空格键，就有“快速查看”预览，图表也在。</li>
  <li>想改的时候，源代码就在旁边。MarsDawn 是编辑器，不只是查看器。</li>
</ul>
<p>如果这份文件是 AI agent 写的，这正是 MarsDawn 要支持的循环：agent 写，你读排好的页面，agent 再修改。请看<a href="/zh-hans/">首页</a>，想让 agent 帮你开文件，请看<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。</p>
<h2>接下来</h2>
<ul>
  <li>命令行工具的所有选项：<a href="/zh-hans/cli/">命令行工具</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hans/limits/">这份清单</a>。</li>
</ul>
""",
    }
    pages['markdown-to-pdf'] = {
        "title": 'Markdown 转 PDF 工具：在 Mac 用命令行转换 · MarsDawn',
        "description": '免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。',
        "body": f"""
<section class="intro">
  <h1>Markdown 转 PDF 工具：在 Mac 上用命令行转换。</h1>
  <p>免费的 <code>marsdawn</code> 工具只要一个命令，就能把 Markdown 文件转成 PDF。表格、数学公式、Mermaid 图表和代码高亮，都会照源文件的样子呈现，而且不需要安装其他东西，连 MarsDawn app 都不用。</p>
</section>
<h2>安装</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>在 Apple 芯片的 Mac 上，Homebrew 会直接安装预先构建好的版本，几秒就完成。在 Intel Mac 上则会从源代码构建，需要几分钟，也需要 Xcode 26 以上。这个工具需要 macOS 15 以上，<code>marsdawn --version</code> 会输出你装到的版本。</p>
<h2>存一份文稿</h2>
<p>把下面的内容贴进一个叫 <code>plan.md</code> 的文件：</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>导出</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>它会在源文件旁边写出 <code>plan.pdf</code>，并输出存放的位置：</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>这是那一页，截取自 <code>marsdawn</code> 0.5.0 的实际运行结果：</p>
<p><img class="pdf-page" src="/assets/cli/plan-zh-hans.png" alt="导出的 PDF：标题、步骤表格、行内与独立的数学公式、“草稿、审阅、发布”流程图，以及一行高亮的 Swift 代码。" width="989" height="930"></p>
<h2>选主题、纸张大小和文件名</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>：dawn、classic、modern 或 vivid，使用主题的浅色配色。没有指定时，<code>export</code> 会用 <code>$MARSDAWN_THEME</code>，再来才是 dawn。</li>
  <li><code>--paper</code>：a4 或 letter，默认是 a4。</li>
  <li><code>-o</code>：PDF 要写到哪里，而不是写在源文件旁边。</li>
  <li><code>--allow-remote-images</code>：转换时加载网络上的图片。没加这个选项就不会加载。</li>
</ul>
<h2>如果没有成功</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> 代表 Homebrew 正在从源代码构建 <code>marsdawn</code>，这在 Intel Mac 上会发生。从 App Store 安装 Xcode 26 以上，再重新安装一次。</li>
  <li><code>marsdawn: No such file: …</code> 路径没有指到文件。确认文件名，或在文件所在的文件夹里运行命令。</li>
  <li><code>… already exists. Pass --force to replace it.</code> 同名的 PDF 已经存在。加上 <code>--force</code> 覆盖它，或用 <code>-o</code> 写到别的地方。</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> 主题或纸张大小不是它认得的。主题有 dawn、classic、modern 和 vivid，纸张是 a4 或 letter。</li>
</ul>
<h2>接下来</h2>
<ul>
  <li>所有选项和它输出的 JSON：<a href="/zh-hans/cli/">命令行工具</a>。</li>
  <li>让写程序的 agent 帮你做这件事：<a href="/zh-hans/cli/skill/">marsdawn 的 agent skill</a>。</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer 对比 MarsDawn：查看器与编辑器 · MarsDawn',
        "description": 'MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer 对比 MarsDawn。</h1>
  <p>两者都是给 Mac 用的 app，都能把 Markdown 排版出来读。MacMD Viewer 打开 <code>.md</code> 文件，显示排好版的页面，但不能编辑它。MarsDawn 则是在同样的预览旁边放了编辑器，让你在同一个窗口里写和读。以下逐项比较两者的差异。</p>
</section>
<h2>如果你只需要读，不需要编辑</h2>
<p>如果你的工作就是读别人写好的 Markdown，完全不用碰源代码，MacMD Viewer 是合理的选择：它就是为这件事做的，现在就能买，也能在比较旧的 macOS 上跑。当阅读不是全部的工作时，MarsDawn 才值得，因为 agent 写的 Markdown 通常还要再改一轮。</p>
<h2>各自能做什么</h2>
<ul>
  <li><strong>编辑：</strong>MacMD Viewer 设计上就是只读。MarsDawn 边编辑源代码边在旁边排版，打字的同时就看得到改动。</li>
  <li><strong>预览主题：</strong>MacMD Viewer 内置 12 种文档主题。MarsDawn 有四种：Dawn、Classic、Modern 和 Vivid，各有浅色与深色。</li>
  <li><strong>图表与数学公式：</strong>两者都能画出 Mermaid 图表、也都有代码高亮。MarsDawn 还能排版 KaTeX 数学公式；MacMD Viewer 自己的介绍页没有提到数学公式排版。</li>
  <li><strong>访达集成：</strong>两者都有访达的快速查看扩展功能，对 <code>.md</code> 文件按空格键就能看到排好版的页面。</li>
  <li><strong>PDF 与打印：</strong>两者都能把排好版的页面输出或打印成 PDF。</li>
  <li><strong>系统需求：</strong>MacMD Viewer 需要 macOS 14（Sonoma）以上。MarsDawn 需要 macOS 26（Tahoe）以上。</li>
  <li><strong>语言：</strong>MarsDawn 的界面有{k.APP_UI_LANGUAGES}。MacMD Viewer 自己的资料没有写出界面语言，这页就不比较这一项。</li>
</ul>
<h2>价格与购买方式</h2>
<ul>
  <li><strong>从哪里买：</strong>MacMD Viewer 从自己的网站直接下载，也上架 Homebrew 和 Setapp，但不在 Mac App Store 上；MarsDawn 只在 Mac App Store 上架。</li>
  <li><strong>价格：</strong>MacMD Viewer 一台 Mac 一次 USD 19.99（三台的组合包和批量授权更贵）。MarsDawn 免费下载，之后以 USD 4.99 一次解锁。</li>
  <li><strong>先试用：</strong>MacMD Viewer 没有免费试用，直接购买改用 14 天内可退款的保证。MarsDawn 在你付费之前，先给你 14 天的试用。</li>
  <li><strong>退款与更新：</strong>MacMD Viewer 的退款和更新都在它自己的网站上处理。MarsDawn 通过 Apple 购买，退款和更新都走 Apple 的标准流程。</li>
  <li><strong>账户：</strong>两者都不需要账户就能使用。</li>
</ul>
<h2>现在就能免费试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架，现在还没开卖。在那之前，免费的 <code>marsdawn</code> 命令行工具今天就能把任何 Markdown 文件转成 PDF，Mermaid 图表和代码高亮都在，而且不需要安装其他东西：</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>接下来</h2>
<ul>
  <li>完整步骤：<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hans/limits/">这份清单</a>。</li>
  <li>命令行工具的所有选项：<a href="/zh-hans/cli/">命令行工具</a>。</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn：免费的 Markdown 转 PDF 命令行工具 · MarsDawn',
        "description": '免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。',
        "body": f"""
<section class="intro">
  <h1>命令行工具</h1>
  <p>免费的 <code>marsdawn</code> 命令行工具：从终端或 LLM agent 把 Markdown 导出成 PDF；装了 MarsDawn app 的话，也能用它打开文件。</p>
</section>

<div class="summary"><p><strong>marsdawn 免费、另外发布，不通过 Mac App Store。</strong>用 Homebrew 安装，在 Apple 芯片的 Mac 上装好就能直接使用。<code>export</code> 可以单独使用；<code>open</code> 需要 MarsDawn app。</p></div>

<p>要从 AI agent 或脚本调用 marsdawn？请看<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>，里面有 JSON 输出、Schema 和所有退出代码。</p>

<h2>安装</h2>
<p>使用 <a href="https://brew.sh">Homebrew</a>：</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>在用写程序的 agent 吗？<a href="/zh-hans/cli/skill/">加上 marsdawn skill</a>：一个文件，教它把自己写的文稿在 MarsDawn 里打开给你检阅，也能导出 PDF。</p>
<p>在 Apple 芯片的 Mac 上，Homebrew 会直接安装预先构建好的版本，几秒就完成，不需要另外安装任何东西。在 Intel Mac 上则会从源代码构建，需要几分钟，也需要 Xcode 26 以上（Swift 6.2）。这个工具需要 macOS 15 以上。</p>
<p>也可以从<a href="{k.KIT_URL}">源代码</a>用 Swift Package Manager 构建：</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>用 <code>marsdawn --version</code> 查看安装的版本。</p>

<h2>命令</h2>

<h3>marsdawn open</h3>
<p>在 MarsDawn app 中打开一个或多个 Markdown 文件，方便审阅。需要先安装这个 app：没有安装时，<code>marsdawn open</code> 会以代码 3 结束，并说明没有安装 MarsDawn。<code>export</code> 不需要这个 app。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>：请 MarsDawn 定位到那一行。后面再接列号，例如 <code>notes.md:120:8</code>，会被忽略。如果有文件的完整名称就是这个参数，则视为那个文件。</li>
  <li><code>--line &lt;n&gt;</code>：同样的功能，只用于单一文件，也可以用在文件名本身以冒号加数字结尾的情况。只能搭配一个文件。</li>
  <li>行号范围是 1 到 999999999。</li>
  <li>MarsDawn 1.0 会打开文件，但还不会跳到指定的行。</li>
  <li><code>--json</code>：输出 JSON 结果，而不是文本。</li>
</ul>
<p>行号功能从 marsdawn 0.3.0 开始提供。</p>

<h3>marsdawn export</h3>
<p>把 Markdown 文件输出成分页的 PDF，使用和 MarsDawn 输出 PDF 相同的组件。不需要安装 MarsDawn app。相对路径的图片，会以输入文件所在的文件夹为准。</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF 的输出位置，默认是把输入文件的扩展名换成 <code>.pdf</code>。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：预览主题的浅色版本，默认读取 <code>$MARSDAWN_THEME</code>，否则用 <code>dawn</code>。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：纸张大小，默认 <code>a4</code>。</li>
  <li><code>--allow-remote-images</code>：输出时加载网络图片，默认关闭。</li>
  <li><code>--force</code>：如果输出文件已存在就直接覆盖。</li>
  <li><code>--json</code>：输出 JSON 结果，而不是文本。</li>
</ul>

<h2>$MARSDAWN_THEME 环境变量</h2>
<p>没有传入 <code>--theme</code> 时，<code>export</code> 会读取 <code>$MARSDAWN_THEME</code> 环境变量，值必须是 <code>dawn</code>、<code>classic</code>、<code>modern</code> 或 <code>vivid</code> 其中之一，其他值都会改用 <code>dawn</code>。这个工具不会读取 App 本身的主题设置，因为读取其他 App 的容器可能触发 macOS 隐私提示。</p>

<h2>覆盖文件的规则</h2>
<p><code>export</code> 默认不会覆盖已存在的输出文件，除非加上 <code>--force</code>。</p>

<h2>退出代码</h2>
<ul>
  <li><code>0</code>：成功。</li>
  <li><code>2</code>：找不到输入文件。</li>
  <li><code>3</code>：尚未安装 MarsDawn（只有 <code>open</code> 会用到）。</li>
  <li><code>4</code>：输出文件已存在（可加上 <code>--force</code>）。</li>
  <li><code>5</code>：输出失败。</li>
  <li><code>64</code>：使用方式错误，包括行号超出范围，或 <code>--line</code> 搭配了多个文件。</li>
</ul>

<h2>--json 输出</h2>
<p>成功时，<code>marsdawn open --json</code> 会输出 <code>ok</code>、<code>opened</code>（每个文件的 <code>path</code>，有指定行号时另含 <code>line</code>）与 <code>app</code>（App 路径）；<code>marsdawn export --json</code> 会输出 <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code> 与 <code>diagramErrors</code>。失败时两者都会输出 <code>ok</code>、<code>error</code> 与 <code>message</code>。</p>
""",
    }
    pages['cli/agents'] = {
        "title": '给 AI agent 的 marsdawn 参考：用脚本转 PDF · MarsDawn',
        "description": '给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。',
        "body": f"""
<section class="intro">
  <h1>给 AI agent 的 marsdawn 参考</h1>
  <p>给调用 <code>marsdawn</code> 命令行工具的 AI agent 与脚本参考。本页每个范例都用目前源代码构建的工具实际运行过。</p>
</section>

<div class="summary"><p><strong>要把 Markdown 文件转成 PDF，运行 <code>marsdawn export notes.md --json</code>，再从 stdout 读取一个 JSON 对象。</strong>Mermaid 图表与代码高亮的呈现方式和 MarsDawn app 相同。<code>export</code> 不需要 app，<code>open</code> 需要。</p></div>

<h2>能做什么</h2>
<ul>
  <li><code>export</code>：用和 MarsDawn app 相同的导出程序，把一个 Markdown 文件输出成分页的 PDF，不会打开任何窗口。</li>
  <li><code>open</code>：在 MarsDawn app 中打开一或多个 Markdown 文件，让人检阅，也可以指定每个文件要定位的行。</li>
</ul>

<h2>不做什么</h2>
<ul>
  <li>不从 stdin 读取 Markdown，请传入文件路径。</li>
  <li>不把 PDF 写到 stdout。PDF 一律写成文件，stdout 只输出结果。</li>
  <li>文件已存在时不会覆盖，除非加上 <code>--force</code>。</li>
  <li>不加载网络图片，除非加上 <code>--allow-remote-images</code>，而且只走 https。</li>
  <li>没有安装 MarsDawn 时，<code>open</code> 无法使用，会以代码 3 结束。<code>export</code> 不需要 app。</li>
  <li>MarsDawn 1.0 还不会跳到 <code>open</code> 指定的行，会从文件开头显示。</li>
  <li>只能在 macOS 上运行。</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>在 <code>notes.md</code> 旁写出 <code>notes.pdf</code>。选项：</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF 的写入位置。默认为输入文件路径，扩展名换成 <code>.pdf</code>。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：使用主题的浅色调色板。默认为 <code>$MARSDAWN_THEME</code>，其次是 <code>dawn</code>。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：纸张大小。默认为 <code>a4</code>。</li>
  <li><code>--allow-remote-images</code>：渲染时加载网络上的 https 图片。</li>
  <li><code>--force</code>：输出文件已存在时覆盖。</li>
  <li><code>--json</code>：在 stdout 输出一个 JSON 对象，而不是文本。</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>成功，退出代码 0：</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>：写出的 PDF 的绝对路径。</li>
  <li><code>pages</code>：页数。</li>
  <li><code>theme</code> 与 <code>paper</code>：实际使用的值。</li>
  <li><code>diagramErrors</code>：每个渲染失败的 Mermaid 图表各一则消息。PDF 仍会写出。</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> 指定要定位的行。后面再接列号，例如 <code>notes.md:120:8</code>，会被忽略。如果参数本身就是一个存在的文件名，就一律当成那个文件，所以名为 <code>weird:12</code> 的文件会照原名打开。</li>
  <li><code>--line &lt;n&gt;</code> 为单一文件指定行号，包括文件名本身以冒号加数字结尾的情况。只能搭配一个文件。</li>
  <li>行号范围是 1 到 999999999，超出范围是用法错误。</li>
  <li>行号从 marsdawn 0.3.0 开始提供。MarsDawn 1.0 会打开文件，但还不会跳到指定的行。</li>
</ul>
<p>成功，退出代码 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：每个文件一个对象，顺序与传入时相同。<code>path</code> 是文件的绝对路径；只有指定了行号时才有 <code>line</code>。</li>
  <li><code>app</code>：打开它们的 MarsDawn app 路径。</li>
</ul>
<p>marsdawn 0.2.x 的 <code>opened</code> 是路径字符串的清单。如果需要同时处理两种格式，请先查看 <code>marsdawn --version</code>。</p>

<h2>失败</h2>
<p>加上 <code>--json</code> 时，失败会在 stdout 输出一个 JSON 对象，并以对应的代码结束：</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>，<code>input_not_found</code>：输入文件不存在、是文件夹，或不是 UTF-8 文本。</li>
  <li><code>3</code>，<code>app_not_installed</code>：没有安装 MarsDawn。只有 <code>open</code> 会返回这个代码。</li>
  <li><code>4</code>，<code>output_exists</code>：输出文件已存在，请加上 <code>--force</code>。</li>
  <li><code>5</code>，<code>export_failed</code>：导出本身失败。</li>
  <li><code>64</code>：用法错误，例如未知的选项、无效的值、行号超出范围，或 <code>--line</code> 搭配了多个文件。这种错误一律以文本输出到 stderr，即使加了 <code>--json</code> 也一样。</li>
</ul>

<h2>JSON Schema</h2>
<p>每种 <code>--json</code> 结果的 JSON Schema（draft 2020-12）：</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>环境变量</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>：没有传入 <code>--theme</code> 时，<code>export</code> 使用的主题。未知的值会直接改用 <code>dawn</code>，不会报错。</li>
</ul>

<h2>系统需求</h2>
<ul>
  <li>这个工具需要 macOS 15 以上。在 Apple 芯片的 Mac 上，Homebrew 会安装预先构建好的版本，不需要其他东西。自己构建时（在 Intel Mac 上，或从源代码构建），需要 Swift 6.2 以上，也就是 Xcode 26 以上。</li>
  <li>MarsDawn app 需要 macOS 26 以上。</li>
</ul>

<h2>安装</h2>
<p>使用 Homebrew。在 Apple 芯片的 Mac 上，会直接安装预先构建好的版本，几秒就完成，不需要 Xcode。在 Intel Mac 上则会从源代码编译 marsdawn，需要几分钟，也需要 Xcode 26 以上。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>也可以从<a href="{k.KIT_URL}">源代码</a>构建。第一次构建会下载依赖项并编译，同样需要几分钟。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> 会输出版本号，例如 <code>0.3.0</code>，并以代码 0 结束。</p>
""",
    }
    pages['cli/skill'] = {
        "title": '让写程序的 agent 把 Markdown 转 PDF 的 skill · MarsDawn',
        "description": '一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你检阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。',
        "body": f"""
<section class="intro">
  <h1>让 agent 把写好的文稿拿给你看，也帮你做出 PDF。</h1>
  <p>这个 skill 是一个 Markdown 文件。它教写程序的 agent 把自己写的文稿在 MarsDawn 里打开给你检阅，也教它安装 <code>marsdawn</code>、确认它能用、把文稿导出成 PDF 并读懂结果。</p>
</section>
<h2>在 Claude Code 中安装</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>需要做出 PDF，或写好、改好一份要给你读的 Markdown 文稿时，Claude Code 会自动加载它，你也可以用 <code>/marsdawn</code> 自己运行。它只是<a href="/cli/skill/SKILL.md">一个简短的文件</a>，安装前先读一遍。</p>
<p>其他 agent 也能用同一个文件。它是纯 Markdown，只有说明和命令，让你的 agent 读这个网址，或直接贴给它就好。这个文件是英文的。</p>
<h2>它教什么</h2>
<ul>
  <li>如果没有 <code>marsdawn</code>，就用 Homebrew 安装，再用 <code>marsdawn --version</code> 确认版本，而不是假设某个版本。</li>
  <li>用 <code>marsdawn export … --json</code> 导出，并读懂结果：PDF 存到哪里、有几页，以及有没有 Mermaid 图表没画出来。</li>
  <li>依退出代码分辨失败的原因：找不到文件、PDF 已经存在、导出失败、选项错误。</li>
  <li>用 <code>marsdawn open file.md:行号</code> 打开自己写的文稿，停在第一处修改，而且只打开一次：之后的修改会自己出现在已打开的窗口里。</li>
  <li>如果没有安装 MarsDawn app，就告诉你一次然后继续，不会一直重试。绝不用 <code>open</code> 来做 PDF。</li>
  <li>使用 <code>--folder</code>（marsdawn 0.5.1 以上）时，把文件夹报告为“已请求显示”，而不是“已显示”：由 app 决定，也不会有结果返回。</li>
</ul>
<h2>它不会做的事</h2>
<ul>
  <li>它不会自己取得运行任何东西的权限。你的 agent 在安装或运行 <code>marsdawn</code> 之前，仍然会先问你，就像运行其他命令一样。</li>
  <li>它不会把你的文稿传到任何地方。<code>marsdawn</code> 在你的 Mac 上产生 PDF，除非你加上 <code>--allow-remote-images</code>，否则不会加载网络上的图片。</li>
</ul>
<p>完整的规格，每个字段和每个代码，都在<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>里。</p>
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
