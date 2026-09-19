# MacMD Viewer 対 MarsDawn。

どちらも Markdown をレンダリングして読むための Mac アプリです。MacMD Viewer は `.md` ファイルを開いて完成したページを表示しますが、編集はできません。MarsDawn は同じようにレンダリングされたプレビューの隣にエディタを置き、1つのウインドウで書きながら確認できます。ここでは機能ごとに両者の違いを見ていきます。

## 読むだけでよく、編集の必要がない場合

他の人が書いた Markdown を読むことだけが仕事で、ソースに触れる必要が一切ないなら、MacMD Viewer は妥当な選択です。まさにそのために作られており、今すぐ入手でき、より古い macOS でも動作します。読むことだけが仕事ではなくなったときに MarsDawn が価値を持ちます。エージェントの Markdown はたいてい、もう一度手直しが入るからです。

## それぞれのアプリでできること

- **編集：**MacMD Viewer は設計上、読み取り専用です。MarsDawn はソースを編集しながらその場でレンダリングするので、入力すると変更が表示されます。
- **プレビューのテーマ：**MacMD Viewer には12種類の文書テーマがあります。MarsDawn は Dawn、Classic、Modern、Vivid の4種類で、それぞれライトとダークのパレットがあります。
- **図と数式：**どちらも Mermaid 図をレンダリングし、コードをハイライトします。MarsDawn は KaTeX の数式もレンダリングしますが、MacMD Viewer 自身の紹介には数式のレンダリングについて記載がありません。
- **Finder 連携：**どちらもクイックルック拡張機能を追加しており、Finder で `.md` ファイルを選んでスペースキーを押すとレンダリングされたページが表示されます。
- **PDF と印刷：**どちらもレンダリングされたページを PDF として書き出したり印刷したりできます。
- **システム要件：**MacMD Viewer は macOS 14（Sonoma）以降が必要です。MarsDawn は macOS 26（Tahoe）以降が必要です。
- **言語：**MarsDawn のインターフェースは英語、繁体字中国語、簡体字中国語、日本語に対応しています。MacMD Viewer 自身の資料は UI の言語を明記していないため、このページではその点を比較していません。

## 価格と購入方法

- **購入場所：**MacMD Viewer は自社サイトから直接ダウンロードでき、Homebrew と Setapp にもありますが、Mac App Store にはありません。MarsDawn は Mac App Store のみです。
- **価格：**MacMD Viewer は1台の Mac につき一度きり USD 19.99（3台パックやボリュームパックはより高額）。MarsDawn は無料でダウンロードでき、その後 USD 4.99 の一度きりのロック解除です。
- **先に試す：**MacMD Viewer には無料トライアルはなく、直接購入には代わりに14日間の返金保証が付いています。MarsDawn は支払う前に14日間のトライアルを提供します。
- **返金と更新：**MacMD Viewer の返金と更新は自社サイトで処理されます。MarsDawn の購入は Apple を通じて行われるため、返金と更新は Apple の標準プロセスを使います。
- **アカウント：**どちらのアプリも利用にアカウントは不要です。

## 今すぐ無料で試す

MarsDawn は Mac App Store で近日公開予定で、まだ販売されていません。それまでは、無料の `marsdawn` コマンドラインツールが、今すぐどんな Markdown ファイルも Mermaid 図とハイライトされたコード付きの PDF にレンダリングでき、他に何もインストールする必要はありません。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 次に

- 完全な解説：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- MarsDawn ができないこと：[一覧はこちら](/ja/limits/)。
- コマンドラインツールのすべてのオプション：[コマンドライン](/ja/cli/)。

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
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
