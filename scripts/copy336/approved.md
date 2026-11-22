## 結論

`/zh-hant/best-markdown-viewer-mac/` 改版用的文案如下：標題、description、開頭答案、三組情境、兩款新工具、比較表的兩個新欄位、「不適合誰」和兩題 FAQ。網址不變，舊的 8 款段落沿用。以下是提案，等 Ray 核准。

- **標題**：用「2026 Markdown 閱讀器推薦：只想看、不想改，Mac 和 iPhone 怎麼選」。關鍵詞「Markdown 閱讀器推薦」放在最前面，「只想看、不想改」是這頁和其他比較文不同的地方。
- **比較表的新欄位**：我先依官網和商店頁填了一版，每一格都標了「待查證」。驗收要求每格附來源或查證日期，所以實作時請照表格下的「來源」逐格確認。我沒有實際裝過每一款，有幾格只能寫「未記載」。
- **MarsDawn 只出現在兩組**：「看 AI／agent 產出的計畫」和「在手機上看」。「看完要交 PDF」那組推 Typora 和 Marked 3，MarsDawn 只在內文裡提一句（因為它的 PDF 沒有頁碼）。

---

### title／h1

- `<title>`：2026 Markdown 閱讀器推薦：Mac、iPhone 只看不改 · MarsDawn
- `<h1>`：2026 Markdown 閱讀器推薦：只想看、不想改，Mac 和 iPhone 怎麼選

`<title>` 比較短，搜尋結果裡才不會被截掉；`<h1>` 把讀者的問題寫完整。兩者都有「Markdown 閱讀器推薦」和「iPhone」，符合驗收。

### description

> Markdown 閱讀器推薦：只想讀、不想改的話，Mac 和 iPhone 各用哪一款。比較 10 款的價格、iPhone／iPad、唯讀、Mermaid、數學式和 PDF，依情境分組。

（第一句有「閱讀器」和「推薦」。字數約 75 字，在搜尋結果的顯示範圍內。）

### 開頭（取代現有第一段）

~~~markdown
只想讀 Markdown、不想改的話，先看你在哪裡讀、讀的是什麼：

- **看 AI／agent 寫的計畫和報告**：用 MarsDawn。agent 存檔時頁面會跟著更新，Mermaid 圖表和數學式都畫好。
- **在 iPhone 上看**：MarsDawn 的 iPhone 版只能讀，不會誤改；Obsidian 能讀也能寫，但檔案要放在它的 vault 裡。
- **看完要交 PDF，而且要頁碼**：用 Typora 或 Marked 3。

市面上的比較文多半在比「編輯器」，比的是寫起來順不順手。這篇只比「讀」：打開後看到的是不是排好的頁面、會不會一不小心就改到檔案、手機上能不能看。以下 10 款依字母排序，每款都寫出適合誰、一個老實的缺點和價格。價格和功能的查證日期是 {{查證日期}}。
~~~

### 依情境分組（放在各款介紹之前）

~~~markdown
## 依情境挑

### 看 AI／agent 產出的計畫

agent 寫的檔案很長，會一直被改寫，裡面常常有表格和 Mermaid 圖表。挑的時候，看三件事：檔案被改了會不會自動更新、圖表畫不畫得出來、能不能從終端機直接打開。

- **MarsDawn**：agent 存檔時，開著的視窗會自動「從磁碟更新」，而且可以撤銷。`marsdawn open plan.md` 從終端機打開，也有給 agent 用的 skill。
- **ColaMD**：免費開源，agent 改檔時畫面也會即時更新，Windows 和 Linux 也能用。

### 在手機上看

- **MarsDawn（iPhone／iPad）**：只能讀，不能改，Mermaid、數學式和表格都畫好。和 Mac 版共用一次買斷。
- **Obsidian**：有 iPhone 版，能讀也能寫。檔案要放在它的 vault 裡。

### 看完要交 PDF

- **Typora**：輸出 PDF 時，頁首或頁尾可以加頁碼。
- **Marked 3**：專門用來預覽和列印，PDF 有分頁和頁碼。

MarsDawn 也能輸出 PDF，但沒有頁碼。
~~~

### 新增兩款（依字母排序插入）

~~~markdown
## Chrome 的 Markdown Reader 擴充功能

裝在 Chrome 裡的擴充功能。把 .md 檔拖進瀏覽器，就會顯示排好的頁面，旁邊有目錄。{{Mermaid／數學式：待查證}}

- 適合：不想多裝一個 App、本來就整天開著 Chrome 的人。
- 缺點：要先在擴充功能設定裡打開「允許存取檔案網址」，才能讀本機檔案。iPhone 上的 Chrome 不能裝擴充功能。
- 價格：免費。

## ColaMD

免費開源（MIT）的 Markdown 編輯器，用 Electron 做的，macOS、Windows、Linux 都能用。agent 改檔時，畫面會即時更新，不用重新打開。

- 適合：要在 Windows 或 Linux 上看 agent 寫的檔案的人。
- 缺點：是所見即所得的編輯器，打開後就能直接改，沒有只讀模式。{{Mermaid／數學式：主程式未內建，有第三方延伸版本；待查證}}
- 價格：免費。
~~~

### 比較表新增的兩欄

欄名：**iPhone／iPad**、**只讀（不會誤改）**

| App | iPhone／iPad | 只讀（不會誤改） |
|---|---|---|
| Chrome Markdown Reader | 無（iOS 版 Chrome 不支援擴充功能） | 有 |
| ColaMD | 無 | 無，打開就是編輯 |
| MacDown 3000 | 無 | 無，原始碼可以直接改 |
| Marked 3 | 無 | 有，本身就是預覽器 |
| MarkEdit | {{待查證}} | 無 |
| MarsDawn | 有，只能讀 | Mac：預覽窗格不能改，原始碼窗格可以改；iPhone／iPad：只能讀 |
| Obsidian | 有，能讀也能寫 | 有，閱讀檢視 |
| QLMarkdown | 無 | 有，只在 Finder 預覽 |
| Typora | 無 | 無，打開就是編輯 |
| VS Code | 無 | 有，預覽分頁 |

「自動重新載入」欄的 MarsDawn 照實寫「有，可撤銷」，現在就是這樣寫的，不用改。新增的兩款依各自的頁面填其他欄位，沒寫的就填「未記載」，不留空格。

來源（實作時逐格確認，並寫上查證日期）：
- ColaMD：github.com/marswaveai/ColaMD（MIT、Electron、三平台）、Homebrew cask `colamd`
- Chrome Markdown Reader：Chrome 線上應用程式商店 `medapdbncneneejhbgcjceippjlfkmkg`。同名的擴充功能有好幾個，請在頁面上寫明是哪一個。
- iPhone 版有沒有：各家的 App Store 頁

### 「MarsDawn 不適合誰」（取代現有段落）

~~~markdown
## MarsDawn 不適合誰

- PDF 一定要有頁碼。Typora 與 Marked 3 能加，MarsDawn 不能。
- 想在 iPhone 或 iPad 上改檔案。MarsDawn 的 iPhone、iPad 版只能讀；要在手機上寫，Obsidian 可以。
- 用 Windows 或 Linux。MarsDawn 只有 Mac、iPhone 和 iPad 版；ColaMD 三個平台都有。
- 你在經營互相連結的個人筆記庫。Obsidian 就是為此打造的。
- 你只想在 Finder 預覽。QLMarkdown 免費。
~~~

（「從不離開 VS Code」那一條拿掉了，因為這頁現在講的是閱讀器，VS Code 的預覽已經寫在比較表裡。如果想保留，可以加回去，總共 6 條。）

### FAQ 新增兩題（放在最前面）

~~~markdown
### iPhone 怎麼看 .md 檔？

在「檔案」App 點一下就能打開，但{{依 #337 實機結果：看到的是原始文字／表格和圖表不會畫出來}}。想看排好的頁面，用 MarsDawn 的 iPhone 版，Mermaid、數學式和表格都在，只能讀，不會誤改。步驟請看 [iPhone、iPad 怎麼看 md 檔](/zh-hant/view-markdown-on-iphone/)。

### Mac 預設能開 .md 嗎？

能打開，但通常是用「文字編輯」，看到的是 `#` 和 `**` 這些記號，不是排好的頁面。換成 Markdown 閱讀器再設成預設 App，之後雙擊就會在那裡打開。做法請看 [Mac 怎麼開 md 檔](/zh-hant/view-markdown-on-mac/)。
~~~

### 用字（台灣）

整頁統一用：檔案（不用文件、文檔）、預覽、買斷、App（大寫）、閱讀器（標題和開頭用；比較表的欄名維持原樣）。MarsDawn 那一段的價格改成「免費下載，試用 14 天，之後 USD 4.99 一次買斷。同一個 Apple 帳號，一次購買，Mac、iPhone、iPad 都能用。」。原本的「僅在 Mac App Store 提供」拿掉，因為已經不對了。

## 待確認

- **Mac 版 MarsDawn 的「只讀」那一格**：Mac 版是編輯器，原始碼窗格可以改。照實寫成「預覽窗格不能改」，不寫「有」。如果 Ray 覺得太長，可以只寫「iPhone／iPad 有」。
- **#337 的網址**：FAQ 連到 `/zh-hant/view-markdown-on-iphone/`，這是我在 #337 提的網址。#337 改網址的話，這裡要一起改。
- **新增工具的 Mermaid／數學式**：我只查了官方 repo 和商店頁的說明，沒有實際裝來試。實作的人請確認後再填，查不到就寫「未記載」。
- **8 週後的檢討**：照票上的驗收，不在文案範圍。

- [ ] 標題、description、開頭
- [ ] 情境分組、兩款新工具
- [ ] 比較表兩欄（查證後）
- [ ] 不適合誰、FAQ
