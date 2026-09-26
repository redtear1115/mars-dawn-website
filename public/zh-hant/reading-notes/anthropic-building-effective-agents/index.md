# Anthropic 把 workflow 和 agent 分開來看，你的閱讀落在哪一邊？

**Anthropic 在 2024 年 12 月發表的〈Building Effective Agents〉，是寫給打造 AI agent 的人看的指南。一開頭就把「workflow」和「agent」分開，接著建議先從能用的最簡單做法開始——也可能完全不需要 agentic 系統——只有在這樣還不夠的時候，才用得上它整理出的五種 workflow 模式。其中一種模式，是讓另一次 LLM 呼叫坐上審查者的位置。這篇要談的就是這種模式，以及另外四種模式各自會留下什麼給你讀。**

## 指南主張什麼

Erik S. 與 Barry Zhang 寫這篇文章，是給正在決定怎麼用 LLM 打造系統的工程師看的。文章一開頭先下了一個定義：

> “Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.”

（Workflow 是 LLM 和工具透過事先寫好的程式路徑被安排執行的系統；相對地，agent 則是 LLM 自己動態決定流程、自己決定怎麼使用工具、掌控自己怎麼完成任務的系統。）

接著，他們的建議很克制：

> “When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.”

（用 LLM 打造應用程式時，我們建議先找出最簡單可行的做法，只有在真的需要時才增加複雜度。這可能代表根本不需要打造 agentic 系統。）

需要更多結構的時候，他們描述了五種 workflow 模式：prompt chaining（把任務拆成一連串呼叫，步驟之間可以加檢查）、routing（路由）、parallelization（平行化）、orchestrator-workers（一個 LLM 把任務拆給多個 worker LLM 執行，再把結果合起來），還有 evaluator-optimizer。最後這一種，原文是這樣寫的：

> “In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.”

（在 evaluator-optimizer workflow 裡，一次 LLM 呼叫產生答案，另一次呼叫則在迴圈裡負責評估、給回饋。）

Anthropic 在這份指南裡完全沒有提到 MarsDawn，也沒有推薦任何 Markdown 工具。這份指南談透明和「檢查點」的部分，〈[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)〉已經完整談過，這篇不再重複；那篇談人工審閱 code 的那句話，來自附錄裡專門講 coding agent 的段落，脈絡也在那篇文章裡。

## 以下是我們的解讀，不是 Anthropic 的

Anthropic 沒有說 workflow 跑完之後誰來檢查最終結果，這整篇也不是在談文件，而是給打造 agent 的人的架構決定。但這五種模式，會留下給你讀的東西並不一樣。Prompt chaining 和 routing 通常是看不見的管線；就算有東西送到你手上，也只是這條鏈最後一次呼叫的輸出，跟其他單次回答沒兩樣。Orchestrator-workers 就不同了：如果你的 coding agent 內部用的是這種模式，落進你資料夾的可能是一份由好幾個 worker 呼叫拼起來、再由 orchestrator 組合成的文件，其中一個 worker 那一段出了錯，很容易被整體讀起來很順的摘要蓋過去。

Evaluator-optimizer 特別值得停下來想一下，因為指南把原本可能由人來坐的審查者位置，換成了另一次 LLM 呼叫。這確實能便宜地抓到一類錯誤，但終究還是模型照著某組標準去檢查模型，這個系列裡也有作者提過這個顧慮：模型評判自己或另一個模型的成果。指南完全沒有說要有人再覆核 evaluator 的判斷，它根本沒表態。如果你才是最後要讀這一切的人，「迴圈通過了」和「我自己查過了」不是同一句話——就算你手上的檔案兩種情況看起來一模一樣。

## MarsDawn 幫得上、幫不上的地方

MarsDawn 不知道一份檔案是哪種 workflow 模式做出來的，裡面也沒有 AI 模型——它不會自己跑一次 evaluator 步驟，也沒辦法告訴你 Anthropic 描述的那個評估到底做得好不好。它做的是：側邊欄（「顯示方式 ▸ 顯示側邊欄」，⌃⌘S）的「大綱」分頁列出一份 orchestrator 拼出來的長檔案的所有標題，點一下就跳過去；原始碼和排好的頁面並排（⌘2），一起捲動，Mermaid 圖表和 KaTeX 數學式都直接畫出來。agent 讀到一半改寫檔案的話，MarsDawn 會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改。「編輯 ▸ 拷貝引用」（⌥⌘C）把你的位置拷貝成 `docs/plan.md:42`，直接貼回 agent 的對話裡就好。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- 這份指南談透明和檢查點的完整討論：〈[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)〉
- agent 的產出為什麼普遍難讀：〈[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)〉
- 回到系列索引：〈[編者的閱讀筆記](/zh-hant/reading-notes/)〉

## 資料來源

- Erik S. 與 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) （2026-09-26 讀取並引用）

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
- [閱讀筆記：Chip Huyen](https://marsdawn.southern-light.dev/zh-hant/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章裡，把 agent 的動作分成 read-only 和 write action 兩種。這個分法為什麼是核準計畫前，快速拓出該多看一眼的那一行的好方法。
- [閱讀筆記：Lilian Weng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被廣泛引用的整理，把 LLM agent 描述成大腦加上規劃、記憶、工具使用。每個部件通常會留給你讀什麼，以及她點名的一個限制：計畫遇到意外不太會調整。
- [閱讀筆記：Harrison Chase](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [閱讀筆記：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [閱讀筆記：Andrew Ng](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和 agent 分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/anthropic-building-effective-agents/index.md): 2024 年 12 月に Anthropic が発表したガイドは workflow と agent を分けて考え、5 つの workflow パターンを説明している。そのうち 1 つは、もう一回の LLM 呼び出しがレビューを担う。これは、あなたのフォルダに落ちてくるものにとって何を意味するか。
