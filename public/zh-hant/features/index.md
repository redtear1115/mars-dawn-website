# MarsDawn 能做的事，一頁看完。

MarsDawn 是為 Mac 做的 Markdown 編輯器。一邊寫，一邊讀排版後的頁面，圖表、數學式和程式碼都畫在裡面。它沒有自己的 AI 模型：做它是為了讀 agent 寫的東西，也讓你寫自己的。工作換到會議桌或檔案櫃上時，它也能印出、輸出乾淨的頁面。

下面每一節說明 app 做了什麼，並連到講得更細的頁面。

![MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

這張截圖裡：

1. 原生的 Mac 視窗。
2. Mac 原生的文字編輯器，附 Markdown 語法上色。
3. ⌘1 原始碼、⌘2 並排、⌘3 預覽。
4. 頁面會隨著打字更新。

## 讀 agent 寫的 Markdown

### 原始碼和預覽並排

打開 Markdown 檔，排版後的頁面就在原始碼旁邊（⌘2）；也可以只看原始碼（⌘1）或只看預覽（⌘3）。兩邊一起捲動，頁面會隨著打字更新。

[為 Mac 而做](/zh-hant/native/)

### 大綱和檔案側邊欄

側邊欄的「大綱」列出文件的標題，點一下就跳到該處。打開資料夾後，「檔案」分頁列出裡面的檔案；agent 正在寫入時，新檔案會自動出現。如果資料夾是 git 檢出，上方標題會寫出是哪個分支或工作樹。

[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)

### 指出確切的那一行

「編輯 ▸ 拷貝引用」會把你的位置拷貝成路徑加行號，例如 `docs/plan.md:42`。「拷貝給 AI」再附上所選的文字。貼到 agent 的對話裡就行。

[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)

### 跟著連結跳到另一個檔案

在預覽裡點一個指向另一個 Markdown 檔的連結，MarsDawn 會打開那個檔案（已經開著就帶到前面），並捲到那個標題。

## 紙本在人與人之間的用處

不是所有的工作都在螢幕上做。MarsDawn 印出和輸出的頁面，就是你在螢幕上讀的那幾頁，所以人們聚在一起、讀東西、留紀錄的地方都用得上。

### 開會討論

把頁面印出來，或把同一份 PDF 傳給每個人，大家就是看同一份文件，不用擠在一個螢幕前。拿到同一個檔案的人，分頁位置都一樣，所以「第 3 頁那張表」指的是同一個東西。接著由人把決議寫下來，寫在印出來的紙上，或寫成筆記。會議記錄範本把決議放在最前面，每個行動項目都有負責人。

[輸出 PDF](/zh-hant/pdf/) · [會議記錄範本](/zh-hant/templates/meeting-notes/)

### 拿筆邊讀邊寫

有些人習慣用筆讀東西：畫線、在頁邊寫幾個字，才記得住。把文件印出來，就可以在紙上這樣做。MarsDawn 本身沒有加註功能；想直接在 PDF 上標記的話，用你原本就有的 PDF app 就好。

[輸出 PDF](/zh-hant/pdf/)

### 紙本保存

有些行業還是要把紙本存起來，會計就是一個例子。MarsDawn 沒有任何歸檔或合規的聲明。它做的是印出和輸出乾淨、分好頁的頁面：圖表畫進去，短的程式碼區塊不被切開，用主題的淺色配色。紙本還是正式紀錄的地方，就可以用這些頁面。

[輸出 PDF](/zh-hant/pdf/)

### 交給不寫 Markdown 的人

PDF 在任何地方都能打開，也不需要懂 Markdown，所以也適合寄給主管或客戶。

[分享輸出的 PDF](/zh-hant/sharing-exported-pdfs/)

## 寫作和版面

### 純 Markdown，附語法上色

粗體、斜體、刪除線、行內程式碼、連結、引言和待辦清單都照常使用。編輯器會幫 Markdown 語法上色，顏色和預覽主題一致。

[為 Mac 而做](/zh-hant/native/)

### 縮放、行號和狀態列

原始碼和預覽可以一起縮放，範圍 50% 到 300%。原始碼旁有行號欄；狀態列顯示游標所在的行與欄，以及整份文件或所選文字的字數、字元數和閱讀時間。

### 圖片

先儲存文件，再把圖片拖進或貼到編輯器。MarsDawn 會把圖片複製到文件旁的 assets 資料夾，並寫好連結。網路圖片在你按下「載入圖片」之前都不會載入，所以打開文件不會讓任何伺服器知道你讀了它。

[你寫的內容留在你的 Mac 上](/zh-hant/yours/)

### Front matter 不礙事

檔案開頭的 front matter 區塊，在預覽和快速查看裡會收成可展開的「文件資訊」，輸出 PDF 時則不會印出。

### 八種語言

App 介面有英文、繁體中文、簡體中文、日文、德文、法文、西班牙文和韓文。

[為 Mac 而做](/zh-hant/native/)

## 圖表、程式碼和數學式

### Mermaid 圖表

標記為 `mermaid` 的程式碼區塊會畫成圖表。圖表寫錯時，預覽會顯示它的原始碼，下方附上錯誤訊息；點一下訊息，就跳到編輯器裡那一行。

[在 Mac 上預覽 Mermaid](/zh-hant/mermaid-preview-mac/)

### 程式碼上色

常見的程式語言都會語法上色，在開頭的 ````` 後面寫上語言名稱就好。

### 數學式

用 KaTeX 語法寫的數學式，會在預覽和快速查看裡畫出來，輸出的 PDF 裡也有。

[為什麼 AI 寫的東西還是需要人讀過](/zh-hant/reviewing-ai-output/)

## 主題、PDF 和列印

### 四種主題，各有淺色和深色

黎明、典雅、流行、活潑各有淺色和深色版本。MarsDawn 會跟著 Mac 的外觀切換，也可以在設定中固定一種。從「顯示方式 ▸ 預覽主題」或工具列的調色盤按鈕選擇。

[預覽主題與 PDF 輸出](/zh-hant/themes/)

### 更多主題

「設定 ▸ 外觀 ▸ 取得更多主題⋯」會打開額外預覽主題的主題庫。裝上一個，它就出現在「顯示方式 ▸ 預覽主題」裡；按「移除」就拿掉。主題庫只在打開的時候連上網路。

[主題庫](/zh-hant/themes/gallery/) · [打造一個主題](/zh-hant/themes/new/)

### 輸出 PDF，或列印

「檔案 ▸ 輸出為 PDF⋯」會存成自動分頁的 PDF，「檔案 ▸ 列印⋯」印出相同的頁面。Mermaid 圖表直接畫進去，程式碼保留語法上色，分頁時會盡量不讓標題落在頁尾，也不切開短的程式碼和圖表。PDF 一律用主題的淺色配色，就算你是在深色下讀的也一樣。

[輸出 PDF](/zh-hant/pdf/)

![用 MarsDawn 輸出的 PDF，在內建的 PDF 檢視器中開啟，旁邊有頁面縮圖。](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

這張截圖裡：

1. Mermaid 圖表直接畫進 PDF。
2. 程式碼保留語法上色。

## 檔案、分頁和快速查看

### 視窗和分頁

每份文件預設在自己的視窗打開。用「視窗 ▸ 合併所有視窗」，可以把開著的視窗收成同一個視窗裡的分頁。打字時會自動儲存。

[為 Mac 而做](/zh-hant/native/)

### 在 Finder 用快速查看

在 Finder 選取 Markdown 檔並按空白鍵，就能看到排版後的樣子，圖表也會顯示。快速查看會用你在 MarsDawn 選的主題，也跟著 MarsDawn 的外觀設定。

[為 Mac 而做](/zh-hant/native/) · [Markdown 快速查看](/zh-hant/quicklook/)

### 其他檔案

MarsDawn 也能打開純文字檔（`.txt`、`.log`、程式碼檔）和 PDF。UTF-8 純文字檔打開就能直接編輯，只顯示原始碼。PDF 則在有頁面縮圖、縮放和搜尋的檢視器中開啟。

### 你的檔案留在你手上

不需要帳號，沒有同步，也沒有雲端。文件留在你儲存的位置，MarsDawn 不收集任何關於你的資料。

[你寫的內容留在你的 Mac 上](/zh-hant/yours/)

## 給 agent 和腳本

### 免費的命令列工具

免費的 `marsdawn` 工具另外用 Homebrew 安裝。`marsdawn export` 把 Markdown 檔輸出成 PDF，排版和 MarsDawn 的預覽一樣，不需要 app；可以用 `--theme` 選主題，紙張選 A4 或 Letter。`marsdawn open` 在 app 裡打開檔案讓你審閱，還可以指定行號，這個需要先裝 app。

[命令列工具](/zh-hant/cli/)

### 腳本讀得懂的輸出

加上 `--json`，兩個指令都會回傳 agent 或腳本能解析的結果。

[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)

### Skill 和 MCP 伺服器

一個 agent skill 檔案，教寫程式的 agent 把自己寫的東西在 MarsDawn 裡打開給你審閱。沒有 shell 的用戶端，則可以用另外的 MCP 伺服器執行同一個 export。

[給 agent 的 skill](/zh-hant/cli/skill/) · [MCP 伺服器](/zh-hant/cli/mcp/)

### 裡面沒有 AI

MarsDawn 沒有自己的 AI 模型。它不會幫你摘要或評分 agent 寫的東西，只是讓一份又長又一直在改的檔案保持好讀，讀的人是你。

[MarsDawn 做不到的事](/zh-hant/limits/)

## Siri 和捷徑

在「捷徑」App 搜尋 MarsDawn，可以找到三個動作：「新增 Markdown 文件」（可選範本）、「新增筆記到收件匣」和「打開最近的文件」。筆記會加到你在「MarsDawn ▸ 設定⋯ ▸ 筆記資料夾」選的資料夾中的 `Inbox.md`。

[為 Mac 而做](/zh-hant/native/)

## 頁面印出來之後

大家圍著印出來的頁面開會，有人拿筆在頁邊寫字，紙本紀錄收進檔案。

[MarsDawn 影片，88 秒](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## 在你的 Mac 上試試

MarsDawn 可以免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。需要 macOS 26 以上。

[立刻下載試用](https://apps.apple.com/app/id6812925073)

試用怎麼運作：[免費試用，買一次就好](/zh-hant/pay-once/)。刻意不做的事：[MarsDawn 做不到的事](/zh-hant/limits/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 讀懂、檢查 agent 寫的 Markdown 的 Mac 原生 app：分割即時預覽、Mermaid、KaTeX、快速查看、PDF 輸出。可免費試用，之後一次 USD 4.99。
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
