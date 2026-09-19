# 在 Mac 上，怎麼看 Markdown 檔案。

`.md` 檔案是純文字。標題、粗體、表格和圖表，都是用記號寫成的：`#` 代表標題，`**` 包住粗體，直線符號畫出表格，`mermaid` 程式碼區塊則是一張圖。用純文字編輯器打開，看到的就是這些記號。想照作者的意思讀到排好的頁面，就需要有東西把它排版出來。

## 現在就能用，而且免費：轉成 PDF

免費的 `marsdawn` 命令列工具，能把 Markdown 檔案排版成 PDF，任何一台 Mac 都打得開。表格、數學式、Mermaid 圖表和程式碼上色都會排好，而且不需要安裝其他東西，連 MarsDawn app 都不用。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` 會在 Markdown 檔案旁邊寫出 `notes.pdf`，`open` 會用你的 PDF 檢視器打開它。這個工具需要 macOS 15 以上。完整步驟和一頁實際匯出的結果，請看[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。

## 即將推出：在 MarsDawn 裡讀

MarsDawn 是為 Mac 做的 Markdown 編輯器，即將在 Mac App Store 上架。打開 `.md` 檔案，排好的頁面就在原始碼旁邊：

- 預覽會隨著你打字即時更新，兩邊的窗格一起捲動。
- Mermaid 流程圖和循序圖直接畫在預覽裡，程式碼區塊也會上色。
- 在 Finder 裡對 Markdown 檔案按空白鍵，就有「快速查看」預覽，圖表也在。
- 想改的時候，原始碼就在旁邊。MarsDawn 是編輯器，不只是檢視器。

如果這份檔案是 AI agent 寫的，這正是 MarsDawn 要支援的循環：agent 寫，你讀排好的頁面，agent 再修改。請看[首頁](/zh-hant/)，想讓 agent 幫你開檔案，請看[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)。

## 接下來

- 命令列工具的所有選項：[命令列工具](/zh-hant/cli/)。
- MarsDawn 做不到的事：[這份清單](/zh-hant/limits/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。一份誠實、附來源的比較。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.
