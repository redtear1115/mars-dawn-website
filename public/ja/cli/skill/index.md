# 書いたものをエージェントに見せてもらい、PDF も作ってもらう。

このスキルは1つの Markdown ファイルです。コーディングエージェントに、自分が書いた文書を MarsDawn で開いてあなたに確認してもらう方法と、`marsdawn` のインストール方法、動作確認の方法、文書を PDF に書き出す方法、結果の読み方を教えます。

## Claude Code にインストールする

```
mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md
```

Claude Code は、PDF が必要なタスクのとき、またはあなたが読む Markdown 文書を書いたり修正したりしたときに、これを自動的に読み込みます。`/marsdawn` として自分で実行することもできます。[短いファイル1つ](/cli/skill/SKILL.md)なので、インストールする前に読んでみてください。

他のエージェントでも同じファイルを使えます。ただの Markdown で、説明とコマンドが書いてあるだけなので、あなたのエージェントにこの URL を指定するか、そのまま貼り付けてください。このファイルは英語です。

## 教えること

- `marsdawn` がなければ Homebrew でインストールし、バージョンを決め打ちせず `marsdawn --version` で確認する。
- `marsdawn export … --json` で書き出し、結果を読み取る：PDF の書き出し先、ページ数、レンダリングされなかった Mermaid 図の有無。
- 終了コードで失敗の種類を見分ける：ファイルが見つからない、PDF がすでにある、書き出しに失敗した、オプションが不正、など。
- `marsdawn open file.md:line` で自分が書いた文書を開き、最初の変更箇所に移動する。開くのは1回だけ：その後の編集は、開いているウインドウに自動的に反映される。
- MarsDawn アプリがインストールされていなければ、一度だけそう伝えて作業を続け、再試行はしない。PDF を作るために `open` を使うことは絶対にない。
- `--folder`（marsdawn 0.5.1 以降）を使ったときは、フォルダを「表示された」ではなく「表示を依頼した」と報告する：判断するのはアプリで、結果は返ってこない。

## しないこと

- 何かを実行する権限を自分自身に与えることはありません。あなたのエージェントは、他のコマンドと同じように、`marsdawn` をインストールしたり実行したりする前に、あなたに確認します。
- あなたの文書をどこかに送信することはありません。`marsdawn` はあなたの Mac 上でレンダリングし、`--allow-remote-images` を指定しない限りウェブからの画像を除外します。

すべての仕様、すべてのフィールドとコードは[AI エージェント向け marsdawn](/ja/cli/agents/)にあります。

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
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [English](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你檢閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你检阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
