# 你寫的內容，留在你的 Mac 上。

MarsDawn 不需要帳號，沒有同步，也沒有雲端。它打開檔案、讓你寫，再存回你選的位置。

![MarsDawn 以 Classic 主題顯示文件，預覽佔滿整個視窗。](https://marsdawn.southern-light.dev/assets/screens/02-classic-1180.png)

這張截圖裡：

1. 視窗標題就是檔名：你 Mac 上一個普通的 .md 檔。
2. 工具列只有主題和版面，沒有帳號按鈕，也不用登入。

**MarsDawn 不收集任何關於你的資料。**App 從不上傳你的文件；你的 Mac 從網路載入內容時，開發者也收不到任何資訊。

## 沒有帳號、沒有雲端、不追蹤

- **沒有帳號。**不用註冊，也不用登入。
- **沒有同步。**文件存在哪裡就留在哪裡；想在另一台 Mac 上用，就放在你本來就會同步的資料夾。詳見 [MarsDawn 做不到的事](/zh-hant/limits/)。
- **沒有分析、廣告或追蹤。**App Store 隱私權標示將會是「未收集資料」。
- **只讀你打開的東西。**MarsDawn 只讀取你打開或選擇的檔案與資料夾。在側邊欄打開的資料夾，會一直可以讀寫，直到你到 MarsDawn › 設定⋯ 移除。詳見[留在你 Mac 上的東西](/zh-hant/privacy/#on-your-mac)。

## 它只在這些時候連網

MarsDawn 可以完全離線使用，只有在你自己選擇時才會連網：

- **Markdown 裡的網路圖片**：按下「載入圖片」時才載入；在設定中開啟「自動載入網路圖片」則一律載入。在那之前，打開文件不會讓任何伺服器知道你讀了它。載入時，你的 Mac 直接向存放圖片的伺服器發出請求，那台伺服器會看到你的 IP 位址；MarsDawn 的開發者收不到任何這類資訊。
- **HTML 文件**開啟時是靜態的：不載入任何東西，程式碼也不執行，除非你針對這份文件選擇「顯示方式 › 執行這份文件」。執行期間，這份文件可以透過網路傳送資料。這個選擇不會被記住。
- **連結**會用你的預設瀏覽器打開，適用該瀏覽器的隱私做法。
- **免費的 [marsdawn CLI](/zh-hant/cli/)** 完全在你的 Mac 上執行，只有加上 `--allow-remote-images` 時才會載入網路圖片。

網路內容只走 https：http 位址一律不會載入，任何設定都無法開啟。對 Siri 說的話與 App Store 購買，由 Apple 依其條款處理。

完整說明請看[隱私權政策](/zh-hant/privacy/#internet)。隱私相關問題：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
