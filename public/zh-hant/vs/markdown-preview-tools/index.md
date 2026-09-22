# 在別處看 Markdown，對比 MarsDawn。

如果你手邊剛好開著 VS Code、瀏覽器或 Claude Desktop，用它們順手看一眼 Markdown 檔案也合理。以下是它們各自實際排版出什麼、要花多少功夫才能看到，和在 MarsDawn 裡打開同一份檔案的比較。

## VS Code 內建的預覽

在 VS Code 按 `⌘⇧V`，就會用內建的預覽窗格排版出 Markdown 檔案，免費，不用另外安裝。從 VS Code 1.121（2026 年 5 月）開始，這個預覽也能原生畫出 Mermaid 圖表——微軟把一個 Mermaid 擴充功能併進了 VS Code 本體，以前需要另外裝擴充功能，現在不用了。它做不到的：這是編輯器裡的一個預覽窗格，不是為了閱讀而做的編輯器——窗格旁邊還有檔案樹、終端機和 VS Code 能顯示的其他所有面板，而 VS Code 本身是 Electron app，你裝的是一整套開發環境，不是一個用來讀檔案的工具。

## 看本機檔案的瀏覽器擴充功能

看本機 `.md` 檔案，沒有哪一個瀏覽器擴充功能是主流：Local Markdown Viewer、Markdown Viewer、MarkView 等等做的事都差不多，沒有哪一個是預設會裝的。每一個都要先做同一件事才能打開任何檔案：把該擴充功能的「允許存取檔案網址」打開，因為瀏覽器預設不讓擴充功能讀取 `file://` 開頭的頁面。這個權限每個擴充功能只要開一次，但也很容易忘記自己開過，或忘記為什麼要開。開了之後，檔案會顯示在瀏覽器分頁裡——也就是說，看一個檔案要開一整個瀏覽器。

## Claude Desktop 的檔案預覽

Claude Desktop 顯示的是已經在 Project 或對話裡的檔案。它不是為了瀏覽磁碟上任意檔案而做的——你能看的是對話裡已經有的東西，不是一個可以一直開在旁邊的筆記資料夾。Anthropic 自己列出[可以上傳的檔案類型](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)是 PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON 和 XLSX，裡面沒有 Markdown。

## 為了讀一份檔案，背後跑著一整套瀏覽器引擎

VS Code 是 Electron app：內建一套 Chromium 和 Node.js 執行環境，不是原生的 Mac app。走瀏覽器擴充功能這條路，則是真的在瀏覽器裡執行。不管哪一種，看一份 Markdown 檔案都要有一整套瀏覽器引擎在背後跑。MarsDawn 是原生的 AppKit app：沒有內建的瀏覽器執行環境、直接打開任何本機檔案，不用裝擴充功能，也不用記得開過哪個權限。

## 接下來

- MarsDawn 也做不到的事：[這份清單](/zh-hant/limits/)。
- 今天就能免費把任何 Markdown 檔案轉成 PDF：[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。
- 和一個 Mac 原生的檢視器比較：[MacMD Viewer 對比 MarsDawn](/zh-hant/vs/macmd-viewer/)。

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
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [English](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/markdown-preview-tools/index.md): VS Code の内蔵プレビュー、ブラウザ拡張機能、Claude Desktop のファイルプレビューで Markdown を読む場合と、MarsDawn を比較：それぞれが実際にレンダリングするもの、1つのファイルを開くのにかかる手間。
