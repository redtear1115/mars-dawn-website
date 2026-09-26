# Lilian Weng が 2023 年に描いたエージェントの設計図、各部分が残すファイル

**2023 年 6 月、当時 OpenAI に在籍していた Lilian Weng は、自身のブログ Lil'Log に長いサーベイを発表し、LLM を使ったエージェントを、脳（モデル）とプランニング、記憶、ツール利用という 3 つの部品の組み合わせとして描いた。これは広く引用されている初期のエージェントの枠組みであり、彼女はその枠組みがどこでまだ崩れるかについても率直だ。**

## この記事が主張すること

Weng は冒頭で、記事全体の枠組みをこう定める。

> “In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components: Planning ... Memory ... Tool use”.

（LLM を使った自律型エージェントのシステムでは、LLM がエージェントの脳として機能し、いくつかの主要な部品——プランニング……記憶……ツール利用……によって補われる。）

彼女の説明では、プランニングはタスクをサブゴールに分解することと、過去の行動を振り返って今後の行動を改善することの両方を含む。記憶は短期（モデルがいま見ているコンテキストで、彼女は in-context と呼ぶ）と長期（通常はモデルの外、検索可能なデータベースに保存され、彼女は vector store と呼ぶ）に分かれる。ツール利用は、モデルが自分の重みの中にない情報——最新の情報、コードの実行、ほかの API——を外部に求めることを可能にする。記事の終わりに近い、彼女自身が「Challenges」と題した節で、彼女はある限界をはっきりと指摘する。

> “LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.”

（LLM は予想外のエラーに直面したとき、計画を調整するのが苦手であり、試行錯誤から学ぶ人間と比べて頑健さに欠ける。）

また、化学エージェント「ChemCrow」についてのツール利用の事例研究のなかで、彼女はもっと狭い問題を指摘している：LLM による評価では GPT-4 とほぼ同等とされたが、人間の専門家による評価では、ChemCrow は正確性の点でずっと優れているとされた。彼女の結論は「自己評価」についてのものであり、彼女自身の「反省（reflection）」の部品そのものについてではない。

> “The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.”

（専門知識が欠けていることが原因で、LLM は自分自身の欠陥に気づかず、タスクの結果が正しいかどうかをうまく判断できないことがある。）

Weng はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。

## ここから先は、私たちの解釈であって、Weng の主張ではない

Weng が描いているのは 2023 年時点のエージェントのアーキテクチャであって、「誰かがエージェントの出力を読む」という話はまったく出てこない——ファイルを確認する人がいるとすら、彼女は書いていない。とはいえ、彼女自身が挙げる 3 つの部品は、あなたが読むことになりうる 3 種類のものにちょうど対応している。プランニングは、たいてい実行前に読む文書——計画そのもの——を残す。すでにその中に、ひとまわりの「反省」や自己チェックが組み込まれていることもある。記憶は、たいてい目に見えない。ただしエージェントが長期記憶を、書き続けている下書きファイルとして保存している場合は別で、そのファイル自体を単独で開く価値がある。なぜなら、それは古い、間違った前提を、何も言わないまま後続の多くのステップに持ち越してしまうことがあるからだ。ツール利用は、たいてい「何を実行し、何を得たか」というレポートを残す——計画というより、記録に近い。

計画が予想外の事態に調整できないという彼女の指摘は、あなたの側から見れば、昨日承認した計画が、今日にはもう古くなっているかもしれない理由になる：計画が想定していなかった何かが途中で起きても、エージェントは計画を立て直すのではなく、そのまま進んでしまうかもしれない。すると最後のレポートは、途中で回り道をしたことには触れずに、もとの計画が「成功した」ことだけを描くかもしれない。これは私たちの推論であって、彼女自身の主張ではない——彼女が語っているのはモデル自身の頑健さについてであって、読み手が何に注意すべきかについてではない。

## MarsDawn が助けになるところ、ならないところ

MarsDawn の中に AI モデルはなく、ある計画が実際に起きたことから静かにずれてしまっていないかを教えてくれることもなければ、あるファイルがプランニングのファイルなのか、記憶のファイルなのか、ツール利用のレポートなのかを見分けてくれることもない——それは内容を読み込んで初めてできる判断であり、あなた自身がする必要がある。MarsDawn がしているのは：サイドバー（「表示 ▸ サイドバーを表示」、⌃⌘S）のアウトラインタブが、長い計画の形をひと目で見せてくれる。ソースとレンダリングされたプレビューは並んで表示され（⌘2）、Mermaid と KaTeX はそのまま描画される。読んでいる途中でエージェントがファイルを書き換えても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ——これは特に役に立つ。なぜなら、静かに書き換えられた計画こそ、彼女が「Challenges」の節でモデル側から描いている、まさにその失敗モードだからだ。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- 異なるエージェントの設計パターンがそれぞれ何のファイルを渡してくるか：[「4 つのエージェント設計パターンと、それぞれが渡してくる文書」](/ja/agent-design-patterns/)
- 実行前に計画を 5 分でレビューする方法：[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)
- シリーズに戻る：[「編集者の読書ノート」](/ja/reading-notes/)

## 出典

- Lilian Weng、「LLM Powered Autonomous Agents」、Lil'Log、2023 年 6 月 23 日：[https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)（2026-09-26 に取得・引用。この記事を書いた当時、彼女は OpenAI に在籍しており、ここでもその当時の立場としてのみ記す）

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で近日公開予定です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で近日公開予定の MarsDawn アプリで読む方法です。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込んで marsdawn をインストールし、動作確認をし、Markdown を PDF に書き出し、JSON の結果を読み取るための1つのファイルです。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
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
- [編集者の読書ノート](https://marsdawn.southern-light.dev/ja/reading-notes/index.md): AI エージェントを作っている人たちが実際に何を主張しているかを見る、6 本の短いノート——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain、Andrew Ng——それぞれが、エージェントの返してきたものを読む人にとって何を意味するか。
- [読書ノート：Anthropic](https://marsdawn.southern-light.dev/ja/reading-notes/anthropic-building-effective-agents/index.md): 2024 年 12 月に Anthropic が発表したガイドは workflow と agent を分けて考え、5 つの workflow パターンを説明している。そのうち 1 つは、もう一回の LLM 呼び出しがレビューを担う。これは、あなたのフォルダに落ちてくるものにとって何を意味するか。
- [読書ノート：Chip Huyen](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
- [読書ノート：Harrison Chase](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng's widely cited 2023 survey describes an LLM agent as a brain plus planning, memory and tool use. What each part tends to leave behind for you to read, and the limitation she names in plans that don't adjust to surprises.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被廣泛引用的整理，把 LLM agent 描述成大腦加上規劃、記憶、工具使用。每個部件通常會留給你讀什麼，以及她點名的一個限制：計畫遇到意外不太會調整。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM agent 描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
