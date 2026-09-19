# 給 AI agent 的 marsdawn 參考

給呼叫 `marsdawn` 命令列工具的 AI agent 與腳本參考。本頁每個範例都用目前原始碼建置的工具實際執行過。

**要把 Markdown 檔轉成 PDF，執行 `marsdawn export notes.md --json`，再從 stdout 讀取一個 JSON 物件。**Mermaid 圖表與程式碼上色的呈現方式和 MarsDawn app 相同。`export` 不需要 app，`open` 需要。

## 能做什麼

- `export`：用和 MarsDawn app 相同的匯出程式，把一個 Markdown 檔輸出成分頁的 PDF，不會開啟任何視窗。
- `open`：在 MarsDawn app 中開啟一或多個 Markdown 檔，讓人審閱，也可以指定每個檔案要定位的行，或在視窗的側邊欄顯示一個資料夾。

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
marsdawn open . --json
marsdawn open notes.md --folder . --background --json
```

- `path:line` 指定要定位的行。後面再接欄位，例如 `notes.md:120:8`，會被忽略。如果參數本身就是一個存在的檔名，就一律當成那個檔案，所以名為 `weird:12` 的檔案會照原名開啟。
- `--line <n>` 為單一檔案指定行號，包括檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。
- 行號範圍是 1 到 999999999，超出範圍是用法錯誤。
- 行號從 marsdawn 0.3.0 開始提供。MarsDawn 1.0 會打開檔案，但還不會跳到指定的行。
- 資料夾參數會在視窗的側邊欄開啟，而不是當成文件，所以 `marsdawn open .` 會顯示目前的資料夾；`--folder <path>` 可以在開啟檔案的同時做到一樣的事。一個視窗的側邊欄只顯示一個資料夾：指定兩個是用法錯誤，同一個資料夾指定兩次則算一個。資料夾沒有行號，所以 `--line` 搭配資料夾是用法錯誤。沒有 `-a`：傳入它是用法錯誤，錯誤訊息會指向 `--folder`。
- `--background` 開啟時不把 MarsDawn 帶到最前面，適合在使用者做別的事時開檔的 agent。兩種情況的 JSON 都一樣。
- 資料夾與 `--background` 從 marsdawn 0.5.1 開始提供。

成功，離開代碼 0：

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`：每個檔案一個物件，順序與傳入時相同。`path` 是檔案的絕對路徑；只有指定了行號時才有 `line`。
- `app`：開啟它們的 MarsDawn app 路徑。

有資料夾時（marsdawn 0.5.1 以後），離開代碼 0：

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/project","requested":true},"ok":true,"opened":[{"path":"/path/to/project/notes.md"}]}
```

- `folder`：只有指定了資料夾時才有。`path` 是它的絕對路徑。`requested` 一律是 `true`：marsdawn 已請 MarsDawn 顯示這個資料夾，但無法得知側邊欄是否真的顯示了，因為 app 可能會先向使用者要求存取權限。請回報為「已要求」，而不是「已完成」。
- 只指定資料夾時，`opened` 是空的。

marsdawn 0.2.x 的 `opened` 是路徑字串的清單。如果需要同時處理兩種格式，請先查看 `marsdawn --version`。

## 失敗

加上 `--json` 時，失敗會在 stdout 輸出一個 JSON 物件，並以對應的代碼結束：

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`，`input_not_found`：輸入檔不存在、是資料夾，或不是 UTF-8 文字；或 `--folder` 的路徑不存在、不是資料夾。
- `3`，`app_not_installed`：沒有安裝 MarsDawn。只有 `open` 會回傳這個代碼。
- `4`，`output_exists`：輸出檔已存在，請加上 `--force`。
- `5`，`export_failed`：匯出本身失敗。
- `64`：用法錯誤，例如未知的選項、無效的值、行號超出範圍、`--line` 搭配了多個檔案或資料夾、指定了多個資料夾，或使用了 `-a`。這種錯誤一律以文字輸出到 stderr，即使加了 `--json` 也一樣。

## JSON Schema

每種 `--json` 結果的 JSON Schema（draft 2020-12）：

- [export.v1.json](/schemas/cli/export.v1.json): export 成功
- [open.v3.json](/schemas/cli/open.v3.json): open 成功，marsdawn 0.5.1 以後，包括在側邊欄顯示的資料夾
- [error.v1.json](/schemas/cli/error.v1.json): 兩個指令的失敗結果
- [open.v2.json](/schemas/cli/open.v2.json): open 成功，marsdawn 0.3.0 到 0.5.0
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

## 接下來

- 給讀指令檔而不是執行 shell 的 agent 用的一個檔案：[marsdawn skill](/zh-hant/cli/skill/)。
- 包住同一個 `export` 的 MCP 伺服器：[marsdawn-mcp](/zh-hant/cli/mcp/)。
- 這份 JSON 結果為什麼不花 agent 自己的 context：[節省 token 的審閱方式](/zh-hant/token-efficient-review/)。

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
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
