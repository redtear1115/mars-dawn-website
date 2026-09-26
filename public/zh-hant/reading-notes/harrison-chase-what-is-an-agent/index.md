# Harrison Chase 的 agentic 光譜：愈自主，愈需要盯著看

**2024 年 6 月，LangChain 的 Harrison Chase 用一個看似簡單的問題——「什麼是 agent？」——開啟了一個新系列，給出一個技術定義，還有一條「agentic」程度的光譜。他主張：系統在這條光譜上愈往自主那端走，就愈需要能在它運作時看得到裡面發生了什麼。**

## 這篇文章主張什麼

Chase 自己給的定義，還先承認這比大部分人的定義更技術性、涵蓋的範圍也更廣：

> “An agent is a system that uses an LLM to decide the control flow of an application.”

（Agent 是用 LLM 來決定應用程式控制流程的系統。「控制流程」指的就是程式接下來要跑哪一步。）

他馬上承認這個定義並不完美——一個只是讓 LLM 在兩條路徑之間做選擇的簡單系統，照他的定義算是 agent，但不太符合大部分人對「agent」的直覺想像。與其去爭誰才是「真正的」agent，他採用了 Andrew Ng 的說法——他引用 Ng 的一則推文，並註明出自 Ng：「rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic」（與其去爭該把哪些工作算進「真正的」agent、哪些不算，不如承認系統可以有不同程度的 agentic）。 Chase 自己的回應是：「I really agree with this viewpoint and I think Andrew expressed it nicely」（我很認同這個看法，覺得 Andrew 講得很好）。從這裡出發：系統愈由 LLM 決定該怎麼運作，就愈「agentic」，從固定的路由器，到狀態機，一路到能自己建立並記住工具的完全自主 agent。他從這條光譜出發，提出一個實際的主張：系統愈 agentic，某些基礎建設就愈重要，其中最重要的是可觀測性：

> “You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”

（你會希望能觀察系統內部發生了什麼，因為它實際採取的步驟事先可能無法得知。）

他還進一步主張不只要看，還要能介入：你也會希望能在某個時間點，修改一個正在運作的 agent 的狀態或指示，如果它偏離了原本設定的路徑，就把它拉回來。Chase 在這篇文章裡完全沒有提到 MarsDawn，也沒有推薦任何 Markdown 工具。

## 以下是我們的解讀，不是 Chase 的

Chase 談的是給打造 agent 框架的人用的工具——他點名了 LangGraph 和 LangSmith——不是給讀一份完成文件的人看的。但他這條光譜，給了一個很實用的方式，讓你在開始讀之前先估量一下手上這份東西：產出它的系統愈 agentic，你就愈不該預期它的步驟從最初的 prompt 就能猜得到，手上這份檔案也就愈值得當成「實際發生了什麼」的紀錄來讀，而不是「原本該發生什麼」的紀錄。他說的「觀察系統內部」，講的是一個正在運作的系統的內部狀態——trace（一次執行過程中，agent 做過的所有事的紀錄）、中間步驟、工具呼叫——不是事後讀一份 Markdown 計畫。但他給的理由——步驟事先無法得知——用在 agent 做完之後交給你的那份文件上，一樣說得通：如果一開始步驟就無法預測，那份做完之後的報告，就是唯一還能檢查它們的地方。

## MarsDawn 幫得上、幫不上的地方

MarsDawn 不會去觀察一個正在運作的 agent 的內部——它裡面沒有 AI 模型，也沒有連到產生這份檔案的任何框架，所以沒辦法告訴你某個 agent 在 Chase 的光譜上落在哪裡。它處理的是事後落到你手上的那份文件：側邊欄（「顯示方式 ▸ 顯示側邊欄」，⌃⌘S）的「大綱」分頁讓你看清楚一份長報告的架構；原始碼和排好的預覽並排（⌘2），處理圖表和數學式；agent 改寫檔案時會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改——這就是「盯著還在動的東西」的檔案版本。「編輯 ▸ 拷貝引用」（⌥⌘C）和「拷貝給 AI」（⌃⌥⌘C）讓你精準指出哪一步走偏了，等於是文件版的「把跑偏的 agent 拉回正軌」。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- 這個系列對透明和檢查點更完整的討論：〈[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)〉
- LangChain 2026 年在這篇文章原本的網址上發表的新文章，定義幾乎一模一樣：〈[Jess Ou 的評測流程，裡面還留給你的那一步](/zh-hant/reading-notes/langchain-what-is-an-agent/)〉
- 回到系列索引：〈[編者的閱讀筆記](/zh-hant/reading-notes/)〉

## 資料來源

- Harrison Chase，〈What is an agent?〉，LangChain，2024 年 6 月 28 日，存檔版本：[http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) （透過 Wayback Machine 於 2026-09-26 讀取並引用；原網址現在顯示的是 Jess Ou 在 2026 年寫的另一篇文章）

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。即將在 Mac App Store 上架。
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
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
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
- [閱讀筆記：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [閱讀筆記：Andrew Ng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
