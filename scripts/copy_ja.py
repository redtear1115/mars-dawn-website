"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
For now it has the privacy policy and support pages only, which the App Store listings link to.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


# /themes/agents/ prose (machine draft of the en text, needs-i18n; plan PLAN-web-theme-tuning W3).
# The tables come from scripts/theme_agents.py, not from here.
THEME_AGENTS = {
    "title": "エージェントと MarsDawn のテーマを作る · MarsDawn",
    "description": "MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。",
    "label": "エージェントとテーマを作る",
    "h1": "エージェントとテーマを作る",
    "lede": "MarsDawn のプレビューテーマを作る AI エージェント向けの参考資料です。エージェントは <code>theme.json</code> を1つ書き、コマンドラインツール <code>marsdawn</code> で検証してレンダリングし、リンクを渡します。人は<a href=\"/themes/new/\">「テーマを作る」</a>ページで見た目を整えて投稿します。下のフィールド表は kit のソースコードから直接読み取ったもので、チェックによって一致が保たれています。",
    "summary": "<strong><code>theme.json</code> を書き、終了コードが 0 になるまで <code>marsdawn theme validate theme.json --require-complete --json</code> を実行し、<code>marsdawn theme preview</code> でライトとダークをレンダリングしてから、人にリンクを渡します。</strong>テーマはパラメーターだけで、CSS は含みません。",
    "what_h": "テーマとは",
    "what_items": [
        "ライトとダークそれぞれの<strong>色</strong>：基本パレットと、任意の構文色・図の色。どれも <code>#RRGGBB</code> です。",
        "<strong>フォントデザイン</strong>：<code>sans</code>、<code>serif</code>、<code>rounded</code> のいずれか。",
        "<strong>閉じたスタイルオプションの集合</strong>：決まった範囲の数値と、決まったリストから選ぶ値。スタイルオプションの色は常に <code>accent</code> のようなパレットのロールで、色の値を直接書くことはありません。",
        "<strong>表示用の文字列</strong>：名前と概要、任意で作者とライセンス。"
    ],
    "what_note": "下の表にないキーはエラーで、同じキーを2回書くこともエラーです。ファイルは最大 16,384 バイトです。",
    "loop_h": "検証とレンダリング",
    "loop_intro": "<code>theme.json</code> のあるフォルダで実行します。<code>marsdawn</code> ツールが必要です。<a href=\"/cli/agents/\">AI エージェント向け marsdawn</a>を参照してください。",
    "loop_items": [
        "終了コード：0 は有効、1 は無効（ルール ID 付き）、2 はファイルが見つからない、64 は使い方の誤りです。<code>preview</code> にはさらに、PNG がすでにある場合の 4（<code>--force</code> を付けるか別の名前にします）と、レンダリング失敗の 5 があります。",
        "<code>--json</code> を付けると、無効なテーマは問題を <code>issues</code> の下に並べ、それぞれに <code>rule</code> ID、<code>path</code>、<code>message</code> が付きます。直して再実行してください。",
        "<code>--require-complete</code> は公開するテーマ向けのチェックで、両方のパレットに <code>syntax</code> と <code>diagram</code> の色も求めます。",
        "<code>css</code> はプレビューが使う CSS を出力し、<code>preview</code> はサンプル文書を PNG にレンダリングします。どちらも先に検証するので、無効なテーマはレンダリングされません。",
        "テーマを渡す前に、ライトとダークの PNG を両方確認してください。"
    ],
    "start_h": "組み込みテーマから始める",
    "start_intro": "4つの組み込みテーマのどれかをコピーして変更します。どれも完全で有効なファイルです。",
    "start_dawn": "既定のテーマで、下の例",
    "start_classic": "より落ち着いた、文書らしいパレット",
    "start_modern": "より涼しげで現代的なパレット",
    "start_vivid": "より明るくコントラストの強いパレット",
    "ex_h": "例：Dawn",
    "ex_intro": "<code>dawn.json</code> を1バイトも変えずに載せています。スタイルオプションは <code>hr</code> の細いアクセントカラーの線だけです。",
    "fields_h": "フィールド",
    "fields_intro": "下のオブジェクトはどれも同じように読まれます。<code>required</code> はキーが必須という意味で、載っていないキーはエラーです。",
    "types_note": "型：<code>string</code>、<code>integer</code>、<code>number</code>、<code>boolean</code>、<code>map</code>（言語タグからテキストへ）、<code>enum</code>（挙げた値のいずれか）、<code>role</code>（パレットのロール）、<code>object</code>（リンク先の表）。型の後ろの <code>[]</code> はリストを表します。",
    "c_field": "フィールド",
    "c_type": "型",
    "c_presence": "必須か",
    "c_values": "値と備考",
    "c_option": "オプション",
    "c_kind": "type",
    "c_min": "最小",
    "c_max": "最大",
    "c_step": "刻み",
    "see_roles": "パレットのロール",
    "see_ranges": "範囲",
    "publish_note": "（公開には必須。<code>--require-complete</code> で検証）",
    "h_kinds": "type を持つオプション",
    "kinds_intro": "これらのスタイルオプションは <code>type</code> を持つオブジェクトです。それぞれの <code>type</code> は、そこに挙げたフィールドだけを受け付けます。",
    "h_roles": "パレットのロール",
    "roles_intro": "パレットのロールは次の名前のいずれかです。",
    "h_numbers": "数値",
    "numbers_intro": "数値は最も近い刻みの倍数に丸められ、最小と最大の間に収まる必要があります。収まらない場合のルールは <code>number.range</code> です。",
    "n_schemaVersion": "常に <code>1</code>。",
    "n_id": "1〜32文字：小文字と数字を、単独のハイフンでつないだ区切り。例：<code>calm-green</code>。",
    "n_version": "<code>MAJOR.MINOR.PATCH</code>。例：<code>1.0.0</code>。",
    "n_name": "言語タグからテキストへ。<code>en</code> は必須で、ほかのキーは <code>zh-Hant</code> のような言語タグです。各テキストは最大48文字で、リンクや改行は使えません。",
    "n_summary": "<code>name</code> と同じ形式で、テキストごとに最大120文字。",
    "n_scenarios": "1つまたは2つ、重複不可。テーマが満たすべきコントラストの水準を決めます。",
    "n_license": "SPDX 識別子。例：<code>Apache-2.0</code>。投稿されたテーマは Apache-2.0 で公開されます。",
    "n_author_name": "最大64文字、リンク不可。",
    "n_author_github": "GitHub のログイン名。投稿の場合は、投稿する人のものを入れます。",
    "n_hex": "<code>#</code> と16進数6桁。例：<code>#1C1C1C</code>。",
    "n_inline_code": "<code>text</code> か構文ロールのみ：<code>keyword</code>、<code>string</code>、<code>comment</code>、<code>number</code>、<code>function</code>、<code>type</code>。",
    "n_gradient": "ロールを2つまたは3つ。",
    "rules_h": "ほかに検証されること",
    "rules_items": [
        "<strong>コントラスト。</strong><code>background</code> 上の <code>text</code> のように、プレビューが描く色の組はすべて、テキストは 4.5:1、線やそのほかの非テキストは 3:1 に達する必要があります。指定したシナリオによって、一部の色は 4.5:1 に引き上げられます。メッセージには、その組と比率、必要な比率が示されます。",
        "<strong>文字列。</strong>名前、概要、作者名が空、長すぎる、またはリンク・制御文字・不可視文字・双方向書式文字を含む場合は拒否されます。",
        "<strong>ルール ID。</strong>すべての問題には <code>contrast.pair</code>、<code>color.hex</code>、<code>number.range</code>、<code>id.pattern</code>、<code>schema.unknownKey</code>、<code>palette.incomplete</code> などの ID が付きます。ID と <code>path</code> が示すとおりにファイルを直してください。"
    ],
    "link_h": "リンクとして渡す",
    "link_intro": "<a href=\"/themes/new/\">「テーマを作る」</a>ページは、リンクからテーマを開けるので、人が見た目を整えられます。リンクは、そのページのアドレス、<code>#theme=</code>、パディングなしの base64url にしたファイルのバイト列でできています。ファイルは最大 16,384 バイトです。次の1行で、macOS と Linux の zsh と bash でリンクを作れます。",
    "link_note": "テーマはブラウザがサイトに送らない <code>#</code> の後ろに入り、サイトもそれをどこにも送りません。ただしリンクはシェルとブラウザの履歴に残り、リンクを貼った相手はテーマを読めます。",
    "submit_h": "投稿する",
    "submit_intro": "エージェントがファイルとリンクを用意し、投稿は人が行います。どちらの方法でも Developer Certificate of Origin と Apache-2.0 での公開への確認が必要で、この確認は人が自分で行います。エージェントがチェックボックスにチェックしたり、代わりに署名したりすることはありません。",
    "submit_issue": "<strong>Issue。</strong>人がリンクを開いて「テーマを作る」ページの <strong>Submit</strong> を押すか、<a href=\"{issue_url}\">Issue フォーム</a>を開いて JSON を <em>Theme</em> に貼り付けます。ワークフローがテーマを検証して返信します。",
    "submit_pr": "<strong>Pull request。</strong><code>themes/&lt;id&gt;/theme.json</code> だけを変更し、<code>author.github</code> を pull request の作者のログイン名にして、すべてのコミットに <code>git commit -s</code> で署名します。ルールは <a href=\"{contributing_url}\">CONTRIBUTING.md</a> にあります。",
    "submit_note": "投稿されたテーマの作者名、名前、概要、GitHub のログイン名は永久に公開されます。<code>author.name</code> には、その人が公開してよいと考える名前を入れてください。",
    "gallery_h": "公開されているテーマ",
    "gallery_p": "公開されているテーマの見た目は、<a href=\"/themes/gallery/\">テーマギャラリー</a>で確認できます。"
}


# /features/ prose (machine draft of the en text, needs-i18n; owner-approved en/zh-Hant copy of 2026-10-15).
# UI labels quoted in it are the app's own strings in this language (Localizable.xcstrings and the
# Welcome guide, tag 1.1.0). The links, the button and the screenshots come from the site, not from here.
FEATURES = {'title': '機能一覧：Mac 用 Markdown エディタを1ページで · MarsDawn',
 'description': 'Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF '
                'とプリントのページ。',
 'h1': 'MarsDawn でできることを、1ページで。',
 'intro': ['MarsDawn は Mac 用の Markdown エディタです。片側で書き、もう片側で整形されたページを読めて、図や数式、コードもそのまま描画されます。独自の AI '
           'モデルは持っていません。エージェントが書いたものを読むために、そして自分の文章を書くために作られています。作業の場が会議の席やファイル棚に移るときは、きれいなページをプリントしたり書き出したりできます。',
           '以下の各セクションで、アプリにできることを説明し、さらに詳しいページへのリンクを付けています。'],
 'sections': [{'id': 'read',
               'h2': 'エージェントが書いたものを読む',
               'lead': '',
               'lead_links': [],
               'items': [{'h': 'ソースとプレビューを並べて表示',
                          'p': 'Markdown '
                               'ファイルを開くと、整形されたページがソースの隣に表示されます（⌘2）。ソースのみ（⌘1）、プレビューのみ（⌘3）にも切り替えられます。両側は一緒にスクロールし、ページは入力に合わせて更新されます。',
                          'links': ['native']},
                         {'h': 'アウトラインとファイルのサイドバー',
                          'p': 'サイドバーの「アウトライン」には書類の見出しが並び、クリックするとその位置に移動します。フォルダを開くと「ファイル」タブに中身が一覧表示され、エージェントが書き込んでいるあいだも新しいファイルが自動的に現れます。フォルダが '
                               'git のチェックアウトなら、見出しにブランチまたはワークツリーの名前が表示されます。',
                          'links': ['reading-agent-output']},
                         {'h': '正確な行を示す',
                          'p': '「編集 ▸ 参照をコピー」は、現在の位置を docs/plan.md:42 のようにパスと行番号でコピーします。「AI '
                               '用にコピー」は、その下に選択したテキストも付けます。どちらもエージェントのチャットにそのままペーストできます。',
                          'links': ['reading-agent-output']},
                         {'h': 'ファイル間のリンクをたどる',
                          'p': 'プレビューで別の Markdown ファイルへのリンクをクリックすると、MarsDawn '
                               'がそのファイルを開き（すでに開いていれば前面に出し）、見出しの位置までスクロールします。',
                          'links': []}]},
              {'id': 'paper',
               'h2': '紙の上で、人と人のあいだで',
               'lead': 'すべての作業が画面の上で行われるわけではありません。MarsDawn '
                       'がプリントして書き出すページは画面で読むページそのものなので、人が集まり、読み、記録を残す場面で使えます。',
               'lead_links': [],
               'items': [{'h': '会議で',
                          'p': 'ページをプリントするか、同じ PDF '
                               'を全員に送れば、1つの画面を囲むのではなく、全員が同じ書類で作業できます。同じファイルを持っていれば改ページ位置も同じなので、「3ページの表」は誰にとっても同じものを指します。そのあと、人が決定事項を、プリントした紙の上やメモに書き留めます。会議メモのテンプレートは決定事項から始まり、各アクションアイテムに担当者を置きます。',
                          'links': ['pdf', 'templates/meeting-notes']},
                         {'h': 'ペンで読む',
                          'p': 'ペンを使うほうが頭に入る人もいます。線を引き、余白に書き込み、記憶に残すためです。書類をプリントして、紙の上でそうしてください。MarsDawn '
                               '自体には注釈ツールがないので、PDF に書き込みたい場合は、お使いの PDF アプリを使ってください。',
                          'links': ['pdf']},
                         {'h': '紙での記録',
                          'p': '分野によっては、いまも紙で保管します。会計はその一例です。MarsDawn '
                               'は保管やコンプライアンスについて何も謳っていません。できるのは、きれいに改ページされたページをプリントして書き出すことです。図は描画され、短いコードブロックは途中で切れず、テーマのライトの配色で出力されます。紙がいまも正式な記録である場面で使ってください。',
                          'links': ['pdf']},
                         {'h': 'Markdown を使わない人に渡す',
                          'p': 'PDF はどんなアプリでも開け、Markdown の知識も要らないので、上司やクライアントに送るのにも向いています。',
                          'links': ['sharing-exported-pdfs']}]},
              {'id': 'write',
               'h2': '書く、レイアウトする',
               'lead': '',
               'lead_links': [],
               'items': [{'h': 'プレーンな Markdown、ハイライト付き',
                          'p': '太字、斜体、取り消し線、インラインコード、リンク、引用、ToDo リストがすべて使えます。エディタは Markdown '
                               'の構文に色を付け、その色はプレビューのテーマと揃います。',
                          'links': ['native']},
                         {'h': '拡大・縮小、行番号、ステータスバー',
                          'p': 'ソースとプレビューを一緒に 50% から 300% まで拡大・縮小できます。ソースの横には行番号の欄があり、ステータスバーにはカーソルの行と列、'
                               'そして書類または選択範囲の文字数、単語数、読む時間が表示されます。',
                          'links': []},
                         {'h': 'イメージ',
                          'p': '書類を保存してから、イメージをエディタにドラッグまたはペーストします。MarsDawn は書類の横の assets '
                               'フォルダにコピーし、リンクを書き込みます。Web '
                               '上のイメージは「イメージを読み込む」を押すまで表示されないので、書類を開いても、読んだことがサーバに知られることはありません。',
                          'links': ['yours']},
                         {'h': 'フロントマターは邪魔になりません',
                          'p': 'ファイル先頭のフロントマター（front '
                               'matter）のブロックは、プレビューとクイックルックでは折りたたまれた「書類の情報」として表示され、PDF には出力されません。',
                          'links': []},
                         {'h': '8つの言語',
                          'p': 'アプリは、英語、繁体字中国語、簡体字中国語、日本語、ドイツ語、フランス語、スペイン語、韓国語に対応しています。',
                          'links': ['native']}]},
              {'id': 'diagrams',
               'h2': '図、コード、数式',
               'lead': '',
               'lead_links': [],
               'items': [{'h': 'Mermaid の図',
                          'p': 'mermaid '
                               'と指定したコードブロックは図として描画されます。図に誤りがあると、プレビューにはそのソースとエラーが下に表示され、メッセージをクリックするとその行に移動します。',
                          'links': ['mermaid-preview-mac']},
                         {'h': 'ハイライトされたコード',
                          'p': 'コードブロックは、一般的なほとんどの言語でハイライトされます。先頭の ``` の後ろに言語名を書くだけです。',
                          'links': []},
                         {'h': '数式',
                          'p': 'KaTeX の構文で書いた数式は、プレビューとクイックルックで描画され、書き出した PDF にも反映されます。',
                          'links': ['reviewing-ai-output']}]},
              {'id': 'themes',
               'h2': 'テーマ、PDF、プリント',
               'lead': '',
               'lead_links': [],
               'items': [{'h': '4つのテーマ、ライトとダーク',
                          'p': '夜明け、クラシック、モダン、ビビッドには、それぞれライトとダークがあります。設定で選ばない限り、MarsDawn は Mac '
                               'の外観モードに合わせます。「表示 ▸ プレビューのテーマ」またはツールバーのパレットボタンから選べます。',
                          'links': ['themes']},
                         {'h': 'そのほかのテーマ',
                          'p': '「設定 ▸ 外観モード ▸ テーマを追加…」で、追加のプレビューテーマのギャラリーが開きます。インストールしたものは「表示 ▸ '
                               'プレビューのテーマ」に並び、「取り除く」で削除できます。ギャラリーは開いているあいだだけオンラインになります。',
                          'links': ['themes/gallery', 'themes/new']},
                         {'h': 'PDF として書き出す、またはプリント',
                          'p': '「ファイル ▸ PDF として書き出す…」は改ページ済みの PDF を保存し、「ファイル ▸ '
                               'プリント…」は同じページをプリントします。Mermaid '
                               'の図は描画され、コードはハイライトを保ち、改ページでは見出しが節から離れたり、短いコードブロックや図が途中で切れたりしないようにします。ダークで読んでいても、PDF '
                               'は常にテーマのライトの配色です。',
                          'links': ['pdf']}]},
              {'id': 'files',
               'h2': 'ファイル、タブ、クイックルック',
               'lead': '',
               'lead_links': [],
               'items': [{'h': 'ウインドウとタブ',
                          'p': '書類はそれぞれ別のウインドウで開きます。「ウインドウ ▸ '
                               'すべてのウインドウを結合」を選ぶと、開いているウインドウを1つのウインドウのタブにまとめられます。自動保存は入力中に働きます。',
                          'links': ['native']},
                         {'h': 'Finder のクイックルック',
                          'p': 'Finder で Markdown ファイルを選んでスペースバーを押すと、図も含めて整形された状態で読めます。クイックルックは '
                               'MarsDawn で選んだテーマを使い、その外観モードの設定に従います。',
                          'links': ['native']},
                         {'h': 'そのほかのファイル',
                          'p': 'MarsDawn では、テキストファイル（.txt、.log、ソースコード）と PDF も開けます。UTF-8 '
                               'のテキストはそのまま編集でき、ソースのみの表示になります。PDF '
                               'は、ページのサムネール、拡大・縮小、検索を備えたビューアで開きます。',
                          'links': []},
                         {'h': 'ファイルはあなたのもの',
                          'p': 'アカウントも、同期も、クラウドもありません。書類は保存した場所に残り、MarsDawn '
                               'があなたに関するデータを収集することはありません。',
                          'links': ['yours']}]},
              {'id': 'agents',
               'h2': 'エージェントとスクリプト向け',
               'lead': '',
               'lead_links': [],
               'items': [{'h': '無料のコマンドラインツール',
                          'p': '無料の marsdawn ツールは、Homebrew で別途インストールします。marsdawn export は Markdown '
                               'ファイルを、MarsDawn のプレビューと同じ見た目の PDF にします。アプリは要りません。--theme '
                               'でテーマを、用紙サイズは A4 か Letter を選べます。marsdawn open '
                               'はファイルをアプリで開いて確認できるようにし、行を指定することもできます。こちらはアプリのインストールが必要です。',
                          'links': ['cli']},
                         {'h': 'スクリプトが読める出力',
                          'p': '--json を付けると、どちらのコマンドも、エージェントやスクリプトが解析できる結果を返します。',
                          'links': ['cli/agents']},
                         {'h': 'スキルと MCP サーバ',
                          'p': 'エージェント用のスキルファイルは、コーディングエージェントに、書いたものを MarsDawn '
                               'で開いてあなたの確認に回すことを教えます。シェルのないクライアント向けには、別の MCP サーバが同じ export を実行します。',
                          'links': ['cli/skill', 'cli/mcp']},
                         {'h': 'AI は入っていません',
                          'p': 'MarsDawn は独自の AI '
                               'モデルを持っていません。エージェントが書いたものを要約したり採点したりせず、長くて変わり続けるファイルを読みやすく保つだけで、読むのはあなたです。',
                          'links': ['limits']}]},
              {'id': 'siri',
               'h2': 'Siri とショートカット',
               'lead': '「ショートカット」App で MarsDawn を検索すると、3つのアクションが見つかります：「新規 Markdown '
                       '書類」（テンプレートから）、「受信トレイにメモを追加」、「最近使った書類を開く」。メモは、「MarsDawn ▸ 設定… ▸ '
                       'メモフォルダ」で選んだフォルダの Inbox.md に追加されます。',
               'lead_links': ['native'],
               'items': []}],
 'devices': {'h2': 'Mac で書いて、出先で読む',
             'lead': 'エージェントは Mac で作業します。その計画やレポートは、iPhone や iPad でも読めます。',
             'steps': [
                       'Mac で：エージェントの計画やレポートを、iCloud Drive のフォルダに保存します。',
                       'iPhone や iPad で：MarsDawn で「開く」をタップし、同じファイルを選びます。Mermaid の図、数式、コード、表がきちんと表示され、アウトラインと選んだテーマも使えます。',
                       'Mac に戻って：編集を続けたり、PDF に書き出したりできます。'],
             'buy': '同じ Apple Account なら、1 回のトライアルと 1 回のロック解除で、Mac、iPhone、iPad の MarsDawn をすべて利用できます。',
             'limits': 'iPhone と iPad の MarsDawn は閲覧専用です。開けるのは Markdown とプレーンテキストのファイルだけで、編集や PDF の書き出しはできません。読むのは iCloud Drive に置いたファイルで、MarsDawn 自体にはクラウドサービスがありません。'},
 'cta': {'h2': 'Mac で試してみる',
         'p1': 'MarsDawn は無料でダウンロードできます。14日間はすべての機能を試せて、その後は USD 4.99 '
               'で一度だけ購入します。サブスクリプションもアカウントも不要です。macOS 26 以降が必要です。',
         'trial': ['試用のしくみ：', 'pay-once'],
         'left': ['。あえて入れていないこと：', 'limits'],
         'tail': '。'}}


# Machine drafts (needs-i18n; Grok reviews them): the /view-markdown-on-mac/ revision and the new
# /mermaid-preview-mac/ page (website #227), the same shape as build_pages.OPEN_MD and .MERMAID. The
# Mermaid example is the app's own Welcome guide at tag 1.1.0; menu names are the app's strings at 1.1.0
# and Apple's own Finder strings for this language.
OPEN_MD = {'title': 'Mac で .md ファイルを開く方法：ダブルクリック、標準アプリ、クイックルック · MarsDawn',
 'description': 'Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn '
                'でレンダリングして読めます。',
 'h1': 'Mac で .md ファイルを開く方法。',
 'short': 'ダブルクリックすれば開きます。テキストエディタで開いて、見出しや太字ではなく `#` や `**` が見えても、ファイルは壊れていません。`.md` '
          'ファイルはプレーンテキストで、そのエディタは文字をそのまま表示しているだけです。Markdown をレンダリングするアプリ（たとえば '
          'MarsDawn）で開き、そのアプリを標準に設定すれば、以後すべての `.md` ファイルがそこで開きます。',
 'steps_h2': 'Mac で .md ファイルを開く',
 'steps': '1. **ファイルをダブルクリックする。** Mac が `.md` に設定しているアプリで開きます。Markdown '
          'のアプリがなければ、たいていプレーンテキストエディタで、整ったページではなく記号が見えます。\n'
          '2. **アプリを自分で選ぶ。** Control キーを押しながらファイルをクリックし、「このアプリケーションで開く」からアプリを選びます。または「ファイル ▸ '
          '情報を見る」（⌘I）を選び、「このアプリケーションで開く:」でアプリを選んで「すべてを変更…」をクリックすると、同じ種類のファイルがすべてそのアプリで開きます。MarsDawn は '
          '`.md`、`.markdown`、`.mdown`、`.mkd`、`.mkdn` のファイルを開けます。\n'
          '3. **開かずにプレビューする。** Finder でファイルを選んでスペースキーを押します。MarsDawn '
          'をインストールしていれば、クイックルックにレンダリングされたページが表示され、図も含まれます。',
 'read_mermaid': '- [Mermaid](/ja/mermaid-preview-mac/) のフローチャートとシーケンス図がプレビューに描画され、コードブロックはハイライトされます。',
 'faq_h2': 'よくある質問',
 'faq': [['.md ファイルとは？',
          '`.md` ファイルは、Markdown で書かれたプレーンテキストのファイルです。Markdown は簡単な文字でテキストに印を付ける書き方で、`#` は見出し、`**` '
          'で囲むと太字、縦線は表のセルになります。拡張子 `.markdown`、`.mdown`、`.mkd`、`.mkdn` も同じものです。開発者は README やドキュメントに使い、AI '
          'エージェントも計画やレポートを `.md` ファイルで返してくることがよくあります。'],
         ['.md ファイルがプレーンテキストで開き、# や ** だらけなのはなぜ？',
          'もともとプレーンテキストで、プレーンテキストエディタはそのまま表示するからです。ファイルに問題はありません。見出し、太字、表、図を見るには、Markdown '
          'をレンダリングするアプリで開いてください。MarsDawn では、レンダリングされたページがソースの隣に表示されます。'],
         ['開くと文字化けするのはなぜ？',
          '文字化けは、たいていファイルが UTF-8 以外の文字エンコーディングで保存されていて、開いたアプリが推測を誤ったために起こります。対処は、UTF-8 '
          'のコピーを保存することです。MarsDawn は UTF-8 '
          'ではないプレーンテキストファイルを読み取り専用で開き、ウインドウ上部のバーに読み込んだエンコーディングを表示します。そこにある「UTF-8 で別名保存…」、または「ファイル ▸ '
          '別名で保存…」（⌥⇧⌘S）で、編集できる UTF-8 のコピーを書き出せます。'],
         ['.md ファイルを PDF にできる？',
          'できます。MarsDawn で「ファイル ▸ PDF として書き出す…」（⌥⌘E）または「ファイル ▸ '
          'プリント…」を選ぶと、ページ分けされ、図が描画され、コードはハイライトされたまま、テーマのライトの配色で出力されます。アプリがなくても、無料の `marsdawn export` '
          'コマンドラインツールで同じ PDF を作れます：`marsdawn export notes.md`。[PDF 書き出し](/ja/pdf/)と[Markdown から PDF '
          'へ](/ja/markdown-to-pdf/)をご覧ください。'],
         ['AI エージェントが書いた .md ファイルも開ける？',
          'はい、MarsDawn はそのために作られています。ファイルを開いて、レンダリングされたページをソースの隣で読みます。エージェントが修正したら、もう一度開きます。エージェントが '
          '`marsdawn open plan.md` を実行して、MarsDawn '
          'でファイルを開いてくれることもできます。[エージェントが返してくるものを読む](/ja/reading-agent-output/)をご覧ください。']],
 'next_new': '- Markdown ファイルの中の図：[Mac で Mermaid をプレビューする](/ja/mermaid-preview-mac/)。',
 'opening_html': '<code>.md</code> ファイルはプレーンテキストです。見出し、太字、表、図は記号で書かれています。見出しには <code>#</code>、太字は '
                 '<code>**</code> で囲む、表はパイプで区切る、図は <code>mermaid</code> '
                 'コードブロックといった具合です。プレーンテキストエディタで開くと、これらの記号がそのまま見えます。作者の意図どおりにページを読むには、何かがそれをレンダリングする必要があります。',
 'read_h2': 'MarsDawn で読む',
 'read_p1_html': 'MarsDawn は Mac 向けの Markdown エディタです。Mac App Store から無料でダウンロードでき、14日間すべての機能を試したあと、USD 4.99 '
                 'の一度きりの購入でロックを解除できます。サブスクリプションもアカウントもありません。macOS 26 以降が必要です。',
 'download': 'Mac App Store で MarsDawn を無料でダウンロード',
 'read_p2_html': '<code>.md</code> ファイルを開くと、ソースの隣でレンダリングされたページを読めます。',
 'read_b1_html': '入力すると同時にプレビューが更新され、2つのペインは一緒にスクロールします。',
 'read_b4_html': '何かを変更したいときは、ソースがすぐそこにあります。MarsDawn はビューアだけでなくエディタでもあります。',
 'agents_html': 'もしそのファイルを AI エージェントが書いたなら、これはまさに MarsDawn '
                'が想定しているループです。エージェントが書き、あなたがレンダリングされたページを読み、エージェントが修正します。<a '
                'href="/ja/">ホームページ</a>と、エージェントにファイルを開かせる方法については<a href="/ja/cli/agents/">AI エージェント向け '
                'marsdawn</a>をご覧ください。その読み方がなぜ重要か、計画をどうレビューするかは、<a '
                'href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a>と<a '
                'href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>にあります。',
 'pdf_h2': 'アプリなしで：PDF に変換する',
 'pdf_p1_html': '無料の <code>marsdawn</code> コマンドラインツールは、Markdown ファイルをどの Mac でも開ける PDF '
                'にレンダリングします。表、数式、Mermaid 図、ハイライトされたコードはすべてレンダリングされ、MarsDawn アプリすら含め、他に何もインストールする必要はありません。',
 'pdf_p2_html': '<code>export</code> は Markdown ファイルの隣に <code>notes.pdf</code> を書き出し、<code>open</code> '
                'はそれをあなたの PDF ビューアで表示します。macOS 15 以降が必要です。実際に書き出したページを使った解説は、<a '
                'href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>にあります。',
 'next_h2': '次に',
 'next_items_html': ['コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。',
                     'MarsDawn ができないこと：<a href="/ja/limits/">一覧はこちら</a>。']}

MERMAID = {'title': 'Mac で Mermaid をプレビュー、Markdown の隣で · MarsDawn',
 'description': 'Mac で Mermaid の図を Markdown の隣に描画：リアルタイムプレビュー、クイックルック、PDF 書き出し。図に誤りがあると、エラーとその行が表示されます。',
 'h1': 'Mac で Mermaid をプレビューする。',
 'intro': 'Mermaid を使うと、Markdown ファイルの中に図をテキストで書けます。多くのエディタは、そのテキストを見せるだけです。MarsDawn '
          'は図を描画します。ソースの隣のプレビューで、Finder のクイックルックで、書き出した PDF の中で。',
 'example_h2': '図をテキストで書く',
 'example': '図を、`mermaid` と指定したコードブロックに入れます：',
 'code': '```mermaid\n'
         'flowchart LR\n'
         '    Write[Markdown を書く] --> Preview[リアルタイムプレビュー]\n'
         '    Preview --> Export{共有しますか？}\n'
         '    Export -- PDF --> PDF[ファイル ▸ PDF として書き出す…]\n'
         '    Export -- プリント --> Print[ファイル ▸ プリント…]\n'
         '```',
 'after': 'MarsDawn では、このブロックがフローチャートになります。「Markdown を書く」から「リアルタイムプレビュー」へ、そして「共有しますか？」の分岐から PDF とプリントの 2 '
          'つの道に分かれます。',
 'where_h2': '図が描画される場所',
 'where': '- **プレビューで。** ファイルを開くと、図がソースの隣に表示されます（⌘2）。入力するたびにページが更新され、2 つのペインは一緒にスクロールします。\n'
          '- **クイックルックで。** Finder でファイルを選んでスペースキーを押すと、そこでも図が描画されます。\n'
          '- **PDF で。** 「ファイル ▸ PDF として書き出す…」と「ファイル ▸ プリント…」は、図をページに描き込みます。ページの区切りは、図を途中で分断しないようにします。PDF '
          'はテーマのライトの配色です。\n'
          '- **コマンドラインで。** 無料の `marsdawn export` ツールは、アプリなしで同じ図を PDF に描画します。[コマンドライン](/ja/cli/)をご覧ください。\n'
          '- **外観に合わせて。** プレビューの外観モードの設定は図にも適用されるので、図はライトかダークに従います。',
 'error_h2': '図に誤りがあるとき',
 'error': 'Mermaid '
          'が図を描画できないとき、プレビューにはその図のソースが表示され、その下にエラーメッセージ全文が出ます。エラーが行を示している場合は、メッセージをクリックするとエディタがその行へ移動します。`marsdawn '
          'export --json` は描画に失敗した図を `diagramErrors` で報告するので、スクリプトやエージェントは図が描画されなかったことを知ることができます。',
 'know_h2': '知っておくこと',
 'know': '- 編集するのは Mermaid のテキストです。図のビジュアルエディタはなく、プレビューで四角形をドラッグすることもできません。\n'
         '- どの種類の図が描画できるかは、アプリに入っている Mermaid のバージョンによります。MarsDawn 1.1.0 には Mermaid 12.0.0 が入っています。kit '
         'の書き出しテストは、フローチャート、シーケンス図、クラス図、状態遷移図、ER 図、ガントチャート、円グラフ、マインドマップ、ジャーニー図、タイムライン、git グラフなどの文書を描画します。\n'
         '- MarsDawn には AI '
         'モデルがないので、図を書いてはくれません。[フローチャートテンプレート](/ja/templates/flowchart/)には、自分のエージェントに渡せるプロンプトがあります。',
 'next_h2': '次に',
 'next': '- すでに描画できる図から始める：[フローチャートテンプレート](/ja/templates/flowchart/)。\n'
         '- 書き出す：[PDF 書き出し](/ja/pdf/)。スクリプトから書き出すなら[コマンドライン](/ja/cli/)。\n'
         '- ファイルの開き方がわからない？[Mac で .md ファイルを開く方法](/ja/view-markdown-on-mac/)をご覧ください。',
 'try_h2': 'Mac で試す',
 'try': 'MarsDawn は無料でダウンロードできます。14 日間すべての機能を試したあと、USD 4.99 の一度きりの購入でロックを解除できます。サブスクリプションもアカウントもありません。macOS '
        '26 以降が必要です。\n'
        '\n'
        '[今すぐダウンロードして試す]({App Store 連結})'}


# Machine draft (needs-i18n; Grok reviews it): the revised /vs/macmd-viewer/, the same shape as
# build_pages.VS_MACMD. [S#] marks in a cell or sentence link to the sources list on the page.
VS_MACMD = {'title': 'MacMD Viewer と MarsDawn：Markdown のビューアか、エディタか · MarsDawn',
 'description': 'MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD '
                '4.99 を一度だけ。項目ごとの比較、出典つき。',
 'h1': 'MacMD Viewer と MarsDawn。',
 'intro': ['どちらも、Markdown を整ったページとして読むための Mac アプリです。MacMD Viewer は `.md` '
           'ファイルを開いて表示します。設計上、読み取り専用で、ファイルへの変更は一切保存しません。MarsDawn '
           'は同じようなレンダリングされたプレビューの隣にエディタを置くので、ひとつのウインドウで書いて読めます。このページでは両者を項目ごとに並べ、MacMD Viewer '
           'についての事実にはすべて出典を付け、MacMD Viewer のほうが向いている場合も述べます。',
           'MacMD Viewer 自身のサイトとリポジトリで 2026 年 10 月 15 日に確認しました（バージョン 1.7.0、2026 年 10 月 10 '
           '日公開）。古くなっている点があれば、[サポートページ](/ja/support/)の連絡先までお知らせください。'],
 'tables': [{'h2': 'どんなもので、何ができるか',
             'head': ['', 'MacMD Viewer', 'MarsDawn'],
             'rows': [['種類',
                       'ビューア：「読み取り専用で、ソースファイルへの変更は保存しない」[S1, S9]',
                       'ライブプレビューつきのエディタ：左に Markdown、右にレンダリングされたページ。3 つのレイアウト（ソース、分割、プレビュー）'],
                      ['編集', 'できない [S1, S7, S9]', 'できる。レンダリングされたページ自体は編集できず、隣のソースを編集する'],
                      ['ライブプレビュー',
                       'ファイルを表示する。ほかのエディタが保存すると自動で再読み込みする [S9]',
                       '入力するたびに更新される。ほかのアプリがファイルを変更すると、MarsDawn は再読み込みして位置を保つ（自分の未保存の編集がない場合）。'],
                      ['Mermaid', 'あり：フローチャート、シーケンス図、状態遷移図、ガントチャート、円グラフなど。オフラインで動作 [S1, S3, S7]', 'あり'],
                      ['数式', 'なし：README に「数式（LaTeX/KaTeX）は表示しない」と明記 [S7]', 'あり、KaTeX'],
                      ['コードのハイライト', 'あり [S1, S9]', 'あり'],
                      ['テーマ',
                       '12 種類のドキュメントテーマ [S1, S7]',
                       '標準で 4 種類（夜明け、クラシック、モダン、ビビッド）、それぞれにライトとダーク。テーマギャラリーにはさらに多数'],
                      ['タブ', 'あり。任意で、初期設定はオフ（1.6.0 から）[S5, S8]', 'あり'],
                      ['PDF 書き出し',
                       'あり。1 枚の連続したページで、現在のテーマ、透かしなし [S3, S9]',
                       'あり。ページ分けされ、テーマのライトの配色。ページの区切りは短いコードを分断しないようにする'],
                      ['プリント', 'あり。macOS のプリントダイアログを使う [S3, S9]', 'あり'],
                      ['Finder のクイックルック',
                       'あり。付属。システム設定で有効にする。選んだテーマを使う [S4]',
                       'あり。トライアル中でも期間後でも使える。選んだテーマを使う'],
                      ['クイックルックでの Mermaid と数式', 'Mermaid：あり [S4]。数式：なし。数式は表示しない [S7]', 'あり。どちらも描画される'],
                      ['コマンドライン',
                       '独立したコマンドラインツールの記載なし。`markdownviewer://` の URL スキームと、ファイルを開くための Claude Code '
                       'のプラグインとフックがある [S6]',
                       '無料の `marsdawn` ツール：`marsdawn export` はアプリなしで PDF を書き出し、`marsdawn open` '
                       'は行を指定してファイルを開く'],
                      ['インターフェイスの言語', '公式の資料に記載なし [S1, S3, S7]', '{langs}'],
                      ['動作環境', 'macOS 14（Sonoma）以降。Apple シリコンと Intel [S1, S7]', 'macOS 26（Tahoe）以降'],
                      ['ほかのプラットフォーム', 'Mac のみ [S1]', 'Mac。iPhone と iPad では閲覧のみ']]},
            {'h2': '価格と購入方法',
             'head': ['', 'MacMD Viewer', 'MarsDawn'],
             'rows': [['購入場所', '公式サイト、Homebrew、Setapp。Mac App Store には掲載なし [S2, S7]', 'Mac App Store のみ'],
                      ['価格',
                       '使用中の Mac 1 台につき USD 19.99 を一度（別の Mac に移せる）。Family Pack は 3 キーで USD 39.99。10 キーは USD '
                       '129 [S2]',
                       '無料ダウンロード、その後 USD 4.99 を一度'],
                      ['購入前に試す', 'トライアルも無料版もなし。直接購入は 14 日以内なら全額返金 [S2]', '14 日間の無料トライアル。すべての機能が使える'],
                      ['返金', '14 日以内に、自社のサポート窓口を通じて [S2]', 'Apple 経由'],
                      ['アップデート',
                       '同じメジャーバージョン内のアップデートは無料 [S2]。直接ダウンロード版は Sparkle で自動更新 [S7]',
                       'Mac App Store 経由'],
                      ['アカウント', '不要 [S2]', '不要'],
                      ['サブスクリプション', 'なし [S1, S2]', 'なし']]},
            {'h2': 'トライアルや購入のあと',
             'head': ['', 'MacMD Viewer', 'MarsDawn'],
             'rows': [['状態',
                       'トライアルなし。買えばずっと使える',
                       '14 日後にロックを解除しないと、書類は開くが内容は覆われる。ファイルには一切変更が加わらず、クイックルックと無料の `marsdawn` '
                       'の書き出しはそのまま使える']]}],
 'sources_h2': '出典',
 'sources': [['S1', 'https://macmdviewer.com/'],
             ['S2', 'https://macmdviewer.com/pricing'],
             ['S3', 'https://macmdviewer.com/features'],
             ['S4', 'https://macmdviewer.com/quicklook'],
             ['S5', 'https://macmdviewer.com/changelog'],
             ['S6', 'https://macmdviewer.com/docs/integrations'],
             ['S7', 'https://github.com/macmdviewer/MacMDViewer'],
             ['S8', 'https://macmdviewer.com/press'],
             ['S9', 'https://macmdviewer.com/product-facts.md'],
             ['S10', 'https://github.com/macmdviewer/MacMDViewer/releases']],
 'pick_h2': 'どちらを選ぶか',
 'pick': ['**MacMD Viewer を選ぶのは、**Markdown を読むだけで、ファイルを変更しないことが保証されていてほしい場合です。ファイルへの変更は一切保存されません '
          '[S1]。次の場合にも向いています。Mac が macOS 14 または 15 である（MarsDawn は macOS 26 が必要）[S1, S7]。Mac App Store '
          'より、開発者の公式サイト、Homebrew、Setapp から買いたい [S2, S7]。エージェントが編集したファイルを自動でビューアに開かせたい（Claude '
          'Code、Cursor、Windsurf のフックで実現） [S6]。ページ分けされた PDF より、1 枚の連続したページの PDF がよい [S9]。トライアルはありませんが、14 '
          '日間の返金があります [S2]。',
          '**MarsDawn を選ぶのは、**Markdown を読んだあとにもう一度手を入れる場合です。エージェントが書いた計画、README、仕様書は、たいてい 1 か所直す、1 文を言い換える、1 '
          '節を足す必要があり、MarsDawn なら読んでいるそのウインドウで直せます。数式（KaTeX）にも対応しており、MacMD Viewer は表示しないと述べています '
          '[S7]。インターフェイスは 8 言語。無料の `marsdawn` コマンドラインでアプリなしに PDF を書き出せます。価格は、すべて使える 14 日間のトライアルのあと USD 4.99 '
          'です。',
          '**どちらでもよいのは、**新しめの Mac で Markdown を読み、Mermaid の図をきちんと描画したく、Finder のクイックルックも使いたい場合です。どちらも対応しています。',
          '**両方使うこともできます。**両者は排他的ではありません。読むだけのファイルには読み取り専用のビューア、書くファイルにはエディタ、という使い分けも問題ありません。'],
 'faq_h2': 'よくある質問',
 'faq': [['MacMD Viewer はファイルを編集できますか？',
          'いいえ。読み取り専用で、本人の言葉によれば、ソースファイルへの変更は保存しません [S1, S9]。お使いのテキストエディタでファイルを開くことはできますが（「ファイル」メニュー、'
          '⇧⌘E、1.7.0 から）、これはファイルをほかのアプリに渡す機能です [S5]。'],
         ['MacMD Viewer は Mac App Store にありますか？',
          '自身のページに挙がっているのは公式サイト、Homebrew、Setapp で、Mac App Store への言及はありません [S2, S7]。MarsDawn は Mac App Store '
          'のみです。'],
         ['MarsDawn は同じファイルを開けますか？',
          'はい。`.md` ファイルのほか、プレーンテキストと PDF も開けます。UTF-8 のテキストはそのまま編集でき、PDF はビューアで開きます。'],
         ['macOS 14 や 15 の場合は？',
          'MacMD Viewer は macOS 14 以降で動きます [S1]。MarsDawn は macOS 26 以降が必要ですが、無料の `marsdawn` コマンドラインツールなら PDF '
          'の書き出しはできます。'],
         ['なぜ片方は USD 19.99 で、もう片方は USD 4.99 なのですか？',
          '得られるものと支払い方が違います。MacMD Viewer は一度きりの購入で、14 日間の返金があり、トライアルはありません [S2]。MarsDawn は無料でダウンロードでき、14 '
          '日間のトライアルのあと、一度きりのロック解除です。どちらもサブスクリプションではありません。']],
 'try_h2': '今すぐ無料で試す',
 'try_p_html': 'MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールも、どんな Markdown ファイルも '
               'Mermaid 図とハイライトされたコード付きの PDF にレンダリングでき、他に何もインストールする必要はありません。',
 'next_h2': '次に',
 'next_items_html': ['完全な解説：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。',
                     'MarsDawn ができないこと：<a href="/ja/limits/">一覧はこちら</a>。',
                     'コマンドラインツールのすべてのオプション：<a href="/ja/cli/">コマンドライン</a>。'],
 'features_item': '- MarsDawn の機能をすべて 1 ページで：[機能一覧](/ja/features/)。'}


# Machine draft (needs-i18n; Grok reviews it): the install section of /cli/skill/ (website #231). Commands, flags and
# paths stay in <code>, untranslated. {_SKILL_URL} is the skill's address, filled in by the builder.
SKILL_INSTALL = '<h2>Claude Code にインストールする</h2>\n<p>コマンドラインツール <code>marsdawn</code> がスキルを書き出します。書き出されるファイルは、インストール済みの <code>marsdawn</code> のバージョンに合ったものです。まだ <code>marsdawn</code> がない場合は、<a href="https://brew.sh">Homebrew</a> でインストールしてください。</p>\n<pre><code>brew install redtear1115/tap/marsdawn</code></pre>\n<p>そのあと、スキルをインストールします。</p>\n<pre><code>marsdawn skill --install</code></pre>\n<p>これで <code>~/.claude/skills/marsdawn/SKILL.md</code> が書き出されます。フォルダがなければ作成されます。ファイルは手元の <code>marsdawn</code> から作られるので、そのバージョンにないオプションが書かれることはありません。</p>\n<p>Claude Code は、PDF が必要なタスクのとき、またはあなたが読む Markdown 文書を書いたり修正したりしたときに、これを自動的に読み込みます。<code>/marsdawn</code> として自分で実行することもできます。先に中身を読みたい場合は、<a href="/cli/skill/SKILL.md">短いファイル1つ</a>です。</p>\n<h2>marsdawn をアップグレードしたあと</h2>\n<p>Homebrew は <code>marsdawn</code> をアップグレードしますが、スキルには手を触れないので、更新するまで古いバージョンのままです。</p>\n<pre><code>marsdawn skill --install --force</code></pre>\n<p><code>--force</code> は、既存の <code>SKILL.md</code> を、あなたが加えた変更も含めて置き換えます。<code>--force</code> を付けない場合、内容の異なる <code>SKILL.md</code> がすでにあると、<code>marsdawn</code> はそのファイルに触れず、内容が違うことを知らせて、終了コード 64（<code>skill_differs</code>）で終了します。ファイルがすでに最新なら、何も変わりません。</p>\n<h2>ほかのエージェントの場合</h2>\n<p><code>--dir</code> に、お使いのエージェントがスキルを置くフォルダを指定すると、<code>marsdawn</code> はそこに <code>SKILL.md</code> を書き出します。</p>\n<pre><code>marsdawn skill --install --dir &lt;path&gt;</code></pre>\n<p>このファイルはただの Markdown で、説明とコマンドだけなので、指示ファイルを読むエージェントならそのまま使えます。</p>\n<h2>Homebrew やコマンドラインツールがない場合</h2>\n<p>先に <code>marsdawn</code> をインストールできない場合は、ファイルを直接ダウンロードします。</p>\n<pre><code>mkdir -p ~/.claude/skills/marsdawn\ncurl -fsSL {_SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>\n<p>これはこのサイトにある最新のスキルを取得するので、古い <code>marsdawn</code> より新しいことがあります。ツールをインストールしたら、<code>marsdawn skill --install --force</code> で、それに合ったものに置き換えられます。エージェントにこの URL を指定するか、ファイルをそのまま貼り付けることもできます。このファイルは英語です。</p>'


def build(k) -> dict:
    k.set_skill_install(SKILL_INSTALL)
    ui = {'features': '機能一覧', 'home': 'MarsDawn', 'privacy': 'プライバシーポリシー', 'support': 'サポート', 'cli': 'コマンドライン', 'agents': 'AI エージェント向け marsdawn', 'using_cli': 'CLI の使い方', 'markdown-to-pdf': 'Markdown から PDF へ', 'skill': 'エージェント用スキル', 'view-markdown-on-mac': 'Mac で .md ファイルを開く方法', 'mermaid-preview-mac': 'Mac で Mermaid をプレビューする', 'vs-macmd-viewer': 'MacMD Viewer と MarsDawn', 'updated': f"最終更新日：{k.UPDATED}", 'tagline': 'エージェントが書いた Markdown を読む。', 'slogan': 'Markdown の新しい夜明け。', 'footer_store': f'MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。', 'footer_nav': 'サイト', 'more': 'その他', 'yours': 'あなたの文章は Mac に残ります', 'pay-once': '無料で試して、一度だけ購入', 'pdf': 'PDF 書き出し', 'native': 'Mac アプリ', 'limits': 'MarsDawn ができないこと', 'mcp': 'MCP サーバー', 'token-efficient-review': 'トークンを抑えたレビュー', 'vs-markdown-preview-tools': '他のツールで Markdown を見る場合との比較', 'themes': 'テーマ', 'themes-new': 'テーマを作る', 'themes-agents': 'エージェントとテーマを作る', 'themes-gallery': 'テーマギャラリー', 'sharing-exported-pdfs': '書き出した PDF を共有する', 'reviewing-ai-output': 'AI の出力を人が確認する理由', 'reading-agent-output': 'エージェントが返してくるものを読む', 'agent-transparency': 'エージェントの透明性', 'reviewing-agent-plans': 'エージェントの計画をレビューする', 'agent-design-patterns': 'エージェント設計パターン', 'changelog': '更新履歴', 'roadmap': 'ロードマップ', 'reading-notes': '編集者の読書ノート', 'reading-notes-anthropic': '読書ノート：Anthropic', 'reading-notes-chip-huyen': '読書ノート：Chip Huyen', 'reading-notes-lilian-weng': '読書ノート：Lilian Weng', 'reading-notes-harrison-chase': '読書ノート：Harrison Chase', 'reading-notes-langchain': '読書ノート：LangChain（Jess Ou）', 'reading-notes-andrew-ng': '読書ノート：Andrew Ng', 'consent_text': '分析用クッキーを使います。「同意する」を選ぶまで無効です。', 'consent_accept': '同意する', 'consent_decline': '同意しない', 'consent_aria': 'クッキーの同意設定', 'cookie_settings': 'Cookie 設定', 'view_markdown_source': 'Markdown のソースを見る'}
    store_chip = 'Mac App Store で配信中'
    schema_notes = {'export': 'export 成功時', 'open': 'open 成功時、marsdawn 0.5.1 以降、サイドバーに表示するフォルダを含む', 'open_v2': 'open 成功時、marsdawn 0.3.0〜0.5.0', 'error': '失敗時、両方のコマンド共通、marsdawn 0.5.2 以降', 'open_v1': 'open 成功時、marsdawn 0.2.x（<code>opened</code> がパスのリストだった頃）', 'error_v1': '失敗時、両方のコマンド共通、marsdawn 0.5.1 以前'}
    example_plan = '# 計画：書き出しを高速化\n\nこの計画はエージェントが書きました。内容を確認してから、PDF にします。\n\n## ステップ\n\n| ステップ | 担当 | 状況 |\n|------|-------|--------|\n| 遅いページを計測する | エージェント | 完了 |\n| レンダリング済み図をキャッシュする | エージェント | レビュー中 |\n\n50 ページの文書で目標とするのは $t < 2\\,\\text{s}$：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  ドラフト --> レビュー --> 公開\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'features': ('機能一覧', 'MarsDawn でできることを、1ページで。'), 'yours': ('あなたの文章は Mac に残ります', 'アカウント不要、同期なし、クラウドなし。'), 'pay-once': ('無料で試して、一度だけ購入', '14日間無料、その後は一度だけ USD 4.99。サブスクリプションはありません。'), 'pdf': ('PDF 書き出し', '図表、コードのハイライト、配慮された改ページ。'), 'native': ('Mac アプリ', 'ネイティブのウインドウとタブ、自動保存、クイックルック。'), 'limits': ('MarsDawn ができないこと', '購入前に知っておくこと。')}
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
        "body": k.render_legal_body("support", "ja"),
    }
    pages['privacy'] = {
        "title": 'プライバシーポリシー · MarsDawn',
        "description": 'MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。',
        "body": k.render_legal_body("privacy", "ja"),
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
  <li><strong>MarsDawn で確認する。</strong>ファイルを開き、<a href="/ja/mermaid-preview-mac/">Mermaid 図</a>やハイライトされたコードとともにレンダリングされたページを、ソースの隣で読みます。</li>
  <li><strong>エージェントが修正する。</strong>変更を依頼します。修正されたファイルを開き、同じように読みます。</li>
</ol>
<p><a href="/ja/reading-agent-output/">エージェントが返してくるものをどう確認するか</a> · <a href="/ja/view-markdown-on-mac/">Mac で .md ファイルを開く方法</a></p>
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
  <li><strong>14 日間、すべて使える。</strong> トライアルを始めると、14日間は MarsDawn のすべての機能（すべてのテーマとレイアウト、PDF の書き出しとプリント、Siri とショートカットのアクション）が使えます。Finder のクイックルックは、トライアルの有無にかかわらず使えます。</li>
  <li><strong>一度の購入で解除。</strong> その後も使い続けるには、USD 4.99 の一度きりの購入でロックを解除します。App 内課金であり、サブスクリプションではないので、自動更新もあとから請求されることもありません。</li>
</ol>
<ul>
  <li>トライアル自体も課金されません。終了時、あなたがロック解除を選ばない限り何も購入されません。</li>
  <li>アカウントはありません。MarsDawn がアカウント作成を求めることは決してありません。</li>
  <li>同じ Apple Account なら、1回のトライアルと1回のロック解除で、Mac、iPhone、iPad の MarsDawn をすべて利用できます。iPhone と iPad では閲覧専用で、編集や PDF の書き出しはできません。</li>
</ul>
<h2>各段階でできること</h2>
<!--compare:pay-once-states-->
<p>トライアルを始める前は、MarsDawn がトライアルの案内を表示します。開始しても料金はかかりません。</p>
<p>トライアル終了後は、MarsDawn で開いた PDF ファイルも同じようにロックされます。</p>
<h2>ロックを解除しない場合</h2>
<ul>
  <li>14日後、ロックを解除するまでは、MarsDawn で文書を読んだり編集したり書き出したりプリントしたりできません。文書自体は開きますが、内容は覆われます。</li>
  <li>あなたのファイルは変わりません。Mac 上の普通のファイルのままで、Finder のクイックルックでも引き続き表示されます。</li>
  <li>無料の<a href="/ja/cli/"><code>marsdawn</code> コマンドラインツール</a>は、トライアルの有無にかかわらず、引き続き PDF に書き出せます。</li>
  <li>トライアル終了時に MarsDawn で文書が開いていた場合、入力した文字が失われることはありません。「ファイル」▸「別名で保存…」で保存してください。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Mac で Markdown を PDF に書き出す、図も含めて · MarsDawn',
        "description": 'Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックを分断しないよう配慮されます。',
        "intro": f"""
<section class="intro">
  <h1>PDF は、あなたが書いたページそのままに見えます。</h1>
  <p>テーマのライトカラーで PDF に書き出す、またはプリントできます。図やハイライトされたコードもそのまま反映され、改ページはひとまとまりの内容を分断しないよう配慮されます。</p>
</section>
""",
        "body": f"""
<h2>それが意味すること</h2>
<ul>
  <li>Mermaid 図は PDF に描き込まれます。</li>
  <li>コードブロックはシンタックスハイライトを保ちます。</li>
  <li>改ページは、見出しがページの下端に残ったり、コードや図が分断されたりしないよう配慮されます。</li>
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
        "description": '同期なし、iPhone・iPad では編集不可、プラグインなし、アカウントなし。テーマは変更できますが、カスタム CSS は使えません。購入前に知っておいてください。',
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
  <li><strong>iPhone と iPad：</strong>これらの端末では閲覧専用です。Markdown とテキストファイルを開いて整えて表示し、アウトラインとテーマも使えますが、編集、PDF の書き出し、同期はできません。ファイルは、普段使っているクラウドを通して届けます。</li>
  <li><strong>共有：</strong>アカウントも共同編集もありません。MarsDawn は自分の Mac で使う一人のためのものです。</li>
  <li><strong>システム：</strong>MarsDawn には、Mac では macOS 26 以降、iPhone と iPad では iOS 26 または iPadOS 26 以降が必要です。</li>
</ul>
<h3>ファイルと機能</h3>
<ul>
  <li><strong>編集：</strong>左に Markdown を書き、右でページを読みます。ページ自体は編集できません。</li>
  <li><strong>形式：</strong>MarsDawn は PDF の書き出しとプリントに対応していますが、Word ファイルへの書き出しはできません。</li>
  <li><strong>その他のファイル：</strong>プレーンテキストファイルと PDF は読み取り専用で開きます。</li>
  <li><strong>テーマ：</strong>夜明け、クラシック、モダン、ビビッドの4種類が内蔵されており、それぞれライトとダークがあります。また、審査済みの<a href="/ja/themes/gallery/">テーマギャラリー</a>からさらにインストールできます（「設定 ▸ 外観モード ▸ テーマを追加…」）。テーマは色といくつかのスタイルオプションを設定するもので、カスタム CSS は使えません。詳しくは<a href="/ja/themes/">テーマ</a>をご覧ください。</li>
  <li><strong>プラグイン：</strong>MarsDawn にプラグインや拡張機能はありません。</li>
</ul>
<h2>試用期間が終わったら</h2>
<p>14日間のトライアルが終わってロックを解除しなければ、MarsDawn で文書を読んだり編集したり書き出したりプリントしたりできません。文書は開きますが、内容は覆われます。ファイルはそのまま残り、クイックルックでも引き続き表示され、無料のコマンドラインツールで PDF に書き出すこともできます。<a href="/ja/pay-once/">トライアルとロック解除のページ</a>に、3つの段階を並べた表があります。</p>
""",
    }
    pages['view-markdown-on-mac'] = k.open_md_page(OPEN_MD)
    pages['mermaid-preview-mac'] = k.mermaid_page(MERMAID)
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
  <li>コーディングエージェントにこれをやらせるには、<code>marsdawn skill --install</code> を実行して<a href="/ja/cli/skill/">marsdawn のエージェントスキル</a>を追加してください。</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = k.vs_macmd_page(VS_MACMD)
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
<p>コーディングエージェントを使っていますか？<code>marsdawn skill --install</code> を実行して<a href="/ja/cli/skill/">marsdawn スキル</a>を追加してください。自分が書いたものを MarsDawn で開いてあなたに確認してもらう方法と、PDF の書き出しを教える、1つのファイルです。</p>
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
  <li>MarsDawn 1.0 はその行にジャンプしてファイルを開きます。</li>
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
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> は移動先の行を指定します。その後にコロンが続く場合、たとえば <code>notes.md:120:8</code> の列部分は無視されます。存在するファイル名を丸ごと表す引数は常にそのファイル名として扱われるため、<code>weird:12</code> という名前のファイルはそのまま開きます。</li>
  <li><code>--line &lt;n&gt;</code> は単一ファイルの行を指定します。それ自体がコロンと数字で終わるパスも含みます。ファイルは1つだけ指定できます。</li>
  <li>行番号は 1 から 999999999 までで、それ以外は使用方法のエラーになります。</li>
  <li>行の指定は marsdawn 0.3.0 で追加されました。MarsDawn 1.0 はその行にジャンプしてファイルを開きます。</li>
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

<h2>次に</h2>
<ul>
  <li>エージェントで MarsDawn のテーマを作る：<a href="/ja/themes/agents/">エージェントとテーマを作る</a>。</li>
</ul>
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
<!--skill-install-->
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
  <li><strong>Registry：</strong><a href="https://registry.modelcontextprotocol.io/v0/servers/dev.southern-light.mcp%2Fmarsdawn/versions/latest">MCP Registry</a> に <code>dev.southern-light.mcp/marsdawn</code> として登録されています。</li>
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
    pages['themes/agents'] = k.theme_agents_page(THEME_AGENTS)
    pages['features'] = k.features_page(FEATURES)
    pages['themes/new'] = {
        "title": "ブラウザで MarsDawn のテーマを作る · MarsDawn",
        "description": "配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。",
        "body": """
<section class="intro">
  <h1>テーマを作る</h1>
  <p>下で配色といくつかのスタイルオプションを選んでください。右側のサンプル文書がライトとダークの両方でその場で更新され、テーマギャラリーの CI が行うチェックもここに表示されます。投稿用の issue に届く頃には、たいてい先にすべて通っています。</p>
  <p>投稿には GitHub アカウントが必要です。このページ自体はインストールも git も不要です。</p>
  <p>AI エージェントがテーマのファイルを代わりに書けます。<a href="/ja/themes/agents/">エージェントとテーマを作る</a>を見て、渡されたリンクをここで開いて整えてください。</p>
</section>
<div id="theme-sim-app" data-locale="ja"><p>このページの作成とプレビューには JavaScript が必要です。</p></div>
""",
    }
    pages['themes'] = {
        "title": 'プレビューテーマとテーマギャラリー · MarsDawn',
        "description": 'それぞれライトとダークを備えた4種類の内蔵プレビューテーマに加え、Mac 版 MarsDawn の設定から開ける厳選ギャラリーも。クイックルックにも選んだテーマが反映されます。',
        "body": '''
<section class="intro">
  <h1>4種類のテーマを内蔵。ギャラリーにはさらに多く。</h1>
  <p>MarsDawn には 夜明け、クラシック、モダン、ビビッド の4種類のプレビューテーマが内蔵されており、それぞれライトとダークの配色があります。バージョン 1.1 からはアプリ内のテーマギャラリーからさらに追加でき、Finder のクイックルックでも選んだテーマで書類が表示されます。</p>
</section>

<h2>4種類のテーマ</h2>
<!--theme-gallery-->
<ul>
  <li><strong>夜明け</strong>、デフォルト：このサイトと同じ、温かみのある紙の質感と Mars Rust のアクセントカラー。</li>
  <li><strong>クラシック</strong>：より素朴で、紙の文書らしい配色。</li>
  <li><strong>モダン</strong>：より涼しげで、現代的な配色。</li>
  <li><strong>ビビッド</strong>：より明るく、コントラストの高い配色。</li>
</ul>
<p>それぞれ独自のライトとダークの配色を持つので、Mac の外観を切り替えると、インターフェースの色だけでなくテーマの配色自体も切り替わります。</p>

<h2>アプリ内のテーマギャラリー</h2>
<p>MarsDawn で「設定 &#9656; 外観モード」を開き、「テーマを追加&#8230;」をクリックします。テーマギャラリーは開いたときに一覧を読み込みます。オンラインになるのは開いているあいだだけで、接続がないときは通知を表示し、内蔵の4つのテーマはそのまま使えます。</p>
<ul>
  <li>「インストール」は「ライトテーマ」と「ダークテーマ」の選択メニュー、および「表示 &#9656; プレビューのテーマ」にテーマを追加します。「取り除く」で削除します。</li>
  <li>「テーマのアップデートを確認」は、新しいバージョンがないかギャラリーに再度問い合わせます。</li>
  <li>テーマの用途で絞り込めます：エージェント出力のレビュー、技術ドキュメント、フォーマルな出力、メモ・共有。</li>
  <li>「テーマを報告&#8230;」は、入力済みの GitHub issue または私たち宛てのメールを開きます。</li>
</ul>

<h2>ギャラリーにあるテーマ</h2>
<p>現在は8つのテーマがあり、すべて私たちが作成・レビューしたものです。よく知られた配色を基に読みやすく調整した Dracula、Gruvbox、Nord、Solarized に加え、ユーザーガイド、予算表、PRD、スプリントノート向けに作られた Guide、Ledger、Spec、Story を揃えています。</p>

<h2>レビュー済みで、中身はデータのみ</h2>
<p>すべてのテーマは、ギャラリーに表示される前に私たちがレビューしてマージしています。テーマは色といくつかの範囲が限られたオプションだけを収めた小さな JSON ファイルです。スクリプトも CSS も作者の画像も含まれず、MarsDawn はインストール前にすべての値を検証します。報告されたテーマは24時間以内にギャラリーから取り下げられます。有害なテーマであった場合は、次にギャラリーを開いたときにインストール済みの Mac からも削除され、使用中だった場合は夜明けに戻ります。</p>
<p>ギャラリーが通信するのは <code>marsdawn.southern-light.dev/themes/v1/</code> のみで、ギャラリーを開くとき、アップデートを確認するとき、またはテーマをインストールするときに限られます。アカウント、識別子、Cookie、書類の内容は一切送信しません。</p>

<h2>クイックルックにも選んだテーマを反映</h2>
<p>Finder で Markdown ファイルを選んでスペースキーを押します。クイックルックは、インストールしたテーマも含めてあなたが選んだテーマでファイルを表示し、MarsDawn の「外観モード」の設定に従います。「ライト」と「ダーク」は選んだまま固定され、「システム」は Mac に合わせます。</p>

<h2>PDF 書き出しとプリント</h2>
<p>PDF に書き出す、またはプリントすると、ページには「ライト」に選んだテーマが使われます。Mermaid の図はそこに描き込まれ、コードブロックはハイライトを保ち、改ページは見出しをそのセクションから切り離したり、表や図を途中で切ったりしないよう配慮されます。無料の<a href="/ja/cli/">marsdawn コマンドラインツール</a>も同じ書き出しエンジンを使い、<code>--theme</code> で4つの内蔵テーマのどれでも指定できます。</p>

<h2>自分のテーマを作る</h2>
<p><a href="/ja/themes/new/">ブラウザでテーマを作れます</a>：色といくつかのスタイルオプションを選び、その場で反映を確認して、レビュー用に GitHub の issue として送信します。GitHub アカウントは必要ですが、インストールも git も不要です。送信しただけでは公開されず、私たちがレビューしてマージしたあとにのみ<a href="/ja/themes/gallery/">ギャラリー</a>に表示されます。</p>
<p>エージェントと作業していますか？<a href="/ja/themes/agents/">エージェントにテーマを作らせて</a>、ブラウザで整えましょう。</p>

<h2>次に</h2>
<ul>
  <li>コマンドラインからの、完全な PDF 書き出しの手順：<a href="/ja/markdown-to-pdf/">Markdown から PDF へ</a>。</li>
  <li>MarsDawn がまだできないこと：<a href="/ja/limits/">その一覧</a>。</li>
  <li>Markdown を使わない人に、書き出した PDF を渡す：<a href="/ja/sharing-exported-pdfs/">PDF を共有する</a>。</li>
</ul>
''',
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
  <li>改ページは、見出しがページの下端に一人取り残されたり、図が2ページにまたがって切れたりしないよう選ばれます。</li>
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
  <li>なぜ読みにくいのか、どう読むか：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
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
<p>MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。無料の <code>marsdawn</code> コマンドラインツールもあります：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。<code>marsdawn open</code> でエージェントにファイルを MarsDawn で開かせることもできます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; AI エージェント向けの参照：<a href="/ja/cli/agents/">marsdawn for agents</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>AI の出力をそもそも読むべき理由（短い版）：<a href="/ja/reviewing-ai-output/">AI の出力を人が確認する理由</a>。</li>
  <li>レビュー中もエージェントの context を小さく保つ：<a href="/ja/token-efficient-review/">トークンを抑えたレビュー</a>。</li>
  <li>なぜエージェントはそもそも計画を示すのか：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>上のチェックリストを、実例つきで詳しく：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>エージェントの種類ごとに、どんな文書が返ってくるか：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
  <li>エージェントを作る人たちが実際に何を語っているか、6 本の長めのノート：<a href="/ja/reading-notes/">編集者の読書ノート</a>。</li>
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
<p>MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。無料の <code>marsdawn</code> コマンドラインツールもあります：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>エージェントの出力がなぜ読みにくいか、そのチェックリスト：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>そのチェックリストを、実例つきで詳しく：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>エージェントの種類ごとに、どんな文書が返ってくるか：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
  <li>AI の出力をそもそも読むべき理由（短い版）：<a href="/ja/reviewing-ai-output/">AI の出力を人が確認する理由</a>。</li>
  <li>このガイド自身の workflow パターンを、より詳しく：<a href="/ja/reading-notes/anthropic-building-effective-agents/">Anthropic は workflow と agent を分けて考える。あなたの読み方はどちらに近いか？</a></li>
  <li>Harrison Chase の可観測性についての主張を、より詳しく：<a href="/ja/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる</a></li>
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
<p>MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。無料の <code>marsdawn</code> コマンドラインツールもあります：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>そもそもエージェントの出力がなぜ読みにくいか：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>なぜエージェントはそもそも計画を示すのか：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>エージェントが返すのは計画だけではない：<a href="/ja/agent-design-patterns/">4 つのエージェント設計パターンと、それぞれが返す文書</a>。</li>
  <li>Chip Huyen の read-only／write action という分け方を、より詳しく：<a href="/ja/reading-notes/chip-huyen-agents/">Chip Huyen の read-only／write action という分け方、承認する前になぜ大事か</a></li>
  <li>Andrew Ng が自分の設計パターンをどうランク付けしているか、より詳しく：<a href="/ja/reading-notes/andrew-ng-design-patterns/">Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする</a></li>
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
<p>MarsDawn は <a href="{k.LISTING_URL}">Mac App Store</a> で配信中です。無料の <code>marsdawn</code> コマンドラインツールもあります：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。詳しくは<a href="/ja/markdown-to-pdf/">「Markdown から PDF へ」</a>を見てください。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>エージェントの出力がなぜ読みにくいか、そのチェックリスト：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
  <li>計画のチェックを、完全な形で：<a href="/ja/reviewing-agent-plans/">エージェントの計画を 5 分でレビューする</a>。</li>
  <li>透明性があなたに求めること、求めないこと：<a href="/ja/agent-transparency/">Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？</a></li>
  <li>Andrew Ng が自分でこれらのパターンをどうランク付けしているか、より詳しく：<a href="/ja/reading-notes/andrew-ng-design-patterns/">Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする</a></li>
  <li>Lilian Weng によるもっと早い時期のエージェントの設計図、より詳しく：<a href="/ja/reading-notes/lilian-weng-llm-agents/">Lilian Weng が 2023 年に描いたエージェントの設計図、各部分が残すファイル</a></li>
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

<h2>marsdawn 0.6.3</h2>
<p>2026年10月6日。MarsDawn が Mac App Store で公開。</p>
<ul>
  <li>アプリがインストールされていないとき、<code>marsdawn open</code> は Mac App Store の MarsDawn を案内します。</li>
  <li>README とエージェントスキルで <code>marsdawn open .</code> と <code>--folder</code> を説明します。MarsDawn 1.0.0 はフォルダをウインドウのサイドバーに表示します。</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>2026年9月26日。Mermaid の修正、図のエラーの行番号、スキルのインストール。</p>
<ul>
  <li>シーケンス図で、メッセージのラベルがほかの参加者のライフラインをまたいでも、文字が読みやすいままです。プレビューでも、書き出した PDF でも同じです。</li>
  <li><code>marsdawn export</code> が、Mermaid の図をたくさん含むファイルを書き出せるようになりました。図が 50 個あり、これまでコード 5 で終了していたファイルも書き出せます。</li>
  <li><code>marsdawn export --json</code> に <code>diagramErrorDetails</code> が加わりました。図のエラーごとに、その図がファイルの何行目から始まるかと、Mermaid が行を示している場合はエラーそのものの行を、行番号で返します。</li>
  <li><code>marsdawn skill --install</code> は、Claude Code 用のエージェントスキルを <code>~/.claude/skills/marsdawn/SKILL.md</code> にインストールします。<code>--dir</code> でほかのフォルダも指定できます。同じ内容のファイルがあればそのままにし、内容が違うファイルは <code>--force</code> を付けたときだけ置き換えます。付けないときはコード 64（<code>skill_differs</code>）で終了し、何も変更しません。</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>2026年9月25日。フォルダの状態、Mermaid エラーの全文、そのほかの修正。</p>
<ul>
  <li><code>marsdawn open --folder</code> が、フォルダがどうなったかを返せるようになりました。状態を返すアプリが相手なら、<code>--wait</code> の秒数（デフォルトは 2 秒）まで応答を待ち、<code>--json</code> に <code>attached</code> や <code>needsUser</code> などの状態が入ります。</li>
  <li>Mermaid の図を解析できないとき、最初の行だけでなく Mermaid のエラーメッセージ全文を表示します。行番号もファイルの先頭から数えた値になりました。</li>
  <li>フロントマターの終わりを探すのは 1,000 行までになりました。閉じていないブロックがあっても、大きなファイルを毎回最後まで調べることはありません。</li>
  <li>脚注の戻りリンクのラベルを、アプリが PDF の書き出しとプリント用に翻訳して渡せるようになりました。このラベルはページにはプリントされず、<code>marsdawn export</code> では英語のままです。</li>
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
    pages['reading-notes'] = {
        "title": "編集者の読書ノート · MarsDawn",
        "description": "AI エージェントを作っている人たちが実際に何を主張しているかを見る、6 本の短いノート——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain、Andrew Ng——それぞれが、エージェントの返してきたものを読む人にとって何を意味するか。",
        "body": f"""
<section class="intro">
  <h1>編集者の読書ノート</h1>
  <p>AI エージェントがどう動くかについて、6 人がそれぞれ書いている：エージェントが何でできているか、何が「agentic」と呼べるのか、どの設計パターンが実際に通用し、どれがまだ未成熟か。誰も「エージェントの返してきたものをどう読むか」については書いていないし、誰も MarsDawn には触れておらず、Markdown ツールを勧めてもいない。私たちはそれぞれの記事をその文脈のまま読み、私たち自身の解釈がどこから始まるかをはっきり示したうえで、どの出典にも同じ問いを立てた：この記事の内容から、あなたのフォルダにはどんなファイルが落ちてくるのか、そしてそれを読むとき MarsDawn は何の役に立つのか。</p>
</section>

<p>まず実用的なほうから読みたいなら、<a href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a>と<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>から始めてほしい。この 6 本のノートは、そのもとになった出典によりくわしく踏み込んでいる。どれも単独で読めるので、順番は問わない。</p>

<ul>
  <li><a href="/ja/reading-notes/anthropic-building-effective-agents/">Anthropic は workflow と agent を分けて考える。あなたの読み方はどちらに近いか？</a>&#8212;&#8212;エージェントを作る人向けの Anthropic のガイドは、決まった手順と、自分で次の一手を決めるモデルを分けて説明し、「レビュアー」が実は人ではなく、もう一回の LLM 呼び出しである workflow を 1 つ描いている。</li>
  <li><a href="/ja/reading-notes/chip-huyen-agents/">Chip Huyen の read-only／write action という分け方、承認する前になぜ大事か</a>&#8212;&#8212;彼女によるエージェントの平易な定義と、「見るだけ」の行動と「何かを変える」行動の違い。これこそ 5 分のレビューで一番時間をかける価値がある場所だ。</li>
  <li><a href="/ja/reading-notes/lilian-weng-llm-agents/">Lilian Weng が 2023 年に描いたエージェントの設計図、各部分が残すファイル</a>&#8212;&#8212;脳、プランニング、記憶、ツール利用：エージェントが何でできているかについての、彼女自身のフレームワークと、うまくいかないときに彼女が名指ししている限界。</li>
  <li><a href="/ja/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる</a>&#8212;&#8212;彼によるエージェントの技術的な定義と、システムがそのスペクトラムを進むほど観測可能性が必要だという、彼自身の主張。</li>
  <li><a href="/ja/reading-notes/langchain-what-is-an-agent/">Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事</a>&#8212;&#8212;2026 年 7 月、LangChain は Harrison Chase の 2024 年の記事があった URL に、Jess Ou が書いた新しい「What is an AI agent?」を公開した。定義はほぼ彼のものと一言一句同じで、そこから先は、自動評価がどこで止まり、どこから先は人がやるしかないかを説明している。</li>
  <li><a href="/ja/reading-notes/andrew-ng-design-patterns/">Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする</a>&#8212;&#8212;The Batch の 5 本の手紙のなかで、彼はどのパターンをより信頼でき、どれを予測しづらいと感じているか、はっきり書いている。</li>
</ul>

<p>この 6 本のどれも、「エージェントの出力をもっと注意深く読むべきだ」とは主張していないし、どれも MarsDawn についてのものではない。その結びつきをつけているのは私たちであって、どのノートもそう断っている。</p>
""",
    }
    pages['reading-notes/anthropic-building-effective-agents'] = {
        "title": "Anthropic は workflow と agent を分けて考える。あなたの読み方はどちらに近いか？ · MarsDawn",
        "description": "2024 年 12 月に Anthropic が発表したガイドは workflow と agent を分けて考え、5 つの workflow パターンを説明している。そのうち 1 つは、もう一回の LLM 呼び出しがレビューを担う。これは、あなたのフォルダに落ちてくるものにとって何を意味するか。",
        "body": f"""
<section class="intro">
  <h1>Anthropic は workflow と agent を分けて考える。あなたの読み方はどちらに近いか？</h1>
</section>

<div class="summary"><p><strong>2024 年 12 月に Anthropic が発表した「Building Effective Agents」は、AI エージェントを作る人向けのガイドだ。冒頭で「workflow」と「agent」という 2 つの言葉を分け、そのあと、まず使える中で一番シンプルなやり方から始めること——場合によっては agentic なシステムをまったく作らないことさえ含めて——を勧め、それでは足りないときにだけ、整理された 5 つの workflow パターンのどれかに手を伸ばすよう提案する。そのパターンの 1 つでは、もう一回の LLM 呼び出しがレビュアーの席に座る。このノートはそのパターンについて、そして残りの 4 つがあなたに何を読ませることになるかについて書く。</strong></p></div>

<h2>ガイドが主張すること</h2>
<p>Erik S. と Barry Zhang がこの記事を書いたのは、LLM でどうシステムを作るか決めようとしているエンジニア向けだ。まず、こういう定義から始まる。</p>
<blockquote><p>&#8220;Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.&#8221;</p></blockquote>
<p>（Workflow とは、LLM とツールがあらかじめ決められたコードの経路にしたがってオーケストレーションされるシステムだ。一方 agent は、LLM が自分自身のプロセスとツールの使い方を動的に決め、タスクをどう成し遂げるかをみずから制御し続けるシステムだ。）</p>
<p>そのあと、彼らのアドバイスは控えめに始まる。</p>
<blockquote><p>&#8220;When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.&#8221;</p></blockquote>
<p>（LLM を使ってアプリケーションを作るとき、私たちはまず可能な限りシンプルな解決策を見つけ、必要なときだけ複雑さを増やしていくことを勧める。これは、agentic なシステムをまったく作らないことを意味する場合もある。）</p>
<p>より多くの構造が必要なとき向けに、彼らは 5 つの workflow パターンを説明している：prompt chaining（タスクを一連の呼び出しに分割し、ステップの間に任意でチェックを挟む）、routing（ルーティング）、parallelization（並列化）、orchestrator-workers（1 つの LLM がタスクを複数の部分に分け、複数の worker LLM に渡し、その結果をまとめる）、そして evaluator-optimizer。最後のこのパターンについて、原文はこう書いている。</p>
<blockquote><p>&#8220;In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.&#8221;</p></blockquote>
<p>（evaluator-optimizer workflow では、1 回の LLM 呼び出しが応答を生成し、もう 1 回の呼び出しがループの中で評価とフィードバックを行う。）</p>
<p>Anthropic はこのガイドのなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。このガイドの透明性の原則と「チェックポイント」という言葉については、<a href="/ja/agent-transparency/">「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」</a>がすでにくわしく扱っているので、このノートでは繰り返さない。人によるコードレビューについての一文も、本来の文脈（コーディングエージェントに特化した付録）とともに、あの記事で扱っている。</p>

<h2>ここから先は、私たちの解釈であって、Anthropic の主張ではない</h2>
<p>Anthropic は、workflow が終わったあと最終的な出力を誰がチェックするかについては書いていない。そもそもこの記事全体が文書についてのものではなく、作る人向けのアーキテクチャの決め方についてのものだ。とはいえ、この 5 つのパターンが、あなたに読ませることになるファイルの種類は同じではない。prompt chaining と routing は、たいてい目に見えない配管のようなもので、何かがあなたのところに届くとしても、それはこの連鎖の最後の呼び出しの出力にすぎず、ほかの単発の応答と変わらない。Orchestrator-workers は違う：あなたのコーディングエージェントが内部でこのパターンを使っているなら、フォルダに落ちてくるのは、複数の worker の呼び出しを orchestrator がつなぎ合わせて組み立てた 1 つの文書かもしれず、そのうち 1 つの worker の担当箇所にあるミスは、全体としてなめらかに読める要約のなかに埋もれて見逃されやすい。</p>
<p>Evaluator-optimizer は特に立ち止まる価値がある。もともと人間のレビュアーが座っていたかもしれない位置に、このガイドはもう一回の LLM 呼び出しを置いているからだ。これは一種のミスを安く捕まえる正当な方法ではあるが、結局はモデルが、与えられた基準にしたがって別のモデルをチェックしているにすぎない——このシリーズのほかの著者たちも、モデルが自分自身や別のモデルの成果を判定することについて、同じ懸念を口にしている。このガイドは、人が evaluator の判定をもう一度確かめるべきだとはどこにも書いておらず、そのこと自体について立場を取っていない。もしあなたがこの一連のプロセスの返してきたものを最後に読む立場なら、「ループが通した」ことと「私が確認した」ことは同じ文ではない——手元のファイルが両方の場合でまったく同じに見えたとしても。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn は、あるファイルがどの workflow パターンから生まれたのかを知らないし、中に AI モデルもない——自前で evaluator のステップを走らせることもなければ、Anthropic が描いたその評価がきちんと仕事をしたかどうかを教えてくれることもない。MarsDawn がしているのは：サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブが、orchestrator が組み立てた長いファイルの見出しを一覧にし、クリックするとそこへジャンプする。ソースとレンダリングされたページは並んで表示され（&#8984;2）、一緒にスクロールし、Mermaid の図や KaTeX の数式もソースのままではなく描画される。読んでいる途中でエージェントがファイルを書き換えても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）は、いまいる場所を <code>docs/plan.md:42</code> の形でコピーし、そのままエージェントとのチャットに貼り付ければいい。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>このガイドの透明性の原則とチェックポイントについての、より詳しい話：<a href="/ja/agent-transparency/">「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」</a></li>
  <li>エージェントの出力が一般になぜ読みにくいか：<a href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Erik S. と Barry Zhang、「Building Effective Agents」、Anthropic、2024 年 12 月 19 日：<a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a>（2026-09-26 に取得・引用）</li>
</ul>
""",
    }
    pages['reading-notes/chip-huyen-agents'] = {
        "title": "Chip Huyen の read-only／write action という分け方、承認する前になぜ大事か · MarsDawn",
        "description": "Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。",
        "body": f"""
<section class="intro">
  <h1>Chip Huyen の read-only／write action という分け方、承認する前になぜ大事か</h1>
</section>

<div class="summary"><p><strong>Chip Huyen が 2025 年 1 月に発表したエッセイ「Agents」は、教科書的な定義から出発し、もっと具体的な分け方にたどり着く：エージェントの行動は、世界を見るだけのものと、世界を変えるものに分かれる、というものだ。この分け方は、あなたに与えられた 5 分間で、計画のどの行を特によく見るべきかを決めるのに役立つ。</strong></p></div>

<h2>この記事が主張すること</h2>
<p>Huyen はまっすぐにこう始める。</p>
<blockquote><p>&#8220;An agent is anything that can perceive its environment and act upon that environment.&#8221;</p></blockquote>
<p>（エージェントとは、自分の環境を知覚し、その環境に対して行動できる、あらゆるものだ。）</p>
<p>そこから彼女は、エージェントに何が必要かを組み立てていく：行動できる環境と、それが何をできるかを決める一組のツール——彼女はこれを「tool inventory」と呼ぶ。彼女は、エージェントが環境を知覚するだけの行動（「read-only actions」）と、環境に対して行動する行動（「write actions」）を分ける。後者について、彼女はとても率直だ。</p>
<blockquote><p>&#8220;Write actions enable a system to do more.&#8221;</p></blockquote>
<p>（Write action は、システムがより多くのことをできるようにする。）</p>
<p>ただし彼女は、その 2 つ目の種類がもたらすリスクについてもはっきり指摘している。「the prospect of giving AI the ability to automatically alter our lives is frightening」（AI に、私たちの生活を自動的に変える力を与えるという見通しは恐ろしい）、彼女の言葉を借りれば「you shouldn&#8217;t allow an unreliable AI to initiate bank transfers」（信頼できない AI に、銀行送金を開始させるべきではない）。エージェントで一番うまくいかせるのが難しい部分についても、彼女は率直だ。</p>
<blockquote><p>&#8220;If you&#8217;ve ever been in any planning meeting, you know that planning is hard.&#8221;</p></blockquote>
<p>（計画づくりの会議に出たことがあるなら、計画がいかに難しいかを知っているはずだ。）</p>
<p>Huyen はこのエッセイのなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>は、同じエッセイから彼女の 3 つの文をすでに引用している：監督なしで実行することの代償、終わっていないのに終わったと思い込むエージェント、そしてステップ 3 のなかで、リスクのある操作に対しては「実行前に人間の明示的な承認を求められる」と述べている一文だ。このノートではそれらの引用を繰り返さない。まだ読んでいなければ、下にリンクがある。</p>

<h2>ここから先は、私たちの解釈であって、Huyen の主張ではない</h2>
<p>Huyen の read-only／write action という分け方は、レビューのために書かれたアドバイスではなく、ツールを分類するための方法だ。とはいえ、これは「エージェントの計画を 5 分でレビューする」のステップ 3 がすでに立ち止まるよう求めているような、リスクのある操作を見分けるための、平易で汎用的な判定法でもある。ファイルを読む、検索を実行する、ディレクトリを一覧表示する、といったものは read-only で、間違えても、やり直すコストで済む。データを削除する、force push する、ブランチをマージする、メールを送る、カードに課金する、といったものは write action で——彼女の言うとおり、間違えたときには「恐ろしい」種類のものであり、あなたがエージェントのレポートを読むころには、すでに実行されてしまっているかもしれない。人が一緒の部屋にいてさえ計画は難しいという彼女の指摘は、計画の精度に対して、その形式が支えられる以上のものを期待しないための、有用な歯止めでもある。自信たっぷりに読める計画が、正しい計画とは限らない。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn は、計画のどのステップが read-only でどれが write なのかを見分けられない——それは文章にラベルとしては書かれていない判断であり、アプリの中の何かが意味を読み取ってくれるわけではない。中に AI モデルもない：リスクの高い行を教えてくれることもなければ、「計画づくりはどれほど難しいか」というチェックを代わりに走らせることもなく、計画に点数をつけることもない。MarsDawn がしているのは、その判断を自分でするあいだ、ファイルを読みやすく保つことだ：サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブで、1 行ずつ読む前に計画の形を見ておける。ソースとレンダリングされたページは並んで表示され（&#8984;2）、手順の図が Mermaid のソースのままで止まってしまうこともない。「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）は、いまいる場所を <code>plan.md:10</code> の形でコピーし、順番のおかしい write の動作を見つけたその場で、フィードバックとして貼り付けられる。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>同じエッセイから組み立てた、6 ステップ・5 分のチェックリスト全体：<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a></li>
  <li>エージェントの出力が一般になぜ読みにくいか：<a href="/ja/reading-agent-output/">「エージェントが返してくるものを読む」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Chip Huyen、「Agents」、2025 年 1 月 7 日：<a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a>（2026-09-26 に取得・引用）</li>
</ul>
""",
    }
    pages['reading-notes/lilian-weng-llm-agents'] = {
        "title": "Lilian Weng が 2023 年に描いたエージェントの設計図、各部分が残すファイル · MarsDawn",
        "description": "Lilian Weng が 2023 年に書いた、広く引用されているサーベイは、LLM エージェントを、脳とプランニング、記憶、ツール利用の組み合わせとして描く。各部分が普通あなたに何を読ませることになるか、そして計画が予想外の事態に調整できないという、彼女自身が挙げる限界。",
        "body": f"""
<section class="intro">
  <h1>Lilian Weng が 2023 年に描いたエージェントの設計図、各部分が残すファイル</h1>
</section>

<div class="summary"><p><strong>2023 年 6 月、当時 OpenAI に在籍していた Lilian Weng は、自身のブログ Lil'Log に長いサーベイを発表し、LLM を使ったエージェントを、脳（モデル）とプランニング、記憶、ツール利用という 3 つの部品の組み合わせとして描いた。これは広く引用されている初期のエージェントの枠組みであり、彼女はその枠組みがどこでまだ崩れるかについても率直だ。</strong></p></div>

<h2>この記事が主張すること</h2>
<p>Weng は冒頭で、記事全体の枠組みをこう定める。</p>
<blockquote><p>&#8220;In a LLM-powered autonomous agent system, LLM functions as the agent&#8217;s brain, complemented by several key components: Planning ... Memory ... Tool use&#8221;.</p></blockquote>
<p>（LLM を使った自律型エージェントのシステムでは、LLM がエージェントの脳として機能し、いくつかの主要な部品——プランニング……記憶……ツール利用……によって補われる。）</p>
<p>彼女の説明では、プランニングはタスクをサブゴールに分解することと、過去の行動を振り返って今後の行動を改善することの両方を含む。記憶は短期（モデルがいま見ているコンテキストで、彼女は in-context と呼ぶ）と長期（通常はモデルの外、検索可能なデータベースに保存され、彼女は vector store と呼ぶ）に分かれる。ツール利用は、モデルが自分の重みの中にない情報——最新の情報、コードの実行、ほかの API——を外部に求めることを可能にする。記事の終わりに近い、彼女自身が「Challenges」と題した節で、彼女はある限界をはっきりと指摘する。</p>
<blockquote><p>&#8220;LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.&#8221;</p></blockquote>
<p>（LLM は予想外のエラーに直面したとき、計画を調整するのが苦手であり、試行錯誤から学ぶ人間と比べて頑健さに欠ける。）</p>
<p>また、化学エージェント「ChemCrow」についてのツール利用の事例研究のなかで、彼女はもっと狭い問題を指摘している：LLM による評価では GPT-4 とほぼ同等とされたが、人間の専門家による評価では、ChemCrow は正確性の点でずっと優れているとされた。彼女の結論は「自己評価」についてのものであり、彼女自身の「反省（reflection）」の部品そのものについてではない。</p>
<blockquote><p>&#8220;The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.&#8221;</p></blockquote>
<p>（専門知識が欠けていることが原因で、LLM は自分自身の欠陥に気づかず、タスクの結果が正しいかどうかをうまく判断できないことがある。）</p>
<p>Weng はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。</p>

<h2>ここから先は、私たちの解釈であって、Weng の主張ではない</h2>
<p>Weng が描いているのは 2023 年時点のエージェントのアーキテクチャであって、「誰かがエージェントの出力を読む」という話はまったく出てこない——ファイルを確認する人がいるとすら、彼女は書いていない。とはいえ、彼女自身が挙げる 3 つの部品は、あなたが読むことになりうる 3 種類のものにちょうど対応している。プランニングは、たいてい実行前に読む文書——計画そのもの——を残す。すでにその中に、ひとまわりの「反省」や自己チェックが組み込まれていることもある。記憶は、たいてい目に見えない。ただしエージェントが長期記憶を、書き続けている下書きファイルとして保存している場合は別で、そのファイル自体を単独で開く価値がある。なぜなら、それは古い、間違った前提を、何も言わないまま後続の多くのステップに持ち越してしまうことがあるからだ。ツール利用は、たいてい「何を実行し、何を得たか」というレポートを残す——計画というより、記録に近い。</p>
<p>計画が予想外の事態に調整できないという彼女の指摘は、あなたの側から見れば、昨日承認した計画が、今日にはもう古くなっているかもしれない理由になる：計画が想定していなかった何かが途中で起きても、エージェントは計画を立て直すのではなく、そのまま進んでしまうかもしれない。すると最後のレポートは、途中で回り道をしたことには触れずに、もとの計画が「成功した」ことだけを描くかもしれない。これは私たちの推論であって、彼女自身の主張ではない——彼女が語っているのはモデル自身の頑健さについてであって、読み手が何に注意すべきかについてではない。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn の中に AI モデルはなく、ある計画が実際に起きたことから静かにずれてしまっていないかを教えてくれることもなければ、あるファイルがプランニングのファイルなのか、記憶のファイルなのか、ツール利用のレポートなのかを見分けてくれることもない——それは内容を読み込んで初めてできる判断であり、あなた自身がする必要がある。MarsDawn がしているのは：サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブが、長い計画の形をひと目で見せてくれる。ソースとレンダリングされたプレビューは並んで表示され（&#8984;2）、Mermaid と KaTeX はそのまま描画される。読んでいる途中でエージェントがファイルを書き換えても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ——これは特に役に立つ。なぜなら、静かに書き換えられた計画こそ、彼女が「Challenges」の節でモデル側から描いている、まさにその失敗モードだからだ。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>異なるエージェントの設計パターンがそれぞれ何のファイルを渡してくるか：<a href="/ja/agent-design-patterns/">「4 つのエージェント設計パターンと、それぞれが渡してくる文書」</a></li>
  <li>実行前に計画を 5 分でレビューする方法：<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Lilian Weng、「LLM Powered Autonomous Agents」、Lil'Log、2023 年 6 月 23 日：<a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a>（2026-09-26 に取得・引用。この記事を書いた当時、彼女は OpenAI に在籍しており、ここでもその当時の立場としてのみ記す）</li>
</ul>
""",
    }
    pages['reading-notes/harrison-chase-what-is-an-agent'] = {
        "title": "Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる · MarsDawn",
        "description": "Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。",
        "body": f"""
<section class="intro">
  <h1>Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる</h1>
</section>

<div class="summary"><p><strong>2024 年 6 月、LangChain の Harrison Chase は「エージェントとは何か？」という、一見単純な問いから新しいシリーズを始めた。彼は技術的な定義と、「agentic」の度合いを表すスペクトラムを示す。彼の主張では、システムがこのスペクトラムを先へ進むほど、それが動いているあいだの内部を見られる必要が高まる。</strong></p></div>

<h2>この記事が主張すること</h2>
<p>Chase 自身の定義は、多くの人の直感より技術的で、範囲も広いと最初に断ったうえで示される。</p>
<blockquote><p>&#8220;An agent is a system that uses an LLM to decide the control flow of an application.&#8221;</p></blockquote>
<p>（エージェントとは、LLM を使ってアプリケーションの制御フローを決めるシステムだ。「制御フロー」とは、プログラムが次にどのステップを実行するかのことにすぎない。）</p>
<p>彼はすぐに、この定義が完璧ではないことを認める——LLM が 2 つの経路のどちらかを選ぶだけの単純なシステムも、彼の定義では agent に含まれるが、多くの人の「agent」という直感には合わない。何を「本物の」エージェントに含めるか、含めないかを争うのではなく、彼は Andrew Ng の言い方を採用する——彼は Ng のツイートを引用し、出典を明記している：「rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic」（どの仕事を「本物の」エージェントに含めるか、含めないかを争うより、システムには agentic である度合いにさまざまな段階があると認めればいい）。Chase 自身のコメントはこうだ：「I really agree with this viewpoint and I think Andrew expressed it nicely」（私はこの見方に心から同意する。Andrew はうまく言い表したと思う）。そこから：システムがどれだけ LLM に自分の動き方を決めさせているかによって、システムはより「agentic」になっていく。固定されたルーターから、状態機械、そして自分でツールを作り、記憶する完全に自律したエージェントまで。このスペクトラムをもとに、彼は実際的な主張を展開する：システムが agentic であるほど、あるインフラがより重要になり、中でも一番重要なのが可観測性だ。</p>
<blockquote><p>&#8220;You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.&#8221;</p></blockquote>
<p>（内部で何が起きているかを観察できる必要がある。実際に取られるステップは、事前には分からないことがあるからだ。）</p>
<p>彼はさらに、見るだけでなく介入する能力も必要だと主張を進める：動いているエージェントの状態や指示を、ある時点で修正できる能力もほしくなる。もし意図した経路から外れているなら、それを軌道に戻すために。Chase はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。</p>

<h2>ここから先は、私たちの解釈であって、Chase の主張ではない</h2>
<p>Chase が語っているのは、エージェントのフレームワークを作る人向けのツール——彼は LangGraph と LangSmith を名指ししている——についてであって、完成した文書を読む人についてではない。とはいえ、彼のスペクトラムは、読み始める前に手元のものを見積もる、とても実用的な方法をくれる：あるファイルを生み出したシステムが agentic であればあるほど、その手順がもとのプロンプトから予測できるとは期待しないほうがよく、手元のファイルは「本来起きるはずだったこと」の記録というより、「実際に何が起きたか」の記録として読む価値が増す。彼が言う「内部で何が起きているかを観察する」とは、動いているシステムの内部状態——trace（1 回の実行のあいだにエージェントが行ったすべての記録）、途中のステップ、ツール呼び出し——についてであり、あとから Markdown の計画を読むことについてではない。ただし彼が挙げる理由——手順が事前には分からない——は、エージェントが仕事を終えたあとにあなたに渡してくる文書にも同じように当てはまる：最初から手順が予測できないなら、終わったあとのレポートこそが、それをチェックできる唯一の場所になる。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn は、動いているエージェントの内部を観察したりはしない——中に AI モデルはなく、そのファイルを生み出したどんなフレームワークにも接続していないので、あるエージェントが Chase のスペクトラムのどこにいたかを教えてくれることもない。MarsDawn が扱うのは、事後にあなたの手元に届く文書のほうだ：サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブが、長いレポートの形をはっきり見せてくれる。ソースとレンダリングされたプレビューは並んで表示され（&#8984;2）、図や数式を扱う。エージェントがファイルを書き換えたときは再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ——これは「まだ動いているものを見ている」ことの、ファイル版だ。「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）と「AI 用にコピー」（&#8963;&#8997;&#8984;C）を使えば、どのステップで外れたかを正確に指し示せる。これは、走り出したエージェントを軌道に戻すことの、文書版にあたる。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>このシリーズによる、透明性とチェックポイントについてのより完全な議論：<a href="/ja/agent-transparency/">「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」</a></li>
  <li>LangChain が 2026 年に、この記事と同じ URL で発表した新しい記事。定義はほぼ同一：<a href="/ja/reading-notes/langchain-what-is-an-agent/">「Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Harrison Chase、「What is an agent?」、LangChain、2024 年 6 月 28 日、アーカイブ版：<a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a>（Wayback Machine 経由で 2026-09-26 に取得・引用。元の URL には現在、Jess Ou が 2026 年に書いた別の記事が表示される）</li>
</ul>
""",
    }
    pages['reading-notes/langchain-what-is-an-agent'] = {
        "title": "Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事 · MarsDawn",
        "description": "LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。",
        "body": f"""
<section class="intro">
  <h1>Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事</h1>
</section>

<div class="summary"><p><strong>2026 年 7 月、LangChain は Harrison Chase の 2024 年の記事「What is an agent?」があった URL に、新しい「What is an AI agent?」を公開した——今回は Jess Ou が書いたもので、定義は当時の彼の一文とほぼ一言一句同じだ。彼女の記事の大半は、彼の記事が扱わなかったこと、つまりエージェントを自動的に評価する一連のパイプライン全体について書かれている。そのパイプラインのどこにまだ人が必要で、どこはもう必要ないか、彼女の文章は率直に書いている。</strong></p></div>

<h2>この記事が主張すること</h2>
<p>Ou の定義は、Chase のあの一文をほとんどそのまま繰り返している。</p>
<blockquote><p>&#8220;An AI agent is a system that uses a large language model to decide the control flow of an application.&#8221;</p></blockquote>
<p>（AI エージェントとは、大規模言語モデルを使ってアプリケーションの制御フローを決めるシステムだ。「制御フロー」も、次にどのステップを実行するかのことを指す。）</p>
<p>そこから彼女は、LangChain の Agent Development Lifecycle を説明する：build、test、deploy、monitor の 4 段階と、人がすべての実行記録を読まなくてもエージェントの働きをチェックできる、階層的なやり方だ。online evals は本番のトラフィックの trace（1 回の実行の記録）をサンプリングして退行を検出し、offline evals は整理されたデータセットに対して実行し、変更をリリースする前に問題を見つける。「LLM-as-a-judge」は、人があらかじめ決めた基準にしたがって 1 回の実行の出力に点数をつける方法で、人手によるレビューでは届かない規模で動く。彼女はまた、このパイプラインの中で人がまだどこに立つべきかについても、率直に書いている。</p>
<blockquote><p>&#8220;For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.&#8221;</p></blockquote>
<p>（慎重な扱いが必要な、あるいは取り消せない行動については、承認、編集、拒否、または明確化のためにエージェントを一時停止させる human-in-the-loop の仕組みを勧める。）</p>
<p>また彼女には、パイプラインがどれだけ整っても省けない判断についての一文もある：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（自分で評価できない判断を、外部に任せてはいけない。あなたが正しい答えを見分けられないなら、エージェントにもできない。）<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a>はすでにこの一文をもとに議論を組み立てているので、このノートでは繰り返さない。Ou はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。また彼女は Chase の名前にも一度も触れていない。この 2 つの記事をつないでいるのは、LangChain が 2026 年に、Chase の 2024 年の記事があった URL に彼女のこの記事を公開したこと、そして定義がほぼ同一であることだ——これは私たちの観察であって、彼女自身の主張ではない。</p>

<h2>ここから先は、私たちの解釈であって、Ou の主張ではない</h2>
<p>Ou の言う human-in-the-loop は、特定の行動が実行される前にそれを止めること——write の動作を一時停止し、人の承認を待つこと——についてであり、これは Chip Huyen の read-only／write action という分け方を、別の角度から見たのと同じことだ。完成したレポートをあとから読むこととは違う。彼女のパイプライン全体をよく見ると、その大部分は、人を日常的なチェックから外すために設計されている。加えるためではない：online evals、offline evals、LLM-as-a-judge が存在する目的は、そのままチームが 1 回 1 回の実行記録を手作業で確認しなくて済むようにすることだ。これはこの記事への批判ではない——それは彼女自身がはっきり述べている目標であり、本番の規模ではもっともなことでもある。ただしそれは、あなたが自分の手で行うレビュー——エージェントが渡してきた計画やレポートを直接読むこと——が、まさに彼女のパイプラインが減らそうとしている、置き換えようとしているのではない、その種のチェックであることを意味する。彼女自身のあの判断についての一文は、その削減に下限を引いている：自分で読んでも正しいかどうか見分けられない場所は、それでも自分で読むしかない。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn は評価パイプラインではなく、中に AI モデルもない——1 回の実行記録に点数をつけたり、LLM-as-a-judge を走らせたり、どの行動が一時停止するほど機密性が高いかを決めたりはしない。MarsDawn がしているのは、彼女のパイプラインがそれでも人に残しているその瞬間、つまり直接読むことだ。サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブが、長いレポートの見出しを一覧にする。ソースとレンダリングされたプレビューは並んで表示され（&#8984;2）、Mermaid と KaTeX はそのまま描画される。「編集 &#9656; 参照をコピー」（&#8997;&#8984;C）と「AI 用にコピー」（&#8963;&#8997;&#8984;C）を組み合わせれば、抜き取りチェックを、エージェントが理解でき、直せる具体的なフィードバックに変えられる。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>彼女の「判断を外部に任せるな」という一文を一部使って組み立てた、完全なチェックリスト：<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a></li>
  <li>この定義が 2024 年に最初どう書かれていたか：<a href="/ja/reading-notes/harrison-chase-what-is-an-agent/">「Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Jess Ou、「What is an AI agent?」、LangChain、2026 年 7 月 31 日：<a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a>（2026-09-26 に取得・引用）</li>
</ul>
""",
    }
    pages['reading-notes/andrew-ng-design-patterns'] = {
        "title": "Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする · MarsDawn",
        "description": "The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。",
        "body": f"""
<section class="intro">
  <h1>Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする</h1>
</section>

<div class="summary"><p><strong>2024 年の初め、Andrew Ng は The Batch の 5 本の手紙で、4 つの agentic な設計パターン——reflection（反省）、tool use（ツール利用）、planning（プランニング）、multi-agent collaboration（複数エージェントの協調）——を説明した。そして珍しく、この 4 つのうちどれをより信頼でき、どれを予測しづらいと感じているかを、読者にはっきり伝えている。</strong></p></div>

<h2>これらの手紙が主張すること</h2>
<p><a href="/ja/agent-design-patterns/">「4 つのエージェント設計パターンと、それぞれが渡してくる文書」</a>は、この 4 つのパターンがそれぞれ何であるか、私たち自身の推論として、それぞれが普通あなたに何を渡してくるか、そして Part 4 から引用した、planning についての Ng 自身の評価——「while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications&#8217; performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do」（Reflection と Tool Use という設計パターンは、どちらも自分のアプリケーションで確実に動かし、性能を高められている。しかし Planning はまだ成熟していない技術で、それが何をするか事前に予測するのは難しいと感じる）——をすでにくわしく扱っている。このノートで補うのは、あの記事が使っていない、残り 2 本の手紙にある同じランク付けだ：Part 3 は Part 4 の 1 週間前に書かれ、先にこのランク付けを述べている。Part 5 は、Part 4 が触れていないパターン——multi-agent collaboration——にまでランク付けを広げる。tool use を紹介する Part 3 で、彼はこう書いている。</p>
<blockquote><p>&#8220;In future letters, I&#8217;ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable &#8212; albeit very exciting &#8212; technologies.&#8221;</p></blockquote>
<p>（今後の手紙では、Planning と Multi-agent collaboration という設計パターンについて説明する。これらは AI エージェントにずっと多くのことをさせられるが、成熟度が低く、予測しづらい——とはいえ、とても刺激的な——技術だ。）</p>
<p>2 週間後、彼はシリーズの最後の手紙で multi-agent collaboration を扱いながら、別の角度から同じランク付けを確認している。</p>
<blockquote><p>&#8220;Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.&#8221;</p></blockquote>
<p>（Planning という設計パターンと同じように、multi-agent collaboration の出力品質は予測しづらいと感じる。特に、エージェント同士を自由にやり取りさせ、複数のツールを与えたときはそうだ。より成熟した Reflection と Tool Use のパターンのほうが、より信頼できる。）</p>
<p>彼が語っているのは、これらのパターンが自分のアプリケーションの成果をどれだけ高めるかについてであって、その出力をどれだけ注意深く審査すべきかについてではない——このシリーズは人によるレビューをまったく求めておらず、MarsDawn にも、どんな Markdown ツールにも触れていない。</p>

<h2>ここから先は、私たちの解釈であって、Ng の主張ではない</h2>
<p>Ng のランク付けは、開発者の椅子から見た出力品質と予測可能性についてのものだが、大まかに言えば、それぞれのパターンが残す記録に、あなたの側からどれだけの注意を払う価値があるかにも対応している。彼がより信頼できると感じている reflection と tool use は、たいてい「すでに終わった作業」を描くもの——修正済みの草稿、何を実行したかのレポート——を渡してくるので、そのなかの 1 つの主張を実際の出力と照らし合わせれば、たいていリスクの大部分をカバーできる。彼が予測しづらいと感じている planning と multi-agent collaboration は、たいてい「まだ起きていないこと」について書かれたもの、あるいは複数のエージェントに分散した複数のファイルを渡してくる：あなたの承認を待っている計画や、まだ実行によって検証されていないエージェント間の引き継ぎだ。彼自身の言葉を借りれば、この 2 つこそ、「書かれていること」と「実際に起きること」のギャップが一番大きい場所であり——これはまさに「エージェントの計画を 5 分でレビューする」が、Chip Huyen のエッセイから引き出している「実行前に手間をかける理由」という節の道理でもある。何かが実行される前に問題を見つけることが、一番安く済むタイミングだ。</p>

<h2>MarsDawn が助けになるところ、ならないところ</h2>
<p>MarsDawn は、あるファイルが Ng の 4 つのパターンのどれから生まれたのかを知らないし、何かを予測可能性でランク付けすることもなく、中に AI モデルもない——彼のランク付けが示唆しているようなチェックを、代わりにしてくれるわけではない。MarsDawn がしているのは、あなた自身がチェックするあいだ、ファイルを読みやすく保つことだ：サイドバー（「表示 &#9656; サイドバーを表示」、&#8963;&#8984;S）のアウトラインタブで、長い計画の形が見て取れる。ソースとレンダリングされたプレビューは並んで表示される（&#8984;2）。複数エージェントの引き継ぎの場合は、「ファイル &#9656; フォルダを開く&#8230;」（&#8679;&#8984;O）で共有フォルダを開くと、別々のエージェントが新しいファイルを書いたとき、それはおよそ 1 秒でファイルタブに現れ、リストの上には git のブランチや worktree の名前も表示されるので、別々のエージェントが書いた同じ名前のファイルを取り違えることもない。</p>

<h2>試してみる</h2>
<p>MarsDawn は Mac App Store で配信中です。無料の <code>marsdawn</code> コマンドラインツールは今日から使えます：</p>
<pre><code>{k.INSTALL}</code></pre>
<p>アプリなしで Markdown を PDF に書き出せます。</p>
<p><a href="/ja/cli/">コマンドライン</a> &#183; 購入前に：<a href="/ja/limits/">MarsDawn ができないこと</a></p>

<h2>次に</h2>
<ul>
  <li>それぞれのパターンが渡してくる文書の全体像：<a href="/ja/agent-design-patterns/">「4 つのエージェント設計パターンと、それぞれが渡してくる文書」</a></li>
  <li>実行前に計画を 5 分でレビューする方法：<a href="/ja/reviewing-agent-plans/">「エージェントの計画を 5 分でレビューする」</a></li>
  <li>シリーズに戻る：<a href="/ja/reading-notes/">「編集者の読書ノート」</a></li>
</ul>

<h2>出典</h2>
<ul>
  <li>Andrew Ng、「Agentic Design Patterns Part 1」、The Batch、2024 年 3 月 20 日：<a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng、「Agentic Design Patterns Part 3: Tool Use」、The Batch、2024 年 4 月 3 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/</a>（2026-09-26 に取得・引用）</li>
  <li>Andrew Ng、「Agentic Design Patterns Part 4: Planning」、The Batch、2024 年 4 月 10 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a>（引用は <code>design/inbox/276-agent-blog-series.md</code> からそのまま再利用したもので、<code>/ja/agent-design-patterns/</code> ですでに使われている）</li>
  <li>Andrew Ng、「Agentic Design Patterns Part 5, Multi-Agent Collaboration」、The Batch、2024 年 4 月 17 日：<a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/</a>（2026-09-26 に取得・引用）</li>
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
