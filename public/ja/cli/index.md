# コマンドライン

無料の `marsdawn` コマンドラインツール：シェルや LLM エージェントから Markdown を PDF に書き出せます。MarsDawn アプリがインストールされていれば、そのアプリでファイルを開くこともできます。

**marsdawn は無料で、Mac App Store とは別に配布されています。**Homebrew でインストールすると、Apple シリコンの Mac では、すぐに実行できる状態でインストールされます。`export` は単独で動作し、`open` には MarsDawn アプリが必要です。

AI エージェントやスクリプトから marsdawn を呼び出しますか？JSON 出力とそのスキーマ、すべての終了コードについては[AI エージェント向け marsdawn](/ja/cli/agents/)をご覧ください。

## インストール

[Homebrew](https://brew.sh) を使う場合：

```
brew tap redtear1115/tap && brew install marsdawn
```

コーディングエージェントを使っていますか？[marsdawn スキルを追加](/ja/cli/skill/)してください。自分が書いたものを MarsDawn で開いてあなたに確認してもらう方法と、PDF の書き出しを教える、1つのファイルです。

Apple シリコンの Mac では、Homebrew がビルド済みのコピーを数秒でインストールし、他に何もインストールする必要はありません。Intel Mac では代わりにソースから marsdawn をビルドするため数分かかり、Xcode 26 以降（Swift 6.2）が必要です。このツールは macOS 15 以降で動作します。

または、Swift Package Manager で[ソース](https://github.com/redtear1115/mars-dawn-kit)からビルドします。

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

インストールされているバージョンは `marsdawn --version` で確認できます。

## コマンド

### marsdawn open

1つ以上の Markdown ファイルを MarsDawn アプリで開いて確認できます。アプリのインストールが必要です。インストールされていない場合、`marsdawn open` はコード 3 で終了し、MarsDawn がインストールされていないことを知らせます。`export` にはアプリは不要です。

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .
```

- `path:line`：MarsDawn にその行に移動するよう指定します。その後にコロンが続く場合、たとえば `notes.md:120:8` の列部分は無視されます。引数全体と一致するファイル名が存在する場合、その引数はそのファイルとして扱われます。
- `--line <n>`：単一ファイルに対して同じ指定ができ、それ自体がコロンと数字で終わるパスに対して行を指定する方法でもあります。ファイルは1つだけ指定できます。
- 行番号は 1 から 999999999 までです。
- フォルダを引数にすると、書類としてではなくウインドウのサイドバーに開きます：`marsdawn open .` で現在のフォルダを表示します。`--folder <path>` はファイルと一緒に同じことをします。ウインドウのサイドバーに表示できるフォルダは1つなので、2つ指定すると使用方法のエラーになります。
- `--background`：MarsDawn を前面に出さずに開きます。
- MarsDawn 1.0 はファイルを開きますが、まだその行にジャンプしません。
- `--json`：テキストではなく JSON の結果を出力します。

行の指定は marsdawn 0.3.0 で、フォルダと `--background` は 0.5.1 で追加されました。

### marsdawn export

Markdown ファイルを、MarsDawn 自身の PDF 書き出しと同じ書き出しエンジンで、ページ分割された PDF にレンダリングします。MarsDawn アプリは不要です。相対パスの画像は、入力ファイルのあるフォルダを基準に解決されます。

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`：PDF の書き出し先。デフォルトは入力パスの拡張子を `.pdf` にしたものです。
- `--theme <dawn|classic|modern|vivid>`：プレビューテーマのライトパレット。デフォルトは `$MARSDAWN_THEME`、それもなければ `dawn` です。
- `--paper <a4|letter>`：用紙サイズ。デフォルトは `a4` です。
- `--allow-remote-images`：レンダリング時にウェブから画像を読み込みます。デフォルトはオフです。
- `--force`：出力ファイルがすでに存在する場合に置き換えます。
- `--json`：テキストではなく JSON の結果を出力します。

## $MARSDAWN_THEME 環境変数

`--theme` が指定されない場合、`export` は `$MARSDAWN_THEME` 環境変数を読み取ります。値は `dawn`、`classic`、`modern`、`vivid` のいずれかである必要があり、それ以外は `dawn` にフォールバックします。CLI はアプリ自身のテーマ設定を読み取りません。他のアプリのコンテナを読み取ると、macOS のプライバシープロンプトが表示されることがあるためです。

## ファイルの上書き

`export` は、`--force` を指定しない限り、既存の出力ファイルを置き換えません。

## 終了コード

- `0`：成功。
- `2`：入力が見つからない。
- `3`：MarsDawn がインストールされていない（`open` のみ）。
- `4`：出力先がすでに存在する（`--force` を指定してください）。
- `5`：書き出しに失敗。
- `64`：使用方法のエラー。範囲外の行、複数ファイルやフォルダに対する `--line` の指定、複数のフォルダの指定などを含みます。

## --json 出力

成功時、`marsdawn open --json` は `ok`、`opened`（各ファイルの `path`、行が指定されていれば `line` も含む）、`app`（アプリのパス）、フォルダが指定されていれば `folder` を出力します。`marsdawn export --json` は `ok`、`output`、`pages`、`theme`、`paper`、`diagramErrors` を出力します。失敗時はどちらも `ok`、`error`、`message` を出力します。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向け Markdown エディタ。AI エージェントが書いた文章を読むために作られました。Mac App Store で近日公開予定です。
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
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
