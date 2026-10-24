# Mac向けMarkdownビューアのおすすめ8選（2026年）

どのMarkdownビューアがよいかは、何を読むかで決まります。自分で書くメモなら、オールインワンのノートアプリで十分です。図や数式の入った長い文書や、AIエージェントが何度も書き換えるファイルなら、自動再読み込み、Mermaid、PDFの扱いを確かめてください。以下はアルファベット順で、それぞれ向いている人、正直な欠点、価格を載せています。

## MacDown 3000

元のMacDownは開発が止まっています。MacDown 3000はコミュニティによる後継版で、無料のオープンソース（MIT）、ネイティブで、Mermaid、MathJax、PDF書き出し、自動再読み込み、クイックルックに対応しています。

- 向いている人：無料のネイティブな左右分割が欲しい人。
- 欠点：コマンドラインから指定行で開く方法は記載されていません。
- 価格：無料。

## Marked

Marked 3は、ほかのアプリで書いたMarkdownを見るためのプレビューアです。ファイルが変わるたびに再読み込みし、MathJaxとKaTeXに対応し、ページ番号付きのPDFを印刷できます。Marked 2も引き続き販売されています。

- 向いている人：自分のエディタを使い続け、きれいなプレビューと印刷が欲しい書き手。
- 欠点：クイックルックは別アプリのMarked QL（USD 9.99）です。
- 価格：Marked 3は無料ダウンロード、その後は月額USD 2.99、年額USD 29.99、または買い切りUSD 69.99。Marked 2は公式サイトでUSD 14.99、Mac App StoreでUSD 13.99。

## MarkEdit

軽くて無料のネイティブアプリ（Webビュー内でCodeMirrorを使用）で、クイックルックに対応しています。

- 向いている人：Macらしく速いプレーンテキストのツールが欲しい人。
- 欠点：Mermaidと数式は公式の拡張機能が必要で、PDFにはPandocが必要です。
- 価格：無料。

## MarsDawn

ソースとライブプレビューを左右に並べるネイティブMacアプリで、MermaidとKaTeXを内蔵しています。エージェントがファイルを保存すると、開いているウインドウはその変更を取り消せる1回の「ディスクから更新」として取り込みます。`marsdawn open notes.md:120`で指定行を開け、エージェント向けのスキルとMCPサーバもあります。クイックルックは試用中かどうかに関係なく使えます。「AI 用にコピー」と「参照をコピー」でテキストをエージェントに渡せます。自分で選ばない限り、データがMacの外に出ることはありません。

- 向いている人：AIエージェントが書いたMarkdownをレビューする人。
- 欠点：書き出したPDFにページ番号は付きません。
- 価格：無料ダウンロードで14日間試用でき、その後はUSD 4.99の買い切り。アカウント不要。Mac App Storeのみ。

## Obsidian

リンクし合うMarkdownファイルのVaultを中心にしたノートアプリで、Mermaid、MathJax、PDF書き出し、自動再読み込みに対応しています。

- 向いている人：自分のメモで知識ベースを作る人。
- 欠点：Electronアプリで、ファイルはVaultの中にあるときに最も使いやすくなります。
- 価格：無料。SyncとPublishは有料。

## QLMarkdown

クイックルックの拡張機能です。Finderで.mdファイルを選んでスペースキーを押します。MermaidとMathJaxはオプションです。

- 向いている人：Finderでファイルをさっと見たいだけの人。
- 欠点：読んだり編集したりするアプリではなく、PDF書き出しの記載もありません。
- 価格：無料（GPL-3.0）。

## Typora

プレビューがそのまま文書になる書き味のツールで、Mermaid、MathJax、ヘッダやフッタにページ番号を入れられるPDF書き出しに対応しています。

- 向いている人：仕上がりに近い画面で書きたい人。
- 欠点：ソースとプレビューを左右に並べる表示はありません。
- 価格：USD 14.99の買い切りで、3台まで。

## VS Codeのプレビュー

標準のMarkdownプレビューで、1.121からMermaidを内蔵し、KaTeXに対応しています。`code -g file:line`で指定行を開けます。

- 向いている人：普段からVS Codeで作業している開発者。
- 欠点：Electronアプリで、PDF書き出しは標準ではありません。
- 価格：無料。

## 比較表

| アプリ | 価格 | Mermaid | 数式 | PDF | 自動再読み込み | CLIで指定行 | クイックルック | 構成 |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | 無料 | あり | MathJax | あり | あり | 記載なし | あり | ネイティブ |
| Marked 3 | 月額USD 2.99から | あり | MathJax、KaTeX | あり、ページ番号付き | あり | 記載なし | Marked QL、USD 9.99 | ネイティブ |
| MarkEdit | 無料 | 拡張機能 | KaTeX（拡張機能） | Pandoc | 記載なし | 記載なし | あり | ネイティブ（Webビュー） |
| MarsDawn | USD 4.99買い切り | あり | KaTeX | あり、ページ番号なし | あり、取り消し可 | あり | あり | ネイティブ |
| Obsidian | 無料 | あり | MathJax | あり | あり | 記載なし | 記載なし | Electron |
| QLMarkdown | 無料 | オプション | MathJax（オプション） | 記載なし | 該当なし | 該当なし | それ自体 | ネイティブ |
| Typora | USD 14.99買い切り | あり | MathJax | あり、ページ番号付き | 記載なし | 記載なし | 記載なし | ネイティブ |
| VS Code | 無料 | あり（1.121以降） | KaTeX | なし | 記載なし | あり | 記載なし | Electron |

## MarsDawnが向かない人

- PDFにページ番号が必要な人。TyporaとMarked 3は付けられますが、MarsDawnは付けられません。
- リンクし合う自分のメモの知識ベースを育てている人。Obsidianはそのために作られています。
- VS Codeから離れない人。標準のプレビューは無料で、VS CodeはAgentsウインドウに実験的なMarkdown表示を追加しつつあります。
- Finderでプレビューできれば十分な人。QLMarkdownは無料です。

## よくある質問

### Mermaidに対応した無料のMac向けMarkdownビューアは？

MacDown 3000、Obsidian、VS Code（1.121以降）が内蔵しています。QLMarkdownはオプションで、MarkEditは拡張機能で対応します。

### ページ番号付きのPDFを書き出せるのは？

TyporaとMarked 3です。MarsDawnのPDFにページ番号は付きません。

### コマンドラインから指定行でファイルを開けるのは？

MarsDawn（`marsdawn open notes.md:120`）とVS Code（`code -g file:line`）です。ほかは記載がありません。

### ElectronではなくネイティブのMacアプリは？

ObsidianとVS Code以外のすべてです。MarkEditはネイティブで、編集部分にWebビューを使っています。

[今すぐダウンロードして試す](https://apps.apple.com/app/id6812925073)

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
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
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
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
