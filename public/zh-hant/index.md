給建造者的前線工具

# 拿穩地圖。讀過黎明。

給要掌舵 agentic 開發的人用的 Markdown。

MarsDawn 是讀、檢查 Markdown 的 Mac 原生 app，有分割即時預覽、Mermaid 圖表、KaTeX 數學式、快速查看與 PDF 輸出；可免費試用 14 天，一次付 USD 4.99 解鎖。

頁面上有一個可以操作的 MarsDawn 視窗，內容是 App 內建歡迎指南的一段。調色盤選單可以選外觀（系統、淺色、深色），並分別替淺色和深色從四個預覽主題（黎明、典雅、流行、活潑）裡選一個；工具列可以選三種版面（原始碼、並排、預覽）。

## 讀 agent 寫的 Markdown。

1. **Agent 動筆。**你的程式碼助手或寫作 agent 先寫出 Markdown：README、規格文件，或一份筆記。
2. **你在 MarsDawn 裡讀。**打開檔案，看排版後的頁面，[Mermaid 圖表](/zh-hant/mermaid-preview-mac/)和程式碼上色都在，旁邊就是原始碼。
3. **Agent 修改。**提出修改意見，agent 改好之後，再打開來讀一次。

[如何審閱 agent 交回來的東西](/zh-hant/reading-agent-output/) · [Mac 怎麼開 md 檔](/zh-hant/view-markdown-on-mac/)

## agent 的計畫，執行前先看過。

找出順序不對的那一步，指出是哪一行，再交回給 agent。

1. 看改了什麼：agent 一存檔，開著的視窗就從磁碟更新，一步完成，也能撤銷。
2. 跳到那一行：marsdawn open plan-checkout-v2.md:10 讓視窗停在第 10 行，預覽裡對應的區塊會閃一下。
3. 回給 agent：「拷貝引用」（⌥⌘C）拷貝 plan-checkout-v2.md:10，連同你的意見貼進 agent 的對話。

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

- [為 Mac 而做](/zh-hant/native/)：原生視窗、分頁、自動儲存、[快速查看](/zh-hant/quicklook/)。
- [你寫的內容留在你的 Mac 上](/zh-hant/yours/)：不需要帳號，沒有同步，也沒有雲端。
- [免費試用，買一次就好](/zh-hant/pay-once/)：免費試用 14 天，之後 USD 4.99 買一次，沒有訂閱。
- [功能一覽](/zh-hant/features/)：MarsDawn 能做的事，一頁看完。

購買前先知道。 [MarsDawn 做不到的事](/zh-hant/limits/)

## 各部分怎麼搭在一起

以 MarsDawn 1.1.1、marsdawn 0.6.4、marsdawn-mcp v0.2.4 為準，各部分目前能做的事。

| 功能 | App 內 | CLI | MCP／skill | 狀態 |
|---|---|---|---|---|
| 打開到某一行 | 停在那一行，預覽區塊閃一下 | marsdawn open notes.md:120（--background 不搶焦點） | open_in_marsdawn；skill 只開一次 | 已推出 |
| 輸出 PDF | 檔案 ▸ 輸出為 PDF⋯（⌥⌘E） | marsdawn export，不需要 app | export_markdown_to_pdf；skill | 已推出 |
| JSON 結果 | — | open、export 加 --json | MCP 回傳同一份 JSON | 已推出 |
| Agent skill | — | marsdawn skill --install | 教 agent 開一次、輸出 PDF | 已推出 |
| MCP 伺服器 | — | 在底下執行 | marsdawn-mcp：兩個工具，只碰允許的資料夾 | 已推出 |
| 拷貝給 AI、拷貝引用 | 編輯 ▸ 拷貝給 AI（⌃⌥⌘C）、拷貝引用（⌥⌘C） | — | —（貼給任何 agent） | 已推出 |
| 存檔後自動更新 | 接收存檔的變更，可撤銷一次 | — | skill：不用再開一次 | 已推出 |
| Claude Code hook | — | 用 open --background | /cli/agents/ 的 hook 腳本 | 有文件，選用 |

已推出：在上面寫的發行版本裡。有文件，選用：本站上的說明，要你自己加，不在工具裡。規劃中：還沒做，沒有日期。規劃中：MCP 的 open_in_marsdawn 加上資料夾選項。--folder 等其他選項見[命令列工具](/zh-hant/cli/)。

## 用 coding agent 做 Mac app 的你

寫給獨立 Mac 開發者：你的 agent 現在怎麼把它寫的檔案打開在 MarsDawn 裡。

| 工具 | 怎麼搭配 | 設定 |
|---|---|---|
| Claude Code | skill 會讓它寫完後打開一次，直接停在那一行：`marsdawn open plan.md:42`。另有選用的 hook，它寫的每個 .md 都會在背景打開 | `marsdawn skill --install`；hook 腳本見 /cli/agents/ |
| Codex、Cursor、Xcode | 還沒有專屬的設定說明。能跑 shell 指令的工具都能呼叫 `marsdawn open file:line --json`；會讀指令檔的 agent 可以用 SKILL.md（`--dir`），只走 MCP 的工具可以用 marsdawn-mcp | `brew install redtear1115/tap/marsdawn` |

hook 與指令：[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/) · [給 agent 的 skill](/zh-hant/cli/skill/) · [MarsDawn 做不到的事](/zh-hant/limits/)

在 MarsDawn、VS Code 預覽、Obsidian、QLMarkdown、LynxOffice 之間猶豫？比較頁列出各家自己的說法、MarsDawn 沒有的東西，以及什麼時候用不到它。[看比較](/zh-hant/vs/)

## 文件留在你的 Mac 上

在你的 Mac 上。閱讀、編輯、算繪、[輸出 PDF](/zh-hant/privacy/#exporting-and-printing) 和 [marsdawn 命令列](/zh-hant/privacy/#the-marsdawn-command-line-tool)都在本機完成，可以完全離線；App 不會上傳你的文件。

詳見：[隱私權政策](/zh-hant/privacy/#what-stays-on-your-mac)

預設不連網。網路圖片只有在你按「載入圖片」，或在設定中開啟「自動載入網路圖片」後才會載入；HTML 文件開啟時是靜態的，程式碼不會執行。

詳見：[隱私權政策](/zh-hant/privacy/#when-marsdawn-uses-the-internet)

只在你選擇時離開。「拷貝給 AI」只把文字放進剪貼板，由你自己貼上；下載主題、用「顯示方式 › 執行這份文件」執行的文件，以及你讓 agent 讀的檔案，都要你決定才會往外送。

詳見：[隱私權政策](/zh-hant/privacy/#when-marsdawn-uses-the-internet)

## 常見問題

### MarsDawn 是什麼？

MarsDawn 是 Mac 原生 app，用來讀懂、檢查 agent 寫的 Markdown：原始碼和即時預覽並排，能畫 Mermaid、排 KaTeX，在快速查看裡預覽 .md，也能輸出 PDF。原始碼也可以直接改。

### MarsDawn 要訂閱嗎？

不用。MarsDawn 免費下載，14 天內所有功能都能試用；之後一次 USD 4.99 的 App 內購買就能永久解鎖。沒有任何續訂，也不需要帳號。

### MarsDawn 有 iPhone 或 iPad 版嗎？

還沒有。MarsDawn 是 Mac app，需要 macOS 26 或更新版本。iPhone 與 iPad 版正在開發中，目前還不能使用。

詳見：[路線圖](/zh-hant/roadmap/)

### Claude Code 可以用 MarsDawn 開檔案嗎？

可以。免費的 marsdawn 命令列工具有 open 指令，能用 MarsDawn 開啟 Markdown 檔案，所以 Claude Code，或任何能執行 shell 指令的 agent，都能呼叫它。另有一個需要自行啟用的 Claude Code hook，可以在 Claude 寫入或編輯 Markdown 檔案時自動開啟。

### MarsDawn 會上傳我的文件嗎？

不會。App 不會上傳你的文件，不收集任何關於你的資料，也沒有帳號；文件和設定都留在你的 Mac 上。只有文件引用網路內容、而你選擇載入時，你的 Mac 才會向放置那些內容的伺服器取用，MarsDawn 的開發者收不到這些資訊。

詳見：[隱私權政策](/zh-hant/privacy/#what-stays-on-your-mac)

### 用 MCP 或 skill 時，誰能看到我的檔案？

MarsDawn 本身不傳送任何東西。skill 只是一份文字說明，marsdawn 命令列和 MCP 伺服器都在你的 Mac 上執行，MCP 伺服器也只在你允許的資料夾裡動作。真正讀檔的是你的 agent，它和它的模型供應商怎麼處理這些檔案，依照那個 agent 的政策；MarsDawn 無法控制，也不代為說明。

詳見：[MCP](/zh-hant/cli/mcp/)

### 打開別人傳給我的 HTML 安全嗎？

預設開啟時是靜態的：程式碼不會執行，也不會從網路載入任何東西。若你選擇「顯示方式 › 執行這份文件」，這份文件就會執行，可以透過網路傳送資料，並讀取它所在資料夾裡的圖片、樣式表、字型與媒體檔案。這個選擇不會被記住，下次打開又是靜態的。

詳見：[隱私權政策](/zh-hant/privacy/#when-marsdawn-uses-the-internet)

### 網站的分析 cookie 和 App 有關嗎？

沒有關係。App 和這個網站是兩件事：App 不收集資料，會記下造訪的只有 marsdawn.southern-light.dev。網站的 Google Analytics 一開始是拒絕狀態，你在橫幅中選擇「接受」之後才會設定 cookie，頁尾的「Cookie 設定」可以隨時改。App 下載 /themes/ 底下主題檔的請求不會被記錄。

詳見：[隱私權政策](/zh-hant/privacy/#the-website)

### 為什麼用 MarsDawn，不用別的 App？

你可能不需要它。如果你主要寫自己的筆記，Obsidian 這類筆記 App 更適合。如果你整天待在 VS Code，它內建的預覽是免費的。如果你只想在 Finder 裡瞄一眼檔案，免費的快速查看擴充功能就夠了。如果你的 PDF 需要頁碼，MarsDawn 不會加。MarsDawn 是用來閱讀和審閱 agent 寫的 Markdown：原始碼旁邊就是即時預覽，agent 的修改一步就能撤銷，檔案直接開到指定的那一行。如果它不合用，歡迎寫信告訴我們原因。

詳見：[MarsDawn 與其他工具比較](/zh-hant/vs/) · [Mac Markdown 檢視器推薦](/zh-hant/best-markdown-viewer-mac/)

### MarsDawn 會持續維護嗎？

會。MarsDawn 上架 Mac App Store 以來的每次更新都在更新紀錄裡，iPhone 與 iPad 版也在開發中。MarsDawn 的算繪核心和免費的 marsdawn 命令列工具，已經以 Apache-2.0 授權在 mars-dawn-kit 開源。如果 MarsDawn 的開發者哪天停止維護這個 App，會以開源授權公開 App 本身的原始碼，讓其他人可以接手。

詳見：[更新紀錄](/zh-hant/changelog/) · [路線圖](/zh-hant/roadmap/) · [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)

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

- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號。內建四種主題，主題庫還有更多。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Mac 怎麼開 md 檔](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hant/quicklook/index.md): MarsDawn 的快速查看讓你在 Finder 按空白鍵就看到排版後的 Markdown，Mermaid 圖表、KaTeX 數學式和程式碼上色都在。試用期結束後，快速查看照常可用。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MarsDawn 比較：VS Code 預覽、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [2026 Mac Markdown 檢視器推薦](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。在瀏覽器裡打造自己的主題，也可以逛逛社群主題庫。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [和 agent 一起做主題](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽社群投稿的 MarsDawn 預覽主題，依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造一個自己的主題，不用安裝，也不用 git。
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
- [English](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown を読んで確かめる Mac ネイティブアプリ。分割ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、解除は一度だけ USD 4.99。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
