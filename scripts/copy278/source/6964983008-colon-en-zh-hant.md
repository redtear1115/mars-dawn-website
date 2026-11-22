## 結論

**`:::` 可以拿掉【待定】了。** #300 隨 Mac 1.2.2 上架（11/14）。查得到的範圍是：`:::info／success／warning／danger` 顯示成有色條的區塊，`:::spoiler` 顯示成可收合區塊，其他名稱或少結尾的 `:::` 照原文顯示。下面 §1 是 en／zh-Hant 各一句，**要 Ray 核准**。

**其餘版本宣稱重核過：** 頁面（en、zh-Hant 和六語）沒有任何一句提到開啟網址（#355）或圖片下載（#457）。兩張票都還開著、沒進 main，原本「不寫」維持。要改的只有備註和 claim-check 裡的 1.2.1 舊條件（§2）。

**沒查到的：** 上架的 1.2.2 沒有 `:::info／success／warning／danger` 的實機紀錄。證據是程式碼、kit 測試和我的 CLI 渲染；實機只測過 `:::spoiler` 那一族（§5）。

**要 Ray 決定：** ① §1 兩句同意請回「#278 `:::` ok」，要改哪裡寫在這裡；② §3 的幾列要不要加（我標了建議，沒加）。沒回的話，這一句先不放進頁面。Dev 可以先做其他部分。沒有改檔，也還沒翻六語。

## 1. 拿掉【待定】（`:::` 區塊）

位置用留言 6684344469 的行號。

| 位置 | 現在 | 建議 |
|---|---|---|
| en 第 82 行（`## How your notes will look`） | 【待定，#300】`:::info` blocks and other `:::` containers. | `:::` blocks work too. `:::info`, `:::success`, `:::warning` and `:::danger` show as blocks with a colored bar and a heading (Note, Tip, Warning or Caution), or your own heading if you write one after the name. `:::spoiler` shows as a collapsible section that opens when you click it. A `:::` block with any other name, or without its closing `:::`, shows as you typed it. |
| zh-Hant 第 184 行（`## 讀起來的樣子`） | 【待定，#300】`:::info` 等 `:::` 區塊。 | `:::` 區塊也看得到。`:::info`、`:::success`、`:::warning`、`:::danger` 會顯示成有色條的區塊，上面有標題，預設是附註、提示、警告、小心；在名稱後面自己寫標題的話，就用你寫的。`:::spoiler` 會顯示成點一下才展開的可收合區塊。其他名稱的 `:::` 區塊，或少了結尾 `:::` 的，會照原文顯示。 |

**位置：** 這一句改放在「A few things look different:」（zh-Hant 是「有幾個地方不一樣：」）之前，緊接「大多照樣能讀」那一段。現在【待定】在清單後面，「work too／也看得到」接不上。這是我多提的一處，Ray 不同意就維持放在清單後面。

給 Dev 複製的原文：

```md
`:::` blocks work too. `:::info`, `:::success`, `:::warning` and `:::danger` show as blocks with a colored bar and a heading (Note, Tip, Warning or Caution), or your own heading if you write one after the name. `:::spoiler` shows as a collapsible section that opens when you click it. A `:::` block with any other name, or without its closing `:::`, shows as you typed it.
```

```md
`:::` 區塊也看得到。`:::info`、`:::success`、`:::warning`、`:::danger` 會顯示成有色條的區塊，上面有標題，預設是附註、提示、警告、小心；在名稱後面自己寫標題的話，就用你寫的。`:::spoiler` 會顯示成點一下才展開的可收合區塊。其他名稱的 `:::` 區塊，或少了結尾 `:::` 的，會照原文顯示。
```

用語跟 App：「可收合區塊」是 Mac 1.2.2 的名稱；預設標題的 en／zh-Hant 是 Note、Tip、Warning、Caution／附註、提示、警告、小心（kit 的在地化字串）。

## 2. 其餘版本宣稱：現在／建議

| 位置 | 現在 | 建議 |
|---|---|---|
| 頁面本文（en、zh-Hant、六語） | 沒有任何一句寫到開啟網址、圖片下載。「Load Images／載入圖片」是預覽既有的按鈕（Mac 1.2.1 起），和 #355、#457 無關 | 不用改。Dev 照現況做，別加這兩項 |
| 6684344469 第 14 行 | 開啟網址不寫：排在 1.3.0。圖片下載（#457）也不寫，排在 1.2.3。 | 開啟網址（#355）不寫：milestone 1.3.0（12/31），還開著。圖片下載（#457）也不寫：milestone 1.2.4（12/16），還開著。兩項都在 12/04 之後，頁面不會用到。（原寫的「1.2.3」過時了，票上現在是 1.2.4） |
| 6684344469 第 15 行 | `:::` 區塊標【待定】：1.2.1 的 kit 畫得出來，但 #300 還開著，要實機確認或等 1.2.2。 | 作廢。`:::` 以 §1 為準，狀態已上線（Mac 1.2.2） |
| 6684344469 第 5 行 | 頁面只剩 `:::` 一處【待定】。 | 作廢，頁面沒有【待定】了（核准後） |
| 6684344469 第 231 行 | 上線條件：寫到的 MarsDawn 功能都在 1.2.1，不用等版本。`:::` 那段要等 #300。 | 上線條件：寫到的 MarsDawn 功能都在已上架的 Mac 1.2.2 或更早，不用等版本。（含 `:::`。） |
| 6684344469 第 235 行 | Mac 程式查自 mars-dawn tag `1.2.1`（`244803c`）。 | Mac 程式查自 mars-dawn tag `1.2.2`（`6c5d17f`）和 `main`（`fa1cef14`）；App Store 頁 11-18 讀到 Version 1.2.2（11-14）。 |
| 6684344469 第 239–243 行 | 狀態「已上線（1.2.1）」，行號：`MainMenu.swift:88`、`PRODUCT.md:42`、`Preview/PreviewViewController.swift:568-570`、`SettingsView.swift:5,160`、`AppSettings.swift:296`、`No folders yet…` | 狀態「已上線（Mac 1.2.2）」，行號改：`MainMenu.swift:92`、`PRODUCT.md:43`、`PreviewViewController.swift:794`（main 是 801）、`SettingsView.swift:160`（說明 164）、`AppSettings.swift:296`、`SettingsView.swift:170`。1.2.1 的行號在 1.2.2 都位移了 |
| 6684344469 第 252–253 行 | 開啟網址、圖片下載：計畫中，不寫；`:::` 區塊：【待定】 | 第 252 行補 milestone（#355 1.3.0／#457 1.2.4，都還開著）。第 253 行換成 §4 的 `:::` 幾列 |
| 6684344469 `++ins++`、emoji、`{%hackmd id %}`、Font Awesome 那列 | kit 0.7.6 實測，App 未實測 | kit 0.7.7 實測（11-18）：這四項結果和 0.7.6 一樣；`==`、`^`、`~`、`[TOC]`、`{%youtube %}` 也一樣；圖片尺寸這次沒重跑。App 未實測。1.2.2 內建的是 kit 0.7.7 |
| 6685163599 第 3 行，和 zh-hans 第 73、ja 第 175、ko 第 277、de 第 379、fr 第 481、es 第 583 行；第 632 行的 `:::` 勾選項 | 第 3 行：`:::` 維持【待定】。各語第 73…583 行：【待定，#300】`:::info`… 的句子。第 632 行：上線前依 #300 改寫或刪掉 | 核准 §1 之後我才翻六語，再整行換掉。在那之前 Dev 不要放這六行。ja 我把關，不請 Ray 看 |

## 3. 可以更完整的地方（只列，沒加）

1.2.2 上架後，頁面還有幾處可以多寫一點。每列我標了建議，請 Ray 取捨。

| # | 位置 | 現在 | 建議 |
|---|---|---|---|
| 1 | 「大多照樣能讀」那段的換行設定句 | 「To keep every line break as HackMD does, turn on Settings ▸ Appearance ▸ Keep single line breaks.」 | **不加。** 1.2.2 的更新說明沒有提到換行設定；這個設定在 tag 和 main 都是 `SettingsView.swift:122`，句子照舊 |
| 2 | §1 的放法 | 獨立一句，放在「大多照樣能讀」之後 | 另一種：把 `:::` 併進「大多照樣能讀」那段，再在「不一樣」清單加一條「`:::` 區塊會加上標題（附註、提示、警告、小心）」。搬家的人最在意哪裡不同；缺點是拆成兩處、已核准的那段要動。**我建議維持獨立一句**，Ray 取捨 |
| 3 | `:::spoiler {state="open"}`、`::::` 巢狀 | 頁面沒寫 | **不加。** 這兩個 1.2.2 都支援（kit 測試和 PR #623 實機），但是細節，加進去句子會變長，只有 HackMD 老手會用到 |
| 4 | `## Questions`／`## 常見問題` | 現在 3 則（下載全部、圖片、離開 HackMD） | **建議加 1 則**，搬家的人會搜這個問題，對 SEO／AEO 有用。en：見下，zh-Hant：見下 |
| 5 | 列印與 PDF | 頁面沒寫 | **不加。** 匯出時 `:::spoiler` 有「全部展開（預設）」和「依照文件設定」兩種（PR #623 實機），屬於 `/pdf/`（#383），不放這頁 |
| 6 | View ▸「全部收合到標題 2」等收合指令 | 頁面沒寫 | **不加。** 和搬 HackMD 無關 |

第 4 列的原文（要加才用）：

```md
### Do HackMD's `:::info` and `:::spoiler` blocks work in MarsDawn?

Yes. `:::info`, `:::success`, `:::warning` and `:::danger` show as blocks with a colored bar, and `:::spoiler` shows as a collapsible section. A `:::` block with any other name shows as you typed it.
```

```md
### HackMD 的 `:::info`、`:::spoiler` 區塊，在 MarsDawn 看得到嗎？

看得到。`:::info`、`:::success`、`:::warning`、`:::danger` 會顯示成有色條的區塊，`:::spoiler` 會顯示成可收合區塊。其他名稱的 `:::` 區塊會照原文顯示。
```

## 4. claim-check（只列這次查的）

Mac 程式查自 mars-dawn tag `1.2.2`（`6c5d17f`）和 `main`（`fa1cef14`）。兩處的 `project.yml:39` 都是 mars-dawn-kit `exactVersion: 0.7.7`（`13327b6`）。

| 句子 | 狀態 | 來源 |
|---|---|---|
| `:::info`、`:::success`、`:::warning`、`:::danger` 顯示成有色條的區塊 | 已上線（Mac 1.2.2）。App 實機：沒有 | kit 0.7.7 `Callouts.swift:406-409`（info→Note、success→Tip、warning→Warning、danger→Caution）、`Resources/Preview/preview.css:106-117`（色條）；kit 測試 `Tests/MarsDawnExportTests/Corpus/callouts/document.md:20-33`、`CountMatchesPageTests.swift:126-173`；我 11-18 的 CLI 渲染：四種都有色條和標題 |
| 沒寫標題時有預設標題，自己寫的優先 | 已上線（Mac 1.2.2）。App 實機：沒有 | `Callouts.swift:10-15`（opener 後面可接標題）；`preview.css:100-104, 118-123`（沒有自己的標題才補預設）；CLI 渲染：`:::info` 後面寫的標題（含行內 Markdown）會顯示成自己的 |
| 預設標題 en 是 Note、Tip、Warning、Caution，zh-Hant 是附註、提示、警告、小心 | 已上線（Mac 1.2.2）。標題隨語言 | `CalloutTitles.swift:9`；`Resources/Localization/<語言>.lproj/Localizable.strings`（zh-Hant `:21` 是 `"Note" = "附註"`；八語都有）；CLI 渲染的 zh-Hant 對上 |
| `:::spoiler` 顯示成可收合區塊，點一下才展開，預設收合 | 已上線（Mac 1.2.2）。App 實機：有 | `Callouts.swift:410`；PR #623 的 MBA 實測：6708429691、6746065458、6754865110、6755629350（kit 0.7.7）；CLI 渲染 |
| `:::spoiler {state="open"}` 預設展開；`::::spoiler` 裡可以放 `:::spoiler`（巢狀） | 已上線（Mac 1.2.2）。App 實機：有 | 同上 MBA 留言；kit 測試 `callouts/document.md:43`。頁面沒寫這兩點（§3 第 3 列） |
| 其他名稱的 `:::`（例如 `:::tip`）或少了結尾 `:::` 的，照原文顯示 | 已上線（Mac 1.2.2）。App 實機：沒有 | `Callouts.swift` 的 `default` 分支；CLI 渲染：兩種都留著 `:::` 原文 |
| Mac 1.2.2 已上架 | 已上線 | App Store 頁 [Version 1.2.2，2026-11-14](https://apps.apple.com/us/app/marsdawn-markdown-editor/id6812925073)；tag `1.2.2` = `6c5d17f`（2026-11-13，build 15） |
| #300 的內容在 1.2.2 裡 | 已上線 | mars-dawn#300 CLOSED（11/14：已進 Mac 1.2.2 送審 build，milestone「1.2.2 callouts and sidebar」）；PR #623（Folding，2026-11-10 合併）是 `6c5d17f` 的祖先 |
| 開啟網址（#355） | 計畫中，不寫 | #355 OPEN，milestone 1.3.0（12/31）；PR #589、#624 OPEN 未合併；tag 和 main 的 `MarsDawn/` 與 `project.yml` 用 `Open URL`、`openFromURL` 等字串 grep 沒有結果 |
| 圖片下載（#457） | 計畫中，不寫 | #457 OPEN，milestone 1.2.4（12/16）；PR #638 OPEN 未合併；同上 grep 沒有結果 |
| 預覽「載入圖片」、設定「自動載入網路圖片」預設關、「保留單一換行」、打開資料夾 | 已上線 | §2 的新行號（tag 和 main 在 `SettingsView.swift:122、160`、`MainMenu.swift:92` 位置相同；八語 UI 字串和 1.2.2 字串目錄逐項對過，「外觀」「圖片」面板名只用子字串比對） |

## 5. 待確認／風險

- [ ] **實機：** 上架的 1.2.2 沒有人在 App 裡開過 `:::info／success／warning／danger`。MBA 在 PR #623 測的檔案只有 `:::spoiler` 和 Obsidian 的 callout。頁面寫「看得到」之前，建議請 MBA 把文末的測試檔開一次，確認四種顏色、標題、`:::spoiler` 和最後兩個照原文顯示。沒做之前，這句的證據是程式碼、測試和 CLI。
- [ ] **商店 What's New 沒提 `:::`：** Mac 1.2.2 商店更新說明只有 4 條，沒有收合區塊和 `:::`。這和頁面無關，只是別拿更新說明當來源。
- [ ] **binary 對 tag：** 商店只看得到版本號，看不到 binary 的 commit。我以 tag `1.2.2`（build 15，11-13）為準。
- [ ] **milestone 和 Paula 的說法不同：** 派工寫「#355／#457 排在 1.2.4（12/16）之前不會上架」。票上 #457 是 1.2.4（12/16）、#355 是 1.3.0（12/31）。結論一樣（12/04 前都不會上架），只是我寫的是票上的實際值。
- [ ] **預設標題的語言：** 看起來是跟著 App 語言走（我的 CLI 在 zh-Hant 環境出附註、提示…）。頁面的 en 句子寫 Note／Tip／Warning／Caution，是 en App 的樣子。

<details><summary>測試檔（我 11-18 用 CLI 渲染的同一份，給 MBA 用）</summary>

```md
# HackMD containers

:::info
Plain info block, no title.
:::

:::success
Success block, no title.
:::

:::warning
Warning block, no title.
:::

:::danger
Danger block, no title.
:::

:::info Custom **title** with `code`
Info with a title.
:::

:::spoiler Click to open
Spoiler body.
:::

:::spoiler {state="open"} Open by default
Spoiler written open.
:::

::::spoiler Outer
Outer text.

:::info
Inner info inside a spoiler.
:::

::::

:::tip
Unknown type tip should stay literal.
:::

:::info
Unclosed info block stays literal.

Last line.
```

</details>

## 6. 給 Paula／Dev

- Dev A 可以先做這頁：§2 第一列說了不用改本文；`:::` 那一行等 Ray 回「#278 `:::` ok」。
- 核准後我翻六語，貼在新留言，並把 6685163599 裡對應的【待定】各處換掉（§2 最後一列）。我不會去改舊留言。
- 沒動 repo、沒開 PR、沒動 #382／#383／#721。

整理：Claude Code／Anthropic／claude-sonnet-5-5／en、zh-Hant 文案與查證；查證：mars-dawn tag `1.2.2`（`6c5d17f`）與 `origin/main`（`fa1cef14`）、mars-dawn-kit `0.7.7`（`13327b6`）的程式碼與測試（只讀），mars-dawn PR #623 的 MBA 留言，App Store 頁面（2026-11-18 讀），以及我 11-18 在本機用 kit 0.7.7 的 `marsdawn` CLI 渲染的測試檔；未做：改 repo、開 PR、翻其餘六語、跑 kit 測試、在上架的 1.2.2 App 實機操作 `:::info／success／warning／danger`、母語者審稿。

