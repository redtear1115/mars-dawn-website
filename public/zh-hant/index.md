給建造者的前線工具

# 拿穩地圖。讀過黎明。

給要掌舵 agentic 開發的人用的 Markdown。

MarsDawn 是 macOS 原生的 Markdown 編輯器，有即時分割預覽、Mermaid 圖表、KaTeX 數學式、快速查看與 PDF 輸出，可免費試用 14 天，之後只要一次 USD 4.99 解鎖。

頁面上有一個可以操作的 MarsDawn 視窗，內容是 App 內建歡迎指南的一段。調色盤選單可以選外觀（系統、淺色、深色），並分別替淺色和深色從四個預覽主題（黎明、典雅、流行、活潑）裡選一個；工具列可以選三種版面（原始碼、並排、預覽）。

## 讀 agent 寫的 Markdown。

1. **Agent 動筆。**你的程式碼助手或寫作 agent 先寫出 Markdown：README、規格文件，或一份筆記。
2. **你在 MarsDawn 裡讀。**打開檔案，看排版後的頁面，Mermaid 圖表和程式碼上色都在，旁邊就是原始碼。
3. **Agent 修改。**提出修改意見，agent 改好之後，再打開來讀一次。

[如何審閱 agent 交回來的東西](/zh-hant/reading-agent-output/)。

## 現在就能做的事

免費的 `marsdawn` 命令列工具現在就能用。用 Homebrew 安裝：

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` 把 Markdown 檔輸出成 PDF，排版和 MarsDawn 的預覽一樣，不需要 app。
- `marsdawn open` 在 MarsDawn app 裡開啟檔案，讓你審閱。
- `--json` 回傳腳本和 agent 能解析的結果。

[命令列工具](/zh-hant/cli/) · [給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/) · [給 agent 的 skill](/zh-hant/cli/skill/) · [MCP 伺服器](/zh-hant/cli/mcp/)

## MarsDawn 是什麼樣的 app

- [為 Mac 而做](/zh-hant/native/)：原生視窗、分頁、自動儲存、快速查看。
- [你寫的內容留在你的 Mac 上](/zh-hant/yours/)：不需要帳號，沒有同步，也沒有雲端。
- [免費試用，買一次就好](/zh-hant/pay-once/)：免費試用 14 天，之後 USD 4.99 買一次，沒有訂閱。

購買前先知道。 [MarsDawn 做不到的事](/zh-hant/limits/)

## 常見問題

### MarsDawn 是什麼？

MarsDawn 是 Mac 上原生的 Markdown 編輯器。原始碼旁邊有即時預覽，能畫出 Mermaid 圖表和 KaTeX 數學式，在 Finder 用快速查看預覽 Markdown 檔案，也能輸出 PDF。

### MarsDawn 要訂閱嗎？

不用。MarsDawn 免費下載，14 天內所有功能都能試用；之後一次 USD 4.99 的 App 內購買就能永久解鎖。沒有任何續訂，也不需要帳號。

### MarsDawn 有 iPhone 或 iPad 版嗎？

沒有。MarsDawn 是 Mac app，需要 macOS 26 或更新版本，沒有 iPhone 或 iPad 版。

### Claude Code 可以用 MarsDawn 開檔案嗎？

可以。免費的 marsdawn 命令列工具有 open 指令，能用 MarsDawn 開啟 Markdown 檔案，所以 Claude Code，或任何能執行 shell 指令的 agent，都能呼叫它。另有一個需要自行啟用的 Claude Code hook，可以在 Claude 寫入或編輯 Markdown 檔案時自動開啟。

### 試用結束後，快速查看還能用嗎？

能。不論試用是否進行中，Finder 裡的快速查看都會繼續顯示你的 Markdown 檔案。試用結束、尚未解鎖時，在 MarsDawn 裡開啟的文件內容會被遮住。

## App 實際的樣子

### [為 Mac 而做](/zh-hant/native/)

![MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

這張截圖裡：

1. 原生的 Mac 視窗。
2. Mac 原生的文字編輯器，附 Markdown 語法上色。
3. ⌘1 原始碼、⌘2 並排、⌘3 預覽。
4. 頁面會隨著打字更新。

### [輸出 PDF](/zh-hant/pdf/)

![用 MarsDawn 輸出的 PDF，在內建的 PDF 檢視器中開啟，旁邊有頁面縮圖。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

這張截圖裡：

1. Mermaid 圖表直接畫進 PDF。
2. 程式碼保留語法上色。

## 其他頁面

- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hant/quicklook/index.md): 在 Finder 選取 Markdown 檔案後按空白鍵，就能看到排版後的頁面，Mermaid 圖表、KaTeX 數學式和程式碼上色都在。MarsDawn 的快速查看不受試用期限制。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。在瀏覽器裡打造自己的主題，也可以逛逛社群主題庫。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽社群投稿的 MarsDawn 預覽主題，依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造一個自己的主題，不用安裝，也不用 git。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [讀懂 agent 交回來的 Markdown](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [編者的閱讀筆記](https://marsdawn.southern-light.dev/zh-hant/reading-notes/index.md): 六篇短筆記，談打造 AI agent 的人實際主張了什麼——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 與 Andrew Ng——以及這些主張對「要讀 agent 交回來的東西」的人分別意味著什麼。
- [閱讀筆記：Anthropic](https://marsdawn.southern-light.dev/zh-hant/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月發表的指南把 workflow 和 agent 分開來看，並描述了五種 workflow 模式，其中一種讓另一次 LLM 呼叫來審查。這對落進你資料夾的東西來說，意味著什麼。
- [閱讀筆記：Chip Huyen](https://marsdawn.southern-light.dev/zh-hant/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章裡，把 agent 的動作分成 read-only 和 write action 兩種。這個分法為什麼是核準計畫前，快速拓出該多看一眼的那一行的好方法。
- [閱讀筆記：Lilian Weng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被廣泛引用的整理，把 LLM agent 描述成大腦加上規劃、記憶、工具使用。每個部件通常會留給你讀什麼，以及她點名的一個限制：計畫遇到意外不太會調整。
- [閱讀筆記：Harrison Chase](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [閱讀筆記：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [閱讀筆記：Andrew Ng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/index.md): Native Markdown editor for Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, $4.99 once.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): Mac 原生 Markdown 编辑器：实时分栏预览、Mermaid、KaTeX、快速查看、PDF 导出。免费试用，只需买一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): Mac 向けネイティブ Markdown エディタ。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Éditeur Markdown natif pour Mac : aperçu en direct à côté de la source, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Editor de Markdown nativo para Mac: vista previa en vivo junto al código, Mermaid, KaTeX, Vista rápida, exportación a PDF. Pruébalo gratis, 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
