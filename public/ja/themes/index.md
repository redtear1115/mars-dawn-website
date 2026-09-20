# 8つの見た目、1つの書き出し。

MarsDawn には Dawn、Classic、Modern、Vivid の4種類のプレビューテーマが付属し、それぞれライトとダークがあります。文書を読むための8通りの組み合わせです。PDF に書き出す、または印刷すると、そのとき読んでいたものと同じ見た目でページが出てきます。

**4つのテーマ × ライトとダーク＝文書を読む8つの方法があり、書き出しはどれを選んでいても対応します。**もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーは計画中で、まだ作られていません。

## 4種類のテーマ

- **Dawn**、デフォルト：このサイトと同じ、温かみのある紙の質感と Mars Rust のアクセントカラー。
- **Classic**（典雅）：より素朴で、紙の文書らしい配色。
- **Modern**（流行）：より涼しげで、現代的な配色。
- **Vivid**（活潑）：より明るく、コントラストの高い配色。

それぞれ独自のライトとダークの配色を持つので、Mac の外観を切り替えると、インターフェースの色だけでなくテーマの配色自体も切り替わります。

## PDF 書き出しと印刷は同じテーマを使う

PDF に書き出す、または印刷すると、テーマのライトカラーが使われます。Mermaid 図はそこに描き込まれ、コードブロックは構文のハイライトを保ち、改ページは見出しをそのセクションから切り離したり、表や図を途中で切ったりしないよう配慮されます。無料の[marsdawn コマンドラインツール](/ja/cli/)も同じ書き出しエンジンを使うので、スクリプトやエージェントも `--theme` で、4種類のどのテーマでも同一の PDF を作れます。

## 計画中：もっと多くのテーマと、ギャラリー

今後登場する予定でまだ実装されていないもの：輸入可能なプレビューテーマの追加と、このサイト上で誰もが自分のテーマを投稿できるギャラリーです。`/themes/v1/` はすでにそのために予約されています。それが公開されるまで、MarsDawn にあるのはこの4つの内蔵テーマだけで、他のテーマをインストールすることはできません。

## 次に

- コマンドラインからの、完全な PDF 書き出しの手順：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- MarsDawn がまだできないこと：[その一覧](/ja/limits/)。
- Markdown を使わない人に、書き出した PDF を渡す：[PDF を共有する](/ja/sharing-exported-pdfs/)。

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
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/themes/index.md): Four preview themes, each with a light and dark palette, and one PDF/print export that matches whichever you're in. More importable themes, and a gallery to share your own, are planned.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
