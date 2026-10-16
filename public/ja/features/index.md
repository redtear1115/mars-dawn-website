# MarsDawn でできることを、1ページで。

MarsDawn は Mac 用の Markdown エディタです。片側で書き、もう片側で整形されたページを読めて、図や数式、コードもそのまま描画されます。独自の AI モデルは持っていません。エージェントが書いたものを読むために、そして自分の文章を書くために作られています。作業の場が会議の席やファイル棚に移るときは、きれいなページをプリントしたり書き出したりできます。

以下の各セクションで、アプリにできることを説明し、さらに詳しいページへのリンクを付けています。

![MarsDawn の分割ビュー：左が Markdown のソース、右がレンダリングされたページ。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

このスクリーンショットの内容：

1. ネイティブの Mac ウインドウ。
2. Mac のテキストエディタに、Markdown ハイライトを追加したもの。
3. ⌘1 でソース、⌘2 で分割、⌘3 でプレビュー。
4. 入力するとページが更新されます。

## エージェントが書いたものを読む

### ソースとプレビューを並べて表示

Markdown ファイルを開くと、整形されたページがソースの隣に表示されます（⌘2）。ソースのみ（⌘1）、プレビューのみ（⌘3）にも切り替えられます。両側は一緒にスクロールし、ページは入力に合わせて更新されます。

[Mac アプリ](/ja/native/)

### アウトラインとファイルのサイドバー

サイドバーの「アウトライン」には書類の見出しが並び、クリックするとその位置に移動します。フォルダを開くと「ファイル」タブに中身が一覧表示され、エージェントが書き込んでいるあいだも新しいファイルが自動的に現れます。フォルダが git のチェックアウトなら、見出しにブランチまたはワークツリーの名前が表示されます。

[エージェントが返してくるものを読む](/ja/reading-agent-output/)

### 正確な行を示す

「編集 ▸ 参照をコピー」は、現在の位置を `docs/plan.md:42` のようにパスと行番号でコピーします。「AI 用にコピー」は、その下に選択したテキストも付けます。どちらもエージェントのチャットにそのままペーストできます。

[エージェントが返してくるものを読む](/ja/reading-agent-output/)

### ファイル間のリンクをたどる

プレビューで別の Markdown ファイルへのリンクをクリックすると、MarsDawn がそのファイルを開き（すでに開いていれば前面に出し）、見出しの位置までスクロールします。

## 紙の上で、人と人のあいだで

すべての作業が画面の上で行われるわけではありません。MarsDawn がプリントして書き出すページは画面で読むページそのものなので、人が集まり、読み、記録を残す場面で使えます。

### 会議で

ページをプリントするか、同じ PDF を全員に送れば、1つの画面を囲むのではなく、全員が同じ書類で作業できます。同じファイルを持っていれば改ページ位置も同じなので、「3ページの表」は誰にとっても同じものを指します。そのあと、人が決定事項を、プリントした紙の上やメモに書き留めます。会議メモのテンプレートは決定事項から始まり、各アクションアイテムに担当者を置きます。

[PDF 書き出し](/ja/pdf/) · [議事録テンプレート](/ja/templates/meeting-notes/)

### ペンで読む

ペンを使うほうが頭に入る人もいます。線を引き、余白に書き込み、記憶に残すためです。書類をプリントして、紙の上でそうしてください。MarsDawn 自体には注釈ツールがないので、PDF に書き込みたい場合は、お使いの PDF アプリを使ってください。

[PDF 書き出し](/ja/pdf/)

### 紙での記録

分野によっては、いまも紙で保管します。会計はその一例です。MarsDawn は保管やコンプライアンスについて何も謳っていません。できるのは、きれいに改ページされたページをプリントして書き出すことです。図は描画され、短いコードブロックや表は途中で切れず、テーマのライトの配色で出力されます。紙がいまも正式な記録である場面で使ってください。

[PDF 書き出し](/ja/pdf/)

### Markdown を使わない人に渡す

PDF はどんなアプリでも開け、Markdown の知識も要らないので、上司やクライアントに送るのにも向いています。

[書き出した PDF を共有する](/ja/sharing-exported-pdfs/)

## 書く、レイアウトする

### プレーンな Markdown、ハイライト付き

太字、斜体、取り消し線、インラインコード、リンク、引用、ToDo リストがすべて使えます。エディタは Markdown の構文に色を付け、その色はプレビューのテーマと揃います。

[Mac アプリ](/ja/native/)

### 拡大・縮小、行番号、ステータスバー

ソースとプレビューを一緒に 50% から 300% まで拡大・縮小できます。ソースの横には行番号の欄があり、ステータスバーにはカーソルの行と列、そして書類または選択範囲の文字数、単語数、読む時間が表示されます。

### イメージ

書類を保存してから、イメージをエディタにドラッグまたはペーストします。MarsDawn は書類の横の assets フォルダにコピーし、リンクを書き込みます。Web 上のイメージは「イメージを読み込む」を押すまで表示されないので、書類を開いても、読んだことがサーバに知られることはありません。

[あなたの文章は Mac に残ります](/ja/yours/)

### フロントマターは邪魔になりません

ファイル先頭のフロントマター（front matter）のブロックは、プレビューとクイックルックでは折りたたまれた「書類の情報」として表示され、PDF には出力されません。

### 8つの言語

アプリは、英語、繁体字中国語、簡体字中国語、日本語、ドイツ語、フランス語、スペイン語、韓国語に対応しています。

[Mac アプリ](/ja/native/)

## 図、コード、数式

### Mermaid の図

`mermaid` と指定したコードブロックは図として描画されます。図に誤りがあると、プレビューにはそのソースとエラーが下に表示され、メッセージをクリックするとその行に移動します。

[Mac で Mermaid をプレビューする](/ja/mermaid-preview-mac/)

### ハイライトされたコード

コードブロックは、一般的なほとんどの言語でハイライトされます。先頭の ````` の後ろに言語名を書くだけです。

### 数式

KaTeX の構文で書いた数式は、プレビューとクイックルックで描画され、書き出した PDF にも反映されます。

[AI の出力を人が確認する理由](/ja/reviewing-ai-output/)

## テーマ、PDF、プリント

### 4つのテーマ、ライトとダーク

夜明け、クラシック、モダン、ビビッドには、それぞれライトとダークがあります。設定で選ばない限り、MarsDawn は Mac の外観モードに合わせます。「表示 ▸ プレビューのテーマ」またはツールバーのパレットボタンから選べます。

[プレビューテーマと PDF 書き出し](/ja/themes/)

### そのほかのテーマ

「設定 ▸ 外観モード ▸ テーマを追加…」で、追加のプレビューテーマのギャラリーが開きます。インストールしたものは「表示 ▸ プレビューのテーマ」に並び、「取り除く」で削除できます。ギャラリーは開いているあいだだけオンラインになります。

[テーマギャラリー](/ja/themes/gallery/) · [テーマを作る](/ja/themes/new/)

### PDF として書き出す、またはプリント

「ファイル ▸ PDF として書き出す…」は改ページ済みの PDF を保存し、「ファイル ▸ プリント…」は同じページをプリントします。Mermaid の図は描画され、コードはハイライトを保ち、改ページでは見出しが節から離れたり、短いコードブロックや表、図が途中で切れたりしないようにします。ダークで読んでいても、PDF は常にテーマのライトの配色です。

[PDF 書き出し](/ja/pdf/)

![MarsDawn から書き出した PDF を、ページのサムネイル付きの PDF ビューアで開いたところ。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

このスクリーンショットの内容：

1. Mermaid 図は PDF に描き込まれます。
2. コードはハイライトを保ちます。

## ファイル、タブ、クイックルック

### ウインドウとタブ

書類はそれぞれ別のウインドウで開きます。「ウインドウ ▸ すべてのウインドウを結合」を選ぶと、開いているウインドウを1つのウインドウのタブにまとめられます。自動保存は入力中に働きます。

[Mac アプリ](/ja/native/)

### Finder のクイックルック

Finder で Markdown ファイルを選んでスペースバーを押すと、図も含めて整形された状態で読めます。クイックルックは MarsDawn で選んだテーマを使い、その外観モードの設定に従います。

[Mac アプリ](/ja/native/)

### そのほかのファイル

MarsDawn では、テキストファイル（`.txt`、`.log`、ソースコード）と PDF も開けます。UTF-8 のテキストはそのまま編集でき、ソースのみの表示になります。PDF は、ページのサムネール、拡大・縮小、検索を備えたビューアで開きます。

### ファイルはあなたのもの

アカウントも、同期も、クラウドもありません。書類は保存した場所に残り、MarsDawn があなたに関するデータを収集することはありません。

[あなたの文章は Mac に残ります](/ja/yours/)

## エージェントとスクリプト向け

### 無料のコマンドラインツール

無料の `marsdawn` ツールは、Homebrew で別途インストールします。`marsdawn export` は Markdown ファイルを、MarsDawn のプレビューと同じ見た目の PDF にします。アプリは要りません。`--theme` でテーマを、用紙サイズは A4 か Letter を選べます。`marsdawn open` はファイルをアプリで開いて確認できるようにし、行を指定することもできます。こちらはアプリのインストールが必要です。

[コマンドライン](/ja/cli/)

### スクリプトが読める出力

`--json` を付けると、どちらのコマンドも、エージェントやスクリプトが解析できる結果を返します。

[AI エージェント向け marsdawn](/ja/cli/agents/)

### スキルと MCP サーバ

エージェント用のスキルファイルは、コーディングエージェントに、書いたものを MarsDawn で開いてあなたの確認に回すことを教えます。シェルのないクライアント向けには、別の MCP サーバが同じ export を実行します。

[エージェント用スキル](/ja/cli/skill/) · [MCP サーバー](/ja/cli/mcp/)

### AI は入っていません

MarsDawn は独自の AI モデルを持っていません。エージェントが書いたものを要約したり採点したりせず、長くて変わり続けるファイルを読みやすく保つだけで、読むのはあなたです。

[MarsDawn ができないこと](/ja/limits/)

## Siri とショートカット

「ショートカット」App で MarsDawn を検索すると、3つのアクションが見つかります：「新規 Markdown 書類」（テンプレートから）、「受信トレイにメモを追加」、「最近使った書類を開く」。メモは、「MarsDawn ▸ 設定… ▸ メモフォルダ」で選んだフォルダの `Inbox.md` に追加されます。

[Mac アプリ](/ja/native/)

## ページをプリントしたあと

プリントしたページを囲んで会議をし、余白にペンで書き込み、紙の記録をファイルに綴じる。

[MarsDawn の動画（88 秒）](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## Mac で試してみる

MarsDawn は無料でダウンロードできます。14日間はすべての機能を試せて、その後は USD 4.99 で一度だけ購入します。サブスクリプションもアカウントも不要です。macOS 26 以降が必要です。

[今すぐダウンロードして試す](https://apps.apple.com/app/id6812925073)

試用のしくみ：[無料で試して、一度だけ購入](/ja/pay-once/)。あえて入れていないこと：[MarsDawn ができないこと](/ja/limits/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で配信中です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類で、テーマギャラリーにはさらに多くあります。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で .md ファイルを開く方法](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Mac で Mermaid をプレビューする](https://marsdawn.southern-light.dev/ja/mermaid-preview-mac/index.md): Mac で Mermaid の図を Markdown の隣に描画：リアルタイムプレビュー、クイックルック、PDF 書き出し。図に誤りがあると、エラーとその行が表示されます。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・プリント書き出し。ブラウザで自分のテーマを作り、コミュニティギャラリーも閲覧できます。
- [テーマを作る](https://marsdawn.southern-light.dev/ja/themes/new/index.md): 配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。
- [エージェントとテーマを作る](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [テーマギャラリー](https://marsdawn.southern-light.dev/ja/themes/gallery/index.md): コミュニティが投稿した MarsDawn のプレビューテーマを閲覧し、シナリオで絞り込み、問題があれば通報できます。ブラウザで自分のテーマを作れます。インストールも git も不要です。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [編集者の読書ノート](https://marsdawn.southern-light.dev/ja/reading-notes/index.md): AI エージェントを作っている人たちが実際に何を主張しているかを見る、6 本の短いノート——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain、Andrew Ng——それぞれが、エージェントの返してきたものを読む人にとって何を意味するか。
- [読書ノート：Anthropic](https://marsdawn.southern-light.dev/ja/reading-notes/anthropic-building-effective-agents/index.md): 2024 年 12 月に Anthropic が発表したガイドは workflow と agent を分けて考え、5 つの workflow パターンを説明している。そのうち 1 つは、もう一回の LLM 呼び出しがレビューを担う。これは、あなたのフォルダに落ちてくるものにとって何を意味するか。
- [読書ノート：Chip Huyen](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
- [読書ノート：Lilian Weng](https://marsdawn.southern-light.dev/ja/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng が 2023 年に書いた、広く引用されているサーベイは、LLM エージェントを、脳とプランニング、記憶、ツール利用の組み合わせとして描く。各部分が普通あなたに何を読ませることになるか、そして計画が予想外の事態に調整できないという、彼女自身が挙げる限界。
- [読書ノート：Harrison Chase](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
