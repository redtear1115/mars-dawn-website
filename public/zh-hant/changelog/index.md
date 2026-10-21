# 更新紀錄

黑色星期五特價：一次解鎖只要半價 USD 2.49（原價 USD 4.99），優惠到 11 月 30 日，12 月 1 日起恢復 USD 4.99。 <!-- sale-line -->

Mac App Store 上的 MarsDawn App，以及免費的 marsdawn 命令列工具，每個版本改了什麼。App 的日期是該版本在 Mac App Store 上架的日子。

## MarsDawn App

### MarsDawn 1.1.1

2026 年 10 月 15 日

- 在德文、日文、西班牙文與法文裡，「設定 ▸ 外觀 ▸ 取得更多主題⋯」的情境篩選改成標示為「情境」的彈出式選單，五個選項才放得下。英文、韓文與中文仍使用分段控制項。
- 主題從主題庫下架時，「取得更多主題⋯」裡的提示現在會顯示主題名稱（例如 Inkwell Ivory），不再顯示內部 id。
- 依 GitHub 寫法撰寫的可收合 details 區塊，在預覽與「快速查看」中會先收合並顯示摘要，點一下才展開。匯出 PDF 時仍會印出每一段內容。
- 從 Finder、Dock、「檔案 ▸ 打開⋯」或 marsdawn open 指令打開的文件，以及新增的文件，現在都會成為最前面視窗的分頁。想維持以前的方式，可以在「設定 ▸ 外觀」選擇「依照系統設定」。

### MarsDawn 1.1.0

2026 年 10 月 9 日

- 「設定 ▸ 外觀」新增「取得更多主題⋯」按鈕，可開啟主題庫，挑選更多預覽主題。安裝後，主題會出現在「顯示方式 ▸ 預覽主題」，也可以隨時移除。主題庫只在開啟時才會連線。
- 在 Finder 中用「快速查看」預覽時，現在會使用你選的主題，不再一律使用黎明主題。
- 「快速查看」也會跟著 MarsDawn 的外觀設定：選「淺色」或「深色」就固定使用該外觀，即使 Mac 設成另一種；選「系統」則跟著 Mac。
- 視窗標題中的 git 標記，現在遇到已暫存但尚未提交的檔案會顯示「+」，以前看起來像是沒有變更。
- 在預覽中點一下指向其他 Markdown 檔案的連結，例如 [notes](notes.md#plan)，現在會開啟該檔案；如果已經開著就帶到最前面，並捲動到對應的標題。檔案若不在側邊欄的資料夾內，MarsDawn 會先請你把該資料夾加入側邊欄，加入後再點一次連結。

### MarsDawn 1.0.2

2026 年 10 月 7 日

- 修正：第一次切換版面，或顯示、隱藏側邊欄時，編輯器不會再往上偏移一小段。
- 無法繪製的 Mermaid 圖表現在會顯示完整的錯誤訊息；知道行號時，點一下錯誤訊息就會跳到編輯器中該圖表所在的行。
- 繁體中文、簡體中文與西班牙文的選單用字，改為與 macOS 內建的翻譯一致，例如「儲存為⋯」和「移到⋯」。

### MarsDawn 1.0.0

2026 年 10 月 5 日

首次發表。

## marsdawn 命令列工具

0.5.1 以前的版本不列。

### marsdawn 0.7.2

2026 年 10 月 20 日。手冊版面、提示區塊，以及日文字型。

- 原本的 manual 版面改名為「手冊」：`marsdawn export --layout handbook`。`--layout manual` 仍可使用，但已不建議使用。
- 預覽和輸出的 PDF 都會呈現提示區塊：GitHub 的 alert（例如 `> [!NOTE]`、`> [!WARNING]`），以及 HackMD 的容器（例如 `:::info`、`:::warning`）。`:::spoiler` 會成為可收合的區塊。
- 日文文件的假名和漢字會改用日文字型。語言取自 front matter 的 `lang: ja`；沒有寫時，依內文的假名比例判斷。
- 在終端機裡成功執行 `export` 或 `open` 之後，如果 agent skill 沒有安裝或已經過期，marsdawn 會在 stderr 顯示一次提示。stdout 和 `--json` 的輸出都不變。設定 `MARSDAWN_NO_SKILL_HINT=1` 就不再提示。

### marsdawn 0.7.1

2026 年 10 月 20 日。手冊版面，以及檔案大小上限。

- `marsdawn export --layout manual` 輸出成使用手冊：邊界較寬、裝訂側留 25 mm，每個一級標題從新的一頁開始；另外有封面（取自 front matter 的 title、subtitle、version、date、author 和 logo）、列出一、二級標題並附頁碼的目錄、`n / N` 頁碼，以及 PDF 書籤。目錄頁的標題可以用 `--toc-title` 指定。預設仍是 `--layout document`。
- 單獨一行的 `<!--BREAK-->` 會從新的一頁開始，兩種版面都適用。
- `marsdawn export` 不處理超過 16 MiB 的檔案：以代碼 5 結束，加上 `--json` 時回報 `input_too_large`，不寫出任何檔案。
- 預覽頁會移除 script 和 noscript 元素；Mermaid 重畫時保留圖表自己的 SVG。
- 解碼後是 `=` 或 `^` 的字元參照（例如 `&#61;`）不再和 HackMD 標記配對。

### marsdawn 0.7.0

2026 年 10 月 18 日。HackMD 語法、換行，以及超大檔案的上限。

- 支援 HackMD 的行內標記：`==mark==`、`^sup^` 和 `~sub~`。單獨成段的 `[TOC]` 會變成目錄；HackMD 寫法的圖片尺寸會套用；嵌入標籤會變成一般的 https 連結；程式碼區塊的語言會先讀出來，再處理 `js=` 這類 HackMD 選項。
- `marsdawn export --breaks` 會把段落內的每個換行都當成換行，和 HackMD 一樣。不加時，兩個中文或日文字之間的換行會拿掉，讓前後兩行連成一句；韓文的詞與詞之間本來就空格，所以保留空格。
- 超大檔案在預覽和輸出的 PDF 裡都有上限：單一程式碼區塊超過 128K 字元就不上色，整份累計超過 256K 字元後也不再上色。每次更新最多畫 100 張 Mermaid 圖表、算 1,000 個數學式；其餘圖表顯示原始碼並附上說明，即使之前畫過也一樣。
- 循序圖中，`rect` 區塊裡的訊息標籤，外框底色改用該區塊的顏色。
- 表格正上方有註腳參照時，`marsdawn export` 不再當掉。
- `marsdawn skill --install` 無法建立資料夾或寫入檔案時，以代碼 7（`skill_install_failed`）結束，原本的 SKILL.md 保持不變。

### marsdawn 0.6.4

2026 年 10 月 13 日。可收合的 `<details>` 區塊。

- GitHub 風格的 `<details>` 區塊裡有空行時，也會呈現為一個可收合的區塊；預覽和輸出的 PDF 都一樣。以前遇到第一個空行就會斷開。
- 輸出 PDF 時，會先把每個 `<details>` 區塊展開再列印（front matter 除外）。
- 展開或收合 `<details>` 區塊時，預覽會保持原本的捲動位置。

### marsdawn 0.6.3

2026 年 10 月 6 日。MarsDawn 在 Mac App Store 上架。

- 沒有安裝 app 時，`marsdawn open` 會指向 Mac App Store 上的 MarsDawn。
- README 和 agent skill 會教 `marsdawn open .` 與 `--folder`：MarsDawn 1.0.0 會把資料夾顯示在視窗的側邊欄。

### marsdawn 0.6.1

2026 年 9 月 29 日。檢查主題。

- `marsdawn theme validate` 會用 app 採用的規則檢查 `theme.json`。主題有效時以代碼 0 結束，無效時以代碼 1 結束，並列出每個問題。加上 `--require-complete` 時，也會要求語法上色和圖表的顏色。
- `marsdawn theme css` 會印出預覽替有效主題使用的 CSS；`marsdawn theme preview` 會用這個主題把一份範例文件畫成 PNG，淺色或深色都可以。

### marsdawn 0.5.4

2026 年 9 月 26 日。Mermaid 修正、圖表錯誤的行號，以及安裝 skill。

- 循序圖中，訊息標籤跨過其他參與者的生命線時，文字仍清楚可讀；預覽和輸出的 PDF 都一樣。
- `marsdawn export` 能處理含有大量 Mermaid 圖表的文件。一份有 50 張圖表、原本會以代碼 5 結束的文件，現在可以順利輸出。
- `marsdawn export --json` 新增 `diagramErrorDetails`，用行號標出每個圖表錯誤：圖表在文件中從第幾行開始；Mermaid 指出行號時，也列出錯誤本身所在的行。
- `marsdawn skill --install` 會把 agent skill 安裝到 `~/.claude/skills/marsdawn/SKILL.md`，供 Claude Code 使用；加上 `--dir` 可以改裝到其他資料夾。已有相同的檔案時不會動它；內容不同時，只有加上 `--force` 才會取代，否則以代碼 64（`skill_differs`）結束，不做任何更動。

### marsdawn 0.5.3

2026 年 9 月 25 日。資料夾狀態、完整的 Mermaid 錯誤訊息，以及其他小修正。

- `marsdawn open --folder` 可以回報資料夾後來怎麼了。搭配會回報狀態的 app，它最多等待 `--wait` 秒（預設 2 秒），`--json` 會給出 `attached`、`needsUser` 等狀態。
- Mermaid 圖表無法解析時，會顯示 Mermaid 完整的錯誤訊息，不再只有第一行；行號也改成從文件開頭算起。
- 尋找 front matter 區塊的結尾時，最多只找 1,000 行；沒有結尾的區塊，不再讓大型文件每次都被掃描到最後。
- app 可以為 PDF 輸出與列印，替註腳的返回連結提供翻譯後的標籤。這個標籤不會印在頁面上，`marsdawn export` 仍使用英文。
- 內建的 highlight.js 現在和 KaTeX、Mermaid 一樣，記錄版本、來源與 SHA-256。

### marsdawn 0.5.2

2026 年 9 月 24 日。註腳、對比度與資料夾。

- 輸出的 PDF 會呈現註腳：引用有編號，註腳內容接在正文之後。
- 所有主題的淺色與深色都符合 WCAG AA 對比度。Classic 改為黑白。
- `marsdawn skill` 會印出和已安裝的 marsdawn 相符的 agent skill。
- 找到的 MarsDawn 無法顯示資料夾時，`marsdawn open` 會以代碼 6（`app_cannot_open_folders`）結束，不再回報成功。
- 畫進輸出頁面的佔位文字，也有德文、法文、西班牙文和韓文。
- 相對路徑很長時，圖片佔位文字不再顯示它背後的絕對路徑。
- `MARSDAWN_APP_PATH` 只有指向 MarsDawn app 時才會採用。

### marsdawn 0.5.1

2026 年 9 月 19 日。PDF 輸出，以及從命令列打開檔案。

- 輸出的 PDF 中，中文、日文與韓文的文字層已修正。
- `marsdawn open --background` 會打開檔案，但不會把 MarsDawn 帶到最前面。
- `marsdawn open` 可以指定一個資料夾，MarsDawn 會把它顯示在視窗的側邊欄（MarsDawn 1.0.0 起）。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 讀懂、檢查 agent 寫的 Markdown 的 Mac 原生 app：分割即時預覽、Mermaid、KaTeX、快速查看、PDF 輸出。可免費試用，之後一次 USD 2.49。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 2.49 解鎖一次就好。沒有訂閱，也不需要帳號。
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
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 2.49 解鎖一次。逐項比較，附來源。
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
