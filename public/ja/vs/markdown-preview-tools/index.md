# ほかの場所で Markdown を見る、対 MarsDawn。

すでに VS Code やブラウザ、Claude Desktop を開いているなら、それらで Markdown ファイルをちらっと見るのは妥当な選択です。それぞれが実際に何をレンダリングし、そこにたどり着くのに何が必要か、MarsDawn で同じファイルを開いた場合と比較してみます。

## VS Code の内蔵プレビュー

VS Code で `⌘⇧V` を押すと、内蔵のプレビューパネルで Markdown ファイルがレンダリングされます。無料で、インストールするものもありません。VS Code 1.121（2026年5月）以降、このプレビューは Mermaid 図もネイティブに描画します。Microsoft が Mermaid 拡張機能を VS Code 本体に組み込んだためで、以前は別の拡張機能が必要でしたが、今は不要です。できないこと：これはエディタの中のプレビューパネルであって、読むために作られたエディタではありません。パネルの隣にはファイルツリー、ターミナル、VS Code が表示できるその他のパネルが並び、VS Code 自体も Electron アプリで、Mac ではおよそ150〜250MB のダウンロードになります。

## ローカルファイル用のブラウザ拡張機能

ローカルの `.md` ファイルを読むために主流と呼べるブラウザ拡張機能はありません。Local Markdown Viewer、Markdown Viewer、MarkView などがだいたい同じことをしていて、どれもデフォルトではありません。どれも、何かを開く前に同じ手順が必要です。ブラウザはデフォルトで拡張機能に `file://` のページを読ませないので、その拡張機能の「ファイルの URL へのアクセスを許可」を有効にする必要があります。これは拡張機能ごとに一度だけ与える権限ですが、与えたこと自体や、なぜ与えたのかを忘れやすいものです。有効にすると、ファイルはブラウザのタブに表示されます。つまり、1つのファイルを見るために、ブラウザを丸ごと動かすことになります。

## Claude Desktop のファイルプレビュー

Claude Desktop は、すでに Project や会話の中にあるファイルについては、Markdown をきちんとレンダリングします。frontmatter は表として、見出し、太字、インラインコードもすべてスタイルが付き、生のソースではありません。それが作られていないのは、ディスク上の任意のファイルを閲覧することです。会話にすでにあるものをプレビューするのであって、フォルダの中のメモをプレビューするわけではありません。そのパネルにあるアクションは「ダウンロード」で `.md` ファイルを取り戻すものであり、PDF に書き出すものではなく、オフラインやローカルでの編集もありません。プレビューは会話の一部であり、開いたまま手を加え続ける文書ではありません。

## 三つとも、ブラウザエンジンの中で動いている

VS Code と Claude Desktop はどちらも Electron アプリです。Chromium と Node.js のランタイムが同梱されていて、ネイティブの Mac アプリではありません。ブラウザ拡張機能という道は、実際のブラウザの中で動きます。どちらにしても、1つの Markdown ファイルを見るために、丸ごとのブラウザエンジンが裏で動いていることになります。MarsDawn はネイティブの AppKit アプリです。ダウンロードは軽く、どんなローカルファイルも直接開けて、インストールする拡張機能も、覚えておくべき権限フラグもありません。

## 次に

- MarsDawn もできないこと：[その一覧](/ja/limits/)。
- 今日、無料でどんな Markdown ファイルも PDF にする：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- Mac ネイティブのビューアとの比較：[MacMD Viewer と MarsDawn](/ja/vs/macmd-viewer/)。

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
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は Markdown を読み取り専用で表示、USD 19.99。MarsDawn は編集とプレビューを並べて表示、Mac App Store で無料お試し後に USD 4.99 を一度だけ。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): Mac 向けの無料コマンドラインツール marsdawn：シェルやスクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストールできます。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): Markdown を PDF に変換するために marsdawn を呼び出す AI エージェントやスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、動作要件。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルで、marsdawn をインストールし、動作を確認し、Markdown を PDF に書き出し、JSON 結果を読み取れるようにします。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを使わないレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく精簡な JSON 結果を返すので、呼び出し自体も安上がりです。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
