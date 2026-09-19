ビルダーのためのフロンティアツール

# 地図を手に。夜明けを読む。

エージェント開発の舵を取る人のための Markdown。

ページには操作できる MarsDawn のウインドウがあり、アプリ内蔵のようこそガイドの一部を表示しています。4 つのプレビューテーマ（夜明け、クラシック、モダン、ビビッド）と 3 つのレイアウト（ソース、分割、プレビュー）から選べます。

## エージェントが書いた Markdown を読む。

1. **エージェントが書く。**あなたのコーディングエージェントやライティングアシスタントが Markdown の下書きを作ります。README、仕様書、メモなど。
2. **MarsDawn で確認する。**ファイルを開き、Mermaid 図やハイライトされたコードとともにレンダリングされたページを、ソースの隣で読みます。
3. **エージェントが修正する。**変更を依頼します。修正されたファイルを開き、同じように読みます。

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

- [Mac アプリ](/ja/native/)：ネイティブのウインドウとタブ、自動保存、クイックルック。
- [あなたの文章は Mac に残ります](/ja/yours/)：アカウント不要、同期なし、クラウドなし。
- [無料で試して、一度だけ購入](/ja/pay-once/)：14日間無料、その後は一度だけ USD 4.99。サブスクリプションはありません。

購入前に知っておくこと。 [MarsDawn ができないこと](/ja/limits/)

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

- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したり印刷したりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で配信中の MarsDawn アプリで読む方法です。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [English](https://marsdawn.southern-light.dev/index.md): Markdown for humans who steer agentic work: a native Mac editor with live preview, Mermaid diagrams and PDF export. On the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。已在 Mac App Store 上架。
