# 命令列工具

免費的 `marsdawn` 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。

**marsdawn 免費、另外發佈，不透過 Mac App Store。**目前尚未發佈到 Homebrew，需要用 Swift Package Manager 自行建置。兩個指令都需要先安裝 MarsDawn。

要從 AI agent 或腳本呼叫 marsdawn？請看[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)，裡面有 JSON 輸出、Schema 和所有離開代碼。

## 安裝

下載[原始碼](https://github.com/redtear1115/mars-dawn-kit)，並用 Swift Package Manager 執行：

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift run marsdawn open notes.md
```

## 指令

### marsdawn open

在 MarsDawn 中開啟一個或多個 Markdown 檔案，方便審閱。需要先安裝 MarsDawn。

```
marsdawn open notes.md
```

- `--json`：印出 JSON 結果，而不是文字。

### marsdawn export

把 Markdown 檔案輸出成分頁的 PDF，使用和 MarsDawn 輸出 PDF 相同的元件。同樣需要先安裝 MarsDawn。相對路徑的圖片，會以輸入檔案所在的資料夾為準。

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`：PDF 的輸出位置，預設是把輸入檔的副檔名換成 `.pdf`。
- `--theme <dawn|classic|modern|vivid>`：預覽主題的淺色版本，預設讀取 `$MARSDAWN_THEME`，否則用 `dawn`。
- `--paper <a4|letter>`：紙張大小，預設 `a4`。
- `--allow-remote-images`：輸出時載入網路圖片，預設關閉。
- `--force`：如果輸出檔已存在就直接覆蓋。
- `--json`：印出 JSON 結果，而不是文字。

## $MARSDAWN_THEME 環境變數

沒有傳入 `--theme` 時，`export` 會讀取 `$MARSDAWN_THEME` 環境變數，值必須是 `dawn`、`classic`、`modern` 或 `vivid` 其中之一，其他值都會改用 `dawn`。這個工具不會讀取 App 本身的主題設定，因為讀取其他 App 的容器可能觸發 macOS 隱私權提示。

## 覆蓋檔案的規則

`export` 預設不會覆蓋已存在的輸出檔，除非加上 `--force`。

## 結束代碼

- `0`：成功。
- `2`：找不到輸入檔。
- `3`：尚未安裝 MarsDawn。
- `4`：輸出檔已存在（可加上 `--force`）。
- `5`：輸出失敗。
- `64`：使用方式錯誤。

## --json 輸出

成功時，`marsdawn open --json` 會印出 `ok`、`opened`（檔案路徑）與 `app`（App 路徑）；`marsdawn export --json` 會印出 `ok`、`output`、`pages`、`theme`、`paper` 與 `diagramErrors`。失敗時兩者都會印出 `ok`、`error` 與 `message`。

## 需要先安裝 MarsDawn

`open` 和 `export` 都需要先從 Mac App Store 安裝 MarsDawn；`export` 雖然使用和 App 相同的元件，仍會先檢查 App 是否已安裝。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是原生的 Mac Markdown 編輯器，支援即時預覽和 Mermaid 圖表，也能輸出 PDF。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端，你的文件留在你的 Mac 上。
- [買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 售價 USD 4.99，買一次就好。沒有訂閱、不需要帳號，也沒有付費進階版。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 輸出成 PDF 或列印，Mermaid 圖表、程式碼上色都會保留，分頁也經過安排。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 原生視窗與分頁、自動儲存、版本記錄、快速查看，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.
