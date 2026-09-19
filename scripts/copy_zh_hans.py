"""Simplified Chinese (zh-Hans) copy for the MarsDawn site, translated from the zh-hant copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': '隐私政策', 'support': '支持', 'cli': '命令行工具', 'agents': '给 AI agent 的 marsdawn 参考', 'using_cli': '使用 CLI', 'markdown-to-pdf': 'Markdown 转 PDF', 'skill': '给 agent 的 skill', 'view-markdown-on-mac': '在 Mac 上看 Markdown', 'vs-macmd-viewer': 'MacMD Viewer 对比 MarsDawn', 'updated': f"最后更新：{k.UPDATED}", 'tagline': '读 agent 写的 Markdown。', 'slogan': 'Markdown 的新黎明。', 'footer_store': f'MarsDawn 已在 <a href="{k.LISTING_URL}">Mac App Store</a> 上架。', 'footer_nav': '网站', 'more': '其他页面', 'yours': '你写的内容留在你的 Mac 上', 'pay-once': '免费试用，买一次就好', 'pdf': '输出 PDF', 'native': '为 Mac 而做', 'limits': 'MarsDawn 做不到的事', 'mcp': 'MCP 服务器', 'token-efficient-review': '节省 token 的审阅方式', 'vs-markdown-preview-tools': '在别处看 Markdown，对比 MarsDawn', 'themes': '预览主题与 PDF 导出', 'sharing-exported-pdfs': '分享导出的 PDF', 'reviewing-ai-output': '为什么 AI 写的东西还是需要人读过', 'changelog': '更新记录', 'consent_text': '本网站使用分析用 cookie，用来了解访客如何使用网站。除非你点击“接受”，否则这些 cookie 都不会启用。', 'consent_accept': '接受', 'consent_decline': '拒绝', 'consent_aria': 'Cookie 同意设置', 'cookie_settings': 'Cookie 设置'}
    store_chip = '已在 Mac App Store 上架'
    schema_notes = {'export': 'export 成功', 'open': 'open 成功，marsdawn 0.5.1 以后，包括在侧边栏显示的文件夹', 'open_v2': 'open 成功，marsdawn 0.3.0 到 0.5.0', 'error': '两个命令的失败结果', 'open_v1': 'open 成功，marsdawn 0.2.x，当时 <code>opened</code> 是路径清单'}
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
            "alt": 'MarsDawn 以典雅主题显示文稿，预览占满整个窗口。',
            "callouts": ['你 Mac 上的一个文件，存在你选的地方。', '整条工具栏只有主题和布局，没有任何需要登录的地方。'],
        },
        'pay-once': {
            "alt": 'MarsDawn 使用活泼主题，左边是 Markdown 源代码，右边是排版后的页面。',
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

<div class="summary"><p><strong>MarsDawn app 不收集任何关于你的数据。</strong>没有账户、没有广告，也不追踪。你的文稿与设置都留在你的 Mac 上。</p></div>

<h2>这个网站</h2>
<p>App 和这个网站是两件事。App 不收集数据。会记下访问的，只有 marsdawn.southern-light.dev。</p>
<p>这个网站使用通过<strong>Google Tag Manager</strong>载入的<strong>Google Analytics 4</strong>。每位访客一开始的分析状态都是拒绝：Google 的同意模式只会发送一个没有 cookie、不含任何持续性标识符的连接，直到你在横幅中选择“接受”为止。选择“拒绝”，或是不做选择，都会维持这个状态；如果先前选过“接受”后又改选“拒绝”，分析会立即关闭，下面提到的 cookie 也会被移除。你可以随时用每一页页脚的“Cookie 设置”链接改变选择；这个选择只存在你浏览器的本地存储里，不是我们设下的 cookie。</p>
<p>一旦你点击接受，Google Analytics 就会设置自己的 cookie（<code>_ga</code> 与 <code>_ga_&lt;衡量 ID&gt;</code>），并记录：</p>
<ul>
  <li><strong>页面浏览与来源网址。</strong>被浏览的页面，以及浏览器有发送来源网址时的那个网址。</li>
  <li><strong>大致位置、设备与浏览器。</strong>由你的 IP 地址推算出的粗略位置（最多到城市级别）、设备类型、操作系统与浏览器，都不足以用来识别你是谁。</li>
  <li><strong>经由本站离开的点击与滚动。</strong>Google Analytics 的增强型衡量会记录离开本站的点击（例如前往 Mac App Store 的链接），以及你在页面上滚动的程度。</li>
  <li><strong>IP 地址。</strong>Google Analytics 4 不会记录或保存 IP 地址。</li>
  <li><strong>不会记录的。</strong>没有账户，因为这个网站不需要账户。没有你的文稿，也没有你打的字。没有跨站广告，也不会建立你的个人档案。App 向 <code>/themes/</code> 索取主题文件的请求会被跳过，不会送出。</li>
  <li><strong>保留期限。</strong>Google 会保留这些数据 14 个月，之后删除。</li>
  <li><strong>数据处理地点。</strong>Google Tag Manager 与 Google Analytics 由 Google 运营；你的数据可能会在美国及 Google 运营所在的其他国家处理。</li>
  <li><strong>主机。</strong>网站放在 Cloudflare 上。和任何主机一样，它在响应请求时会看到你的 IP 地址。那是主机自己的日志，不是上面的分析。</li>
</ul>

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
<p>MarsDawn app 不向任何人收集数据，包括儿童。网站上记下的访问不是账户，也不用来辨认任何人。</p>

<h2>购买</h2>
<p>MarsDawn 通过 Mac App Store 销售，付款由 Apple 依其条款处理，开发者不会取得你的付款信息。</p>

<h2>政策变更</h2>
<p>如果 MarsDawn 未来处理数据的方式有所改变，本页会在该版本推出前更新，页面顶部的日期也会一并更改。</p>

<h2>联系我们</h2>
<p>隐私相关问题：<a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
""",
    }
    pages['index'] = {
        "title": 'MarsDawn：Mac 上的 Markdown 编辑器，实时预览',
        "description": '给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。已在 Mac App Store 上架。',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">给建造者的前线工具</p>
  <h1><span>拿稳地图。</span><span>读过黎明。</span></h1>
  <p>给要掌舵 agentic 开发的人用的 Markdown。</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">读 agent 写的 Markdown。</h2>
<ol class="loop-steps">
  <li><strong>Agent 动笔。</strong>你的代码助手或写作 agent 先写出 Markdown：README、规格文档，或一份笔记。</li>
  <li><strong>你在 MarsDawn 里读。</strong>打开文件，看排版后的页面，Mermaid 图表和代码高亮都在，旁边就是源代码。</li>
  <li><strong>Agent 修改。</strong>提出修改意见，agent 改好之后，再打开来读一次。</li>
</ol>
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
<p>在用写程序的 agent 吗？<a href="/zh-hans/cli/skill/">加上 marsdawn skill</a>：一个文件，教它把自己写的文稿在 MarsDawn 里打开给你审阅，也能导出 PDF。</p>
<p>在 Apple 芯片的 Mac 上，Homebrew 会直接安装预先构建好的版本，几秒就完成，不需要另外安装任何东西。在 Intel Mac 上则会从源代码构建，需要几分钟，也需要 Xcode 26 以上（Swift 6.2）。这个工具需要 macOS 15 以上。</p>
<p>也可以从<a href="{k.KIT_URL}">源代码</a>用 Swift Package Manager 构建：</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>用 <code>marsdawn --version</code> 查看安装的版本。</p>

<h2>命令</h2>

<h3>marsdawn open</h3>
<p>在 MarsDawn app 中打开一个或多个 Markdown 文件，方便审阅。需要先安装这个 app：没有安装时，<code>marsdawn open</code> 会以代码 3 结束，并说明没有安装 MarsDawn。<code>export</code> 不需要这个 app。App 已在 <a href="{k.LISTING_URL}">Mac App Store</a> 上架。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code>：请 MarsDawn 定位到那一行。后面再接列号，例如 <code>notes.md:120:8</code>，会被忽略。如果有文件的完整名称就是这个参数，则视为那个文件。</li>
  <li><code>--line &lt;n&gt;</code>：同样的功能，只用于单一文件，也可以用在文件名本身以冒号加数字结尾的情况。只能搭配一个文件。</li>
  <li>行号范围是 1 到 999999999。</li>
  <li>文件夹参数会在窗口的侧边栏打开，而不是当成文稿：<code>marsdawn open .</code> 会显示当前的文件夹。<code>--folder &lt;path&gt;</code> 可以在打开文件的同时做到一样的事。一个窗口的侧边栏只显示一个文件夹，所以指定两个是使用方式错误。</li>
  <li><code>--background</code>：打开时不把 MarsDawn 带到最前面。</li>
  <li><code>--json</code>：输出 JSON 结果，而不是文本。</li>
</ul>
<p>行号功能从 marsdawn 0.3.0 开始提供，文件夹与 <code>--background</code> 从 0.5.1 开始。</p>

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
<!--exit-table-->
<ul>
  <li><code>0</code>：成功。</li>
  <li><code>2</code>：找不到输入文件。</li>
  <li><code>3</code>：尚未安装 MarsDawn（只有 <code>open</code> 会用到）。</li>
  <li><code>4</code>：输出文件已存在（可加上 <code>--force</code>）。</li>
  <li><code>5</code>：输出失败。</li>
  <li><code>64</code>：使用方式错误，包括行号超出范围、<code>--line</code> 搭配了多个文件或文件夹，或指定了多个文件夹。</li>
</ul>

<h2>--json 输出</h2>
<p>成功时，<code>marsdawn open --json</code> 会输出 <code>ok</code>、<code>opened</code>（每个文件的 <code>path</code>，有指定行号时另含 <code>line</code>）、<code>app</code>（App 路径），有文件夹时另含 <code>folder</code>；<code>marsdawn export --json</code> 会输出 <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code> 与 <code>diagramErrors</code>。失败时两者都会输出 <code>ok</code>、<code>error</code> 与 <code>message</code>。</p>
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
  <li><code>open</code>：在 MarsDawn app 中打开一或多个 Markdown 文件，让人审阅，也可以指定每个文件要定位的行，或在窗口的侧边栏显示一个文件夹。</li>
</ul>

<h2>不做什么</h2>
<ul>
  <li>不从 stdin 读取 Markdown，请传入文件路径。</li>
  <li>不把 PDF 写到 stdout。PDF 一律写成文件，stdout 只输出结果。</li>
  <li>文件已存在时不会覆盖，除非加上 <code>--force</code>。</li>
  <li>不加载网络图片，除非加上 <code>--allow-remote-images</code>，而且只走 https。</li>
  <li>没有安装 MarsDawn 时，<code>open</code> 无法使用，会以代码 3 结束。<code>export</code> 不需要 app。App 已在 <a href="{k.LISTING_URL}">Mac App Store</a> 上架。</li>
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
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> 指定要定位的行。后面再接列号，例如 <code>notes.md:120:8</code>，会被忽略。如果参数本身就是一个存在的文件名，就一律当成那个文件，所以名为 <code>weird:12</code> 的文件会照原名打开。</li>
  <li><code>--line &lt;n&gt;</code> 为单一文件指定行号，包括文件名本身以冒号加数字结尾的情况。只能搭配一个文件。</li>
  <li>行号范围是 1 到 999999999，超出范围是用法错误。</li>
  <li>行号从 marsdawn 0.3.0 开始提供。</li>
  <li>文件夹参数会在窗口的侧边栏打开，而不是当成文稿，所以 <code>marsdawn open .</code> 会显示当前的文件夹；<code>--folder &lt;path&gt;</code> 可以在打开文件的同时做到一样的事。一个窗口的侧边栏只显示一个文件夹：指定两个是用法错误，同一个文件夹指定两次则算一个。文件夹没有行号，所以 <code>--line</code> 搭配文件夹是用法错误。没有 <code>-a</code>：传入它是用法错误，错误消息会指向 <code>--folder</code>。</li>
  <li><code>--background</code> 打开时不把 MarsDawn 带到最前面，适合在用户做别的事时打开文件的 agent。两种情况的 JSON 都一样。</li>
  <li>文件夹与 <code>--background</code> 从 marsdawn 0.5.1 开始提供。</li>
</ul>
<p>成功，退出代码 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：每个文件一个对象，顺序与传入时相同。<code>path</code> 是文件的绝对路径；只有指定了行号时才有 <code>line</code>。</li>
  <li><code>app</code>：打开它们的 MarsDawn app 路径。</li>
</ul>
<p>有文件夹时（marsdawn 0.5.1 以后），退出代码 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code>：只有指定了文件夹时才有。<code>path</code> 是它的绝对路径。<code>requested</code> 一律是 <code>true</code>：marsdawn 已请 MarsDawn 显示这个文件夹，但无法得知侧边栏是否真的显示了，因为 app 可能会先向用户请求访问权限。请报告为“已请求”，而不是“已完成”。</li>
  <li>只指定文件夹时，<code>opened</code> 是空的。</li>
</ul>
<p>marsdawn 0.2.x 的 <code>opened</code> 是路径字符串的清单。如果需要同时处理两种格式，请先查看 <code>marsdawn --version</code>。</p>

<h2>失败</h2>
<p>加上 <code>--json</code> 时，失败会在 stdout 输出一个 JSON 对象，并以对应的代码结束：</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>，<code>input_not_found</code>：输入文件不存在、是文件夹，或不是 UTF-8 文本；或 <code>--folder</code> 的路径不存在、不是文件夹。</li>
  <li><code>3</code>，<code>app_not_installed</code>：没有安装 MarsDawn。只有 <code>open</code> 会返回这个代码。</li>
  <li><code>4</code>，<code>output_exists</code>：输出文件已存在，请加上 <code>--force</code>。</li>
  <li><code>5</code>，<code>export_failed</code>：导出本身失败。</li>
  <li><code>64</code>：用法错误，例如未知的选项、无效的值、行号超出范围、<code>--line</code> 搭配了多个文件或文件夹、指定了多个文件夹，或使用了 <code>-a</code>。这种错误一律以文本输出到 stderr，即使加了 <code>--json</code> 也一样。</li>
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
    pages['cli/mcp'] = {
        "title": "调用 marsdawn 的三种方式：CLI、skill 文件、MCP 服务器 · MarsDawn",
        "description": "marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。",
        "body": """
<section class="intro">
  <h1>调用 marsdawn 的三种方式。</h1>
  <p>MarsDawn 没有自己的 AI 模型：它是为了审阅 Markdown 而做的，不是用来写的，所以是哪个 agent 或模型写出这份 Markdown 并不重要。agent 或脚本调用 <code>marsdawn</code> 有三种方式，最后都会运行同一个 <code>export</code>。</p>
</section>

<div class="summary"><p><strong>挑你的工具支持的那一种：免费的 <code>marsdawn</code> CLI、纯 Markdown 的 skill 文件，或是 <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> 这个 MCP 服务器。</strong>三者都调用同一个 <code>marsdawn export</code>，返回一样的 JSON 结果。</p></div>

<h2>该用哪一个</h2>
<!--compare:mcp-choice-->

<h2>CLI</h2>
<p><code>marsdawn export notes.md --json</code> 可以被任何能运行 shell 命令的 agent 或脚本调用，因为是命令行工具，天生就跟模型无关。它返回的每个字段都写在<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>里，那一页是 JSON schema 的权威来源，下面另外两种方式都会连回去。</p>

<h2>Skill 文件</h2>
<p>如果你的 agent 读的是纯 Markdown 指令，而不是直接运行 shell&#8212;&#8212;目前是 Claude Code&#8212;&#8212;<a href="/zh-hans/cli/skill/">marsdawn skill</a> 就是一个文件，教它安装 marsdawn、运行 <code>export</code>、读懂结果。因为它就是纯 Markdown，其他会读指令文件的 agent 也能用同一个文件。</p>

<h2>MCP 服务器</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> 是另一个独立、公开、Apache-2.0 授权的 repository。它是一个有两个工具的 MCP 服务器，<code>export_markdown_to_pdf</code> 和 <code>open_in_marsdawn</code>，分别包住 <code>marsdawn export --json</code> 和 <code>marsdawn open --json</code>：把 MCP 客户端指向它，工具调用返回的 JSON 和 CLI 一样。</p>
<ul>
  <li><strong>获取方式：</strong>以 MCP Bundle（<code>marsdawn.mcpb</code>）的形式附在<a href="https://github.com/redtear1115/marsdawn-mcp/releases">GitHub release</a> 上，或从源代码以 stdio 运行服务器。</li>
  <li><strong>Registry：</strong>还没上架 MCP Registry（目前版本：0.2.1）。要靠 registry 搜索找到它之前，请先到 repository 确认目前状态。</li>
  <li><strong>托管：</strong>只能自架，没有代管服务。服务器跑在你自己的机器上，就在 marsdawn 旁边。</li>
  <li><strong>系统要求：</strong>macOS、marsdawn 0.5.0 以上，以及运行服务器需要的 Node.js 20 以上。</li>
</ul>

<h2>只能在你允许的文件夹里运行</h2>
<p>两个工具都只能在你允许的文件夹里读写：扩展的「Allowed folders」设置（默认是空的），或者你的 MCP 客户端提供的 roots。两者都没设置时，每次调用都会被拒绝，拒绝消息会说明怎么设置。每个路径都必须是绝对路径，而 <code>export_markdown_to_pdf</code> 只会写出 <code>.pdf</code> 文件，不会通过 symlink 写。</p>
<p><strong>安全性：</strong>请更新到 <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>&#8212;&#8212;0.1.0 和 0.2.0 会让调用把 PDF 写到你账号能写入的任何路径，已在 <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a> 修复。</p>

<h2>同一个 export，三扇门</h2>
<p>不管从哪个界面调用，底层行为都一样：同一套输出程序、同样的主题和纸张大小，Mermaid 图表画不出来时也是同样的 <code>diagramErrors</code>。这页不重复那份规格&#8212;&#8212;<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>里有完整内容。</p>

<h2>接下来</h2>
<ul>
  <li>完整 JSON schema 和所有退出代码：<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。</li>
  <li>给 Claude Code 等 agent 用的一个文件：<a href="/zh-hans/cli/skill/">marsdawn skill</a>。</li>
  <li>精简的 JSON 结果为什么对 agent 自己的 context 很重要：<a href="/zh-hans/token-efficient-review/">节省 token 的审阅方式</a>。</li>
</ul>
""",
    }
    pages['cli/skill'] = {
        "title": '让写程序的 agent 把 Markdown 转 PDF 的 skill · MarsDawn',
        "description": '一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。',
        "body": f"""
<section class="intro">
  <h1>让 agent 把写好的文稿拿给你看，也帮你做出 PDF。</h1>
  <p>这个 skill 是一个 Markdown 文件。它教写程序的 agent 把自己写的文稿在 MarsDawn 里打开给你审阅，也教它安装 <code>marsdawn</code>、确认它能用、把文稿导出成 PDF 并读懂结果。</p>
</section>
<div class="summary"><p><strong>一个 Markdown 文件，放在 <code>~/.claude/skills/marsdawn/SKILL.md</code>。</strong>有了它，你的 agent 会安装 <code>marsdawn</code>、导出 PDF 并读懂 JSON 结果；运行任何命令之前，它还是会先问你。</p></div>
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
<h3>设备与使用的人</h3>
<ul>
  <li><strong>同步：</strong>MarsDawn 不会同步文稿，文稿存在哪里就留在哪里；要在另一台 Mac 上使用，请放在你原本就会同步的文件夹。</li>
  <li><strong>iPhone 和 iPad：</strong>没有这两个平台的版本，MarsDawn 只给 Mac。</li>
  <li><strong>分享：</strong>没有账户，也不能共同编辑，因为 MarsDawn 是给一个人在自己的 Mac 上用的。</li>
  <li><strong>系统：</strong>MarsDawn 需要 macOS 26 以上。</li>
</ul>
<h3>文件与功能</h3>
<ul>
  <li><strong>编辑：</strong>你在左边写 Markdown，在右边阅读排版后的页面；页面本身不能直接编辑。</li>
  <li><strong>格式：</strong>MarsDawn 能输出 PDF 和打印，不能输出 Word 文件。</li>
  <li><strong>其他文件：</strong>纯文本文件和 PDF 以只读方式打开。</li>
  <li><strong>主题：</strong>内置 黎明、典雅、流行和活泼，每种都有浅色与深色，无法安装其他主题。</li>
  <li><strong>插件：</strong>MarsDawn 没有插件或扩展功能。</li>
</ul>
<h2>试用结束之后</h2>
<p>如果 14 天试用结束后没有解锁，就无法在 MarsDawn 中阅读和编辑文稿：文稿会打开，但内容会被遮住。你的文件维持原样，“快速查看”依然看得到，免费的命令行工具也依然能导出它们。</p>
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
<h3>编辑</h3>
<ul>
  <li>源代码、并排、预览三种布局，一个快捷键切换（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>两侧同步滚动，正在编辑的段落一直在眼前。</li>
  <li>编辑器内置 Markdown 语法高亮，颜色与预览主题一致。</li>
</ul>
<h3>和 Mac 的其他部分</h3>
<ul>
  <li>原生窗口、标签页、自动保存和版本记录。</li>
  <li>快速查看：在访达选取 Markdown 文件按空格键就能预览，图表也会显示。</li>
  <li>Siri 和快捷指令：用模板添加文稿、在笔记收件箱加上一行，或重新打开最近的文稿。</li>
  <li>支持{k.APP_UI_LANGUAGES}。</li>
</ul>
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
<ol class="loop-steps">
  <li><strong>免费下载。</strong> 在 Mac App Store 免费下载 MarsDawn。</li>
  <li><strong>14 天，全部都能用。</strong> 开始试用后，14 天内所有功能都能使用：所有主题与布局、PDF 输出与打印、快速查看，以及 Siri 和快捷指令操作。</li>
  <li><strong>买一次就解锁。</strong> 试用结束后想继续使用，花 USD 4.99 解锁一次就好。这是 App 内购买，不是订阅，不会自动续费，之后也不会再扣款。</li>
</ol>
<ul>
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
    pages['reviewing-ai-output'] = {
        "title": "为什么 AI 写的东西还是需要人读过 · MarsDawn",
        "description": "AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。",
        "body": """
<section class="intro">
  <h1>agent 写出来，还是得由你理解。</h1>
  <p>AI agent 可以很快写出一份计划、一份规格或一堆笔记。它写出来的东西，还是得由要照着做的人去理解&#8212;&#8212;不能因为读起来通顺，就直接相信。</p>
</section>

<div class="summary"><p><strong>MarsDawn 就是为了这种阅读而做的：排版后的页面和源代码并排，Mermaid 图表和 KaTeX 数学式直接画出来，而不是留着记号，让文稿的结构一眼就看得懂。</strong></p></div>

<h2>读起来通顺，不代表是对的</h2>
<p>Simon Willison 在谈 AI 辅助写代码时，对那些还会被继续维护、不是写完就丢的代码这么说：“the quality and understandability of the underlying code is crucial”（底层代码的质量和是否容易理解，至关重要，<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>，2025）。文稿也一样：agent 写出来读起来很顺的草稿，结构、数字或逻辑还是可能是错的，而通顺的文字并不会告诉你哪里该多留意。</p>

<h2>是推理，不是编译</h2>
<p>Thoughtworks 的 Birgitta B&#246;ckeler 讲得很直接：“LLMs are NOT compilers, interpreters, transpilers or assemblers of natural language, they are inferrers”（LLM 不是自然语言的编译器、解释器、转译器或汇编器，它们是推理器，<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>）。编译器要么接受你的输入，要么报告错误；agent 给你的东西即使能运行、读起来也通顺，也不保证是对的。还是得有人检查。</p>

<h2>MarsDawn 给读的人什么</h2>
<ul>
  <li>排版后的页面和源代码并排，两边一改就同步更新，让文字里的说法和它的结构同时在你眼前。</li>
  <li>Mermaid 图表画出来：agent 用文字描述的流程图，变成一个你真的能看懂的形状。</li>
  <li>KaTeX 数学式排版出来，不是留着一串反斜杠：公式看起来就是公式。</li>
  <li>它本身不会自动做任何事。MarsDawn 不会帮你评分、摘要或标记这份文稿&#8212;&#8212;它只是把结构摊在你面前，让你自己判断。</li>
</ul>

<h2>接下来</h2>
<ul>
  <li>这样的审阅怎么不花 agent 自己的 context：<a href="/zh-hans/token-efficient-review/">节省 token 的审阅方式</a>。</li>
  <li>把审阅过的文稿交给别人：<a href="/zh-hans/sharing-exported-pdfs/">分享 PDF</a>。</li>
  <li>MarsDawn 是什么，一页讲完：<a href="/zh-hans/">首页</a>。</li>
</ul>
""",
    }
    pages['sharing-exported-pdfs'] = {
        "title": "把 agent 写的东西交出去，不用教对方 Markdown · MarsDawn",
        "description": "把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。",
        "body": """
<section class="intro">
  <h1>把 PDF 交出去，不是把 Markdown 交出去。</h1>
  <p>agent 写完一份文稿，你审阅、修改过后，公司里不写程序的人也要看&#8212;&#8212;主管、客户，或另一个团队的人。他们不需要知道 <code>##</code> 或表格的竖线符号是什么意思。导出成 PDF，交给他们那份就好。</p>
</section>

<div class="summary"><p><strong>把审阅过的文稿导出成 PDF，发那个文件就好。</strong>它在任何地方都打得开，不需要懂 Markdown，也不用安装任何东西，看起来就跟你在预览里看到的一样&#8212;&#8212;图表、表格、格式都在。</p></div>

<h2>为什么不直接发 .md 文件</h2>
<p>用纯文本编辑器打开 <code>.md</code> 文件，看到的是记号，不是排好版的页面：<code>#</code> 是标题，<code>**</code> 包住粗体文字，围住 Mermaid 图表的代码块没有画出图。不写 Markdown 的人看不出这些记号原本要呈现什么，而为了一份文稿就要对方先装一个查看器，也要求太多。</p>

<h2>为什么不直接发截图</h2>
<p>截图只能定格文稿的其中一个画面，文稿可能有好几页，内容不能搜索也不能选取，转发几次、被压缩后也会更难读。PDF 不管文稿多长，都能保留文字、图表和分页。</p>

<h2>PDF 能给你什么</h2>
<ul>
  <li>对方已经有的东西就能打开&#8212;&#8212;Preview、浏览器、Acrobat、手机都行，不需要任何 Markdown 工具。</li>
  <li>Mermaid 图表会画出来，不会留着代码原样；代码块保留语法上色。</li>
  <li>分页位置经过安排，标题不会孤零零留在页尾，表格或图表也不会被切成两半。</li>
  <li>不管是从 MarsDawn app 还是免费的命令行导出，得到的都是同一份文件&#8212;&#8212;完整步骤请看<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF</a>。</li>
</ul>

<h2>接下来</h2>
<ul>
  <li>可以用哪些主题和布局导出：<a href="/zh-hans/themes/">预览主题与 PDF 导出</a>。</li>
  <li>从脚本或 agent 导出，而不是从 app：<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。</li>
  <li>为什么还是要先有人读过这份文稿：<a href="/zh-hans/reviewing-ai-output/">审阅的理由</a>。</li>
</ul>
""",
    }
    pages['themes'] = {
        "title": "MarsDawn 的预览主题与 PDF 导出 · MarsDawn",
        "description": "四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。",
        "body": """
<section class="intro">
  <h1>八种样子，一套导出。</h1>
  <p>MarsDawn 内置四种预览主题：黎明、典雅、流行和活泼，各有浅色与深色&#8212;&#8212;八种读文稿的样子。导出成 PDF 或打印，出来的就是你正在读的那个样子。</p>
</section>

<div class="summary"><p><strong>四种主题 &#215; 浅色与深色＝八种读文稿的方式，导出时用的正是你选的那一种。</strong>更多可导入的主题，还有让大家投稿主题的主题库，都还在规划中，尚未推出。</p></div>

<h2>四种主题</h2>
<!--theme-gallery-->
<ul>
  <li><strong>黎明</strong>，默认主题：和这个网站一样的暖色纸感与 Mars Rust 强调色。</li>
  <li><strong>典雅</strong>：比较朴素、像纸质文稿的配色。</li>
  <li><strong>流行</strong>：比较冷调、当代感的配色。</li>
  <li><strong>活泼</strong>：比较明亮、对比度较高的配色。</li>
</ul>
<p>每种主题都有各自的浅色和深色版本，所以切换 Mac 的外观，连带切换的是主题本身的配色，不只是界面的颜色。</p>

<h2>PDF 导出和打印用同一个主题</h2>
<p>导出成 PDF 或打印，用的是你主题的浅色配色：Mermaid 图表会直接画进去，代码块保留语法上色，分页时也会尽量不让标题和内容分开，或切开表格与图表。免费的 <a href="/zh-hans/cli/">marsdawn 命令行工具</a>使用同一套输出程序，所以脚本或 agent 也能用 <code>--theme</code> 生成一模一样的 PDF，四种主题都可以。</p>

<h2>规划中：更多主题，还有主题库</h2>
<p>之后会推出、但现在还没做的：更多可导入的预览主题，以及一个让大家投稿自己主题的网站主题库。<code>/themes/v1/</code> 这个路径已经为它保留。在那之前，MarsDawn 有的就是这四种内置主题，无法安装其他的。</p>

<h2>接下来</h2>
<ul>
  <li>完整的 PDF 导出步骤，从命令行开始：<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF</a>。</li>
  <li>MarsDawn 现在还做不到的事：<a href="/zh-hans/limits/">这份清单</a>。</li>
  <li>把导出的 PDF 交给不写 Markdown 的人：<a href="/zh-hans/sharing-exported-pdfs/">分享 PDF</a>。</li>
</ul>
""",
    }
    pages['token-efficient-review'] = {
        "title": "不花 agent token 的审阅方式 · MarsDawn",
        "description": "人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。",
        "body": """
<section class="intro">
  <h1>审阅不花 agent 的 token。</h1>
  <p>这个循环里有两件事分开来看，都很省：agent 调用工具拿回什么，以及确认结果排版正确要花多少力气。</p>
</section>

<div class="summary"><p><strong>工具调用返回的是一个小小的 JSON 对象，不是排版后的页面；排版后的页面由人在 MarsDawn 里阅读&#8212;&#8212;不会被读回 agent 的 context。</strong></p></div>

<h2>工具调用本身很便宜</h2>
<p>不管是从 CLI、skill，还是<a href="/zh-hans/cli/mcp/">MCP 服务器</a>调用 <code>marsdawn export</code>，返回的都是<a href="/zh-hans/cli/agents/">精简的 JSON 对象</a>：<code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code> 和 <code>diagramErrors</code>。完整 schema 在 <a href="/schemas/cli/export.v1.json">export.v1.json</a>。里面没有排版后的文稿内容。一份 50 页、有十几张 Mermaid 图表的 PDF，返回的字段和一份一页的笔记一样多。</p>

<h2>审阅在另一边进行</h2>
<p>PDF 生成之后，人会打开它&#8212;&#8212;在 MarsDawn 里，或任何 PDF 查看器&#8212;&#8212;阅读排版好的图表、数学式和版面。agent 不需要把排版结果读回自己的 context 才能确认它看起来对：审阅在另一个窗口、另一个屏幕上进行，不会变成又一轮花 token 描述一张图表长什么样子。</p>

<h2>这样省下什么</h2>
<ul>
  <li>不用把排版后的 Markdown、一张截图，或对截图的描述贴回对话里，只为了让 agent 确认导出成功。</li>
  <li>agent 不需要重建 Mermaid 图表或 KaTeX 公式排版后的样子，直接让人去看就好。</li>
  <li>不需要在第一次调用已经报告成功之后，再多一次调用去读取 PDF 的内容。</li>
</ul>

<h2>接下来</h2>
<ul>
  <li>调用 marsdawn 的三种方式&#8212;&#8212;CLI、skill 文件、MCP 服务器：<a href="/zh-hans/cli/mcp/">三种入口</a>。</li>
  <li>JSON 结果的每个字段：<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。</li>
  <li>为什么还是需要有人读 agent 写的东西：<a href="/zh-hans/reviewing-ai-output/">审阅的理由</a>。</li>
</ul>
""",
    }
    pages['view-markdown-on-mac'] = {
        "title": '在 Mac 上怎么看 Markdown 文件 · MarsDawn',
        "description": 'md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。',
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
<h2>在 MarsDawn 里读</h2>
<p>MarsDawn 是为 Mac 做的 Markdown 编辑器，已在 Mac App Store 上架。打开 <code>.md</code> 文件，排好的页面就在源代码旁边：</p>
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
<!--compare:macmd-features-->
<h2>价格与购买方式</h2>
<!--compare:macmd-buying-->
<h2>现在就能免费试试看</h2>
<p>MarsDawn 已在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具也能把任何 Markdown 文件转成 PDF，Mermaid 图表和代码高亮都在，而且不需要安装其他东西：</p>
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
    pages['vs/markdown-preview-tools'] = {
        "title": "在别处看 Markdown，对比 MarsDawn · MarsDawn",
        "description": "MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。",
        "body": """
<section class="intro">
  <h1>在别处看 Markdown，对比 MarsDawn。</h1>
  <p>如果你手边刚好开着 VS Code、浏览器或 Claude Desktop，用它们顺手看一眼 Markdown 文件也合理。以下是它们各自实际排版出什么、要花多少功夫才能看到，和在 MarsDawn 里打开同一份文件的比较。</p>
</section>
<h2>一眼看完</h2>
<!--compare:preview-tools-->

<h2>VS Code 内置的预览</h2>
<p>在 VS Code 按 <kbd>&#8984;&#8679;V</kbd>，就会用内置的预览窗格排版出 Markdown 文件，免费，不用另外安装。从 VS Code 1.121（2026 年 5 月）开始，这个预览也能原生画出 Mermaid 图表&#8212;&#8212;微软把一个 Mermaid 扩展并进了 VS Code 本体，以前需要另外装扩展，现在不用了。它做不到的：这是编辑器里的一个预览窗格，不是为了阅读而做的编辑器&#8212;&#8212;窗格旁边还有文件树、终端和 VS Code 能显示的其他所有面板，而 VS Code 本身是 Electron app，你装的是一整套开发环境，不是一个用来读文件的工具。</p>
<h2>看本机文件的浏览器扩展</h2>
<p>看本机 <code>.md</code> 文件，没有哪一个浏览器扩展是主流：Local Markdown Viewer、Markdown Viewer、MarkView 等等做的事都差不多，没有哪一个是默认会装的。每一个都要先做同一件事才能打开任何文件：把该扩展的“允许访问文件网址”打开，因为浏览器默认不让扩展读取 <code>file://</code> 开头的页面。这个权限每个扩展只要开一次，但也很容易忘记自己开过，或忘记为什么要开。开了之后，文件会显示在浏览器标签页里&#8212;&#8212;也就是说，看一个文件要开一整个浏览器。</p>
<h2>Claude Desktop 的文件预览</h2>
<p>Claude Desktop 显示的是已经在 Project 或对话里的文件。它不是为了浏览磁盘上任意文件而做的&#8212;&#8212;你能看的是对话里已经有的东西，不是一个可以一直开在旁边的笔记文件夹。Anthropic 自己列出<a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">可以上传的文件类型</a>是 PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON 和 XLSX，里面没有 Markdown。</p>
<h2>为了读一份文件，背后跑着一整套浏览器引擎</h2>
<p>VS Code 是 Electron app：内置一套 Chromium 和 Node.js 运行环境，不是原生的 Mac app。走浏览器扩展这条路，则是真的在浏览器里运行。不管哪一种，看一份 Markdown 文件都要有一整套浏览器引擎在背后跑。MarsDawn 是原生的 AppKit app：没有内置的浏览器运行环境、直接打开任何本地文件，不用装扩展，也不用记得开过哪个权限。</p>
<h2>接下来</h2>
<ul>
  <li>MarsDawn 也做不到的事：<a href="/zh-hans/limits/">这份清单</a>。</li>
  <li>今天就能免费把任何 Markdown 文件转成 PDF：<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF</a>。</li>
  <li>和一个 Mac 原生的查看器比较：<a href="/zh-hans/vs/macmd-viewer/">MacMD Viewer 对比 MarsDawn</a>。</li>
</ul>
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
    pages['changelog'] = {
        "title": '更新记录 · MarsDawn',
        "description": '免费的 marsdawn 命令行工具改了什么。',
        "body": f"""
<section class="intro">
  <h1>更新记录</h1>
  <p>免费的 marsdawn 命令行工具改了什么。Mac App Store 上的 MarsDawn，只有某个版本值得单独记一笔时才会出现在这里。0.5.1 以前的版本不列。</p>
</section>

<h2>marsdawn 0.5.1</h2>
<p>2026 年 9 月 19 日。PDF 输出，以及从命令行打开文件。</p>
<ul>
  <li>输出的 PDF 中，中文、日文与韩文的文字层已修正。</li>
  <li><code>marsdawn open --background</code> 会打开文件，但不会把 MarsDawn 带到最前面。</li>
  <li><code>marsdawn open</code> 可以指定一个文件夹。Mac App Store 上的 app 还不能显示文件夹，所以这个选项要等做得到的版本。</li>
</ul>
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
