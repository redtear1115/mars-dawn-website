# Andrew Ng が自分の設計パターンを予測可能性で自らランク付けする

**2024 年の初め、Andrew Ng は The Batch の 5 本の手紙で、4 つの agentic な設計パターン——reflection（反省）、tool use（ツール利用）、planning（プランニング）、multi-agent collaboration（複数エージェントの協調）——を説明した。そして珍しく、この 4 つのうちどれをより信頼でき、どれを予測しづらいと感じているかを、読者にはっきり伝えている。**

## これらの手紙が主張すること

[「4 つのエージェント設計パターンと、それぞれが渡してくる文書」](/ja/agent-design-patterns/)は、この 4 つのパターンがそれぞれ何であるか、私たち自身の推論として、それぞれが普通あなたに何を渡してくるか、そして Part 4 から引用した、planning についての Ng 自身の評価——「while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do」（Reflection と Tool Use という設計パターンは、どちらも自分のアプリケーションで確実に動かし、性能を高められている。しかし Planning はまだ成熟していない技術で、それが何をするか事前に予測するのは難しいと感じる）——をすでにくわしく扱っている。このノートで補うのは、あの記事が使っていない、残り 2 本の手紙にある同じランク付けだ：Part 3 は Part 4 の 1 週間前に書かれ、先にこのランク付けを述べている。Part 5 は、Part 4 が触れていないパターン——multi-agent collaboration——にまでランク付けを広げる。tool use を紹介する Part 3 で、彼はこう書いている。

> “In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.”

（今後の手紙では、Planning と Multi-agent collaboration という設計パターンについて説明する。これらは AI エージェントにずっと多くのことをさせられるが、成熟度が低く、予測しづらい——とはいえ、とても刺激的な——技術だ。）

2 週間後、彼はシリーズの最後の手紙で multi-agent collaboration を扱いながら、別の角度から同じランク付けを確認している。

> “Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.”

（Planning という設計パターンと同じように、multi-agent collaboration の出力品質は予測しづらいと感じる。特に、エージェント同士を自由にやり取りさせ、複数のツールを与えたときはそうだ。より成熟した Reflection と Tool Use のパターンのほうが、より信頼できる。）

彼が語っているのは、これらのパターンが自分のアプリケーションの成果をどれだけ高めるかについてであって、その出力をどれだけ注意深く審査すべきかについてではない——このシリーズは人によるレビューをまったく求めておらず、MarsDawn にも、どんな Markdown ツールにも触れていない。

## ここから先は、私たちの解釈であって、Ng の主張ではない

Ng のランク付けは、開発者の椅子から見た出力品質と予測可能性についてのものだが、大まかに言えば、それぞれのパターンが残す記録に、あなたの側からどれだけの注意を払う価値があるかにも対応している。彼がより信頼できると感じている reflection と tool use は、たいてい「すでに終わった作業」を描くもの——修正済みの草稿、何を実行したかのレポート——を渡してくるので、そのなかの 1 つの主張を実際の出力と照らし合わせれば、たいていリスクの大部分をカバーできる。彼が予測しづらいと感じている planning と multi-agent collaboration は、たいてい「まだ起きていないこと」について書かれたもの、あるいは複数のエージェントに分散した複数のファイルを渡してくる：あなたの承認を待っている計画や、まだ実行によって検証されていないエージェント間の引き継ぎだ。彼自身の言葉を借りれば、この 2 つこそ、「書かれていること」と「実際に起きること」のギャップが一番大きい場所であり——これはまさに〈エージェントの計画を 5 分でレビューする〉が、Chip Huyen のエッセイから引き出している「なぜ実行前に見るのか」という節の道理でもある。何かが実行される前に問題を見つけることが、一番安く済むタイミングだ。

## MarsDawn が助けになるところ、ならないところ

MarsDawn は、あるファイルが Ng の 4 つのパターンのどれから生まれたのかを知らないし、何かを予測可能性でランク付けすることもなく、中に AI モデルもない——彼のランク付けが示唆しているようなチェックを、代わりにしてくれるわけではない。MarsDawn がしているのは、あなた自身がチェックするあいだ、ファイルを読みやすく保つことだ：サイドバー（「表示 ▸ サイドバーを表示」、⌃⌘S）のアウトラインタブで、長い計画の形が見て取れる。ソースとレンダリングされたプレビューは並んで表示される（⌘2）。複数エージェントの引き継ぎの場合は、「ファイル ▸ フォルダを開く…」（⇧⌘O）で共有フォルダを開くと、別々のエージェントが新しいファイルを書いたとき、それはおよそ 1 秒でファイルタブに現れ、リストの上には git のブランチや worktree の名前も表示されるので、別々のエージェントが書いた同じ名前のファイルを取り違えることもない。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- それぞれのパターンが渡してくる文書の全体像：[「4 つのエージェント設計パターンと、それぞれが渡してくる文書」](/ja/agent-design-patterns/)
- 実行前に計画を 5 分でレビューする方法：[「エージェントの計画を 5 分でレビューする」](/ja/reviewing-agent-plans/)
- シリーズに戻る：[「編集者の読書ノート」](/ja/reading-notes/)

## 出典

- Andrew Ng、「Agentic Design Patterns Part 1」、The Batch、2024 年 3 月 20 日：[https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng、「Agentic Design Patterns Part 3: Tool Use」、The Batch、2024 年 4 月 3 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/)（2026-09-26 に取得・引用）
- Andrew Ng、「Agentic Design Patterns Part 4: Planning」、The Batch、2024 年 4 月 10 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)（引用は `design/inbox/276-agent-blog-series.md` からそのまま再利用したもので、`/ja/agent-design-patterns/` ですでに使われている）
- Andrew Ng、「Agentic Design Patterns Part 5, Multi-Agent Collaboration」、The Batch、2024 年 4 月 17 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/)（2026-09-26 に取得・引用）

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
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
