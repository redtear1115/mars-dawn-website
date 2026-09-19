# プライバシーポリシー

macOS 向け Markdown エディタ、MarsDawn がどのようにあなたの情報を扱うか。

最終更新日：2026-09-19

**MarsDawn はあなたに関するデータを一切収集しません。**アカウントも、アナリティクスも、広告も、トラッキングもありません。文書と設定はあなたの Mac 上に残ります。

## あなたの Mac に残るもの

- **あなたの文書。**MarsDawn は、あなたが開いた、保存した、または選んだファイルとフォルダだけを読み書きします。App がそれらをどこかにアップロードすることはありません。
- **あなたの設定。**外観、プレビューのテーマ、ウィンドウのレイアウト、画像の設定は、あなたの Mac 上にある App 自身の環境設定に保存されます。
- **許可したフォルダへのアクセス。**フォルダ内の画像やページファイルを MarsDawn に表示させたり、メモフォルダを選んだりすると、App はそのフォルダを再び開けるように macOS のブックマークを保持します。サイドバーで開いたフォルダは、ウィンドウが開いている間だけでなく、設定で削除するまで MarsDawn から読み書き可能な状態が続きます。フォルダはいつでも MarsDawn › 設定で削除できます。

## MarsDawn がインターネットを使うとき

MarsDawn は完全にオフラインで動作します。インターネットに接続するのは**あなたが選んだときだけ**、ウェブを参照する文書に対してです。

- **Markdown 文書。**ウェブ画像はデフォルトでブロックされています。プレビューで*イメージを読み込む*をクリックするか、設定で*リモートイメージを自動的に読み込む*をオンにしたときだけ読み込まれます。Markdown 文書が参照するそれ以外のものは、ウェブから読み込まれません。
- **HTML 文書。**HTML 文書は静的な状態で開きます。コードは実行されず、ウェブから何も読み込まれません。文書に実行され得るコードが含まれる場合、その文書について*表示 › この書類を実行*を選ぶことができます。すると、その文書自身のコードは、あなたが停止するか、文書が再読み込みされるか、ウィンドウを閉じるまで実行され続けます。この選択が記憶されることはなく、設定項目でもありません。実行中、文書はネットワーク経由でデータを送信でき、自身のフォルダとその中のフォルダにある画像、スタイルシート、フォント、メディアを読み取れます。ウェブからダウンロードされたコードが実行されることはありません。

MarsDawn は https 経由でのみウェブコンテンツを読み込みます。http のみのアドレスは、どの設定でも読み込まれることはなく、MarsDawn がそれを https に書き換えることもありません。Markdown 文書では、プレビューにその代わりのプレースホルダーが表示されます。

ウェブコンテンツを読み込むとき、あなたの Mac はそれを配信するサーバーへ直接リクエストを送ります。他のウェブリクエストと同様に、これによってそれらのサーバーはあなたの IP アドレスとリクエストされた内容を知ることができます。MarsDawn の開発者はこれらの情報を一切受け取りません。

プレビュー内でクリックしたリンクは、デフォルトのウェブブラウザで、そのブラウザ自体のプライバシー方針に従って開きます。音声と動画が自動的に再生されることはありません。

## Siri、ショートカット、Spotlight

MarsDawn は Siri、ショートカット App、Spotlight 向けに、文書の作成やメモの追加などのアクションを提供します。これらを使用すると、入力したテキストはあなたの Mac 上の MarsDawn に渡され、そのアクションが指定する場所（新規文書、または選んだメモフォルダ内の `Inbox.md`）にのみ保存されます。Siri に話した音声は、[Apple のプライバシーポリシー](https://www.apple.com/legal/privacy/)のもとで Apple が処理します。

## 書き出しと印刷

PDF の書き出しと印刷は、あなたの Mac 上で行われます。PDF は選んだ場所に保存されます。印刷は macOS を通じて選んだプリンタに送られます。

## marsdawn コマンドラインツール

別途配布される、使うかどうかを選べる `marsdawn` コマンドラインツールも、完全にあなたの Mac 上で動作します。指定した Markdown ファイルを読み込み、要求された PDF を書き出します。`--allow-remote-images` を指定したときだけウェブ画像を読み込みます。

## 子ども

MarsDawn は、子どもを含め、誰からもデータを収集しません。

## 購入

MarsDawn は Mac App Store を通じて販売されます。購入は Apple 自身の規約のもとで処理され、開発者があなたの支払い情報を受け取ることはありません。

## このポリシーの変更

MarsDawn がデータの扱い方を変える場合、そのバージョンがリリースされる前にこのページが更新され、冒頭の日付も変わります。

## お問い合わせ

プライバシーに関するご質問：[support@southern-light.dev](mailto:support@southern-light.dev)

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向け Markdown エディタ。AI エージェントが書いた文章を読むために作られました。Mac App Store で近日公開予定です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したり印刷したりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウィンドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で近日公開予定の MarsDawn アプリで読む方法です。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
