# 命令列工具

免費的 `marsdawn` 命令列工具：從終端機或 LLM agent 把 Markdown 匯出成 PDF；裝了 MarsDawn app 的話，也能用它開啟檔案。

**marsdawn 免費、另外發佈，不透過 Mac App Store。**用 Homebrew 安裝，在 Apple 晶片的 Mac 上裝好就能直接使用。`export` 可以單獨使用；`open` 需要 MarsDawn app。

要從 AI agent 或腳本呼叫 marsdawn？請看[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)，裡面有 JSON 輸出、Schema 和所有離開代碼；如果你的 agent 是透過 MCP 呼叫工具，也可以看[MCP 伺服器](/zh-hant/cli/mcp/)。

## 安裝

使用 [Homebrew](https://brew.sh)：

```
brew tap redtear1115/tap && brew install marsdawn
```

在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成，不需要另外安裝任何東西。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上（Swift 6.2）。這個工具需要 macOS 15 以上。

也可以從[原始碼](https://github.com/redtear1115/mars-dawn-kit)用 Swift Package Manager 建置：

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

用 `marsdawn --version` 查看安裝的版本。

## 指令

### marsdawn open

在 MarsDawn app 中開啟一個或多個 Markdown 檔案，方便審閱。需要先安裝這個 app：沒有安裝時，`marsdawn open` 會以代碼 3 結束，並說明沒有安裝 MarsDawn。`export` 不需要這個 app。

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
```

- `path:line`：請 MarsDawn 定位到那一行。後面再接欄位，例如 `notes.md:120:8`，會被忽略。如果有檔案的完整名稱就是這個參數，則視為那個檔案。
- `--line <n>`：同樣的功能，只用於單一檔案，也可以用在檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。
- 行號範圍是 1 到 999999999。
- MarsDawn 1.0 會打開檔案，並跳到指定的行。
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

| 代碼 | 意思 | 怎麼處理 |
|---|---|---|
| `0` | 成功。 | 加了 `--json` 時，讀 stdout 上的那一行 JSON |
| `2` | 找不到輸入檔。 | 檢查路徑和檔名 |
| `3` | 尚未安裝 MarsDawn（只有 `open` 會用到）。 | 安裝 app，或改用不需要 app 的 `export` |
| `4` | 輸出檔已存在（可加上 `--force`）。 | 加上 `--force` 覆寫，或用 `-o` 寫到別處 |
| `5` | 輸出失敗。 | 讀 JSON 結果裡的 `message` |
| `64` | 使用方式錯誤，包括行號超出範圍，或 `--line` 搭配了多個檔案。 | 修正選項或值；這種錯誤以文字輸出到 stderr，即使加了 `--json` 也一樣 |

## --json 輸出

成功時，`marsdawn open --json` 會印出 `ok`、`opened`（每個檔案的 `path`，有指定行號時另含 `line`）與 `app`（App 路徑）；`marsdawn export --json` 會印出 `ok`、`output`、`pages`、`theme`、`paper` 與 `diagramErrors`。失敗時兩者都會印出 `ok`、`error` 與 `message`。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
