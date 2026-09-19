# 讓 agent 寫的 Markdown，被好好讀過一遍。

AI agent 寫 Markdown，你在 MarsDawn 裡讀，原始碼和排版後的頁面並排顯示，再把修改意見交回去。

即將在 Mac App Store 上架 · 免費試用 14 天，之後 USD 4.99 買一次 · 需要 macOS 26 以上 · [免費的 marsdawn CLI 現在就能用](/zh-hant/cli/)

![MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

## 整個循環

1. **Agent 動筆。**Claude Code、Cursor 或你的寫作助手先寫出 Markdown：README、規格文件，或一份設計筆記。
2. **你在 MarsDawn 裡讀。**Agent 執行 `marsdawn open SPEC.md`，或你自己打開檔案。圖表、數學式和程式碼都排好，旁邊就是原始碼。
3. **Agent 修改。**告訴它要改哪裡，改好之後，用同樣的方式再讀一次。

## 先試 agent 這一端

[marsdawn CLI](/zh-hant/cli/) 免費，輸出 PDF 不需要 app。裝好之後，你的 agent 就能把它寫的 Markdown 轉成 PDF，並從一行 JSON 得知每張 Mermaid 圖表是否都畫出來了。

```
brew tap redtear1115/tap
brew install marsdawn
marsdawn export SPEC.md --json
```

它只回一行：

```
{"diagramErrors":[],"ok":true,"output":"/path/to/SPEC.pdf","pages":3,"paper":"a4","theme":"dawn"}
```

所有選項、結束代碼和 JSON schema，都在[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)。

**讀 agent 寫的 Markdown。** MarsDawn 即將在 Mac App Store 上架。

## 其他頁面

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
- [English](https://marsdawn.southern-light.dev/index.md): A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.
