# エージェントとテーマを作る

MarsDawn のプレビューテーマを作る AI エージェント向けの参考資料です。エージェントは `theme.json` を1つ書き、コマンドラインツール `marsdawn` で検証してレンダリングし、リンクを渡します。人は[テーマビルダー](/ja/themes/new/)で見た目を整えて投稿します。下のフィールド表は kit のソースコードから直接読み取ったもので、チェックによって一致が保たれています。

**`theme.json` を書き、終了コードが 0 になるまで `marsdawn theme validate theme.json --require-complete --json` を実行し、`marsdawn theme preview` でライトとダークをレンダリングしてから、人にリンクを渡します。**テーマはパラメーターだけで、CSS は含みません。

## テーマとは

- ライトとダークそれぞれの**色**：基本パレットと、任意の構文色・ダイアグラム色。どれも `#RRGGBB` です。
- **フォントデザイン**：`sans`、`serif`、`rounded` のいずれか。
- **閉じたスタイルオプションの集合**：決まった範囲の数値と、決まったリストから選ぶ値。スタイルオプションの色は常に `accent` のようなパレットのロールで、色の値を直接書くことはありません。
- **表示用の文字列**：名前と概要、任意で作者とライセンス。

下の表にないキーはエラーで、同じキーを2回書くこともエラーです。ファイルは最大 16,384 バイトです。

## 検証とレンダリング

`theme.json` のあるフォルダーで実行します。`marsdawn` ツールが必要です。[AI エージェント向け marsdawn](/ja/cli/agents/)を参照してください。

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- 終了コード：0 は有効、1 は無効（ルール ID 付き）、2 はファイルが見つからない、64 は使い方の誤りです。`preview` にはさらに、PNG がすでにある場合の 4（`--force` を付けるか別の名前にします）と、レンダリング失敗の 5 があります。
- `--json` を付けると、無効なテーマは問題を `issues` の下に並べ、それぞれに `rule` ID、`path`、`message` が付きます。直して再実行してください。
- `--require-complete` は公開するテーマ向けのチェックで、両方のパレットに `syntax` と `diagram` の色も求めます。
- `css` はプレビューが使う CSS を出力し、`preview` はサンプル文書を PNG にレンダリングします。どちらも先に検証するので、無効なテーマはレンダリングされません。
- テーマを渡す前に、ライトとダークの PNG を両方確認してください。

## 組み込みテーマから始める

4つの組み込みテーマのどれかをコピーして変更します。どれも完全で有効なファイルです。

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): 既定のテーマで、下の例
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): より落ち着いた、文書らしいパレット
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): より涼しげで現代的なパレット
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): より明るくコントラストの強いパレット

### 例：Dawn

`dawn.json` を1バイトも変えずに載せています。スタイルオプションは `hr` の細いアクセントカラーの線だけです。

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## フィールド

下のオブジェクトはどれも同じように読まれます。`required` はキーが必須という意味で、載っていないキーはエラーです。

型：`string`、`integer`、`number`、`boolean`、`map`（言語タグからテキストへ）、`enum`（挙げた値のいずれか）、`role`（パレットのロール）、`object`（リンク先の表）。型の後ろの `[]` はリストを表します。

### `theme.json`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | 常に `1`。 |
| `id` | `string` | `required` | 1〜32文字：小文字と数字を、単独のハイフンでつないだ区切り。例：`calm-green`。 |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`。例：`1.0.0`。 |
| `name` | `map` | `required` | 言語タグからテキストへ。`en` は必須で、ほかのキーは `zh-Hant` のような言語タグです。各テキストは最大48文字で、リンクや改行は使えません。 |
| `summary` | `map` | `required` | `name` と同じ形式で、テキストごとに最大120文字。 |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — 1つまたは2つ、重複不可。テーマが満たすべきコントラストの水準を決めます。 |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | SPDX 識別子。例：`Apache-2.0`。投稿されたテーマは Apache-2.0 で公開されます。 |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `name` | `string` | `required` | 最大64文字、リンク不可。 |
| `github` | `string` | `optional` | GitHub のログイン名。投稿の場合は、投稿する人のものを入れます。 |

### `light, dark`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `background` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `surface` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `text` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `muted` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `border` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `heading` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `accent` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `link` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `quote` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `syntax` | `object` | `optional` （公開には必須。`--require-complete` で検証） | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` （公開には必須。`--require-complete` で検証） | [`diagram`](#t-diagram-colors) |

### `syntax`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `string` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `comment` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `number` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `function` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `type` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |

### `diagram`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `node` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `nodeBorder` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `text` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `line` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `secondary` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `tertiary` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |
| `note` | `string` | `required` | `#` と16進数6桁。例：`#1C1C1C`。 |

### `style`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [範囲](#t-numbers) |
| `lineHeight` | `number` | `optional` | [範囲](#t-numbers) |
| `headingWeight` | `number` | `optional` | [範囲](#t-numbers) |
| `radius` | `number` | `optional` | [範囲](#t-numbers) |
| `maxWidth` | `number` | `optional` | [範囲](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [パレットのロール](#roles) |
| `inlineCode` | `role` | `optional` | [パレットのロール](#roles) — `text` か構文ロールのみ：`keyword`、`string`、`comment`、`number`、`function`、`type`。 |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `size` | `number` | `optional` | [範囲](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [範囲](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [範囲](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| フィールド | 型 | 必須か | 値と備考 |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### type を持つオプション

これらのスタイルオプションは `type` を持つオブジェクトです。それぞれの `type` は、そこに挙げたフィールドだけを受け付けます。

| オプション | type | フィールド | 必須か | 型 |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [範囲](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [範囲](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` ロールを2つまたは3つ。 |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### パレットのロール

パレットのロールは次の名前のいずれかです。

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### 数値

数値は最も近い刻みの倍数に丸められ、最小と最大の間に収まる必要があります。収まらない場合のルールは `number.range` です。

| フィールド | 最小 | 最大 | 刻み |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## ほかに検証されること

- **コントラスト。**`background` 上の `text` のように、プレビューが描く色の組はすべて、テキストは 4.5:1、線やそのほかの非テキストは 3:1 に達する必要があります。指定したシナリオによって、一部の色は 4.5:1 に引き上げられます。メッセージには、その組と比率、必要な比率が示されます。
- **文字列。**名前、概要、作者名が空、長すぎる、またはリンク・制御文字・不可視文字・双方向書式文字を含む場合は拒否されます。
- **ルール ID。**すべての問題には `contrast.pair`、`color.hex`、`number.range`、`id.pattern`、`schema.unknownKey`、`palette.incomplete` などの ID が付きます。ID と `path` が示すとおりにファイルを直してください。

## リンクとして渡す

[テーマビルダー](/ja/themes/new/)は、リンクからテーマを開けるので、人が見た目を整えられます。リンクは、ビルダーのアドレス、`#theme=`、パディングなしの base64url にしたファイルのバイト列でできています。ファイルは最大 16,384 バイトです。次の1行で、macOS と Linux の zsh と bash でリンクを作れます。

```
printf 'https://marsdawn.southern-light.dev/ja/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

テーマはブラウザーがサイトに送らない `#` の後ろに入り、サイトもそれをどこにも送りません。ただしリンクはシェルとブラウザーの履歴に残り、リンクを貼った相手はテーマを読めます。

## 投稿する

エージェントがファイルとリンクを用意し、投稿は人が行います。どちらの方法でも Developer Certificate of Origin と Apache-2.0 での公開への確認が必要で、この確認は人が自分で行います。エージェントがチェックボックスにチェックしたり、代わりに署名したりすることはありません。

- **Issue。**人がリンクを開いてテーマビルダーの **Submit** を押すか、[Issue フォーム](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml)を開いて JSON を *Theme* に貼り付けます。ワークフローがテーマを検証して返信します。
- **Pull request。**`themes/<id>/theme.json` だけを変更し、`author.github` を pull request の作者のログイン名にして、すべてのコミットに `git commit -s` で署名します。ルールは [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md) にあります。

投稿されたテーマの作者名、名前、概要、GitHub のログイン名は永久に公開されます。`author.name` には、その人が公開してよいと考える名前を入れてください。

## 公開されているテーマ

公開されているテーマの見た目は、[テーマギャラリー](/ja/themes/gallery/)で確認できます。

## その他

- [MarsDawn](https://marsdawn.southern-light.dev/ja/index.md): エージェント開発の舵を取る人のための Markdown。ライブプレビュー、Mermaid 図、PDF 書き出しに対応したネイティブ Mac 向けエディタです。Mac App Store で配信中です。
- [あなたの文章は Mac に残ります](https://marsdawn.southern-light.dev/ja/yours/index.md): MarsDawn にはアカウントも同期もクラウドもありません。Markdown 文書はあなたの Mac 上に、選んだファイルとフォルダの中に残ります。
- [無料で試して、一度だけ購入](https://marsdawn.southern-light.dev/ja/pay-once/index.md): MarsDawn は無料でダウンロードできます。14日間すべての機能を試したあと、USD 4.99 の一度だけの購入でロックを解除できます。サブスクリプションもアカウントも不要です。
- [PDF 書き出し](https://marsdawn.southern-light.dev/ja/pdf/index.md): Mac で Markdown を PDF に書き出したりプリントしたりできます。Mermaid 図やハイライトされたコードにも対応。改ページは短いコードブロックや表を分断しないよう配慮されます。
- [Mac アプリ](https://marsdawn.southern-light.dev/ja/native/index.md): 本物の Mac アプリである Markdown エディタ。ネイティブなウインドウとタブ、自動保存、バージョン履歴、Finder のクイックルック、Mac らしく動くテキストエディタ。
- [MarsDawn ができないこと](https://marsdawn.southern-light.dev/ja/limits/index.md): 同期なし、iPhone・iPad アプリなし、プラグインなし、アカウントなし。組み込みテーマは4種類で、テーマギャラリーにはさらに多くあります。購入前に知っておいてください。
- [サポート](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [プライバシーポリシー](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Mac で Markdown を見る](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): .md ファイルは書式記号が入ったプレーンテキストです。Mac でレンダリングして読む方法を紹介します。今すぐ使える無料の marsdawn コマンドラインツールで PDF にする方法と、Mac App Store で配信中の MarsDawn アプリで読む方法です。
- [Markdown から PDF へ](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールしてコマンド1つで実行：表、数式、Mermaid、コードに対応。
- [MacMD Viewer と MarsDawn](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [コマンドライン](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [AI エージェント向け marsdawn](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [エージェント用スキル](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [MCP サーバー](https://marsdawn.southern-light.dev/ja/cli/mcp/index.md): marsdawn には自前の AI モデルがないので、どのエージェントが書いた Markdown かは関係ありません。CLI、skill ファイル、marsdawn-mcp という MCP サーバーのいずれからでも呼び出せ、三つとも同じ export を実行します。
- [トークンを抑えたレビュー](https://marsdawn.southern-light.dev/ja/token-efficient-review/index.md): 人が MarsDawn でレンダリングされたページを読みます。それがエージェントの context に読み戻されることはありません。ツール呼び出し自体も、レンダリングされた内容ではなく簡潔な JSON 結果を返すので、呼び出し自体も安上がりです。
- [他のツールで Markdown を見る場合との比較](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
- [プレビューテーマと PDF 書き出し](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを持つ4種類のプレビューテーマと、今見ているテーマに合わせた1つの PDF・プリント書き出し。ブラウザで自分のテーマを作り、コミュニティギャラリーも閲覧できます。
- [テーマを作る](https://marsdawn.southern-light.dev/ja/themes/new/index.md): 配色といくつかのスタイルオプションを選ぶと、サンプル文書にその場で反映されます。できあがったテーマは GitHub の issue として送信できます。インストールも git も不要です。
- [テーマギャラリー](https://marsdawn.southern-light.dev/ja/themes/gallery/index.md): コミュニティが投稿した MarsDawn のプレビューテーマを閲覧し、シナリオで絞り込み、問題があれば通報できます。ブラウザで自分のテーマを作れます。インストールも git も不要です。
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
- [読書ノート：Andrew Ng](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [テンプレート](https://marsdawn.southern-light.dev/ja/templates/index.md): エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。
- [仕様書テンプレート](https://marsdawn.southern-light.dev/ja/templates/spec/index.md): 要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。
- [フローチャートテンプレート](https://marsdawn.southern-light.dev/ja/templates/flowchart/index.md): Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。
- [議事録テンプレート](https://marsdawn.southern-light.dev/ja/templates/meeting-notes/index.md): 決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): A reference for AI agents that make a MarsDawn theme: every theme.json field with its type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit it.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的參考：做一個 MarsDawn 主題所需的 theme.json 每個欄位與型別、範圍，檢查並渲染它的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI agent 的参考：做一个 MarsDawn 主题所需的 theme.json 每个字段与类型、范围，检查并渲染它的 CLI 流程、交给人的链接，以及怎么投稿。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): Eine Referenz für KI-Agenten, die ein MarsDawn-Thema erstellen: jedes Feld der theme.json mit Typ und Wertebereich, die CLI-Schleife zum Prüfen und Rendern, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Une référence pour les agents IA qui créent un thème MarsDawn : chaque champ de theme.json avec son type et sa plage, la boucle CLI qui le vérifie et le rend, un lien de transmission et la façon de le soumettre.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Una referencia para agentes de IA que crean un tema de MarsDawn: cada campo de theme.json con su tipo y su rango, el ciclo de la CLI que lo comprueba y lo renderiza, un enlace de entrega y cómo enviarlo.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, 검사하고 렌더링하는 CLI 절차, 사람에게 넘기는 링크, 제출 방법을 담았습니다.
