# ある Mac で通るテストが、思っているものをテストしているとは限りません。

バイブコーディング（vibe coding）は悪いことではなく、MarsDawn もエージェントと一緒に作っています。ただ、人が長く頼るソフトウェアを支えるのは、最初のバージョンのあとの何年にもわたるメンテナンスと安全であり、その出発点は、変更が何も壊していないと確かめることです。

**あるテストが Mac mini では通り、MacBook Air では失敗しました。製品に問題はありませんでした。テストが画面のカラープロファイルを通して色を読んでいて、Mac mini で通っていたのはたまたまでした。2 台目のマシンが見つけたのは、コードではなくテストのバグです。**

MarsDawn がどんな極端なファイルや悪意のあるファイルでテストされているかだけ知りたい方は、「[テストに投げ込むもの](#inputs)」へどうぞ。

## MacBook Air でだけ失敗したテスト

書き出しエンジンのテストを GitHub の macOS 15 ランナーで一通り実行すると、1 時間近くかかります。debug ビルドで約 32 分、release ビルドで約 25 分です。これを短くするため、macOS 26 の分を自前の MacBook Air に移してみました（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)）。

そこでの最初の実行で、テストがひとつ失敗しました。コールアウト（Note、Tip、Warning）を含む PDF を書き出し、それぞれの端にある色の帯が正しい色か、つまり色差が 0.16 未満かを確かめるテストです。MacBook Air での色差は 0.1634、0.1648、0.1796 でした。Mac mini では、同じコミット、同じ macOS と Xcode で、テストは通りました。

最初は書き出しが壊れたのだと思いました。違いました。PDF には何の問題もなく、2 台で違っていたのは、テストがそれを読む方法でした。

このテストは PDF の各ページを画像にしてピクセルを読みます。macOS はその画像を、メインディスプレイのカラースペースで描きます。Mac mini はふつうの外部ディスプレイにつながっていて、MacBook Air は内蔵ディスプレイを使っていました。1 色のオレンジで塗りつぶした画像を読み戻すと、(0.784, 0.278, 0.106) が Mac mini では (0.822, 0.335, 0.179)、MacBook Air では (0.782, 0.395, 0.221) になりました。

大事なのはここからです。Mac mini でも、テストは正しい色を読めていませんでした。ずれは最大 0.128 で、0.16 の上限にぎりぎり収まっていただけです。通っていたのはディスプレイのおかげで、帯の色を正しく測れていたからではありません。

修正（[kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)）で変えたのはテストだけです。ページを sRGB に固定したカラースペースの画像に描くので、画面はまったく関わりません。いまは 2 台とも帯の色を正確に読めます。色差は、MacBook Air の内蔵ディスプレイでも Mac mini でも 0.0 です。プルリクエストの CI は通り（[run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)）、修正が MacBook Air のランナー用ブランチに入ったあと、そのマシンでも全テストが通りました（[run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)）。そのあと、わざと失敗させました。期待する色をすべて青にすると、5 つのコールアウトすべてで赤になりました。

既知の穴もまだあります。Note と Caution は色差が約 0.119 の 2 つのオレンジを使っていて、0.16 の上限より内側です。この 2 色が入れ替わっても、テストはおそらく気づきません。テストが完全なふりはせず、このことを記録に残しました。

失敗しようのないテストは何も守りません。画面のカラープロファイルのような、間違った理由で失敗するテストも同じです。1 台のマシンでの緑は、そこでテストが通ったことを示すだけで、名前どおりのものを測っているという意味ではありません。

## テストは何層にも重ねた網

すべてを捕まえるテストはひとつもありません。層ごとに網目の違う網があり、ひとつをすり抜けた間違いは次の網にかかるはずです。

- **参照 PDF：**書き出しエンジン（オープンソースの [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)。`marsdawn` コマンドもこれで動いています）でサンプルの書類を書き出し、各ページのテキストを記録済みのものと比べます。内容が知らないうちに消えることや、ページ数が変わることを捕まえます。
- **異なるシステムとビルド：**エンジンは、サポートする最も古い macOS 15 と、アプリを出荷している macOS 26 の両方で、それぞれ debug と release のビルドとして実行します。アプリの全テストは 4 通りの組み合わせで実行します。署名ありと署名なし、それぞれペイウォールのオフとオンです。古いシステムでだけ、あるいはお客さまが実際に受け取るビルドでだけ壊れるものを捕まえます。
- **実機：**アプリの CI は自前の Mac（Mac mini と MacBook Air の両方）で動いています。エンジンのテスト一式をその MacBook Air で試したこと（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)、いまもオープンな実験ドラフト）が、上のカラープロファイルの不具合を捕まえました。2 台目のマシンは、そのマシンで動いているから通っているだけのテストを捕まえます。
- **赤になるべき対照群：**アプリの CI には、わざと壊したクリーンアップスクリプトのコピーが 22 個、テスト実行スクリプトのコピーが 20 個あり、それぞれ安全チェックがひとつずつ抜いてあります。テストはそのすべてで失敗しなければなりません。クリーンアップスクリプトは Mac から古いビルドや作業コピーを削除するので、チェックがひとつ欠けるだけで、消してはいけないものを消しかねません。壊したコピーがひとつでも通れば、壊れているのはテストのほうです。
- **もうひとつの目：**kit #242 のように、マージの前に別のエージェントに変更を検証させるのが私たちのやり方です。使い方の流れに関わる変更は、先にシナリオレビューを通します。「完了」と言いながら終わっていないことや、動くけれど使われる場面を間違えているコードを捕まえます。
- **マージするのは人です。**どの変更も MarsDawn の開発者本人が確認し、自分でマージします。エージェントやボットがマージすることはありません。

## テストに投げ込むもの

網が役に立つかどうかは、何を投げ込むかで決まります。エンジンのテストが与える入力の一部と、それぞれのテストが保証することです。

- **とても大きなファイル。**私たちのテストマシンで release ビルドを使って測ると、2 MB の書類は 1.5 秒以内に表示され、レイアウトしきれないほど複雑な 5 MB の書類も 1 秒以内にプレーンテキストとして開きます。16 MB を超えるものは、まったく解析せずにテキストとして表示します。
- **何十万もの行。**1 行 1 語で約 3 MB、80 万行近い書類は、途中で多すぎると判断されます。エンジンはそこで読むのをやめ、プレーンテキストとして表示します。
- **閉じない記号。**閉じのないブロックの開始記号が 1 MB 分あっても、何万層にも積み重なったブロックでも、同じ 1 MB のプレーンテキストのおよそ 2 倍より長くかかってはいけません。8 階層より深い部分は、それ以上入れ子になりません。
- **数式。**間違った数式は、ページを壊さずにその場所にエラーを表示します。10,000 文字を超える数式は書かれたまま残し、一度に描くのは書類の最初の 1,000 個までです。数式の中身がリンクや画像、ページのマークアップになることはありません。
- **Markdown に紛れ込んだ悪意のある HTML。**スクリプトは取り除かれ、実行されることはありません。埋め込みフレームも、ページに表示される前に取り除かれます。リモート画像は許可しないかぎり読み込まず、許可しても安全な（HTTPS の）ものだけを読み込みます。スクリプトのフィルタを外した対照用のコピーもあり、テストはそこで失敗しなければなりません。
- **悪意のあるテーマファイル。**拒否され、エラーメッセージがファイル内の隠れた制御文字やリンクを繰り返すこともありません。16 KB を超えるテーマファイルは読み込みもしません。

どれもただではありません。エンジン 1 回分の制限時間は 30 分から 45 分、50 分、70 分、いまは 90 分まで延びました。macOS 15 は全テストが通っていたのに 50 分の上限に 2 回達したことがあり、その後、それまでの手順はすべて通ったまま、最後の手順で 70 分に達したことがあります。

## まねできる 4 つの習慣

1. **書くエージェントと確かめるエージェントを分ける。**確かめる側には、書いたエージェントの説明は付けず、変更そのものと「完了」の条件を渡し、テストを自分で実行して、確かめなかったことを挙げてもらいます。kit #242 では、検証したエージェントが新しいテストを通す前に、MacBook Air で古いテストを実行して失敗するのを確かめました。かかるのは 2 つ目のセッションのトークン代です。
2. **どのテストも一度は失敗するのを見る。**緑に意味があるのは、確かめている対象が本当に間違っているときに、同じテストが赤になるのを見たことがある場合だけです。緑を信じる前に、そのテストが守っているものを壊して（またはエージェントに壊してもらって）赤になるのを見て、元に戻して緑になるのを見ます。エージェントは通るテストを書くのが得意です。だからこそ、失敗するところを見る必要があります。
3. **テストを 2 つ目の環境で実行する。**2 台目の Mac がなくてもかまいません。2 つの OS バージョン、あるいは debug ビルドと release ビルドの CI マトリクスで十分なスタートです。探すのは、偶然に通っているだけのテストです。
4. **「テストが 1 つも実行されなかった」を失敗として扱う。**Python 3.9 の `unittest` は、テストが 1 つも見つからなくても成功として終了します。パスを 1 文字打ち間違えただけで緑になるわけです。私たちの CI はテストの数を読んで 0 なら失敗にし、終了コードだけでなく、まとめに「0 failed」と書かれていることも確かめます。このチェックは、独立した検証で私たち自身の CI のこの穴が見つかってから加えたものです。

## まとめ

アプリがバイブコーディングで作られたかどうかより、誰かがテストとメンテナンスを続けているかどうかのほうが大事です。ソフトウェアを選ぶときに確かめる価値があります。テストのしかたを説明しているか。最後に更新されたのはいつか。

速さはエージェントに任せましょう。確認は、正しいものを測るテストと、結果を読む人に任せます。

## 次に

- エージェントが書いたものを、それでも人が読まなければならない理由：[AI の出力を人が確認する理由](/ja/reviewing-ai-output/)。
- エージェントが返してくる計画やレポートの読み方：[エージェントが返してくるものを読む](/ja/reading-agent-output/)。

## 出典

- 失敗したテストとその原因：[mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241)。
- 修正と独立した検証：[mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)。
- MacBook Air で CI を試した作業（オープンな実験ドラフト）と実行時間：[mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)。
- 書き出しエンジンの CI。制限時間の変遷はコメントにあります：[ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml)。
- アプリのリポジトリは非公開です。上のアプリに関する内容は、その CI ワークフローとテストスクリプトにもとづいています。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown を読んで確かめる Mac ネイティブアプリ。分割ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、解除は一度だけ USD 4.99。
- [機能一覧](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックを分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。テーマは変更できますが、カスタム CSS は使えません。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で .md ファイルを開く方法](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Mac で Mermaid をプレビューする](https://marsdawn.southern-light.dev/ja/mermaid-preview-mac/index.md): Mac で Mermaid の図を Markdown の隣に描画：リアルタイムプレビュー、クイックルック、PDF 書き出し。図に誤りがあると、エラーとその行が表示されます。
- [Markdown のクイックルック](https://marsdawn.southern-light.dev/ja/quicklook/index.md): MarsDawn のクイックルックなら、Finder でスペースキーを押すだけで Markdown を描画して表示します。Mermaid 図、KaTeX 数式、ハイライトされたコードにも対応。トライアル終了後も使えます。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MarsDawn と比較：VS Code プレビュー、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Mac向けMarkdownビューアのおすすめ8選（2026年）](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [テーマ](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを備えた4種類の内蔵プレビューテーマに加え、Mac 版 MarsDawn の設定から開ける厳選ギャラリーも。クイックルックにも選んだテーマが反映されます。
- [テーマを作る](https://marsdawn.southern-light.dev/ja/themes/new/index.md): 配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。
- [エージェントとテーマを作る](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [テーマギャラリー](https://marsdawn.southern-light.dev/ja/themes/gallery/index.md): 開発者がレビューした MarsDawn のプレビューテーマを閲覧し、シナリオで絞り込み、問題があれば通報できます。ブラウザで自分のテーマを作れます。インストールも git も不要です。
- [書き出した PDF を共有する](https://marsdawn.southern-light.dev/ja/sharing-exported-pdfs/index.md): エージェントの書いた Markdown を PDF に書き出し、Markdown を読まず何もインストールしない同僚に渡します。構文もアプリもアカウントも、開くのに一切不要です。
- [AI の出力を人が確認する理由](https://marsdawn.southern-light.dev/ja/reviewing-ai-output/index.md): AI が書いた Markdown も、結局は人が理解しなければなりません。読みやすいからといって鵜呑みにはできません。MarsDawn はレンダリングされたページとソースを並べ、Mermaid 図と KaTeX 数式を描画するので、構造が一目で分かります。
- [エージェントが返してくるものを読む](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [エージェントの透明性](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [エージェントの計画をレビューする](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [エージェント設計パターン](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [更新履歴](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [ロードマップ](https://marsdawn.southern-light.dev/ja/roadmap/index.md): Mac、iPhone、iPad 向け MarsDawn で開発中の機能と次に予定している機能を、バージョンごとにまとめました。日付は書かず、未定のものは明記しています。
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
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
