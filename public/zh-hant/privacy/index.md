# 隱私權政策

macOS 的 Markdown 編輯器 MarsDawn 如何處理你的資訊。

最後更新：2026-09-19

**MarsDawn 不收集任何關於你的資料。**沒有帳號、沒有分析、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。

## 留在你 Mac 上的東西

- **你的文件。**MarsDawn 只讀寫你打開、儲存或選擇的檔案與資料夾，App 不會把它們上傳到任何地方。
- **你的設定。**外觀、預覽主題、視窗版面和圖片偏好，都存在 App 自己的偏好設定裡。
- **你授權的資料夾。**當你讓 MarsDawn 顯示某個資料夾裡的圖片或網頁檔案，或選擇筆記資料夾時，App 會保存 macOS 書籤，以便之後再次開啟。你在側邊欄開啟的資料夾，MarsDawn 會保持可讀寫，直到你在設定中移除為止，而不只是在那個視窗開著的時候。你隨時可以到 MarsDawn › 設定⋯ 移除。

## MarsDawn 什麼時候會連上網路

MarsDawn 可以完全離線使用，只有在**你自己選擇時**，才會為引用網路內容的文件連網：

- **Markdown 文件。**網路圖片預設不載入，只有在你按下預覽中的「載入圖片」，或在設定中開啟「自動載入網路圖片」後才會載入。Markdown 文件引用的其他網路內容一律不載入。
- **HTML 文件。**HTML 文件開啟時是靜態的：它的程式碼不會執行，也不會從網路載入任何東西。如果文件含有可以執行的程式碼，你可以針對這份文件選擇「顯示方式 › 執行這份文件」。之後它自己的程式碼會一直執行，直到你停止它、文件重新載入，或關閉視窗為止。這個選擇不會被記住，也不是一項設定。執行期間，這份文件可以透過網路傳送資料，並讀取它所在資料夾及其子資料夾中的圖片、樣式表、字型與媒體檔案。從網路下載的程式碼一律不會執行。

MarsDawn 只透過 https 載入網路內容。http 位址一律不會載入，任何設定都無法開啟，MarsDawn 也不會自動改寫成 https。在 Markdown 文件中，預覽會以佔位圖示代替。

載入網路內容時，你的 Mac 會直接向存放內容的伺服器發出請求。和所有網路請求一樣，這些伺服器會看到你的 IP 位址與請求的內容。MarsDawn 的開發者不會收到任何這類資訊。

在預覽中點選的連結會用你的預設瀏覽器打開，適用該瀏覽器的隱私做法。音訊與影片不會自動播放。

## Siri、捷徑和 Spotlight

MarsDawn 提供 Siri、捷徑 App 和 Spotlight 可用的動作，例如新增文件或加入筆記。使用時，你提供的文字會交給你 Mac 上的 MarsDawn，並只存到動作指定的位置（新文件，或你所選筆記資料夾中的 `Inbox.md`）。對 Siri 說的話由 Apple 依 [Apple 隱私權政策](https://www.apple.com/legal/privacy/) 處理。

## 輸出 PDF 和列印

輸出 PDF 和列印都在你的 Mac 上完成。PDF 存在你選擇的位置，列印則透過 macOS 送到你選的印表機。

## marsdawn 命令列工具

另外發佈、可自由選用的 `marsdawn` 命令列工具，同樣完全在你的 Mac 上執行：只讀取你指定的 Markdown 檔，並寫出你要求的 PDF。只有在加上 `--allow-remote-images` 時才會載入網路圖片。

## 兒童

MarsDawn 不向任何人收集資料，包括兒童。

## 購買

MarsDawn 將透過 Mac App Store 販售，付款會由 Apple 依其條款處理，開發者不會取得你的付款資訊。

## 政策變更

如果 MarsDawn 未來處理資料的方式有所改變，本頁會在該版本推出前更新，頁首的日期也會一併更改。

## 聯絡我們

隱私相關問題：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
