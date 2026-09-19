# 用命令列，把 Markdown 轉成 PDF。

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

## 如果沒有成功

- `A full installation of Xcode.app 26.0 is required to compile this software.` 代表 Homebrew 正在從原始碼建置 `marsdawn`，這在 Intel Mac 上會發生。從 App Store 安裝 Xcode 26 以上，再重新安裝一次。
- `marsdawn: No such file: …` 路徑沒有指到檔案。確認檔名，或在檔案所在的資料夾裡執行指令。
- `… already exists. Pass --force to replace it.` 同名的 PDF 已經存在。加上 `--force` 覆蓋它，或用 `-o` 寫到別的地方。
- `Error: The value '…' is invalid for '--theme <theme>'.` 主題或紙張大小不是它認得的。主題有 dawn、classic、modern 和 vivid，紙張是 a4 或 letter。

## 接下來

- 所有選項和它印出的 JSON：[命令列工具](/zh-hant/cli/)。
- 讓寫程式的 agent 幫你做這件事：[marsdawn 的 agent skill](/zh-hant/cli/skill/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是原生的 Mac Markdown 編輯器，為 AI 工作流程而生：agent 寫 Markdown，你用即時預覽檢閱，agent 再修改。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端，你的文件留在你的 Mac 上。
- [買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 售價 USD 4.99，買一次就好。沒有訂閱、不需要帳號，也沒有付費進階版。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 輸出成 PDF 或列印，Mermaid 圖表、程式碼上色都會保留，分頁也經過安排。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 原生視窗與分頁、自動儲存、版本記錄、快速查看，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：從終端機或 LLM agent 把 Markdown 匯出成 PDF；裝了 MarsDawn app 的話，也能用它開啟檔案。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [English](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Turn a Markdown file into a PDF with the free marsdawn command-line tool. Install it with Homebrew, run one command, and get tables, math, Mermaid diagrams and highlighted code on the page.
