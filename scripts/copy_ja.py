"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': 'プライバシーポリシー', 'support': 'サポート', 'cli': 'コマンドライン', 'agents': 'AI エージェント向け marsdawn', 'using_cli': 'CLI の使い方', 'markdown-to-pdf': 'Markdown から PDF へ', 'skill': 'エージェント用スキル', 'view-markdown-on-mac': 'Mac で Markdown を見る', 'vs-macmd-viewer': 'MacMD Viewer と MarsDawn', 'updated': f"最終更新日：{k.UPDATED}", 'tagline': 'エージェントが書いた Markdown を読む。', 'footer_store': 'MarsDawn は Mac App Store で近日公開予定です。', 'more': 'その他', 'yours': 'あなたの文章は Mac に残ります', 'pay-once': '無料で試して、一度だけ購入', 'pdf': 'PDF 書き出し', 'native': 'Mac アプリ', 'limits': 'MarsDawn ができないこと'}
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
            "alt": 'MarsDawn が Classic テーマで文書を表示し、プレビューがウインドウいっぱいに広がっている。',
            "callouts": ['あなたの Mac 上のファイルで、選んだ場所に保存されます。', 'ツールバーにあるのはテーマとレイアウトだけで、サインインするものは何もありません。'],
        },
        'pay-once': {
            "alt": 'MarsDawn が Vivid テーマで、左に Markdown のソース、右にレンダリングされたページを表示している。',
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
    pages['index'] = {
        "title": 'MarsDawn：ライブプレビュー搭載、Mac 向け Markdown エディタ',
        "description": 'ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向け Markdown エディタ。AI エージェントが書いた文章を読むために作られました。Mac App Store で近日公開予定です。',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">AI ワークフローのために作られました</p>
  <h1>エージェントが書いた Markdown を、じっくり読む場所。</h1>
  <p>AI エージェントが Markdown を書きます。あなたは MarsDawn でそれを確認します。ソースとレンダリングされたページを並べて見て、修正を伝えます。</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">このループ</h2>
<ol class="loop-steps">
  <li><strong>エージェントが書く。</strong>あなたのコーディングエージェントやライティングアシスタントが Markdown の下書きを作ります。README、仕様書、メモなど。</li>
  <li><strong>MarsDawn で確認する。</strong>ファイルを開き、Mermaid 図やハイライトされたコードとともにレンダリングされたページを、ソースの隣で読みます。</li>
  <li><strong>エージェントが修正する。</strong>変更を依頼します。修正されたファイルを開き、同じように読みます。</li>
</ol>
<p>エージェントは MarsDawn を直接操作することもできます。無料の <a href="/ja/cli/">marsdawn</a> コマンドラインツールは、確認用にファイルを開いたり PDF を書き出したりでき、スクリプト向けの JSON 出力にも対応しています。詳細は<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>をご覧ください。</p>
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
<ul>
  <li>MarsDawn は Mac App Store から無料でダウンロードできます。</li>
  <li>トライアルを始めると、14日間はすべての機能が使えます。すべてのテーマとレイアウト、PDF 書き出しと印刷、クイックルック、Siri とショートカットのアクションです。</li>
  <li>その後も使い続けるには、USD 4.99 の一度きりの購入でロックを解除します。App 内課金であり、サブスクリプションではないので、自動更新もあとから請求されることもありません。</li>
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
<ul>
  <li>ソース、分割、プレビューの3つのレイアウトを、キー1つで切り替え（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>2つのペインは一緒にスクロールするので、編集中の段落が常に見えています。</li>
  <li>エディタの Markdown シンタックスハイライトは、プレビューのテーマに合わせられます。</li>
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
<ul>
  <li><strong>同期：</strong>MarsDawn は文書を同期しません。文書は保存した場所にそのまま残るので、別の Mac でも使いたい場合は、すでに同期しているフォルダに保存してください。</li>
  <li><strong>iPhone と iPad：</strong>これらの端末向けアプリはありません。MarsDawn は Mac 専用です。</li>
  <li><strong>プラグイン：</strong>MarsDawn にプラグインや拡張機能はありません。</li>
  <li><strong>共有：</strong>アカウントも共同編集もありません。MarsDawn は自分の Mac で使う一人のためのものです。</li>
  <li><strong>編集：</strong>左に Markdown を書き、右でページを読みます。ページ自体は編集できません。</li>
  <li><strong>形式：</strong>MarsDawn は PDF の書き出しと印刷に対応していますが、Word ファイルへの書き出しはできません。</li>
  <li><strong>テーマ：</strong>Dawn、Classic、Modern、Vivid の4種類が組み込まれており、それぞれライトとダークがあります。他のテーマを追加することはできません。</li>
  <li><strong>その他のファイル：</strong>プレーンテキストファイルと PDF は読み取り専用で開きます。</li>
  <li><strong>トライアル終了後：</strong>14日間のトライアルが終わってロックを解除しなければ、MarsDawn で文書を読んだり編集したりできません。内容が覆われた状態で開きます。ファイルはそのまま残り、クイックルックでは引き続き表示され、無料のコマンドラインツールも引き続き書き出せます。</li>
  <li><strong>システム：</strong>MarsDawn には macOS 26 以降が必要です。</li>
</ul>
""",
    }
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
        "body": f"""
<section class="intro">
  <h1>プライバシーポリシー</h1>
  <p>macOS 向け Markdown エディタ、MarsDawn がどのようにあなたの情報を扱うか。</p>
  <p class="updated">最終更新日：{k.PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn はあなたに関するデータを一切収集しません。</strong>アカウントも、アナリティクスも、広告も、トラッキングもありません。文書と設定はあなたの Mac 上に残ります。</p></div>

<h2>あなたの Mac に残るもの</h2>
<ul>
  <li><strong>あなたの文書。</strong>MarsDawn は、あなたが開いた、保存した、または選んだファイルとフォルダだけを読み書きします。App がそれらをどこかにアップロードすることはありません。</li>
  <li><strong>あなたの設定。</strong>外観、プレビューのテーマ、ウインドウのレイアウト、画像の設定は、あなたの Mac 上にある App 自身の環境設定に保存されます。</li>
  <li><strong>許可したフォルダへのアクセス。</strong>フォルダ内の画像やページファイルを MarsDawn に表示させたり、メモフォルダを選んだりすると、App はそのフォルダを再び開けるように macOS のブックマークを保持します。サイドバーで開いたフォルダは、ウインドウが開いている間だけでなく、設定で削除するまで MarsDawn から読み書き可能な状態が続きます。フォルダはいつでも MarsDawn › 設定で削除できます。</li>
</ul>

<h2>MarsDawn がインターネットを使うとき</h2>
<p>MarsDawn は完全にオフラインで動作します。インターネットに接続するのは<strong>あなたが選んだときだけ</strong>、ウェブを参照する文書に対してです。</p>
<ul>
  <li><strong>Markdown 文書。</strong>ウェブ画像はデフォルトでブロックされています。プレビューで<em>イメージを読み込む</em>をクリックするか、設定で<em>リモートイメージを自動的に読み込む</em>をオンにしたときだけ読み込まれます。Markdown 文書が参照するそれ以外のものは、ウェブから読み込まれません。</li>
  <li><strong>HTML 文書。</strong>HTML 文書は静的な状態で開きます。コードは実行されず、ウェブから何も読み込まれません。文書に実行され得るコードが含まれる場合、その文書について<em>表示 › この書類を実行</em>を選ぶことができます。すると、その文書自身のコードは、あなたが停止するか、文書が再読み込みされるか、ウインドウを閉じるまで実行され続けます。この選択が記憶されることはなく、設定項目でもありません。実行中、文書はネットワーク経由でデータを送信でき、自身のフォルダとその中のフォルダにある画像、スタイルシート、フォント、メディアを読み取れます。ウェブからダウンロードされたコードが実行されることはありません。</li>
</ul>
<p>MarsDawn は https 経由でのみウェブコンテンツを読み込みます。http のみのアドレスは、どの設定でも読み込まれることはなく、MarsDawn がそれを https に書き換えることもありません。Markdown 文書では、プレビューにその代わりのプレースホルダーが表示されます。</p>
<p>ウェブコンテンツを読み込むとき、あなたの Mac はそれを配信するサーバーへ直接リクエストを送ります。他のウェブリクエストと同様に、これによってそれらのサーバーはあなたの IP アドレスとリクエストされた内容を知ることができます。MarsDawn の開発者はこれらの情報を一切受け取りません。</p>
<p>プレビュー内でクリックしたリンクは、デフォルトのウェブブラウザで、そのブラウザ自体のプライバシー方針に従って開きます。音声と動画が自動的に再生されることはありません。</p>

<h2>Siri、ショートカット、Spotlight</h2>
<p>MarsDawn は Siri、ショートカット App、Spotlight 向けに、文書の作成やメモの追加などのアクションを提供します。これらを使用すると、入力したテキストはあなたの Mac 上の MarsDawn に渡され、そのアクションが指定する場所（新規文書、または選んだメモフォルダ内の <code>Inbox.md</code>）にのみ保存されます。Siri に話した音声は、<a href="https://www.apple.com/legal/privacy/">Apple のプライバシーポリシー</a>のもとで Apple が処理します。</p>

<h2>書き出しと印刷</h2>
<p>PDF の書き出しと印刷は、あなたの Mac 上で行われます。PDF は選んだ場所に保存されます。印刷は macOS を通じて選んだプリンタに送られます。</p>

<h2>marsdawn コマンドラインツール</h2>
<p>別途配布される、使うかどうかを選べる <code>marsdawn</code> コマンドラインツールも、完全にあなたの Mac 上で動作します。指定した Markdown ファイルを読み込み、要求された PDF を書き出します。<code>--allow-remote-images</code> を指定したときだけウェブ画像を読み込みます。</p>

<h2>子ども</h2>
<p>MarsDawn は、子どもを含め、誰からもデータを収集しません。</p>

<h2>購入</h2>
<p>MarsDawn は Mac App Store を通じて販売されます。購入は Apple 自身の規約のもとで処理され、開発者があなたの支払い情報を受け取ることはありません。</p>

<h2>このポリシーの変更</h2>
<p>MarsDawn がデータの扱い方を変える場合、そのバージョンがリリースされる前にこのページが更新され、冒頭の日付も変わります。</p>

<h2>お問い合わせ</h2>
<p>プライバシーに関するご質問：<a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
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
<p>もしそのファイルを AI エージェントが書いたなら、これはまさに MarsDawn が想定しているループです。エージェントが書き、あなたがレンダリングされたページを読み、エージェントが修正します。<a href="/ja/">ホームページ</a>と、エージェントにファイルを開かせる方法については<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>をご覧ください。</p>
<h2>次に</h2>
<ul>
  <li>コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>MarsDawn ができないこと：<a href="/ja/limits/">一覧はこちら</a>。</li>
</ul>
""",
    }
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
<ul>
  <li><strong>編集：</strong>MacMD Viewer は設計上、読み取り専用です。MarsDawn はソースを編集しながらその場でレンダリングするので、入力すると変更が表示されます。</li>
  <li><strong>プレビューのテーマ：</strong>MacMD Viewer には12種類の文書テーマがあります。MarsDawn は Dawn、Classic、Modern、Vivid の4種類で、それぞれライトとダークのパレットがあります。</li>
  <li><strong>図と数式：</strong>どちらも Mermaid 図をレンダリングし、コードをハイライトします。MarsDawn は KaTeX の数式もレンダリングしますが、MacMD Viewer 自身の紹介には数式のレンダリングについて記載がありません。</li>
  <li><strong>Finder 連携：</strong>どちらもクイックルック拡張機能を追加しており、Finder で <code>.md</code> ファイルを選んでスペースキーを押すとレンダリングされたページが表示されます。</li>
  <li><strong>PDF と印刷：</strong>どちらもレンダリングされたページを PDF として書き出したり印刷したりできます。</li>
  <li><strong>システム要件：</strong>MacMD Viewer は macOS 14（Sonoma）以降が必要です。MarsDawn は macOS 26（Tahoe）以降が必要です。</li>
  <li><strong>言語：</strong>MarsDawn のインターフェースは{k.APP_UI_LANGUAGES}に対応しています。MacMD Viewer 自身の資料は UI の言語を明記していないため、このページではその点を比較していません。</li>
</ul>
<h2>価格と購入方法</h2>
<ul>
  <li><strong>購入場所：</strong>MacMD Viewer は自社サイトから直接ダウンロードでき、Homebrew と Setapp にもありますが、Mac App Store にはありません。MarsDawn は Mac App Store のみです。</li>
  <li><strong>価格：</strong>MacMD Viewer は1台の Mac につき一度きり USD 19.99（3台パックやボリュームパックはより高額）。MarsDawn は無料でダウンロードでき、その後 USD 4.99 の一度きりのロック解除です。</li>
  <li><strong>先に試す：</strong>MacMD Viewer には無料トライアルはなく、直接購入には代わりに14日間の返金保証が付いています。MarsDawn は支払う前に14日間のトライアルを提供します。</li>
  <li><strong>返金と更新：</strong>MacMD Viewer の返金と更新は自社サイトで処理されます。MarsDawn の購入は Apple を通じて行われるため、返金と更新は Apple の標準プロセスを使います。</li>
  <li><strong>アカウント：</strong>どちらのアプリも利用にアカウントは不要です。</li>
</ul>
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
  <li>MarsDawn 1.0 はファイルを開きますが、まだその行にジャンプしません。</li>
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
  <li>MarsDawn 1.0 はまだ <code>open</code> が指定した行にジャンプしません。ファイルは先頭から開きます。</li>
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
  <li>行の指定は marsdawn 0.3.0 で追加されました。MarsDawn 1.0 はファイルを開きますが、まだその行にジャンプしません。</li>
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
