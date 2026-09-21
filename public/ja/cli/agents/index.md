# AI エージェント向け marsdawn

`marsdawn` コマンドラインツールを呼び出す AI エージェントとスクリプトのためのリファレンスです。このページのすべての例は、現在のソースからビルドしたツールに対して実際に実行したものです。

**Markdown ファイルを PDF に変換するには、`marsdawn export notes.md --json` を実行し、stdout から1つの JSON オブジェクトを読み取ってください。**Mermaid 図とハイライトされたコードは、MarsDawn アプリと同じ方法でレンダリングされます。`export` にアプリは不要ですが、`open` には必要です。

## できること

- `export`：MarsDawn アプリと同じ書き出しエンジンで、1つの Markdown ファイルをページ分割された PDF にレンダリングします。ウインドウは開きません。
- `open`：1つ以上の Markdown ファイルを MarsDawn アプリで開き、人が確認できるようにします。各ファイルが移動すべき行を指定することもできます。

## できないこと

- stdin から Markdown を読み込みません。ファイルパスを渡してください。
- PDF を stdout に書き出しません。PDF は常にファイルとして書き出され、stdout には結果だけが出力されます。
- `--force` を指定しない限り、既存のファイルを置き換えません。
- `--allow-remote-images` を指定しない限りウェブから画像を読み込まず、指定した場合も https のみです。
- `open` は MarsDawn アプリがインストールされていないと動作せず、コード 3 で終了します。`export` にアプリは不要です。
- MarsDawn 1.0 はまだ `open` が指定した行にジャンプしません。ファイルは先頭から開きます。
- macOS でのみ動作します。

## export

```
marsdawn export notes.md --json
```

`notes.pdf` を `notes.md` の隣に書き出します。オプション：

- `-o, --output <path>`：PDF の書き出し先。デフォルトは入力パスの拡張子を `.pdf` にしたものです。
- `--theme <dawn|classic|modern|vivid>`：テーマのライトパレット。デフォルトは `$MARSDAWN_THEME`、それもなければ `dawn` です。
- `--paper <a4|letter>`：用紙サイズ。デフォルトは `a4` です。
- `--allow-remote-images`：レンダリング時にウェブから https の画像を読み込みます。
- `--force`：出力ファイルが存在する場合に置き換えます。
- `--json`：stdout にテキストではなく1つの JSON オブジェクトを出力します。

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

成功、終了コード 0：

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`：書き出された PDF の絶対パス。
- `pages`：ページ数。
- `theme` と `paper`：実際に使われた値。
- `diagramErrors`：レンダリングに失敗した Mermaid 図につき1件のメッセージ。PDF はそれでも書き出されます。

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
```

- `path:line` は移動先の行を指定します。その後にコロンが続く場合、たとえば `notes.md:120:8` の列部分は無視されます。存在するファイル名を丸ごと表す引数は常にそのファイル名として扱われるため、`weird:12` という名前のファイルはそのまま開きます。
- `--line <n>` は単一ファイルの行を指定します。それ自体がコロンと数字で終わるパスも含みます。ファイルは1つだけ指定できます。
- 行番号は 1 から 999999999 までで、それ以外は使用方法のエラーになります。
- 行の指定は marsdawn 0.3.0 で追加されました。MarsDawn 1.0 はファイルを開きますが、まだその行にジャンプしません。

成功、終了コード 0：

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`：渡された順に、ファイルごとの1つのオブジェクト。`path` はファイルの絶対パス、`line` は行が指定されたときだけ現れます。
- `app`：それらを開いた MarsDawn アプリのパス。

marsdawn 0.2.x では `opened` はパス文字列のリストでした。両方を扱う必要がある場合は `marsdawn --version` を確認してください。

## 失敗時

`--json` を指定すると、失敗時は stdout に1つの JSON オブジェクトを出力し、対応するコードで終了します。

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`、`input_not_found`：入力が存在しない、フォルダである、または UTF-8 テキストでない。
- `3`、`app_not_installed`：MarsDawn がインストールされていない。`open` のみがこれを返します。
- `4`、`output_exists`：出力ファイルが存在する。`--force` を指定してください。
- `5`、`export_failed`：書き出し自体が失敗した。
- `64`：使用方法のエラー。未知のオプション、無効な値、範囲外の行、複数ファイルに対する `--line` の指定など。この場合は、`--json` を指定していても stderr にテキストとして出力されます。

## JSON Schema

各 `--json` 結果に対応する JSON Schema（draft 2020-12）：

- [export.v1.json](/schemas/cli/export.v1.json): export 成功時
- [open.v2.json](/schemas/cli/open.v2.json): open 成功時、marsdawn 0.3.0 以降
- [error.v1.json](/schemas/cli/error.v1.json): 失敗時、両方のコマンド共通
- [open.v1.json](/schemas/cli/open.v1.json): open 成功時、marsdawn 0.2.x（`opened` がパスのリストだった頃）

## 環境変数

- `MARSDAWN_THEME`：`export` が、`--theme` が指定されないときに使うテーマ。未知の値はエラーにならず `dawn` にフォールバックします。

## 必要環境

- このツールは macOS 15 以降で動作します。Apple シリコンでは、Homebrew がビルド済みのボトルをインストールし、他に何も必要ありません。Intel Mac やソースから自分でビルドする場合は、Swift 6.2 以降が必要で、これは Xcode 26 以降に付属しています。
- MarsDawn アプリには macOS 26 以降が必要です。

## インストール

Homebrew を使う場合。Apple シリコンでは、Xcode 不要でビルド済みのボトルを数秒でインストールします。Intel Mac では marsdawn をソースからコンパイルするため数分かかり、Xcode 26 以降が必要です。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

または、[ソース](https://github.com/redtear1115/mars-dawn-kit)からビルドします。最初のビルドでは依存関係の取得とコンパイルが行われ、これも数分かかります。

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` は `0.3.0` のようなバージョン番号を表示し、コード 0 で終了します。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で近日公開予定です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したり印刷したりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で近日公開予定の MarsDawn アプリで読む方法です。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
