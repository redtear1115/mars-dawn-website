# Harrison Chase のスペクトラム：agentic であるほど、見ていたくなる

**2024 年 6 月、LangChain の Harrison Chase は「エージェントとは何か？」という、一見単純な問いから新しいシリーズを始めた。彼は技術的な定義と、「agentic」の度合いを表すスペクトラムを示す。彼の主張では、システムがこのスペクトラムのどこまで進むかによって、それが動いているあいだの内部を見られる必要性が変わってくる。**

## この記事が主張すること

Chase 自身の定義は、多くの人の直感より技術的で、範囲も広いと最初に断ったうえで示される。

> “An agent is a system that uses an LLM to decide the control flow of an application.”

（エージェントとは、LLM を使ってアプリケーションの制御フローを決めるシステムだ。「制御フロー」とは、プログラムが次にどのステップを実行するかのことにすぎない。）

彼はすぐに、この定義が完璧ではないことを認める——LLM が 2 つの経路のどちらかを選ぶだけの単純なシステムも、彼の定義では agent に含まれるが、多くの人の「agent」という直感には合わない。何を「本物の」エージェントに含めるか、含めないかを争うのではなく、彼は Andrew Ng の言い方を採用する——彼は Ng のツイートを引用し、出典を明記している：「rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic」（どの仕事を「本物の」エージェントに含めるか、含めないかを争うより、システムには agentic である度合いにさまざまな段階があると認めればいい）。Chase 自身のコメントはこうだ：「I really agree with this viewpoint and I think Andrew expressed it nicely」（私はこの見方に心から同意する。Andrew はうまく言い表したと思う）。そこから：システムがどれだけ LLM に自分の動き方を決めさせているかによって、システムはより「agentic」になっていく。固定されたルーターから、状態機械、そして自分でツールを作り、記憶する完全に自律したエージェントまで。この光谱をもとに、彼は実際的な主張を展開する：システムが agentic であるほど、あるインフラがより重要になり、中でも一番重要なのが可観測性だ。

> “You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”

（内部で何が起きているかを観察できる必要がある。実際に取られるステップは、事前には分からないことがあるからだ。）

彼はさらに、見るだけでなく介入する能力も必要だと主張を進める：動いているエージェントの状態や指示を、ある時点で修正できる能力もほしくなる。もし意図した経路から外れているなら、それを軌道に戻すために。Chase はこの記事のなかで MarsDawn にはまったく触れておらず、どんな Markdown ツールも勧めていない。

## ここから先は、私たちの解釈であって、Chase の主張ではない

Chase が語っているのは、エージェントのフレームワークを作る人向けのツール——彼は LangGraph と LangSmith を名指ししている——についてであって、完成した文書を読む人についてではない。とはいえ、彼のスペクトラムは、読み始める前に手元のものを見積もる、とても実用的な方法をくれる：あるファイルを生み出したシステムが agentic であればあるほど、その手順がもとのプロンプトから予測できるとは期待しないほうがよく、手元のファイルは「本来起きるはずだったこと」の記録というより、「実際に何が起きたか」の記録として読む価値が増す。彼が言う「内部で何が起きているかを観察する」とは、動いているシステムの内部状態——trace（1 回の実行のあいだにエージェントが行ったすべての記録）、途中のステップ、ツール呼び出し——についてであり、あとから Markdown の計画を読むことについてではない。ただし彼が挙げる理由——手順が事前には分からない——は、エージェントが仕事を終えたあとにあなたに渡してくる文書にも同じように当てはまる：最初から手順が予測できないなら、終わったあとのレポートこそが、それをチェックできる唯一の場所になる。

## MarsDawn が助けになるところ、ならないところ

MarsDawn は、動いているエージェントの内部を観察したりはしない——中に AI モデルはなく、そのファイルを生み出したどんなフレームワークにも接続していないので、あるエージェントが Chase のスペクトラムのどこにいたかを教えてくれることもない。MarsDawn が扱うのは、事後にあなたの手元に届く文書のほうだ：サイドバー（「表示 ▸ サイドバーを表示」、⌃⌘S）のアウトラインタブが、長いレポートの形をはっきり見せてくれる。ソースとレンダリングされたプレビューは並んで表示され（⌘2）、図や数式を扱う。エージェントがファイルを書き換えたときは再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ——これは「まだ動いているものを見ている」ことの、ファイル版だ。「編集 ▸ 参照をコピー」（⌥⌘C）と「AI 用にコピー」（⌃⌥⌘C）を使えば、どのステップで外れたかを正確に指し示せる。これは、走り出したエージェントを軌道に戻すことの、文書版にあたる。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- このシリーズによる、透明性とチェックポイントについてのより完全な議論：[「Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？」](/ja/agent-transparency/)
- LangChain が 2026 年に、この記事と同じ URL で発表した新しい記事。定義はほぼ同一：[「Jess Ou の評価パイプライン、そのうち 1 ステップだけはまだあなたの仕事」](/ja/reading-notes/langchain-what-is-an-agent/)
- シリーズに戻る：[「編集者の読書ノート」](/ja/reading-notes/)

## 出典

- Harrison Chase、「What is an agent?」、LangChain、2024 年 6 月 28 日、アーカイブ版：[http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/)（Wayback Machine 経由で 2026-09-26 に取得・引用。元の URL には現在、Jess Ou が 2026 年に書いた別の記事が表示される）

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
- [読書ノート：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
