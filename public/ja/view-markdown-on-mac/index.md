# Mac で Markdown ファイルを見る方法。

`.md` ファイルはプレーンテキストです。見出し、太字、表、図は記号で書かれています。見出しには `#`、太字は `**` で囲む、表はパイプで区切る、図は `mermaid` コードブロックといった具合です。プレーンテキストエディタで開くと、これらの記号がそのまま見えます。作者の意図どおりにページを読むには、何かがそれをレンダリングする必要があります。

## 今すぐ無料で：PDF に変換する

無料の `marsdawn` コマンドラインツールは、Markdown ファイルをどの Mac でも開ける PDF にレンダリングします。表、数式、Mermaid 図、ハイライトされたコードはすべてレンダリングされ、MarsDawn アプリすら含め、他に何もインストールする必要はありません。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` は Markdown ファイルの隣に `notes.pdf` を書き出し、`open` はそれをあなたの PDF ビューアで表示します。macOS 15 以降が必要です。実際に書き出したページを使った解説は、[Markdown から PDF へ](/ja/markdown-to-pdf/)にあります。

## MarsDawn で読む

MarsDawn は Mac 向けの Markdown エディタで、Mac App Store で配信中です。`.md` ファイルを開くと、ソースの隣でレンダリングされたページを読めます。

- 入力すると同時にプレビューが更新され、2つのペインは一緒にスクロールします。
- Mermaid のフローチャートとシーケンス図がプレビューに描画され、コードブロックはハイライトされます。
- Finder で Markdown ファイルを選んでスペースキーを押せば、図も含めてクイックルックでプレビューできます。
- 何かを変更したいときは、ソースがすぐそこにあります。MarsDawn はビューアだけでなくエディタでもあります。

もしそのファイルを AI エージェントが書いたなら、これはまさに MarsDawn が想定しているループです。エージェントが書き、あなたがレンダリングされたページを読み、エージェントが修正します。[ホームページ](/ja/)と、エージェントにファイルを開かせる方法については[AI エージェント向け marsdawn](/ja/cli/agents/)をご覧ください。その読み方がなぜ重要か、計画をどうレビューするかは、[「エージェントが返してくるものを読む」](/ja/reading-agent-output/)と[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)にあります。

## 次に

- コマンドラインツールのすべてのオプション：[コマンドライン](/ja/cli/)。
- MarsDawn ができないこと：[一覧はこちら](/ja/limits/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): Mac 向けネイティブ Markdown エディタ。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Markdown のクイックルック](https://marsdawn.southern-light.dev/ja/quicklook/index.md): Finder で Markdown ファイルを選んでスペースキーを押すと、Mermaid 図、KaTeX 数式、ハイライトされたコードまで表示された状態で読めます。MarsDawn のクイックルックは体験期間の制限を受けません。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・プリント書き出し。ブラウザで自分のテーマを作り、コミュニティギャラリーも閲覧できます。
- [テーマを作る](https://marsdawn.southern-light.dev/ja/themes/new/index.md): 配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。
- [テーマギャラリー](https://marsdawn.southern-light.dev/ja/themes/gallery/index.md): コミュニティが投稿した MarsDawn のプレビューテーマを閲覧し、シナリオで絞り込み、問題があれば通報できます。ブラウザで自分のテーマを作れます。インストールも git も不要です。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [編集者の読書ノート](https://marsdawn.southern-light.dev/ja/reading-notes/index.md): AI エージェントを作っている人たちが実際に何を主張しているかを見る、6 本の短いノート——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain、Andrew Ng——それぞれが、エージェントの返してきたものを読む人にとって何を意味するか。
- [読書ノート：Anthropic](https://marsdawn.southern-light.dev/ja/reading-notes/anthropic-building-effective-agents/index.md): 2024 年 12 月に Anthropic が発表したガイドは workflow と agent を分けて考え、5 つの workflow パターンを説明している。そのうち 1 つは、もう一回の LLM 呼び出しがレビューを担う。これは、あなたのフォルダに落ちてくるものにとって何を意味するか。
- [読書ノート：Chip Huyen](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
- [読書ノート：Lilian Weng](https://marsdawn.southern-light.dev/ja/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng が 2023 年に書いた、広く引用されているサーベイは、LLM エージェントを、脳とプランニング、記憶、ツール利用の組み合わせとして描く。各部分が普通あなたに何を読ませることになるか、そして計画が予想外の事態に調整できないという、彼女自身が挙げる限界。
- [読書ノート：Harrison Chase](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.
- [Français](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Español](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.
- [한국어](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
