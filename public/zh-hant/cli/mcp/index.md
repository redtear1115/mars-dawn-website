# 呼叫 marsdawn 的三種方式。

MarsDawn 沒有自己的 AI 模型：它是為了審閱 Markdown 而做的，不是用來寫的，所以是哪個 agent 或模型寫出這份 Markdown 並不重要。agent 或腳本呼叫 `marsdawn` 有三種方式，最後都會執行同一個 `export`。

**挑你的工具支援的那一種：免費的 `marsdawn` CLI、純 Markdown 的 skill 檔案，或是 [marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) 這個 MCP 伺服器。**三者都呼叫同一個 `marsdawn export`，回傳一樣的 JSON 結果。

## CLI

`marsdawn export notes.md --json` 可以被任何能執行 shell 指令的 agent 或腳本呼叫，因為是命令列工具，天生就跟模型無關。它回傳的每個欄位都寫在[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)裡，那一頁是 JSON schema 的權威來源，底下另外兩種方式都會連回去。

## Skill 檔案

如果你的 agent 讀的是純 Markdown 指令，而不是直接執行 shell——目前是 Claude Code——[marsdawn skill](/zh-hant/cli/skill/) 就是一個檔案，教它安裝 marsdawn、執行 `export`、讀懂結果。因為它就是純 Markdown，其他會讀指令檔的 agent 也能用同一個檔案。

## MCP 伺服器

[marsdawn-mcp](https://github.com/redtear1115/marsdawn-mcp) 是另一個獨立、公開、Apache-2.0 授權的 repository。它是一個只有一個工具的 MCP 伺服器，`export_markdown_to_pdf`，包住 `marsdawn export --json`：把 MCP 用戶端指向它，工具呼叫回傳的 JSON 和 CLI 一樣。

- **取得方式：**以 MCP Bundle（`marsdawn.mcpb`）的形式附在[GitHub release](https://github.com/redtear1115/marsdawn-mcp/releases) 上，或從原始碼以 stdio 執行伺服器。
- **Registry：**還沒上架 MCP Registry（目前版本：0.1.0）。要靠 registry 搜尋找到它之前，請先到 repository 確認目前狀態。
- **託管：**只能自架，沒有代管服務。伺服器跑在你自己的機器上，就在 marsdawn 旁邊。
- **系統需求：**macOS、marsdawn 0.5.0 以上，以及執行伺服器需要的 Node.js 20 以上。

## 同一個 export，三扇門

不管從哪個介面呼叫，底層行為都一樣：同一套輸出程式、同樣的主題和紙張大小，Mermaid 圖表畫不出來時也是同樣的 `diagramErrors`。這頁不重複那份規格——[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)裡有完整內容。

## 接下來

- 完整 JSON schema 和所有離開代碼：[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)。
- 給 Claude Code 等 agent 用的一個檔案：[marsdawn skill](/zh-hant/cli/skill/)。
- 精簡的 JSON 結果為什麼對 agent 自己的 context 很重要：[節省 token 的審閱方式](/zh-hant/token-efficient-review/)。

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
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [English](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
