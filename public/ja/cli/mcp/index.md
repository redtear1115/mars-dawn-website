# marsdawn を呼び出す三つの方法。

MarsDawn には自前の AI モデルがありません。Markdown を書くためではなく、レビューするために作られているので、どのエージェントやモデルがそのファイルを作ったかは関係ありません。エージェントやスクリプトが `marsdawn` を呼び出す方法は三つあり、どれも最終的に同じ `export` を実行します。

**使っているツールが対応しているものを選んでください：無料の `marsdawn` CLI、プレーンな Markdown の skill ファイル、または [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) という MCP サーバーです。**三つとも同じ `marsdawn export` を呼び出し、同じ JSON 結果を返します。

## CLI

`marsdawn export notes.md --json` は、シェルコマンドを実行できるエージェントやスクリプトならどれからでも呼び出せます。構造上、モデルに依存しません。返されるすべてのフィールドは[AI エージェント向け marsdawn](/ja/cli/agents/)に文書化されており、そこが JSON スキーマの正典で、以下の二つの経路もそこを参照します。

## skill ファイル

シェルを直接呼び出すのではなく、プレーンな Markdown の指示を読むエージェント向け——現時点では Claude Code——には、[marsdawn skill](/ja/cli/skill/) という1ファイルが、marsdawn のインストール、`export` の実行、結果の読み取りを教えます。プレーンな Markdown なので、指示ファイルを読み込む他のエージェントも同じファイルを使えます。

## MCP サーバー

[marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) は、別の、公開された、Apache-2.0 ライセンスの独立した repository です。`export_markdown_to_pdf` という1つのツールを持つ MCP サーバーで、`marsdawn export --json` をラップしています。MCP クライアントをそれに向ければ、ツール呼び出しは CLI と同じ JSON を返します。

- **入手方法：**[GitHub のリリース](https://github.com/redtear1115/marsdawn-mcp/releases)に添付された MCP Bundle（`marsdawn.mcpb`）として、またはソースから stdio でサーバーを実行することで入手できます。
- **Registry：**まだ MCP Registry には登録されていません（現在のリリース：0.1.0）。registry 経由で見つかる前に、repository で現在の状況を確認してください。
- **ホスティング：**自分でホストするしかありません。marsdawn-mcp のホスティングサービスは存在せず、サーバーは marsdawn 自身の隣、あなた自身のマシン上で動きます。
- **動作要件：**macOS、marsdawn 0.5.0 以降、そしてサーバーを実行するための Node.js 20 以降。

## 同じ export、三つの入り口

どの入り口から呼び出しても、内部の動作は変わりません。同じ書き出しエンジン、同じテーマと紙のサイズ、Mermaid 図の描画に失敗したときの同じ `diagramErrors`。このページではその契約内容を繰り返しません。[AI エージェント向け marsdawn](/ja/cli/agents/)に完全な内容があります。

## 次に

- 完全な JSON スキーマとすべての終了コード：[AI エージェント向け marsdawn](/ja/cli/agents/)。
- Claude Code などのエージェント向けの1ファイルの skill：[marsdawn skill](/ja/cli/skill/)。
- 精簡な JSON 結果が、なぜエージェント自身の context にとって重要なのか：[トークンを節約するレビュー方法](/ja/token-efficient-review/)。

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
- [トークンを使わないレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく精簡な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
