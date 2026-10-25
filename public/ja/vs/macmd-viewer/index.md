# MacMD Viewer と MarsDawn。

どちらも、Markdown を整ったページとして読むための Mac アプリです。MacMD Viewer は `.md` ファイルを開いて表示します。設計上、読み取り専用で、ファイルへの変更は一切保存しません。MarsDawn は同じようなレンダリングされたプレビューの隣にエディタを置くので、ひとつのウインドウで書いて読めます。このページでは両者を項目ごとに並べ、MacMD Viewer についての事実にはすべて出典を付け、MacMD Viewer のほうが向いている場合も述べます。

MacMD Viewer 自身のサイトとリポジトリで 2026 年 10 月 15 日に確認しました（バージョン 1.7.0、2026 年 10 月 10 日公開）。古くなっている点があれば、[サポートページ](/ja/support/)の連絡先までお知らせください。

## どんなもので、何ができるか

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 種類 | ビューア：「読み取り専用で、ソースファイルへの変更は保存しない」[[S1](#s1), [S9](#s9)] | ライブプレビューつきのエディタ：左に Markdown、右にレンダリングされたページ。3 つのレイアウト（ソース、分割、プレビュー） |
| 編集 | できない [[S1](#s1), [S7](#s7), [S9](#s9)] | できる。レンダリングされたページ自体は編集できず、隣のソースを編集する |
| ライブプレビュー | ファイルを表示する。ほかのエディタが保存すると自動で再読み込みする [[S9](#s9)] | 入力するたびに更新される。ほかのアプリがファイルを変更すると、MarsDawn は再読み込みして位置を保つ（自分の未保存の編集がない場合）。 |
| Mermaid | あり：フローチャート、シーケンス図、状態遷移図、ガントチャート、円グラフなど。オフラインで動作 [[S1](#s1), [S3](#s3), [S7](#s7)] | あり |
| 数式 | なし：README に「数式（LaTeX/KaTeX）は表示しない」と明記 [[S7](#s7)] | あり、KaTeX |
| コードのハイライト | あり [[S1](#s1), [S9](#s9)] | あり |
| テーマ | 12 種類のドキュメントテーマ [[S1](#s1), [S7](#s7)] | 標準で 4 種類（夜明け、クラシック、モダン、ビビッド）、それぞれにライトとダーク。テーマギャラリーにはさらに多数 |
| タブ | あり。任意で、初期設定はオフ（1.6.0 から）[[S5](#s5), [S8](#s8)] | あり |
| PDF 書き出し | あり。1 枚の連続したページで、現在のテーマ、透かしなし [[S3](#s3), [S9](#s9)] | あり。ページ分けされ、テーマのライトの配色。ページの区切りは短いコードを分断しないようにする |
| プリント | あり。macOS のプリントダイアログを使う [[S3](#s3), [S9](#s9)] | あり |
| Finder のクイックルック | あり。付属。システム設定で有効にする。選んだテーマを使う [[S4](#s4)] | あり。トライアル中でも期間後でも使える。選んだテーマを使う |
| クイックルックでの Mermaid と数式 | Mermaid：あり [[S4](#s4)]。数式：なし。数式は表示しない [[S7](#s7)] | あり。どちらも描画される |
| コマンドライン | 独立したコマンドラインツールの記載なし。`markdownviewer://` の URL スキームと、ファイルを開くための Claude Code のプラグインとフックがある [[S6](#s6)] | 無料の `marsdawn` ツール：`marsdawn export` はアプリなしで PDF を書き出し、`marsdawn open` は行を指定してファイルを開く |
| インターフェイスの言語 | 公式の資料に記載なし [[S1](#s1), [S3](#s3), [S7](#s7)] | 英語、繁体字中国語、簡体字中国語、日本語、ドイツ語、フランス語、スペイン語、韓国語 |
| 動作環境 | macOS 14（Sonoma）以降。Apple シリコンと Intel [[S1](#s1), [S7](#s7)] | macOS 26（Tahoe）以降 |
| ほかのプラットフォーム | Mac のみ [[S1](#s1)] | Mac のみ。iPhone や iPad のアプリはない |

## 価格と購入方法

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 購入場所 | 公式サイト、Homebrew、Setapp。Mac App Store には掲載なし [[S2](#s2), [S7](#s7)] | Mac App Store のみ |
| 価格 | 使用中の Mac 1 台につき USD 19.99 を一度（別の Mac に移せる）。Family Pack は 3 キーで USD 39.99。10 キーは USD 129 [[S2](#s2)] | 無料ダウンロード、その後 USD 4.99 を一度 |
| 購入前に試す | トライアルも無料版もなし。直接購入は 14 日以内なら全額返金 [[S2](#s2)] | 14 日間の無料トライアル。すべての機能が使える |
| 返金 | 14 日以内に、自社のサポート窓口を通じて [[S2](#s2)] | Apple 経由 |
| アップデート | 同じメジャーバージョン内のアップデートは無料 [[S2](#s2)]。直接ダウンロード版は Sparkle で自動更新 [[S7](#s7)] | Mac App Store 経由 |
| アカウント | 不要 [[S2](#s2)] | 不要 |
| サブスクリプション | なし [[S1](#s1), [S2](#s2)] | なし |

## トライアルや購入のあと

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 状態 | トライアルなし。買えばずっと使える | 14 日後にロックを解除しないと、書類は開くが内容は覆われる。ファイルには一切変更が加わらず、クイックルックと無料の `marsdawn` の書き出しはそのまま使える |

## 出典

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## どちらを選ぶか

**MacMD Viewer を選ぶのは、**Markdown を読むだけで、ファイルを変更しないことが保証されていてほしい場合です。ファイルへの変更は一切保存されません [[S1](#s1)]。次の場合にも向いています。Mac が macOS 14 または 15 である（MarsDawn は macOS 26 が必要）[[S1](#s1), [S7](#s7)]。Mac App Store より、開発者の公式サイト、Homebrew、Setapp から買いたい [[S2](#s2), [S7](#s7)]。エージェントが編集したファイルを自動でビューアに開かせたい（Claude Code、Cursor、Windsurf のフックで実現） [[S6](#s6)]。ページ分けされた PDF より、1 枚の連続したページの PDF がよい [[S9](#s9)]。トライアルはありませんが、14 日間の返金があります [[S2](#s2)]。

**MarsDawn を選ぶのは、**Markdown を読んだあとにもう一度手を入れる場合です。エージェントが書いた計画、README、仕様書は、たいてい 1 か所直す、1 文を言い換える、1 節を足す必要があり、MarsDawn なら読んでいるそのウインドウで直せます。数式（KaTeX）にも対応しており、MacMD Viewer は表示しないと述べています [[S7](#s7)]。インターフェイスは 8 言語。無料の `marsdawn` コマンドラインでアプリなしに PDF を書き出せます。価格は、すべて使える 14 日間のトライアルのあと USD 4.99 です。

**どちらでもよいのは、**新しめの Mac で Markdown を読み、Mermaid の図をきちんと描画したく、Finder のクイックルックも使いたい場合です。どちらも対応しています。

**両方使うこともできます。**両者は排他的ではありません。読むだけのファイルには読み取り専用のビューア、書くファイルにはエディタ、という使い分けも問題ありません。

## よくある質問

### MacMD Viewer はファイルを編集できますか？

いいえ。読み取り専用で、本人の言葉によれば、ソースファイルへの変更は保存しません [[S1](#s1), [S9](#s9)]。お使いのテキストエディタでファイルを開くことはできますが（「ファイル」メニュー、⇧⌘E、1.7.0 から）、これはファイルをほかのアプリに渡す機能です [[S5](#s5)]。

### MacMD Viewer は Mac App Store にありますか？

自身のページに挙がっているのは公式サイト、Homebrew、Setapp で、Mac App Store への言及はありません [[S2](#s2), [S7](#s7)]。MarsDawn は Mac App Store のみです。

### MarsDawn は同じファイルを開けますか？

はい。`.md` ファイルのほか、プレーンテキストと PDF も開けます。UTF-8 のテキストはそのまま編集でき、PDF はビューアで開きます。

### macOS 14 や 15 の場合は？

MacMD Viewer は macOS 14 以降で動きます [[S1](#s1)]。MarsDawn は macOS 26 以降が必要ですが、無料の `marsdawn` コマンドラインツールなら PDF の書き出しはできます。

### なぜ片方は USD 19.99 で、もう片方は USD 4.99 なのですか？

得られるものと支払い方が違います。MacMD Viewer は一度きりの購入で、14 日間の返金があり、トライアルはありません [[S2](#s2)]。MarsDawn は無料でダウンロードでき、14 日間のトライアルのあと、一度きりのロック解除です。どちらもサブスクリプションではありません。

## 今すぐ無料で試す

MarsDawn は Mac App Store で配信中です。無料の `marsdawn` コマンドラインツールも、どんな Markdown ファイルも Mermaid 図とハイライトされたコード付きの PDF にレンダリングでき、他に何もインストールする必要はありません。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 次に

- 完全な解説：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- MarsDawn ができないこと：[一覧はこちら](/ja/limits/)。
- コマンドラインツールのすべてのオプション：[コマンドライン](/ja/cli/)。
- MarsDawn の機能をすべて 1 ページで：[機能一覧](/ja/features/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown を読んで確かめる Mac ネイティブアプリ。分割ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、解除は一度だけ USD 4.99。
- [機能一覧](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックを分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。テーマは変更できますが、カスタム CSS は使えません。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で .md ファイルを開く方法](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Mac で Mermaid をプレビューする](https://marsdawn.southern-light.dev/ja/mermaid-preview-mac/index.md): Mac で Mermaid の図を Markdown の隣に描画：リアルタイムプレビュー、クイックルック、PDF 書き出し。図に誤りがあると、エラーとその行が表示されます。
- [Markdown のクイックルック](https://marsdawn.southern-light.dev/ja/quicklook/index.md): MarsDawn のクイックルックなら、Finder でスペースキーを押すだけで Markdown を描画して表示します。Mermaid 図、KaTeX 数式、ハイライトされたコードにも対応。トライアル終了後も使えます。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MarsDawn と比較：VS Code プレビュー、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
