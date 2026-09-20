"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': 'プライバシーポリシー', 'support': 'サポート', 'cli': 'コマンドライン', 'agents': 'AI エージェント向け marsdawn', 'using_cli': 'CLI の使い方', 'markdown-to-pdf': 'Markdown から PDF へ', 'skill': 'エージェント用スキル', 'view-markdown-on-mac': 'Mac で Markdown を見る', 'vs-macmd-viewer': 'MacMD Viewer と MarsDawn', 'updated': f"最終更新日：{k.UPDATED}", 'tagline': 'エージェントが書いた Markdown を読む。', 'footer_store': 'MarsDawn は Mac App Store で近日公開予定です。', 'more': 'その他', 'yours': 'あなたの文章は Mac に残ります', 'pay-once': '無料で試して、一度だけ購入', 'pdf': 'PDF 書き出し', 'native': 'Mac アプリ', 'limits': 'MarsDawn ができないこと', 'mcp': 'MCP サーバー', 'token-efficient-review': 'トークンを使わないレビュー', 'vs-markdown-preview-tools': '他のツールで Markdown を見る場合との比較', 'themes': 'プレビューテーマと PDF 書き出し', 'sharing-exported-pdfs': '書き出した PDF を共有する', 'reviewing-ai-output': 'AI の出力を人が確認する理由'}
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
    pages['index'] = {
        "title": 'MarsDawn：Mac 向けの Markdown エディタ、リアルタイムプレビュー付き',
        "description": 'リアルタイムプレビュー、Mermaid 図、PDF 書き出しを備えたネイティブの Mac 向け Markdown エディタ。AI エージェントが書いた文章を読むために作られました。Mac App Store に近日公開予定。',
        "intro": """
<section class="intro hero">
  <p class="kicker">AI ワークフローのために作った</p>
  <h1>エージェントが書いた Markdown を、じっくり読む場所。</h1>
  <p>AI エージェントが Markdown を書き、あなたは MarsDawn でソースとレンダリングされたページを並べて読み、修正を伝えて送り返します。</p>
</section>
""",
        "body": """
<h2 class="loop-title">ループ</h2>
<ol class="loop-steps">
  <li><strong>エージェントが書く。</strong>あなたのコーディングエージェントや文章作成アシスタントが、README や仕様書、メモなどの Markdown を書きます。</li>
  <li><strong>MarsDawn で読む。</strong>ファイルを開き、Mermaid 図やハイライトされたコードとともに、レンダリングされたページをソースの隣で読みます。</li>
  <li><strong>エージェントが直す。</strong>修正を頼み、直った後のファイルを開いて、同じように読みます。</li>
</ol>
<p>エージェントは MarsDawn を直接操作できます。無料の <a href="/ja/cli/">marsdawn</a> コマンドラインツールが、レビュー用にファイルを開いたり PDF を書き出したりします。スクリプト向けの JSON 出力も用意されています。詳細は<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>をご覧ください。</p>
""",
    }
    pages['yours'] = {
        "title": 'アカウントもクラウドも不要な Mac 向け Markdown エディタ · MarsDawn',
        "description": 'MarsDawn にはアカウントも同期もクラウドもありません。あなたの Markdown 文書は、選んだファイルとフォルダの中で、あなたの Mac に留まります。',
        "intro": """
<section class="intro">
  <h1>あなたの文章は、あなたの Mac に残ります。</h1>
  <p>MarsDawn にはアカウントも同期もクラウドもありません。ファイルを開き、あなたが書き、選んだ場所に保存します。</p>
</section>
""",
        "body": """
<h2>これが意味すること</h2>
<ul>
  <li>登録もサインインも必要なアカウントはありません。</li>
  <li>クラウドへの同期は一切ありません。文書は保存した場所にそのまま残ります。</li>
  <li>何も追跡されません。MarsDawn はあなたに関するデータを収集せず、App Store のプライバシーラベルは「データは収集されません」です。</li>
  <li>ウェブ画像はあなたが読み込みを選ぶまでブロックされたままなので、文書を開いただけでサーバーに読んだことが伝わることはありません。読み込むときも https のみです。</li>
  <li>ローカルの画像は、そのフォルダへのアクセスを許可すればプレビューに表示されます。</li>
</ul>
<p>詳細は<a href="/ja/privacy/">プライバシーポリシー</a>をご覧ください。</p>
""",
    }
    pages['pay-once'] = {
        "title": '無料で試して、一度だけ購入 · MarsDawn',
        "description": 'MarsDawn は無料でダウンロードできます。14 日間すべての機能を試したあとは、USD 4.99 を一度だけ支払えば使い続けられます。サブスクリプションもアカウントも不要です。',
        "intro": """
<section class="intro">
  <h1>まず全部試して、それから一度だけ購入。</h1>
  <p>MarsDawn は無料でダウンロードできます。14 日間の試用を始めれば、すべての機能が使えます。その後も使い続けるには、USD 4.99 を一度だけ支払って解除してください。サブスクリプションもアカウントもありません。</p>
</section>
""",
        "body": """
<h2>仕組み</h2>
<ul>
  <li>MarsDawn は Mac App Store から無料でダウンロードできます。</li>
  <li>試用を始めると、14 日間はすべてが使えます。すべてのテーマとレイアウト、PDF 書き出しと印刷、クイックルック、Siri とショートカットのアクションも含みます。</li>
  <li>その後も使い続けるには、USD 4.99 を一度だけ支払って解除してください。App 内課金であり、サブスクリプションではないので、自動更新も後からの請求もありません。</li>
  <li>試用そのものにも料金はかかりません。試用が終わっても、解除を選ばない限り何も購入されません。</li>
  <li>アカウントはありません。MarsDawn が作成を求めることは一切ありません。</li>
</ul>
<h2>解除しない場合</h2>
<ul>
  <li>14 日後、解除するまでは MarsDawn で文書を読む、編集する、書き出す、印刷することができません。文書は開きますが、内容は覆われます。</li>
  <li>ファイル自体は変わりません。あなたの Mac 上にある普通のファイルのままで、Finder のクイックルックでも引き続き表示されます。</li>
  <li>無料の<a href="/ja/cli/"><code>marsdawn</code> コマンドラインツール</a>は、試用期間にかかわらず引き続き PDF に書き出せます。</li>
  <li>試用が終わったときに MarsDawn で文書を開いていても、入力した文章は失われません。「ファイル」▸「別名で保存…」で保存できます。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Mac で Markdown を PDF に書き出す、図表も込みで · MarsDawn',
        "description": 'Mac 上で Markdown を PDF に書き出す、または印刷する。Mermaid 図とハイライトされたコードも含まれます。改ページは短いコードブロックや表を分断しません。',
        "intro": """
<section class="intro">
  <h1>PDF は、あなたが書いたページそのままの見た目になります。</h1>
  <p>テーマのライトカラーで PDF に書き出す、または印刷します。図やハイライトされたコードもそのまま反映され、改ページはひとまとまりの内容を分断しません。</p>
</section>
""",
        "body": """
<h2>これが意味すること</h2>
<ul>
  <li>Mermaid 図は PDF に描き込まれます。</li>
  <li>コードブロックはハイライトを保ちます。</li>
  <li>改ページは、見出しをページの下端に残したり、コード、表、図を分断したりしないよう配慮されます。</li>
  <li>どのレイアウトでも書き出せます。ソースだけを表示している状態でも構いません。</li>
</ul>
<p>無料の<a href="/ja/cli/">marsdawn コマンドラインツール</a>も同じ書き出しエンジンを使うので、スクリプトや AI エージェントも同じ PDF を得られます。</p>
""",
    }
    pages['native'] = {
        "title": 'Mac ネイティブの Markdown アプリ：タブとクイックルック · MarsDawn',
        "description": '本物の Mac アプリとしての Markdown エディタ：ネイティブのウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。',
        "intro": """
<section class="intro">
  <h1>Mac そのものの部品で作られています。</h1>
  <p>ウインドウ、タブ、メニュー、テキストエディタは Mac 自身のものです。レンダリングされたページは、Safari と同じ WebKit エンジンで描画されます。</p>
</section>
""",
        "body": f"""
<h2>これが意味すること</h2>
<ul>
  <li>ソース、分割、プレビューの3つのレイアウトを、ワンキーで切り替えられます（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>2つのペインは連動してスクロールするので、編集中の段落が常に見えています。</li>
  <li>エディタには Markdown のシンタックスハイライトがあり、プレビューのテーマに合わせて色が変わります。</li>
  <li>ネイティブのウインドウ、タブ、自動保存、バージョン履歴。</li>
  <li>クイックルック：Finder で Markdown ファイルを選んで空白キーを押せば、図も含めてプレビューできます。</li>
  <li>Siri とショートカット：テンプレートから新規文書を作る、メモの受信箱に一行追加する、最近使った文書を開き直す、といった操作ができます。</li>
  <li>{k.APP_UI_LANGUAGES}に対応しています。</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'MarsDawn ができないこと · MarsDawn',
        "description": '同期なし、iPhone・iPad アプリなし、プラグインなし、アカウント不要。内蔵テーマは4種類。購入前に知っておきたいこと。',
        "intro": """
<section class="intro">
  <h1>MarsDawn ができないこと。</h1>
  <p>いくつかの機能は、意図的に含まれていません。必要な機能がここにあるなら、購入後より今知っておくほうがいいはずです。</p>
</section>
""",
        "body": """
<h2>含まれていないもの</h2>
<ul>
  <li><strong>同期：</strong>MarsDawn は文書を同期しません。保存した場所にそのまま残るので、別の Mac で使うには、もともと同期しているフォルダに置いてください。</li>
  <li><strong>iPhone と iPad：</strong>それらのための App はありません。MarsDawn は Mac 専用です。</li>
  <li><strong>プラグイン：</strong>MarsDawn にはプラグインも拡張機能もありません。</li>
  <li><strong>共有：</strong>アカウントも共同編集もありません。MarsDawn は、ひとりの人が自分の Mac で使うために作られています。</li>
  <li><strong>編集：</strong>左側で Markdown を書き、右側でページを読みます。ページ自体を編集することはできません。</li>
  <li><strong>形式：</strong>MarsDawn は PDF への書き出しと印刷に対応していますが、Word ファイルへの書き出しはできません。</li>
  <li><strong>テーマ：</strong>付属するのは Dawn、Classic、Modern、Vivid で、それぞれライトとダークがあります。今のところ他のテーマを追加することはできません。今後の計画は<a href="/ja/themes/">プレビューテーマと PDF 書き出し</a>をご覧ください。</li>
  <li><strong>その他のファイル：</strong>プレーンテキストファイルと PDF は読み取り専用で開きます。</li>
  <li><strong>試用期間後：</strong>14 日間の試用が終わっても解除しない場合、MarsDawn で文書を読んだり編集したりできません。文書は開きますが、内容は覆われます。ファイル自体はそのまま残り、クイックルックでも引き続き見られ、無料のコマンドラインツールも引き続き書き出せます。</li>
  <li><strong>システム：</strong>MarsDawn には macOS 26 以降が必要です。</li>
</ul>
""",
    }
    pages['view-markdown-on-mac'] = {
        "title": 'Mac で Markdown ファイルを見る方法 · MarsDawn',
        "description": '.md ファイルは、整形用の記号が入ったプレーンテキストです。Mac 上でレンダリングされた見た目を読む方法：今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store に近日公開予定の MarsDawn アプリで読む方法。',
        "body": f"""
<section class="intro">
  <h1>Mac で、Markdown ファイルを見る方法。</h1>
  <p><code>.md</code> ファイルはプレーンテキストです。見出しや太字、表、図は記号として書かれています。見出しは <code>#</code>、太字は前後を <code>**</code> で囲み、表は縦棒の記号、図は <code>mermaid</code> のコードブロックです。プレーンテキストエディタで開くと、これらの記号がそのまま見えます。著者が意図した通りのページとして読むには、何かがそれをレンダリングする必要があります。</p>
</section>
<h2>今すぐ、無料で：PDF にする</h2>
<p>無料の <code>marsdawn</code> コマンドラインツールが、Markdown ファイルを PDF にレンダリングします。どんな Mac でも開けます。表、数式、Mermaid 図、ハイライトされたコードもレンダリングされ、他に何もインストールする必要はありません。MarsDawn アプリすら不要です。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> は Markdown ファイルの隣に <code>notes.pdf</code> を書き出し、<code>open</code> は PDF ビューアでそれを表示します。macOS 15 以降が必要です。実際に書き出したページを使った完全な手順は<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>にあります。</p>
<h2>近日公開：MarsDawn で読む</h2>
<p>MarsDawn は Mac 向けの Markdown エディタで、Mac App Store に近日公開予定です。<code>.md</code> ファイルを開くと、レンダリングされたページがソースの隣に表示されます。</p>
<ul>
  <li>入力するとプレビューが更新され、2つのペインは一緒にスクロールします。</li>
  <li>Mermaid のフローチャートやシーケンス図はプレビュー内に描画され、コードブロックもハイライトされます。</li>
  <li>Finder で Markdown ファイルを選んで空白キーを押せば、図も含めてクイックルックでプレビューできます。</li>
  <li>何かを直したくなったら、ソースはすぐそこにあります。MarsDawn はビューアだけでなく、エディタでもあります。</li>
</ul>
<p>AI エージェントがそのファイルを書いたなら、これはまさに MarsDawn が想定しているループです。エージェントが書き、あなたがレンダリングされたページを読み、エージェントが直します。<a href="/ja/">ホームページ</a>をご覧ください。エージェントに代わりにファイルを開かせたい場合は<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>もどうぞ。</p>
<h2>次に</h2>
<ul>
  <li>コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>MarsDawn ができないこと：<a href="/ja/limits/">その一覧</a>。</li>
  <li>VS Code やブラウザ、Claude Desktop で Markdown を読む場合との比較：<a href="/ja/vs/markdown-preview-tools/">比較はこちら</a>。</li>
</ul>
""",
    }
    _plan_en = '# Plan: faster exports\n\nAn agent wrote this plan. You review it, then turn it into a PDF.\n\n## Steps\n\n| Step | Owner | Status |\n|------|-------|--------|\n| Measure the slow pages | Agent | Done |\n| Cache rendered diagrams | Agent | In review |\n\nThe target is $t < 2\\,\\text{s}$ for a 50-page document:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Draft --> Review --> Ship\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    pages['markdown-to-pdf'] = {
        "title": 'コマンドラインで Markdown を PDF に変換する（Mac）· MarsDawn',
        "description": '無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールし、コマンドを一つ実行するだけ：表、数式、Mermaid、コードに対応。',
        "body": f"""
<section class="intro">
  <h1>コマンドラインで、Mac 上の Markdown を PDF に変換する。</h1>
  <p>無料の <code>marsdawn</code> ツールは、コマンド一つで Markdown ファイルを PDF に変換します。表、数式、Mermaid 図、ハイライトされたコードも、ソースで読めるとおりに出力され、MarsDawn アプリを含め、他に何もインストールする必要はありません。</p>
</section>
<h2>インストールする</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Apple シリコンの Mac では、Homebrew が数秒でビルド済みのコピーをインストールします。Intel Mac では代わりにソースからビルドするため数分かかり、Xcode 26 以降が必要です。macOS 15 以降で動作し、<code>marsdawn --version</code> でインストールされたバージョンが表示されます。</p>
<h2>文書を保存する</h2>
<p><code>plan.md</code> という名前のファイルに、次の内容を貼り付けてください：</p>
<pre><code>{k.xml_escape(_plan_en)}</code></pre>
<h2>書き出す</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>ソースの隣に <code>plan.pdf</code> を書き出し、保存先を表示します：</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>これは実際に <code>marsdawn</code> 0.5.0 を実行して得られたそのページです：</p>
<p><img class="pdf-page" src="/assets/cli/plan-en.png" alt="書き出された PDF：見出し、ステップの表、インラインとディスプレイ数式、Draft・Review・Ship の図、そしてハイライトされた Swift の一行。" width="989" height="930"></p>
<h2>テーマ、紙のサイズ、ファイル名を選ぶ</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>：dawn、classic、modern、vivid のいずれか、テーマのライトカラーを使います。指定しない場合、<code>export</code> はまず <code>$MARSDAWN_THEME</code> を、それもなければ dawn を使います。</li>
  <li><code>--paper</code>：a4 または letter。デフォルトは a4 です。</li>
  <li><code>-o</code>：PDF の書き出し先。指定しなければソースの隣に書き出されます。</li>
  <li><code>--allow-remote-images</code>：書き出し中にウェブから画像を読み込みます。指定しない限りオフのままです。</li>
</ul>
<h2>うまくいかないとき</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew が <code>marsdawn</code> をソースからビルドしています。Intel Mac ではこうなります。App Store から Xcode 26 以降をインストールし、もう一度インストールし直してください。</li>
  <li><code>marsdawn: No such file: …</code> パスがファイルを指していません。名前を確認するか、ファイルがあるフォルダでコマンドを実行してください。</li>
  <li><code>… already exists. Pass --force to replace it.</code> 同じ名前の PDF がすでにあります。<code>--force</code> を付けて上書きするか、<code>-o</code> で別の場所に書き出してください。</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> テーマまたは紙のサイズが認識されていません。テーマは dawn、classic、modern、vivid、紙は a4 または letter です。</li>
</ul>
<h2>次に</h2>
<ul>
  <li>すべてのオプションと出力される JSON：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>コーディングエージェントにこれをやらせるには：<a href="/ja/cli/skill/">marsdawn の agent skill</a>。</li>
  <li>4つのプレビューテーマすべてと、PDF 書き出しの今後：<a href="/ja/themes/">プレビューテーマと PDF 書き出し</a>。</li>
  <li>Markdown を使わない人に PDF を渡す：<a href="/ja/sharing-exported-pdfs/">PDF を共有する</a>。</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer と MarsDawn：ビューアかエディタか · MarsDawn',
        "description": 'MacMD Viewer は Markdown を読み取り専用で表示、USD 19.99。MarsDawn は編集とプレビューを並べて表示、Mac App Store で無料お試し後に USD 4.99 を一度だけ。',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer と MarsDawn。</h1>
  <p>どちらも、レンダリングされた Markdown を読むための Mac アプリです。MacMD Viewer は <code>.md</code> ファイルを開いて完成したページを表示しますが、編集はできません。MarsDawn は同じようなプレビューの隣にエディタを置き、同じウインドウで書きながら読めます。以下、機能ごとに両者の違いを見ていきます。</p>
</section>
<h2>読むだけでよく、編集が不要なら</h2>
<p>他の人が書いた Markdown を読むだけが仕事で、ソースに触れる必要が一切ないなら、MacMD Viewer は妥当な選択です。まさにそのために作られていて、今すぐ使え、より古い macOS でも動きます。読むことが仕事の全部ではなくなった時点で、MarsDawn の価値が出てきます。エージェントの書いた Markdown は、たいてい次の修正のためにまた戻ってくるからです。</p>
<h2>それぞれができること</h2>
<ul>
  <li><strong>編集：</strong>MacMD Viewer は設計上、読み取り専用です。MarsDawn はソースを編集しながら隣でレンダリングするので、入力すると変更がその場に表示されます。</li>
  <li><strong>プレビューテーマ：</strong>MacMD Viewer は12種類の文書テーマを備えています。MarsDawn は Dawn、Classic、Modern、Vivid の4種類で、それぞれライトとダークがあります。</li>
  <li><strong>図と数式：</strong>両者とも Mermaid 図を描画し、コードをハイライトします。MarsDawn は KaTeX の数式もレンダリングします。MacMD Viewer 自身の紹介ページには数式のレンダリングについての記載がありません。</li>
  <li><strong>Finder 連携：</strong>両者とも Finder のクイックルック拡張を追加するので、<code>.md</code> ファイルを選んで空白キーを押せばレンダリングされたページが表示されます。</li>
  <li><strong>PDF と印刷：</strong>両者ともレンダリングされたページを PDF として書き出す、または印刷できます。</li>
  <li><strong>システム要件：</strong>MacMD Viewer は macOS 14（Sonoma）以降が必要です。MarsDawn は macOS 26（Tahoe）以降が必要です。</li>
  <li><strong>言語：</strong>MarsDawn のインターフェースは{k.APP_UI_LANGUAGES}に対応しています。MacMD Viewer 自身の資料にはインターフェース言語の記載がないため、このページでは比較していません。</li>
</ul>
<h2>価格と購入方法</h2>
<ul>
  <li><strong>購入場所：</strong>MacMD Viewer は自社サイトから直接ダウンロードでき、Homebrew と Setapp でも入手できますが、Mac App Store にはありません。MarsDawn は Mac App Store のみです。</li>
  <li><strong>価格：</strong>MacMD Viewer は Mac 1台につき USD 19.99 の買い切り（3台パックやボリュームパックはより高額）。MarsDawn は無料でダウンロードでき、USD 4.99 の一度だけの解除です。</li>
  <li><strong>まず試す：</strong>MacMD Viewer に無料お試しはなく、直接購入には代わりに14日間の返金保証が付きます。MarsDawn は支払う前に14日間の試用期間があります。</li>
  <li><strong>返金とアップデート：</strong>MacMD Viewer の返金とアップデートは自社サイトを通じて行われます。MarsDawn の購入は Apple を通すので、返金とアップデートも Apple の標準的な仕組みに従います。</li>
  <li><strong>アカウント：</strong>どちらのアプリも、使うのにアカウントは必要ありません。</li>
</ul>
<h2>今日から無料で試す</h2>
<p>MarsDawn は Mac App Store に近日公開予定で、まだ販売開始していません。それまでの間、無料の <code>marsdawn</code> コマンドラインツールが、今すぐどんな Markdown ファイルでも PDF にレンダリングできます。Mermaid 図もハイライトされたコードも含み、他に何もインストールする必要はありません。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>次に</h2>
<ul>
  <li>完全な手順：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。</li>
  <li>MarsDawn ができないこと：<a href="/ja/limits/">その一覧</a>。</li>
  <li>コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。</li>
  <li>VS Code やブラウザ、Claude Desktop で Markdown を読む場合との比較：<a href="/ja/vs/markdown-preview-tools/">比較はこちら</a>。</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn：無料の Markdown to PDF コマンドラインツール · MarsDawn',
        "description": 'Mac 向けの無料コマンドラインツール marsdawn：シェルやスクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストールできます。',
        "body": f"""
<section class="intro">
  <h1>コマンドライン</h1>
  <p>無料の <code>marsdawn</code> コマンドラインツール：シェルや LLM エージェントから Markdown を PDF に書き出し、MarsDawn アプリがインストールされていればファイルをそこで開くこともできます。</p>
</section>

<div class="summary"><p><strong>marsdawn は無料で、Mac App Store とは別に配布されています。</strong>Homebrew でインストールしてください。Apple シリコンの Mac ではすぐに使える状態で届きます。<code>export</code> は単独で動作し、<code>open</code> には MarsDawn アプリが必要です。</p></div>

<p>AI エージェントやスクリプトから marsdawn を呼び出しますか？JSON 出力、スキーマ、すべての終了コードは<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>を、エージェントが代わりに MCP でツールを呼び出す場合は<a href="/ja/cli/mcp/">MCP サーバー</a>をご覧ください。</p>

<h2>インストール</h2>
<p><a href="https://brew.sh">Homebrew</a> を使う場合：</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>Apple シリコンの Mac では、Homebrew が数秒でビルド済みのコピーをインストールし、他に何もインストールする必要はありません。Intel Mac では代わりにソースからビルドするため数分かかり、Xcode 26 以降（Swift 6.2）が必要です。このツールは macOS 15 以降で動作します。</p>
<p>または、<a href="{k.KIT_URL}">ソース</a>から Swift Package Manager でビルドすることもできます：</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>インストールされたバージョンは <code>marsdawn --version</code> で確認できます。</p>

<h2>コマンド</h2>

<h3>marsdawn open</h3>
<p>1つ以上の Markdown ファイルを MarsDawn アプリで開き、レビューできるようにします。アプリのインストールが必要です。インストールされていない場合、<code>marsdawn open</code> は代コード 3 で終了し、MarsDawn がインストールされていないと表示します。<code>export</code> にはアプリは不要です。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>：MarsDawn にその行へ移動するよう伝えます。後ろにさらに列番号が続く場合（<code>notes.md:120:8</code> など）は無視されます。その名前そのままのファイルが存在する場合は、その引数はそのファイルとして扱われます。</li>
  <li><code>--line &lt;n&gt;</code>：単一ファイルに対して同じことをします。ファイル名自体がコロンと数字で終わる場合の行指定にも使えます。ファイルは1つだけ指定できます。</li>
  <li>行番号の範囲は 1 から 999999999 です。</li>
  <li>MarsDawn 1.0 はファイルを開きますが、まだその行へジャンプはしません。</li>
  <li><code>--json</code>：テキストの代わりに JSON 結果を出力します。</li>
</ul>
<p>行番号は marsdawn 0.3.0 で追加されました。</p>

<h3>marsdawn export</h3>
<p>Markdown ファイルを、MarsDawn 自身の PDF 書き出しと同じエンジンでページ分割された PDF に変換します。MarsDawn アプリは不要です。相対パスの画像は、入力ファイルのフォルダを基準に解決されます。</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF の書き出し先。デフォルトは入力パスの拡張子を <code>.pdf</code> に変えたものです。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：プレビューテーマのライトカラー。デフォルトは <code>$MARSDAWN_THEME</code>、それもなければ <code>dawn</code> です。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：紙のサイズ。デフォルトは <code>a4</code> です。</li>
  <li><code>--allow-remote-images</code>：書き出し中にウェブから画像を読み込みます。デフォルトはオフです。</li>
  <li><code>--force</code>：出力先ファイルがすでに存在する場合に置き換えます。</li>
  <li><code>--json</code>：テキストの代わりに JSON 結果を出力します。</li>
</ul>

<h2>$MARSDAWN_THEME 環境変数</h2>
<p><code>--theme</code> が指定されない場合、<code>export</code> は <code>$MARSDAWN_THEME</code> 環境変数を読みます。値は <code>dawn</code>、<code>classic</code>、<code>modern</code>、<code>vivid</code> のいずれかである必要があり、それ以外は <code>dawn</code> にフォールバックします。この CLI はアプリ自身のテーマ設定を読みません。他のアプリのコンテナを読むと、macOS のプライバシープロンプトが表示されることがあるためです。</p>

<h2>ファイルの上書き</h2>
<p><code>export</code> は、<code>--force</code> を指定しない限り既存の出力ファイルを置き換えません。</p>

<h2>終了コード</h2>
<ul>
  <li><code>0</code>：成功。</li>
  <li><code>2</code>：入力が見つかりません。</li>
  <li><code>3</code>：MarsDawn がインストールされていません（<code>open</code> のみ）。</li>
  <li><code>4</code>：出力先がすでに存在します（<code>--force</code> を指定してください）。</li>
  <li><code>5</code>：書き出しに失敗しました。</li>
  <li><code>64</code>：使い方の誤り。行番号が範囲外だったり、<code>--line</code> に複数ファイルを指定した場合などです。</li>
</ul>

<h2>--json 出力</h2>
<p>成功時、<code>marsdawn open --json</code> は <code>ok</code>、<code>opened</code>（各ファイルの <code>path</code>、行が指定されていれば <code>line</code> も含むリスト）、<code>app</code>（アプリのパス）を出力します。<code>marsdawn export --json</code> は <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code>、<code>diagramErrors</code> を出力します。失敗時は、どちらも <code>ok</code>、<code>error</code>、<code>message</code> を出力します。</p>
""",
    }
    pages['cli/agents'] = {
        "title": 'AI エージェント向け marsdawn：スクリプトから Markdown を PDF に · MarsDawn',
        "description": 'Markdown を PDF に変換するために marsdawn を呼び出す AI エージェントやスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、動作要件。',
        "body": f"""
<section class="intro">
  <h1>AI エージェント向け marsdawn</h1>
  <p><code>marsdawn</code> コマンドラインツールを呼び出す AI エージェントやスクリプトのためのリファレンスです。このページのすべての例は、現在のソースからビルドしたツールに対して実際に実行したものです。</p>
</section>

<div class="summary"><p><strong>Markdown ファイルを PDF に変換するには、<code>marsdawn export notes.md --json</code> を実行し、stdout から1つの JSON オブジェクトを読み取ってください。</strong>Mermaid 図とハイライトされたコードは、MarsDawn アプリと同じ方法で描画されます。<code>export</code> にアプリは不要ですが、<code>open</code> には必要です。</p></div>

<h2>できること</h2>
<ul>
  <li><code>export</code>：MarsDawn アプリと同じ書き出しエンジンで、1つの Markdown ファイルをページ分割された PDF に変換します。ウインドウは開きません。</li>
  <li><code>open</code>：1つ以上の Markdown ファイルを MarsDawn アプリで開き、人がレビューできるようにします。各ファイルが移動すべき行を指定することもできます。</li>
</ul>

<h2>できないこと</h2>
<ul>
  <li>stdin から Markdown を読み込みません。ファイルパスを渡してください。</li>
  <li>PDF を stdout に書き出しません。PDF は必ずファイルに書き込まれ、stdout には結果だけが出力されます。</li>
  <li><code>--force</code> を指定しない限り、既存のファイルを置き換えません。</li>
  <li><code>--allow-remote-images</code> を指定しない限りウェブから画像を読み込まず、指定した場合も https のみです。</li>
  <li><code>open</code> は MarsDawn アプリがインストールされていないと動作せず、代コード 3 で終了します。<code>export</code> にアプリは不要です。</li>
  <li>MarsDawn 1.0 はまだ <code>open</code> が指定した行へジャンプしません。ファイルの先頭を開きます。</li>
  <li>macOS でのみ動作します。</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p><code>notes.md</code> の隣に <code>notes.pdf</code> を書き出します。オプション：</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF の書き出し先。デフォルトは入力パスの拡張子を <code>.pdf</code> に変えたものです。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：テーマのライトカラー。デフォルトは <code>$MARSDAWN_THEME</code>、それもなければ <code>dawn</code> です。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：紙のサイズ。デフォルトは <code>a4</code> です。</li>
  <li><code>--allow-remote-images</code>：書き出し中にウェブから https の画像を読み込みます。</li>
  <li><code>--force</code>：出力先ファイルが存在する場合に置き換えます。</li>
  <li><code>--json</code>：テキストの代わりに、stdout に1つの JSON オブジェクトを出力します。</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>成功、終了コード 0：</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>：書き出された PDF の絶対パス。</li>
  <li><code>pages</code>：ページ数。</li>
  <li><code>theme</code> と <code>paper</code>：実際に使われた値。</li>
  <li><code>diagramErrors</code>：描画に失敗した Mermaid 図ごとに1件のメッセージ。PDF はそれでも書き出されます。</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> は移動先の行を指定します。後ろにさらに列番号が続く場合（<code>notes.md:120:8</code> など）は無視されます。存在するファイル名そのものを指す引数は常にそのファイル名として扱われるので、<code>weird:12</code> という名前のファイルはそのまま開きます。</li>
  <li><code>--line &lt;n&gt;</code> は単一ファイルの行を指定します。ファイル名自体がコロンと数字で終わる場合も含みます。ファイルは1つだけ指定できます。</li>
  <li>行番号の範囲は 1 から 999999999 です。それ以外は使い方の誤りになります。</li>
  <li>行番号は marsdawn 0.3.0 で追加されました。MarsDawn 1.0 はファイルを開きますが、まだその行へジャンプしません。</li>
</ul>
<p>成功、終了コード 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：指定した順に、ファイルごとの1オブジェクト。<code>path</code> はファイルの絶対パス、<code>line</code> は行が指定された場合にのみ含まれます。</li>
  <li><code>app</code>：それらを開いた MarsDawn アプリのパス。</li>
</ul>
<p>marsdawn 0.2.x では <code>opened</code> はパス文字列のリストでした。両方に対応する必要がある場合は <code>marsdawn --version</code> を確認してください。</p>

<h2>失敗</h2>
<p><code>--json</code> を指定すると、失敗時は stdout に1つの JSON オブジェクトを出力し、対応するコードで終了します：</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>、<code>input_not_found</code>：入力が存在しない、フォルダである、または UTF-8 テキストでない。</li>
  <li><code>3</code>、<code>app_not_installed</code>：MarsDawn がインストールされていません。これを返すのは <code>open</code> だけです。</li>
  <li><code>4</code>、<code>output_exists</code>：出力先ファイルがすでに存在します。<code>--force</code> を指定してください。</li>
  <li><code>5</code>、<code>export_failed</code>：書き出し自体が失敗しました。</li>
  <li><code>64</code>：使い方の誤り。未知のオプション、無効な値、範囲外の行番号、複数ファイルに対する <code>--line</code> など。これは <code>--json</code> を指定していても、常にテキストとして stderr に出力されます。</li>
</ul>

<h2>JSON スキーマ</h2>
<p>それぞれの <code>--json</code> 結果に対する JSON Schema（draft 2020-12）：</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>環境変数</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>：<code>--theme</code> が指定されないときに <code>export</code> が使うテーマ。未知の値はエラーなしで <code>dawn</code> にフォールバックします。</li>
</ul>

<h2>動作要件</h2>
<ul>
  <li>このツールは macOS 15 以降で動作します。Apple シリコンでは Homebrew がビルド済みのボトルをインストールし、他には何も必要ありません。自分でビルドする場合（Intel Mac、またはソースから）は Swift 6.2 以降が必要で、これは Xcode 26 以降に含まれています。</li>
  <li>MarsDawn アプリには macOS 26 以降が必要です。</li>
</ul>

<h2>インストール</h2>
<p>Homebrew を使います。Apple シリコンではビルド済みのボトルを数秒で取得でき、Xcode は不要です。Intel Mac ではソースから marsdawn をコンパイルするため数分かかり、Xcode 26 以降が必要です。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>または<a href="{k.KIT_URL}">ソース</a>からビルドすることもできます。最初のビルドでは依存関係の取得とコンパイルが行われ、これも数分かかります。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> は <code>0.3.0</code> のようなバージョン番号を出力し、終了コード 0 で終了します。</p>

<h2>次に</h2>
<ul>
  <li>シェルではなく指示を読むエージェント向けの、1ファイルの skill：<a href="/ja/cli/skill/">marsdawn skill</a>。</li>
  <li>同じ <code>export</code> をラップする MCP サーバー：<a href="/ja/cli/mcp/">marsdawn-mcp</a>。</li>
  <li>この JSON 結果が、なぜエージェント自身の context にとって安上がりなのか：<a href="/ja/token-efficient-review/">トークンを節約するレビュー方法</a>。</li>
</ul>
""",
    }
    pages['cli/skill'] = {
        "title": 'コーディングエージェント向けの、Markdown to PDF skill · MarsDawn',
        "description": 'コーディングエージェントが読み込む1つのファイルで、marsdawn をインストールし、動作を確認し、Markdown を PDF に書き出し、JSON 結果を読み取れるようにします。',
        "body": f"""
<section class="intro">
  <h1>PDF 作成をエージェントに任せる。</h1>
  <p>この skill は1つの Markdown ファイルです。コーディングエージェントに <code>marsdawn</code> のインストール、動作確認、文書の PDF 書き出し、結果の読み取りを教えます。これにより、Markdown を書いたエージェントが、あなたに PDF も渡せるようになります。</p>
</section>
<h2>Claude Code にインストールする</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code はタスクが PDF を必要とするときに自動で読み込み、自分で <code>/marsdawn</code> として実行することもできます。<a href="/cli/skill/SKILL.md">短いファイル</a>なので、インストールする前に読んでおいてください。</p>
<p>他のエージェントも同じファイルを使えます。これは指示とコマンドだけのプレーンな Markdown なので、あなたのエージェントにこの URL を指すか、貼り付けてください。このファイルは英語で書かれています。</p>
<h2>教える内容</h2>
<ul>
  <li><code>marsdawn</code> がなければ Homebrew でインストールし、バージョンを決め打ちせず <code>marsdawn --version</code> で確認する。</li>
  <li><code>marsdawn export … --json</code> で書き出し、結果を読み取る：PDF の保存先、ページ数、描画されなかった Mermaid 図があるかどうか。</li>
  <li>終了コードで失敗の種類を見分ける：ファイルが見つからない、PDF がすでにある、書き出しの失敗、オプションの誤り。</li>
  <li>MarsDawn アプリがインストールされているときだけ <code>open</code> を使い、PDF を作るためには絶対に使わない。</li>
</ul>
<h2>しないこと</h2>
<ul>
  <li>自分自身に何かを実行する権限を与えることはありません。あなたのエージェントは、他のコマンドと同じように、<code>marsdawn</code> をインストールしたり実行したりする前に、これまでどおり許可を求めます。</li>
  <li>あなたの文書をどこにも送信しません。<code>marsdawn</code> はあなたの Mac 上で描画し、<code>--allow-remote-images</code> を指定しない限りウェブの画像は含めません。</li>
</ul>
<p>すべての契約内容、すべてのフィールドとコードは<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>にあります。skill ファイルを読む代わりに MCP でツールを呼び出すエージェント向けには、<a href="/ja/cli/mcp/">MCP サーバー</a>もあります。</p>
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

<h2>CLI</h2>
<p><code>marsdawn export notes.md --json</code> は、シェルコマンドを実行できるエージェントやスクリプトならどれからでも呼び出せます。構造上、モデルに依存しません。返されるすべてのフィールドは<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>に文書化されており、そこが JSON スキーマの正典で、以下の二つの経路もそこを参照します。</p>

<h2>skill ファイル</h2>
<p>シェルを直接呼び出すのではなく、プレーンな Markdown の指示を読むエージェント向け——現時点では Claude Code——には、<a href="/ja/cli/skill/">marsdawn skill</a> という1ファイルが、marsdawn のインストール、<code>export</code> の実行、結果の読み取りを教えます。プレーンな Markdown なので、指示ファイルを読み込む他のエージェントも同じファイルを使えます。</p>

<h2>MCP サーバー</h2>
<p><a href="{_mcp_url}">marsdawn-mcp</a> は、別の、公開された、{_mcp_license} ライセンスの独立した repository です。<code>export_markdown_to_pdf</code> という1つのツールを持つ MCP サーバーで、<code>marsdawn export --json</code> をラップしています。MCP クライアントをそれに向ければ、ツール呼び出しは CLI と同じ JSON を返します。</p>
<ul>
  <li><strong>入手方法：</strong><a href="{_mcp_url}/releases">GitHub のリリース</a>に添付された MCP Bundle（<code>marsdawn.mcpb</code>）として、またはソースから stdio でサーバーを実行することで入手できます。</li>
  <li><strong>Registry：</strong>まだ MCP Registry には登録されていません（現在のリリース：0.1.0）。registry 経由で見つかる前に、repository で現在の状況を確認してください。</li>
  <li><strong>ホスティング：</strong>自分でホストするしかありません。marsdawn-mcp のホスティングサービスは存在せず、サーバーは marsdawn 自身の隣、あなた自身のマシン上で動きます。</li>
  <li><strong>動作要件：</strong>macOS、marsdawn 0.5.0 以降、そしてサーバーを実行するための Node.js 20 以降。</li>
</ul>

<h2>同じ export、三つの入り口</h2>
<p>どの入り口から呼び出しても、内部の動作は変わりません。同じ書き出しエンジン、同じテーマと紙のサイズ、Mermaid 図の描画に失敗したときの同じ <code>diagramErrors</code>。このページではその契約内容を繰り返しません。<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>に完全な内容があります。</p>

<h2>次に</h2>
<ul>
  <li>完全な JSON スキーマとすべての終了コード：<a href="/ja/cli/agents/">AI エージェント向け marsdawn</a>。</li>
  <li>Claude Code などのエージェント向けの1ファイルの skill：<a href="/ja/cli/skill/">marsdawn skill</a>。</li>
  <li>精簡な JSON 結果が、なぜエージェント自身の context にとって重要なのか：<a href="/ja/token-efficient-review/">トークンを節約するレビュー方法</a>。</li>
</ul>
""",
    }
    pages['token-efficient-review'] = {
        "title": 'エージェントのトークンを使わずに MarsDawn の出力をレビューする · MarsDawn',
        "description": '人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく精簡な JSON 結果を返すので、呼び出し自体も安上がりです。',
        "body": """
<section class="intro">
  <h1>エージェントのトークンを使わずにレビューする。</h1>
  <p>このループでは、二つの別々のことがどちらも安く済みます。エージェントがツール呼び出しから受け取るもの、そして結果が正しく見えることを確認するのに必要なもの、です。</p>
</section>

<div class="summary"><p><strong>ツール呼び出しが返すのは小さな JSON オブジェクトであり、レンダリングされたページではありません。レンダリングされたページ自体は、人が MarsDawn の中で読みます。エージェントの context に読み戻されることは決してありません。</strong></p></div>

<h2>ツール呼び出し自体が安い</h2>
<p><code>marsdawn export</code> を、CLI、skill、または<a href="/ja/cli/mcp/">MCP サーバー</a>のいずれからでも呼び出すと、返ってくるのは<a href="/ja/cli/agents/">精簡な JSON オブジェクト</a>です：<code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code>、<code>diagramErrors</code>。完全なスキーマは <a href="/schemas/cli/export.v1.json">export.v1.json</a> にあります。そのどれもレンダリングされた文書そのものではありません。十数個の Mermaid 図がある50ページの PDF も、1ページのメモと同じ数のフィールドしか返しません。</p>

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

<h2>VS Code の内蔵プレビュー</h2>
<p>VS Code で <kbd>&#8984;&#8679;V</kbd> を押すと、内蔵のプレビューパネルで Markdown ファイルがレンダリングされます。無料で、インストールするものもありません。VS Code 1.121（2026年5月）以降、このプレビューは Mermaid 図もネイティブに描画します。Microsoft が Mermaid 拡張機能を VS Code 本体に組み込んだためで、以前は別の拡張機能が必要でしたが、今は不要です。できないこと：これはエディタの中のプレビューパネルであって、読むために作られたエディタではありません。パネルの隣にはファイルツリー、ターミナル、VS Code が表示できるその他のパネルが並び、VS Code 自体も Electron アプリで、Mac ではおよそ150〜250MB のダウンロードになります。</p>

<h2>ローカルファイル用のブラウザ拡張機能</h2>
<p>ローカルの <code>.md</code> ファイルを読むために主流と呼べるブラウザ拡張機能はありません。Local Markdown Viewer、Markdown Viewer、MarkView などがだいたい同じことをしていて、どれもデフォルトではありません。どれも、何かを開く前に同じ手順が必要です。ブラウザはデフォルトで拡張機能に <code>file://</code> のページを読ませないので、その拡張機能の「ファイルの URL へのアクセスを許可」を有効にする必要があります。これは拡張機能ごとに一度だけ与える権限ですが、与えたこと自体や、なぜ与えたのかを忘れやすいものです。有効にすると、ファイルはブラウザのタブに表示されます。つまり、1つのファイルを見るために、ブラウザを丸ごと動かすことになります。</p>

<h2>Claude Desktop のファイルプレビュー</h2>
<p>Claude Desktop は、すでに Project や会話の中にあるファイルについては、Markdown をきちんとレンダリングします。frontmatter は表として、見出し、太字、インラインコードもすべてスタイルが付き、生のソースではありません。それが作られていないのは、ディスク上の任意のファイルを閲覧することです。会話にすでにあるものをプレビューするのであって、フォルダの中のメモをプレビューするわけではありません。そのパネルにあるアクションは「ダウンロード」で <code>.md</code> ファイルを取り戻すものであり、PDF に書き出すものではなく、オフラインやローカルでの編集もありません。プレビューは会話の一部であり、開いたまま手を加え続ける文書ではありません。</p>

<h2>三つとも、ブラウザエンジンの中で動いている</h2>
<p>VS Code と Claude Desktop はどちらも Electron アプリです。Chromium と Node.js のランタイムが同梱されていて、ネイティブの Mac アプリではありません。ブラウザ拡張機能という道は、実際のブラウザの中で動きます。どちらにしても、1つの Markdown ファイルを見るために、丸ごとのブラウザエンジンが裏で動いていることになります。MarsDawn はネイティブの AppKit アプリです。ダウンロードは軽く、どんなローカルファイルも直接開けて、インストールする拡張機能も、覚えておくべき権限フラグもありません。</p>

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
  <p>MarsDawn には Dawn、Classic、Modern、Vivid の4種類のプレビューテーマが付属し、それぞれライトとダークがあります。文書を読むための8通りの組み合わせです。PDF に書き出す、または印刷すると、そのとき読んでいたものと同じ見た目でページが出てきます。</p>
</section>

<div class="summary"><p><strong>4つのテーマ × ライトとダーク＝文書を読む8つの方法があり、書き出しはどれを選んでいても対応します。</strong>もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーは計画中で、まだ作られていません。</p></div>

<h2>4種類のテーマ</h2>
<ul>
  <li><strong>Dawn</strong>、デフォルト：このサイトと同じ、温かみのある紙の質感と Mars Rust のアクセントカラー。</li>
  <li><strong>Classic</strong>（典雅）：より素朴で、紙の文書らしい配色。</li>
  <li><strong>Modern</strong>（流行）：より涼しげで、現代的な配色。</li>
  <li><strong>Vivid</strong>（活潑）：より明るく、コントラストの高い配色。</li>
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
</ul>
""",
    }
    pages['reviewing-ai-output'] = {
        "title": 'なぜ AI の出力には、今も人の目が必要なのか · MarsDawn',
        "description": 'AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。',
        "body": """
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
  <li>このレビューが、なぜエージェント自身の context にとって安上がりなのか：<a href="/ja/token-efficient-review/">トークンを節約するレビュー方法</a>。</li>
  <li>レビュー済みの文書を、ほかの人に渡す：<a href="/ja/sharing-exported-pdfs/">PDF を共有する</a>。</li>
  <li>MarsDawn とは何か、1ページで：<a href="/ja/">ホームページ</a>。</li>
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
