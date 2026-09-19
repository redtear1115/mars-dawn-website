# 支援

macOS Markdown 編輯器 MarsDawn 的使用說明。

## 寫信給我們

[support@southern-light.dev](mailto:support@southern-light.dev?subject=MarsDawn%20support)

請附上你的 macOS 版本與 MarsDawn 版本（MarsDawn › 關於 MarsDawn）。如果畫面看起來不對，附上截圖或一份小的範例文件會很有幫助。

## 常見問題

### MarsDawn 需要什麼環境？

macOS 26 Tahoe 或更新版本的 Mac，Apple 晶片或 Intel 皆可。

### 怎麼切換編輯器與預覽？

按 `⌘1` 只看原始碼、`⌘2` 左右並排、`⌘3` 只看預覽。「顯示方式」選單和工具列也有相同選項。

### 文件裡的圖片沒有顯示。

- **Mac 上的圖片：**先儲存文件，再按預覽中的「授權資料夾存取⋯」，選擇圖片所在的資料夾。MarsDawn 會記住這個資料夾，你可以到 MarsDawn › 設定⋯ › 資料夾存取查看。
- **網路上的圖片：**網路圖片在你按下預覽上方的「載入圖片」之前不會載入。想要一律載入，可在設定中開啟「自動載入網路圖片」。

### 怎麼加入圖片？

把圖片拖進編輯器，或直接貼上。文件需要先儲存：MarsDawn 會把圖片複製到文件旁的 `assets` 資料夾，並幫你寫好 Markdown 連結。

### Mermaid 圖表顯示錯誤。

MarsDawn 會顯示圖表的原始碼，下方附上 Mermaid 錯誤訊息的第一行。請檢查訊息指出的那一行，例如箭頭後面缺了目標，或括號沒有閉合。

### 怎麼產生 PDF？

選擇「檔案 › 輸出為 PDF⋯」（`⌥⌘E`）。不論目前是哪種版面，PDF 都會使用預覽主題的淺色版本並自動分頁。「檔案 › 列印⋯」會印出相同的頁面。

### 怎麼搭配 Siri 或捷徑使用？

打開「捷徑」App 搜尋 MarsDawn，就能找到「新增 Markdown 文件」、「新增筆記到收件匣」與「打開最近的文件」。要新增筆記之前，請先到 MarsDawn › 設定⋯ › 筆記資料夾選擇資料夾，筆記會加到該資料夾的 `Inbox.md`。

### 設定在哪裡？

MarsDawn › 設定⋯（`⌘,`），包含外觀、圖片、筆記資料夾、資料夾存取與預覽主題。

### 怎麼申請退款？

購買由 Apple 處理，請到 [reportaproblem.apple.com](https://reportaproblem.apple.com) 申請退款。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 售價 USD 4.99，買一次就好。沒有訂閱、不需要帳號，也沒有付費進階版。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
