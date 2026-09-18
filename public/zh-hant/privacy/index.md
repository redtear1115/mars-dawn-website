# 隱私權政策

macOS 的 Markdown 編輯器 MarsDawn 如何處理你的資訊。

最後更新：2026-09-17

**MarsDawn 不收集任何關於你的資料。**沒有帳號、沒有分析、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。

## 留在你 Mac 上的東西

- **你的文件。**MarsDawn 只讀寫你打開、儲存或選擇的檔案與資料夾，App 不會把它們上傳到任何地方。
- **你的設定。**外觀、預覽主題、視窗版面，以及你對網路圖片與網路內容的選擇，都存在 App 自己的偏好設定裡。
- **你授權的資料夾。**當你讓 MarsDawn 顯示某個資料夾裡的圖片或網頁檔案，或選擇筆記資料夾時，App 會保存 macOS 書籤，以便之後再次開啟。你在側邊欄開啟的資料夾，MarsDawn 會保持可讀寫，直到你在設定中移除為止，而不只是在那個視窗開著的時候。你隨時可以到 MarsDawn › 設定⋯ 移除。

## MarsDawn 什麼時候會連上網路

MarsDawn 可以完全離線使用，只有在**你選擇載入文件引用的網路內容**時才會連網：

- **Markdown 文件。**網路圖片預設不載入，只有在你按下預覽中的「載入圖片」，或在設定中開啟「自動載入網路圖片」後才會載入。Markdown 文件引用的其他網路內容一律不載入。
- **HTML 網頁。**MarsDawn 以唯讀方式顯示 HTML 檔。網頁引用的網路內容（圖片、樣式表、字型、音訊與影片）只有在你選擇時才會載入，這項設定獨立於圖片設定，預設為關閉。網頁中的程式碼一律不會執行。

MarsDawn 只透過 https 載入網路內容。文件若引用 http 位址，一律不會載入，任何設定都無法開啟，MarsDawn 也不會自動改寫成 https，預覽中會以佔位圖示代替。

載入網路內容時，你的 Mac 會直接向存放內容的伺服器發出請求。和所有網路請求一樣，這些伺服器會看到你的 IP 位址與請求的內容。MarsDawn 的開發者不會收到任何這類資訊。

如果你允許某個 HTML 網頁載入網路內容，該網頁的版面配置可能讓那些伺服器得知：網頁本身引用的檔案是否存在於你授權給 MarsDawn 的資料夾中，以及大約的檔案大小。網頁無法讀取你的檔案，也無法傳出檔案內容；網路內容保持封鎖時，這種情況不會發生。

在預覽中點選的連結會用你的預設瀏覽器打開，適用該瀏覽器的隱私做法。音訊與影片不會自動播放。

## Siri、捷徑和 Spotlight

MarsDawn 提供 Siri、捷徑 App 和 Spotlight 可用的動作，例如新增文件或加入筆記。使用時，你提供的文字會交給你 Mac 上的 MarsDawn，並只存到動作指定的位置（新文件，或你所選筆記資料夾中的 `Inbox.md`）。對 Siri 說的話由 Apple 依[Apple 隱私權政策](https://www.apple.com/legal/privacy/)處理。

## 輸出 PDF 和列印

輸出 PDF 和列印都在你的 Mac 上完成。PDF 存在你選擇的位置，列印則透過 macOS 送到你選的印表機。

## marsdawn 命令列工具

另外發佈、可自由選用的 `marsdawn` 命令列工具，同樣完全在你的 Mac 上執行：只讀取你指定的 Markdown 檔，並寫出你要求的 PDF。只有在加上 `--allow-remote-images` 時才會載入網路圖片。

## 兒童

MarsDawn 不向任何人收集資料，包括兒童。

## 購買

MarsDawn 透過 Mac App Store 販售，付款由 Apple 依其條款處理，開發者不會取得你的付款資訊。

## 政策變更

如果 MarsDawn 未來處理資料的方式有所改變，本頁會在該版本推出前更新，頁首的日期也會一併更改。

## 聯絡我們

隱私相關問題：[support@southern-light.dev](mailto:support@southern-light.dev)

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是原生的 Mac Markdown 編輯器，支援即時預覽和 Mermaid 圖表，也能輸出 PDF。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
