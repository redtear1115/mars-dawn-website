# MacMD Viewer 對比 MarsDawn。

兩者都是給 Mac 用的 app，都能把 Markdown 排版成完整的頁面來讀。MacMD Viewer 打開 `.md` 檔案並顯示出來；它設計上就是唯讀，不會儲存對檔案的任何更動。MarsDawn 則是在同樣的預覽旁邊放了編輯器，讓你在同一個視窗裡寫和讀。這一頁把兩者逐項並排，MacMD Viewer 的每一項事實都附上來源，也會說明什麼情況下 MacMD Viewer 是比較好的選擇。

以上依 2026 年 10 月 15 日 MacMD Viewer 自己的網站和 repo 核對（版本 1.7.0，2026 年 10 月 10 日發布）。如果有哪裡過時了，請照[支援頁](/zh-hant/support/)上的聯絡方式告訴我們。

## 它是什麼、能做什麼

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 是什麼 | 檢視器：「唯讀，不會儲存對原始檔的更動」[[S1](#s1), [S9](#s9)] | 有即時預覽的編輯器：左邊寫 Markdown，右邊看排版後的頁面，三種版面（原始碼、並排、預覽） |
| 編輯 | 不能 [[S1](#s1), [S7](#s7), [S9](#s9)] | 可以。排版後的頁面本身不能直接編輯，要編輯旁邊的原始碼 |
| 即時預覽 | 顯示檔案；別的編輯器儲存檔案後會自動重新載入 [[S9](#s9)] | 打字時就更新。別的 app 改了檔案，MarsDawn 會重新載入並保留你的位置，前提是你自己沒有未儲存的修改。 |
| Mermaid | 有：流程圖、循序圖、狀態圖、甘特圖、圓餅圖等，離線可用 [[S1](#s1), [S3](#s3), [S7](#s7)] | 有 |
| 數學式 | 沒有：它的 README 寫明「不顯示數學式（LaTeX／KaTeX）」[[S7](#s7)] | 有，KaTeX |
| 程式碼上色 | 有 [[S1](#s1), [S9](#s9)] | 有 |
| 主題 | 12 種文件主題 [[S1](#s1), [S7](#s7)] | 內建 4 種（黎明、典雅、流行、活潑），各有淺色與深色，主題庫還有更多 |
| 分頁 | 有，選用，預設關閉（1.6.0 起）[[S5](#s5), [S8](#s8)] | 有 |
| PDF 輸出 | 有，單一連續頁面，用目前的主題，無浮水印 [[S3](#s3), [S9](#s9)] | 有，分頁輸出，用主題的淺色配色；分頁時盡量不切開短的程式碼 |
| 列印 | 有，走 macOS 的列印對話框 [[S3](#s3), [S9](#s9)] | 有 |
| Finder 的快速查看 | 有，已包含；要在系統設定裡啟用；使用你選的主題 [[S4](#s4)] | 有，不論有沒有試用都能用；使用你選的主題 |
| 快速查看裡的 Mermaid 與數學式 | Mermaid：有 [[S4](#s4)]。數學式：沒有，它不顯示數學式 [[S7](#s7)] | 有，兩者都會畫出來 |
| 命令列 | 沒有描述獨立的命令列工具。它有 `markdownviewer://` URL scheme，以及用來開啟檔案的 Claude Code 外掛和 hook [[S6](#s6)] | 免費的 `marsdawn` 工具：`marsdawn export` 不需要 app 就能輸出 PDF，`marsdawn open` 能在指定行開啟檔案 |
| 介面語言 | 自己的資料沒有寫出 [[S1](#s1), [S3](#s3), [S7](#s7)] | 英文、繁體中文、簡體中文、日文、德文、法文、西班牙文和韓文 |
| 系統需求 | macOS 14（Sonoma）以上；Apple 晶片與 Intel [[S1](#s1), [S7](#s7)] | macOS 26（Tahoe）以上 |
| 其他平台 | 只有 Mac [[S1](#s1)] | Mac；iPhone 和 iPad 上只能閱讀 |

## 價格與購買方式

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 從哪裡買 | 自己的網站、Homebrew 或 Setapp；沒有 Mac App Store 上架 [[S2](#s2), [S7](#s7)] | 只在 Mac App Store |
| 價格 | 一台使用中的 Mac 一次 USD 19.99（可以移到另一台 Mac）；Family Pack 3 把 USD 39.99；10 把 USD 129 [[S2](#s2)] | 免費下載，之後一次 USD 4.99 |
| 先試用 | 沒有試用，也沒有免費版；直接購買 14 天內全額退款 [[S2](#s2)] | 14 天免費試用，所有功能都能用 |
| 退款 | 14 天內，透過它自己的支援信箱 [[S2](#s2)] | 透過 Apple |
| 更新 | 同一主版本內的更新免費 [[S2](#s2)]；直接下載的版本用 Sparkle 自動更新 [[S7](#s7)] | 透過 Mac App Store |
| 需要帳號 | 不用 [[S2](#s2)] | 不用 |
| 訂閱 | 沒有 [[S1](#s1), [S2](#s2)] | 沒有 |

## 試用或購買之後

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 狀態 | 沒有試用；買了就一直能用 | 14 天後沒有解鎖，文件仍會開啟但內容被遮住；檔案不會有任何改變，快速查看和免費的 `marsdawn` 輸出都照常 |

## 來源

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## 該選哪一個

**選 MacMD Viewer，如果**你只讀 Markdown，而且希望「不會改到檔案」這件事是保證的：它不會儲存對檔案的任何更動 [[S1](#s1)]。這些情況它也比較合適：你的 Mac 跑的是 macOS 14 或 15（MarsDawn 需要 macOS 26）[[S1](#s1), [S7](#s7)]；你比較想從開發者自己的網站、Homebrew 或 Setapp 買，而不是 Mac App Store [[S2](#s2), [S7](#s7)]；你想讓 agent 改過的檔案自動在檢視器裡打開，它用 Claude Code、Cursor 和 Windsurf 的 hook 做到 [[S6](#s6)]；或者你想要單一連續頁面的 PDF，而不是分頁的 PDF [[S9](#s9)]。它沒有試用，但有 14 天退款 [[S2](#s2)]。

**選 MarsDawn，如果** Markdown 讀完還要再改一輪。agent 寫的計畫、README 或規格，通常要修一個地方、改一句話或加一段，在 MarsDawn 裡就在你正在讀的那個視窗裡改。它也支援數學式（KaTeX），MacMD Viewer 自己說不顯示 [[S7](#s7)]；介面有八種語言；有免費的 `marsdawn` 命令列工具，不需要 app 就能輸出 PDF；價格是 14 天全功能試用後 USD 4.99。

**兩個都可以，如果**你在較新的 Mac 上讀 Markdown，想把 Mermaid 圖表畫好，也想在 Finder 用快速查看。兩者都做得到。

**也可以兩個都用。**兩者不互斥：只讀的檔案用唯讀檢視器，要寫的檔案用編輯器，並不衝突。

## 常見問題

### MacMD Viewer 能編輯檔案嗎？

不能。它是唯讀的，照它自己的說法，不會儲存對原始檔的更動 [[S1](#s1), [S9](#s9)]。它可以把檔案交給你的文字編輯器開啟（「檔案」選單，⇧⌘E，1.7.0 起）[[S5](#s5)]。

### MacMD Viewer 在 Mac App Store 上嗎？

它自己的頁面列出的是官網、Homebrew 和 Setapp，沒有提到 Mac App Store [[S2](#s2), [S7](#s7)]。MarsDawn 只在 Mac App Store。

### MarsDawn 能打開同樣的檔案嗎？

可以。它打開 `.md` 檔案，也能打開純文字檔和 PDF：UTF-8 的文字檔可直接編輯，PDF 以檢視器開啟。

### 我的 Mac 是 macOS 14 或 15 呢？

MacMD Viewer 在 macOS 14 以上都能跑 [[S1](#s1)]。MarsDawn 需要 macOS 26 以上，不過免費的 `marsdawn` 命令列工具仍然可以輸出 PDF。

### 為什麼一個是 USD 19.99，一個是 USD 4.99？

兩者拿到的東西和付費方式不同。MacMD Viewer 是一次買斷，有 14 天退款，沒有試用 [[S2](#s2)]。MarsDawn 免費下載，有 14 天試用，之後一次解鎖。兩者都不是訂閱。

## 現在就能免費試試看

MarsDawn 已在 Mac App Store 上架。免費的 `marsdawn` 命令列工具也能把任何 Markdown 檔案轉成 PDF，Mermaid 圖表和程式碼上色都在，而且不需要安裝其他東西：

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 接下來

- 完整步驟：[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。
- MarsDawn 做不到的事：[這份清單](/zh-hant/limits/)。
- 命令列工具的所有選項：[命令列工具](/zh-hant/cli/)。
- 和在 VS Code、瀏覽器或 Claude Desktop 看 Markdown 比較：[比較一下](/zh-hant/vs/markdown-preview-tools/)。
- MarsDawn 的全部功能，一頁看完：[功能一覽](/zh-hant/features/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 檢查 agent 寫的 Markdown、JSON、YAML：Mac 原生 app，即時預覽、Mermaid、KaTeX、快速查看、PDF。免費試用，之後一次 USD 4.99。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown、JSON、YAML 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可拿去開會或存檔。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、iPhone 和 iPad 上不能編輯、沒有外掛、不需要帳號；可以換主題，但不能自訂 CSS。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Mac 怎麼開 md 檔](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hant/quicklook/index.md): MarsDawn 的快速查看讓你在 Finder 按空白鍵就看到排版後的 Markdown，Mermaid 圖表、KaTeX 數學式和程式碼上色都在。試用期結束後，快速查看照常可用。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MarsDawn 比較：VS Code 預覽、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [2026 Mac Markdown 檢視器推薦](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [主題](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 內建四種預覽主題，各有淺色與深色；在 Mac 版 MarsDawn 的設定裡打開主題庫，還能安裝更多。快速查看也會用你選的主題。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [和 agent 一起做主題](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽 MarsDawn 的預覽主題，每一個都經過開發者審核；可以依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造自己的主題，不用安裝，也不用 git。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [讀懂 agent 交回來的 Markdown](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [路線圖](https://marsdawn.southern-light.dev/zh-hant/roadmap/index.md): MarsDawn 在 Mac、iPhone 與 iPad 上正在做與接下來要做的功能，依版本列出。不寫日期，未排程的項目另外標明。
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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
