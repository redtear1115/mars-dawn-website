# 隱私權政策

macOS 的 Markdown 編輯器 MarsDawn 如何處理你的資訊。

最後更新：2026-09-23

**MarsDawn app 不收集任何關於你的資料。**沒有帳號、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。

## 這個網站

App 和這個網站是兩件事。App 不收集資料。會記下造訪的，只有 marsdawn.southern-light.dev。

這個網站使用透過**Google Tag Manager**載入的**Google Analytics 4**。每位訪客一開始的分析狀態都是拒絕：Google 的同意模式只會送出一個沒有 cookie、不含任何持續性識別碼的連線，直到你在橫幅中選擇「接受」為止。選擇「拒絕」，或是不做選擇，都會維持這個狀態；如果先前選過「接受」再改選「拒絕」，分析會立即關閉，下面提到的 cookie 也會被移除。你可以隨時用每一頁頁尾的「Cookie 設定」連結改變選擇；這個選擇只存在你瀏覽器的本機儲存空間裡，不是我們設下的 cookie。

一旦你按下接受，Google Analytics 就會設定自己的 cookie（`_ga` 與 `_ga_<評估 ID>`），並記錄：

- **頁面瀏覽與來源網址。**被瀏覽的頁面，以及瀏覽器有送出來源網址時的那個網址。
- **大略位置、裝置與瀏覽器。**由你的 IP 位址推算出的粗略位置（最多到城市層級）、裝置類型、作業系統與瀏覽器，都不足以用來辨識你是誰。
- **經由本站離開的點擊與捲動。**Google Analytics 的加強型評估會記錄離開本站的點擊（例如前往 Mac App Store 的連結），以及你在頁面上捲動的程度。
- **IP 位址。**Google Analytics 4 不會記錄或保存 IP 位址。
- **不會記錄的。**沒有帳號，因為這個網站不需要帳號。沒有你的文件，也沒有你打的字。沒有跨站廣告，也不會建立你的個人檔案。App 向 `/themes/` 索取主題檔案的請求會被略過，不會送出。
- **保留期限。**Google 會保留這些資料 14 個月，之後刪除。
- **資料處理地點。**Google Tag Manager 與 Google Analytics 由 Google 營運；你的資料可能會在美國及 Google 營運所在的其他國家處理。
- **主機。**網站放在 Cloudflare。和任何主機一樣，它在回應請求時會看到你的 IP 位址。那是主機自己的日誌，不是上面的分析。

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

MarsDawn app 不向任何人收集資料，包括兒童。網站上記下的造訪不是帳號，也不用來辨認任何人。

## 購買

MarsDawn 將透過 Mac App Store 販售，付款會由 Apple 依其條款處理，開發者不會取得你的付款資訊。

## 政策變更

如果 MarsDawn 未來處理資料的方式有所改變，本頁會在該版本推出前更新，頁首的日期也會一併更改。

## 聯絡我們

隱私相關問題：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
