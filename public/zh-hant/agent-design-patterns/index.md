# 四種 agent 設計模式，各自會交給你什麼文件

2024 年 3 月，Andrew Ng 在他的電子報 The Batch 介紹了四種 AI agent 的設計模式：reflection（反思）、tool use（使用工具）、planning（規劃）和 multi-agent collaboration（多 agent 協作）。大家通常從開發者的角度談它們，當成讓模型表現更好的方法。這篇換個方向看：如果你用的 agent 是照這些模式做的，最後會有什麼東西落進你的資料夾？你該先讀哪裡？

**四種模式是 Andrew Ng 提出的。每種模式通常會交給你什麼文件、該檢查什麼，是我們自己的推論。這兩件事他都沒有寫，他在這個系列裡也沒有主張要人工審閱。**

## 四種模式，簡單說

Ng 在〈Agentic Design Patterns Part 1〉裡介紹了這四種模式。簡單說：**reflection** 是模型回頭檢查自己的成果，再加以改進；**tool use** 是讓模型能呼叫網路搜尋、執行程式碼之類的工具；**planning** 是模型自己擬出多步驟的計畫再執行；**multi-agent collaboration** 是好幾個 agent 分工、互相討論。

他在 Part 1 用一個程式碼基準測試 HumanEval 說明這些模式的效果，數據是他的團隊整理多個研究團隊的結果：「GPT-3.5 (zero shot) was 48.1% correct. GPT-4 (zero shot) does better at 67.0%. However, the improvement from GPT-3.5 to GPT-4 is dwarfed by incorporating an iterative agent workflow. Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%.」（GPT-3.5 在 zero-shot 下的正確率是 48.1%，GPT-4 在 zero-shot 下好一些，是 67.0%。但和加入迭代式 agent 工作流程相比，從 GPT-3.5 換到 GPT-4 的進步就顯得微不足道：放進 agent 迴圈後，GPT-3.5 最高可達 95.1%。）這些數字只針對一個程式碼基準測試，95.1% 是最好的情況（"up to"，最高可達）。它們說明 agent 工作流程能提升產出品質，但完全沒有談到誰來檢查。

**以下「交給你什麼文件」和「該檢查什麼」，都是我們的解讀，不是 Ng 的。**實際的 agent 通常會混用好幾種模式。一個 coding agent 可能在同一次工作裡規劃、跑工具、再檢查自己的成果，所以四種文件你常常會一次全收到。

## 1. Reflection：一份已經自己審過的草稿

Ng 談 reflection 的那篇，把它說成是把原本由人給的回饋自動化：「What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?」（如果把提出批評性回饋這一步自動化，讓模型自動批評自己的產出、改進它的回答呢？）

**通常會交給你：**一份改過的文件，有時附上一段自我檢查，或是「邊界情況都再確認過了」之類的句子。

**該檢查什麼：**拿結果對照「你」的要求，不是對照 agent 自己的批評。自我檢查也會出錯。Chip Huyen 寫道：「An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it’s accomplished a task when it hasn’t.」（有一種有趣的規劃失敗，是反思出錯造成的：agent 深信自己已完成任務，但其實並沒有。）Lilian Weng 在 2023 年 6 月（當時任職 OpenAI）於她的部落格 Lil’Log 談到當時的模型：「The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.」（缺乏專業知識可能使 LLM 不知道自己的缺陷，因而無法妥善判斷任務結果的正確性。）她描述的那項研究裡，LLM 對結果的評估和人類專家的評估並不一致。文件裡寫「已驗證」的話，自己挑一項查。

## 2. Tool use：一份「跑了什麼」的報告

**通常會交給你：**一份總結，說 agent 跑了什麼、搜了什麼、得到什麼結果。「跑完測試：全部通過。」一張結果表格。它找到的一串連結。

Anthropic 的指南把工具結果說成 agent 自我檢查的依據：「During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.」（執行過程中，agent 必須在每一步從環境取得「ground truth」，例如工具呼叫的結果或程式執行的結果，用來評估自己的進度。）這個檢查發生在 agent 內部。到你手上的，是 agent 對這些結果的轉述。

**該檢查什麼：**每個宣稱都要追得回你看得到的輸出。挑總結裡的一個數字，對照真正的輸出；點開其中一個連結看看。

## 3. Planning：`plan.md`

**通常會交給你：**一份計畫、一份規格，或一份 agent 做完一項就勾一項的待辦清單。

Ng 在 Part 4 對這個模式講得很坦白：

> “On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.”

（一方面，規劃是非常強大的能力；另一方面，它會導致較難預測的結果。就我的經驗，Reflection 和 Tool Use 這兩種模式我都能讓它們穩定運作、提升應用程式的表現，但 Planning 還是比較不成熟的技術，我很難事先預測它會怎麼做。）

他也很樂觀：「But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.」（不過這個領域持續快速發展，我相信規劃能力很快就會進步。）

**該檢查什麼：**在執行前審計畫，用〈[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)〉的方法：看架構、查一個宣稱、找出回不去的步驟、看圖表、看影響範圍。agent 中途改寫計畫的話，拿它和你核准的版本比對；如果有用 git，`git diff plan.md` 就看得到改了什麼。在 MarsDawn 裡，「大綱」分頁讓你一眼看出長計畫的架構；計畫被改寫時會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改。

## 4. Multi-agent collaboration：好幾份檔案，好幾個作者

**通常會交給你：**一個 agent 寫的規格、另一個寫的實作筆記、第三個寫的審查意見，還有它們之間互相交接的摘要。有時每個 agent 各自在自己的分支或 worktree 裡工作。

**該檢查什麼：**交接的地方。一個 agent 在總結另一個的成果時，看有沒有哪條需求沒被帶過去。找出彼此矛盾的兩份檔案，在任何人接著往下做之前，先決定哪一份才算數。在 MarsDawn 裡，用「檔案 ▸ 打開資料夾⋯」（⇧⌘O）打開它們共用的資料夾：agent 寫出新檔案，大約一秒內就會出現在「檔案」分頁；如果是 git 檢出，清單上方會標出分支或工作樹，兩個視窗就算開著不同分支上同名的檔案，也不會搞混。成果要交給不讀 Markdown 的人時，可以看〈[把 agent 寫的東西交出去，不用教對方 Markdown](/zh-hant/sharing-exported-pdfs/)〉。

## 一覽表

| 模式（Ng 提出） | 通常會交給你（我們的推論） | 先讀哪裡（我們的建議） |
|---|---|---|
| Reflection 反思 | 一份改過的草稿，可能附自我檢查 | 對照你自己的要求；挑一個「已驗證」自己查 |
| Tool use 使用工具 | 一份「跑了什麼、得到什麼」的報告 | 挑一個宣稱，追回真正的輸出 |
| Planning 規劃 | `plan.md`、規格、待辦清單 | 執行前的五分鐘審閱 |
| Multi-agent collaboration 多 agent 協作 | 好幾個 agent 寫的好幾份檔案，可能分散在不同分支 | 交接的地方，以及哪一份才算數 |

上面引用的作者都沒有提到 MarsDawn，也沒有推薦 MarsDawn 或任何 Markdown 工具。MarsDawn 裡沒有 AI 模型：它不知道一份檔案是哪種模式產生的，也不會替你做這些檢查。它負責讓這些檔案在你檢查的時候保持好讀。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF，詳見〈[Markdown 轉 PDF 工具](/zh-hant/markdown-to-pdf/)〉。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- agent 的產出為什麼難讀，以及一份檢查清單：[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。
- 完整的計畫審閱方法：[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)。
- 透明對你的要求是什麼、不是什麼：[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)
- Andrew Ng 自己怎麼幫這些模式排序，更深入的一篇：[Andrew Ng 自己幫四種設計模式的可預測程度排序](/zh-hant/reading-notes/andrew-ng-design-patterns/)
- Lilian Weng 更早的 agent 藍圖，更深入的一篇：[Lilian Weng 2023 年畫的 agent 藍圖，每個部件會留下什麼檔案](/zh-hant/reading-notes/lilian-weng-llm-agents/)

## 資料來源

- Andrew Ng，〈Agentic Design Patterns Part 1〉，The Batch，2024 年 3 月 20 日：[https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng，〈Agentic Design Patterns Part 2, Reflection〉，The Batch，2024 年 3 月 27 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng，〈Agentic Design Patterns Part 4, Planning〉，The Batch，2024 年 4 月 10 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen，〈Agents〉，2025 年 1 月 7 日：[https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng，〈LLM Powered Autonomous Agents〉，Lil’Log，2023 年 6 月 23 日：[https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. 與 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) （引文依 2026-09-26 的線上版本）

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
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
