"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': 'プライバシーポリシー', 'support': 'サポート', 'cli': 'コマンドライン', 'agents': 'AI エージェント向け marsdawn', 'using_cli': 'CLI の使い方', 'markdown-to-pdf': 'Markdown から PDF へ', 'skill': 'エージェント用スキル', 'view-markdown-on-mac': 'Mac で Markdown を見る', 'vs-macmd-viewer': 'MacMD Viewer と MarsDawn', 'updated': f"最終更新日：{k.UPDATED}", 'tagline': 'エージェントが書いた Markdown を読む。', 'slogan': 'Markdown の新しい夜明け。', 'footer_store': f'MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。', 'footer_nav': 'サイト', 'more': 'その他', 'yours': 'あなたの文章は Mac に残ります', 'pay-once': '無料で試して、一度だけ購入', 'pdf': 'PDF 書き出し', 'native': 'Mac アプリ', 'limits': 'MarsDawn ができないこと', 'mcp': 'MCP サーバー', 'token-efficient-review': 'トークンを抑えたレビュー', 'vs-markdown-preview-tools': '他のツールで Markdown を見る場合との比較', 'themes': 'プレビューテーマと PDF 書き出し', 'sharing-exported-pdfs': '書き出した PDF を共有する', 'reviewing-ai-output': 'AI の出力を人が確認する理由', 'changelog': '更新履歴', 'consent_text': 'このサイトでは、訪問者がどのように利用しているかを把握するために分析用クッキーを使用します。「同意する」を選ばない限り、これらのクッキーは使われません。', 'consent_accept': '同意する', 'consent_decline': '同意しない', 'consent_aria': 'クッキーの同意設定', 'cookie_settings': 'Cookie 設定'}
    store_chip = 'Mac App Store で配信中'
    schema_notes = {'export': 'export 成功時', 'open': 'open 成功時、marsdawn 0.5.1 以降、サイドバーに表示するフォルダを含む', 'open_v2': 'open 成功時、marsdawn 0.3.0〜0.5.0', 'error': '失敗時、両方のコマンド共通、marsdawn 0.5.2 以降', 'open_v1': 'open 成功時、marsdawn 0.2.x（<code>opened</code> がパスのリストだった頃）', 'error_v1': '失敗時、両方のコマンド共通、marsdawn 0.5.1 以前'}
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
        "body": f"""
<section class="intro">
  <h1>プライバシーポリシー</h1>
  <p>macOS 向け Markdown エディタ、MarsDawn がどのようにあなたの情報を扱うか。</p>
  <p class="updated">最終更新日：{k.PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn アプリは、あなたに関するデータを一切収集しません。</strong>アカウントも、広告も、トラッキングもありません。文書と設定はあなたの Mac 上に残ります。</p></div>

<h2>このウェブサイト</h2>
<p>アプリとこのウェブサイトは別のものです。アプリはデータを収集しません。訪問が記録され得るのは、marsdawn.southern-light.dev だけです。</p>
<p>このサイトは<strong>Google タグマネージャー</strong>経由で読み込まれる<strong>Google アナリティクス 4</strong>を使用しています。訪問者は最初、分析が拒否された状態で始まります。Google の同意モードは、バナーで「同意する」を選ぶまで、クッキーを使わず持続的な識別子も含まない通信だけを送ります。「同意しない」を選んだ場合、または何も選ばなかった場合も、この状態が続きます。以前に「同意する」を選んでいた場合でも、あとから「同意しない」に変更すると、分析はすぐに無効になり、下記のクッキーも削除されます。いつでもフッターの「Cookie 設定」リンクから選択を変更できます。この選択はブラウザのローカルストレージにのみ保存され、当サイト独自のクッキーではありません。</p>
<p>同意すると、Google アナリティクスは自身のクッキー（<code>_ga</code> と <code>_ga_&lt;測定 ID&gt;</code>）を設定し、次を記録します。</p>
<ul>
  <li><strong>ページビューと参照元。</strong>閲覧されたページと、ブラウザが送信した場合の参照元アドレス。</li>
  <li><strong>おおよその位置情報、デバイス、ブラウザ。</strong>IP アドレスから推定される、市区町村レベル程度までの位置情報、デバイスの種類、OS、ブラウザ。いずれも個人を特定できるものではありません。</li>
  <li><strong>サイトを離れるクリックとスクロール。</strong>Google アナリティクスの拡張計測機能は、サイトを離れるクリック（Mac App Store へのリンクなど）と、ページをどこまでスクロールしたかを記録します。</li>
  <li><strong>IP アドレス。</strong>Google アナリティクス 4 は IP アドレスを記録・保存しません。</li>
  <li><strong>記録しないもの。</strong>アカウントはありません。このサイトにアカウント機能がないためです。文書も、入力した文字も記録しません。サイトをまたいだ広告もなく、あなたのプロフィールも作りません。アプリが <code>/themes/</code> 以下のテーマファイルを取りに行くリクエストは対象外で、送られません。</li>
  <li><strong>保持期間。</strong>Google はこのデータを14か月保持したあと、削除します。</li>
  <li><strong>データの処理場所。</strong>Google タグマネージャーと Google アナリティクスは Google が運営しており、データは米国および Google が事業を行うその他の国で処理される場合があります。</li>
  <li><strong>ホスティング。</strong>サイトは Cloudflare 上にあります。どのホストとも同じく、リクエストに応答する間は IP アドレスを見ます。それはホスト自身のログであり、上のアナリティクスではありません。</li>
</ul>

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
<p>MarsDawn アプリは、子どもを含め、誰からもデータを収集しません。ウェブサイトに記録される訪問はアカウントではなく、誰かを識別するためにも使いません。</p>

<h2>購入</h2>
<p>MarsDawn は Mac App Store を通じて販売されます。購入は Apple 自身の規約のもとで処理され、開発者があなたの支払い情報を受け取ることはありません。</p>

<h2>このポリシーの変更</h2>
<p>MarsDawn がデータの扱い方を変える場合、そのバージョンがリリースされる前にこのページが更新され、冒頭の日付も変わります。</p>

<h2>お問い合わせ</h2>
<p>プライバシーに関するご質問：<a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
""",
    }
    pages['index'] = {
        "title": 'MarsDawn：ライブプレビュー搭載、Mac 向け Markdown エディタ',
        "description": 'エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で配信中です。',
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
        "description": '.md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で配信中の MarsDawn アプリで読む方法です。',
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
<h2>MarsDawn で読む</h2>
<p>MarsDawn は Mac 向けの Markdown エディタで、Mac App Store で配信中です。<code>.md</code> ファイルを開くと、ソースの隣でレンダリングされたページを読めます。</p>
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
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールも、どんな Markdown ファイルも Mermaid 図とハイライトされたコード付きの PDF にレンダリングでき、他に何もインストールする必要はありません。</p>
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
<p>コーディングエージェントを使っていますか？<a href="/ja/cli/skill/">marsdawn スキルを追加</a>してください。自分が書いたものを MarsDawn で開いてあなたに確認してもらう方法と、PDF の書き出しを教える、1つのファイルです。</p>
<p>Apple シリコンの Mac では、Homebrew がビルド済みのコピーを数秒でインストールし、他に何もインストールする必要はありません。Intel Mac では代わりにソースから marsdawn をビルドするため数分かかり、Xcode 26 以降（Swift 6.2）が必要です。このツールは macOS 15 以降で動作します。</p>
<p>または、Swift Package Manager で<a href="{k.KIT_URL}">ソース</a>からビルドします。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>インストールされているバージョンは <code>marsdawn --version</code> で確認できます。</p>

<h2>コマンド</h2>

<h3>marsdawn open</h3>
<p>1つ以上の Markdown ファイルを MarsDawn アプリで開いて確認できます。アプリのインストールが必要です。インストールされていない場合、<code>marsdawn open</code> はコード 3 で終了し、MarsDawn がインストールされていないことを知らせます。<code>export</code> にはアプリは不要です。アプリは <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code>：MarsDawn にその行に移動するよう指定します。その後にコロンが続く場合、たとえば <code>notes.md:120:8</code> の列部分は無視されます。引数全体と一致するファイル名が存在する場合、その引数はそのファイルとして扱われます。</li>
  <li><code>--line &lt;n&gt;</code>：単一ファイルに対して同じ指定ができ、それ自体がコロンと数字で終わるパスに対して行を指定する方法でもあります。ファイルは1つだけ指定できます。</li>
  <li>行番号は 1 から 999999999 までです。</li>
  <li>フォルダを引数にすると、書類としてではなくウインドウのサイドバーに開きます：<code>marsdawn open .</code> で現在のフォルダを表示します。<code>--folder &lt;path&gt;</code> はファイルと一緒に同じことをします。ウインドウのサイドバーに表示できるフォルダは1つなので、2つ指定すると使用方法のエラーになります。</li>
  <li><code>--background</code>：MarsDawn を前面に出さずに開きます。</li>
  <li><code>--json</code>：テキストではなく JSON の結果を出力します。</li>
</ul>
<p>行の指定は marsdawn 0.3.0 で、フォルダと <code>--background</code> は 0.5.1 で追加されました。</p>

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
  <li><code>6</code>：この MarsDawn はまだフォルダを表示できないため、何も開かなかった（<code>open</code> のみ）。</li>
  <li><code>64</code>：使用方法のエラー。範囲外の行、複数ファイルやフォルダに対する <code>--line</code> の指定、複数のフォルダの指定などを含みます。</li>
</ul>

<h2>--json 出力</h2>
<p>成功時、<code>marsdawn open --json</code> は <code>ok</code>、<code>opened</code>（各ファイルの <code>path</code>、行が指定されていれば <code>line</code> も含む）、<code>app</code>（アプリのパス）、フォルダが指定されていれば <code>folder</code> を出力します。<code>marsdawn export --json</code> は <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code>、<code>diagramErrors</code> を出力します。失敗時はどちらも <code>ok</code>、<code>error</code>、<code>message</code> を出力します。</p>
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
  <li><code>open</code>：1つ以上の Markdown ファイルを MarsDawn アプリで開き、人が確認できるようにします。各ファイルが移動すべき行を指定したり、ウインドウのサイドバーにフォルダを表示したりすることもできます。</li>
</ul>

<h2>できないこと</h2>
<ul>
  <li>stdin から Markdown を読み込みません。ファイルパスを渡してください。</li>
  <li>PDF を stdout に書き出しません。PDF は常にファイルとして書き出され、stdout には結果だけが出力されます。</li>
  <li><code>--force</code> を指定しない限り、既存のファイルを置き換えません。</li>
  <li><code>--allow-remote-images</code> を指定しない限りウェブから画像を読み込まず、指定した場合も https のみです。</li>
  <li><code>open</code> は MarsDawn アプリがインストールされていないと動作せず、コード 3 で終了します。<code>export</code> にアプリは不要です。アプリは <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。</li>
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
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> は移動先の行を指定します。その後にコロンが続く場合、たとえば <code>notes.md:120:8</code> の列部分は無視されます。存在するファイル名を丸ごと表す引数は常にそのファイル名として扱われるため、<code>weird:12</code> という名前のファイルはそのまま開きます。</li>
  <li><code>--line &lt;n&gt;</code> は単一ファイルの行を指定します。それ自体がコロンと数字で終わるパスも含みます。ファイルは1つだけ指定できます。</li>
  <li>行番号は 1 から 999999999 までで、それ以外は使用方法のエラーになります。</li>
  <li>行の指定は marsdawn 0.3.0 で追加されました。</li>
  <li>フォルダを引数にすると、書類としてではなくウインドウのサイドバーに開きます。<code>marsdawn open .</code> で現在のフォルダを表示し、<code>--folder &lt;path&gt;</code> はファイルと一緒に同じことをします。ウインドウのサイドバーに表示できるフォルダは1つです：2つ指定すると使用方法のエラーになり、<code>--folder</code> を2回使った場合も（同じフォルダでも）エラーです。同じフォルダを引数でもう一度指定した場合は1つとして扱います。フォルダには行がないため、フォルダに <code>--line</code> を指定すると使用方法のエラーです。<code>-a</code> はありません：指定すると使用方法のエラーになり、<code>--folder</code> を案内します。</li>
  <li><code>--background</code> は MarsDawn を前面に出さずに開きます。人が別の作業をしている間にファイルを開くエージェント向けです。JSON はどちらでも同じです。</li>
  <li>フォルダと <code>--background</code> は marsdawn 0.5.1 で追加されました。</li>
</ul>
<p>成功、終了コード 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：渡された順に、ファイルごとの1つのオブジェクト。<code>path</code> はファイルの絶対パス、<code>line</code> は行が指定されたときだけ現れます。</li>
  <li><code>app</code>：それらを開いた MarsDawn アプリのパス。</li>
</ul>
<p>フォルダを指定した場合（marsdawn 0.5.1 以降）、終了コード 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code>：フォルダを指定したときだけ現れます。<code>path</code> はその絶対パスです。<code>requested</code> は常に <code>true</code> です：marsdawn は MarsDawn にフォルダの表示を依頼しましたが、サイドバーに実際に表示されたかどうかは分かりません。アプリが先に人にアクセスの許可を求めることがあるためです。「完了した」ではなく「依頼した」と報告してください。</li>
  <li>フォルダだけを指定したとき、<code>opened</code> は空です。</li>
</ul>
<p>marsdawn 0.2.x では <code>opened</code> はパス文字列のリストでした。両方を扱う必要がある場合は <code>marsdawn --version</code> を確認してください。</p>

<h2>Claude Code が編集したファイルを開く</h2>
<p>オプトインの <a href="https://code.claude.com/docs/en/hooks">Claude Code フック</a>です。Claude が Markdown ファイルを書き込んだり編集したりすると、そのファイルを MarsDawn でバックグラウンドで開きます。開くのはセッションごと、ファイルごとに一度だけです。頼んでいないウインドウは注意をそらすので、追加しない限り有効にならず、プロジェクトごとに追加します。シェルコマンドを実行するだけなので、モデルのトークンは使いません。</p>
<p><code>--background</code> のために marsdawn 0.5.1 以降と、MarsDawn アプリが必要です。</p>
<p>次の内容をプロジェクトの <code>.claude/hooks/marsdawn-open.sh</code> として保存し、<code>chmod +x</code> で実行可能にします。</p>
<pre><code>#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2&gt;/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2&gt;/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || {{ [ -x /opt/homebrew/bin/marsdawn ] &amp;&amp; echo /opt/homebrew/bin/marsdawn; }}) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${{TMPDIR:-/tmp}}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2&gt;/dev/null &amp;&amp; exit 0
echo "$file" &gt;&gt; "$seen"

"$marsdawn" open --background "$file" &gt;/dev/null 2&gt;&amp;1 || true
exit 0</code></pre>
<p>次に、プロジェクトの <code>.claude/settings.json</code> にフックを追加します。自分だけで使う場合は <code>.claude/settings.local.json</code> に追加します。</p>
<pre><code>{{
  "hooks": {{
    "PostToolUse": [
      {{
        "matcher": "Write|Edit",
        "hooks": [
          {{ "type": "command", "command": "\\"$CLAUDE_PROJECT_DIR\\"/.claude/hooks/marsdawn-open.sh" }}
        ]
      }}
    ]
  }}
}}</code></pre>
<ul>
  <li>Claude の Write ツールと Edit ツールのあとに実行されます。<code>.md</code> または <code>.markdown</code> で終わらないファイルには何もしません。</li>
  <li>Claude が何度編集しても、各ファイルは Claude Code のセッションごとに一度だけ開きます。記録は <code>$TMPDIR/marsdawn-hook/</code> にセッションごとに一つのファイルとして残るので、新しいセッションでは再び開きます。</li>
  <li><code>--background</code> により MarsDawn は前面に出ません。作業中のウインドウのフォーカスはそのままです。</li>
  <li>Claude の邪魔はしません。どの経路でも終了コード 0 で終わり、marsdawn や MarsDawn アプリがインストールされていなければ何もしません。</li>
  <li>フックの入力は <code>/usr/bin/jq</code> で読みます。これは macOS 26 に含まれていて、MarsDawn アプリも macOS 26 を必要とします。</li>
  <li>無効にするには、設定ファイルからこの項目を削除します。</li>
</ul>

<h2>失敗時</h2>
<p><code>--json</code> を指定すると、失敗時は stdout に1つの JSON オブジェクトを出力し、対応するコードで終了します。</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>、<code>input_not_found</code>：入力が存在しない、フォルダである、または UTF-8 テキストでない。または <code>--folder</code> のパスが存在しないか、フォルダでない。</li>
  <li><code>3</code>、<code>app_not_installed</code>：MarsDawn がインストールされていない。<code>open</code> のみがこれを返します。</li>
  <li><code>4</code>、<code>output_exists</code>：出力ファイルが存在する。<code>--force</code> を指定してください。</li>
  <li><code>5</code>、<code>export_failed</code>：書き出し自体が失敗した。</li>
  <li><code>6</code>、<code>app_cannot_open_folders</code>：この MarsDawn はまだフォルダを表示できないため、何も開かなかった。<code>open</code> のみがこれを返します。</li>
  <li><code>64</code>：使用方法のエラー。未知のオプション、無効な値、範囲外の行、複数ファイルやフォルダに対する <code>--line</code> の指定、複数のフォルダの指定、<code>-a</code> の指定など。この場合は、<code>--json</code> を指定していても stderr にテキストとして出力されます。</li>
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
        "description": 'コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。',
        "body": f"""
<section class="intro">
  <h1>書いたものをエージェントに見せてもらい、PDF も作ってもらう。</h1>
  <p>このスキルは1つの Markdown ファイルです。コーディングエージェントに、自分が書いた文書を MarsDawn で開いてあなたに確認してもらう方法と、<code>marsdawn</code> のインストール方法、動作確認の方法、文書を PDF に書き出す方法、結果の読み方を教えます。</p>
</section>
<div class="summary"><p><strong>1つの Markdown ファイルを <code>~/.claude/skills/marsdawn/SKILL.md</code> に置くだけ。</strong>これでエージェントが <code>marsdawn</code> をインストールし、PDF に書き出し、JSON の結果を読みます。何かを実行する前には、これまでどおり確認を求めます。</p></div>
<h2>Claude Code にインストールする</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code は、PDF が必要なタスクのとき、またはあなたが読む Markdown 文書を書いたり修正したりしたときに、これを自動的に読み込みます。<code>/marsdawn</code> として自分で実行することもできます。<a href="/cli/skill/SKILL.md">短いファイル1つ</a>なので、インストールする前に読んでみてください。</p>
<p>他のエージェントでも同じファイルを使えます。ただの Markdown で、説明とコマンドが書いてあるだけなので、あなたのエージェントにこの URL を指定するか、そのまま貼り付けてください。このファイルは英語です。</p>
<h2>教えること</h2>
<ul>
  <li><code>marsdawn</code> がなければ Homebrew でインストールし、バージョンを決め打ちせず <code>marsdawn --version</code> で確認する。</li>
  <li><code>marsdawn export … --json</code> で書き出し、結果を読み取る：PDF の書き出し先、ページ数、レンダリングされなかった Mermaid 図の有無。</li>
  <li>終了コードで失敗の種類を見分ける：ファイルが見つからない、PDF がすでにある、書き出しに失敗した、オプションが不正、など。</li>
  <li><code>marsdawn open file.md:line</code> で自分が書いた文書を開き、最初の変更箇所に移動する。開くのは1回だけ：その後の編集は、開いているウインドウに自動的に反映される。</li>
  <li>MarsDawn アプリがインストールされていなければ、一度だけそう伝えて作業を続け、再試行はしない。PDF を作るために <code>open</code> を使うことは絶対にない。</li>
  <li><code>--folder</code>（marsdawn 0.5.1 以降）を使ったときは、フォルダを「表示された」ではなく「表示を依頼した」と報告する：判断するのはアプリで、結果は返ってこない。</li>
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
  <li>MarsDawn とは何か、1ページで：<a href="/ja/">ホームページ</a>。</li>
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

<h2>marsdawn 0.6.0</h2>
<p>2026年10月1日。MarsDawn が Mac App Store で公開。</p>
<ul>
  <li>アプリがインストールされていないとき、<code>marsdawn open</code> は Mac App Store の MarsDawn を案内します。</li>
  <li>README とエージェントスキルで <code>marsdawn open .</code> と <code>--folder</code> を説明します。MarsDawn 1.0.0 はフォルダをウインドウのサイドバーに表示します。</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>2026年9月25日。フォルダの状態、Mermaid エラーの全文、そのほかの修正。</p>
<ul>
  <li><code>marsdawn open --folder</code> が、フォルダがどうなったかを返せるようになりました。状態を返すアプリが相手なら、<code>--wait</code> の秒数（デフォルトは 2 秒）まで応答を待ち、<code>--json</code> に <code>attached</code> や <code>needsUser</code> などの状態が入ります。</li>
  <li>Mermaid の図を解析できないとき、最初の行だけでなく Mermaid のエラーメッセージ全文を表示します。行番号もファイルの先頭から数えた値になりました。</li>
  <li>フロントマターの終わりを探すのは 1,000 行までになりました。閉じていないブロックがあっても、大きなファイルを毎回最後まで調べることはありません。</li>
  <li>脚注の戻りリンクのラベルを、アプリが PDF の書き出しとプリント用に翻訳して渡せるようになりました。このラベルはページには印刷されず、<code>marsdawn export</code> では英語のままです。</li>
  <li>同梱の highlight.js を、KaTeX や Mermaid と同じく、バージョン、入手元、SHA-256 で記録するようになりました。</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>2026年9月24日。脚注、コントラスト、フォルダ。</p>
<ul>
  <li>書き出した PDF に脚注が表示されます。参照には番号が付き、注は本文のあとに並びます。</li>
  <li>すべてのテーマが、ライトでもダークでも WCAG AA のコントラストを満たします。Classic は白黒になりました。</li>
  <li><code>marsdawn skill</code> は、インストールされている marsdawn に合ったエージェントスキルを出力します。</li>
  <li>見つかった MarsDawn がフォルダを表示できないとき、<code>marsdawn open</code> は成功を報告せず、コード 6（<code>app_cannot_open_folders</code>）で終了します。</li>
  <li>書き出したページに描かれるプレースホルダが、ドイツ語、フランス語、スペイン語、韓国語にも対応しました。</li>
  <li>相対パスがとても長くても、画像のプレースホルダにその先の絶対パスが表示されなくなりました。</li>
  <li><code>MARSDAWN_APP_PATH</code> は、MarsDawn アプリを指しているときだけ使われます。</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>2026年9月19日。PDF 書き出しと、コマンドラインからファイルを開くこと。</p>
<ul>
  <li>書き出した PDF のテキストレイヤーを、中国語、日本語、韓国語について修正しました。</li>
  <li><code>marsdawn open --background</code> はファイルを開きますが、MarsDawn を前面には出しません。</li>
  <li><code>marsdawn open</code> にフォルダを渡すと、MarsDawn がウインドウのサイドバーに表示します（MarsDawn 1.0.0 以降）。</li>
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
