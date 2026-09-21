# Mac のコマンドラインで、Markdown を PDF に。

無料の `marsdawn` ツールは、コマンド1つで Markdown ファイルを PDF に変換します。表、数式、Mermaid 図、ハイライトされたコードはソースの見た目そのままに仕上がり、MarsDawn アプリすら含め、他に何もインストールする必要はありません。

## インストール

```
brew install redtear1115/tap/marsdawn
marsdawn --version
```

Apple シリコンの Mac では、Homebrew がビルド済みのコピーを数秒でインストールします。Intel Mac ではソースからビルドするため数分かかり、Xcode 26 以降が必要です。macOS 15 以降で動作し、`marsdawn --version` がインストールされたバージョンを表示します。

## 文書を保存する

`plan.md` という名前のファイルに、次の内容を貼り付けてください。

````
# 計画：エクスポートを高速化

この計画はエージェントが書きました。内容を確認してから、PDF にします。

## ステップ

| ステップ | 担当 | 状況 |
|------|-------|--------|
| 遅いページを計測する | エージェント | 完了 |
| レンダリング済み図をキャッシュする | エージェント | レビュー中 |

50 ページの文書で目標とするのは $t < 2\,\text{s}$：

$$
t_{\text{total}} = \sum_{i=1}^{n} t_i
$$

```mermaid
graph LR
  ドラフト --> レビュー --> 公開
```

```swift
let pdf = try export("plan.md")
```
````

## 書き出す

```
marsdawn export plan.md
```

ソースの隣に `plan.pdf` を書き出し、保存先を表示します。

```
Exported /Users/you/plan.pdf (1 page)
```

これはそのページを、`marsdawn` 0.5.0 の実行結果から実際にキャプチャしたものです。

![書き出された PDF：見出し、ステップの表、インラインと独立した数式、ドラフト・レビュー・公開の図、ハイライトされた Swift のコード1行。](/assets/cli/plan-ja.png)

## テーマ、用紙サイズ、ファイル名を選ぶ

```
marsdawn export plan.md --theme classic --paper letter -o handout.pdf
```

- `--theme`：dawn、classic、modern、vivid のいずれかで、テーマのライトカラーを使います。指定しない場合、`export` は `$MARSDAWN_THEME`、それもなければ dawn を使います。
- `--paper`：a4 または letter。デフォルトは a4 です。
- `-o`：PDF をソースの隣ではなく、どこに書き出すか。
- `--allow-remote-images`：レンダリング時にウェブから画像を読み込みます。指定しない限りオフのままです。

## うまくいかない場合

- `A full installation of Xcode.app 26.0 is required to compile this software.` Homebrew が `marsdawn` をソースからビルドしています。Intel Mac ではこのようになります。App Store から Xcode 26 以降をインストールしてから、もう一度インストールしてください。
- `marsdawn: No such file: …` パスがファイルを指していません。ファイル名を確認するか、そのファイルがあるフォルダでコマンドを実行してください。
- `… already exists. Pass --force to replace it.` 同じ名前の PDF がすでに存在します。`--force` を付けて置き換えるか、`-o` で別の場所に書き出してください。
- `Error: The value '…' is invalid for '--theme <theme>'.` テーマまたは用紙サイズが認識されていません。テーマは dawn、classic、modern、vivid、用紙は a4 または letter です。

## 次に

- すべてのオプションと出力される JSON：[コマンドライン](/ja/cli/)。
- コーディングエージェントにこれをやらせるには：[marsdawn のエージェントスキル](/ja/cli/skill/)。

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
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・印刷書き出し。もっと多くの輸入可能なテーマと、自分のテーマを共有できるギャラリーも計画されています。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [English](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
