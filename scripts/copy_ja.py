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
