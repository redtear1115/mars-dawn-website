# 讓 agent 幫你做出 PDF。

這個 skill 是一個 Markdown 檔案。它教寫程式的 agent 安裝 `marsdawn`、確認它能用、把文件匯出成 PDF 並讀懂結果，這樣寫出 Markdown 的 agent，也能把 PDF 交給你。

## 在 Claude Code 中安裝

```
mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md
```

需要做出 PDF 時，Claude Code 會自動載入它，你也可以用 `/marsdawn` 自己執行。它只是[一個簡短的檔案](/cli/skill/SKILL.md)，安裝前先讀一遍。

其他 agent 也能用同一個檔案。它是純 Markdown，只有說明和指令，讓你的 agent 讀這個網址，或直接貼給它就好。這個檔案是英文的。

## 它教什麼

- 如果沒有 `marsdawn`，就用 Homebrew 安裝，再用 `marsdawn --version` 確認版本，而不是假設某個版本。
- 用 `marsdawn export … --json` 匯出，並讀懂結果：PDF 存到哪裡、有幾頁，以及有沒有 Mermaid 圖表沒畫出來。
- 依結束代碼分辨失敗的原因：找不到檔案、PDF 已經存在、匯出失敗、選項錯誤。
- 只有裝了 MarsDawn app 才用 `open`，而且絕不用它來做 PDF。

## 它不會做的事

- 它不會自己取得執行任何東西的權限。你的 agent 在安裝或執行 `marsdawn` 之前，仍然會先問你，就像執行其他指令一樣。
- 它不會把你的文件傳到任何地方。`marsdawn` 在你的 Mac 上產生 PDF，除非你加上 `--allow-remote-images`，否則不會載入網路上的圖片。

完整的規格，每個欄位和每個代碼，都在[給 AI agent 的 marsdawn 參考](/zh-hans/cli/agents/)裡。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [English](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.
