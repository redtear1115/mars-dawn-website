# Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？

2024 年 12 月、Anthropic は AI エージェントを作る人向けのガイド「Building Effective Agents」を発表した。その要約は 3 つの原則を挙げていて、その 1 つが透明性だ。この記事は、その原則のもう一方の端について書く。エージェントが自分のステップを示したあと、結局は誰かがそれを読むことになる。

**透明性はエージェントがすることで、読むのはあなたがすることだ。Anthropic は開発者に、エージェントの計画のステップを示すよう求めている。コーディングエージェントを日々動かす多くの人にとって、そのステップは結局、しかるべきタイミングで誰かが読む Markdown ファイルとしてやって来る。**

## ガイドが書いていること

Erik S. と Barry Zhang は、要約でこうまとめている。

> “When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.”

（エージェントを実装するとき、私たちは 3 つの中心的な原則に従おうとする。エージェントの設計をシンプルに保つこと。透明性を優先し、エージェントの計画のステップを明示的に示すこと。十分なツールのドキュメントとテストを通じて、エージェントとコンピュータの間のインターフェース（ACI）を丁寧に作り込むこと。）

これらはエージェントを作る人向けの設計原則であって、使う人への操作指示ではない。原則が求めているのはステップを示すことで、誰がそれを読むかは書かれていない。

同じ記事は、タスクを受け取ったあとエージェントが何をするかも描いている：「Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.」（タスクが明確になると、エージェントは計画を立て、自律的に動く。必要に応じて、追加の情報や判断を求めて人間に戻ってくることもある。）そして：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（エージェントはチェックポイントや障害に出会ったとき、人間のフィードバックを待って一時停止できる。）動詞に注目してほしい：*potentially*（必要に応じて）と *can*（できる）。チェックポイントは、エージェントが持ちうる設計として描かれていて、必須のものとしてではない。

## チェックのほとんどは、あなたがしているわけではない

ここは誇張しやすいところなので、ガイドが実際に最初に置いていることを見ておこう。エージェントは、世界に対して自分自身をチェックする：「During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.」（実行中、エージェントが自分の進捗を評価するには、各ステップで環境から「ground truth」（ツール呼び出しの結果やコード実行の結果など）を得ることが重要だ。）この一文の ground truth は、テスト結果やツールの出力を指していて、人間のことではない。

ガイドはリスクについても率直だ：「The autonomous nature of agents means higher costs, and the potential for compounding errors.」（エージェントの自律的な性質は、より高いコストと、エラーが積み重なる可能性を意味する。）その答えは、ガードレール付きのサンドボックス環境での広範なテストであって、「もっと注意深く読め」ではない。

人が実際に登場するのは、コーディングエージェントについての付録だ：「However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.」（しかし、自動テストは機能の検証には役立つ一方、解決策がより広いシステム要件に沿っているかを確かめるには、人によるレビューが依然として重要だ。）この一文はコードについてのものだが、それが指し示すギャップは、どんなエージェントを使っていても見覚えがあるはずだ。テストは、何かが動くことは教えてくれても、それがあなたの意図どおりかまでは教えてくれない。

## 示されたステップは、どこへ行くのか

**ここから先は、私たちの解釈であって、Anthropic の主張ではない。**

コーディングエージェントを日々使っているなら、その計画のステップは、たいていダッシュボードには現れない。ファイルとして現れる：`plan.md`、チェックボックス付きのタスクリスト、エージェントが書き換え続ける進捗ファイル、最後にまとめの文書。透明性は、あなたの側から見ると、読むものが増えるということを意味する。

ステップを示すのはエージェント側の役割だ。もう半分は、それが重要な場面で人が読むこと。マイグレーションを実行する前、ブランチをマージする前、「完了」を受け入れる前。すべてを 600 行の、誰も開かないファイルに書き出すエージェントは、紙の上では透明でも、実際には監督されていない。

Harrison Chase は 2024 年、文書についてではなくエージェントフレームワークがどう動くべきかについて、関連することを述べている：「You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.」（内部で何が起きているかを観察できる必要がある。実際に取られるステップは、事前には分からないことがあるからだ。）彼が話しているのは、エージェントを作る人向けのツールだ。もしあなたがエージェントを動かしている当人なら、それがずっと書き続けている素のファイルこそ、あなたが観察できる部分であることが多い。

ここに挙げた著者は誰も MarsDawn について触れておらず、MarsDawn や他の Markdown ツールを推奨してもいない。

## 見た目より読みにくい理由

ファイルは長く、重要な部分はたいてい先頭にはない。変更を説明する図は Mermaid のソースであって、絵ではない（実際に描画されたものを見る方法は[「Mac で Markdown を見る方法」](/ja/view-markdown-on-mac/)にある）。読んでいる途中で、エージェントがファイルを書き換えることもある。ファイルは複数にまたがることが多く、ブランチや worktree が違うこともある。そして問題を見つけたとき、「キャッシュの部分がおかしい」ではエージェントは推測するしかない。この話の詳しい版は[「エージェントが返してくるものを読む」](/ja/reading-agent-output/)にある。

## MarsDawn ができること、できないこと

MarsDawn は、この読み方のための Mac アプリだ。エージェントをより透明にするわけではなく、中に AI モデルもない。計画を要約したり、正しいかどうか教えたりはしない。できることは：

- **長いファイル：**「表示 ▸ サイドバーを表示」（⌃⌘S）でアウトラインタブを開くと、見出しが並ぶ。クリックするとそこへ移動する。
- **図と数式：**ソースとレンダリングされたページが並んで表示され（⌘2）、一緒にスクロールする。Mermaid と KaTeX は描画される。図が壊れている場合、プレビューはそのソースとエラーを一緒に表示する。
- **読んでいる途中の書き換え：**エージェントがファイルを書き換えると、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。
- **複数のファイル：**「ファイル ▸ フォルダを開く⋯」（⇧⌘O）でエージェントの作業フォルダを開く。新しいファイルは 1 秒ほどでファイルタブに現れ、git のチェックアウトならヘッダーにブランチや worktree の名前が出る。
- **行を指し示す：**「編集 ▸ 参照をコピー」（⌥⌘C）で、いまいる場所を `docs/plan.md:42` の形でコピーできる。「AI 用にコピー」（⌃⌥⌘C）は、その下に選択したテキストを付け加える。エージェントのチャットに貼り付ければいい。

読むのはやはりあなただ。MarsDawn は、長く変わり続けるファイルを、あなたが読んでいる間、読みやすく保つだけだ。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- エージェントの出力がなぜ読みにくいか、そのチェックリスト：[エージェントが返してくるものを読む](/ja/reading-agent-output/)。
- そのチェックリストを、実例つきで詳しく：[エージェントの計画を 5 分でレビューする](/ja/reviewing-agent-plans/)。
- エージェントの種類ごとに、どんな文書が返ってくるか：[4 つのエージェント設計パターンと、それぞれが返す文書](/ja/agent-design-patterns/)。
- AI の出力をそもそも読むべき理由（短い版）：[AI の出力を人が確認する理由](/ja/reviewing-ai-output/)。

## 出典

- Erik S. and Barry Zhang, “Building Effective Agents,” Anthropic, December 19, 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)（2026-09-26 時点のオンライン版から引用。同記事は現在、2024 年 12 月以降ツール環境が大きく変わったと注記している）
- Harrison Chase, “What is an agent?,” LangChain, June 28, 2024, archived copy: [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/)（元の URL は現在 2026 年の別記事を表示している）

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
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
