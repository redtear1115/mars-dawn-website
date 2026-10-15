# 和你的 agent 一起做主題

給製作 MarsDawn 預覽主題的 AI agent 的參考。agent 寫出一個 `theme.json`，用 `marsdawn` 命令列工具檢查並渲染，再把連結交給你。你在[打造一個主題](/zh-hant/themes/new/)頁面用眼睛調整，然後投稿。下面的欄位表直接讀自 kit 的原始碼，並有檢查確保兩者一致。

**寫出一個 `theme.json`，反覆執行 `marsdawn theme validate theme.json --require-complete --json` 直到結束代碼為 0，用 `marsdawn theme preview` 分別渲染淺色與深色，再把連結交給使用者。**主題只有參數，不含任何 CSS。

## 主題是什麼

- **顏色**，淺色與深色各一組：基本色盤，以及選填的語法與圖表顏色。每個顏色都是 `#RRGGBB`。
- **字型設計**：`sans`、`serif` 或 `rounded`。
- **一組封閉的樣式選項**：數字落在固定範圍內，選擇來自固定清單。樣式選項裡的顏色一律是像 `accent` 這樣的色盤角色，不能是顏色字面值。
- **顯示字串**：名稱與摘要，以及選填的作者與授權。

不在下面表格裡的鍵是錯誤，同一個鍵寫兩次也是。檔案最大 16,384 位元組。

## 檢查與渲染

在放有 `theme.json` 的資料夾裡執行這些指令。需要 `marsdawn` 工具：見[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)。

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- 離開代碼：0 表示有效，1 表示無效並列出規則 id，2 表示找不到檔案，64 表示用法錯誤。`preview` 另外有 4（PNG 已存在，傳入 `--force` 或換個檔名）和 5（渲染失敗）。
- 加上 `--json` 時，無效的主題會把問題列在 `issues` 下，每一項都有 `rule` id、`path` 和 `message`。修正後再跑一次。
- `--require-complete` 是要發布的主題用的檢查：它還要求兩組色盤都有 `syntax` 與 `diagram` 顏色。
- `css` 印出預覽使用的 CSS，`preview` 把範例文件渲染成 PNG。兩者都會先驗證，所以無效的主題什麼都不會渲染。
- 交出主題之前，先看過淺色與深色兩張 PNG。

## 從內建主題開始

複製四個內建主題之一再修改。每一個都是完整且有效的檔案：

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): 預設主題，也是下面的範例
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): 較素雅、像文件的色盤
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): 較冷調、較現代的色盤
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): 較明亮、對比較高的色盤

### 範例：Dawn

這是 `dawn.json`，一個位元組都沒改。它唯一的樣式選項是 `hr` 的一條細的強調色分隔線。

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

## 欄位

下面每個物件都用同樣的方式讀取。`required` 表示這個鍵必須存在，沒有列出的鍵都是錯誤。

型別：`string`、`integer`、`number`、`boolean`、`map`（語言標籤對應文字）、`enum`（列出的值之一）、`role`（色盤角色）和 `object`（連到它的表格）。型別後面的 `[]` 表示清單。

### `theme.json`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | 固定是 `1`。 |
| `id` | `string` | `required` | 1 到 32 個字元：小寫字母與數字，以單一連字號連接成段，例如 `calm-green`。 |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`，例如 `1.0.0`。 |
| `name` | `map` | `required` | 語言標籤對應文字。`en` 必填，其他鍵是像 `zh-Hant` 的語言標籤。每段文字最多 48 個字元，不可含連結或換行。 |
| `summary` | `map` | `required` | 和 `name` 的形式相同，每段文字最多 120 個字元。 |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — 一個或兩個，不可重複。它們決定主題必須達到多高的對比。 |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | SPDX 識別碼，例如 `Apache-2.0`。投稿的主題以 Apache-2.0 釋出。 |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `name` | `string` | `required` | 最多 64 個字元，不可含連結。 |
| `github` | `string` | `optional` | GitHub 帳號。投稿時請填投稿者自己的帳號。 |

### `light, dark`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `background` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `surface` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `text` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `muted` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `border` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `heading` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `accent` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `link` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `quote` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `syntax` | `object` | `optional` （發布時必填，用 `--require-complete` 檢查） | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` （發布時必填，用 `--require-complete` 檢查） | [`diagram`](#t-diagram-colors) |

### `syntax`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `string` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `comment` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `number` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `function` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `type` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |

### `diagram`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `node` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `nodeBorder` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `text` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `line` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `secondary` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `tertiary` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |
| `note` | `string` | `required` | `#` 加六個十六進位數字，例如 `#1C1C1C`。 |

### `style`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [範圍](#t-numbers) |
| `lineHeight` | `number` | `optional` | [範圍](#t-numbers) |
| `headingWeight` | `number` | `optional` | [範圍](#t-numbers) |
| `radius` | `number` | `optional` | [範圍](#t-numbers) |
| `maxWidth` | `number` | `optional` | [範圍](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [色盤角色](#roles) |
| `inlineCode` | `role` | `optional` | [色盤角色](#roles) — 只能是 `text` 或語法角色：`keyword`、`string`、`comment`、`number`、`function` 或 `type`。 |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `size` | `number` | `optional` | [範圍](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [範圍](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [範圍](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| 欄位 | 型別 | 必填與否 | 值與備註 |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### 帶 type 的選項

這些樣式選項是帶有 `type` 的物件。每個 `type` 只接受為它列出的欄位，其他都不行。

| 選項 | type | 欄位 | 必填與否 | 型別 |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [範圍](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [範圍](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` 兩個或三個角色。 |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### 色盤角色

色盤角色是下列名稱之一：

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### 數字

數字會先對齊到最接近的間隔倍數，再檢查是否落在最小值與最大值之間，否則規則是 `number.range`。

| 欄位 | 最小值 | 最大值 | 間隔 |
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

## 還會檢查什麼

- **對比。**預覽畫出的每一組顏色配對，例如 `background` 上的 `text`，文字要達到 4.5:1，線條與其他非文字要達到 3:1。你列出的情境會把部分顏色提高到 4.5:1。訊息會指出是哪一組配對、它的比值和需要的比值。
- **字串。**名稱、摘要或作者名稱若是空的、太長，或含有連結、控制字元、不可見或雙向格式字元，都會被拒絕。
- **規則 id。**每個問題都帶一個，例如 `contrast.pair`、`color.hex`、`number.range`、`id.pattern`、`schema.unknownKey` 或 `palette.incomplete`。依 id 與 `path` 的說明修正檔案。

## 用連結交給人

[打造一個主題](/zh-hant/themes/new/)頁面可以從連結開啟主題，讓人用眼睛調整。連結是該頁的網址，接著 `#theme=`，再接檔案位元組的 base64url（不含補位）。檔案最大 16,384 位元組。下面這一行指令在 macOS 與 Linux 的 zsh 和 bash 都能產生連結：

```
printf 'https://marsdawn.southern-light.dev/zh-hant/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

主題跟在 `#` 後面，瀏覽器不會把它送給網站，網站也不會把它送到任何地方。連結確實會留在你的 shell 歷史與瀏覽器歷史裡，你貼給誰，誰就能讀到這個主題。

## 投稿

agent 準備檔案與連結，由人來投稿。兩條路都會要求 Developer Certificate of Origin 與 Apache-2.0 授權聲明，這個聲明由人本人做出：agent 不會替他勾選方框或簽署。

- **Issue。**人開啟連結，在「打造一個主題」頁面按下 **Submit**，或是開啟 [issue 表單](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml)，把 JSON 貼進 *Theme*。接著有工作流程檢查主題並回覆。
- **Pull request。**只改 `themes/<id>/theme.json`，把 `author.github` 設為 pull request 作者的帳號，每個 commit 都用 `git commit -s` 簽署。規則在 [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md)。

投稿主題的作者名稱、名稱、摘要與 GitHub 帳號會永久公開，所以請把 `author.name` 設成人願意公開的名字。

## 已發布的主題

想看已發布的主題長什麼樣子，可以逛逛[主題庫](/zh-hant/themes/gallery/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號。內建四種主題，主題庫還有更多。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Mac 怎麼開 md 檔](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。在瀏覽器裡打造自己的主題，也可以逛逛社群主題庫。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽社群投稿的 MarsDawn 預覽主題，依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造一個自己的主題，不用安裝，也不用 git。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [讀懂 agent 交回來的 Markdown](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [編者的閱讀筆記](https://marsdawn.southern-light.dev/zh-hant/reading-notes/index.md): 六篇短筆記，談打造 AI agent 的人實際主張了什麼——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 與 Andrew Ng——以及這些主張對「要讀 agent 交回來的東西」的人分別意味著什麼。
- [閱讀筆記：Anthropic](https://marsdawn.southern-light.dev/zh-hant/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月發表的指南把 workflow 和 agent 分開來看，並描述了五種 workflow 模式，其中一種讓另一次 LLM 呼叫來審查。這對落進你資料夾的東西來說，意味著什麼。
- [閱讀筆記：Chip Huyen](https://marsdawn.southern-light.dev/zh-hant/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章裡，把 agent 的動作分成 read-only 和 write action 兩種。這個分法為什麼是核準計畫前，快速拓出該多看一眼的那一行的好方法。
- [閱讀筆記：Lilian Weng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被廣泛引用的整理，把 LLM agent 描述成大腦加上規劃、記憶、工具使用。每個部件通常會留給你讀什麼，以及她點名的一個限制：計畫遇到意外不太會調整。
- [閱讀筆記：Harrison Chase](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [閱讀筆記：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [閱讀筆記：Andrew Ng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI agent 的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
