# 給 AI agent 的 marsdawn 參考

給呼叫 `marsdawn` 命令列工具的 AI agent 與腳本參考。本頁每個範例都用目前原始碼建置的工具實際執行過。

**要把 Markdown 檔轉成 PDF，執行 `marsdawn export notes.md --json`，再從 stdout 讀取一個 JSON 物件。**Mermaid 圖表與程式碼上色的呈現方式和 MarsDawn app 相同。需要先安裝 MarsDawn。

## 能做什麼

- `export`：用和 MarsDawn app 相同的匯出程式，把一個 Markdown 檔輸出成分頁的 PDF，不會開啟任何視窗。
- `open`：在 MarsDawn app 中開啟一或多個 Markdown 檔，讓人檢閱。

## 不做什麼

- 不從 stdin 讀取 Markdown，請傳入檔案路徑。
- 不把 PDF 寫到 stdout。PDF 一律寫成檔案，stdout 只輸出結果。
- 檔案已存在時不會覆寫，除非加上 `--force`。
- 不載入網路圖片，除非加上 `--allow-remote-images`，而且只走 https。
- 沒有安裝 MarsDawn 就無法使用，兩個指令都會以代碼 3 結束。
- 沒有 `--version` 選項，傳入會被視為用法錯誤。
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
```

成功，離開代碼 0：

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":["/path/to/notes.md"]}
```

- `opened`：已開啟檔案的絕對路徑。
- `app`：開啟它們的 MarsDawn app 路徑。

## 失敗

加上 `--json` 時，失敗會在 stdout 輸出一個 JSON 物件，並以對應的代碼結束：

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`，`input_not_found`：輸入檔不存在、是資料夾，或不是 UTF-8 文字。
- `3`，`app_not_installed`：沒有安裝 MarsDawn。
- `4`，`output_exists`：輸出檔已存在，請加上 `--force`。
- `5`，`export_failed`：匯出本身失敗。
- `64`：用法錯誤，例如未知的選項或無效的值。這種錯誤一律以文字輸出到 stderr，即使加了 `--json` 也一樣。

## JSON Schema

每種 `--json` 結果的 JSON Schema（draft 2020-12）：

- [export.v1.json](/schemas/cli/export.v1.json): export 成功
- [open.v1.json](/schemas/cli/open.v1.json): open 成功
- [error.v1.json](/schemas/cli/error.v1.json): 兩個指令的失敗結果

## 環境變數

- `MARSDAWN_THEME`：沒有傳入 `--theme` 時，`export` 使用的主題。未知的值會直接改用 `dawn`，不會報錯。

## 系統需求

- 這個工具需要 macOS 15 以上。建置需要 Swift 6.2 以上，也就是 Xcode 26 以上。
- MarsDawn app 需要 macOS 26 以上。

## 安裝

從[原始碼](https://github.com/redtear1115/mars-dawn-kit)建置。第一次建置會下載相依套件並編譯，需要幾分鐘。

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是原生的 Mac Markdown 編輯器，支援即時預覽和 Mermaid 圖表，也能輸出 PDF。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端，你的文件留在你的 Mac 上。
- [買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 售價 USD 4.99，買一次就好。沒有訂閱、不需要帳號，也沒有付費進階版。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 輸出成 PDF 或列印，Mermaid 圖表、程式碼上色都會保留，分頁也經過安排。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 原生視窗與分頁、自動儲存、版本記錄、快速查看，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn: commands, JSON output, schemas, exit codes and requirements.
