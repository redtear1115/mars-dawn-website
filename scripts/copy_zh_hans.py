"""Simplified Chinese (zh-Hans) copy for the MarsDawn site, translated from the zh-hant copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': '隐私政策', 'support': '支持', 'cli': '命令行工具', 'agents': '给 AI agent 的 marsdawn 参考', 'using_cli': '使用 CLI', 'markdown-to-pdf': 'Markdown 转 PDF', 'skill': '给 agent 的 skill', 'view-markdown-on-mac': '在 Mac 上看 Markdown', 'vs-macmd-viewer': 'MacMD Viewer 对比 MarsDawn', 'updated': f"最后更新：{k.UPDATED}", 'tagline': '读 agent 写的 Markdown。', 'slogan': 'Markdown 的新黎明。', 'footer_store': 'MarsDawn 即将在 Mac App Store 上架。', 'footer_nav': '网站', 'more': '其他页面', 'yours': '你写的内容留在你的 Mac 上', 'pay-once': '免费试用，买一次就好', 'pdf': '导出 PDF', 'native': '为 Mac 而做', 'limits': 'MarsDawn 做不到的事', 'mcp': 'MCP 服务器', 'token-efficient-review': '节省 token 的审阅方式', 'vs-markdown-preview-tools': '在别处看 Markdown，对比 MarsDawn', 'themes': '预览主题与 PDF 导出', 'sharing-exported-pdfs': '分享导出的 PDF', 'reviewing-ai-output': '为什么 AI 写的东西还是需要人读过', 'reading-agent-output': '读懂 agent 交回来的 Markdown', 'agent-transparency': 'agent 的透明', 'reviewing-agent-plans': '审 agent 计划', 'agent-design-patterns': 'agent 设计模式', 'changelog': '更新记录', 'reading-notes': '编者的阅读笔记', 'reading-notes-anthropic': '阅读笔记：Anthropic', 'reading-notes-chip-huyen': '阅读笔记：Chip Huyen', 'reading-notes-lilian-weng': '阅读笔记：Lilian Weng', 'reading-notes-harrison-chase': '阅读笔记：Harrison Chase', 'reading-notes-langchain': '阅读笔记：LangChain（Jess Ou）', 'reading-notes-andrew-ng': '阅读笔记：Andrew Ng', 'consent_text': '本网站使用分析用 cookie，用来了解访客如何使用网站。除非你点击“接受”，否则这些 cookie 都不会启用。', 'consent_accept': '接受', 'consent_decline': '拒绝', 'consent_aria': 'Cookie 同意设置', 'cookie_settings': 'Cookie 设置', 'view_markdown_source': '查看 Markdown 源文件'}
    store_chip = '即将在 Mac App Store 上架'
    schema_notes = {'export': 'export 成功', 'open': 'open 成功，marsdawn 0.3.0 以后', 'error': '两个命令的失败结果', 'open_v1': 'open 成功，marsdawn 0.2.x，当时 <code>opened</code> 是路径清单'}
    example_plan = '# 计划：让导出更快\n\n这份计划由 agent 撰写，你审阅后再把它转成 PDF。\n\n## 步骤\n\n| 步骤 | 负责 | 状态 |\n|------|------|------|\n| 找出慢的页面 | Agent | 完成 |\n| 缓存算好的图表 | Agent | 审阅中 |\n\n目标是 50 页的文稿在 $t < 2\\,\\text{s}$ 内完成：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  草稿 --> 审阅 --> 发布\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'yours': ('你写的内容留在你的 Mac 上', '不需要账户，没有同步，也没有云端。'), 'pay-once': ('免费试用，买一次就好', '免费试用 14 天，之后 USD 4.99 买一次，没有订阅。'), 'pdf': ('导出 PDF', '图表、代码高亮、经过安排的分页。'), 'native': ('为 Mac 而做', '原生窗口、标签页、自动保存、快速查看。'), 'limits': ('MarsDawn 做不到的事', '购买前先知道。')}
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
            "alt": '用 MarsDawn 导出的 PDF，在内置的 PDF 查看器中打开，旁边有页面缩略图。',
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
        "body": k.render_legal_body("support", "zh-hans"),
    }
    pages['privacy'] = {
        "title": '隐私政策 · MarsDawn',
        "description": 'MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。',
        "body": k.render_legal_body("privacy", "zh-hans"),
    }
    pages['index'] = {
        "title": 'MarsDawn：Mac 上的 Markdown 编辑器，实时预览',
        "description": '给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 导出。即将在 Mac App Store 上架。',
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
<p><a href="/zh-hans/reading-agent-output/">如何审阅 agent 交回来的东西</a>。</p>
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
  <li>MarsDawn 1.0 会打开文件，并跳到指定的行。</li>
  <li><code>--json</code>：输出 JSON 结果，而不是文本。</li>
</ul>
<p>行号功能从 marsdawn 0.3.0 开始提供。</p>

<h3>marsdawn export</h3>
<p>把 Markdown 文件导出成分页的 PDF，使用和 MarsDawn 导出 PDF 相同的组件。不需要安装 MarsDawn app。相对路径的图片，会以输入文件所在的文件夹为准。</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF 的输出位置，默认是把输入文件的扩展名换成 <code>.pdf</code>。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：预览主题的浅色版本，默认读取 <code>$MARSDAWN_THEME</code>，否则用 <code>dawn</code>。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：纸张大小，默认 <code>a4</code>。</li>
  <li><code>--allow-remote-images</code>：导出时加载网络图片，默认关闭。</li>
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
  <li><code>5</code>：导出失败。</li>
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
  <li><code>export</code>：用和 MarsDawn app 相同的导出程序，把一个 Markdown 文件导出成分页的 PDF，不会打开任何窗口。</li>
  <li><code>open</code>：在 MarsDawn app 中打开一或多个 Markdown 文件，让人审阅，也可以指定每个文件要定位的行。</li>
</ul>

<h2>不做什么</h2>
<ul>
  <li>不从 stdin 读取 Markdown，请传入文件路径。</li>
  <li>不把 PDF 写到 stdout。PDF 一律写成文件，stdout 只输出结果。</li>
  <li>文件已存在时不会覆盖，除非加上 <code>--force</code>。</li>
  <li>不加载网络图片，除非加上 <code>--allow-remote-images</code>，而且只走 https。</li>
  <li>没有安装 MarsDawn 时，<code>open</code> 无法使用，会以代码 3 结束。<code>export</code> 不需要 app。</li>
  <li>MarsDawn 1.0 会跳到 <code>open</code> 指定的行。</li>
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
  <li>行号从 marsdawn 0.3.0 开始提供。MarsDawn 1.0 会打开文件，并跳到指定的行。</li>
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
<p>不管从哪个界面调用，底层行为都一样：同一套导出程序、同样的主题和纸张大小，Mermaid 图表画不出来时也是同样的 <code>diagramErrors</code>。这页不重复那份规格&#8212;&#8212;<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>里有完整内容。</p>

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
        "description": '一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。',
        "body": f"""
<section class="intro">
  <h1>让 agent 帮你做出 PDF。</h1>
  <p>这个 skill 是一个 Markdown 文件。它教写程序的 agent 安装 <code>marsdawn</code>、确认它能用、把文稿导出成 PDF 并读懂结果，这样写出 Markdown 的 agent，也能把 PDF 交给你。</p>
</section>
<div class="summary"><p><strong>一个 Markdown 文件，放在 <code>~/.claude/skills/marsdawn/SKILL.md</code>。</strong>有了它，你的 agent 会安装 <code>marsdawn</code>、导出 PDF 并读懂 JSON 结果；运行任何命令之前，它还是会先问你。</p></div>
<h2>在 Claude Code 中安装</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>需要做出 PDF 时，Claude Code 会自动加载它，你也可以用 <code>/marsdawn</code> 自己运行。它只是<a href="/cli/skill/SKILL.md">一个简短的文件</a>，安装前先读一遍。</p>
<p>其他 agent 也能用同一个文件。它是纯 Markdown，只有说明和命令，让你的 agent 读这个网址，或直接贴给它就好。这个文件是英文的。</p>
<h2>它教什么</h2>
<ul>
  <li>如果没有 <code>marsdawn</code>，就用 Homebrew 安装，再用 <code>marsdawn --version</code> 确认版本，而不是假设某个版本。</li>
  <li>用 <code>marsdawn export … --json</code> 导出，并读懂结果：PDF 存到哪里、有几页，以及有没有 Mermaid 图表没画出来。</li>
  <li>依退出代码分辨失败的原因：找不到文件、PDF 已经存在、导出失败、选项错误。</li>
  <li>只有装了 MarsDawn app 才用 <code>open</code>，而且绝不用它来做 PDF。</li>
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
  <li><strong>格式：</strong>MarsDawn 能导出 PDF 和打印，不能导出 Word 文件。</li>
  <li><strong>其他文件：</strong>纯文本文件和 PDF 以只读方式打开。</li>
  <li><strong>主题：</strong>内置 黎明、典雅、流行和活泼，每种都有浅色与深色，无法安装其他主题。</li>
  <li><strong>插件：</strong>MarsDawn 没有插件或扩展功能。</li>
</ul>
<h2>试用结束之后</h2>
<p>如果 14 天试用结束后没有解锁，就无法在 MarsDawn 中阅读、编辑、导出或打印文稿：文稿会打开，但内容会被遮住。你的文件保持原样，“快速查看”仍然可以显示它们，免费的命令行工具也仍然可以把它们导出为 PDF。<a href="/zh-hans/pay-once/">试用与解锁页面</a>列出了三个阶段的对照表。</p>
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
  <li><strong>14 天，全部都能用。</strong> 开始试用后，14 天内 MarsDawn 的所有功能都能使用：所有主题与布局、PDF 导出与打印，以及 Siri 和快捷指令操作。无论是否试用，访达中的“快速查看”都能使用。</li>
  <li><strong>买一次就解锁。</strong> 试用结束后想继续使用，花 USD 4.99 解锁一次就好。这是 App 内购买，不是订阅，不会自动续费，之后也不会再扣款。</li>
</ol>
<ul>
  <li>试用本身也不会扣款。试用结束时，除非你选择解锁，否则不会购买任何东西。</li>
  <li>不需要账户，MarsDawn 从不要求你创建账户。</li>
</ul>
<h2>各阶段能做什么</h2>
<!--compare:pay-once-states-->
<p>开始试用之前，MarsDawn 会先显示免费试用页面。开始试用不收费。</p>
<p>试用结束后，在 MarsDawn 中打开的 PDF 文件也会同样被锁定。</p>
<h2>如果没有解锁</h2>
<ul>
  <li>14 天后，在你解锁之前，无法在 MarsDawn 中阅读、编辑、导出或打印文稿。文稿仍会打开，但内容会被遮住。</li>
  <li>你的文件不会有任何改变。它们就是你 Mac 上的一般文件，在访达中用“快速查看”依然看得到。</li>
  <li>免费的 <a href="/zh-hans/cli/"><code>marsdawn</code> 命令行工具</a>不受试用影响，仍然可以把它们导出为 PDF。</li>
  <li>如果试用结束时有文稿正开在 MarsDawn 里，你输入的文本不会遗失，可以用“文件”▸“保存为…”保存。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": '在 Mac 把 Markdown 导出成 PDF，图表也在 · MarsDawn',
        "description": '在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。',
        "intro": f"""
<section class="intro">
  <h1>PDF 看起来就是你写的那一页。</h1>
  <p>导出成 PDF 或打印，使用主题的浅色配色。图表和代码高亮都会保留，分页位置也经过安排。</p>
</section>
""",
        "body": f"""
<h2>这代表什么</h2>
<ul>
  <li>Mermaid 图表直接画进 PDF。</li>
  <li>代码块保留语法高亮。</li>
  <li>分页时会尽量不让标题落在页面底部，也不切开代码、表格和图表。</li>
  <li>任何布局都能导出，只显示源代码时也可以。</li>
</ul>
<p>免费的 <a href="/zh-hans/cli/">marsdawn 命令行工具</a>使用同一套导出程序，所以脚本或 AI agent 也能得到一样的 PDF。</p>
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
  <li>为什么难读、该怎么读：<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</li>
  <li>agent 为什么要把计划摊开：<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a></li>
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
  <li>多 agent 交接常常就是要分享 PDF 的时候：<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>。</li>
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
<p>导出成 PDF 或打印，用的是你主题的浅色配色：Mermaid 图表会直接画进去，代码块保留语法上色，分页时也会尽量不让标题和内容分开，或切开表格与图表。免费的 <a href="/zh-hans/cli/">marsdawn 命令行工具</a>使用同一套导出程序，所以脚本或 agent 也能用 <code>--theme</code> 生成一模一样的 PDF，四种主题都可以。</p>

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
  <li>更完整的理由和检查清单：<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</li>
</ul>
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
<p>如果这份文件是 AI agent 写的，这正是 MarsDawn 要支持的循环：agent 写，你读排好的页面，agent 再修改。请看<a href="/zh-hans/">首页</a>，想让 agent 帮你开文件，请看<a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a>。为什么这样的阅读重要、怎么审一份计划，请看<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>和<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>。</p>
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
    pages['reading-agent-output'] = {
        "title": "读懂 agent 交回来的 Markdown · MarsDawn",
        "description": "AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。",
        "body": f"""
<section class="intro">
  <h1>agent 做完的工作，最后都变成一份你要读的 Markdown。</h1>
  <p>你请 coding agent 规划一次数据库迁移、写一份规格，或追一个 bug。它自己跑了一阵子，交回来的是一个文件：<code>plan.md</code>、<code>SPEC.md</code>、一份进度报告，或一份研究摘要。你能检查的工作，全在这份文件里。</p>
</section>

<div class="summary"><p><strong>agent 有没有做对，要读过它交回来的东西才知道。MarsDawn 就是为这种阅读做的 Mac app。</strong></p></div>

<h2>做 agent 的人怎么说</h2>
<p>以下引文照原文，我们的解读放在最后。</p>
<ul>
  <li>Anthropic 的〈Building Effective Agents〉（Erik S. 与 Barry Zhang，2024 年 12 月）列出打造 agent 的三个核心原则，其中一条是“Prioritize transparency by explicitly showing the agent&#8217;s planning steps.”（优先重视透明度：明确展示 agent 的规划步骤。）这是写给开发 agent 的人的原则；站在你这边，这份透明就是你手上那份要读的计划。</li>
  <li>同一篇也写到：“Agents can then pause for human feedback at checkpoints or when encountering blockers.”（Agent 可以在检查点或遇到阻碍时暂停，等待人类反馈。）注意原文用的是 <em>can</em>，可以，没有说必须。</li>
  <li>Chip Huyen 在〈Agents〉（2025 年 1 月）解释为什么规划要和执行分开：“Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it&#8217;s not going anywhere.”（没有监督的话，agent 可能执行那些步骤好几个小时，在 API 呼叫上浪费时间和金钱，你才发现它根本没有进展。）她也描述了一种失败：“The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.”（Agent 深信自己已完成任务，但其实并没有。）请它把 50 个人分到 30 间饭店房间，它只排了 40 人，还坚称做完了。</li>
  <li>Andrew Ng 在 The Batch（2024 年 4 月）谈 planning 这个设计模式：“On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results.”（一方面，规划是非常强大的能力；另一方面，它会导致较难预测的结果。）他讲的是可预测性，并没有呼吁要人工审阅，而且他相信规划能力很快会进步。</li>
</ul>
<p><strong>以下是我们的推论，不是作者的主张：</strong>agent 把计划摊开、在检查点停下来，那在检查点读计划的通常就是你。agent 可能以为自己做完了，那它的“完成报告”也得有人读过。上面这几位作者都没有提到 MarsDawn，也没有推荐 MarsDawn 或任何 Markdown 工具。</p>

<h2>比看起来难读</h2>
<p>文件很长，重要的地方很少在最上面。里面有 Mermaid 图表和数学式，看原始码很难跟上。你读到一半，agent 可能还在改写同一个文件。它通常不只交一个文件，有时还分散在不同的分支或 worktree。等你找到问题，说“缓存那段怪怪的”，agent 只能用猜的；说“<code>docs/plan.md:42</code> 在回填跑完前就把旧表删了”，它就知道要改哪里。</p>

<h2>MarsDawn 帮得上忙的地方</h2>
<ul>
  <li><strong>文件很长：</strong>侧边栏（&#8963;&#8984;S）的“大纲”标签页列出所有标题，点一下，两边窗格都会跳过去。</li>
  <li><strong>图表和数学式：</strong>Mermaid 和 KaTeX 直接画在预览里，和原始码并排（&#8984;2），两边一起卷动。</li>
  <li><strong>读到一半被改写：</strong>agent 改写文件时，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。</li>
  <li><strong>好几个文件：</strong>用“文件 &#9656; 打开文件夹&#8943;”（&#8679;&#8984;O）打开 agent 工作的文件夹，新文件大约一秒内就会出现在“文件”标签页；如果是 git 检出，清单上方会标出分支或工作树。</li>
  <li><strong>反馈要准：</strong>“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）把目前位置拷贝成 <code>docs/plan.md:42</code>，“拷贝给 AI”（&#8963;&#8997;&#8984;C）会在下面附上你选取的文字，直接贴给 agent 就好。</li>
</ul>
<p>另外两件事也和这个循环有关：agent 可以执行 <code>marsdawn open plan.md:42</code>，在 MarsDawn 里帮你打开文件，直接停在第 42 行，也就是它想先让你看的那一行；审完的文件可以从 app 导出 PDF，也可以用免费的 <code>marsdawn export</code> 指令。</p>
<p>MarsDawn 里没有 AI 模型。它不会帮你摘要计划、打分数，也不会告诉你哪里错了。读的人是你，它负责让又长又会变的文件保持好读，让你能准确指出是哪一行。</p>

<h2>五分钟审完一份 agent 计划</h2>
<p>用什么编辑器都适用。</p>
<ol>
  <li>先只看标题。大纲和你要求的对得上吗？少一段，通常就是少做一件事。</li>
  <li>找出所有写着“完成”“通过”“已验证”的地方，挑一个自己查：打开那个文件、跑那个测试、数一下笔数。</li>
  <li>找出做了就回不去的步骤：删资料、数据库迁移、force push，还有任何会寄出、付款或发布的动作。这些要等你明确点头。</li>
  <li>图表要看画出来的样子，逐一对照每个箭头和文字说的是不是同一回事。</li>
  <li>列出计划会动到的文件和系统。你没要求的部分，执行前先问清楚。</li>
  <li>反馈写成“位置、问题、改法”：“<code>plan.md:88</code>：回填排在删表之后，第 4、5 步对调。”一行只讲一个问题。</li>
</ol>
<p>时间只够做一步的话，就做第 2 步吧。以为自己已经做完的 agent，多半是在这一步被抓到的。完整版本、附实际例子：<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。app 上架之后，agent 也能用 <code>marsdawn open</code> 在 MarsDawn 里帮你打开文件。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; <a href="/zh-hans/cli/agents/">给 AI agent 的 marsdawn 参考</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>为什么 AI 写的东西需要人读，短一点的版本：<a href="/zh-hans/reviewing-ai-output/">为什么 AI 写的东西还是需要人读过</a>。</li>
  <li>审阅时不占用 agent 的 context：<a href="/zh-hans/token-efficient-review/">节省 token 的审阅方式</a>。</li>
  <li>agent 为什么要把计划摊开：<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a></li>
  <li>上面那份清单一步一步来，附实际例子：<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>。</li>
  <li>不同类型的 agent 会交给你什么文件：<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>。</li>
  <li>六篇更深入的笔记，谈打造 agent 的人实际说了什么：<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>。</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Erik S. 与 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：<a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> （引文依 2026-09-26 的线上版本；该文现已注明，文中提到的工具生态自 2024 年 12 月以来已有很多改变）</li>
  <li>Chip Huyen，〈Agents〉，2025 年 1 月 7 日：<a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng，〈Agentic Design Patterns Part 4, Planning〉，The Batch，2024 年 4 月 10 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": "Anthropic 说 agent 要透明，那摊开的东西谁来读？ · MarsDawn",
        "description": "Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。",
        "body": f"""
<section class="intro">
  <h1>Anthropic 说 agent 要透明，那摊开的东西谁来读？</h1>
  <p>Anthropic 在 2024 年 12 月发表了〈Building Effective Agents〉，写给打造 AI agent 的人。文章的总结列出三个原则，其中一个是透明。这篇要谈的是这个原则的另一端：agent 把步骤摊开之后，总得有人去读。</p>
</section>

<div class="summary"><p><strong>透明是 agent 要做到的事，读是你要做的事。Anthropic 要求开发者把 agent 的规划步骤摊开；对大多数在驱动 coding agent 的人来说，这些步骤最后会变成一份 Markdown 文件，要有人在对的时间点读它。</strong></p></div>

<h2>指南里写了什么</h2>
<p>Erik S. 与 Barry Zhang 在总结里这样写：</p>
<blockquote><p>&#8220;When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent&#8217;s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.&#8221;</p></blockquote>
<p>（实作 agent 时，我们尽量遵守三个核心原则：让 agent 的设计保持简单；优先重视透明度，明确展示 agent 的规划步骤；通过完整的工具文件与测试，仔细打造 agent 与电脑之间的接口（ACI）。）</p>
<p>这些是写给开发 agent 的人的设计原则，不是给使用者的操作指示。原则要求把步骤摊开，但没有说谁来读。</p>
<p>同一篇也描述了 agent 拿到任务之后会做什么：“Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.”（任务明确之后，agent 会自己规划、独立运作，必要时回头找人类要更多信息或判断。）还有：“Agents can then pause for human feedback at checkpoints or when encountering blockers.”（Agent 可以在检查点或遇到阻碍时暂停，等待人类反馈。）注意用词：<em>potentially</em>（必要时）和 <em>can</em>（可以）。检查点是 agent 可以有的设计，不是一定要有。</p>

<h2>大部分的检查，不是你在做</h2>
<p>这里很容易讲过头，所以先看指南真正放在前面的是什么。agent 会拿外界的结果来检查自己：“During execution, it's crucial for the agents to gain &#8220;ground truth&#8221; from the environment at each step (such as tool call results or code execution) to assess its progress.”（执行过程中，agent 必须在每一步从环境取得“ground truth”，例如工具呼叫的结果或程序执行的结果，用来评估自己的进度。）这句话里的 ground truth 指的是测试结果和工具输出，不是人。</p>
<p>指南对风险也讲得很直接：“The autonomous nature of agents means higher costs, and the potential for compounding errors.”（Agent 的自主性意味着更高的成本，以及错误不断累积的可能。）它给的解方是在沙盒环境里大量测试、加上适当的防护，并没有说“要读得更仔细”。</p>
<p>人真正出场，是在附录谈 coding agent 的段落：“However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.”（然而，自动化测试虽然有助于验证功能，但要确保解法符合更广泛的系统需求，人工审阅仍然至关重要。）这句讲的是代码。不过它点出的落差，用过 agent 的人都不陌生：测试能告诉你东西能动，不能告诉你那是不是你要的。</p>

<h2>摊开的步骤，最后去了哪里</h2>
<p><strong>以下是我们的解读，不是 Anthropic 的主张。</strong></p>
<p>如果你每天都在用 coding agent，它的规划步骤通常不会出现在什么仪表板上，而是变成文件：<code>plan.md</code>、一份有勾选框的待办清单、一个 agent 一直在改写的进度档，最后再来一份总结。从你这边看，透明的意思就是要读的东西变多了。</p>
<p>把步骤摊开，是 agent 那一半的责任。另一半，是有人在关键时刻读它：数据库迁移执行之前、分支合并之前、接受“做完了”之前。一个 agent 把所有东西都写进一份 600 行、没人打开的文件，纸面上很透明，实际上没人在看。</p>
<p>Harrison Chase 在 2024 年也讲过类似的话，不过他谈的是 agent 框架该怎么设计，不是文件：“You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”（你会希望能观察系统内部发生了什么，因为它实际采取的步骤事先可能无法得知。）他讲的是给开发 agent 的人用的工具。如果你是驱动 agent 的那个人，它一直在写的那份纯文字档，常常就是你看得到的部分。</p>
<p>以上几位作者都没有提到 MarsDawn，也没有推荐 MarsDawn 或任何 Markdown 工具。</p>

<h2>比看起来难读</h2>
<p>文件很长，重要的地方很少在最上面。说明这次改动的那张图，是一段 Mermaid 原始码，不是图（想在 Mac 上看到排好的样子，可以先看<a href="/zh-hans/view-markdown-on-mac/">在 Mac 上怎么看 Markdown 文件</a>）。你读到一半，agent 可能正在改写它。文件常常不只一份，有时还分散在不同的分支或 worktree。等你真的找到问题，说“缓存那段怪怪的”，agent 只能用猜的。完整的说明在<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 是为这种阅读做的 Mac app。它不会让 agent 变得更透明，里面也没有 AI 模型：它不会帮你摘要计划，也不会告诉你计划对不对。它做的是：</p>
<ul>
  <li><strong>文件很长：</strong>“显示 &#9656; 显示边栏”（&#8963;&#8984;S）打开“大纲”标签页，列出所有标题，点一下就跳过去。</li>
  <li><strong>图表和数学式：</strong>原始码和排好的页面并排（&#8984;2），两边一起卷动，Mermaid 和 KaTeX 直接画出来。图表写错时，预览会显示它的原始码，下方附上错误信息。</li>
  <li><strong>读到一半被改写：</strong>agent 改写文件时，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。</li>
  <li><strong>好几个文件：</strong>用“文件 &#9656; 打开文件夹&#8943;”（&#8679;&#8984;O）打开 agent 工作的文件夹，新文件大约一秒内就会出现在“文件”标签页；如果是 git 检出，清单上方会标出分支或工作树。</li>
  <li><strong>指出是哪一行：</strong>“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）把目前位置拷贝成 <code>docs/plan.md:42</code>，“拷贝给 AI”（&#8963;&#8997;&#8984;C）会在下面附上你选取的文字，直接贴给 agent 就好。</li>
</ul>
<p>读的人还是你。MarsDawn 负责让一份又长又会变的文件，在你读的时候保持好读。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>agent 的产出为什么难读，以及一份检查清单：<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</li>
  <li>那份清单一步一步来，附实际例子：<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>。</li>
  <li>不同类型的 agent 会交给你什么文件：<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>。</li>
  <li>为什么 AI 写的东西需要人读，短一点的版本：<a href="/zh-hans/reviewing-ai-output/">为什么 AI 写的东西还是需要人读过</a>。</li>
  <li>这份指南自己的 workflow 模式，更深入的一篇：<a href="/zh-hans/reading-notes/anthropic-building-effective-agents/">Anthropic 把 workflow 和 agent 分开来看，你的阅读落在哪一边？</a></li>
  <li>Harrison Chase 对可观测性的主张，更深入的一篇：<a href="/zh-hans/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看</a></li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Erik S. 与 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：<a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> （引文依 2026-09-26 的线上版本；该文现已注明，文中提到的工具生态自 2024 年 12 月以来已有很多改变）</li>
  <li>Harrison Chase，〈What is an agent?〉，LangChain，2024 年 6 月 28 日，存档版本：<a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> （原网址现在显示的是 2026 年的另一篇文章）</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": "五分钟审完一份 agent 计划 · MarsDawn",
        "description": "agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。",
        "body": f"""
<section class="intro">
  <h1>五分钟审完一份 agent 计划</h1>
  <p>agent 写好一份计划，正等你点头。你手上只有五分钟，不是一个小时。下面这套做法用什么编辑器都行，连纯文字编辑器也可以。其中几步 MarsDawn 帮得上忙，我们会讲清楚是哪几步；最重要的那一步，它帮不上。</p>
</section>

<div class="summary"><p><strong>不要从头读到尾。先看架构，再查一个宣称，找出做了就回不去的步骤，看图表和影响范围，最后写出 agent 看得懂、改得动的反馈。六个步骤，大约五分钟。</strong></p></div>

<h2>为什么要在执行前审</h2>
<p>Chip Huyen 解释为什么规划要和执行分开时，把代价讲得很白：“Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it&#8217;s not going anywhere.”（没有监督的话，agent 可能执行那些步骤好几个小时，在 API 呼叫上浪费时间和金钱，你才发现它根本没有进展。）我们补一句：计划是抓错最便宜的地方。在 <code>plan.md</code> 里改一行，只要一句话；等 agent 跑完再收拾，可能要花掉一个下午。</p>

<h2>范例</h2>
<p>你请 agent 把使用者头像搬到物件储存，而且旧链接不能坏。它交回来的是这份：</p>
<pre><code># 计划：把使用者头像搬到物件储存

## 目标
头像改由物件储存提供，不再放在 app 服务器上。

## 步骤
1. 加入储存用的 client 与设定。&#9989; 完成
2. 写一支脚本，把现有头像复制到 bucket。
3. 把模板里的头像网址换掉。
4. 从服务器删除 `public/avatars/`。
5. 执行复制脚本。

## 状态
所有测试都通过。</code></pre>
<p>读起来很顺。照做的话，它也会在复制任何一张头像之前，先把全部头像删光。</p>

<h2>六个步骤</h2>
<p><strong>1. 先只看标题。</strong>（大约一分钟）大纲和你要求的对得上吗？少一段，通常就是少做一件事。这份只有“目标”“步骤”“状态”。你要求旧链接不能坏，可是没有任何一段讲旧链接，也没有讲出问题时怎么退回去。这就是你的第一条意见。</p>
<p>在终端机跑 <code>grep -n '^#' plan.md</code>，就只会印出标题；大部分编辑器也有大纲预览。在 MarsDawn 里，侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页会列出所有标题，点一下就跳过去。</p>
<p><strong>2. 找出所有写着“完成”“通过”“已验证”的地方，挑一个自己查。</strong>（大约一分钟）打开那个文件、跑那个测试、数一下笔数。Chip Huyen 描述过一种失败：“The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.”（Agent 深信自己已完成任务，但其实并没有。）她举的例子是：请 agent 把 50 个人分到 30 间饭店房间，它只排了 40 人，还坚称做完了。</p>
<pre><code>grep -n -E '完成|通过|验证|&#9989;' plan.md</code></pre>
<p>在这份计划里，会找到“&#9989; 完成”和“所有测试都通过”。是哪些测试？有任何一个碰到头像吗？自己跑一次，或直接问。这一步 MarsDawn 没办法替你做，除了你，没有人能替你做。</p>
<p><strong>3. 找出做了就回不去的步骤。</strong>（大约一分钟）删资料、数据库迁移、force push，还有任何会寄出、付款或发布的动作。这些要等你明确点头。Chip Huyen 从系统设计的角度讲过同一件事：“If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.”（如果计划牵涉有风险的操作，例如更新数据库或合并代码变更，系统可以在执行前要求人类明确核准，或交给人类自己执行。）这份计划的第 4 步会删掉原始文件，而且排在第 5 步复制之前。</p>
<p><strong>4. 图表要看画出来的样子，逐一对照每个箭头和文字说的是不是同一回事。</strong>流程图画着“复制 &#8594; 检查 &#8594; 删除”，步骤却不是这个顺序，这本身就是一个发现。这份计划没有图，今天可以跳过。有图的时候，请看画出来的图，不要看 Mermaid 原始码：很多编辑器都有预览，〈<a href="/zh-hans/view-markdown-on-mac/">在 Mac 上怎么看 Markdown 文件</a>〉和〈<a href="/zh-hans/vs/markdown-preview-tools/">在别处看 Markdown，对比 MarsDawn</a>〉整理了各种做法。在 MarsDawn 里，画好的图就在原始码旁边（&#8984;2）；图表写错时，预览会显示原始码、下方附上错误信息，这也值得单独写一条意见。</p>
<p><strong>5. 列出计划会动到的文件和系统，你没要求的部分，先问清楚。</strong>（第 4、5 步合起来大约一分钟）这份会动到：储存设定、模板、服务器上的一个文件夹、一个 bucket。这个 bucket 谁读得到？你没说它要公开。如果你用 MarsDawn 打开 agent 工作的文件夹（“文件 &#9656; 打开文件夹&#8943;”，&#8679;&#8984;O），它新写的文件大约一秒内就会出现在“文件”标签页，清单上方也会标出 git 分支或工作树，你就知道自己审的是哪一份检出。</p>
<p><strong>6. 反馈写成“位置、问题、改法”，一行只讲一个问题。</strong>（最后一分钟）</p>
<pre><code>plan.md:10：第 5 步还没复制，这里就先删了。先复制、核对数量，再删；删之前等我确认。
plan.md:14：是哪些测试？加一个切换后加载旧头像网址的测试。
plan.md:6：没有处理旧链接。加一步让旧链接继续能用，也写出怎么退回去。</code></pre>
<p>有行号的编辑器都能做到。在 MarsDawn 里，“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）会把目前位置拷贝成 <code>plan.md:10</code>，“拷贝给 AI”（&#8963;&#8997;&#8984;C）会在下面附上你选取的文字。</p>

<h2>只有一分钟的话</h2>
<p>就做第 2 步吧。以为自己已经做完的 agent，多半是在这一步被抓到的。</p>

<h2>五分钟不够的时候</h2>
<p>有时候你判断不了某一步对不对，因为它超出你熟悉的范围。Jess Ou 在 LangChain 2026 年介绍 agent 的文章里，用两句话讲完：“Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.”（无法评估的判断，就不要外包出去。如果你自己认不出正确答案，agent 也认不出来。）我们的看法是：判断不了，不是赶快核准的理由，而是该去找懂的人问一下的理由。</p>

<h2>MarsDawn 在这里做什么、不做什么</h2>
<p>MarsDawn 里没有 AI 模型。它不会帮你找出这份计划的问题，第 2、3 步也不会替你做。它做的是让文件在你审的时候保持好读：第 1 步有大纲，第 4 步有画好的图，第 5 步有“文件”标签页，第 6 步有行号引用。你读到一半 agent 改了计划，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。</p>
<p>计划定案、要给别人看的时候，〈<a href="/zh-hans/sharing-exported-pdfs/">把 agent 写的东西交出去，不用教对方 Markdown</a>〉和〈<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF 工具</a>〉说明了怎么转成 PDF 交出去。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>agent 的产出为什么难读：<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</li>
  <li>agent 为什么要把计划摊开：<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a></li>
  <li>agent 交回来的不只有计划：<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>。</li>
  <li>Chip Huyen 的 read-only／write action 分类，更深入的一篇：<a href="/zh-hans/reading-notes/chip-huyen-agents/">Chip Huyen 的 read-only／write action 分类，核准前为什么要看它</a></li>
  <li>Andrew Ng 自己怎么帮设计模式排序，更深入的一篇：<a href="/zh-hans/reading-notes/andrew-ng-design-patterns/">Andrew Ng 自己帮四种设计模式的可预测程度排序</a></li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Chip Huyen，〈Agents〉，2025 年 1 月 7 日：<a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou，〈What is an AI agent?〉，LangChain，2026 年 7 月 31 日：<a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": "四种 agent 设计模式，各自会交给你什么文件 · MarsDawn",
        "description": "Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。",
        "body": f"""
<section class="intro">
  <h1>四种 agent 设计模式，各自会交给你什么文件</h1>
  <p>2024 年 3 月，Andrew Ng 在他的电子报 The Batch 介绍了四种 AI agent 的设计模式：reflection（反思）、tool use（使用工具）、planning（规划）和 multi-agent collaboration（多 agent 协作）。大家通常从开发者的角度谈它们，当成让模型表现更好的方法。这篇换个方向看：如果你用的 agent 是照这些模式做的，最后会有什么东西落进你的文件夹？你该先读哪里？</p>
</section>

<div class="summary"><p><strong>四种模式是 Andrew Ng 提出的。每种模式通常会交给你什么文件、该检查什么，是我们自己的推论。这两件事他都没有写，他在这个系列里也没有主张要人工审阅。</strong></p></div>

<h2>四种模式，简单说</h2>
<p>Ng 在〈Agentic Design Patterns Part 1〉里介绍了这四种模式。简单说：<strong>reflection</strong> 是模型回头检查自己的成果，再加以改进；<strong>tool use</strong> 是让模型能呼叫网络搜寻、执行代码之类的工具；<strong>planning</strong> 是模型自己拟出多步骤的计划再执行；<strong>multi-agent collaboration</strong> 是好几个 agent 分工、互相讨论。</p>
<p>他在 Part 1 用一个代码基准测试 HumanEval 说明这些模式的效果，数据是他的团队整理多个研究团队的结果：“GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.”（GPT-3.5 在 zero-shot 下的正确率是 48.1%，GPT-4 在 zero-shot 下好一些，是 67.0%。但和加入迭代式 agent 工作流程相比，从 GPT-3.5 换到 GPT-4 的进步就显得微不足道：放进 agent 循环后，GPT-3.5 最高可达 95.1%。）这些数字只针对一个代码基准测试，95.1% 是最好的情况（"up to"，最高可达）。它们说明 agent 工作流程能提升产出质量，但完全没有谈到谁来检查。</p>
<p><strong>以下“交给你什么文件”和“该检查什么”，都是我们的解读，不是 Ng 的。</strong>实际的 agent 通常会混用好几种模式。一个 coding agent 可能在同一次工作里规划、跑工具、再检查自己的成果，所以四种文件你常常会一次全收到。</p>

<h2>1. Reflection：一份已经自己审过的草稿</h2>
<p>Ng 谈 reflection 的那篇，把它说成是把原本由人给的反馈自动化：“What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?”（如果把提出批评性反馈这一步自动化，让模型自动批评自己的产出、改进它的回答呢？）</p>
<p><strong>通常会交给你：</strong>一份改过的文件，有时附上一段自我检查，或是“边界情况都再确认过了”之类的句子。</p>
<p><strong>该检查什么：</strong>拿结果对照“你”的要求，不是对照 agent 自己的批评。自我检查也会出错。Chip Huyen 写道：“An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.”（有一种有趣的规划失败，是反思出错造成的：agent 深信自己已完成任务，但其实并没有。）Lilian Weng 在 2023 年 6 月（当时任职 OpenAI）于她的博客 Lil’Log 谈到当时的模型：“The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.”（缺乏专业知识可能使 LLM 不知道自己的缺陷，因而无法妥善判断任务结果的正确性。）她描述的那项研究里，LLM 对结果的评估和人类专家的评估并不一致。文件里写“已验证”的话，自己挑一项查。</p>

<h2>2. Tool use：一份“跑了什么”的报告</h2>
<p><strong>通常会交给你：</strong>一份总结，说 agent 跑了什么、搜了什么、得到什么结果。“跑完测试：全部通过。”一张结果表格。它找到的一串链接。</p>
<p>Anthropic 的指南把工具结果说成 agent 自我检查的依据：“During execution, it's crucial for the agents to gain &#8220;ground truth&#8221; from the environment at each step (such as tool call results or code execution) to assess its progress.”（执行过程中，agent 必须在每一步从环境取得“ground truth”，例如工具呼叫的结果或程序执行的结果，用来评估自己的进度。）这个检查发生在 agent 内部。到你手上的，是 agent 对这些结果的转述。</p>
<p><strong>该检查什么：</strong>每个宣称都要追得回你看得到的输出。挑总结里的一个数字，对照真正的输出；点开其中一个链接看看。</p>

<h2>3. Planning：<code>plan.md</code></h2>
<p><strong>通常会交给你：</strong>一份计划、一份规格，或一份 agent 做完一项就勾一项的待办清单。</p>
<p>Ng 在 Part 4 对这个模式讲得很坦白：</p>
<blockquote><p>&#8220;On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications&#8217; performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.&#8221;</p></blockquote>
<p>（一方面，规划是非常强大的能力；另一方面，它会导致较难预测的结果。就我的经验，Reflection 和 Tool Use 这两种模式我都能让它们稳定运作、提升应用程序的表现，但 Planning 还是比较不成熟的技术，我很难事先预测它会怎么做。）</p>
<p>他也很乐观：“But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.”（不过这个领域持续快速发展，我相信规划能力很快就会进步。）</p>
<p><strong>该检查什么：</strong>在执行前审计划，用〈<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>〉的方法：看架构、查一个宣称、找出回不去的步骤、看图表、看影响范围。agent 中途改写计划的话，拿它和你核准的版本比对；如果有用 git，<code>git diff plan.md</code> 就看得到改了什么。在 MarsDawn 里，“大纲”标签页让你一眼看出长计划的架构；计划被改写时会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。</p>

<h2>4. Multi-agent collaboration：好几份文件，好几个作者</h2>
<p><strong>通常会交给你：</strong>一个 agent 写的规格、另一个写的实作笔记、第三个写的审查意见，还有它们之间互相交接的摘要。有时每个 agent 各自在自己的分支或 worktree 里工作。</p>
<p><strong>该检查什么：</strong>交接的地方。一个 agent 在总结另一个的成果时，看有没有哪条需求没被带过去。找出彼此矛盾的两份文件，在任何人接着往下做之前，先决定哪一份才算数。在 MarsDawn 里，用“文件 &#9656; 打开文件夹&#8943;”（&#8679;&#8984;O）打开它们共用的文件夹：agent 写出新文件，大约一秒内就会出现在“文件”标签页；如果是 git 检出，清单上方会标出分支或工作树，两个窗口就算开着不同分支上同名的文件，也不会搞混。成果要交给不读 Markdown 的人时，可以看〈<a href="/zh-hans/sharing-exported-pdfs/">把 agent 写的东西交出去，不用教对方 Markdown</a>〉。</p>

<h2>一览表</h2>
<table>
<thead><tr><th>模式（Ng 提出）</th><th>通常会交给你（我们的推论）</th><th>先读哪里（我们的建议）</th></tr></thead>
<tbody>
<tr><td>Reflection 反思</td><td>一份改过的草稿，可能附自我检查</td><td>对照你自己的要求；挑一个“已验证”自己查</td></tr>
<tr><td>Tool use 使用工具</td><td>一份“跑了什么、得到什么”的报告</td><td>挑一个宣称，追回真正的输出</td></tr>
<tr><td>Planning 规划</td><td><code>plan.md</code>、规格、待办清单</td><td>执行前的五分钟审阅</td></tr>
<tr><td>Multi-agent collaboration 多 agent 协作</td><td>好几个 agent 写的好几份文件，可能分散在不同分支</td><td>交接的地方，以及哪一份才算数</td></tr>
</tbody>
</table>
<p>上面引用的作者都没有提到 MarsDawn，也没有推荐 MarsDawn 或任何 Markdown 工具。MarsDawn 里没有 AI 模型：它不知道一份文件是哪种模式产生的，也不会替你做这些检查。它负责让这些文件在你检查的时候保持好读。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF，详见〈<a href="/zh-hans/markdown-to-pdf/">Markdown 转 PDF 工具</a>〉。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>agent 的产出为什么难读，以及一份检查清单：<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>。</li>
  <li>完整的计划审阅方法：<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>。</li>
  <li>透明对你的要求是什么、不是什么：<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a></li>
  <li>Andrew Ng 自己怎么帮这些模式排序，更深入的一篇：<a href="/zh-hans/reading-notes/andrew-ng-design-patterns/">Andrew Ng 自己帮四种设计模式的可预测程度排序</a></li>
  <li>Lilian Weng 更早的 agent 蓝图，更深入的一篇：<a href="/zh-hans/reading-notes/lilian-weng-llm-agents/">Lilian Weng 2023 年画的 agent 蓝图，每个部件会留下什么文件</a></li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Andrew Ng，〈Agentic Design Patterns Part 1〉，The Batch，2024 年 3 月 20 日：<a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng，〈Agentic Design Patterns Part 2, Reflection〉，The Batch，2024 年 3 月 27 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng，〈Agentic Design Patterns Part 4, Planning〉，The Batch，2024 年 4 月 10 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen，〈Agents〉，2025 年 1 月 7 日：<a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng，〈LLM Powered Autonomous Agents〉，Lil’Log，2023 年 6 月 23 日：<a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S. 与 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：<a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> （引文依 2026-09-26 的线上版本）</li>
</ul>
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
<p>2026 年 9 月 19 日。PDF 导出，以及从命令行打开文件。</p>
<ul>
  <li>导出的 PDF 中，中文、日文与韩文的文字层已修正。</li>
  <li><code>marsdawn open --background</code> 会打开文件，但不会把 MarsDawn 带到最前面。</li>
  <li><code>marsdawn open</code> 可以指定一个文件夹。Mac App Store 上的 app 还不能显示文件夹，所以这个选项要等做得到的版本。</li>
</ul>
""",
    }
    pages['reading-notes'] = {
        "title": "编者的阅读笔记 · MarsDawn",
        "description": "六篇短笔记，谈打造 AI agent 的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读 agent 交回来的东西”的人分别意味着什么。",
        "body": f"""
<section class="intro">
  <h1>编者的阅读笔记</h1>
  <p>有六个人写过 AI agent 是怎么运作的：agent 是什么组成的、什么样才算“agentic”、哪些设计模式真的撑得住、哪些还不成熟。他们都没有写过“怎么读 agent 交回来的东西”，也都没有提到 MarsDawn 或推荐任何 Markdown 工具。我们照每篇文章自己的脉络去读，清楚标出我们自己的解读从哪里开始，然后对每个来源问同一个问题：因为这篇文章讲的东西，最后会有什么文件落进你的文件夹？读那份文件的时候，MarsDawn 帮得上什么忙？</p>
</section>

<p>想先看实用一点的版本，可以从《<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>》和《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》开始。这六篇笔记比那两页更贴近原始文章；每一篇都能单独读，顺序不拘。</p>

<ul>
  <li>《<a href="/zh-hans/reading-notes/anthropic-building-effective-agents/">Anthropic 把 workflow 和 agent 分开来看，你的阅读落在哪一边？</a>》&#8212;&#8212;Anthropic 写给打造 agent 的人的指南，把固定的流程和自己决定下一步的模型分开来，还描述了一种“审查者”其实是另一次 LLM 调用、不是人的 workflow。</li>
  <li>《<a href="/zh-hans/reading-notes/chip-huyen-agents/">Chip Huyen 的 read-only／write action 分类，核准前为什么要看它</a>》&#8212;&#8212;她对 agent 的简单定义，以及“只是看”和“会改变东西”这两种动作的差别，正好是五分钟审阅最该花时间的地方。</li>
  <li>《<a href="/zh-hans/reading-notes/lilian-weng-llm-agents/">Lilian Weng 2023 年画的 agent 蓝图，每个部件会留下什么文件</a>》&#8212;&#8212;大脑、规划、记忆、工具使用：她自己对 agent 组成的架构，以及她点名的一个限制：计划遇到意外时不太会调整。</li>
  <li>《<a href="/zh-hans/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看</a>》&#8212;&#8212;他对 agent 的技术定义，以及他自己主张的：系统愈往光谱的自主那端走，就愈需要看得到系统内部。</li>
  <li>《<a href="/zh-hans/reading-notes/langchain-what-is-an-agent/">Jess Ou 的评测流程，里面还留给你的那一步</a>》&#8212;&#8212;2026 年 7 月，LangChain 在 Harrison Chase 2024 年那篇文章原本的网址上，发表了 Jess Ou 写的新版《What is an AI agent?》；她的定义几乎和他的一字不差，接下来也讲清楚自动化评测到哪里为止，剩下的还是要人来做。</li>
  <li>《<a href="/zh-hans/reading-notes/andrew-ng-design-patterns/">Andrew Ng 自己帮四种设计模式的可预测程度排序</a>》&#8212;&#8212;在 The Batch 的五篇文章里，他直接说出自己觉得哪些模式比较可靠、哪些难以预测。</li>
</ul>

<p>这六篇文章都没有主张“应该更仔细审阅 agent 的产出”，也都不是在谈 MarsDawn。这个连结是我们自己画的，每篇笔记都会这样说清楚。</p>
""",
    }
    pages['reading-notes/anthropic-building-effective-agents'] = {
        "title": "Anthropic 把 workflow 和 agent 分开来看，你的阅读落在哪一边？ · MarsDawn",
        "description": "Anthropic 在 2024 年 12 月发表的指南把 workflow 和 agent 分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。",
        "body": f"""
<section class="intro">
  <h1>Anthropic 把 workflow 和 agent 分开来看，你的阅读落在哪一边？</h1>
</section>

<div class="summary"><p><strong>Anthropic 在 2024 年 12 月发表的《Building Effective Agents》，是写给打造 AI agent 的人看的指南。一开头就把“workflow”和“agent”分开，接着建议先从能用的最简单做法开始&#8212;&#8212;也可能完全不需要 agentic 系统&#8212;&#8212;只有在这样还不够的时候，才用得上它整理出的五种 workflow 模式。其中一种模式，是让另一次 LLM 调用坐上审查者的位置。这篇要谈的就是这种模式，以及另外四种模式各自会留下什么给你读。</strong></p></div>

<h2>指南主张什么</h2>
<p>Erik S. 与 Barry Zhang 写这篇文章，是给正在决定怎么用 LLM 打造系统的工程师看的。文章一开头先下了一个定义：</p>
<blockquote><p>&#8220;Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.&#8221;</p></blockquote>
<p>（Workflow 是 LLM 和工具透过事先写好的程序路径被安排执行的系统；相对地，agent 则是 LLM 自己动态决定流程、自己决定怎么使用工具、掌控自己怎么完成任务的系统。）</p>
<p>接着，他们的建议很克制：</p>
<blockquote><p>&#8220;When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.&#8221;</p></blockquote>
<p>（用 LLM 打造应用程序时，我们建议先找出最简单可行的做法，只有在真的需要时才增加复杂度。这可能代表根本不需要打造 agentic 系统。）</p>
<p>需要更多结构的时候，他们描述了五种 workflow 模式：prompt chaining（把任务拆成一连串调用，步骤之间可以加检查）、routing（路由）、parallelization（并行化）、orchestrator-workers（一个 LLM 把任务拆给多个 worker LLM 执行，再把结果合起来），还有 evaluator-optimizer。最后这一种，原文是这样写的：</p>
<blockquote><p>&#8220;In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.&#8221;</p></blockquote>
<p>（在 evaluator-optimizer workflow 里，一次 LLM 调用产生答案，另一次调用则在循环里负责评估、给反馈。）</p>
<p>Anthropic 在这份指南里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。这份指南谈透明和“检查点”的部分，《<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a>》已经完整谈过，这篇不再重复；那篇谈人工审阅 code 的那句话，来自附录里专门讲 coding agent 的段落，脉络也在那篇文章里。</p>

<h2>以下是我们的解读，不是 Anthropic 的</h2>
<p>Anthropic 没有说 workflow 跑完之后谁来检查最终结果，这整篇也不是在谈文件，而是给打造 agent 的人的架构决定。但这五种模式，会留下给你读的东西并不一样。Prompt chaining 和 routing 通常是看不见的管线；就算有东西送到你手上，也只是这条链最后一次调用的输出，跟其他单次回答没两样。Orchestrator-workers 就不同了：如果你的 coding agent 内部用的是这种模式，落进你文件夹的可能是一份由好几个 worker 调用拼起来、再由 orchestrator 组合成的文件，其中一个 worker 那一段出了错，很容易被整体读起来很顺的摘要盖过去。</p>
<p>Evaluator-optimizer 特别值得停下来想一下，因为指南把原本可能由人来坐的审查者位置，换成了另一次 LLM 调用。这确实能便宜地抓到一类错误，但终究还是模型照着某组标准去检查模型，这个系列里也有作者提过这个顾虑：模型评判自己或另一个模型的成果。指南完全没有说要有人再复核 evaluator 的判断，它根本没表态。如果你才是最后要读这一切的人，“循环通过了”和“我自己查过了”不是同一句话&#8212;&#8212;就算你手上的文件两种情况看起来一模一样。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 不知道一份文件是哪种 workflow 模式做出来的，里面也没有 AI 模型&#8212;&#8212;它不会自己跑一次 evaluator 步骤，也没办法告诉你 Anthropic 描述的那个评估到底做得好不好。它做的是：侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页列出一份 orchestrator 拼出来的长文件的所有标题，点一下就跳过去；源代码和排好的页面并排（&#8984;2），一起滚动，Mermaid 图表和 KaTeX 数学式都直接画出来。agent 读到一半改写文件的话，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未保存的修改。“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）把你的位置拷贝成 <code>docs/plan.md:42</code>，直接贴回 agent 的对话里就好。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>这份指南谈透明和检查点的完整讨论：《<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a>》</li>
  <li>agent 的产出为什么普遍难读：《<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Erik S. 与 Barry Zhang，《Building Effective Agents》，Anthropic，2024 年 12 月 19 日：<a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> （2026-09-26 读取并引用）</li>
</ul>
""",
    }
    pages['reading-notes/chip-huyen-agents'] = {
        "title": "Chip Huyen 的 read-only／write action 分类，核准前为什么要看它 · MarsDawn",
        "description": "Chip Huyen 在 2025 年 1 月的文章里，把 agent 的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。",
        "body": f"""
<section class="intro">
  <h1>Chip Huyen 的 read-only／write action 分类，核准前为什么要看它</h1>
</section>

<div class="summary"><p><strong>Chip Huyen 在 2025 年 1 月发表的《Agents》，从教科书式的定义出发，一路写到一个更具体的分类：agent 的动作分成“只是看世界”跟“会改变世界”两种。这个分类，正好可以用来判断你手上五分钟该花在计划里的哪几行。</strong></p></div>

<h2>这篇文章主张什么</h2>
<p>Huyen 开门见山：</p>
<blockquote><p>&#8220;An agent is anything that can perceive its environment and act upon that environment.&#8221;</p></blockquote>
<p>（Agent 是任何能感知环境、并对环境采取行动的东西。）</p>
<p>从这里出发，她说明 agent 需要什么：一个可以行动的环境，还有一组决定它能做什么的工具&#8212;&#8212;她称之为“tool inventory”。她点出一个分界：只是让 agent 能感知环境的动作是“read-only actions”，能让它对环境采取行动的动作是“write actions”。对于后者，她讲得很直接：</p>
<blockquote><p>&#8220;Write actions enable a system to do more.&#8221;</p></blockquote>
<p>（Write action 能让系统做到更多事。）</p>
<p>但她也直接点出第二种动作带来的风险：“the prospect of giving AI the ability to automatically alter our lives is frightening”（让 AI 有能力自动改变我们的生活，这个念头令人不安），照她的说法：“you shouldn&#8217;t allow an unreliable AI to initiate bank transfers”（不该让一个不可靠的 AI 去发起银行转账）。她对 agent 最难搞定的那一块也讲得很坦白：</p>
<blockquote><p>&#8220;If you&#8217;ve ever been in any planning meeting, you know that planning is hard.&#8221;</p></blockquote>
<p>（如果你参加过任何一场规划会议，就知道规划有多难。）</p>
<p>Huyen 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》已经引用她这篇文章里三句话：执行前不监督的代价、以为自己做完其实没做完的 agent，还有第三步里她说系统遇到有风险的操作“可以在执行前要求人类明确核准”那一句。这篇不重复这些引文；还没看过那篇的话，下面有连结。</p>

<h2>以下是我们的解读，不是 Huyen 的</h2>
<p>Huyen 的 read-only／write action 分法，不是写给审阅用的建议，而是一种给工具分类的方式。但它是一个很好用的通用判断法，可以用来抓出《五分钟审完一份 agent 计划》第三步已经要你放慢脚步的那种有风险的操作：读一个文件、跑一次搜索、列一下目录，这些是 read-only，做错了顶多重跑一次；删数据、force push、合并分支、发信、扣款，这些是 write action&#8212;&#8212;照她的说法，这种一旦做错就是“令人不安”的那种，而且等你读到 agent 的报告时，它可能已经做完了。她说连人坐在一起开会都觉得规划很难，这也提醒我们别对一份计划的精确度期待过高：计划读起来自信，不代表它是对的。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 没办法帮你判断计划里哪一步是 read-only、哪一步是 write&#8212;&#8212;这是文字没标出来的判断，app 里的任何东西都不会替你读出语义。它里面也没有 AI 模型：不会帮你标出风险高的那一行，不会替你跑“规划到底有多难”的检查，也不会给计划打分数。它做的是让文件在你自己做判断的时候保持好读：侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页让你先看过计划的架构，再逐行读；源代码和排好的页面并排（&#8984;2），步骤图就不会卡在 Mermaid 源代码那个阶段；“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）把你的位置拷贝成 <code>plan.md:10</code>，你一发现顺序不对的 write 动作，马上就能贴出去当反馈。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>用同一篇文章建出来的完整六步骤五分钟检查清单：《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》</li>
  <li>agent 的产出为什么普遍难读：《<a href="/zh-hans/reading-agent-output/">读懂 agent 交回来的 Markdown</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Chip Huyen，《Agents》，2025 年 1 月 7 日：<a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a> （2026-09-26 读取并引用）</li>
</ul>
""",
    }
    pages['reading-notes/lilian-weng-llm-agents'] = {
        "title": "Lilian Weng 2023 年画的 agent 蓝图，每个部件会留下什么文件 · MarsDawn",
        "description": "Lilian Weng 2023 年被广泛引用的整理，把 LLM agent 描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。",
        "body": f"""
<section class="intro">
  <h1>Lilian Weng 2023 年画的 agent 蓝图，每个部件会留下什么文件</h1>
</section>

<div class="summary"><p><strong>2023 年 6 月，当时任职 OpenAI 的 Lilian Weng 在她的博客 Lil'Log 发表了一篇长篇整理，把 LLM-powered agent 描述成一个大脑（模型）加上三个部件：规划、记忆、工具使用。这是一个被广泛引用的早期 agent 架构，而她对这套架构哪里还会出问题，讲得也很坦白。</strong></p></div>

<h2>这篇文章主张什么</h2>
<p>Weng 一开头就定了整篇的架构：</p>
<blockquote><p>&#8220;In a LLM-powered autonomous agent system, LLM functions as the agent&#8217;s brain, complemented by several key components: Planning ... Memory ... Tool use&#8221;.</p></blockquote>
<p>（在一个 LLM-powered 自主 agent 系统里，LLM 扮演 agent 的大脑，再搭配几个关键部件：规划&#8230;&#8230;记忆&#8230;&#8230;工具使用。）</p>
<p>在她的说法里，规划同时包含把任务拆成子目标，以及回头反思过去的行动来改进未来的步骤。记忆分成短期（模型目前看得到的内容，她称为 in-context）和长期（通常存在模型之外、一个可以搜索的数据库里，她称为 vector store）。工具使用则让模型能对外求助，取得模型权重里没有的东西&#8212;&#8212;最新信息、代码执行能力、其他 API。文章接近尾声，在她自己标题为“Challenges”的段落里，她直接点出一个限制：</p>
<blockquote><p>&#8220;LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.&#8221;</p></blockquote>
<p>（LLM 在遇到意外错误时，不太擅长调整计划，这让它们比起会从试错中学习的人类，更缺乏韧性。）</p>
<p>另外，在一个属于“工具使用”案例研究、谈化学 agent“ChemCrow”的段落里，她点出一个较窄的问题：用 LLM 评分的结果认为它和 GPT-4 差不多，但人类专家评估后认为 ChemCrow 在正确性上好得多。她的结论谈的是“自我评估”，不是她的“反思”部件本身：</p>
<blockquote><p>&#8220;The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.&#8221;</p></blockquote>
<p>（缺乏专业知识可能使 LLM 不知道自己的缺陷，因而无法妥善判断任务结果的正确性。）</p>
<p>Weng 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。</p>

<h2>以下是我们的解读，不是 Weng 的</h2>
<p>Weng 描述的是 2023 年的 agent 架构，完全没有谈到“有人在读 agent 的产出”这件事&#8212;&#8212;她根本没提到有人在检查文件。但她自己讲的三个部件，刚好对应到三种你可能会读到的东西。规划通常会留给你一份要在执行前读的文件&#8212;&#8212;计划本身，有时候里面已经先自己做过一轮“反思”或自我检查。记忆通常是看不到的，除非 agent 把长期记忆存成一个持续在写的草稿文件，这种情况下那份文件本身就值得单独打开看，因为它可能悄悄把一个旧的、错的假设，一路带进后面好几个步骤里，却完全没说。工具使用通常会留给你一份“跑了什么、拿到什么结果”的报告&#8212;&#8212;比较像逐字稿，不像计划。</p>
<p>她说计划遇到意外不太会调整，从你的角度来看，这代表你昨天核准的计划，今天可能已经不新鲜了：如果计划没预料到的事在中途发生了，agent 可能还是照原本的计划走下去，而不是重新规划，最后那份报告可能只描述了原本计划“成功了”，却没提到中间绕了路。这是我们的推论，不是她的主张&#8212;&#8212;她讲的是模型本身的韧性，不是读者该注意什么。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 里没有 AI 模型，没办法告诉你一份计划是不是已经悄悄偏离了实际发生的事，也不会替你分辨一份文件是规划文件、记忆文件还是工具使用报告&#8212;&#8212;这是读懂内容之后才能做的判断，要你自己来。它做的是：侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页一眼看出长计划的架构；源代码和排好的预览并排（&#8984;2），Mermaid 和 KaTeX 都直接画出来；agent 读到一半改写文件的话，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未保存的修改&#8212;&#8212;这一点特别有用，因为一份被悄悄改过的计划，正是她“Challenges”那段从模型那一侧描述的失败模式。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>不同 agent 设计模式各自会交给你什么文件：《<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>》</li>
  <li>执行前五分钟审完一份计划的方法：《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Lilian Weng，《LLM Powered Autonomous Agents》，Lil'Log，2023 年 6 月 23 日：<a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a> （2026-09-26 读取并引用；她写这篇时任职于 OpenAI，这里只描述她当时的身份）</li>
</ul>
""",
    }
    pages['reading-notes/harrison-chase-what-is-an-agent'] = {
        "title": "Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看 · MarsDawn",
        "description": "Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。",
        "body": f"""
<section class="intro">
  <h1>Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看</h1>
</section>

<div class="summary"><p><strong>2024 年 6 月，LangChain 的 Harrison Chase 用一个看似简单的问题&#8212;&#8212;“什么是 agent？”&#8212;&#8212;开启了一个新系列，给出一个技术定义，还有一条“agentic”程度的光谱。他主张：系统在这条光谱上愈往自主那端走，就愈需要能在它运作时看得到里面发生了什么。</strong></p></div>

<h2>这篇文章主张什么</h2>
<p>Chase 自己给的定义，还先承认这比大部分人的定义更技术性、涵盖的范围也更广：</p>
<blockquote><p>&#8220;An agent is a system that uses an LLM to decide the control flow of an application.&#8221;</p></blockquote>
<p>（Agent 是用 LLM 来决定应用程序控制流程的系统。“控制流程”指的就是程序接下来要跑哪一步。）</p>
<p>他马上承认这个定义并不完美&#8212;&#8212;一个只是让 LLM 在两条路径之间做选择的简单系统，照他的定义算是 agent，但不太符合大部分人对“agent”的直觉想象。与其去争谁才是“真正的”agent，他采用了 Andrew Ng 的说法&#8212;&#8212;他引用 Ng 的一则推文，并注明出自 Ng：“rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic”（与其去争该把哪些工作算进“真正的”agent、哪些不算，不如承认系统可以有不同程度的 agentic）。Chase 自己的回应是：“I really agree with this viewpoint and I think Andrew expressed it nicely”（我很认同这个看法，觉得 Andrew 讲得很好）。从这里出发：系统愈由 LLM 决定该怎么运作，就愈“agentic”，从固定的路由器，到状态机，一路到能自己建立并记住工具的完全自主 agent。他从这条光谱出发，提出一个实际的主张：系统愈 agentic，某些基础设施就愈重要，其中最重要的是可观测性：</p>
<blockquote><p>&#8220;You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.&#8221;</p></blockquote>
<p>（你会希望能观察系统内部发生了什么，因为它实际采取的步骤事先可能无法得知。）</p>
<p>他还进一步主张不只要看，还要能介入：你也会希望能在某个时间点，修改一个正在运作的 agent 的状态或指示，如果它偏离了原本设定的路径，就把它拉回来。Chase 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。</p>

<h2>以下是我们的解读，不是 Chase 的</h2>
<p>Chase 谈的是给打造 agent 框架的人用的工具&#8212;&#8212;他点名了 LangGraph 和 LangSmith&#8212;&#8212;不是给读一份完成文件的人看的。但他这条光谱，给了一个很实用的方式，让你在开始读之前先估量一下手上这份东西：产出它的系统愈 agentic，你就愈不该预期它的步骤从最初的 prompt 就能猜得到，手上这份文件也就愈值得当成“实际发生了什么”的记录来读，而不是“原本该发生什么”的记录。他说的“观察系统内部”，讲的是一个正在运作的系统的内部状态&#8212;&#8212;trace（一次执行过程中，agent 做过的所有事的记录）、中间步骤、工具调用&#8212;&#8212;不是事后读一份 Markdown 计划。但他给的理由&#8212;&#8212;步骤事先无法得知&#8212;&#8212;用在 agent 做完之后交给你的那份文件上，一样说得通：如果一开始步骤就无法预测，那份做完之后的报告，就是唯一还能检查它们的地方。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 不会去观察一个正在运作的 agent 的内部&#8212;&#8212;它里面没有 AI 模型，也没有连到产生这份文件的任何框架，所以没办法告诉你某个 agent 在 Chase 的光谱上落在哪里。它处理的是事后落到你手上的那份文件：侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页让你看清楚一份长报告的架构；源代码和排好的预览并排（&#8984;2），处理图表和数学式；agent 改写文件时会重新加载，停在你原本读到的位置，前提是你自己没有未保存的修改&#8212;&#8212;这就是“盯着还在动的东西”的文件版本。“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）和“拷贝给 AI”（&#8963;&#8997;&#8984;C）让你精准指出哪一步走偏了，等于是文件版的“把跑偏的 agent 拉回正轨”。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>这个系列对透明和检查点更完整的讨论：《<a href="/zh-hans/agent-transparency/">Anthropic 说 agent 要透明，那摊开的东西谁来读？</a>》</li>
  <li>LangChain 2026 年在这篇文章原本的网址上发表的新文章，定义几乎一模一样：《<a href="/zh-hans/reading-notes/langchain-what-is-an-agent/">Jess Ou 的评测流程，里面还留给你的那一步</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Harrison Chase，《What is an agent?》，LangChain，2024 年 6 月 28 日，存档版本：<a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> （通过 Wayback Machine 于 2026-09-26 读取并引用；原网址现在显示的是 Jess Ou 在 2026 年写的另一篇文章）</li>
</ul>
""",
    }
    pages['reading-notes/langchain-what-is-an-agent'] = {
        "title": "Jess Ou 的评测流程，里面还留给你的那一步 · MarsDawn",
        "description": "LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。",
        "body": f"""
<section class="intro">
  <h1>Jess Ou 的评测流程，里面还留给你的那一步</h1>
</section>

<div class="summary"><p><strong>2026 年 7 月，LangChain 在 Harrison Chase 2024 年那篇《What is an agent?》原本的网址上，发表了一篇新的《What is an AI agent?》&#8212;&#8212;这次是 Jess Ou 写的，定义几乎和他当年那句一字不差。她这篇大部分在谈他那篇没谈到的东西：一整套自动评测 agent 的流程。她的文章很坦白地讲清楚，这套流程哪里还需要人，哪里已经不需要了。</strong></p></div>

<h2>这篇文章主张什么</h2>
<p>Ou 的定义几乎就是 Chase 那句话的回声：</p>
<blockquote><p>&#8220;An AI agent is a system that uses a large language model to decide the control flow of an application.&#8221;</p></blockquote>
<p>（AI agent 是用大型语言模型来决定应用程序控制流程的系统。“控制流程”一样是指接下来要跑哪一步。）</p>
<p>接下来她描述了 LangChain 的 Agent Development Lifecycle：build、test、deploy、monitor 四个阶段，以及一套不靠人读每一次执行记录就能检查 agent 表现的分层做法：online evals 对正式流量的 trace（一次执行的记录）取样，抓退步；offline evals 跑在整理好的数据集上，在变更上线前先抓出问题；“LLM-as-a-judge”则是用一个人事先定好的标准，去替一次执行的输出打分数，而且规模是人工审阅做不到的。她也直接讲清楚人在这套流程里还该站在哪里：</p>
<blockquote><p>&#8220;For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.&#8221;</p></blockquote>
<p>（对于敏感或不可逆的动作，我们建议用 human-in-the-loop 的控制机制，暂停 agent，等待核准、修改、拒绝或澄清。）</p>
<p>她也有一句话讲的是不管流程多完善都省不掉的判断：“Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.”（无法评估的判断，就不要外包出去。如果你自己认不出正确答案，agent 也认不出来。）《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》已经拿这句话建过讨论，这篇不重复。Ou 在这篇文章里完全没有提到 MarsDawn，也没有推荐任何 Markdown 工具。她也从来没提过 Chase 这个人；把这两篇文章连在一起的，是 LangChain 在 2026 年把她这篇发表在 Chase 2024 年那篇文章原本的网址上，而且定义几乎一模一样&#8212;&#8212;这是我们自己的观察，不是她的主张。</p>

<h2>以下是我们的解读，不是 Ou 的</h2>
<p>Ou 讲的 human-in-the-loop，是在特定动作执行前先拦下来&#8212;&#8212;暂停一个 write 动作、等人核准，跟 Chip Huyen 那个 read-only／write action 的分法，其实是同一件事的不同角度&#8212;&#8212;不是读一份已经完成的报告。仔细看她整套流程，大部分设计是要把人从例行检查里拿掉，而不是加进去：online evals、offline evals 和 LLM-as-a-judge，存在的目的就是让团队不用手动看每一次的执行记录。这不是在批评这篇文章&#8212;&#8212;这本来就是她讲明的目标，在正式营运的规模下也很合理。但这代表你亲自动手做的审阅&#8212;&#8212;直接读一份 agent 交给你的计划或报告&#8212;&#8212;正好就是她这套流程想要减少、而不是取代的那种检查。她自己那句判断的话，替这种减少画了一条底线：你自己读了都认不出对错的地方，还是得自己读过。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 不是评测流程，里面也没有 AI 模型&#8212;&#8212;它不会替一次执行记录打分数，不会跑 LLM-as-a-judge，也不会替你决定哪些动作敏感到要先暂停。它做的，正是她这套流程还留给人的那个时刻：直接把东西读过一遍。侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页列出一份长报告的所有标题；源代码和排好的预览并排（&#8984;2），Mermaid 和 KaTeX 都直接画出来；“编辑 &#9656; 拷贝引用”（&#8997;&#8984;C）搭配“拷贝给 AI”（&#8963;&#8997;&#8984;C），让你把一次抽查变成 agent 看得懂、改得动的反馈。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>部分建立在她这句“别外包判断”上的完整检查清单：《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》</li>
  <li>这个定义最早在 2024 年是怎么写的：《<a href="/zh-hans/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase 的 agentic 光谱：愈自主，愈需要盯着看</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Jess Ou，《What is an AI agent?》，LangChain，2026 年 7 月 31 日：<a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a> （2026-09-26 读取并引用）</li>
</ul>
""",
    }
    pages['reading-notes/andrew-ng-design-patterns'] = {
        "title": "Andrew Ng 自己帮四种设计模式的可预测程度排序 · MarsDawn",
        "description": "在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。",
        "body": f"""
<section class="intro">
  <h1>Andrew Ng 自己帮四种设计模式的可预测程度排序</h1>
</section>

<div class="summary"><p><strong>2024 年初，Andrew Ng 在 The Batch 用五篇文章介绍了四种 agentic 设计模式&#8212;&#8212;reflection（反思）、tool use（使用工具）、planning（规划）、multi-agent collaboration（多 agent 协作）&#8212;&#8212;而且很少见地直接告诉读者，这四种里他觉得哪两种比较可靠、哪两种难以预测。</strong></p></div>

<h2>这几篇文章主张什么</h2>
<p>《<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>》已经完整谈过这四种模式各自是什么、当成我们自己的推论各自通常会交给你什么文件，还有 Ng 自己对 planning 的评语，引自 Part 4：“while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications&#8217; performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do”（Reflection 和 Tool Use 这两种设计模式我都能让它们稳定运作、提升应用程序的表现，但 Planning 还是比较不成熟的技术，我很难事先预测它会怎么做）。这篇要补的，是那篇没用到的另外两封信里同一个排序：Part 3，写在 Part 4 之前一周，先讲出了这个排序；Part 5，把排序延伸到 Part 4 没提到的那一种模式&#8212;&#8212;multi-agent collaboration。在介绍 tool use 的 Part 3 里，他写道：</p>
<blockquote><p>&#8220;In future letters, I&#8217;ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable &#8212; albeit very exciting &#8212; technologies.&#8221;</p></blockquote>
<p>（在接下来的信里，我会介绍 Planning 和 Multi-agent collaboration 这两种设计模式。它们能让 AI agent 做到更多事，但也是比较不成熟、比较难预测的技术&#8212;&#8212;虽然非常令人兴奋。）</p>
<p>两周后，他在系列最后一篇谈 multi-agent collaboration 时，从另一个角度确认了同样的排序：</p>
<blockquote><p>&#8220;Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.&#8221;</p></blockquote>
<p>（就像 Planning 这个设计模式一样，我发现 multi-agent collaboration 的输出质量很难预测，尤其是让 agent 之间自由互动、又给它们多种工具的时候。比较成熟的 Reflection 和 Tool Use 模式则可靠得多。）</p>
<p>他讲的是这几种模式对他自己应用程序表现的提升效果，不是在谈应该多仔细审阅它们的产出&#8212;&#8212;这个系列完全没有主张要人工审阅，也没有提到 MarsDawn 或推荐任何 Markdown 工具。</p>

<h2>以下是我们的解读，不是 Ng 的</h2>
<p>Ng 的排序谈的是开发者视角下的输出质量和可预测性，但大致对应到每种模式留下的记录，从你的角度该花多少心力去查。他觉得比较可靠的 reflection 和 tool use，通常会交给你描述“已经做完的事”的东西&#8212;&#8212;一份改过的草稿、一份跑了什么的报告&#8212;&#8212;所以拿里面一个宣称去对照真正的输出，通常就能覆盖大部分风险。他觉得难以预测的 planning 和 multi-agent collaboration，通常会交给你“事情发生之前”写好的东西，或是分散在好几个 agent 手上的好几份文件：一份还在等你点头的计划，或是还没被实际执行验证过的 agent 交接。照他自己的说法，这两种正是“写下来的东西”和“实际会发生的事”落差最大的地方&#8212;&#8212;这也正是《五分钟审完一份 agent 计划》从 Chip Huyen 那篇文章里引出的道理，在“为什么要在执行前审”那一段：在事情跑之前抓到问题，是最便宜的时机。</p>

<h2>MarsDawn 帮得上、帮不上的地方</h2>
<p>MarsDawn 不知道一份文件是 Ng 四种模式里哪一种做出来的，也不会替任何东西按可预测程度排序，里面也没有 AI 模型&#8212;&#8212;他排序背后暗示值得做的那些检查，它不会替你做。它做的是让文件在你自己检查的时候保持好读：侧边栏（“显示 &#9656; 显示边栏”，&#8963;&#8984;S）的“大纲”标签页看得出一份长计划的架构；源代码和排好的预览并排（&#8984;2）；multi-agent 交接的情况下，用“文件 &#9656; 打开文件夹&#8230;”（&#8679;&#8984;O）打开共用的文件夹，不同 agent 写出新文件时，大约一秒内就会出现在“文件”标签页，清单上方也会标出 git 分支或工作树，两份不同 agent 写的同名文件就不会搞混。</p>

<h2>试试看</h2>
<p>MarsDawn 即将在 Mac App Store 上架。免费的 <code>marsdawn</code> 命令行工具现在就能用：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>它不需要 app 就能把 Markdown 导出成 PDF。</p>
<p><a href="/zh-hans/cli/">命令行工具</a> &#183; 买之前先看：<a href="/zh-hans/limits/">MarsDawn 做不到的事</a></p>

<h2>接下来</h2>
<ul>
  <li>每种模式完整会交给你什么文件：《<a href="/zh-hans/agent-design-patterns/">四种 agent 设计模式，各自会交给你什么文件</a>》</li>
  <li>执行前五分钟审完一份计划的方法：《<a href="/zh-hans/reviewing-agent-plans/">五分钟审完一份 agent 计划</a>》</li>
  <li>回到系列索引：《<a href="/zh-hans/reading-notes/">编者的阅读笔记</a>》</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>Andrew Ng，《Agentic Design Patterns Part 1》，The Batch，2024 年 3 月 20 日：<a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng，《Agentic Design Patterns Part 3: Tool Use》，The Batch，2024 年 4 月 3 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/</a> （2026-09-26 读取并引用）</li>
  <li>Andrew Ng，《Agentic Design Patterns Part 4: Planning》，The Batch，2024 年 4 月 10 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a> （引文原封不动沿用自 <code>design/inbox/276-agent-blog-series.md</code>，该引文已用在 <code>/zh-hans/agent-design-patterns/</code>）</li>
  <li>Andrew Ng，《Agentic Design Patterns Part 5, Multi-Agent Collaboration》，The Batch，2024 年 4 月 17 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/</a> （2026-09-26 读取并引用）</li>
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
