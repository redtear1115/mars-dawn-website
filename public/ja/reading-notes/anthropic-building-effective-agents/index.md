# Anthropic は workflow と agent を分けて考える。あなたの読み方はどちらに近いか？

**2024 年 12 月に Anthropic が発表した「Building Effective Agents」は、AI エージェントを作る人向けのガイドだ。冒頭で「workflow」と「agent」という 2 つの言葉を分け、そのあと、まず使える中で一番シンプルなやり方から始めること——場合によっては agentic なシステムをまったく作らないことさえ含めて——を勧め、それでは足りないときにだけ、整理された 5 つの workflow パターンのどれかに手を伸ばすよう提案する。そのパターンの 1 つでは、もう一回の LLM 呼び出しがレビュアーの席に座る。このノートはそのパターンについて、そして残りの 4 つがあなたに何を読ませることになるかについて書く。**

## ガイドが主張すること

Erik S. と Barry Zhang がこの記事を書いたのは、LLM でどうシステムを作るか決めようとしているエンジニア向けだ。まず、こういう定義から始まる。

> “Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.”

（Workflow とは、LLM とツールがあらかじめ決められたコードの経路にしたがってオーケストレーションされるシステムだ。一方 agent は、LLM が自分自身のプロセスとツールの使い方を動的に決め、タスクをどう成し遂げるかをみずから制御し続けるシステムだ。）

そのあと、彼らのアドバイスは控えめに始まる。

> “When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.”

（LLM を使ってアプリケーションを作るとき、私たちはまず可能な限りシンプルな解決策を見つけ、必要なときだけ複雑さを増やしていくことを勧める。これは、agentic なシステムをまったく作らないことを意味する場合もある。）

より多くの構造が必要なとき向けに、彼らは 5 つの workflow パターンを説明している：prompt chaining（タスクを一連の呼び出しに分割し、ステップの間に任意でチェックを挟む）、routing（ルーティング）、parallelization（並列化）、orchestrator-workers（1 つの LLM がタスクを複数の部分に分け、複数の worker LLM に渡し、その結果をまとめる）、そして evaluator-optimizer。最後のこのパターンについて、原文はこう書いている。

> “In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.”

（evaluator-optimizer workflow では、1 回の LLM 呼び出しが応答を生成し、もう 1 回の呼び出しがループの中で評価とフィードバックを行う。）

Anthropic はこのガイドのなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。このガイドの透明性の原則と「チェックポイント」という言葉については、[「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」](/ja/agent-transparency/)がすでにくわしく扱っているので、このノートでは繰り返さない。人によるコードレビューについての一文も、あの記事が扱っている、コーディングエージェント専用の付録という文脈でこそ意味を持つ。

## ここから先は、私たちの解釈であって、Anthropic の主張ではない

Anthropic は、workflow が終わったあと最終的な出力を誰がチェックするかについては書いていない。そもそもこの記事全体が文書についてのものではなく、作る人向けのアーキテクチャの決め方についてのものだ。とはいえ、この 5 つのパターンが、あなたに読ませることになるファイルの種類は同じではない。prompt chaining と routing は、たいてい目に見えない配管のようなもので、何かがあなたのところに届くとしても、それはこの連鎖の最後の呼び出しの出力にすぎず、ほかの単発の応答と変わらない。Orchestrator-workers は違う：あなたのコーディングエージェントが内部でこのパターンを使っているなら、フォルダに落ちてくるのは、複数の worker の呼び出しを orchestrator がつなぎ合わせて組み立てた 1 つの文書かもしれず、そのうち 1 つの worker の担当箇所にあるミスは、全体としてなめらかに読める要約のなかに埋もれて見逃されやすい。

Evaluator-optimizer は特に立ち止まる価値がある。もともと人間のレビュアーが座っていたかもしれない位置に、このガイドはもう一回の LLM 呼び出しを置いているからだ。これは一種のミスを安く捕まえる正当な方法ではあるが、結局はモデルが、与えられた基準にしたがって別のモデルをチェックしているにすぎない——このシリーズのほかの著者たちも、モデルが自分自身や別のモデルの成果を判定することについて、同じ懸念を口にしている。このガイドは、人が evaluator の判定をもう一度確かめるべきだとはどこにも書いておらず、そのこと自体について立場を取っていない。もしあなたがこの一連のプロセスの返してきたものを最後に読む立場なら、「ループが通した」ことと「私が確認した」ことは同じ文ではない——手元のファイルが両方の場合でまったく同じに見えたとしても。

## MarsDawn が助けになるところ、ならないところ

MarsDawn は、あるファイルがどの workflow パターンから生まれたのかを知らないし、中に AI モデルもない——自前で evaluator のステップを走らせることもなければ、Anthropic が描いたその評価がきちんと仕事をしたかどうかを教えてくれることもない。MarsDawn がしているのは：サイドバー（「表示 ▸ サイドバーを表示」、⌃⌘S）のアウトラインタブが、orchestrator が組み立てた長いファイルの見出しを一覧にし、クリックするとそこへジャンプする。ソースとレンダリングされたページは並んで表示され（⌘2）、一緒にスクロールし、Mermaid の図や KaTeX の数式もソースのままではなく描画される。読んでいる途中でエージェントがファイルを書き換えても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。「編集 ▸ 参照をコピー」（⌥⌘C）は、いまいる場所を `docs/plan.md:42` の形でコピーし、そのままエージェントとのチャットに貼り付ければいい。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- このガイドの透明性の原則とチェックポイントについての、より詳しい話：[「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」](/ja/agent-transparency/)
- エージェントの出力が一般になぜ読みにくいか：[「エージェントが返してくるものを読む」](/ja/reading-agent-output/)
- シリーズに戻る：[「編集者の読書ノート」](/ja/reading-notes/)

## 出典

- Erik S. と Barry Zhang、「Building Effective Agents」、Anthropic、2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)（2026-09-26 に取得・引用）

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
- [読書ノート：Chip Huyen](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
- [読書ノート：Lilian Weng](https://marsdawn.southern-light.dev/ja/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng が 2023 年に書いた、広く引用されているサーベイは、LLM エージェントを、脳とプランニング、記憶、ツール利用の組み合わせとして描く。各部分が普通あなたに何を読ませることになるか、そして計画が予想外の事態に調整できないという、彼女自身が挙げる限界。
- [読書ノート：Harrison Chase](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月發表的指南把 workflow 和 agent 分開來看，並描述了五種 workflow 模式，其中一種讓另一次 LLM 呼叫來審查。這對落進你資料夾的東西來說，意味著什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和 agent 分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
