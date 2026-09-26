"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': 'プライバシーポリシー', 'support': 'サポート', 'cli': 'コマンドライン', 'agents': 'AI エージェント向け marsdawn', 'using_cli': 'CLI の使い方', 'markdown-to-pdf': 'Markdown から PDF へ', 'skill': 'エージェント用スキル', 'view-markdown-on-mac': 'Mac で Markdown を見る', 'vs-macmd-viewer': 'MacMD Viewer と MarsDawn', 'updated': f"最終更新日：{k.UPDATED}", 'tagline': 'エージェントが書いた Markdown を読む。', 'slogan': 'Markdown の新しい夜明け。', 'footer_store': 'MarsDawn は Mac App Store で近日公開予定です。', 'footer_nav': 'サイト', 'more': 'その他', 'yours': 'あなたの文章は Mac に残ります', 'pay-once': '無料で試して、一度だけ購入', 'pdf': 'PDF 書き出し', 'native': 'Mac アプリ', 'limits': 'MarsDawn ができないこと', 'mcp': 'MCP サーバー', 'token-efficient-review': 'トークンを抑えたレビュー', 'vs-markdown-preview-tools': '他のツールで Markdown を見る場合との比較', 'themes': 'プレビューテーマと PDF 書き出し', 'sharing-exported-pdfs': '書き出した PDF を共有する', 'reviewing-ai-output': 'AI の出力を人が確認する理由', 'reading-agent-output': 'エージェントが返してくるものを読む', 'agent-transparency': 'エージェントの透明性', 'reviewing-agent-plans': 'エージェントの計画をレビューする', 'agent-design-patterns': 'エージェント設計パターン', 'changelog': '更新履歴', 'consent_text': 'このサイトでは、訪問者がどのように利用しているかを把握するために分析用クッキーを使用します。「同意する」を選ばない限り、これらのクッキーは使われません。', 'consent_accept': '同意する', 'consent_decline': '同意しない', 'consent_aria': 'クッキーの同意設定', 'cookie_settings': 'Cookie 設定'}
    store_chip = 'Mac App Store で近日公開'
    schema_notes = {'export': 'export 成功時', 'open': 'open 成功時、marsdawn 0.3.0 以降', 'error': '失敗時、両方のコマンド共通', 'open_v1': 'open 成功時、marsdawn 0.2.x（<code>opened</code> がパスのリストだった頃）'}
    example_plan = '# 計画：エクスポートを高速化\n\nこの計画はエージェントが書きました。内容を確認してから、PDF にします。\n\n## ステップ\n\n| ステップ | 担当 | 状況 |\n|------|-------|--------|\n| 遅いページを計測する | エージェント | 完了 |\n| レンダリング済み図をキャッシュする | エージェント | レビュー中 |\n\n50 ページの文書で目標とするのは $t < 2\\,\\text{s}$：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  ドラフト --> レビュー --> 公開\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'yours': ('あなたの文章は Mac に残ります', 'アカウント不要、同期なし、クラウドなし。'), 'pay-once': ('無料で試して、一度だけ購入', '14日間無料、その後は一度だけ USD 4.99。サブスクリプションはありません。'), 'pdf': ('PDF 書き出し', '図表、コードのハイライト、配慮された改ページ。'), 'native': ('Mac アプリ', 'ネイティブのウインドウとタブ、自動保存、クイックルック。'), 'limits': ('MarsDawn ができないこと', '購入前に知っておくこと。')}
    trait_nav_heading = 'MarsDawn に期待できること'
    figure_list_label = 'このスクリーンショットの内容'
    figures = {
        'index': {
            "alt": 'MarsDawn の分割ビュー：左が Markdown のソース、右がレンダリングされたページ。',
            "callouts": [],
        },
        'yours': {
            "alt": 'MarsDawn がクラシックテーマで文書を表示し、プレビューがウインドウいっぱいに広がっている。',
            "callouts": ['あなたの Mac 上のファイルで、選んだ場所に保存されます。', 'ツールバーにあるのはテーマとレイアウトだけで、サインインするものは何もありません。'],
        },
        'pay-once': {
            "alt": 'MarsDawn がビビッドテーマで、左に Markdown のソース、右にレンダリングされたページを表示している。',
            "callouts": ['エディタの Markdown ハイライトも含まれます。', 'すべてのテーマとレイアウトが含まれます。', 'Mermaid 図も含まれます。', 'コードのハイライトも含まれます。'],
        },
        'pdf': {
            "alt": 'MarsDawn から書き出した PDF を、ページのサムネイル付きの PDF ビューアで開いたところ。',
            "callouts": ['Mermaid 図は PDF に描き込まれます。', 'コードはハイライトを保ちます。'],
        },
        'native': {
            "alt": 'MarsDawn の分割ビュー：左が Markdown のソース、右がレンダリングされたページ。',
            "callouts": ['ネイティブの Mac ウインドウ。', 'Mac のテキストエディタに、Markdown ハイライトを追加したもの。', '⌘1 でソース、⌘2 で分割、⌘3 でプレビュー。', '入力するとページが更新されます。'],
        },
        'limits': {
            "alt": 'MarsDawn のダークモード、左が Markdown のソース、右がレンダリングされたページ。',
            "callouts": ['この Mac で、ウインドウひとつにつき文書ひとつ。', 'ここで Markdown を書きます。', 'ツールバーにあるのはテーマとレイアウトだけで、プラグインメニューはありません。', 'このページは読むためのもので、編集はできません。'],
        },
    }
    pages = {}
    pages['support'] = {
        "title": 'サポート · MarsDawn',
        "description": 'macOS 向け Markdown エディタ MarsDawn のヘルプ。',
        "body": f"""
<section class="intro">
  <h1>サポート</h1>
  <p>macOS 向け Markdown エディタ、MarsDawn のヘルプです。</p>
</section>

<section class="contact">
  <h2>お問い合わせ</h2>
  <a class="email" href="mailto:{k.EMAIL}?subject=MarsDawn%20support">{k.EMAIL}</a>
  <p>macOS のバージョンと MarsDawn のバージョン（MarsDawn › MarsDawnについて）を書き添えてください。何かおかしく見える場合は、スクリーンショットや小さなサンプル文書がとても役立ちます。</p>
</section>

<section class="faq">
  <h2>よくある質問</h2>

  <h3>MarsDawn を動かすには何が必要ですか？</h3>
  <p>macOS 26 Tahoe 以降を搭載した Mac。Apple シリコンでも Intel でも動作します。</p>

  <h3>エディタとプレビューはどう切り替えますか？</h3>
  <p><kbd>⌘1</kbd> でソースのみ、<kbd>⌘2</kbd> で左右分割、<kbd>⌘3</kbd> でプレビューのみになります。同じ選択肢は「表示」メニューとツールバーにもあります。</p>

  <h3>文書内の画像が表示されません。</h3>
  <ul>
    <li><strong>Mac 上の画像：</strong>まず文書を保存し、プレビューの<em>フォルダへのアクセスを許可…</em>をクリックして、画像があるフォルダを選んでください。MarsDawn はそのフォルダを記憶します。許可したフォルダは MarsDawn › 設定 › フォルダへのアクセスで確認できます。</li>
    <li><strong>ウェブ上の画像：</strong>ウェブ画像は、プレビュー上部の<em>イメージを読み込む</em>をクリックするまでブロックされます。常に読み込みたい場合は、設定で<em>リモートイメージを自動的に読み込む</em>をオンにしてください。</li>
  </ul>

  <h3>画像を追加するには？</h3>
  <p>エディタにドラッグするか、貼り付けてください。文書は先に保存しておく必要があります。MarsDawn が画像を文書の隣にある <code>assets</code> フォルダにコピーし、Markdown のリンクを書き込みます。</p>

  <h3>Mermaid 図にエラーが表示されます。</h3>
  <p>MarsDawn は図のソースと、その下に Mermaid のエラーメッセージの最初の行を表示します。示された行を確認してください。たとえば矢印の先に何もない、または括弧が閉じられていない、といった箇所です。</p>

  <h3>PDF を作るには？</h3>
  <p>ファイル › PDF として書き出す…（<kbd>⌥⌘E</kbd>）を選んでください。PDF はどのレイアウトであっても、プレビューテーマのライト版を使い、ページごとに分割されます。ファイル › プリント…でも同じページが印刷されます。</p>

  <h3>Siri やショートカットで MarsDawn を使うには？</h3>
  <p>ショートカット App を開いて MarsDawn を検索すると、<em>新規 Markdown 書類</em>、<em>受信トレイにメモを追加</em>、<em>最近使った書類を開く</em>が見つかります。メモを追加する前に、MarsDawn › 設定 › メモフォルダでメモフォルダを選んでください。メモはそのフォルダの <code>Inbox.md</code> に追加されます。</p>

  <h3>設定はどこにありますか？</h3>
  <p>MarsDawn › 設定（<kbd>⌘,</kbd>）に、外観モード、イメージ、メモフォルダ、フォルダへのアクセス、プレビューのテーマがあります。</p>

  <h3>返金してもらうには？</h3>
  <p>購入は Apple が処理します。<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> で返金を申請してください。</p>
</section>
""",
    }
    pages['privacy'] = {
        "title": 'プライバシーポリシー · MarsDawn',
        "description": 'MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。',
        "body": k.render_legal_body("privacy", "ja"),
    }
    pages['index'] = {
        "title": 'MarsDawn：ライブプレビュー搭載、Mac 向け Markdown エディタ',
        "description": 'エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で近日公開予定です。',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">ビルダーのためのフロンティアツール</p>
  <h1><span>地図を手に。</span><span>夜明けを読む。</span></h1>
  <p>エージェント開発の舵を取る人のための Markdown。</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">エージェントが書いた Markdown を読む。</h2>
<ol class="loop-steps">
  <li><strong>エージェントが書く。</strong>あなたのコーディングエージェントやライティングアシスタントが Markdown の下書きを作ります。README、仕様書、メモなど。</li>
  <li><strong>MarsDawn で確認する。</strong>ファイルを開き、Mermaid 図やハイライトされたコードとともにレンダリングされたページを、ソースの隣で読みます。</li>
  <li><strong>エージェントが修正する。</strong>変更を依頼します。修正されたファイルを開き、同じように読みます。</li>
</ol>
<p><a href="/ja/reading-agent-output/">エージェントが返してくるものをどう確認するか</a>。</p>
""",
    }
    pages['yours'] = {
        "title": 'アカウントもクラウドも不要な Mac 向け Markdown エディタ · MarsDawn',
        "description": 'MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。',
        "intro": f"""
<section class="intro">
  <h1>あなたの文章は、あなたの Mac に残ります。</h1>
  <p>MarsDawn にはアカウントも同期もクラウドもありません。ファイルを開いて、あなたが書き、選んだ場所に保存します。</p>
</section>
""",
        "body": f"""
<h2>それが意味すること</h2>
<ul>
  <li>登録もサインインも必要なアカウントはありません。</li>
  <li>何もクラウドに同期されません。文書は保存した場所にそのまま残ります。</li>
  <li>何も追跡されません。MarsDawn はあなたに関するデータを一切収集せず、App Store のプライバシーラベルは「データの収集なし」です。</li>
  <li>ウェブ画像は読み込むまでブロックされたままなので、文書を開いただけでサーバーに読んだことが伝わることはありません。読み込む場合も https でのみ読み込まれます。</li>
  <li>ローカル画像は、フォルダへのアクセスを許可するとプレビューに表示されます。</li>
</ul>
<p>詳細は<a href="/ja/privacy/">プライバシーポリシー</a>をご覧ください。</p>
""",
    }
    pages['pay-once'] = {
        "title": '無料で試して、一度だけ購入 · MarsDawn',
        "description": 'MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。',
        "intro": f"""
<section class="intro">
  <h1>すべて試してから、一度だけ支払う。</h1>
  <p>MarsDawn は無料でダウンロードできます。14日間のトライアルを始めればすべての機能が使えます。その後も使い続けるには、USD 4.99 の一度きりの購入でロックが解除されます。サブスクリプションもアカウントもありません。</p>
</section>
""",
        "body": f"""
<h2>仕組み</h2>
<ol class="loop-steps">
  <li><strong>無料でダウンロード。</strong> MarsDawn は Mac App Store から無料でダウンロードできます。</li>
  <li><strong>14 日間、すべて使える。</strong> トライアルを始めると、14日間はすべての機能が使えます。すべてのテーマとレイアウト、PDF 書き出しと印刷、クイックルック、Siri とショートカットのアクションです。</li>
  <li><strong>一度の購入で解除。</strong> その後も使い続けるには、USD 4.99 の一度きりの購入でロックを解除します。App 内課金であり、サブスクリプションではないので、自動更新もあとから請求されることもありません。</li>
</ol>
<ul>
  <li>トライアル自体も課金されません。終了時、あなたがロック解除を選ばない限り何も購入されません。</li>
  <li>アカウントはありません。MarsDawn がアカウント作成を求めることは決してありません。</li>
</ul>
<h2>ロックを解除しない場合</h2>
<ul>
  <li>14日後、ロックを解除するまでは、MarsDawn で文書を読んだり編集したり書き出したり印刷したりできません。文書自体は開きますが、内容は覆われます。</li>
  <li>あなたのファイルは変わりません。Mac 上の普通のファイルのままで、Finder のクイックルックでも引き続き表示されます。</li>
  <li>無料の<a href="/ja/cli/"><code>marsdawn</code> コマンドラインツール</a>は、トライアルの有無にかかわらず、引き続き PDF に書き出せます。</li>
  <li>トライアル終了時に MarsDawn で文書が開いていた場合、入力した文字が失われることはありません。「ファイル」▸「別名で保存…」で保存してください。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Mac で Markdown を PDF に書き出す、図も含めて · MarsDawn',
        "description": 'Mac で Markdown を PDF に書き出したり印刷したりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。',
        "intro": f"""
<section class="intro">
  <h1>PDF は、あなたが書いたページそのままに見えます。</h1>
  <p>テーマのライトカラーで PDF に書き出す、または印刷できます。図やハイライトされたコードもそのまま反映され、改ページはひとまとまりの内容を分断しないよう配慮されます。</p>
</section>
""",
        "body": f"""
<h2>それが意味すること</h2>
<ul>
  <li>Mermaid 図は PDF に描き込まれます。</li>
  <li>コードブロックはシンタックスハイライトを保ちます。</li>
  <li>改ページは、見出しがページの下端に残ったり、コード・表・図が分断されたりしないよう配慮されます。</li>
  <li>どのレイアウトでも書き出せます。ソースだけを表示していても書き出しは機能します。</li>
</ul>
<p>無料の<a href="/ja/cli/">marsdawn コマンドラインツール</a>は同じ書き出しエンジンを使っているので、スクリプトや AI エージェントも同じ PDF を得られます。</p>
""",
    }
    pages['native'] = {
        "title": 'Mac 向けネイティブ Markdown アプリ：タブ、クイックルック · MarsDawn',
        "description": '本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。',
        "intro": f"""
<section class="intro">
  <h1>Mac 自身のパーツで作られています。</h1>
  <p>ウインドウ、タブ、メニュー、テキストエディタはすべて Mac 自身のものです。レンダリングされたページは、Safari を動かしているエンジンである WebKit が描画します。</p>
</section>
""",
        "body": f"""
<h2>それが意味すること</h2>
<h3>編集</h3>
<ul>
  <li>ソース、分割、プレビューの3つのレイアウトを、キー1つで切り替え（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>2つのペインは一緒にスクロールするので、編集中の段落が常に見えています。</li>
  <li>エディタの Markdown シンタックスハイライトは、プレビューのテーマに合わせられます。</li>
</ul>
<h3>Mac のほかの部分と</h3>
<ul>
  <li>ネイティブなウインドウ、タブ、自動保存、バージョン履歴。</li>
  <li>クイックルック：Finder で Markdown ファイルを選んでスペースキーを押すとプレビューでき、図も表示されます。</li>
  <li>Siri とショートカット：テンプレートから新しい文書を作成する、メモの受信トレイに1行追加する、最近使った文書を再度開く、といった操作ができます。</li>
  <li>{k.APP_UI_LANGUAGES}に対応。</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": "MarsDawn ができないこと · MarsDawn",
        "description": '同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。',
        "intro": f"""
<section class="intro">
  <h1>MarsDawn ができないこと。</h1>
  <p>いくつかの機能は意図的に省かれています。必要な機能があれば、購入したあとより今知っておくほうがいいはずです。</p>
</section>
""",
        "body": f"""
<h2>省かれているもの</h2>
<h3>デバイスと使う人</h3>
<ul>
  <li><strong>同期：</strong>MarsDawn は文書を同期しません。文書は保存した場所にそのまま残るので、別の Mac でも使いたい場合は、すでに同期しているフォルダに保存してください。</li>
  <li><strong>iPhone と iPad：</strong>これらの端末向けアプリはありません。MarsDawn は Mac 専用です。</li>
  <li><strong>共有：</strong>アカウントも共同編集もありません。MarsDawn は自分の Mac で使う一人のためのものです。</li>
  <li><strong>システム：</strong>MarsDawn には macOS 26 以降が必要です。</li>
</ul>
<h3>ファイルと機能</h3>
<ul>
  <li><strong>編集：</strong>左に Markdown を書き、右でページを読みます。ページ自体は編集できません。</li>
  <li><strong>形式：</strong>MarsDawn は PDF の書き出しと印刷に対応していますが、Word ファイルへの書き出しはできません。</li>
  <li><strong>その他のファイル：</strong>プレーンテキストファイルと PDF は読み取り専用で開きます。</li>
  <li><strong>テーマ：</strong>夜明け、クラシック、モダン、ビビッド の4種類が組み込まれており、それぞれライトとダークがあります。他のテーマを追加することはできません。</li>
  <li><strong>プラグイン：</strong>MarsDawn にプラグインや拡張機能はありません。</li>
</ul>
<h2>試用期間が終わったら</h2>
<p>14日間のトライアルが終わってロックを解除しなければ、MarsDawn で文書を読んだり編集したりできません。内容が覆われた状態で開きます。ファイルはそのまま残り、クイックルックでは引き続き表示され、無料のコマンドラインツールも引き続き書き出せます。</p>
""",
    }
    pages['view-markdown-on-mac'] = {
        "title": 'Mac で Markdown ファイルを見る方法 · MarsDawn',
        "description": '.md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で近日公開予定の MarsDawn アプリで読む方法です。',
        "body": f"""
<section class="intro">
  <h1>Mac で Markdown ファイルを見る方法。</h1>
  <p><code>.md</code> ファイルはプレーンテキストです。見出し、太字、表、図は記号で書かれています。見出しには <code>#</code>、太字は <code>**</code> で囲む、表はパイプで区切る、図は <code>mermaid</code> コードブロックといった具合です。プレーンテキストエディタで開くと、これらの記号がそのまま見えます。作者の意図どおりにページを読むには、何かがそれをレンダリングする必要があります。</p>
</section>
<h2>今すぐ無料で：PDF に変換する</h2>
<p>無料の <code>marsdawn</code> コマンドラインツールは、Markdown ファイルをどの Mac でも開ける PDF にレンダリングします。表、数式、Mermaid 図、ハイライトされたコードはすべてレンダリングされ、MarsDawn アプリすら含め、他に何もインストールする必要はありません。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> は Markdown ファイルの隣に <code>notes.pdf</code> を書き出し、<code>open</code> はそれをあなたの PDF ビューアで表示します。macOS 15 以降が必要です。実際に書き出したページを使った解説は、<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>にあります。</p>
<h2>近日公開：MarsDawn で読む</h2>
<p>MarsDawn は Mac 向けの Markdown エディタで、Mac App Store で近日公開予定です。<code>.md</code> ファイルを開くと、ソースの隣でレンダリングされたページを読めます。</p>
<ul>
  <li>入力すると同時にプレビューが更新され、2つのペインは一緒にスクロールします。</li>
  <li>Mermaid のフローチャートとシーケンス図がプレビューに描画され、コードブロックはハイライトされます。</li>
  <li>Finder で Markdown ファイルを選んでスペースキーを押せば、図も含めてクイックルックでプレビューできます。</li>
  <li>何かを変更したいときは、ソースがすぐそこにあります。MarsDawn はビューアだけでなくエディタでもあります。</li>
</ul>
<p>もしそのファイルを AI エージェントが書いたなら、これはまさに MarsDawn が想定しているループです。エージェントが書き、あなたがレンダリングされたページを読み、エージェントが修正します。<a href="/ja/">ホームページ</a>と、エージェントにファイルを開かせる方法については<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>をご覧ください。その読み方がなぜ重要か、計画をどうレビューするかは、<a href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a>と<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>にあります。</p>
<h2>次に</h2>
<ul>
  <li>コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>MarsDawn ができないこと：<a href="/ja/limits/">一覧はこちら</a>。</li>
</ul>
""",
    }
    _plan_en = '# Plan: faster exports\n\nAn agent wrote this plan. You review it, then turn it into a PDF.\n\n## Steps\n\n| Step | Owner | Status |\n|------|-------|--------|\n| Measure the slow pages | Agent | Done |\n| Cache rendered diagrams | Agent | In review |\n\nThe target is $t < 2\\,\\text{s}$ for a 50-page document:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Draft --> Review --> Ship\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    pages['markdown-to-pdf'] = {
        "title": 'Mac のコマンドラインで Markdown を PDF に · MarsDawn',
        "description": '無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。',
        "body": f"""
<section class="intro">
  <h1>Mac のコマンドラインで、Markdown を PDF に。</h1>
  <p>無料の <code>marsdawn</code> ツールは、コマンド1つで Markdown ファイルを PDF に変換します。表、数式、Mermaid 図、ハイライトされたコードはソースの見た目そのままに仕上がり、MarsDawn アプリすら含め、他に何もインストールする必要はありません。</p>
</section>
<h2>インストール</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Apple シリコンの Mac では、Homebrew がビルド済みのコピーを数秒でインストールします。Intel Mac ではソースからビルドするため数分かかり、Xcode 26 以降が必要です。macOS 15 以降で動作し、<code>marsdawn --version</code> がインストールされたバージョンを表示します。</p>
<h2>文書を保存する</h2>
<p><code>plan.md</code> という名前のファイルに、次の内容を貼り付けてください。</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>書き出す</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>ソースの隣に <code>plan.pdf</code> を書き出し、保存先を表示します。</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>これはそのページを、<code>marsdawn</code> 0.5.0 の実行結果から実際にキャプチャしたものです。</p>
<p><img class="pdf-page" src="/assets/cli/plan-ja.png" alt="書き出された PDF：見出し、ステップの表、インラインと独立した数式、ドラフト・レビュー・公開の図、ハイライトされた Swift のコード1行。" width="989" height="930"></p>
<h2>テーマ、用紙サイズ、ファイル名を選ぶ</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>：dawn、classic、modern、vivid のいずれかで、テーマのライトカラーを使います。指定しない場合、<code>export</code> は <code>$MARSDAWN_THEME</code>、それもなければ dawn を使います。</li>
  <li><code>--paper</code>：a4 または letter。デフォルトは a4 です。</li>
  <li><code>-o</code>：PDF をソースの隣ではなく、どこに書き出すか。</li>
  <li><code>--allow-remote-images</code>：レンダリング時にウェブから画像を読み込みます。指定しない限りオフのままです。</li>
</ul>
<h2>うまくいかない場合</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew が <code>marsdawn</code> をソースからビルドしています。Intel Mac ではこのようになります。App Store から Xcode 26 以降をインストールしてから、もう一度インストールしてください。</li>
  <li><code>marsdawn: No such file: …</code> パスがファイルを指していません。ファイル名を確認するか、そのファイルがあるフォルダでコマンドを実行してください。</li>
  <li><code>… already exists. Pass --force to replace it.</code> 同じ名前の PDF がすでに存在します。<code>--force</code> を付けて置き換えるか、<code>-o</code> で別の場所に書き出してください。</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> テーマまたは用紙サイズが認識されていません。テーマは dawn、classic、modern、vivid、用紙は a4 または letter です。</li>
</ul>
<h2>次に</h2>
<ul>
  <li>すべてのオプションと出力される JSON：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>コーディングエージェントにこれをやらせるには：<a href="/ja/cli/skill/">marsdawn のエージェントスキル</a>。</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer 対 MarsDawn：ビューアかエディタか · MarsDawn',
        "description": 'MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer 対 MarsDawn。</h1>
  <p>どちらも Markdown をレンダリングして読むための Mac アプリです。MacMD Viewer は <code>.md</code> ファイルを開いて完成したページを表示しますが、編集はできません。MarsDawn は同じようにレンダリングされたプレビューの隣にエディタを置き、1つのウインドウで書きながら確認できます。ここでは機能ごとに両者の違いを見ていきます。</p>
</section>
<h2>読むだけでよく、編集の必要がない場合</h2>
<p>他の人が書いた Markdown を読むことだけが仕事で、ソースに触れる必要が一切ないなら、MacMD Viewer は妥当な選択です。まさにそのために作られており、今すぐ入手でき、より古い macOS でも動作します。読むことだけが仕事ではなくなったときに MarsDawn が価値を持ちます。エージェントの Markdown はたいてい、もう一度手直しが入るからです。</p>
<h2>それぞれのアプリでできること</h2>
<!--compare:macmd-features-->
<h2>価格と購入方法</h2>
<!--compare:macmd-buying-->
<h2>今すぐ無料で試す</h2>
<p>MarsDawn は Mac App Store で近日公開予定で、まだ販売されていません。それまでは、無料の <code>marsdawn</code> コマンドラインツールが、今すぐどんな Markdown ファイルも Mermaid 図とハイライトされたコード付きの PDF にレンダリングでき、他に何もインストールする必要はありません。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>次に</h2>
<ul>
  <li>完全な解説：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。</li>
  <li>MarsDawn ができないこと：<a href="/ja/limits/">一覧はこちら</a>。</li>
  <li>コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn：無料の Markdown から PDF へのコマンドラインツール · MarsDawn',
        "description": '無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。',
        "body": f"""
<section class="intro">
  <h1>コマンドライン</h1>
  <p>無料の <code>marsdawn</code> コマンドラインツール：シェルや LLM エージェントから Markdown を PDF に書き出せます。MarsDawn アプリがインストールされていれば、そのアプリでファイルを開くこともできます。</p>
</section>

<div class="summary"><p><strong>marsdawn は無料で、Mac App Store とは別に配布されています。</strong>Homebrew でインストールすると、Apple シリコンの Mac では、すぐに実行できる状態でインストールされます。<code>export</code> は単独で動作し、<code>open</code> には MarsDawn アプリが必要です。</p></div>

<p>AI エージェントやスクリプトから marsdawn を呼び出しますか？JSON 出力とそのスキーマ、すべての終了コードについては<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>をご覧ください。</p>

<h2>インストール</h2>
<p><a href="https://brew.sh">Homebrew</a> を使う場合：</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>Apple シリコンの Mac では、Homebrew がビルド済みのコピーを数秒でインストールし、他に何もインストールする必要はありません。Intel Mac では代わりにソースから marsdawn をビルドするため数分かかり、Xcode 26 以降（Swift 6.2）が必要です。このツールは macOS 15 以降で動作します。</p>
<p>または、Swift Package Manager で<a href="{k.KIT_URL}">ソース</a>からビルドします。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>インストールされているバージョンは <code>marsdawn --version</code> で確認できます。</p>

<h2>コマンド</h2>

<h3>marsdawn open</h3>
<p>1つ以上の Markdown ファイルを MarsDawn アプリで開いて確認できます。アプリのインストールが必要です。インストールされていない場合、<code>marsdawn open</code> はコード 3 で終了し、MarsDawn がインストールされていないことを知らせます。<code>export</code> にはアプリは不要です。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>：MarsDawn にその行に移動するよう指定します。その後にコロンが続く場合、たとえば <code>notes.md:120:8</code> の列部分は無視されます。引数全体と一致するファイル名が存在する場合、その引数はそのファイルとして扱われます。</li>
  <li><code>--line &lt;n&gt;</code>：単一ファイルに対して同じ指定ができ、それ自体がコロンと数字で終わるパスに対して行を指定する方法でもあります。ファイルは1つだけ指定できます。</li>
  <li>行番号は 1 から 999999999 までです。</li>
  <li>MarsDawn 1.0 はその行にジャンプしてファイルを開きます。</li>
  <li><code>--json</code>：テキストではなく JSON の結果を出力します。</li>
</ul>
<p>行の指定は marsdawn 0.3.0 で追加されました。</p>

<h3>marsdawn export</h3>
<p>Markdown ファイルを、MarsDawn 自身の PDF 書き出しと同じ書き出しエンジンで、ページ分割された PDF にレンダリングします。MarsDawn アプリは不要です。相対パスの画像は、入力ファイルのあるフォルダを基準に解決されます。</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF の書き出し先。デフォルトは入力パスの拡張子を <code>.pdf</code> にしたものです。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：プレビューテーマのライトパレット。デフォルトは <code>$MARSDAWN_THEME</code>、それもなければ <code>dawn</code> です。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：用紙サイズ。デフォルトは <code>a4</code> です。</li>
  <li><code>--allow-remote-images</code>：レンダリング時にウェブから画像を読み込みます。デフォルトはオフです。</li>
  <li><code>--force</code>：出力ファイルがすでに存在する場合に置き換えます。</li>
  <li><code>--json</code>：テキストではなく JSON の結果を出力します。</li>
</ul>

<h2>$MARSDAWN_THEME 環境変数</h2>
<p><code>--theme</code> が指定されない場合、<code>export</code> は <code>$MARSDAWN_THEME</code> 環境変数を読み取ります。値は <code>dawn</code>、<code>classic</code>、<code>modern</code>、<code>vivid</code> のいずれかである必要があり、それ以外は <code>dawn</code> にフォールバックします。CLI はアプリ自身のテーマ設定を読み取りません。他のアプリのコンテナを読み取ると、macOS のプライバシープロンプトが表示されることがあるためです。</p>

<h2>ファイルの上書き</h2>
<p><code>export</code> は、<code>--force</code> を指定しない限り、既存の出力ファイルを置き換えません。</p>

<h2>終了コード</h2>
<!--exit-table-->
<ul>
  <li><code>0</code>：成功。</li>
  <li><code>2</code>：入力が見つからない。</li>
  <li><code>3</code>：MarsDawn がインストールされていない（<code>open</code> のみ）。</li>
  <li><code>4</code>：出力先がすでに存在する（<code>--force</code> を指定してください）。</li>
  <li><code>5</code>：書き出しに失敗。</li>
  <li><code>64</code>：使用方法のエラー。範囲外の行や、複数ファイルに対する <code>--line</code> の指定などを含みます。</li>
</ul>

<h2>--json 出力</h2>
<p>成功時、<code>marsdawn open --json</code> は <code>ok</code>、<code>opened</code>（各ファイルの <code>path</code>、行が指定されていれば <code>line</code> も含む）、<code>app</code>（アプリのパス）を出力します。<code>marsdawn export --json</code> は <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code>、<code>diagramErrors</code> を出力します。失敗時はどちらも <code>ok</code>、<code>error</code>、<code>message</code> を出力します。</p>
""",
    }
    pages['cli/agents'] = {
        "title": 'AI エージェント向け marsdawn：スクリプトから Markdown を PDF に · MarsDawn',
        "description": 'marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。',
        "body": f"""
<section class="intro">
  <h1>AI エージェント向け marsdawn</h1>
  <p><code>marsdawn</code> コマンドラインツールを呼び出す AI エージェントとスクリプトのためのリファレンスです。このページのすべての例は、現在のソースからビルドしたツールに対して実際に実行したものです。</p>
</section>

<div class="summary"><p><strong>Markdown ファイルを PDF に変換するには、<code>marsdawn export notes.md --json</code> を実行し、stdout から1つの JSON オブジェクトを読み取ってください。</strong>Mermaid 図とハイライトされたコードは、MarsDawn アプリと同じ方法でレンダリングされます。<code>export</code> にアプリは不要ですが、<code>open</code> には必要です。</p></div>

<h2>できること</h2>
<ul>
  <li><code>export</code>：MarsDawn アプリと同じ書き出しエンジンで、1つの Markdown ファイルをページ分割された PDF にレンダリングします。ウインドウは開きません。</li>
  <li><code>open</code>：1つ以上の Markdown ファイルを MarsDawn アプリで開き、人が確認できるようにします。各ファイルが移動すべき行を指定することもできます。</li>
</ul>

<h2>できないこと</h2>
<ul>
  <li>stdin から Markdown を読み込みません。ファイルパスを渡してください。</li>
  <li>PDF を stdout に書き出しません。PDF は常にファイルとして書き出され、stdout には結果だけが出力されます。</li>
  <li><code>--force</code> を指定しない限り、既存のファイルを置き換えません。</li>
  <li><code>--allow-remote-images</code> を指定しない限りウェブから画像を読み込まず、指定した場合も https のみです。</li>
  <li><code>open</code> は MarsDawn アプリがインストールされていないと動作せず、コード 3 で終了します。<code>export</code> にアプリは不要です。</li>
  <li>MarsDawn 1.0 は <code>open</code> が指定した行にジャンプします。</li>
  <li>macOS でのみ動作します。</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p><code>notes.pdf</code> を <code>notes.md</code> の隣に書き出します。オプション：</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF の書き出し先。デフォルトは入力パスの拡張子を <code>.pdf</code> にしたものです。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：テーマのライトパレット。デフォルトは <code>$MARSDAWN_THEME</code>、それもなければ <code>dawn</code> です。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：用紙サイズ。デフォルトは <code>a4</code> です。</li>
  <li><code>--allow-remote-images</code>：レンダリング時にウェブから https の画像を読み込みます。</li>
  <li><code>--force</code>：出力ファイルが存在する場合に置き換えます。</li>
  <li><code>--json</code>：stdout にテキストではなく1つの JSON オブジェクトを出力します。</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>成功、終了コード 0：</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>：書き出された PDF の絶対パス。</li>
  <li><code>pages</code>：ページ数。</li>
  <li><code>theme</code> と <code>paper</code>：実際に使われた値。</li>
  <li><code>diagramErrors</code>：レンダリングに失敗した Mermaid 図につき1件のメッセージ。PDF はそれでも書き出されます。</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> は移動先の行を指定します。その後にコロンが続く場合、たとえば <code>notes.md:120:8</code> の列部分は無視されます。存在するファイル名を丸ごと表す引数は常にそのファイル名として扱われるため、<code>weird:12</code> という名前のファイルはそのまま開きます。</li>
  <li><code>--line &lt;n&gt;</code> は単一ファイルの行を指定します。それ自体がコロンと数字で終わるパスも含みます。ファイルは1つだけ指定できます。</li>
  <li>行番号は 1 から 999999999 までで、それ以外は使用方法のエラーになります。</li>
  <li>行の指定は marsdawn 0.3.0 で追加されました。MarsDawn 1.0 はその行にジャンプしてファイルを開きます。</li>
</ul>
<p>成功、終了コード 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：渡された順に、ファイルごとの1つのオブジェクト。<code>path</code> はファイルの絶対パス、<code>line</code> は行が指定されたときだけ現れます。</li>
  <li><code>app</code>：それらを開いた MarsDawn アプリのパス。</li>
</ul>
<p>marsdawn 0.2.x では <code>opened</code> はパス文字列のリストでした。両方を扱う必要がある場合は <code>marsdawn --version</code> を確認してください。</p>

<h2>失敗時</h2>
<p><code>--json</code> を指定すると、失敗時は stdout に1つの JSON オブジェクトを出力し、対応するコードで終了します。</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>、<code>input_not_found</code>：入力が存在しない、フォルダである、または UTF-8 テキストでない。</li>
  <li><code>3</code>、<code>app_not_installed</code>：MarsDawn がインストールされていない。<code>open</code> のみがこれを返します。</li>
  <li><code>4</code>、<code>output_exists</code>：出力ファイルが存在する。<code>--force</code> を指定してください。</li>
  <li><code>5</code>、<code>export_failed</code>：書き出し自体が失敗した。</li>
  <li><code>64</code>：使用方法のエラー。未知のオプション、無効な値、範囲外の行、複数ファイルに対する <code>--line</code> の指定など。この場合は、<code>--json</code> を指定していても stderr にテキストとして出力されます。</li>
</ul>

<h2>JSON Schema</h2>
<p>各 <code>--json</code> 結果に対応する JSON Schema（draft 2020-12）：</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>環境変数</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>：<code>export</code> が、<code>--theme</code> が指定されないときに使うテーマ。未知の値はエラーにならず <code>dawn</code> にフォールバックします。</li>
</ul>

<h2>必要環境</h2>
<ul>
  <li>このツールは macOS 15 以降で動作します。Apple シリコンでは、Homebrew がビルド済みのボトルをインストールし、他に何も必要ありません。Intel Mac やソースから自分でビルドする場合は、Swift 6.2 以降が必要で、これは Xcode 26 以降に付属しています。</li>
  <li>MarsDawn アプリには macOS 26 以降が必要です。</li>
</ul>

<h2>インストール</h2>
<p>Homebrew を使う場合。Apple シリコンでは、Xcode 不要でビルド済みのボトルを数秒でインストールします。Intel Mac では marsdawn をソースからコンパイルするため数分かかり、Xcode 26 以降が必要です。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>または、<a href="{k.KIT_URL}">ソース</a>からビルドします。最初のビルドでは依存関係の取得とコンパイルが行われ、これも数分かかります。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> は <code>0.3.0</code> のようなバージョン番号を表示し、コード 0 で終了します。</p>
""",
    }
    pages['cli/skill'] = {
        "title": 'Markdown から PDF へのコーディングエージェント用スキル · MarsDawn',
        "description": 'コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。',
        "body": f"""
<section class="intro">
  <h1>PDF 作成をエージェントに任せる。</h1>
  <p>このスキルは1つの Markdown ファイルです。コーディングエージェントに <code>marsdawn</code> のインストール方法、動作確認の方法、文書を PDF に書き出す方法、結果の読み方を教えます。これにより、Markdown を書いたエージェントが PDF もあなたに渡せるようになります。</p>
</section>
<div class="summary"><p><strong>1つの Markdown ファイルを <code>~/.claude/skills/marsdawn/SKILL.md</code> に置くだけ。</strong>これでエージェントが <code>marsdawn</code> をインストールし、PDF に書き出し、JSON の結果を読みます。何かを実行する前には、これまでどおり確認を求めます。</p></div>
<h2>Claude Code にインストールする</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code は PDF が必要なタスクのときにこれを自動的に読み込み、<code>/marsdawn</code> として自分で実行することもできます。<a href="/cli/skill/SKILL.md">短いファイル1つ</a>なので、インストールする前に読んでみてください。</p>
<p>他のエージェントでも同じファイルを使えます。ただの Markdown で、説明とコマンドが書いてあるだけなので、あなたのエージェントにこの URL を指定するか、そのまま貼り付けてください。このファイルは英語です。</p>
<h2>教えること</h2>
<ul>
  <li><code>marsdawn</code> がなければ Homebrew でインストールし、バージョンを決め打ちせず <code>marsdawn --version</code> で確認する。</li>
  <li><code>marsdawn export … --json</code> で書き出し、結果を読み取る：PDF の書き出し先、ページ数、レンダリングされなかった Mermaid 図の有無。</li>
  <li>終了コードで失敗の種類を見分ける：ファイルが見つからない、PDF がすでにある、書き出しに失敗した、オプションが不正、など。</li>
  <li>MarsDawn アプリがインストールされているときだけ <code>open</code> を使い、PDF を作るためには絶対に使わない。</li>
</ul>
<h2>しないこと</h2>
<ul>
  <li>何かを実行する権限を自分自身に与えることはありません。あなたのエージェントは、他のコマンドと同じように、<code>marsdawn</code> をインストールしたり実行したりする前に、あなたに確認します。</li>
  <li>あなたの文書をどこかに送信することはありません。<code>marsdawn</code> はあなたの Mac 上でレンダリングし、<code>--allow-remote-images</code> を指定しない限りウェブからの画像を除外します。</li>
</ul>
<p>すべての仕様、すべてのフィールドとコードは<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>にあります。</p>
""",
    }
    _mcp_url = "https://github.com/redtear1115/marsdawn-mcp"
    _mcp_license = "Apache-2.0"
    pages['cli/mcp'] = {
        "title": 'marsdawn を呼び出す三つの方法：CLI、skill ファイル、MCP サーバー · MarsDawn',
        "description": 'marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。',
        "body": f"""
<section class="intro">
  <h1>marsdawn を呼び出す三つの方法。</h1>
  <p>MarsDawn には自前の AI モデルがありません。Markdown を書くためではなく、レビューするために作られているので、どのエージェントやモデルがそのファイルを作ったかは関係ありません。エージェントやスクリプトが <code>marsdawn</code> を呼び出す方法は三つあり、どれも最終的に同じ <code>export</code> を実行します。</p>
</section>

<div class="summary"><p><strong>使っているツールが対応しているものを選んでください：無料の <code>marsdawn</code> CLI、プレーンな Markdown の skill ファイル、または <a href="{_mcp_url}">marsdawn-mcp</a> という MCP サーバーです。</strong>三つとも同じ <code>marsdawn export</code> を呼び出し、同じ JSON 結果を返します。</p></div>

<h2>どれを使うか</h2>
<!--compare:mcp-choice-->

<h2>CLI</h2>
<p><code>marsdawn export notes.md --json</code> は、シェルコマンドを実行できるエージェントやスクリプトならどれからでも呼び出せます。構造上、モデルに依存しません。返されるすべてのフィールドは<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>に文書化されており、そこが JSON スキーマの正典で、以下の二つの経路もそこを参照します。</p>

<h2>skill ファイル</h2>
<p>シェルを直接呼び出すのではなく、プレーンな Markdown の指示を読むエージェント向け——現時点では Claude Code——には、<a href="/ja/cli/skill/">marsdawn skill</a> という1ファイルが、marsdawn のインストール、<code>export</code> の実行、結果の読み取りを教えます。プレーンな Markdown なので、指示ファイルを読み込む他のエージェントも同じファイルを使えます。</p>

<h2>MCP サーバー</h2>
<p><a href="{_mcp_url}">marsdawn-mcp</a> は、別の、公開された、{_mcp_license} ライセンスの独立した repository です。<code>export_markdown_to_pdf</code> と <code>open_in_marsdawn</code> という2つのツールを持つ MCP サーバーで、それぞれ <code>marsdawn export --json</code> と <code>marsdawn open --json</code> をラップしています。MCP クライアントをそれに向ければ、ツール呼び出しは CLI と同じ JSON を返します。</p>
<ul>
  <li><strong>入手方法：</strong><a href="{_mcp_url}/releases">GitHub のリリース</a>に添付された MCP Bundle（<code>marsdawn.mcpb</code>）として、またはソースから stdio でサーバーを実行することで入手できます。</li>
  <li><strong>Registry：</strong>まだ MCP Registry には登録されていません（現在のリリース：0.2.1）。registry 経由で見つかる前に、repository で現在の状況を確認してください。</li>
  <li><strong>ホスティング：</strong>自分でホストするしかありません。marsdawn-mcp のホスティングサービスは存在せず、サーバーは marsdawn 自身の隣、あなた自身のマシン上で動きます。</li>
  <li><strong>動作要件：</strong>macOS、marsdawn 0.5.0 以降、そしてサーバーを実行するための Node.js 20 以降。</li>
</ul>

<h2>許可したフォルダの中でしか動きません</h2>
<p>両方のツールとも、許可したフォルダの中でしか読み書きしません：拡張機能の「Allowed folders」設定（デフォルトは空です）、またはお使いの MCP クライアントが提供する roots のどちらかです。どちらも設定されていない場合、すべての呼び出しは拒否され、拒否メッセージに設定方法が書かれています。パスはすべて絶対パスである必要があり、<code>export_markdown_to_pdf</code> が書き出すのは <code>.pdf</code> ファイルだけで、シンボリックリンク経由で書き込むことはありません。</p>
<p><strong>セキュリティ：</strong><a href="{_mcp_url}/releases/tag/v0.2.1">0.2.1</a> に更新してください&#8212;&#8212;0.1.0 と 0.2.0 では、呼び出しがあなたのアカウントが書き込めるどのパスにも PDF を書き込めてしまう問題があり、<a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a> で修正されました。</p>

<h2>同じ export、三つの入り口</h2>
<p>どの入り口から呼び出しても、内部の動作は変わりません。同じ書き出しエンジン、同じテーマと紙のサイズ、Mermaid 図の描画に失敗したときの同じ <code>diagramErrors</code>。このページではその契約内容を繰り返しません。<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>に完全な内容があります。</p>

<h2>次に</h2>
<ul>
  <li>完全な JSON スキーマとすべての終了コード：<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>。</li>
  <li>Claude Code などのエージェント向けの1ファイルの skill：<a href="/ja/cli/skill/">marsdawn skill</a>。</li>
  <li>簡潔な JSON 結果が、なぜエージェント自身の context にとって重要なのか：<a href="/ja/token-efficient-review/">{ui['token-efficient-review']}</a>。</li>
</ul>
""",
    }
    pages['token-efficient-review'] = {
        "title": 'エージェントのトークンを使わずに MarsDawn の出力をレビューする · MarsDawn',
        "description": '人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。',
        "body": """
<section class="intro">
  <h1>エージェントのトークンを使わずにレビューする。</h1>
  <p>このループでは、二つの別々のことがどちらも安く済みます。エージェントがツール呼び出しから受け取るもの、そして結果が正しく見えることを確認するのに必要なもの、です。</p>
</section>

<div class="summary"><p><strong>ツール呼び出しが返すのは小さな JSON オブジェクトであり、レンダリングされたページではありません。レンダリングされたページ自体は、人が MarsDawn の中で読みます。エージェントの context に読み戻されることは決してありません。</strong></p></div>

<h2>ツール呼び出し自体が安い</h2>
<p><code>marsdawn export</code> を、CLI、skill、または<a href="/ja/cli/mcp/">MCP サーバー</a>のいずれからでも呼び出すと、返ってくるのは<a href="/ja/cli/agents/">簡潔な JSON オブジェクト</a>です：<code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code>、<code>diagramErrors</code>。完全なスキーマは <a href="/schemas/cli/export.v1.json">export.v1.json</a> にあります。そのどれもレンダリングされた文書そのものではありません。十数個の Mermaid 図がある50ページの PDF も、1ページのメモと同じ数のフィールドしか返しません。</p>

<h2>レビューは、別のところで行われる</h2>
<p>PDF ができたら、人がそれを開きます。MarsDawn でも、どんな PDF ビューアでも構いません。そして図、数式、レイアウトがレンダリングされた状態で読みます。エージェントは、それが正しく見えることを確認するために、レンダリング結果を自分の context に読み戻す必要はありません。レビューは別のウインドウ、別の画面で行われ、図がどう見えるかを説明するために token を使うもう一往復にはなりません。</p>

<h2>これが避けられるもの</h2>
<ul>
  <li>レンダリングされた Markdown やスクリーンショット、あるいはその説明を、書き出しが成功したことをエージェントに確認させるためだけに会話に貼り戻すこと。</li>
  <li>エージェントが、Mermaid 図や KaTeX の数式がどう描画されるかを、人が見れば済むところを自分で再構成しなければならないこと。</li>
  <li>最初の呼び出しがすでに成功を報告した後で、PDF の内容を取得するために二度目のツール呼び出しをすること。</li>
</ul>

<h2>次に</h2>
<ul>
  <li>marsdawn を呼び出す三つの方法、CLI、skill ファイル、MCP サーバー：<a href="/ja/cli/mcp/">三つの入り口</a>。</li>
  <li>JSON 結果のすべてのフィールド：<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>。</li>
  <li>なぜ人がエージェントの書いたものを読む必要が今もあるのか：<a href="/ja/reviewing-ai-output/">レビューが必要な理由</a>。</li>
  <li>より詳しい理由とチェックリスト：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
</ul>
""",
    }
    pages['vs/markdown-preview-tools'] = {
        "title": 'ほかの場所で Markdown を見る、対 MarsDawn · MarsDawn',
        "description": 'VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。',
        "body": """
<section class="intro">
  <h1>ほかの場所で Markdown を見る、対 MarsDawn。</h1>
  <p>すでに VS Code やブラウザ、Claude Desktop を開いているなら、それらで Markdown ファイルをちらっと見るのは妥当な選択です。それぞれが実際に何をレンダリングし、そこにたどり着くのに何が必要か、MarsDawn で同じファイルを開いた場合と比較してみます。</p>
</section>

<h2>ひと目で比較</h2>
<!--compare:preview-tools-->

<h2>VS Code の内蔵プレビュー</h2>
<p>VS Code で <kbd>&#8984;&#8679;V</kbd> を押すと、内蔵のプレビューパネルで Markdown ファイルがレンダリングされます。無料で、インストールするものもありません。VS Code 1.121（2026年5月）以降、このプレビューは Mermaid 図もネイティブに描画します。Microsoft が Mermaid 拡張機能を VS Code 本体に組み込んだためで、以前は別の拡張機能が必要でしたが、今は不要です。できないこと：これはエディタの中のプレビューパネルであって、読むために作られたエディタではありません。パネルの隣にはファイルツリー、ターミナル、VS Code が表示できるその他のパネルが並び、VS Code 自体も Electron アプリで、インストールするのは開発環境一式であって、1つのファイルを読むために開くものではありません。</p>

<h2>ローカルファイル用のブラウザ拡張機能</h2>
<p>ローカルの <code>.md</code> ファイルを読むために主流と呼べるブラウザ拡張機能はありません。Local Markdown Viewer、Markdown Viewer、MarkView などがだいたい同じことをしていて、どれもデフォルトではありません。どれも、何かを開く前に同じ手順が必要です。ブラウザはデフォルトで拡張機能に <code>file://</code> のページを読ませないので、その拡張機能の「ファイルの URL へのアクセスを許可」を有効にする必要があります。これは拡張機能ごとに一度だけ与える権限ですが、与えたこと自体や、なぜ与えたのかを忘れやすいものです。有効にすると、ファイルはブラウザのタブに表示されます。つまり、1つのファイルを見るために、ブラウザを丸ごと動かすことになります。</p>

<h2>Claude Desktop のファイルプレビュー</h2>
<p>Claude Desktop が表示するのは、すでに Project や会話の中にあるファイルです。それが作られていないのは、ディスク上の任意のファイルを閲覧することです。見られるのは会話がすでに持っているものであって、作業の傍らに開いておくメモのフォルダではありません。Anthropic 自身が挙げている<a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">アップロードできるファイルの種類</a>は PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX で、Markdown は入っていません。</p>

<h2>1つのファイルを読むために、ブラウザエンジンが動く</h2>
<p>VS Code は Electron アプリです。Chromium と Node.js のランタイムが同梱されていて、ネイティブの Mac アプリではありません。ブラウザ拡張機能という道は、実際のブラウザの中で動きます。どちらにしても、1つの Markdown ファイルを見るために、丸ごとのブラウザエンジンが裏で動いていることになります。MarsDawn はネイティブの AppKit アプリです。ブラウザのランタイムを同梱しておらず、どんなローカルファイルも直接開けて、インストールする拡張機能も、覚えておくべき権限フラグもありません。</p>

<h2>次に</h2>
<ul>
  <li>MarsDawn もできないこと：<a href="/ja/limits/">その一覧</a>。</li>
  <li>今日、無料でどんな Markdown ファイルも PDF にする：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。</li>
  <li>Mac ネイティブのビューアとの比較：<a href="/ja/vs/macmd-viewer/">MacMD Viewer と MarsDawn</a>。</li>
</ul>
""",
    }
    pages['themes'] = {
        "title": 'MarsDawn のプレビューテーマと PDF 書き出し · MarsDawn',
        "description": 'それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。',
        "body": """
<section class="intro">
  <h1>8つの見た目、1つの書き出し。</h1>
  <p>MarsDawn には 夜明け、クラシック、モダン、ビビッド の4種類のプレビューテーマが付属し、それぞれライトとダークがあります。文書を読むための8通りの組み合わせです。PDF に書き出す、または印刷すると、そのとき読んでいたものと同じ見た目でページが出てきます。</p>
</section>

<div class="summary"><p><strong>4つのテーマ × ライトとダーク＝文書を読む8つの方法があり、書き出しはどれを選んでいても対応します。</strong>もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーは計画中で、まだ作られていません。</p></div>

<h2>4種類のテーマ</h2>
<!--theme-gallery-->
<ul>
  <li><strong>夜明け</strong>、デフォルト：このサイトと同じ、温かみのある紙の質感と Mars Rust のアクセントカラー。</li>
  <li><strong>クラシック</strong>：より素朴で、紙の文書らしい配色。</li>
  <li><strong>モダン</strong>：より涼しげで、現代的な配色。</li>
  <li><strong>ビビッド</strong>：より明るく、コントラストの高い配色。</li>
</ul>
<p>それぞれ独自のライトとダークの配色を持つので、Mac の外観を切り替えると、インターフェースの色だけでなくテーマの配色自体も切り替わります。</p>

<h2>PDF 書き出しと印刷は同じテーマを使う</h2>
<p>PDF に書き出す、または印刷すると、テーマのライトカラーが使われます。Mermaid 図はそこに描き込まれ、コードブロックは構文のハイライトを保ち、改ページは見出しをそのセクションから切り離したり、表や図を途中で切ったりしないよう配慮されます。無料の<a href="/ja/cli/">marsdawn コマンドラインツール</a>も同じ書き出しエンジンを使うので、スクリプトやエージェントも <code>--theme</code> で、4種類のどのテーマでも同一の PDF を作れます。</p>

<h2>計画中：もっと多くのテーマと、ギャラリー</h2>
<p>今後登場する予定でまだ実装されていないもの：輸入可能なプレビューテーマの追加と、このサイト上で誰もが自分のテーマを投稿できるギャラリーです。<code>/themes/v1/</code> はすでにそのために予約されています。それが公開されるまで、MarsDawn にあるのはこの4つの内蔵テーマだけで、他のテーマをインストールすることはできません。</p>

<h2>次に</h2>
<ul>
  <li>コマンドラインからの、完全な PDF 書き出しの手順：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。</li>
  <li>MarsDawn がまだできないこと：<a href="/ja/limits/">その一覧</a>。</li>
  <li>Markdown を使わない人に、書き出した PDF を渡す：<a href="/ja/sharing-exported-pdfs/">PDF を共有する</a>。</li>
</ul>
""",
    }
    pages['sharing-exported-pdfs'] = {
        "title": 'Markdown を教えずに、エージェントが書いたものを共有する · MarsDawn',
        "description": 'エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。',
        "body": """
<section class="intro">
  <h1>Markdown ではなく、PDF を渡す。</h1>
  <p>エージェントが文書を仕上げ、あなたがレビューして直したあと、エンジニアリング以外の誰か、マネージャー、クライアント、別のチームの人もそれを読む必要が出てきます。彼らは <code>##</code> や表の縦線が何を意味するかを知る必要はありません。PDF に書き出して、それを代わりに渡しましょう。</p>
</section>

<div class="summary"><p><strong>レビュー済みの文書を PDF に書き出し、そのファイルを送ってください。</strong>どんな環境でも開け、Markdown の知識もインストールも不要で、プレビューで見たときと同じ見た目です。図、表、書式もそのままです。</p></div>

<h2>なぜ .md ファイルをそのまま送らないのか</h2>
<p>プレーンテキストエディタで開いた生の <code>.md</code> ファイルには、ページではなく記号が見えます。見出しは <code>#</code>、太字の前後は <code>**</code>、Mermaid 図を囲むフェンスブロックは、図として描画されないままです。Markdown を書かない人には、これらの記号が意図どおりには伝わりませんし、1つの文書のためにビューアを先にインストールしてもらうのも、頼みごととしては大きすぎます。</p>

<h2>なぜスクリーンショットでもないのか</h2>
<p>スクリーンショットは、複数ページに及ぶかもしれない文書の、画面1枚分を切り取って固定するだけで、検索も選択もできず、圧縮されて何度か転送されるうちにさらに読みにくくなります。PDF は、どんな長さでもテキストと図、改ページをそのまま保ちます。</p>

<h2>PDF が得られるもの</h2>
<ul>
  <li>受け取る側がすでに持っているもので開けます。プレビュー、ブラウザ、Acrobat、スマートフォンなど、Markdown のツールは一切不要です。</li>
  <li>Mermaid 図はコードのままではなく描き込まれ、コードブロックはハイライトを保ちます。</li>
  <li>改ページは、見出しがページの下端に一人取り残されたり、表や図が2ページにまたがって切れたりしないよう選ばれます。</li>
  <li>MarsDawn アプリから来たものでも、無料のコマンドラインから来たものでも、同じファイルになります。その手順は<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>をご覧ください。</li>
</ul>

<h2>次に</h2>
<ul>
  <li>書き出しに使えるテーマとレイアウト：<a href="/ja/themes/">プレビューテーマと PDF 書き出し</a>。</li>
  <li>アプリの代わりに、スクリプトやエージェントから書き出す：<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>。</li>
  <li>なぜ、まず人がその文書を読む必要があるのか：<a href="/ja/reviewing-ai-output/">レビューが必要な理由</a>。</li>
  <li>複数のエージェントの引き継ぎは、共有すべき PDF が生まれやすい場面です：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
</ul>
""",
    }
    pages['reviewing-ai-output'] = {
        "title": 'なぜ AI の出力には、今も人の目が必要なのか · MarsDawn',
        "description": 'AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。',
        "body": f"""
<section class="intro">
  <h1>エージェントが書く。それでも、あなたが理解しなければならない。</h1>
  <p>AI エージェントは、計画書や仕様書、メモをすばやく書き上げられます。それでも、書かれたものを実際に行動に移す人が理解する必要があります。読みやすいからといって、そのまま信用してはいけません。</p>
</section>

<div class="summary"><p><strong>MarsDawn は、まさにそう読むために作られています。レンダリングされたページをソースの隣に置き、Mermaid 図と KaTeX 数式を記号のままにせず描画するので、文書の構造が一目で分かります。</strong></p></div>

<h2>読みやすさと、正しさは別物</h2>
<p>AI を使ったコーディングについて書きながら、Simon Willison は、書き捨てではなく後々また手を加えるコードについてこう述べています。「the quality and understandability of the underlying code is crucial」（根底にあるコードの品質と、理解しやすさが極めて重要だ、<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>、2025年）。文書についても同じことが言えます。すらすら読めるエージェントの草稿でも、構造や数字、論理が間違っていることはあり、読みやすい文章は、どこを確認すべきかを教えてはくれません。</p>

<h2>推論であって、コンパイルではない</h2>
<p>Thoughtworks の Birgitta B&#246;ckeler は、この違いをはっきりと言い切っています。「LLMs are NOT compilers, interpreters, transpilers or assemblers of natural language, they are inferrers」（LLM は自然言語のコンパイラでも、インタプリタでも、トランスパイラでも、アセンブラでもなく、推論器である、<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>）。コンパイラは入力を受理するか、エラーを報告するかのどちらかです。エージェントは、動く、あるいは読める何かを返してきても、それが正しいとは限りません。それでもなお、誰かが確認する必要があります。</p>

<h2>MarsDawn が、読む人に与えるもの</h2>
<ul>
  <li>レンダリングされたページをソースの隣に置き、どちらか一方が変わるたびに更新するので、文章の中の主張と、その構造とを同時に見られます。</li>
  <li>Mermaid 図を描画します。エージェントが文章で説明したフローチャートが、実際に目で追える形になります。</li>
  <li>KaTeX 数式を、バックスラッシュの羅列のままにせずレンダリングします。数式は、数式として読めます。</li>
  <li>何も勝手には動きません。MarsDawn は文書を採点したり、要約したり、代わりに印を付けたりはしません。構造をあなたの目の前に置くだけです。あとはあなたが判断します。</li>
</ul>

<h2>次に</h2>
<ul>
  <li>このレビューが、なぜエージェント自身の context にとって安上がりなのか：<a href="/ja/token-efficient-review/">{ui['token-efficient-review']}</a>。</li>
  <li>レビュー済みの文書を、ほかの人に渡す：<a href="/ja/sharing-exported-pdfs/">PDF を共有する</a>。</li>
  <li>なぜエージェントはそもそも計画を示すのか：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>MarsDawn とは何か、1ページで：<a href="/ja/">ホームページ</a>。</li>
</ul>
""",
    }
    pages['reading-agent-output'] = {
        "title": "エージェントが返してくるものを読む · MarsDawn",
        "description": "AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。",
        "body": f"""
<section class="intro">
  <h1>エージェントの仕事は、あなたが読む Markdown ファイルとして返ってくる。</h1>
  <p>コーディングエージェントに移行を計画させたり、仕様書を書かせたり、バグを追わせたりする。しばらく自分で動いたあと、返ってくるのは 1 つのファイルだ。<code>plan.md</code>、<code>SPEC.md</code>、進捗報告、調査のまとめ。確認できる範囲では、そのファイルが仕事そのものだ。</p>
</section>

<div class="summary"><p><strong>エージェントが正しくやったかどうかは、返ってきたものを読んで初めて分かる。MarsDawn は、その読み方のための Mac アプリだ。</strong></p></div>

<h2>エージェントを作る人たちの言葉</h2>
<p>引用はそのまま。私たちの解釈はあとに書く。</p>
<ul>
  <li>Anthropic の「Building Effective Agents」（Erik S. と Barry Zhang、2024 年 12 月）は、エージェントを作るための 3 つの原則を挙げていて、その 1 つが「Prioritize transparency by explicitly showing the agent&#8217;s planning steps.」（透明性を優先し、エージェントの計画のステップを明示的に示す。）これはエージェントを作る人向けの原則だ。あなたの側から見れば、その透明性とは、結局あなたが読むことになる計画のことだ。</li>
  <li>同じ記事：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（エージェントはチェックポイントや障害に出会ったとき、人間のフィードバックを待って一時停止できる。）動詞に注目してほしい：<em>can</em>（できる）。</li>
  <li>Chip Huyen は「Agents」（2025 年 1 月）で、計画と実行を分けるべき理由をこう説明する：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it&#8217;s not going anywhere.」（監督がなければ、エージェントは何時間もそのステップを実行し続け、API 呼び出しに時間とお金を浪費したあとで、それが何も進んでいないことにあなたが気づく、ということもあり得る。）彼女はさらにこんな失敗も描いている：「The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.」（エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）50 人を 30 部屋に割り振るよう頼まれたエージェントは、40 人しか割り振らないまま、終わったと言い張る。</li>
  <li>Andrew Ng は The Batch（2024 年 4 月）で planning パターンについてこう述べる：「On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results.」（一方で、計画は非常に強力な能力だ。他方で、予測しにくい結果につながる。）これは予測可能性についての指摘であって、人によるレビューを求めているわけではない。彼は計画能力が急速に向上すると見ている。</li>
</ul>
<p><strong>ここからは著者たちの主張ではなく、私たちの推論だ：</strong>エージェントが計画を示し、チェックポイントで止まるなら、そのチェックポイントで計画を読むのは、たいていあなただ。エージェントが終わっていないのに終わったと思い込むことがあるなら、その「完了報告」にも読み手が必要になる。ここに挙げた著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。</p>

<h2>見た目より読みにくい理由</h2>
<p>ファイルは長く、重要な部分はたいてい先頭にはない。Mermaid の図や数式が入っていて、ソースのままでは追いにくい。読んでいる途中で、エージェントがまだファイルを書き換えていることもある。ファイルは複数にまたがることが多く、ブランチや worktree をまたぐこともある。そして問題を見つけたとき、「キャッシュの部分がおかしい」ではエージェントは推測するしかないが、「<code>docs/plan.md:42</code> はバックフィルが終わる前に古いテーブルを落としている」ならそうはならない。</p>

<h2>MarsDawn が助けになるところ</h2>
<ul>
  <li><strong>長いファイル：</strong>サイドバーのアウトラインタブ（&#8963;&#8984;S）に見出しが並ぶ。クリックすると両方のペインがそこへ移動する。</li>
  <li><strong>図と数式：</strong>Mermaid と KaTeX はソースの隣のプレビューに描画され（&#8984;2）、両方のペインが一緒にスクロールする。</li>
  <li><strong>読んでいる途中の書き換え：</strong>エージェントがファイルを書き換えると、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。</li>
  <li><strong>複数のファイル：</strong>「ファイル &#9656; フォルダを開く&#8943;」（&#8679;&#8984;O）でエージェントの作業フォルダを開く。新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出る。</li>
  <li><strong>正確なフィードバック：</strong>「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）で、いまいる場所を <code>docs/plan.md:42</code> の形でコピーできる。「AI 用にコピー」（&#8963;&#8997;&#8984;C）は、その下に選択したテキストを付け加える。どちらもエージェントのチャットに貼り付ければいい。</li>
</ul>
<p>このループにはもう 2 つ関係がある。エージェントは <code>marsdawn open plan.md:42</code> を実行して、MarsDawn でファイルを 42 行目、つまりまず見てほしい行で開かせることができる。そしてレビューが終わったファイルは、アプリから、あるいは無料の <code>marsdawn export</code> コマンドで PDF に書き出せる。</p>
<p>MarsDawn の中に AI モデルはない。計画を要約したり、採点したり、何が間違っているか教えたりはしない。読むのはあなたで、MarsDawn は長く変わり続けるファイルを読みやすく保ち、正確な行を指し示せるようにするだけだ。</p>

<h2>5 分でエージェントの計画をレビューする</h2>
<p>どんなエディタでも使える方法だ。</p>
<ol>
  <li>見出しだけを読む。アウトラインは頼んだ内容と一致しているか。セクションが欠けていれば、たいてい作業も欠けている。</li>
  <li>「完了」「合格」「検証済み」と書かれている箇所をすべて見つけ、そのうち 1 つを自分で確認する：ファイルを開く、テストを実行する、行数を数える。</li>
  <li>取り消せないステップを探す：データの削除、マイグレーション、force push、何かを送信・支払い・公開する処理。それらはあなたの明示的な OK を待つべきだ。</li>
  <li>図はレンダリングした状態で読み、矢印の 1 つひとつを本文と照らし合わせる。</li>
  <li>計画が触れるファイルとシステムを列挙する。頼んでいないことがあれば、実行前に確認する。</li>
  <li>フィードバックは「場所・問題・直し方」で書く：「<code>plan.md:88</code>：バックフィルが drop のあとに実行される。ステップ 4 と 5 を入れ替えて。」1 行に 1 つの問題だけを書く。</li>
</ol>
<p>時間がないなら、ステップ 2 だけをやろう。終わったと思い込んでいるエージェントが見つかるのは、たいていそこだ。より詳しい説明と実例は<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>にある。</p>

<h2>試してみる</h2>
<p>MarsDawn は近日 Mac App Store に登場予定です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。アプリが出たあとは、<code>marsdawn open</code> でエージェントにファイルを開かせることもできます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; AI エージェント向けの参照：<a href="/ja/cli/agents/">marsdawn for agents</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>AI の出力をそもそも読むべき理由（短い版）：<a href="/ja/reviewing-ai-output/">AI の出力を人が確認する理由</a>。</li>
  <li>レビュー中もエージェントの context を小さく保つ：<a href="/ja/token-efficient-review/">トークンを抑えたレビュー</a>。</li>
  <li>なぜエージェントはそもそも計画を示すのか：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>上のチェックリストを、実例つきで詳しく：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>エージェントの種類ごとに、どんな文書が返ってくるか：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
</ul>

<h2>出典</h2>
<ul>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a>（2026-09-26 時点のオンライン版から引用。同記事は現在、2024 年 12 月以降ツール環境が大きく変わったと注記している）</li>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 4, Planning,&#8221; The Batch, April 10, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": "Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？ · MarsDawn",
        "description": "Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。",
        "body": f"""
<section class="intro">
  <h1>Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</h1>
  <p>2024 年 12 月、Anthropic は AI エージェントを作る人向けのガイド「Building Effective Agents」を発表した。その要約は 3 つの原則を挙げていて、その 1 つが透明性だ。この記事は、その原則のもう一方の端について書く。エージェントが自分のステップを示したあと、結局は誰かがそれを読むことになる。</p>
</section>

<div class="summary"><p><strong>透明性はエージェントがすることで、読むのはあなたがすることだ。Anthropic は開発者に、エージェントの計画のステップを示すよう求めている。コーディングエージェントを日々動かす多くの人にとって、そのステップは結局、しかるべきタイミングで誰かが読む Markdown ファイルとしてやって来る。</strong></p></div>

<h2>ガイドが書いていること</h2>
<p>Erik S. と Barry Zhang は、要約でこうまとめている。</p>
<blockquote><p>&#8220;When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent&#8217;s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.&#8221;</p></blockquote>
<p>（エージェントを実装するとき、私たちは 3 つの中心的な原則に従おうとする。エージェントの設計をシンプルに保つこと。透明性を優先し、エージェントの計画のステップを明示的に示すこと。十分なツールのドキュメントとテストを通じて、エージェントとコンピュータの間のインターフェース（ACI）を丁寧に作り込むこと。）</p>
<p>これらはエージェントを作る人向けの設計原則であって、使う人への操作指示ではない。原則が求めているのはステップを示すことで、誰がそれを読むかは書かれていない。</p>
<p>同じ記事は、タスクを受け取ったあとエージェントが何をするかも描いている：「Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.」（タスクが明確になると、エージェントは計画を立て、自律的に動く。必要に応じて、追加の情報や判断を求めて人間に戻ってくることもある。）そして：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（エージェントはチェックポイントや障害に出会ったとき、人間のフィードバックを待って一時停止できる。）動詞に注目してほしい：<em>potentially</em>（必要に応じて）と <em>can</em>（できる）。チェックポイントは、エージェントが持ちうる設計として描かれていて、必須のものとしてではない。</p>

<h2>チェックのほとんどは、あなたがしているわけではない</h2>
<p>ここは誇張しやすいところなので、ガイドが実際に最初に置いていることを見ておこう。エージェントは、世界に対して自分自身をチェックする：「During execution, it's crucial for the agents to gain &#8220;ground truth&#8221; from the environment at each step (such as tool call results or code execution) to assess its progress.」（実行中、エージェントが自分の進捗を評価するには、各ステップで環境から「ground truth」（ツール呼び出しの結果やコード実行の結果など）を得ることが重要だ。）この一文の ground truth は、テスト結果やツールの出力を指していて、人間のことではない。</p>
<p>ガイドはリスクについても率直だ：「The autonomous nature of agents means higher costs, and the potential for compounding errors.」（エージェントの自律的な性質は、より高いコストと、エラーが積み重なる可能性を意味する。）その答えは、ガードレール付きのサンドボックス環境での広範なテストであって、「もっと注意深く読め」ではない。</p>
<p>人が実際に登場するのは、コーディングエージェントについての付録だ：「However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.」（しかし、自動テストは機能の検証には役立つ一方、解決策がより広いシステム要件に沿っているかを確かめるには、人によるレビューが依然として重要だ。）この一文はコードについてのものだが、それが指し示すギャップは、どんなエージェントを使っていても見覚えがあるはずだ。テストは、何かが動くことは教えてくれても、それがあなたの意図どおりかまでは教えてくれない。</p>

<h2>示されたステップは、どこへ行くのか</h2>
<p><strong>ここから先は、私たちの解釈であって、Anthropic の主張ではない。</strong></p>
<p>コーディングエージェントを日々使っているなら、その計画のステップは、たいていダッシュボードには現れない。ファイルとして現れる：<code>plan.md</code>、チェックボックス付きのタスクリスト、エージェントが書き換え続ける進捗ファイル、最後にまとめの文書。透明性は、あなたの側から見ると、読むものが増えるということを意味する。</p>
<p>ステップを示すのはエージェント側の役割だ。もう半分は、それが重要な場面で人が読むこと。マイグレーションを実行する前、ブランチをマージする前、「完了」を受け入れる前。すべてを 600 行の、誰も開かないファイルに書き出すエージェントは、紙の上では透明でも、実際には監督されていない。</p>
<p>Harrison Chase は 2024 年、文書についてではなくエージェントフレームワークがどう動くべきかについて、関連することを述べている：「You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.」（内部で何が起きているかを観察できる必要がある。実際に取られるステップは、事前には分からないことがあるからだ。）彼が話しているのは、エージェントを作る人向けのツールだ。もしあなたがエージェントを動かしている当人なら、それがずっと書き続けている素のファイルこそ、あなたが観察できる部分であることが多い。</p>
<p>ここに挙げた著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。</p>

<h2>見た目より読みにくい理由</h2>
<p>ファイルは長く、重要な部分はたいてい先頭にはない。変更を説明する図は Mermaid のソースであって、絵ではない（実際に描画されたものを見る方法は<a href="/ja/view-markdown-on-mac/">「Mac で Markdown を見る方法」</a>にある）。読んでいる途中で、エージェントがファイルを書き換えることもある。ファイルは複数にまたがることが多く、ブランチや worktree が違うこともある。そして問題を見つけたとき、「キャッシュの部分がおかしい」ではエージェントは推測するしかない。この話の詳しい版は<a href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a>にある。</p>

<h2>MarsDawn ができること、できないこと</h2>
<p>MarsDawn は、この読み方のための Mac アプリだ。エージェントをより透明にするわけではなく、中に AI モデルもない。計画を要約したり、正しいかどうか教えたりはしない。できることは：</p>
<ul>
  <li><strong>長いファイル：</strong>「表示 &#9656; サイドバーを表示」（&#8963;&#8984;S）でアウトラインタブを開くと、見出しが並ぶ。クリックするとそこへ移動する。</li>
  <li><strong>図と数式：</strong>ソースとレンダリングされたページが並んで表示され（&#8984;2）、一緒にスクロールする。Mermaid と KaTeX は描画される。図が壊れている場合、プレビューはそのソースとエラーを一緒に表示する。</li>
  <li><strong>読んでいる途中の書き換え：</strong>エージェントがファイルを書き換えると、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。</li>
  <li><strong>複数のファイル：</strong>「ファイル &#9656; フォルダを開く&#8943;」（&#8679;&#8984;O）でエージェントの作業フォルダを開く。新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出る。</li>
  <li><strong>行を指し示す：</strong>「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）で、いまいる場所を <code>docs/plan.md:42</code> の形でコピーできる。「AI 用にコピー」（&#8963;&#8997;&#8984;C）は、その下に選択したテキストを付け加える。エージェントのチャットに貼り付ければいい。</li>
</ul>
<p>読むのはやはりあなただ。MarsDawn は、長く変わり続けるファイルを、あなたが読んでいる間、読みやすく保つだけだ。</p>

<h2>試してみる</h2>
<p>MarsDawn は近日 Mac App Store に登場予定です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>エージェントの出力がなぜ読みにくいか、そのチェックリスト：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>そのチェックリストを、実例つきで詳しく：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>エージェントの種類ごとに、どんな文書が返ってくるか：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
  <li>AI の出力をそもそも読むべき理由（短い版）：<a href="/ja/reviewing-ai-output/">AI の出力を人が確認する理由</a>。</li>
</ul>

<h2>出典</h2>
<ul>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a>（2026-09-26 時点のオンライン版から引用。同記事は現在、2024 年 12 月以降ツール環境が大きく変わったと注記している）</li>
  <li>Harrison Chase, &#8220;What is an agent?,&#8221; LangChain, June 28, 2024, archived copy: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a>（元の URL は現在 2026 年の別記事を表示している）</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": "エージェントの計画を 5 分でレビューする · MarsDawn",
        "description": "AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。",
        "body": f"""
<section class="intro">
  <h1>エージェントの計画を 5 分でレビューする</h1>
  <p>エージェントが計画を書き上げ、ゴーサインを待っている。あなたにあるのは 5 分で、1 時間ではない。ここでは、その 5 分の使い方を紹介する。プレーンテキストのエディタでも、どんなエディタでも使える方法だ。MarsDawn が助けになるステップもあるので、どこかは明記する。ただし、いちばん大事なステップでは助けにならない。</p>
</section>

<div class="summary"><p><strong>計画は最初から最後まで読まない。まず形を見て、主張を 1 つ確認し、取り消せないものを探し、図と範囲を見て、それからエージェントが動けるフィードバックを書く。6 ステップ、約 5 分。</strong></p></div>

<h2>実行前に手間をかける理由</h2>
<p>Chip Huyen は、計画と実行を分けるべき理由を説明しながら、コストをはっきり言う：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it&#8217;s not going anywhere.」（監督がなければ、エージェントは何時間もそのステップを実行し続け、API 呼び出しに時間とお金を浪費したあとで、それが何も進んでいないことにあなたが気づく、ということもあり得る。）私たちからの補足：計画は、間違いを見つけるのにいちばん安上がりな場所だ。<code>plan.md</code> の 1 行を直すのは、1 文で済む。エージェントが実行し終わったあとの後始末は、午後まるごとかかることもある。</p>

<h2>例</h2>
<p>ユーザーのアバターをオブジェクトストレージに移す作業を、既存のリンクを壊さずにやるようエージェントに頼んだ。返ってきたのはこれだ：</p>
<pre><code># Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. &#9989; done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.</code></pre>
<p>読んだ感じは問題なさそうだ。だがこのとおりにやると、コピーする前に、すべてのアバターを削除してしまう。</p>

<h2>6 つのステップ</h2>
<p><strong>1. 見出しだけを読む。</strong>（約 1 分）アウトラインは頼んだ内容と一致しているか。ここでは Goal、Steps、Status。既存のリンクを壊さないでほしいと頼んだのに、古いリンクや、変更を取り消す方法についての見出しがない。これが最初のコメントになる。</p>
<p>ターミナルから <code>grep -n '^#' plan.md</code> を実行すれば、見出しだけが表示される。多くのエディタにもアウトライン表示がある。MarsDawn では、サイドバーのアウトラインタブ（表示 &#9656; サイドバーを表示、&#8963;&#8984;S）に見出しが並び、クリックするとそこへ移動する。</p>
<p><strong>2. 「完了」「合格」「検証済み」と書かれている箇所をすべて見つけ、そのうち 1 つを自分で確認する。</strong>（約 1 分）ファイルを開く、テストを実行する、行数を数える。Chip Huyen は、こんな失敗を描いている：「The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.」（エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）彼女の例では、50 人を 30 部屋に割り振るよう頼まれたエージェントが、40 人しか割り振らないまま、終わったと言い張る。</p>
<pre><code>grep -n -i -E 'done|pass|verified|&#9989;' plan.md</code></pre>
<p>この例では「&#9989; done」と「All tests pass.」が見つかる。どのテストか？ アバターに触れるものはあるか？ 自分で実行するか、聞いてみる。この作業を MarsDawn が代わりにやることはできない。あなた以外、誰にもできない。</p>
<p><strong>3. 取り消せないステップを探す。</strong>（約 1 分）データの削除、マイグレーション、force push、何かを送信・支払い・公開する処理。それらはあなたの明示的な OK を待つべきだ。Chip Huyen は、同じ考えをシステム側の視点からこう述べている：「If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.」（計画にリスクのある操作、たとえばデータベースの更新やコード変更のマージが含まれる場合、システムは実行前に明示的な人間の承認を求めることも、それらの操作の実行自体を人間に委ねることもできる。）この例では、ステップ 4 が元のファイルを削除し、それがステップ 5 のコピーより前に来ている。</p>
<p><strong>4. 図はレンダリングした状態で読み、矢印の 1 つひとつを本文と照らし合わせる。</strong>フローチャートが「copy &#8594; verify &#8594; delete」と描いているのに、ステップの記述がそうなっていなければ、それ自体が発見だ。この計画には図がないので、今日は飛ばしてよい。図があるときは、Mermaid のソースではなく、描画された絵を見よう。多くのエディタにプレビュー機能があり、<a href="/ja/view-markdown-on-mac/">「Mac で Markdown を見る方法」</a>と<a href="/ja/vs/markdown-preview-tools/">「他のツールで Markdown を見る場合との比較」</a>で選択肢を紹介している。MarsDawn では、レンダリングされた図がソースの隣にあり（&#8984;2）、図が壊れていればソースとエラーが一緒に表示される。それ自体、コメントに値する。</p>
<p><strong>5. 計画が触れるファイルとシステムを列挙し、頼んでいないことがあれば確認する。</strong>（4 と 5 を合わせて約 1 分）ここでは、ストレージの設定、テンプレート、サーバー上のフォルダ、バケット。そのバケットは誰が読めるのか？ 公開すべきだとは頼んでいない。MarsDawn でエージェントの作業フォルダを開いていれば（「ファイル &#9656; フォルダを開く&#8943;」、&#8679;&#8984;O）、エージェントが書いた新しいファイルは 1 秒ほどでファイルタブに現れ、ヘッダーに git のブランチや worktree の名前が出るので、自分がどのチェックアウトをレビューしているか分かる。</p>
<p><strong>6. フィードバックは「場所・問題・直し方」で、1 行に 1 つの問題だけを書く。</strong>（最後の 1 分）</p>
<pre><code>plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.</code></pre>
<p>行番号のあるエディタなら何でもいい。MarsDawn では、「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）でいまいる場所を <code>plan.md:10</code> の形でコピーでき、「AI 用にコピー」（&#8963;&#8997;&#8984;C）はその下に選択したテキストを付け加える。</p>

<h2>1 分しかないなら</h2>
<p>ステップ 2 をやろう。終わったと思い込んでいるエージェントが見つかるのは、たいていそこだ。</p>

<h2>5 分では足りないとき</h2>
<p>あるステップが正しいかどうか、あなたには判断できないこともある。それがあなたの知識の外にあるからだ。Jess Ou は、LangChain の 2026 年のエージェント解説記事で、2 文でこう言い切っている：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（評価できない判断を、外部に委ねてはいけない。正しい答えを自分が見分けられないなら、エージェントにも見分けられない。）私たちの受け止め方：あるステップを判断できないなら、それは早く承認する理由にはならない。分かる人に聞く理由になる。</p>

<h2>ここで MarsDawn がすること、しないこと</h2>
<p>MarsDawn の中に AI モデルはない。この計画の問題を見つけたりはせず、ステップ 2 や 3 を代わりにやることもない。作業中、ファイルを読みやすく保つだけだ：ステップ 1 にはアウトライン、ステップ 4 には描画された図、ステップ 5 にはファイルタブ、ステップ 6 には行の参照。読んでいる途中でエージェントが計画を修正しても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。</p>
<p>計画が固まり、ほかの人にも見せる必要が出てきたら、<a href="/ja/sharing-exported-pdfs/">「書き出した PDF を共有する」</a>と<a href="/ja/markdown-to-pdf/">「Markdown から PDF へ」</a>が、PDF として渡す方法を扱っている。</p>

<h2>試してみる</h2>
<p>MarsDawn は近日 Mac App Store に登場予定です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>そもそもエージェントの出力がなぜ読みにくいか：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>なぜエージェントはそもそも計画を示すのか：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>エージェントが返すのは計画だけではない：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
</ul>

<h2>出典</h2>
<ul>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou, &#8220;What is an AI agent?,&#8221; LangChain, July 31, 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": "4 つのエージェント設計パターンと、それぞれが返す文書 · MarsDawn",
        "description": "Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。",
        "body": f"""
<section class="intro">
  <h1>4 つのエージェント設計パターンと、それぞれが返す文書</h1>
  <p>2024 年 3 月、Andrew Ng は自身のニュースレター The Batch で、AI エージェントの 4 つの設計パターンを紹介した：reflection、tool use、planning、multi-agent collaboration。これらはふつう、モデルからより良い結果を引き出す方法として、作る側の視点から語られる。この記事は反対側から見る。あなたが使っているエージェントが、このどれかのパターンで作られているなら、フォルダには何が入ってくるのか。まず何を読めばいいのか。</p>
</section>

<div class="summary"><p><strong>4 つのパターンは Andrew Ng のものだ。それぞれがどんな文書を返しがちで、何をチェックすべきかは、私たちの推論だ。彼はそのどちらについても書いておらず、このシリーズで人によるレビューを主張してもいない。</strong></p></div>

<h2>4 つのパターン、手短に</h2>
<p>Ng はこれを「Agentic Design Patterns Part 1」で説明している。手短に言えば：<strong>reflection</strong> はモデルが自分の成果を見直して改善するもの。<strong>tool use</strong> は Web 検索やコード実行などのツールを呼べるようにするもの。<strong>planning</strong> はモデルが多段階の計画を立てて実行するもの。<strong>multi-agent collaboration</strong> は複数のエージェントが作業を分担し、議論するものだ。</p>
<p>Part 1 で彼は、コーディングのベンチマーク HumanEval を使い、複数の研究グループの結果をチームでまとめた数字で効果を示している：「GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.」（GPT-3.5 の zero-shot での正答率は 48.1%、GPT-4 の zero-shot はもう少し良く 67.0%。しかし、GPT-3.5 から GPT-4 への向上は、反復的なエージェントワークフローを組み込むことに比べれば見劣りする。実際、エージェントのループに包むと、GPT-3.5 は最大で 95.1% に達する。）これらの数字は 1 つのコーディングベンチマークについてのもので、95.1% は最良のケース（「up to」＝最大で）だ。エージェントのワークフローが出力を改善しうることは示しているが、誰がそれを確認するかについては何も語っていない。</p>
<p><strong>ここから先の、文書とチェック項目は、私たちの解釈であって Ng のものではない。</strong>実際のエージェントは複数のパターンを混ぜて使うことも多い。1 つのコーディングエージェントが、同じセッションの中で計画を立て、ツールを実行し、自分の成果を見直すこともあるので、この 4 種類のファイルを一度に受け取ることもよくある。</p>

<h2>1. Reflection：すでに自分で見直した草稿</h2>
<p>Ng が reflection について書いた記事は、これを、本来は人が与えるフィードバックを自動化するものとして描いている：「What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?」（批判的なフィードバックを与えるステップを自動化し、モデルが自分の出力を自動的に批評して回答を改善するとしたらどうだろうか？）</p>
<p><strong>返ってきがちなもの：</strong>修正済みの文書。自己レビューのセクションや、「エッジケースは再確認済み」のような一文が付いていることもある。</p>
<p><strong>チェックすべきこと：</strong>結果を、エージェント自身の批評ではなく、<em>あなた</em>の依頼内容と照らし合わせる。自己レビューはそれ自体の仕方で間違うことがある。Chip Huyen：「An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it&#8217;s accomplished a task when it hasn&#8217;t.」（計画の失敗の興味深い一形態は、reflection の誤りによって引き起こされる。エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）Lilian Weng は、2023 年 6 月、当時 OpenAI に在籍しながら、ブログ Lil’Log で当時のモデルについてこう書いている：「The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.」（専門知識の不足により、LLM は自分の欠陥に気づかず、タスク結果の正しさをうまく判断できないことがある。）（彼女が説明していた研究では、LLM による結果の評価と、人間の専門家による評価が一致していなかった。）「検証済み」と書かれていたら、1 つは自分で確認しよう。</p>

<h2>2. Tool use：何を実行したかの報告</h2>
<p><strong>返ってきがちなもの：</strong>エージェントが何を実行または検索し、何が返ってきたかのまとめ。「テストスイートを実行：全て合格。」結果の表。見つかったリンク。</p>
<p>Anthropic のガイドは、ツールの結果をエージェント自身のチェックとして描いている：「During execution, it's crucial for the agents to gain &#8220;ground truth&#8221; from the environment at each step (such as tool call results or code execution) to assess its progress.」（実行中、エージェントが自分の進捗を評価するには、各ステップで環境から「ground truth」（ツール呼び出しの結果やコード実行の結果など）を得ることが重要だ。）そのチェックはエージェントの内部で起きる。あなたのもとに届くのは、エージェントによるその語り直しだ。</p>
<p><strong>チェックすべきこと：</strong>それぞれの主張が、実際に見える出力までたどれるか。まとめの中の 1 つの数字を、本当の出力と照合する。リンクを 1 つ開いてみる。</p>

<h2>3. Planning：<code>plan.md</code></h2>
<p><strong>返ってきがちなもの：</strong>計画、仕様書、エージェントが進めながらチェックしていくタスクリスト。</p>
<p>Ng は Part 4 で、このパターンについて率直に語っている：</p>
<blockquote><p>&#8220;On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications&#8217; performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.&#8221;</p></blockquote>
<p>（一方で、計画は非常に強力な能力だ。他方で、予測しにくい結果につながる。私の経験では、Reflection と Tool Use という設計パターンは信頼できる形で動かし、アプリケーションの性能を上げられる一方、Planning はまだ成熟度の低い技術で、それが何をするか事前に予測するのは難しいと感じている。）</p>
<p>楽観的でもある：「But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.」（しかしこの分野は急速に進化し続けていて、計画の能力は早く向上すると確信している。）</p>
<p><strong>チェックすべきこと：</strong>実行前の計画を、<a href="/ja/reviewing-agent-plans/">「5 分でのレビュー」</a>の方法で見る：形、主張を 1 つ、取り消せないステップ、図、範囲。エージェントが途中で計画を書き換えたら、あなたが承認したバージョンと比較する。git を使っているなら、<code>git diff plan.md</code> で何が変わったか分かる。MarsDawn では、アウトラインタブが長い計画の形を示し、書き換えられた計画は、あなた自身に未保存の編集がなければ、読んでいた位置を保ったまま再読み込みされる。</p>

<h2>4. Multi-agent collaboration：複数のファイル、複数の書き手</h2>
<p><strong>返ってきがちなもの：</strong>あるエージェントによる仕様書、別のエージェントによる実装メモ、さらに別のエージェントによるレビュー、そしてそれらの間でやり取りされる要約。それぞれが自分のブランチや worktree で作業していることもある。</p>
<p><strong>チェックすべきこと：</strong>引き継ぎの部分。あるエージェントが別のエージェントの成果をまとめるとき、伝わらなかった要件がないか探す。食い違う 2 つのファイルを見つけたら、誰かがそれを土台に作業を進める前に、どちらを正とするか決める。MarsDawn では、「ファイル &#9656; フォルダを開く&#8943;」（&#8679;&#8984;O）で共有フォルダを開く。エージェントが書いた新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出るので、別々のブランチにある同名のファイルを開いた 2 つのウィンドウを見間違えることもない。結果を Markdown を読まない人に渡す必要があるときは、<a href="/ja/sharing-exported-pdfs/">「書き出した PDF を共有する」</a>が、その手順を扱っている。</p>

<h2>ひと目で見る</h2>
<table>
<thead><tr><th>パターン（Ng）</th><th>返ってきがちなもの（私たちの推論）</th><th>まず読むべきところ（私たちの提案）</th></tr></thead>
<tbody>
<tr><td>Reflection</td><td>修正済みの草稿。自己レビュー付きのことも</td><td>自分自身の依頼内容と照らし合わせる。「検証済み」を 1 つ確認</td></tr>
<tr><td>Tool use</td><td>何を実行し、何が返ってきたかの報告</td><td>主張を 1 つ、実際の出力までたどる</td></tr>
<tr><td>Planning</td><td><code>plan.md</code>、仕様書、タスクリスト</td><td>実行前の 5 分レビュー</td></tr>
<tr><td>Multi-agent collaboration</td><td>複数のエージェントによる複数のファイル。複数のブランチにまたがることも</td><td>引き継ぎの部分と、どれが正か</td></tr>
</tbody>
</table>
<p>ここに引用した著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。MarsDawn の中に AI モデルはない：どのパターンがそのファイルを生んだかを知ることはなく、これらのチェックを代わりにやることもない。ファイルを、あなたがチェックしている間、読みやすく保つだけだ。</p>

<h2>試してみる</h2>
<p>MarsDawn は近日 Mac App Store に登場予定です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。詳しくは<a href="/ja/markdown-to-pdf/">「Markdown から PDF へ」</a>を見てください。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>エージェントの出力がなぜ読みにくいか、そのチェックリスト：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>計画のチェックを、完全な形で：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>透明性があなたに求めること、求めないこと：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 1,&#8221; The Batch, March 20, 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 2, Reflection,&#8221; The Batch, March 27, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 4, Planning,&#8221; The Batch, April 10, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng, &#8220;LLM Powered Autonomous Agents,&#8221; Lil&#8217;Log, June 23, 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a>（2026-09-26 時点のオンライン版から引用）</li>
</ul>
""",
    }

    pages['changelog'] = {
        "title": '更新履歴 · MarsDawn',
        "description": '無料の marsdawn コマンドラインツールの変更点です。',
        "body": f"""
<section class="intro">
  <h1>更新履歴</h1>
  <p>無料の marsdawn コマンドラインツールの変更点です。Mac App Store 版の MarsDawn は、そのバージョン自身について書くことがある場合だけ、ここに載せます。0.5.1 より前のバージョンは載せていません。</p>
</section>

<h2>marsdawn 0.5.1</h2>
<p>2026年9月19日。PDF 書き出しと、コマンドラインからファイルを開くこと。</p>
<ul>
  <li>書き出した PDF のテキストレイヤーを、中国語、日本語、韓国語について修正しました。</li>
  <li><code>marsdawn open --background</code> はファイルを開きますが、MarsDawn を前面には出しません。</li>
  <li><code>marsdawn open</code> にフォルダを渡せます。Mac App Store のアプリはまだフォルダを表示できないので、このオプションは、それができるアプリを待ちます。</li>
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
