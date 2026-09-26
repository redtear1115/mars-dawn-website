# Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事

**2026 年 7 月、LangChain は Harrison Chase の 2024 年の記事「What is an agent?」があった URL に、新しい「What is an AI agent?」を公開した——今回は Jess Ou が書いたもので、定義は当時の彼の一文とほぼ一言一句同じだ。彼女の記事の大半は、彼の記事が扱わなかったこと、つまりエージェントを自動的に評価する一連のパイプライン全体について書かれている。そのパイプラインのどこにまだ人が必要で、どこはもう必要ないか、彼女の文章は率直に書いている。**

## この記事が主張すること

Ou の定義は、Chase のあの一文をほとんどそのまま繰り返している。

> “An AI agent is a system that uses a large language model to decide the control flow of an application.”

（AI エージェントとは、大規模言語モデルを使ってアプリケーションの制御フローを決めるシステムだ。「制御フロー」も、次にどのステップを実行するかのことを指す。）

そこから彼女は、LangChain の Agent Development Lifecycle を説明する：build、test、deploy、monitor の 4 段階と、人がすべての実行記録を読まなくてもエージェントの働きをチェックできる、階層的なやり方だ。online evals は本番のトラフィックの trace（1 回の実行の記録）をサンプリングして退行を検出し、offline evals は整理されたデータセットに対して実行し、変更をリリースする前に問題を見つける。「LLM-as-a-judge」は、人があらかじめ決めた基準にしたがって 1 回の実行の出力に点数をつける方法で、人手によるレビューでは届かない規模で動く。彼女はまた、このパイプラインの中で人がまだどこに立つべきかについても、率直に書いている。

> “For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.”

（慎重な扱いが必要な、あるいは取り消せない行動については、承認、編集、拒否、または明確化のためにエージェントを一時停止させる human-in-the-loop の仕組みを勧める。）

また彼女には、パイプラインがどれだけ整っても省けない判断についての一文もある：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（自分で評価できない判断を、外部に任せてはいけない。あなたが正しい答えを見分けられないなら、エージェントにもできない。）[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)はすでにこの一文をもとに議論を組み立てているので、このノートでは繰り返さない。Ou はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。また彼女は Chase の名前にも一度も触れていない。この 2 つの記事をつないでいるのは、LangChain が 2026 年に、Chase の 2024 年の記事があった URL に彼女のこの記事を公開したこと、そして定義がほぼ同一であることだ——これは私たちの観察であって、彼女自身の主張ではない。

## ここから先は、私たちの解釈であって、Ou の主張ではない

Ou の言う human-in-the-loop は、特定の行動が実行される前にそれを止めること——write の動作を一時停止し、人の承認を待つこと——についてであり、これは Chip Huyen の read-only／write action という分け方を、別の角度から見たのと同じことだ。完成したレポートをあとから読むこととは違う。彼女のパイプライン全体をよく見ると、その大部分は、人を日常的なチェックから外すために設計されている。加えるためではない：online evals、offline evals、LLM-as-a-judge が存在する目的は、そのままチームが 1 回 1 回の実行記録を手作業で確認しなくて済むようにすることだ。これはこの記事への批判ではない——それは彼女自身がはっきり述べている目標であり、本番の規模ではもっともなことでもある。ただしそれは、あなたが自分の手で行うレビュー——エージェントが渡してきた計画やレポートを直接読むこと——が、まさに彼女のパイプラインが減らそうとしている、置き換えようとしているのではない、その種のチェックであることを意味する。彼女自身のあの判断についての一文は、その削減に下限を引いている：自分で読んでも正しいかどうか見分けられない場所は、それでも自分で読むしかない。

## MarsDawn が助けになるところ、ならないところ

MarsDawn は評価パイプラインではなく、中に AI モデルもない——1 回の実行記録に点数をつけたり、LLM-as-a-judge を走らせたり、どの行動が一時停止するほど機密性が高いかを決めたりはしない。MarsDawn がしているのは、彼女のパイプラインがそれでも人に残しているその瞬間、つまり直接読むことだ。サイドバー（「表示 ▸ サイドバーを表示」、⌃⌘S）のアウトラインタブが、長いレポートの見出しを一覧にする。ソースとレンダリングされたプレビューは並んで表示され（⌘2）、Mermaid と KaTeX はそのまま描画される。「編集 ▸ 参照をコピー」（⌥⌘C）と「AI 用にコピー」（⌃⌥⌘C）を組み合わせれば、抜き取りチェックを、エージェントが理解でき、直せる具体的なフィードバックに変えられる。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- 彼女の「判断を外部に任せるな」という一文を一部使って組み立てた、完全なチェックリスト：[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)
- この定義が 2024 年に最初どう書かれていたか：[「Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる」](/ja/reading-notes/harrison-chase-what-is-an-agent/)
- シリーズに戻る：[「編集者の読書ノート」](/ja/reading-notes/)

## 出典

- Jess Ou、「What is an AI agent?」、LangChain、2026 年 7 月 31 日：[https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)（2026-09-26 に取得・引用）

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
- [読書ノート：Lilian Weng](https://marsdawn.southern-light.dev/ja/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng が 2023 年に書いた、広く引用されているサーベイは、LLM エージェントを、脳とプランニング、記憶、ツール利用の組み合わせとして描く。各部分が普通あなたに何を読ませることになるか、そして計画が予想外の事態に調整できないという、彼女自身が挙げる限界。
- [読書ノート：Harrison Chase](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
