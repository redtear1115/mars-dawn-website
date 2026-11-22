# 2026 Markdown 閱讀器推薦：只想看、不想改，Mac 和 iPhone 怎麼選

只想讀 Markdown、不想改的話，先看你在哪裡讀、讀的是什麼：

- **看 AI／agent 寫的計畫和報告**：用 MarsDawn。agent 存檔時頁面會跟著更新，Mermaid 圖表和數學式都畫好。
- **在 iPhone 上看**：MarsDawn 的 iPhone 版只能讀，不會誤改；Obsidian 能讀也能寫，但檔案要放在它的 vault 裡。
- **看完要交 PDF，而且要頁碼**：用 Typora 或 Marked 3；MarsDawn 要選手冊或講義版面。

市面上的比較文多半在比「編輯器」，比的是寫起來順不順手。這篇只比「讀」：打開後看到的是不是排好的頁面、會不會一不小心就改到檔案、手機上能不能看。以下 10 款依字母排序，每款都寫出適合誰、一個老實的缺點和價格。價格和功能的查證日期是 2026-11-18。

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

MarsDawn 也能輸出 PDF：手冊和講義版面有頁碼，預設的文件版面沒有。

## Chrome 的 Markdown Reader 擴充功能

裝在 Chrome 裡的擴充功能。把 .md 檔拖進瀏覽器，就會顯示排好的頁面，旁邊有目錄。Mermaid 圖表和數學式（KaTeX）都內建。

- 適合：不想多裝一個 App、本來就整天開著 Chrome 的人。
- 缺點：要先在擴充功能設定裡打開「允許存取檔案網址」，才能讀本機檔案。
- 價格：免費版可以用，另有 Pro 訂閱。
- 是哪一個：Chrome 線上應用程式商店裡的「Markdown Reader」（ID `medapdbncneneejhbgcjceippjlfkmkg`，開發者網站 md-reader.github.io）。官方頁面：[商店頁](https://chromewebstore.google.com/detail/md-reader/medapdbncneneejhbgcjceippjlfkmkg)、[官網](https://md-reader.github.io/)、[價格頁](https://md-reader.github.io/pricing)。查證日期 2026-11-18。

## ColaMD

免費開源（MIT）的 Markdown 編輯器，用 Electron 做的，macOS、Windows、Linux 都能用。agent 改檔時，畫面會即時更新，不用重新打開。

- 適合：要在 Windows 或 Linux 上看 agent 寫的檔案的人。
- 缺點：是所見即所得的編輯器，打開後就能直接改，沒有只讀模式。Mermaid 圖表和數學式（KaTeX）都內建。
- 價格：免費。
- 官方頁面：[GitHub](https://github.com/marswaveai/ColaMD)、[官網](https://colamd.com/)。查證日期 2026-11-18。

## MacDown 3000

原版 MacDown 已停止維護。MacDown 3000 是社群接手的版本：免費開源（MIT）、原生，具備 Mermaid、MathJax、PDF 輸出、自動重新載入與快速查看。

- 適合：想要免費原生左右分欄的人。
- 缺點：沒有記載可從命令列開到指定行的方法。
- 價格：免費。

## Marked

Marked 3 是預覽器，用來看你在其他 App 寫的 Markdown。檔案一變就重新載入，支援 MathJax 與 KaTeX，能列印分頁並加頁碼的 PDF。Marked 2 仍在販售。

- 適合：保留自己編輯工具、想要精緻預覽與列印的寫作者。
- 缺點：快速查看要另買 Marked QL（USD 9.99）。
- 價格：Marked 3 免費試用，之後每月 USD 2.99、每年 USD 29.99 或終身 USD 69.99（限時優惠價，原價每月 USD 4.99、每年 USD 49.99、終身 USD 89.99）。Marked 2 官網 USD 14.99，Mac App Store USD 13.99。

## MarkEdit

輕巧免費的原生 App（在 web view 中使用 CodeMirror），支援快速查看。

- 適合：想要快速、有 Mac 手感的純文字工具的人。
- 缺點：Mermaid 與數學式要裝官方擴充功能，PDF 要靠 Pandoc。
- 價格：免費。

## MarsDawn

原生 Mac App，原始碼與即時預覽左右並排，內建 Mermaid 與 KaTeX。AI 代理存檔時，開著的視窗會把變更收成一步可撤銷的「從磁碟更新」。`marsdawn open notes.md:120` 可開到指定行，另有給代理用的技能與 MCP 伺服器。快速查看不論試用與否都能用。「拷貝給 AI」與「拷貝引用」能把文字交給代理。除非你選擇，資料不會離開你的 Mac。

- 適合：審閱 AI 代理所寫 Markdown 的人。
- 缺點：PDF 要用手冊或講義版面才有頁碼，預設的文件版面沒有。
- 價格：免費下載，試用 14 天，之後 USD 4.99 一次買斷。同一個 Apple 帳號，一次購買，Mac、iPhone、iPad 都能用。

## Obsidian

以連結 Markdown 檔的 vault 為核心的筆記 App，具備 Mermaid、MathJax、PDF 輸出與自動重新載入。

- 適合：建立個人知識庫的人。
- 缺點：是 Electron App，檔案放在 vault 裡才最順手。
- 價格：免費，Sync 與 Publish 另外付費。

## QLMarkdown

快速查看擴充功能：在 Finder 選取 .md 檔按空白鍵即可。Mermaid 與 MathJax 需自行開啟。

- 適合：只想在 Finder 裡瞄一眼檔案的人。
- 缺點：不是用來閱讀或編輯的 App，也沒有記載 PDF 輸出。
- 價格：開源（GPL-3.0）。

## Typora

預覽即文件的所見即所得式寫作工具，具備 Mermaid、MathJax，PDF 輸出可在頁首或頁尾加頁碼。

- 適合：偏好在排版畫面中直接寫的人。
- 缺點：沒有原始碼與預覽左右並排。
- 價格：一次 USD 14.99，最多 3 台裝置。

## VS Code 預覽

內建 Markdown 預覽，1.121 起內建 Mermaid，支援 KaTeX。`code -g file:line` 可開到指定行。

- 適合：本來就整天用 VS Code 的開發者。
- 缺點：是 Electron App，沒有內建 PDF 輸出。
- 價格：免費。

## 比較表

| App | 價格 | iPhone／iPad | 只讀（不會誤改） | Mermaid | 數學式 | PDF | 自動重新載入 | 命令列開到指定行 | 快速查看 | 架構 |
|---|---|---|---|---|---|---|---|---|---|---|
| Chrome Markdown Reader | 免費，另有 Pro 訂閱 | 無 | 有 | 有 | KaTeX | 未記載 | 有 | 未記載 | 未記載 | 瀏覽器擴充功能 |
| ColaMD | 免費（MIT） | 無 | 無，打開就是編輯 | 有 | KaTeX | 有 | 有 | 未記載 | 未記載 | Electron |
| MacDown 3000 | 免費 | 無 | 未記載，官方稱是編輯器 | 有 | MathJax | 有 | 有 | 未記載 | 有 | 原生 |
| Marked 3 | 優惠價每月 USD 2.99 起 | 無 | 有，本身就是預覽器 | 有 | MathJax、KaTeX | 有，含頁碼 | 有 | 未記載 | Marked QL，USD 9.99 | 原生 |
| MarkEdit | 免費 | 無 | 有（Read Only Mode） | 擴充功能 | KaTeX（擴充功能） | Pandoc | 未記載 | 未記載 | 有 | 原生（web view） |
| MarsDawn | 一次 USD 4.99 | 有，只能讀 | Mac：預覽窗格不能改，原始碼窗格可以改；iPhone／iPad：只能讀 | 有 | KaTeX | 有，手冊與講義版面含頁碼 | 有，可撤銷 | 有 | 有 | 原生 |
| Obsidian | 免費 | 有，能讀也能寫 | 有，閱讀檢視 | 有 | MathJax | 有 | 有 | 未記載 | 未記載 | Electron |
| QLMarkdown | 開源（GPL-3.0） | 無 | 有，只在 Finder 預覽 | 需開啟 | MathJax（需開啟） | 未記載 | 不適用 | 不適用 | 本身即是 | 原生 |
| Typora | 一次 USD 14.99 | 無 | 未記載，官方稱是編輯器 | 有 | MathJax | 有，含頁碼 | 未記載 | 未記載 | 未記載 | 原生 |
| VS Code | 免費 | 無 | 有，預覽分頁 | 有（1.121 起） | KaTeX | 無 | 未記載 | 有 | 未記載 | Electron |

## MarsDawn 不適合誰

- 你要的 PDF 得有頁碼，又不想換成手冊或講義版面。MarsDawn 預設的文件版面沒有頁碼；Typora 與 Marked 3 能加。
- 想在 iPhone 或 iPad 上改檔案。MarsDawn 的 iPhone、iPad 版只能讀；要在手機上寫，Obsidian 可以。
- 用 Windows 或 Linux。MarsDawn 只有 Mac、iPhone 和 iPad 版；ColaMD 三個平台都有。
- 你在經營互相連結的個人筆記庫。Obsidian 就是為此打造的。
- 你只想在 Finder 預覽。QLMarkdown 開源（GPL-3.0）。

## 常見問題

### Mac 預設能開 .md 嗎？

能打開，但通常是用「文字編輯」，看到的是 `#` 和 `**` 這些記號，不是排好的頁面。換成 Markdown 閱讀器再設成預設 App，之後雙擊就會在那裡打開。做法請看 [Mac 怎麼開 md 檔](/zh-hant/view-markdown-on-mac/)。

### 哪些免費的 Mac Markdown 檢視器支援 Mermaid？

MacDown 3000、Obsidian 與 VS Code（1.121 起）內建。QLMarkdown 可選擇開啟，MarkEdit 要透過擴充功能。

### 哪些能輸出含頁碼的 PDF？

Typora、Marked 3 與 MarsDawn。在 MarsDawn 選手冊或講義版面；預設的文件版面沒有頁碼。

### 哪些能從命令列開到指定行？

MarsDawn（`marsdawn open notes.md:120`）與 VS Code（`code -g file:line`）。其他幾款未記載。

### 哪些是原生 Mac App，不是 Electron？

Obsidian、VS Code 與 ColaMD 是 Electron，Chrome Markdown Reader 是瀏覽器擴充功能，不是 Mac App；其餘都是原生 Mac App。MarkEdit 是原生 App，編輯區用 web view。

[立刻下載試用](https://apps.apple.com/app/id6812925073)

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 檢查 agent 寫的 Markdown、JSON、YAML：Mac 原生 app，即時預覽、Mermaid、KaTeX、快速查看、PDF。免費試用，之後一次 USD 4.99。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown、JSON、YAML 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可拿去開會或存檔。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [列印與 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上先預覽，再把 Markdown 列印或儲存為 PDF；有文件、手冊、講義三種版面，Mermaid 圖表和程式碼上色都會保留。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、iPhone 和 iPad 上不能編輯、沒有外掛、不需要帳號；可以換主題，但不能自訂 CSS。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Mac 怎麼開 md 檔](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hant/quicklook/index.md): MarsDawn 的快速查看讓你在 Finder 按空白鍵就看到排版後的 Markdown，Mermaid 圖表、KaTeX 數學式和程式碼上色都在。試用期結束後，快速查看照常可用。
- [拷貝給 AI](https://marsdawn.southern-light.dev/zh-hant/copy-for-ai/index.md): 選取文字，連同檔案路徑和行號一起拷貝，貼進 Claude Code 或任何 agent。在 Mac 上就能做，不用開 IDE，也不用裝外掛。
- [從 HackMD 搬到 Mac](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MarsDawn 比較：VS Code 預覽、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日（MarsDawn 的 PDF 格子更新於 2026 年 11 月 7 日）；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 輸出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 輸出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [主題](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 內建四種預覽主題，各有淺色與深色；在 Mac 版 MarsDawn 的設定裡打開主題庫，還能安裝更多。快速查看也會用你選的主題。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [和 agent 一起做主題](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽 MarsDawn 的預覽主題，每一個都經過開發者審核；可以依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造自己的主題，不用安裝，也不用 git。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [讀懂 agent 交回來的 Markdown](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [路線圖](https://marsdawn.southern-light.dev/zh-hant/roadmap/index.md): MarsDawn 在 Mac、iPhone 與 iPad 上正在做與接下來要做的功能，依版本列出。不寫日期，未排程的項目另外標明。
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
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista Rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
