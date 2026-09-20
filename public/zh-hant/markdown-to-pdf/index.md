# Markdown 轉 PDF 工具：在 Mac 上用命令列轉檔。

免費的 `marsdawn` 工具只要一個指令，就能把 Markdown 檔案轉成 PDF。表格、數學式、Mermaid 圖表和程式碼上色，都會照原始檔的樣子呈現，而且不需要安裝其他東西，連 MarsDawn app 都不用。

## 安裝

```
brew install redtear1115/tap/marsdawn
marsdawn --version
```

在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上。這個工具需要 macOS 15 以上，`marsdawn --version` 會印出你裝到的版本。

## 存一份文件

把下面的內容貼進一個叫 `plan.md` 的檔案：

````
# 計畫：讓輸出更快

這份計畫由 agent 撰寫，你審閱後再把它轉成 PDF。

## 步驟

| 步驟 | 負責 | 狀態 |
|------|------|------|
| 找出慢的頁面 | Agent | 完成 |
| 快取算好的圖表 | Agent | 審閱中 |

目標是 50 頁的文件在 $t < 2\,\text{s}$ 內完成：

$$
t_{\text{total}} = \sum_{i=1}^{n} t_i
$$

```mermaid
graph LR
  草稿 --> 審閱 --> 發佈
```

```swift
let pdf = try export("plan.md")
```
````

## 匯出

```
marsdawn export plan.md
```

它會在原始檔旁邊寫出 `plan.pdf`，並印出存放的位置：

```
Exported /Users/you/plan.pdf (1 page)
```

這是那一頁，擷取自 `marsdawn` 0.5.0 的實際執行結果：

![匯出的 PDF：標題、步驟表格、行內與獨立的數學式、「草稿、審閱、發佈」流程圖，以及一行上色的 Swift 程式碼。](/assets/cli/plan-zh.png)

## 選主題、紙張大小和檔名

```
marsdawn export plan.md --theme classic --paper letter -o handout.pdf
```

- `--theme`：dawn、classic、modern 或 vivid，使用主題的淺色配色。沒有指定時，`export` 會用 `$MARSDAWN_THEME`，再來才是 dawn。
- `--paper`：a4 或 letter，預設是 a4。
- `-o`：PDF 要寫到哪裡，而不是寫在原始檔旁邊。
- `--allow-remote-images`：轉檔時載入網路上的圖片。沒加這個選項就不會載入。

## 如果沒有成功

- `A full installation of Xcode.app 26.0 is required to compile this software.` 代表 Homebrew 正在從原始碼建置 `marsdawn`，這在 Intel Mac 上會發生。從 App Store 安裝 Xcode 26 以上，再重新安裝一次。
- `marsdawn: No such file: …` 路徑沒有指到檔案。確認檔名，或在檔案所在的資料夾裡執行指令。
- `… already exists. Pass --force to replace it.` 同名的 PDF 已經存在。加上 `--force` 覆蓋它，或用 `-o` 寫到別的地方。
- `Error: The value '…' is invalid for '--theme <theme>'.` 主題或紙張大小不是它認得的。主題有 dawn、classic、modern 和 vivid，紙張是 a4 或 letter。

## 接下來

- 所有選項和它印出的 JSON：[命令列工具](/zh-hant/cli/)。
- 讓寫程式的 agent 幫你做這件事：[marsdawn 的 agent skill](/zh-hant/cli/skill/)。
- 四種預覽主題，以及 PDF 輸出接下來的規劃：[預覽主題與 PDF 輸出](/zh-hant/themes/)。
- 把 PDF 交給不寫 Markdown 的人：[分享 PDF](/zh-hant/sharing-exported-pdfs/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [English](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学式、Mermaid 图表和代码上色都在。
- [日本語](https://marsdawn.southern-light.dev/ja/markdown-to-pdf/index.md): 無料の marsdawn コマンドラインツールで、Mac 上の Markdown を PDF に変換します。Homebrew でインストールし、コマンドを一つ実行するだけ：表、数式、Mermaid、コードに対応。
