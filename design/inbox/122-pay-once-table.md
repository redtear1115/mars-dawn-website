# /pay-once/: trial, trial ended, unlocked — copy (#122)

This file covers en and zh-Hant, as the #122 comment asks. zh-hans and ja follow once these two are approved. It has three parts:

1. The new comparison table on `/pay-once/`.
2. The corrected step 2 on `/pay-once/`: Quick Look is out of the trial-only list.
3. A matching update to the `/limits/` "After the trial" paragraph.

The source is `scripts/build_pages.py` on `release-1.0.2` (0f4ee3e). `/pay-once/` and `/limits/` read the same on `1001-go-live` (70568a9).

## Facts, checked

Every cell restates the facts table in #122. I checked those against the app repo (`redtear1115/mars-dawn` main, c0d4add):

- `docs/free-trial-plan.md` §3 (states) and §3.1 (the locked-state table):
  - Save As… works after expiry.
  - Export as PDF, Print and Save in place are blocked.
  - App Intents are locked.
  - The Quick Look extension is not locked.
  - `marsdawn export` is "unchanged and free, forever".
  - Files on disk are never written with wrong or empty content.
- `docs/free-trial-plan.md` §3.3 records the owner's decision of 2026-09-26: Quick Look keeps rendering Mermaid and math after the trial.
- `PRODUCT.md`:
  - 14-day trial, then a $4.99 one-time unlock.
  - The trial is a $0 in-app purchase.
- `docs/paywall-screens.md` screen C: the Save As… line appears only in a window that was open at expiry. That's why the table qualifies that cell.
- `LicenseRules.swift`: `trial` and `unlocked` allow reading; `expired`, `notStarted` and `unconfirmed` don't.

No price, duration or feature is new. USD 4.99 and 14 days are already on the page.

## 1. Comparison table

Placement: a new `<h2>` and table on `/pay-once/`, between the "How it works" list and "If you don't unlock". The prose under "If you don't unlock" stays, as the detail behind the table.

Implementation:

- Add a `COMPARE_TABLES["pay-once-states"]` entry in the same shape as `macmd-features`.
- Put the `<!--compare:pay-once-states-->` placeholder in the page body.
- It has 4 columns, so `compare_table_html` gives it the `compare compare-wide` class.

`<code>` in a cell is intentional; the other compare tables already carry HTML in cells.

### en

Heading: `<h2>What works when</h2>`

| | Trial (days 1–14) | Trial ended, not unlocked | Unlocked |
|---|---|---|---|
| Open a document in MarsDawn | Yes | Opens, with the content covered | Yes |
| Read and edit in MarsDawn (source, preview, Mermaid, math) | Yes | No | Yes |
| Export as PDF and print from MarsDawn | Yes | No | Yes |
| Keep typed text with File ▸ Save As… | Yes | Yes, in a window open when the trial ended | Yes |
| Siri and Shortcuts actions | Yes | No | Yes |
| Quick Look in Finder, with Mermaid diagrams and math | Yes | Yes, unchanged | Yes |
| `marsdawn export` (free command-line tool): PDF with diagrams and math | Yes | Yes, unchanged | Yes |
| Your files on disk | As you saved them | As you saved them; the lock never changes them | As you saved them |

Line under the table: `<p>Before you start the trial, MarsDawn shows the trial offer. Starting it costs nothing.</p>`

For `COMPARE_TABLES`:

```python
"head": {"en": ["", "Trial (days 1–14)", "Trial ended, not unlocked", "Unlocked"]},
"rows": {"en": [
    ["Open a document in MarsDawn", "Yes", "Opens, with the content covered", "Yes"],
    ["Read and edit in MarsDawn (source, preview, Mermaid, math)", "Yes", "No", "Yes"],
    ["Export as PDF and print from MarsDawn", "Yes", "No", "Yes"],
    ["Keep typed text with File ▸ Save As…", "Yes", "Yes, in a window open when the trial ended", "Yes"],
    ["Siri and Shortcuts actions", "Yes", "No", "Yes"],
    ["Quick Look in Finder, with Mermaid diagrams and math", "Yes", "Yes, unchanged", "Yes"],
    ["<code>marsdawn export</code> (free command-line tool): PDF with diagrams and math", "Yes", "Yes, unchanged", "Yes"],
    ["Your files on disk", "As you saved them", "As you saved them; the lock never changes them", "As you saved them"],
]},
```

### zh-Hant

Heading: `<h2>各階段能做什麼</h2>`

| | 試用期間（第 1–14 天） | 試用結束、未解鎖 | 已解鎖 |
|---|---|---|---|
| 在 MarsDawn 打開文件 | 可以 | 會開啟，但內容被遮住 | 可以 |
| 在 MarsDawn 閱讀與編輯（原始碼、預覽、Mermaid、數學式） | 可以 | 不行 | 可以 |
| 在 MarsDawn 輸出 PDF 與列印 | 可以 | 不行 | 可以 |
| 用「檔案」▸「另存新檔⋯」保存輸入的文字 | 可以 | 可以，限試用結束時已開著的視窗 | 可以 |
| Siri 和捷徑動作 | 可以 | 不行 | 可以 |
| Finder 快速查看，含 Mermaid 圖表與數學式 | 可以 | 可以，不受影響 | 可以 |
| `marsdawn export`（免費命令列工具）：含圖表與數學式的 PDF | 可以 | 可以，不受影響 | 可以 |
| 你磁碟上的檔案 | 維持你存的樣子 | 維持你存的樣子，鎖定不會改動它們 | 維持你存的樣子 |

Line under the table: `<p>開始試用之前，MarsDawn 會先顯示免費試用的畫面。開始試用不用付費。</p>`

```python
"head": {"zh-hant": ["", "試用期間（第 1–14 天）", "試用結束、未解鎖", "已解鎖"]},
"rows": {"zh-hant": [
    ["在 MarsDawn 打開文件", "可以", "會開啟，但內容被遮住", "可以"],
    ["在 MarsDawn 閱讀與編輯（原始碼、預覽、Mermaid、數學式）", "可以", "不行", "可以"],
    ["在 MarsDawn 輸出 PDF 與列印", "可以", "不行", "可以"],
    ["用「檔案」▸「另存新檔⋯」保存輸入的文字", "可以", "可以，限試用結束時已開著的視窗", "可以"],
    ["Siri 和捷徑動作", "可以", "不行", "可以"],
    ["Finder 快速查看，含 Mermaid 圖表與數學式", "可以", "可以，不受影響", "可以"],
    ["<code>marsdawn export</code>（免費命令列工具）：含圖表與數學式的 PDF", "可以", "可以，不受影響", "可以"],
    ["你磁碟上的檔案", "維持你存的樣子", "維持你存的樣子，鎖定不會改動它們", "維持你存的樣子"],
]},
```

## 2. `/pay-once/` step 2, corrected

Replace the second `<li>` of `<ol class="loop-steps">`.

en, before:

```html
<li><strong>Try all of it for 14 days.</strong> Start the trial and everything works for 14 days: every theme and layout, PDF export and printing, Quick Look, and the Siri and Shortcuts actions.</li>
```

en, after:

```html
<li><strong>Try all of it for 14 days.</strong> Start the trial and everything in MarsDawn works for 14 days: every theme and layout, PDF export and printing, and the Siri and Shortcuts actions. Quick Look in Finder works with or without the trial.</li>
```

zh-Hant, before:

```html
<li><strong>14 天，全部都能用。</strong> 開始試用後，14 天內所有功能都能使用：所有主題與版面、PDF 輸出與列印、快速查看，以及 Siri 和捷徑動作。</li>
```

zh-Hant, after:

```html
<li><strong>14 天，全部都能用。</strong> 開始試用後，14 天內 MarsDawn 的所有功能都能使用：所有主題與版面、PDF 輸出與列印，以及 Siri 和捷徑動作。Finder 的「快速查看」不論有沒有試用都能用。</li>
```

## 3. `/limits/` "After the trial", kept consistent

The current paragraph leaves out export and print, which the table lists as blocked. It also doesn't point to the table.

en, after:

```html
<p>If you don't unlock MarsDawn once the 14-day trial ends, you can't read, edit, export or print documents in it: they open with their content covered. Your files stay as they are, Quick Look still shows them, and the free command-line tool still exports them. The <a href="/pay-once/">trial and unlock page</a> sets all three stages side by side.</p>
```

zh-Hant, after:

```html
<p>如果 14 天試用結束後沒有解鎖，就無法在 MarsDawn 中閱讀、編輯、輸出或列印文件：文件會開啟，但內容會被遮住。你的檔案維持原樣，「快速查看」依然看得到，免費的命令列工具也依然能把它們輸出成 PDF。<a href="/zh-hant/pay-once/">試用與解鎖頁面</a>有三個階段的對照表。</p>
```

## Terms

- zh-Hant uses 輸出 for export (the app's 輸出為 PDF⋯), 列印, 另存新檔⋯ with ⋯, 快速查看, Siri 和捷徑, and 「檔案」▸ with the same ▸ as the existing page.
- The existing `/pay-once/` and `/limits/` zh-Hant say 匯出 for the CLI. So does the app's own paywall reassurance line. In the two lines I rewrote, I used 輸出; see 待確認.
- en: no Oxford comma. The menu path is written File ▸ Save As…, as on the page today.
