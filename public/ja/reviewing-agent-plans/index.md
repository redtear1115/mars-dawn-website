# エージェントの計画を 5 分でレビューする

エージェントが計画を書き上げ、ゴーサインを待っている。あなたにあるのは 5 分で、1 時間ではない。ここでは、その 5 分の使い方を紹介する。プレーンテキストのエディタでも、どんなエディタでも使える方法だ。MarsDawn が助けになるステップもあるので、どこかは明記する。ただし、いちばん大事なステップでは助けにならない。

**計画は最初から最後まで読まない。まず形を見て、主張を 1 つ確認し、取り消せないものを探し、図と範囲を見て、それからエージェントが動けるフィードバックを書く。6 ステップ、約 5 分。**

## 実行前に手間をかける理由

Chip Huyen は、計画と実行を分けるべき理由を説明しながら、コストをはっきり言う：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.」（監督がなければ、エージェントは何時間もそのステップを実行し続け、API 呼び出しに時間とお金を浪費したあとで、それが何も進んでいないことにあなたが気づく、ということもあり得る。）私たちからの補足：計画は、間違いを見つけるのにいちばん安上がりな場所だ。`plan.md` の 1 行を直すのは、1 文で済む。エージェントが実行し終わったあとの後始末は、午後まるごとかかることもある。

## 例

ユーザーのアバターをオブジェクトストレージに移す作業を、既存のリンクを壊さずにやるようエージェントに頼んだ。返ってきたのはこれだ：

```
# Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. ✅ done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.
```

読んだ感じは問題なさそうだ。だがこのとおりにやると、コピーする前に、すべてのアバターを削除してしまう。

## 6 つのステップ

**1. 見出しだけを読む。**（約 1 分）アウトラインは頼んだ内容と一致しているか。ここでは Goal、Steps、Status。既存のリンクを壊さないでほしいと頼んだのに、古いリンクや、変更を取り消す方法についての見出しがない。これが最初のコメントになる。

ターミナルから `grep -n '^#' plan.md` を実行すれば、見出しだけが表示される。多くのエディタにもアウトライン表示がある。MarsDawn では、サイドバーのアウトラインタブ（表示 ▸ サイドバーを表示、⌃⌘S）に見出しが並び、クリックするとそこへ移動する。

**2. 「完了」「合格」「検証済み」と書かれている箇所をすべて見つけ、そのうち 1 つを自分で確認する。**（約 1 分）ファイルを開く、テストを実行する、行数を数える。Chip Huyen は、こんな失敗を描いている：「The agent is convinced that it’s accomplished a task when it hasn’t.」（エージェントは、実際には終わっていないのに、タスクを終えたと確信している。）彼女の例では、50 人を 30 部屋に割り振るよう頼まれたエージェントが、40 人しか割り振らないまま、終わったと言い張る。

```
grep -n -i -E 'done|pass|verified|✅' plan.md
```

この例では「✅ done」と「All tests pass.」が見つかる。どのテストか？ アバターに触れるものはあるか？ 自分で実行するか、聞いてみる。この作業を MarsDawn が代わりにやることはできない。あなた以外、誰にもできない。

**3. 取り消せないステップを探す。**（約 1 分）データの削除、マイグレーション、force push、何かを送信・支払い・公開する処理。それらはあなたの明示的な OK を待つべきだ。Chip Huyen は、同じ考えをシステム側の視点からこう述べている：「If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.」（計画にリスクのある操作、たとえばデータベースの更新やコード変更のマージが含まれる場合、システムは実行前に明示的な人間の承認を求めることも、それらの操作の実行自体を人間に委ねることもできる。）この例では、ステップ 4 が元のファイルを削除し、それがステップ 5 のコピーより前に来ている。

**4. 図はレンダリングした状態で読み、矢印の 1 つひとつを本文と照らし合わせる。**フローチャートが「copy → verify → delete」と描いているのに、ステップの記述がそうなっていなければ、それ自体が発見だ。この計画には図がないので、今日は飛ばしてよい。図があるときは、Mermaid のソースではなく、描画された絵を見よう。多くのエディタにプレビュー機能があり、[「Mac で Markdown を見る方法」](/ja/view-markdown-on-mac/)と[「他のツールで Markdown を見る場合との比較」](/ja/vs/markdown-preview-tools/)で選択肢を紹介している。MarsDawn では、レンダリングされた図がソースの隣にあり（⌘2）、図が壊れていればソースとエラーが一緒に表示される。それ自体、コメントに値する。

**5. 計画が触れるファイルとシステムを列挙し、頼んでいないことがあれば確認する。**（4 と 5 を合わせて約 1 分）ここでは、ストレージの設定、テンプレート、サーバー上のフォルダ、バケット。そのバケットは誰が読めるのか？ 公開すべきだとは頼んでいない。MarsDawn でエージェントの作業フォルダを開いていれば（「ファイル ▸ フォルダを開く⋯」、⇧⌘O）、エージェントが書いた新しいファイルは 1 秒ほどでファイルタブに現れ、ヘッダーに git のブランチや worktree の名前が出るので、自分がどのチェックアウトをレビューしているか分かる。

**6. フィードバックは「場所・問題・直し方」で、1 行に 1 つの問題だけを書く。**（最後の 1 分）

```
plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.
```

行番号のあるエディタなら何でもいい。MarsDawn では、「編集 ▸ 参照をコピー」（⌥⌘C）でいまいる場所を `plan.md:10` の形でコピーでき、「AI 用にコピー」（⌃⌥⌘C）はその下に選択したテキストを付け加える。

## 1 分しかないなら

ステップ 2 をやろう。終わったと思い込んでいるエージェントが見つかるのは、たいていそこだ。

## 5 分では足りないとき

あるステップが正しいかどうか、あなたには判断できないこともある。それがあなたの知識の外にあるからだ。Jess Ou は、LangChain の 2026 年のエージェント解説記事で、2 文でこう言い切っている：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（評価できない判断を、外部に委ねてはいけない。正しい答えを自分が見分けられないなら、エージェントにも見分けられない。）私たちの受け止め方：あるステップを判断できないなら、それは早く承認する理由にはならない。分かる人に聞く理由になる。

## ここで MarsDawn がすること、しないこと

MarsDawn の中に AI モデルはない。この計画の問題を見つけたりはせず、ステップ 2 や 3 を代わりにやることもない。作業中、ファイルを読みやすく保つだけだ：ステップ 1 にはアウトライン、ステップ 4 には描画された図、ステップ 5 にはファイルタブ、ステップ 6 には行の参照。読んでいる途中でエージェントが計画を修正しても、MarsDawn は再読み込みしつつ、あなた自身に未保存の編集がなければ、読んでいた位置を保つ。

計画が固まり、ほかの人にも見せる必要が出てきたら、[「書き出した PDF を共有する」](/ja/sharing-exported-pdfs/)と[「Markdown から PDF へ」](/ja/markdown-to-pdf/)が、PDF として渡す方法を扱っている。

## 試してみる

MarsDawn は近日 Mac App Store に登場予定です。無料の `marsdawn` コマンドラインツールは今日から使えます：

```
brew install redtear1115/tap/marsdawn
```

アプリなしで Markdown を PDF に書き出せます。

[コマンドライン](/ja/cli/) · 購入前に：[MarsDawn ができないこと](/ja/limits/)

## 次に

- そもそもエージェントの出力がなぜ読みにくいか：[エージェントが返してくるものを読む](/ja/reading-agent-output/)。
- なぜエージェントはそもそも計画を示すのか：[Anthropic はエージェントに透明性を求めた。では誰がそれを読むのか？](/ja/agent-transparency/)
- エージェントが返すのは計画だけではない：[4 つのエージェント設計パターンと、それぞれが返す文書](/ja/agent-design-patterns/)。

## 出典

- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou, “What is an AI agent?,” LangChain, July 31, 2026: [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

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
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
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
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
