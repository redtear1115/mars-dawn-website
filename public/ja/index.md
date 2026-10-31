ビルダーのためのフロンティアツール

# 地図を手に。夜明けを読む。

エージェント開発の舵を取る人のための Markdown。

MarsDawn は、Markdown を読んで確かめるための Mac ネイティブアプリです。分割ライブプレビュー、Mermaid の図、KaTeX の数式、クイックルック、PDF 書き出しに対応し、14 日間無料で試せて、一度だけ USD 4.99 で解除できます。

ページには操作できる MarsDawn のウインドウがあり、アプリ内蔵のようこそガイドの一部を表示しています。パレットのメニューで外観モード（システム、ライト、ダーク）を選び、ライトとダークそれぞれに 4 つのプレビューテーマ（夜明け、クラシック、モダン、ビビッド）から 1 つを選べます。ツールバーでは 3 つのレイアウト（ソース、分割、プレビュー）から選べます。

## 席を離れても、エージェントが書いたものを読める

1. Mac で、エージェントにファイルを iCloud Drive のフォルダへ保存させます。
2. iPhone や iPad で MarsDawn を開き、そのファイルを選びます。
3. 編集や PDF の書き出しは、Mac に戻って行います。

iPhone と iPad では閲覧専用で、開けるのは Markdown とプレーンテキストのファイルだけです。

[![App Storeからダウンロード](/assets/badges/app-store-ja.svg)](https://apps.apple.com/app/id6812925073)

[iPhone と iPad 版について詳しく](/ja/features/#iphone-ipad)

## エージェントが書いた Markdown を読む。

1. **エージェントが書く。**あなたのコーディングエージェントやライティングアシスタントが Markdown の下書きを作ります。README、仕様書、メモなど。
2. **MarsDawn で確認する。**ファイルを開き、[Mermaid 図](/ja/mermaid-preview-mac/)やハイライトされたコードとともにレンダリングされたページを、ソースの隣で読みます。
3. **エージェントが修正する。**変更を依頼します。修正されたファイルを開き、同じように読みます。

[エージェントが返してくるものをどう確認するか](/ja/reading-agent-output/) · [Mac で .md ファイルを開く方法](/ja/view-markdown-on-mac/)

## エージェントの計画を、実行する前に読む。

順番のおかしい手順を見つけ、その行を示して、エージェントに戻します。

1. 変更を見る：エージェントが保存すると、開いているウインドウがディスクから更新されます。一度の操作で取り消せます。
2. その行へ：marsdawn open plan-checkout-v2.md:10 でウインドウが 10 行目に移り、プレビューの該当ブロックが光ります。
3. 返す：「参照をコピー」（⌥⌘C）で plan-checkout-v2.md:10 をコピーし、コメントを添えてエージェントとのチャットに貼ります。

## 今すぐできること

無料の `marsdawn` コマンドラインツールは今すぐ使えます。Homebrew でインストール：

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` は Markdown ファイルを、MarsDawn のプレビューと同じ見た目の PDF にします。アプリは要りません。
- `marsdawn open` はファイルを MarsDawn アプリで開き、確認できるようにします。
- `--json` は、スクリプトやエージェントが解析できる結果を返します。

[コマンドライン](/ja/cli/) · [AI エージェント向け marsdawn](/ja/cli/agents/) · [エージェント用スキル](/ja/cli/skill/) · [MCP サーバー](/ja/cli/mcp/)

## MarsDawn に期待できること

- [Mac アプリ](/ja/native/)：ネイティブのウインドウとタブ、自動保存、[クイックルック](/ja/quicklook/)。
- [あなたの文章は Mac に残ります](/ja/yours/)：アカウント不要、同期なし、クラウドなし。
- [無料で試して、一度だけ購入](/ja/pay-once/)：14日間無料、その後は一度だけ USD 4.99。サブスクリプションはありません。
- [機能一覧](/ja/features/)：MarsDawn でできることを、1ページで。
- [テーマ](/ja/themes/)：4種類を内蔵、ギャラリーにはさらに多く。

購入前に知っておくこと。 [MarsDawn ができないこと](/ja/limits/)

## それぞれの役割

MarsDawn 1.1.1、marsdawn 0.6.4、marsdawn-mcp v0.2.4 の時点で、それぞれができること。

| 機能 | アプリ | CLI | MCP／skill | 状態 |
|---|---|---|---|---|
| 行を指定して開く | その行へ移り、プレビューのブロックが光る | marsdawn open notes.md:120（--background で前面に出ない） | open_in_marsdawn、skill は一度だけ開く | 提供中 |
| PDF 書き出し | ファイル ▸ PDF として書き出す…（⌥⌘E） | marsdawn export、アプリ不要 | export_markdown_to_pdf、skill | 提供中 |
| JSON の結果 | — | open と export に --json | MCP は同じ JSON を返す | 提供中 |
| エージェント用スキル | — | marsdawn skill --install | 一度開く・書き出すを教える | 提供中 |
| MCP サーバー | — | 内部で実行 | marsdawn-mcp：ツール 2 つ、許可したフォルダだけ | 提供中 |
| AI 用にコピー、参照をコピー | 編集 ▸ AI 用にコピー（⌃⌥⌘C）、参照をコピー（⌥⌘C） | — | —（どのエージェントにも貼れる） | 提供中 |
| 保存を自動で反映 | 保存された変更を反映、取り消しは一度で | — | skill：もう一度開かない | 提供中 |
| Claude Code の hook | — | open --background を使用 | /cli/agents/ の hook スクリプト | ドキュメントあり・任意 |

提供中：上に書いたリリース版に含まれています。ドキュメントあり・任意：このサイトの手順で自分で追加するもので、ツールには含まれません。予定：まだなく、日付は未定です。予定：MCP の open_in_marsdawn にフォルダのオプション。--folder などほかのオプションは[コマンドライン](/ja/cli/)へ。

## コーディングエージェントと Mac アプリを作るなら

個人で Mac アプリを作る開発者へ。エージェントが書いたファイルを MarsDawn で開く、いまの方法です。

| ツール | 組み合わせ方 | 設定 |
|---|---|---|
| Claude Code | skill に従い、書いたファイルを一度だけ、その行で開きます：`marsdawn open plan.md:42`。オプトインの hook を入れると、書いた .md をそのつどバックグラウンドで開きます | `marsdawn skill --install`、hook スクリプトは /cli/agents/ に |
| Codex、Cursor、Xcode | 専用の設定ガイドはまだありません。シェルコマンドを実行できるツールなら `marsdawn open file:line --json` を呼べます。指示ファイルを読むエージェントは SKILL.md（`--dir`）、MCP だけのクライアントは marsdawn-mcp を使えます | `brew install redtear1115/tap/marsdawn` |

hook とコマンド：[AI エージェント向け marsdawn](/ja/cli/agents/) · [エージェント用スキル](/ja/cli/skill/) · [MarsDawn ができないこと](/ja/limits/)

MarsDawn、VS Code のプレビュー、Obsidian、QLMarkdown、LynxOffice で迷っていますか。比較ページに、各社の記載、MarsDawn にないもの、MarsDawn がいらない場面をまとめました。[比較を見る](/ja/vs/)

## 文書はあなたの Mac に残ります

Mac の中で。閲覧、編集、レンダリング、[PDF 書き出し](/ja/privacy/#exporting-and-printing)、[marsdawn コマンドライン](/ja/privacy/#the-marsdawn-command-line-tool)はすべて手元で動き、オフラインでも使えます。アプリが文書をアップロードすることはありません。

詳しくは：[プライバシーポリシー](/ja/privacy/#what-stays-on-your-mac)

初期設定ではネットにつながりません。Web のイメージは「イメージを読み込む」をクリックするか、設定で「リモートイメージを自動的に読み込む」をオンにしたときだけ読み込まれ、HTML 文書は静的に開き、コードは実行されません。

詳しくは：[プライバシーポリシー](/ja/privacy/#when-marsdawn-uses-the-internet)

外に出るのは、あなたが選んだときだけ。「AI 用にコピー」はテキストをクリップボードに置くだけで、貼るのはあなたです。テーマのダウンロード、「表示 › この書類を実行」で実行した文書、エージェントに読ませたファイルも、あなたが選んだときだけ外に出ます。

詳しくは：[プライバシーポリシー](/ja/privacy/#when-marsdawn-uses-the-internet)

## よくある質問

### MarsDawn とは何ですか？

MarsDawn は、エージェントが書いた Markdown を読んで確かめるための Mac ネイティブアプリです。ソースの横にライブプレビューを並べ、Mermaid と KaTeX を描画し、クイックルックで .md をプレビューし、PDF に書き出せます。ソースの編集もできます。

### MarsDawn はサブスクリプションですか？

いいえ。MarsDawn は無料でダウンロードでき、14日間はすべての機能を試せます。そのあとは USD 4.99 のApp 内課金を一度行うだけで、ずっとロック解除されます。更新はなく、アカウントも不要です。

### MarsDawn は iPhone や iPad で使えますか？

はい、閲覧用です。iPhone と iPad の MarsDawn は Markdown とプレーンテキストのファイルを開き、Mermaid 図、数式、コード、表を整えて表示します。アウトラインとテーマも使えます。編集と PDF の書き出しはできません。iOS 26 または iPadOS 26 以降が必要です。同じ Apple Account なら、1回のトライアルと1回のロック解除で、Mac、iPhone、iPad の MarsDawn をすべて利用できます。

詳しくは：[ロードマップ](/ja/roadmap/)

### Claude Code から MarsDawn でファイルを開けますか？

はい。無料の marsdawn コマンドラインツールには open コマンドがあり、Markdown ファイルを MarsDawn で開けるので、Claude Code やシェルコマンドを実行できるエージェントから呼び出せます。Claude が Markdown ファイルを書いたり編集したりするたびに開く、任意で有効にする Claude Code フックもあります。

### MarsDawn は文書をアップロードしますか？

いいえ。アプリが文書をアップロードすることはなく、あなたに関するデータも集めず、アカウントもありません。文書と設定は Mac に残ります。文書が Web を参照していて、それを読み込むと選んだときだけ、Mac がその内容をホストしているサーバから直接取得します。MarsDawn の開発者はその情報を一切受け取りません。

詳しくは：[プライバシーポリシー](/ja/privacy/#what-stays-on-your-mac)

### MCP または skill を使うと、ファイルを見られるのは誰ですか？

MarsDawn 自体は何も送りません。skill は指示を書いたテキストファイルで、marsdawn CLI と MCP サーバーは Mac の上で動き、MCP サーバーはあなたが許可したフォルダの中だけで動作します。ファイルを読むのはあなたのエージェントで、そのエージェントとモデル提供元がファイルをどう扱うかは、そのエージェントのポリシーによります。MarsDawn はそれを管理せず、説明もしません。

詳しくは：[MCP](/ja/cli/mcp/)

### 送られてきた HTML を開いても安全ですか？

初期状態では静的に開き、コードは実行されず、Web からも何も読み込まれません。「表示 › この書類を実行」を選ぶと、その文書が実行され、ネットワーク経由でデータを送ったり、同じフォルダの画像、スタイルシート、フォント、メディアを読んだりできるようになります。この選択は記憶されないので、次に開くときはまた静的です。

詳しくは：[プライバシーポリシー](/ja/privacy/#when-marsdawn-uses-the-internet)

### サイトの分析用クッキーはアプリと関係がありますか？

関係ありません。アプリとこのウェブサイトは別のものです。アプリはデータを収集せず、訪問が記録され得るのは marsdawn.southern-light.dev だけです。サイトの Google Analytics は最初は拒否の状態で、バナーで「同意する」を選んだあとにだけクッキーを設定し、フッターの「Cookie 設定」でいつでも変えられます。アプリが /themes/ のテーマファイルを取りに行くリクエストは記録されません。

詳しくは：[プライバシーポリシー](/ja/privacy/#the-website)

### ほかのアプリではなく MarsDawn を使う理由は？

必要ないかもしれません。自分のメモを書くのが中心なら、Obsidian のようなノートアプリのほうが向いています。VS Code でずっと作業しているなら、標準のプレビューが無料で使えます。Finder でファイルをさっと見たいだけなら、無料のクイックルック拡張機能で十分です。PDF にページ番号が必要なら、MarsDawn は付けられません。MarsDawn は、エージェントが書いた Markdown を読んでレビューするためのアプリです。ソースの横にライブプレビューがあり、エージェントの変更は一度で取り消せ、ファイルを指定の行で開けます。合わないと感じたら、その理由をメールで教えてください。

詳しくは：[MarsDawn とほかのツールの比較](/ja/vs/) · [Mac 向け Markdown ビューアのおすすめ](/ja/best-markdown-viewer-mac/)

### MarsDawn はこれからもメンテナンスされますか？

はい。MarsDawn が Mac App Store に登場してからのアップデートはすべて更新履歴に載っています。2026 年 10 月 28 日からは、iPhone と iPad でも MarsDawn で書類を読めます。MarsDawn のレンダリングの中核と無料の marsdawn コマンドラインツールは、すでに Apache-2.0 ライセンスで mars-dawn-kit としてオープンソースになっています。そして、MarsDawn の開発者がアプリのメンテナンスをやめるときは、アプリ自体のソースコードをオープンソースライセンスで公開し、ほかの人が引き継げるようにします。

詳しくは：[更新履歴](/ja/changelog/) · [ロードマップ](/ja/roadmap/) · [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)

## 実際のアプリ画面

### [Mac アプリ](/ja/native/)

![MarsDawn の分割ビュー：左が Markdown のソース、右がレンダリングされたページ。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

このスクリーンショットの内容：

1. ネイティブの Mac ウインドウ。
2. Mac のテキストエディタに、Markdown ハイライトを追加したもの。
3. ⌘1 でソース、⌘2 で分割、⌘3 でプレビュー。
4. 入力するとページが更新されます。

### [PDF 書き出し](/ja/pdf/)

![MarsDawn から書き出した PDF を、ページのサムネイル付きの PDF ビューアで開いたところ。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

このスクリーンショットの内容：

1. Mermaid 図は PDF に描き込まれます。
2. コードはハイライトを保ちます。

## その他

- [機能一覧](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
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
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
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
- [English](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 讀懂、檢查 agent 寫的 Markdown 的 Mac 原生 app：分割即時預覽、Mermaid、KaTeX、快速查看、PDF 輸出。可免費試用，之後一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
