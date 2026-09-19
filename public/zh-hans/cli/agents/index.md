# 給 AI agent 的 marsdawn 參考

給呼叫 `marsdawn` 命令列工具的 AI agent 與腳本參考。本頁每個範例都用目前原始碼建置的工具實際執行過。

**要把 Markdown 檔轉成 PDF，執行 `marsdawn export notes.md --json`，再從 stdout 讀取一個 JSON 物件。**Mermaid 圖表與程式碼上色的呈現方式和 MarsDawn app 相同。`export` 不需要 app，`open` 需要。

## 能做什麼

- `export`：用和 MarsDawn app 相同的匯出程式，把一個 Markdown 檔輸出成分頁的 PDF，不會開啟任何視窗。
- `open`：在 MarsDawn app 中開啟一或多個 Markdown 檔，讓人檢閱，也可以指定每個檔案要定位的行。

## 不做什麼

- 不從 stdin 讀取 Markdown，請傳入檔案路徑。
- 不把 PDF 寫到 stdout。PDF 一律寫成檔案，stdout 只輸出結果。
- 檔案已存在時不會覆寫，除非加上 `--force`。
- 不載入網路圖片，除非加上 `--allow-remote-images`，而且只走 https。
- 沒有安裝 MarsDawn 時，`open` 無法使用，會以代碼 3 結束。`export` 不需要 app。
- MarsDawn 1.0 還不會跳到 `open` 指定的行，會從檔案開頭顯示。
- 只能在 macOS 上執行。

## export

```
marsdawn export notes.md --json
```

在 `notes.md` 旁寫出 `notes.pdf`。選項：

- `-o, --output <path>`：PDF 的寫入位置。預設為輸入檔路徑，副檔名換成 `.pdf`。
- `--theme <dawn|classic|modern|vivid>`：使用主題的淺色色盤。預設為 `$MARSDAWN_THEME`，其次是 `dawn`。
- `--paper <a4|letter>`：紙張大小。預設為 `a4`。
- `--allow-remote-images`：算繪時載入網路上的 https 圖片。
- `--force`：輸出檔已存在時覆寫。
- `--json`：在 stdout 輸出一個 JSON 物件，而不是文字。

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

成功，離開代碼 0：

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`：寫出的 PDF 的絕對路徑。
- `pages`：頁數。
- `theme` 與 `paper`：實際使用的值。
- `diagramErrors`：每個算繪失敗的 Mermaid 圖表各一則訊息。PDF 仍會寫出。

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
```

- `path:line` 指定要定位的行。後面再接欄位，例如 `notes.md:120:8`，會被忽略。如果參數本身就是一個存在的檔名，就一律當成那個檔案，所以名為 `weird:12` 的檔案會照原名開啟。
- `--line <n>` 為單一檔案指定行號，包括檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。
- 行號範圍是 1 到 999999999，超出範圍是用法錯誤。
- 行號從 marsdawn 0.3.0 開始提供。MarsDawn 1.0 會打開檔案，但還不會跳到指定的行。

成功，離開代碼 0：

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`：每個檔案一個物件，順序與傳入時相同。`path` 是檔案的絕對路徑；只有指定了行號時才有 `line`。
- `app`：開啟它們的 MarsDawn app 路徑。

marsdawn 0.2.x 的 `opened` 是路徑字串的清單。如果需要同時處理兩種格式，請先查看 `marsdawn --version`。

## 失敗

加上 `--json` 時，失敗會在 stdout 輸出一個 JSON 物件，並以對應的代碼結束：

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`，`input_not_found`：輸入檔不存在、是資料夾，或不是 UTF-8 文字。
- `3`，`app_not_installed`：沒有安裝 MarsDawn。只有 `open` 會回傳這個代碼。
- `4`，`output_exists`：輸出檔已存在，請加上 `--force`。
- `5`，`export_failed`：匯出本身失敗。
- `64`：用法錯誤，例如未知的選項、無效的值、行號超出範圍，或 `--line` 搭配了多個檔案。這種錯誤一律以文字輸出到 stderr，即使加了 `--json` 也一樣。

## JSON Schema

每種 `--json` 結果的 JSON Schema（draft 2020-12）：

- [export.v1.json](/schemas/cli/export.v1.json): export 成功
- [open.v2.json](/schemas/cli/open.v2.json): open 成功，marsdawn 0.3.0 以後
- [error.v1.json](/schemas/cli/error.v1.json): 兩個指令的失敗結果
- [open.v1.json](/schemas/cli/open.v1.json): open 成功，marsdawn 0.2.x，當時 `opened` 是路徑清單

## 環境變數

- `MARSDAWN_THEME`：沒有傳入 `--theme` 時，`export` 使用的主題。未知的值會直接改用 `dawn`，不會報錯。

## 系統需求

- 這個工具需要 macOS 15 以上。在 Apple 晶片的 Mac 上，Homebrew 會安裝預先建置好的版本，不需要其他東西。自己建置時（在 Intel Mac 上，或從原始碼建置），需要 Swift 6.2 以上，也就是 Xcode 26 以上。
- MarsDawn app 需要 macOS 26 以上。

## 安裝

使用 Homebrew。在 Apple 晶片的 Mac 上，會直接安裝預先建置好的版本，幾秒就完成，不需要 Xcode。在 Intel Mac 上則會從原始碼編譯 marsdawn，需要幾分鐘，也需要 Xcode 26 以上。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

也可以從[原始碼](https://github.com/redtear1115/mars-dawn-kit)建置。第一次建置會下載相依套件並編譯，同樣需要幾分鐘。

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` 會印出版本號，例如 `0.3.0`，並以代碼 0 結束。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
