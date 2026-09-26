# エージェントの仕事は、あなたが読む Markdown ファイルとして返ってくる。

コーディングエージェントに移行を計画させたり、仕様書を書かせたり、バグを追わせたりする。しばらく自分で動いたあと、返ってくるのは 1 つのファイルだ。`plan.md`、`SPEC.md`、進捗報告、調査のまとめ。確認できる範囲では、そのファイルが仕事そのものだ。

**エージェントが正しくやったかどうかは、返ってきたものを読んで初めて分かる。MarsDawn は、その読み方のための Mac アプリだ。**

## エージェントを作る人たちの言葉

引用はそのまま。私たちの解釈はあとに書く。

- Anthropic の「Building Effective Agents」（Erik S. と Barry Zhang、2024 年 12 月）は、エージェントを作るための 3 つの原則を挙げていて、その 1 つが「Prioritize transparency by explicitly showing the agent’s planning steps.」（透明性を優先し、エージェントの計画のステップを明示的に示す。）これはエージェントを作る人向けの原則だ。あなたの側から見れば、その透明性とは、結局あなたが読むことになる計画のことだ。
- 同じ記事：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（エージェントはチェックポイントや障害に出会ったとき、人間のフィードバックを待って一時停止できる。）動詞に注目してほしい：*can*（できる）。
- Chip Huyen は「Agents」（2025 年 1 月）で、計画と実行を分けるべき理由をこう説明する：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.」（監督がなければ、エージェントは何時間もそのステップを実行し続け、API 呼び出しに時間とお金を浪費したあとで、それが何も進んでいないことにあなたが気づく、ということもあり得る。）彼女はさらにこんな失敗も描いている：「The agent is convinced that it’s accomplished a task when it hasn’t.」（エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）50 人を 30 部屋に割り振るよう頼まれたエージェントは、40 人しか割り振らないまま、終わったと言い張る。
- Andrew Ng は The Batch（2024 年 4 月）で planning パターンについてこう述べる：「On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results.」（一方で、計画は非常に強力な能力だ。他方で、予測しにくい結果につながる。）これは予測可能性についての指摘であって、人によるレビューを求めているわけではない。彼は計画能力が急速に向上すると見ている。

**ここからは著者たちの主張ではなく、私たちの推論だ：**エージェントが計画を示し、チェックポイントで止まるなら、そのチェックポイントで計画を読むのは、たいていあなただ。エージェントが終わっていないのに終わったと思い込むことがあるなら、その「完了報告」にも読み手が必要になる。ここに挙げた著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。

## 見た目より読みにくい理由

ファイルは長く、重要な部分はたいてい先頭にはない。Mermaid の図や数式が入っていて、ソースのままでは追いにくい。読んでいる途中で、エージェントがまだファイルを書き換えていることもある。ファイルは複数にまたがることが多く、ブランチや worktree をまたぐこともある。そして問題を見つけたとき、「キャッシュの部分がおかしい」ではエージェントは推測するしかないが、「`docs/plan.md:42` はバックフィルが終わる前に古いテーブルを落としている」ならそうはならない。

## MarsDawn が助けになるところ

- **長いファイル：**サイドバーのアウトラインタブ（⌃⌘S）に見出しが並ぶ。クリックすると両方のペインがそこへ移動する。
- **図と数式：**Mermaid と KaTeX はソースの隣のプレビューに描画され（⌘2）、両方のペインが一緒にスクロールする。
- **読んでいる途中の書き換え：**エージェントがファイルを書き換えると、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。
- **複数のファイル：**「ファイル ▸ フォルダを開く⋯」（⇧⌘O）でエージェントの作業フォルダを開く。新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出る。
- **正確なフィードバック：**「編集 ▸ 参照をコピー」（⌥⌘C）で、いまいる場所を `docs/plan.md:42` の形でコピーできる。「AI 用にコピー」（⌃⌥⌘C）は、その下に選択したテキストを付け加える。どちらもエージェントのチャットに貼り付ければいい。

このループにはもう 2 つ関係がある。エージェントは `marsdawn open plan.md:42` を実行して、MarsDawn でファイルを 42 行目、つまりまず見てほしい行で開かせることができる。そしてレビューが終わったファイルは、アプリから、あるいは無料の `marsdawn export` コマンドで PDF に書き出せる。

MarsDawn の中に AI モデルはない。計画を要約したり、採点したり、何が間違っているか教えたりはしない。読むのはあなたで、MarsDawn は長く変わり続けるファイルを読みやすく保ち、正確な行を指し示せるようにするだけだ。

## 5 分でエージェントの計画をレビューする

どんなエディタでも使える方法だ。

1. 見出しだけを読む。アウトラインは頼んだ内容と一致しているか。セクションが欠けていれば、たいてい作業も欠けている。
2. 「完了」「合格」「検証済み」と書かれている箇所をすべて見つけ、そのうち 1 つを自分で確認する：ファイルを開く、テストを実行する、行数を数える。
3. 取り消せないステップを探す：データの削除、マイグレーション、force push、何かを送信・支払い・公開する処理。それらはあなたの明示的な OK を待つべきだ。
4. 図はレンダリングした状態で読み、矢印の 1 つひとつを本文と照らし合わせる。
5. 計画が触れるファイルとシステムを列挙する。頼んでいないことがあれば、実行前に確認する。
6. フィードバックは「場所・問題・直し方」で書く：「`plan.md:88`：バックフィルが drop のあとに実行される。ステップ 4 と 5 を入れ替えて。」1 行に 1 つの問題だけを書く。

時間がないなら、ステップ 2 だけをやろう。終わったと思い込んでいるエージェントが見つかるのは、たいていそこだ。より詳しい説明と実例は[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)にある。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。アプリが出たあとは、`marsdawn open` でエージェントにファイルを開かせることもできます。

[コマンドライン](/ja/cli/) · AI エージェント向けの参照：[marsdawn for agents](/ja/cli/agents/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- AI の出力をそもそも読むべき理由（短い版）：[AI の出力を人が確認する理由](/ja/reviewing-ai-output/)。
- レビュー中もエージェントの context を小さく保つ：[トークンを抑えたレビュー](/ja/token-efficient-review/)。
- なぜエージェントはそもそも計画を示すのか：[Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？](/ja/agent-transparency/)
- 上のチェックリストを、実例つきで詳しく：[エージェントの計画を 5 分でレビューする](/ja/reviewing-agent-plans/)。
- エージェントの種類ごとに、どんな文書が返ってくるか：[4 つのエージェント設計パターンと、それぞれが返す文書](/ja/agent-design-patterns/)。

## 出典

- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)（2026-09-26 時点のオンライン版から引用。同記事は現在、2024 年 12 月以降ツール環境が大きく変わったと注記している）
- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

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
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
