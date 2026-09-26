# Jess Ou 的評測流程，裡面還留給你的那一步

**2026 年 7 月，LangChain 在 Harrison Chase 2024 年那篇〈What is an agent?〉原本的網址上，發表了一篇新的〈What is an AI agent?〉——這次是 Jess Ou 寫的，定義幾乎和他當年那句一字不差。她這篇大部分在談他那篇沒談到的東西：一整套自動評測 agent 的流程。她的文章很坦白地講清楚，這套流程哪裡還需要人，哪裡已經不需要了。**

## 這篇文章主張什麼

Ou 的定義幾乎就是 Chase 那句話的迴聲：

> “An AI agent is a system that uses a large language model to decide the control flow of an application.”

（AI agent 是用大型語言模型來決定應用程式控制流程的系統。「控制流程」一樣是指接下來要跑哪一步。）

接下來她描述了 LangChain 的 Agent Development Lifecycle：build、test、deploy、monitor 四個階段，以及一套不靠人讀每一次執行紀錄就能檢查 agent 表現的分層做法：online evals 對正式流量的 trace（一次執行的紀錄）取樣，抓退步；offline evals 跑在整理好的資料集上，在變更上線前先抓出問題；「LLM-as-a-judge」則是用一個人事先定好的標準，去替一次執行的輸出打分數，而且規模是人工審閱做不到的。她也直接講清楚人在這套流程裡還該站在哪裡：

> “For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.”

（對於敏感或不可逆的動作，我們建議用 human-in-the-loop 的控制機制，暫停 agent，等待核准、修改、拒絕或澄清。）

她也有一句話講的是不管流程多完善都省不掉的判斷：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（無法評估的判斷，就不要外包出去。如果你自己認不出正確答案，agent 也認不出來。）〈[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)〉已經拿這句話建過討論，這篇不重複。Ou 在這篇文章裡完全沒有提到 MarsDawn，也沒有推薦任何 Markdown 工具。她也從來沒提過 Chase 這個人；把這兩篇文章連在一起的，是 LangChain 在 2026 年把她這篇發表在 Chase 2024 年那篇文章原本的網址上，而且定義幾乎一模一樣——這是我們自己的觀察，不是她的主張。

## 以下是我們的解讀，不是 Ou 的

Ou 講的 human-in-the-loop，是在特定動作執行前先攔下來——暫停一個 write 動作、等人核准，跟 Chip Huyen 那個 read-only／write action 的分法，其實是同一件事的不同角度——不是讀一份已經完成的報告。仔細看她整套流程，大部分設計是要把人從例行檢查裡拿掉，而不是加進去：online evals、offline evals 和 LLM-as-a-judge，存在的目的就是讓團隊不用手動看每一次的執行紀錄。這不是在批評這篇文章——這本來就是她講明的目標，在正式營運的規模下也很合理。但這代表你親自動手做的審閱——直接讀一份 agent 交給你的計畫或報告——正好就是她這套流程想要減少、而不是取代的那種檢查。她自己那句判斷的話，替這種減少畫了一條底線：你自己讀了都認不出對錯的地方，還是得自己讀過。

## MarsDawn 幫得上、幫不上的地方

MarsDawn 不是評測流程，裡面也沒有 AI 模型——它不會替一次執行紀錄打分數，不會跑 LLM-as-a-judge，也不會替你決定哪些動作敏感到要先暫停。它做的，正是她這套流程還留給人的那個時刻：直接把東西讀過一遍。側邊欄（「顯示方式 ▸ 顯示側邊欄」，⌃⌘S）的「大綱」分頁列出一份長報告的所有標題；原始碼和排好的預覽並排（⌘2），Mermaid 和 KaTeX 都直接畫出來；「編輯 ▸ 拷貝引用」（⌥⌘C）搭配「拷貝給 AI」（⌃⌥⌘C），讓你把一次抽查變成 agent 看得懂、改得動的回饋。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- 部分建立在她這句「別外包判斷」上的完整檢查清單：〈[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)〉
- 這個定義最早在 2024 年是怎麼寫的：〈[Harrison Chase 的 agentic 光譜：愈自主，愈需要盯著看](/zh-hant/reading-notes/harrison-chase-what-is-an-agent/)〉
- 回到系列索引：〈[編者的閱讀筆記](/zh-hant/reading-notes/)〉

## 資料來源

- Jess Ou，〈What is an AI agent?〉，LangChain，2026 年 7 月 31 日：[https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent) （2026-09-26 讀取並引用）

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
- [閱讀筆記：Harrison Chase](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [閱讀筆記：Andrew Ng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
