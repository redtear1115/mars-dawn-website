# MacMD Viewer と MarsDawn。

どちらも、レンダリングされた Markdown を読むための Mac アプリです。MacMD Viewer は `.md` ファイルを開いて完成したページを表示しますが、編集はできません。MarsDawn は同じようなプレビューの隣にエディタを置き、同じウインドウで書きながら読めます。以下、機能ごとに両者の違いを見ていきます。

## 読むだけでよく、編集が不要なら

他の人が書いた Markdown を読むだけが仕事で、ソースに触れる必要が一切ないなら、MacMD Viewer は妥当な選択です。まさにそのために作られていて、今すぐ使え、より古い macOS でも動きます。読むことが仕事の全部ではなくなった時点で、MarsDawn の価値が出てきます。エージェントの書いた Markdown は、たいてい次の修正のためにまた戻ってくるからです。

## それぞれができること

- **編集：**MacMD Viewer は設計上、読み取り専用です。MarsDawn はソースを編集しながら隣でレンダリングするので、入力すると変更がその場に表示されます。
- **プレビューテーマ：**MacMD Viewer は12種類の文書テーマを備えています。MarsDawn は Dawn、Classic、Modern、Vivid の4種類で、それぞれライトとダークがあります。
- **図と数式：**両者とも Mermaid 図を描画し、コードをハイライトします。MarsDawn は KaTeX の数式もレンダリングします。MacMD Viewer 自身の紹介ページには数式のレンダリングについての記載がありません。
- **Finder 連携：**両者とも Finder のクイックルック拡張を追加するので、`.md` ファイルを選んで空白キーを押せばレンダリングされたページが表示されます。
- **PDF と印刷：**両者ともレンダリングされたページを PDF として書き出す、または印刷できます。
- **システム要件：**MacMD Viewer は macOS 14（Sonoma）以降が必要です。MarsDawn は macOS 26（Tahoe）以降が必要です。
- **言語：**MarsDawn のインターフェースは英語と繁体字中国語に対応しています。MacMD Viewer 自身の資料にはインターフェース言語の記載がないため、このページでは比較していません。

## 価格と購入方法

- **購入場所：**MacMD Viewer は自社サイトから直接ダウンロードでき、Homebrew と Setapp でも入手できますが、Mac App Store にはありません。MarsDawn は Mac App Store のみです。
- **価格：**MacMD Viewer は Mac 1台につき USD 19.99 の買い切り（3台パックやボリュームパックはより高額）。MarsDawn は無料でダウンロードでき、USD 4.99 の一度だけの解除です。
- **まず試す：**MacMD Viewer に無料お試しはなく、直接購入には代わりに14日間の返金保証が付きます。MarsDawn は支払う前に14日間の試用期間があります。
- **返金とアップデート：**MacMD Viewer の返金とアップデートは自社サイトを通じて行われます。MarsDawn の購入は Apple を通すので、返金とアップデートも Apple の標準的な仕組みに従います。
- **アカウント：**どちらのアプリも、使うのにアカウントは必要ありません。

## 今日から無料で試す

MarsDawn は Mac App Store に近日公開予定で、まだ販売開始していません。それまでの間、無料の `marsdawn` コマンドラインツールが、今すぐどんな Markdown ファイルでも PDF にレンダリングできます。Mermaid 図もハイライトされたコードも含み、他に何もインストールする必要はありません。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 次に

- 完全な手順：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- MarsDawn ができないこと：[その一覧](/ja/limits/)。
- コマンドラインツールのすべてのオプション：[コマンドライン](/ja/cli/)。
- VS Code やブラウザ、Claude Desktop で Markdown を読む場合との比較：[比較はこちら](/ja/vs/markdown-preview-tools/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): リアルタイムプレビュー、Mermaid 図、PDF 書き出しを備えたネイティブの Mac 向け Markdown エディタ。AI エージェントが書いた文章を読むために作られました。Mac App Store に近日公開予定。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。あなたの Markdown 文書は、選んだファイルとフォルダの中で、あなたの Mac に留まります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14 日間すべての機能を試したあとは、USD 4.99 を一度だけ支払えば使い続けられます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac 上で Markdown を PDF に書き出す、または印刷する。Mermaid 図とハイライトされたコードも含まれます。改ページは短いコードブロックや表を分断しません。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリとしての Markdown エディタ：ネイティブのウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウント不要。内蔵テーマは4種類。購入前に知っておきたいこと。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは、整形用の記号が入ったプレーンテキストです。Mac 上でレンダリングされた見た目を読む方法：今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store に近日公開予定の MarsDawn アプリで読む方法。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールし、コマンドを一つ実行するだけ：表、数式、Mermaid、コードに対応。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): Mac 向けの無料コマンドラインツール marsdawn：シェルやスクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストールできます。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): Markdown を PDF に変換するために marsdawn を呼び出す AI エージェントやスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、動作要件。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルで、marsdawn をインストールし、動作を確認し、Markdown を PDF に書き出し、JSON 結果を読み取れるようにします。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを使わないレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく精簡な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
