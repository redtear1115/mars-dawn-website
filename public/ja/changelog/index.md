# 更新履歴

Mac App Store 版 MarsDawn アプリと、無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。アプリの日付は、そのバージョンが Mac App Store に公開された日です。

今後の予定は[ロードマップ](/ja/roadmap/)にあります。

## MarsDawn アプリ

### MarsDawn 1.1.1

2026年10月15日

- ドイツ語、日本語、スペイン語、フランス語では、「設定 > 外観モード > テーマを追加…」のシナリオの絞り込みが「シナリオ」というラベルのポップアップメニューになり、5つの選択肢が収まるようになりました。英語、韓国語、中国語では引き続きセグメンテッドコントロールを使います。
- テーマがテーマギャラリーから取り下げられたとき、「テーマを追加…」に表示されるお知らせに、内部 ID ではなくテーマ名（例：Inkwell Ivory）が表示されるようになりました。
- GitHub の書き方で書いた折りたたみ可能な details セクションが、プレビューとクイックルックで、要約を表示した折りたたみ状態で始まり、クリックすると開くようになりました。PDF への書き出しでは、引き続きすべてのセクションの内容が印刷されます。
- Finder、Dock、「ファイル > 開く…」、marsdawn open コマンドで開いた書類が、最前面のウインドウのタブとして開くようになりました。新規書類も同様です。以前の動作のままにするには、「設定 > 外観モード」で「システム設定に従う」を選びます。

### MarsDawn 1.1.0

2026年10月9日

- 「設定 > 外観モード」に「テーマを追加…」ボタンが加わりました。プレビュー用テーマのギャラリーが開きます。インストールしたテーマは「表示 > プレビューのテーマ」に並び、「取り除く」でいつでも外せます。ギャラリーがインターネットに接続するのは、開いている間だけです。
- Finder のクイックルックで、選んだテーマが使われるようになりました。以前は常に「夜明け」テーマでした。
- クイックルックは MarsDawn の外観モード設定にも従います。「ライト」または「ダーク」を選ぶと、Mac が逆の設定でもその外観のままです。「システム」では Mac の設定に従います。
- ウインドウタイトルの git マークが、ステージ済みで未コミットのファイルに「+」を表示するようになりました。以前は変更なしのように見えていました。
- プレビュー内の他の Markdown ファイルへのリンク（例：[notes](notes.md#plan)）をクリックすると、そのファイルが開きます。すでに開いている場合は前面に表示され、見出しの位置までスクロールします。ファイルがサイドバーのフォルダの外にある場合は、そのフォルダをサイドバーに追加するよう MarsDawn が案内します。追加したあと、もう一度リンクをクリックすると開きます。

### MarsDawn 1.0.2

2026年10月7日

- 修正：最初にレイアウトを切り替えたとき、またはサイドバーを表示・非表示にしたときに、エディタがわずかに上へずれることがなくなりました。
- 描画できない Mermaid 図では、エラーメッセージを全文表示するようになりました。行番号がわかる場合は、メッセージをクリックするとエディタ内の該当行へ移動します。

### MarsDawn 1.0.0

2026年10月5日

最初のリリースです。

## marsdawn コマンドラインツール

0.5.1 より前のバージョンは載せていません。

### marsdawn 0.7.2

2026年10月20日。ハンドブックレイアウト、コールアウト、日本語のフォント。

- manual レイアウトの名前が「ハンドブック」になりました：`marsdawn export --layout handbook`。`--layout manual` も使えますが、非推奨です。
- コールアウトを表示します。プレビューでも、書き出した PDF でも同じです。GitHub のアラート（`> [!NOTE]`、`> [!WARNING]` など）と、HackMD のコンテナ（`:::info`、`:::warning` など）に対応します。`:::spoiler` は折りたたみブロックになります。
- 日本語の書類では、かなと漢字に日本語のフォントを使います。言語は front matter の `lang: ja` から、書かれていなければ本文のかなの割合から判断します。
- ターミナルで `export` や `open` が成功したあと、エージェントスキルが入っていないか古いときは、stderr に一度だけヒントを表示します。stdout と `--json` の出力は変わりません。`MARSDAWN_NO_SKILL_HINT=1` を設定すると表示しません。

### marsdawn 0.7.1

2026年10月20日。ハンドブックレイアウトと、ファイルサイズの上限。

- `marsdawn export --layout manual` は、ハンドブックとして書き出します。余白を広くし、綴じ側を 25 mm 取り、レベル 1 の見出しごとに改ページします。front matter の title、subtitle、version、date、author、logo から作る表紙、レベル 1 と 2 の見出しをページ番号付きで並べた目次、`n / N` のページ番号、PDF のブックマークも付きます。目次ページの見出しは `--toc-title` で指定できます。デフォルトはこれまでどおり `--layout document` です。
- 1 行だけの `<!--BREAK-->` で改ページします。どちらのレイアウトでも使えます。
- `marsdawn export` は 16 MiB を超えるファイルを扱いません。コード 5 で終了し、`--json` では `input_too_large` を返し、何も書き出しません。
- プレビューページは script 要素と noscript 要素を取り除きます。Mermaid の図を描き直すときは、その図自身の SVG を保ちます。
- デコードすると `=` や `^` になる文字参照（`&#61;` など）は、HackMD の記法と対になりません。

### marsdawn 0.7.0

2026年10月18日。HackMD の記法、改行、とても大きなファイルの上限。

- HackMD のインライン記法 `==mark==`、`^sup^`、`~sub~` を表示します。`[TOC]` だけの段落は目次になり、HackMD の書き方の画像サイズが反映され、埋め込みタグは通常の https リンクになります。コードフェンスの言語は、`js=` などの HackMD のオプションより先に読み取ります。
- `marsdawn export --breaks` は、HackMD と同じように、段落内の改行をすべて改行として表示します。付けないときは、中国語や日本語の文字どうしのあいだの改行を取り除き、前後の行を 1 つの文としてつなげます。韓国語は単語を空白で区切るので、空白を残します。
- とても大きなファイルには、プレビューでも書き出した PDF でも上限があります。128K 文字を超えるコードブロックは色分けせず、合計 256K 文字を超えたところで色分けをやめます。1 回の更新で描く Mermaid の図は 100 個まで、数式は 1,000 個までです。残りの図は、前に描いたことがあっても、ソースを注記付きで表示します。
- シーケンス図で、`rect` ブロックの中のメッセージラベルの縁取りが、そのブロックの色になります。
- 表のすぐ上に脚注の参照があっても、`marsdawn export` がクラッシュしなくなりました。
- `marsdawn skill --install` は、フォルダを作れないときやファイルを書き込めないとき、コード 7（`skill_install_failed`）で終了します。既存の SKILL.md はそのままです。

### marsdawn 0.6.4

2026年10月13日。折りたためる `<details>` ブロック。

- GitHub 形式の `<details>` ブロックは、中に空行があっても1つの折りたためる要素として表示されます。プレビューでも、書き出した PDF でも同じです。これまでは最初の空行で分かれていました。
- PDF の書き出しでは、プリントの前にすべての `<details>` ブロックを開きます（front matter は除く）。
- `<details>` ブロックを開閉しても、プレビューのスクロール位置は変わりません。

### marsdawn 0.6.3

2026年10月6日。MarsDawn が Mac App Store で公開。

- アプリがインストールされていないとき、`marsdawn open` は Mac App Store の MarsDawn を案内します。
- README とエージェントスキルで `marsdawn open .` と `--folder` を説明します。MarsDawn 1.0.0 はフォルダをウインドウのサイドバーに表示します。

### marsdawn 0.6.1

2026年9月29日。テーマのチェック。

- `marsdawn theme validate` は、アプリと同じルールで `theme.json` をチェックします。有効ならコード 0、無効ならコード 1 で終了し、問題を 1 つずつ示します。`--require-complete` を付けると、シンタックスと図の色も必須になります。
- `marsdawn theme css` は、有効なテーマに対してプレビューが使う CSS を出力します。`marsdawn theme preview` は、そのテーマでサンプルの書類を PNG に描画します。ライトでもダークでも描けます。

### marsdawn 0.5.4

2026年9月26日。Mermaid の修正、図のエラーの行番号、スキルのインストール。

- シーケンス図で、メッセージのラベルがほかの参加者のライフラインをまたいでも、文字が読みやすいままです。プレビューでも、書き出した PDF でも同じです。
- `marsdawn export` が、Mermaid の図をたくさん含むファイルを書き出せるようになりました。図が 50 個あり、これまでコード 5 で終了していたファイルも書き出せます。
- `marsdawn export --json` に `diagramErrorDetails` が加わりました。図のエラーごとに、その図がファイルの何行目から始まるかと、Mermaid が行を示している場合はエラーそのものの行を、行番号で返します。
- `marsdawn skill --install` は、Claude Code 用のエージェントスキルを `~/.claude/skills/marsdawn/SKILL.md` にインストールします。`--dir` でほかのフォルダも指定できます。同じ内容のファイルがあればそのままにし、内容が違うファイルは `--force` を付けたときだけ置き換えます。付けないときはコード 64（`skill_differs`）で終了し、何も変更しません。

### marsdawn 0.5.3

2026年9月25日。フォルダの状態、Mermaid エラーの全文、そのほかの修正。

- `marsdawn open --folder` が、フォルダがどうなったかを返せるようになりました。状態を返すアプリが相手なら、`--wait` の秒数（デフォルトは 2 秒）まで応答を待ち、`--json` に `attached` や `needsUser` などの状態が入ります。
- Mermaid の図を解析できないとき、最初の行だけでなく Mermaid のエラーメッセージ全文を表示します。行番号もファイルの先頭から数えた値になりました。
- フロントマターの終わりを探すのは 1,000 行までになりました。閉じていないブロックがあっても、大きなファイルを毎回最後まで調べることはありません。
- 脚注の戻りリンクのラベルを、アプリが PDF の書き出しとプリント用に翻訳して渡せるようになりました。このラベルはページにはプリントされず、`marsdawn export` では英語のままです。
- 同梱の highlight.js を、KaTeX や Mermaid と同じく、バージョン、入手元、SHA-256 で記録するようになりました。

### marsdawn 0.5.2

2026年9月24日。脚注、コントラスト、フォルダ。

- 書き出した PDF に脚注が表示されます。参照には番号が付き、注は本文のあとに並びます。
- すべてのテーマが、ライトでもダークでも WCAG AA のコントラストを満たします。Classic は白黒になりました。
- `marsdawn skill` は、インストールされている marsdawn に合ったエージェントスキルを出力します。
- 見つかった MarsDawn がフォルダを表示できないとき、`marsdawn open` は成功を報告せず、コード 6（`app_cannot_open_folders`）で終了します。
- 書き出したページに描かれるプレースホルダが、ドイツ語、フランス語、スペイン語、韓国語にも対応しました。
- 相対パスがとても長くても、画像のプレースホルダにその先の絶対パスが表示されなくなりました。
- `MARSDAWN_APP_PATH` は、MarsDawn アプリを指しているときだけ使われます。

### marsdawn 0.5.1

2026年9月19日。PDF 書き出しと、コマンドラインからファイルを開くこと。

- 書き出した PDF のテキストレイヤーを、中国語、日本語、韓国語について修正しました。
- `marsdawn open --background` はファイルを開きますが、MarsDawn を前面には出しません。
- `marsdawn open` にフォルダを渡すと、MarsDawn がウインドウのサイドバーに表示します（MarsDawn 1.0.0 以降）。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown・JSON・YAML を確かめる Mac ネイティブアプリ。ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF。無料で試せて、一度だけ USD 4.99。
- [機能一覧](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown・JSON・YAML エディタ：リアルタイムプレビュー、Mermaid と数式、テーマ、会議や保管に使える PDF とプリントのページ。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックを分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad では編集不可、プラグインなし、アカウントなし。テーマは変更できますが、カスタム CSS は使えません。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で .md ファイルを開く方法](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Mac で Mermaid をプレビューする](https://marsdawn.southern-light.dev/ja/mermaid-preview-mac/index.md): Mac で Mermaid の図を Markdown の隣に描画：リアルタイムプレビュー、クイックルック、PDF 書き出し。図に誤りがあると、エラーとその行が表示されます。
- [Markdown のクイックルック](https://marsdawn.southern-light.dev/ja/quicklook/index.md): MarsDawn のクイックルックなら、Finder でスペースキーを押すだけで Markdown を描画して表示します。Mermaid 図、KaTeX 数式、ハイライトされたコードにも対応。トライアル終了後も使えます。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MarsDawn と比較：VS Code プレビュー、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Mac向けMarkdownビューアのおすすめ8選（2026年）](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [テーマ](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを備えた4種類の内蔵プレビューテーマに加え、Mac 版 MarsDawn の設定から開ける厳選ギャラリーも。クイックルックにも選んだテーマが反映されます。
- [テーマを作る](https://marsdawn.southern-light.dev/ja/themes/new/index.md): 配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。
- [エージェントとテーマを作る](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [テーマギャラリー](https://marsdawn.southern-light.dev/ja/themes/gallery/index.md): 開発者がレビューした MarsDawn のプレビューテーマを閲覧し、シナリオで絞り込み、問題があれば通報できます。ブラウザで自分のテーマを作れます。インストールも git も不要です。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [ロードマップ](https://marsdawn.southern-light.dev/ja/roadmap/index.md): Mac、iPhone、iPad 向け MarsDawn で開発中の機能と次に予定している機能を、バージョンごとにまとめました。日付は書かず、未定のものは明記しています。
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
