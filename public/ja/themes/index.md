# 4種類のテーマを内蔵。ギャラリーにはさらに多く。

MarsDawn には 夜明け、クラシック、モダン、ビビッド の4種類のプレビューテーマが内蔵されており、それぞれライトとダークの配色があります。バージョン 1.1 からはアプリ内のテーマギャラリーからさらに追加でき、Finder のクイックルックでも選んだテーマで書類が表示されます。

## 4種類のテーマ

- ![夜明けテーマの分割表示：左に Markdown のソース、右にレンダリングされたページ。](/assets/screens/01-split-800.png) **夜明け（デフォルト）**
- ![クラシックテーマ。プレビューがウインドウ全体に表示されています。](/assets/screens/02-classic-800.png) **クラシック**
- ![ビビッドテーマの分割表示。](/assets/screens/04-vivid-800.png) **ビビッド**
- ![ダークモードの MarsDawn、分割表示。](/assets/screens/03-dark-800.png) **ダークモード**

モダンのスクリーンショットはまだありません。4枚目はダークモードです。

- **夜明け**、デフォルト：このサイトと同じ、温かみのある紙の質感と Mars Rust のアクセントカラー。
- **クラシック**：より素朴で、紙の文書らしい配色。
- **モダン**：より涼しげで、現代的な配色。
- **ビビッド**：より明るく、コントラストの高い配色。

それぞれ独自のライトとダークの配色を持つので、Mac の外観を切り替えると、インターフェースの色だけでなくテーマの配色自体も切り替わります。

## アプリ内のテーマギャラリー

MarsDawn で「設定 ▸ 外観モード」を開き、「テーマを追加…」をクリックします。テーマギャラリーは開いたときに一覧を読み込みます。オンラインになるのは開いているあいだだけで、接続がないときは通知を表示し、内蔵の4つのテーマはそのまま使えます。

- 「インストール」は「ライトテーマ」と「ダークテーマ」の選択メニュー、および「表示 ▸ プレビューのテーマ」にテーマを追加します。「取り除く」で削除します。
- 「テーマのアップデートを確認」は、新しいバージョンがないかギャラリーに再度問い合わせます。
- テーマの用途で絞り込めます：エージェント出力のレビュー、技術ドキュメント、フォーマルな出力、メモ・共有。
- 「テーマを報告…」は、入力済みの GitHub issue または私たち宛てのメールを開きます。

## ギャラリーにあるテーマ

現在は8つのテーマがあり、すべて私たちが作成・レビューしたものです。よく知られた配色を基に読みやすく調整した Dracula、Gruvbox、Nord、Solarized に加え、ユーザーガイド、予算表、PRD、スプリントノート向けに作られた Guide、Ledger、Spec、Story を揃えています。

## レビュー済みで、中身はデータのみ

すべてのテーマは、ギャラリーに表示される前に私たちがレビューしてマージしています。テーマは色といくつかの範囲が限られたオプションだけを収めた小さな JSON ファイルです。スクリプトも CSS も作者の画像も含まれず、MarsDawn はインストール前にすべての値を検証します。報告されたテーマは24時間以内にギャラリーから取り下げられます。有害なテーマであった場合は、次にギャラリーを開いたときにインストール済みの Mac からも削除され、使用中だった場合は夜明けに戻ります。

ギャラリーが通信するのは `marsdawn.southern-light.dev/themes/v1/` のみで、ギャラリーを開くとき、アップデートを確認するとき、またはテーマをインストールするときに限られます。アカウント、識別子、Cookie、書類の内容は一切送信しません。

## クイックルックにも選んだテーマを反映

Finder で Markdown ファイルを選んでスペースキーを押します。クイックルックは、インストールしたテーマも含めてあなたが選んだテーマでファイルを表示し、MarsDawn の「外観モード」の設定に従います。「ライト」と「ダーク」は選んだまま固定され、「システム」は Mac に合わせます。

## PDF 書き出しとプリント

PDF に書き出す、またはプリントすると、ページには「ライト」に選んだテーマが使われます。Mermaid の図はそこに描き込まれ、コードブロックはハイライトを保ち、改ページは見出しをそのセクションから切り離したり、表や図を途中で切ったりしないよう配慮されます。無料の[marsdawn コマンドラインツール](/ja/cli/)も同じ書き出しエンジンを使い、`--theme` で4つの内蔵テーマのどれでも指定できます。

## ページをプリントしたあと

プリントしたページを囲んで会議をし、余白にペンで書き込み、紙の記録をファイルに綴じる。

[MarsDawn の動画（88 秒）](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## 自分のテーマを作る

[ブラウザでテーマを作れます](/ja/themes/new/)：色といくつかのスタイルオプションを選び、その場で反映を確認して、レビュー用に GitHub の issue として送信します。GitHub アカウントは必要ですが、インストールも git も不要です。送信しただけでは公開されず、私たちがレビューしてマージしたあとにのみ[ギャラリー](/ja/themes/gallery/)に表示されます。

エージェントと作業していますか？[エージェントにテーマを作らせて](/ja/themes/agents/)、ブラウザで整えましょう。

## 次に

- コマンドラインからの、完全な PDF 書き出しの手順：[Markdown から PDF へ](/ja/markdown-to-pdf/)。
- MarsDawn がまだできないこと：[その一覧](/ja/limits/)。
- Markdown を使わない人に、書き出した PDF を渡す：[PDF を共有する](/ja/sharing-exported-pdfs/)。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown・JSON・YAML を確かめる Mac ネイティブアプリ。ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF。無料で試せて、一度だけ USD 4.99。
- [機能一覧](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown・JSON・YAML エディタ：リアルタイムプレビュー、Mermaid と数式、テーマ、会議や保管に使える PDF とプリントのページ。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックを分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad では編集不可、プラグインなし、アカウントなし。テーマは変更できますが、カスタム CSS は使えません。購入前に知っておいてください。
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
- [English](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 內建四種預覽主題，各有淺色與深色；在 Mac 版 MarsDawn 的設定裡打開主題庫，還能安裝更多。快速查看也會用你選的主題。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 内置四种预览主题，各有浅色与深色；在 Mac 版 MarsDawn 的设置里打开主题图库，还能安装更多。快速查看也会用你选的主题。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/index.md): Vier integrierte Vorschauthemen in Hell und Dunkel sowie eine kuratierte Galerie in den Einstellungen von MarsDawn für Mac. Die Übersicht nutzt das Thema.
- [Français](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu intégrés, chacun clair et sombre, et une galerie vérifiée dans les réglages de MarsDawn pour Mac. Coup d’œil utilise votre thème.
- [Español](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa integrados, en claro y oscuro, y una galería revisada que abres desde Ajustes en MarsDawn para Mac. Vista rápida usa tu tema.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크를 각각 갖춘 기본 미리보기 테마 네 가지와, Mac용 MarsDawn 설정에서 여는 엄선된 테마 갤러리. 훑어보기도 고른 테마를 씁니다.
