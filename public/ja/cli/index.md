# コマンドライン

無料の `marsdawn` コマンドラインツール：シェルや LLM エージェントから Markdown を PDF に書き出し、MarsDawn アプリがインストールされていればファイルをそこで開くこともできます。

**marsdawn は無料で、Mac App Store とは別に配布されています。**Homebrew でインストールしてください。Apple シリコンの Mac ではすぐに使える状態で届きます。`export` は単独で動作し、`open` には MarsDawn アプリが必要です。

AI エージェントやスクリプトから marsdawn を呼び出しますか？JSON 出力、スキーマ、すべての終了コードは[AI エージェント向け marsdawn](/ja/cli/agents/)を、エージェントが代わりに MCP でツールを呼び出す場合は[MCP サーバー](/ja/cli/mcp/)をご覧ください。

## インストール

[Homebrew](https://brew.sh) を使う場合：

```
brew tap redtear1115/tap && brew install marsdawn
```

Apple シリコンの Mac では、Homebrew が数秒でビルド済みのコピーをインストールし、他に何もインストールする必要はありません。Intel Mac では代わりにソースからビルドするため数分かかり、Xcode 26 以降（Swift 6.2）が必要です。このツールは macOS 15 以降で動作します。

または、[ソース](https://github.com/redtear1115/mars-dawn-kit)から Swift Package Manager でビルドすることもできます：

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

インストールされたバージョンは `marsdawn --version` で確認できます。

## コマンド

### marsdawn open

1つ以上の Markdown ファイルを MarsDawn アプリで開き、レビューできるようにします。アプリのインストールが必要です。インストールされていない場合、`marsdawn open` は代コード 3 で終了し、MarsDawn がインストールされていないと表示します。`export` にはアプリは不要です。

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
```

- `path:line`：MarsDawn にその行へ移動するよう伝えます。後ろにさらに列番号が続く場合（`notes.md:120:8` など）は無視されます。その名前そのままのファイルが存在する場合は、その引数はそのファイルとして扱われます。
- `--line <n>`：単一ファイルに対して同じことをします。ファイル名自体がコロンと数字で終わる場合の行指定にも使えます。ファイルは1つだけ指定できます。
- 行番号の範囲は 1 から 999999999 です。
- MarsDawn 1.0 はファイルを開きますが、まだその行へジャンプはしません。
- `--json`：テキストの代わりに JSON 結果を出力します。

行番号は marsdawn 0.3.0 で追加されました。

### marsdawn export

Markdown ファイルを、MarsDawn 自身の PDF 書き出しと同じエンジンでページ分割された PDF に変換します。MarsDawn アプリは不要です。相対パスの画像は、入力ファイルのフォルダを基準に解決されます。

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`：PDF の書き出し先。デフォルトは入力パスの拡張子を `.pdf` に変えたものです。
- `--theme <dawn|classic|modern|vivid>`：プレビューテーマのライトカラー。デフォルトは `$MARSDAWN_THEME`、それもなければ `dawn` です。
- `--paper <a4|letter>`：紙のサイズ。デフォルトは `a4` です。
- `--allow-remote-images`：書き出し中にウェブから画像を読み込みます。デフォルトはオフです。
- `--force`：出力先ファイルがすでに存在する場合に置き換えます。
- `--json`：テキストの代わりに JSON 結果を出力します。

## $MARSDAWN_THEME 環境変数

`--theme` が指定されない場合、`export` は `$MARSDAWN_THEME` 環境変数を読みます。値は `dawn`、`classic`、`modern`、`vivid` のいずれかである必要があり、それ以外は `dawn` にフォールバックします。この CLI はアプリ自身のテーマ設定を読みません。他のアプリのコンテナを読むと、macOS のプライバシープロンプトが表示されることがあるためです。

## ファイルの上書き

`export` は、`--force` を指定しない限り既存の出力ファイルを置き換えません。

## 終了コード

- `0`：成功。
- `2`：入力が見つかりません。
- `3`：MarsDawn がインストールされていません（`open` のみ）。
- `4`：出力先がすでに存在します（`--force` を指定してください）。
- `5`：書き出しに失敗しました。
- `64`：使い方の誤り。行番号が範囲外だったり、`--line` に複数ファイルを指定した場合などです。

## --json 出力

成功時、`marsdawn open --json` は `ok`、`opened`（各ファイルの `path`、行が指定されていれば `line` も含むリスト）、`app`（アプリのパス）を出力します。`marsdawn export --json` は `ok`、`output`、`pages`、`theme`、`paper`、`diagramErrors` を出力します。失敗時は、どちらも `ok`、`error`、`message` を出力します。

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
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): Markdown を PDF に変換するために marsdawn を呼び出す AI エージェントやスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、動作要件。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルで、marsdawn をインストールし、動作を確認し、Markdown を PDF に書き出し、JSON 結果を読み取れるようにします。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを使わないレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく精簡な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
