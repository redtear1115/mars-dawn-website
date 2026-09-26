# marsdawn を呼び出す三つの方法。

MarsDawn には自前の AI モデルがありません。Markdown を書くためではなく、レビューするために作られているので、どのエージェントやモデルがそのファイルを作ったかは関係ありません。エージェントやスクリプトが `marsdawn` を呼び出す方法は三つあり、どれも最終的に同じ `export` を実行します。

**使っているツールが対応しているものを選んでください：無料の `marsdawn` CLI、プレーンな Markdown の skill ファイル、または [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) という MCP サーバーです。**三つとも同じ `marsdawn export` を呼び出し、同じ JSON 結果を返します。

## どれを使うか

| エージェントが | 使うもの | 必要なもの |
|---|---|---|
| シェルコマンドを実行できる | [CLI](/ja/cli/agents/) | macOS 15 以降 |
| Claude Code のように指示ファイルを読み込む | [スキルファイル](/ja/cli/skill/) | CLI（スキルがインストールします） |
| MCP でツールを呼び出す | [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) | marsdawn-mcp 0.2.1 以降、marsdawn 0.5.0 以降、Node.js 20 以降 |

## CLI

`marsdawn export notes.md --json` は、シェルコマンドを実行できるエージェントやスクリプトならどれからでも呼び出せます。構造上、モデルに依存しません。返されるすべてのフィールドは[AI エージェント向け marsdawn](/ja/cli/agents/)に文書化されており、そこが JSON スキーマの正典で、以下の二つの経路もそこを参照します。

## skill ファイル

シェルを直接呼び出すのではなく、プレーンな Markdown の指示を読むエージェント向け——現時点では Claude Code——には、[marsdawn skill](/ja/cli/skill/) という1ファイルが、marsdawn のインストール、`export` の実行、結果の読み取りを教えます。プレーンな Markdown なので、指示ファイルを読み込む他のエージェントも同じファイルを使えます。

## MCP サーバー

[marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) は、別の、公開された、Apache-2.0 ライセンスの独立した repository です。`export_markdown_to_pdf` と `open_in_marsdawn` という2つのツールを持つ MCP サーバーで、それぞれ `marsdawn export --json` と `marsdawn open --json` をラップしています。MCP クライアントをそれに向ければ、ツール呼び出しは CLI と同じ JSON を返します。

- **入手方法：**[GitHub のリリース](https://github.com/redtear1115/marsdawn-mcp/releases)に添付された MCP Bundle（`marsdawn.mcpb`）として、またはソースから stdio でサーバーを実行することで入手できます。
- **Registry：**まだ MCP Registry には登録されていません（現在のリリース：0.2.1）。registry 経由で見つかる前に、repository で現在の状況を確認してください。
- **ホスティング：**自分でホストするしかありません。marsdawn-mcp のホスティングサービスは存在せず、サーバーは marsdawn 自身の隣、あなた自身のマシン上で動きます。
- **動作要件：**macOS、marsdawn 0.5.0 以降、そしてサーバーを実行するための Node.js 20 以降。

## 許可したフォルダの中でしか動きません

両方のツールとも、許可したフォルダの中でしか読み書きしません：拡張機能の「Allowed folders」設定（デフォルトは空です）、またはお使いの MCP クライアントが提供する roots のどちらかです。どちらも設定されていない場合、すべての呼び出しは拒否され、拒否メッセージに設定方法が書かれています。パスはすべて絶対パスである必要があり、`export_markdown_to_pdf` が書き出すのは `.pdf` ファイルだけで、シンボリックリンク経由で書き込むことはありません。

**セキュリティ：**[0.2.1](https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1) に更新してください——0.1.0 と 0.2.0 では、呼び出しがあなたのアカウントが書き込めるどのパスにも PDF を書き込めてしまう問題があり、[GHSA-fqgj-hcxc-34qc](https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc) で修正されました。

## 同じ export、三つの入り口

どの入り口から呼び出しても、内部の動作は変わりません。同じ書き出しエンジン、同じテーマと紙のサイズ、Mermaid 図の描画に失敗したときの同じ `diagramErrors`。このページではその契約内容を繰り返しません。[AI エージェント向け marsdawn](/ja/cli/agents/)に完全な内容があります。

## 次に

- 完全な JSON スキーマとすべての終了コード：[AI エージェント向け marsdawn](/ja/cli/agents/)。
- Claude Code などのエージェント向けの1ファイルの skill：[marsdawn skill](/ja/cli/skill/)。
- 簡潔な JSON 結果が、なぜエージェント自身の context にとって重要なのか：[トークンを抑えたレビュー](/ja/token-efficient-review/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で配信中です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
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
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・プリント書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
