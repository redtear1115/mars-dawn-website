# 4 つのエージェント設計パターンと、それぞれが返す文書

2024 年 3 月、Andrew Ng は自身のニュースレター The Batch で、AI エージェントの 4 つの設計パターンを紹介した：reflection、tool use、planning、multi-agent collaboration。これらはふつう、モデルからより良い結果を引き出す方法として、作る側の視点から語られる。この記事は反対側から見る。あなたが使っているエージェントが、このどれかのパターンで作られているなら、フォルダには何が入ってくるのか。まず何を読めばいいのか。

**4 つのパターンは Andrew Ng のものだ。それぞれがどんな文書を返しがちで、何をチェックすべきかは、私たちの推論だ。彼はそのどちらについても書いておらず、このシリーズで人によるレビューを主張してもいない。**

## 4 つのパターン、手短に

Ng はこれを「Agentic Design Patterns Part 1」で説明している。手短に言えば：**reflection** はモデルが自分の成果を見直して改善するもの。**tool use** は Web 検索やコード実行などのツールを呼べるようにするもの。**planning** はモデルが多段階の計画を立てて実行するもの。**multi-agent collaboration** は複数のエージェントが作業を分担し、議論するものだ。

Part 1 で彼は、コーディングのベンチマーク HumanEval を使い、複数の研究グループの結果をチームでまとめた数字で効果を示している：「GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.」（GPT-3.5 の zero-shot での正答率は 48.1%、GPT-4 の zero-shot はもう少し良く 67.0%。しかし、GPT-3.5 から GPT-4 への向上は、反復的なエージェントワークフローを組み込むことに比べれば見劣りする。実際、エージェントのループに包むと、GPT-3.5 は最大で 95.1% に達する。）これらの数字は 1 つのコーディングベンチマークについてのもので、95.1% は最良のケース（「up to」＝最大で）だ。エージェントのワークフローが出力を改善しうることは示しているが、誰がそれを確認するかについては何も語っていない。

**ここから先の、文書とチェック項目は、私たちの解釈であって Ng のものではない。**実際のエージェントは複数のパターンを混ぜて使うことも多い。1 つのコーディングエージェントが、同じセッションの中で計画を立て、ツールを実行し、自分の成果を見直すこともあるので、この 4 種類のファイルを一度に受け取ることもよくある。

## 1. Reflection：すでに自分で見直した草稿

Ng が reflection について書いた記事は、これを、本来は人が与えるフィードバックを自動化するものとして描いている：「What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?」（批判的なフィードバックを与えるステップを自動化し、モデルが自分の出力を自動的に批評して回答を改善するとしたらどうだろうか？）

**返ってきがちなもの：**修正済みの文書。自己レビューのセクションや、「エッジケースは再確認済み」のような一文が付いていることもある。

**チェックすべきこと：**結果を、エージェント自身の批評ではなく、*あなた*の依頼内容と照らし合わせる。自己レビューはそれ自体の仕方で間違うことがある。Chip Huyen：「An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it’s accomplished a task when it hasn’t.」（計画の失敗の興味深い一形態は、reflection の誤りによって引き起こされる。エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）Lilian Weng は、2023 年 6 月、当時 OpenAI に在籍しながら、ブログ Lil’Log で当時のモデルについてこう書いている：「The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.」（専門知識の不足により、LLM は自分の欠陥に気づかず、タスク結果の正しさをうまく判断できないことがある。）（彼女が説明していた研究では、LLM による結果の評価と、人間の専門家による評価が一致していなかった。）「検証済み」と書かれていたら、1 つは自分で確認しよう。

## 2. Tool use：何を実行したかの報告

**返ってきがちなもの：**エージェントが何を実行または検索し、何が返ってきたかのまとめ。「テストスイートを実行：全て合格。」結果の表。見つかったリンク。

Anthropic のガイドは、ツールの結果をエージェント自身のチェックとして描いている：「During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.」（実行中、エージェントが自分の進捗を評価するには、各ステップで環境から「ground truth」（ツール呼び出しの結果やコード実行の結果など）を得ることが重要だ。）そのチェックはエージェントの内部で起きる。あなたのもとに届くのは、エージェントによるその語り直しだ。

**チェックすべきこと：**それぞれの主張が、実際に見える出力までたどれるか。まとめの中の 1 つの数字を、本当の出力と照合する。リンクを 1 つ開いてみる。

## 3. Planning：`plan.md`

**返ってきがちなもの：**計画、仕様書、エージェントが進めながらチェックしていくタスクリスト。

Ng は Part 4 で、このパターンについて率直に語っている：

> “On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.”

（一方で、計画は非常に強力な能力だ。他方で、予測しにくい結果につながる。私の経験では、Reflection と Tool Use という設計パターンは信頼できる形で動かし、アプリケーションの性能を上げられる一方、Planning はまだ成熟度の低い技術で、それが何をするか事前に予測するのは難しいと感じている。）

楽観的でもある：「But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.」（しかしこの分野は急速に進化し続けていて、計画の能力は早く向上すると確信している。）

**チェックすべきこと：**実行前の計画を、[「5 分でのレビュー」](/ja/reviewing-agent-plans/)の方法で見る：形、主張を 1 つ、取り消せないステップ、図、範囲。エージェントが途中で計画を書き換えたら、あなたが承認したバージョンと比較する。git を使っているなら、`git diff plan.md` で何が変わったか分かる。MarsDawn では、アウトラインタブが長い計画の形を示し、書き換えられた計画は、あなた自身に未保存の編集がなければ、読んでいた位置を保ったまま再読み込みされる。

## 4. Multi-agent collaboration：複数のファイル、複数の書き手

**返ってきがちなもの：**あるエージェントによる仕様書、別のエージェントによる実装メモ、さらに別のエージェントによるレビュー、そしてそれらの間でやり取りされる要約。それぞれが自分のブランチや worktree で作業していることもある。

**チェックすべきこと：**引き継ぎの部分。あるエージェントが別のエージェントの成果をまとめるとき、伝わらなかった要件がないか探す。食い違う 2 つのファイルを見つけたら、誰かがそれを土台に作業を進める前に、どちらを正とするか決める。MarsDawn では、「ファイル ▸ フォルダを開く⋯」（⇧⌘O）で共有フォルダを開く。エージェントが書いた新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出るので、別々のブランチにある同名のファイルを開いた 2 つのウィンドウを見間違えることもない。結果を Markdown を読まない人に渡す必要があるときは、[「書き出した PDF を共有する」](/ja/sharing-exported-pdfs/)が、その手順を扱っている。

## ひと目で見る

| パターン（Ng） | 返ってきがちなもの（私たちの推論） | まず読むべきところ（私たちの提案） |
|---|---|---|
| Reflection | 修正済みの草稿。自己レビュー付きのことも | 自分自身の依頼内容と照らし合わせる。「検証済み」を 1 つ確認 |
| Tool use | 何を実行し、何が返ってきたかの報告 | 主張を 1 つ、実際の出力までたどる |
| Planning | `plan.md`、仕様書、タスクリスト | 実行前の 5 分レビュー |
| Multi-agent collaboration | 複数のエージェントによる複数のファイル。複数のブランチにまたがることも | 引き継ぎの部分と、どれが正か |

ここに引用した著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。MarsDawn の中に AI モデルはない：どのパターンがそのファイルを生んだかを知ることはなく、これらのチェックを代わりにやることもない。ファイルを、あなたがチェックしている間、読みやすく保つだけだ。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。詳しくは[「Markdown から PDF へ」](/ja/markdown-to-pdf/)を見てください。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- エージェントの出力がなぜ読みにくいか、そのチェックリスト：[エージェントが返してくるものを読む](/ja/reading-agent-output/)。
- 計画のチェックを、完全な形で：[エージェントの計画を 5 分でレビューする](/ja/reviewing-agent-plans/)。
- 透明性があなたに求めること、求めないこと：[Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？](/ja/agent-transparency/)

## 出典

- Andrew Ng, “Agentic Design Patterns Part 1,” The Batch, March 20, 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, “Agentic Design Patterns Part 2, Reflection,” The Batch, March 27, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, “LLM Powered Autonomous Agents,” Lil’Log, June 23, 2023: [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)（2026-09-26 時点のオンライン版から引用）

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
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
