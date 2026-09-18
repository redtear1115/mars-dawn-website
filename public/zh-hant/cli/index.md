# 命令列工具

免費的 `marsdawn` 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。

**marsdawn 免費、另外發佈，不透過 Mac App Store。**用 Homebrew 安裝，它會在你的 Mac 上從原始碼建置。`export` 可以單獨使用；`open` 需要 MarsDawn app。

要從 AI agent 或腳本呼叫 marsdawn？請看[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)，裡面有 JSON 輸出、Schema 和所有離開代碼。

## 安裝

使用 [Homebrew](https://brew.sh)：

```
brew tap redtear1115/tap && brew install marsdawn
```

Homebrew 會從原始碼編譯 marsdawn，需要幾分鐘。這個工具需要 macOS 15 以上，建置需要 Xcode 26 以上（Swift 6.2）。

也可以從[原始碼](https://github.com/redtear1115/mars-dawn-kit)用 Swift Package Manager 建置：

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

用 `marsdawn --version` 查看安裝的版本。

## 指令

### marsdawn open

在 MarsDawn 中開啟一個或多個 Markdown 檔案，方便審閱。需要先安裝 MarsDawn。

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
```

- `path:line`：請 MarsDawn 定位到那一行。後面再接欄位，例如 `notes.md:120:8`，會被忽略。如果有檔案的完整名稱就是這個參數，則視為那個檔案。
- `--line <n>`：同樣的功能，只用於單一檔案，也可以用在檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。
- 行號範圍是 1 到 999999999。
- MarsDawn 1.0 會打開檔案，但還不會跳到指定的行。
- `--json`：印出 JSON 結果，而不是文字。

行號功能從 marsdawn 0.3.0 開始提供。

### marsdawn export

把 Markdown 檔案輸出成分頁的 PDF，使用和 MarsDawn 輸出 PDF 相同的元件。不需要安裝 MarsDawn app。相對路徑的圖片，會以輸入檔案所在的資料夾為準。

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
- `3`：尚未安裝 MarsDawn（只有 `open` 會用到）。
- `4`：輸出檔已存在（可加上 `--force`）。
- `5`：輸出失敗。
- `64`：使用方式錯誤，包括行號超出範圍，或 `--line` 搭配了多個檔案。

## --json 輸出

成功時，`marsdawn open --json` 會印出 `ok`、`opened`（每個檔案的 `path`，有指定行號時另含 `line`）與 `app`（App 路徑）；`marsdawn export --json` 會印出 `ok`、`output`、`pages`、`theme`、`paper` 與 `diagramErrors`。失敗時兩者都會印出 `ok`、`error` 與 `message`。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是原生的 Mac Markdown 編輯器，支援即時預覽和 Mermaid 圖表，也能輸出 PDF。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.
