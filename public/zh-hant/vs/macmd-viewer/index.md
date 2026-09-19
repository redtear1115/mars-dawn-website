# MacMD Viewer 對比 MarsDawn。

兩者都是給 Mac 用的 app，都能把 Markdown 排版出來讀。MacMD Viewer 打開 `.md` 檔案，顯示排好版的頁面，但不能編輯它。MarsDawn 則是在同樣的預覽旁邊放了編輯器，讓你在同一個視窗裡寫和讀。以下逐項比較兩者的差異。

## 如果你只需要讀，不需要編輯

如果你的工作就是讀別人寫好的 Markdown，完全不用碰原始碼，MacMD Viewer 是合理的選擇：它就是為這件事做的，現在就能買，也能在比較舊的 macOS 上跑。當閱讀不是全部的工作時，MarsDawn 才值得，因為 agent 寫的 Markdown 通常還要再改一輪。

## 各自能做什麼

- **編輯：**MacMD Viewer 設計上就是唯讀。MarsDawn 邊編輯原始碼邊在旁邊排版，打字的同時就看得到改動。
- **預覽主題：**MacMD Viewer 內建 12 種文件主題。MarsDawn 有四種：Dawn、Classic、Modern 和 Vivid，各有淺色與深色。
- **圖表與數學式：**兩者都能畫出 Mermaid 圖表、也都有程式碼上色。MarsDawn 還能排版 KaTeX 數學式；MacMD Viewer 自己的介紹頁沒有提到數學式排版。
- **Finder 整合：**兩者都有 Finder 的快速查看擴充功能，對 `.md` 檔案按空白鍵就能看到排好版的頁面。
- **PDF 與列印：**兩者都能把排好版的頁面輸出或列印成 PDF。
- **系統需求：**MacMD Viewer 需要 macOS 14（Sonoma）以上。MarsDawn 需要 macOS 26（Tahoe）以上。
- **語言：**MarsDawn 的介面有英文、繁體中文、簡體中文和日文。MacMD Viewer 自己的資料沒有寫出介面語言，這頁就不比較這一項。

## 價格與購買方式

- **從哪裡買：**MacMD Viewer 從自己的網站直接下載，也上架 Homebrew 和 Setapp，但不在 Mac App Store 上；MarsDawn 只在 Mac App Store 上架。
- **價格：**MacMD Viewer 一台 Mac 一次 USD 19.99（三台的組合包和大量授權更貴）。MarsDawn 免費下載，之後以 USD 4.99 一次解鎖。
- **先試用：**MacMD Viewer 沒有免費試用，直接購買改用 14 天內可退款的保證。MarsDawn 在你付費之前，先給你 14 天的試用。
- **退款與更新：**MacMD Viewer 的退款和更新都在它自己的網站上處理。MarsDawn 透過 Apple 購買，退款和更新都走 Apple 的標準流程。
- **帳號：**兩者都不需要帳號就能使用。

## 現在就能免費試試看

MarsDawn 即將在 Mac App Store 上架，現在還沒開賣。在那之前，免費的 `marsdawn` 命令列工具今天就能把任何 Markdown 檔案轉成 PDF，Mermaid 圖表和程式碼上色都在，而且不需要安裝其他東西：

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 接下來

- 完整步驟：[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。
- MarsDawn 做不到的事：[這份清單](/zh-hant/limits/)。
- 命令列工具的所有選項：[命令列工具](/zh-hant/cli/)。

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
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
