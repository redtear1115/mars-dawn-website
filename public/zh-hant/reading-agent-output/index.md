# agent 做完的工作，最後都變成一份你要讀的 Markdown。

你請 coding agent 規劃一次資料庫遷移、寫一份規格，或追一個 bug。它自己跑了一陣子，交回來的是一個檔案：`plan.md`、`SPEC.md`、一份進度報告，或一份研究摘要。你能檢查的工作，全在這份檔案裡。

**agent 有沒有做對，要讀過它交回來的東西才知道。MarsDawn 就是為這種閱讀做的 Mac app。**

## 做 agent 的人怎麼說

以下引文照原文，我們的解讀放在最後。

- Anthropic 的〈Building Effective Agents〉（Erik S. 與 Barry Zhang，2024 年 12 月）列出打造 agent 的三個核心原則，其中一條是「Prioritize transparency by explicitly showing the agent’s planning steps.」（優先重視透明度：明確展示 agent 的規劃步驟。）這是寫給開發 agent 的人的原則；站在你這邊，這份透明就是你手上那份要讀的計畫。
- 同一篇也寫到：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（Agent 可以在檢查點或遇到阻礙時暫停，等待人類回饋。）注意原文用的是 *can*，可以，沒有說必須。
- Chip Huyen 在〈Agents〉（2025 年 1 月）解釋為什麼規劃要和執行分開：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.」（沒有監督的話，agent 可能執行那些步驟好幾個小時，在 API 呼叫上浪費時間和金錢，你才發現它根本沒有進展。）她也描述了一種失敗：「The agent is convinced that it’s accomplished a task when it hasn’t.」（Agent 深信自己已完成任務，但其實並沒有。）請它把 50 個人分到 30 間飯店房間，它只排了 40 人，還堅稱做完了。
- Andrew Ng 在 The Batch（2024 年 4 月）談 planning 這個設計模式：「On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results.」（一方面，規劃是非常強大的能力；另一方面，它會導致較難預測的結果。）他講的是可預測性，並沒有呼籲要人工審閱，而且他相信規劃能力很快會進步。

**以下是我們的推論，不是作者的主張：**agent 把計畫攤開、在檢查點停下來，那在檢查點讀計畫的通常就是你。agent 可能以為自己做完了，那它的「完成報告」也得有人讀過。上面這幾位作者都沒有提到 MarsDawn，也沒有推薦 MarsDawn 或任何 Markdown 工具。

## 比看起來難讀

檔案很長，重要的地方很少在最上面。裡面有 Mermaid 圖表和數學式，看原始碼很難跟上。你讀到一半，agent 可能還在改寫同一個檔案。它通常不只交一個檔案，有時還分散在不同的分支或 worktree。等你找到問題，說「快取那段怪怪的」，agent 只能用猜的；說「`docs/plan.md:42` 在回填跑完前就把舊表刪了」，它就知道要改哪裡。

## MarsDawn 幫得上忙的地方

- **檔案很長：**側邊欄（⌃⌘S）的「大綱」分頁列出所有標題，點一下，兩邊窗格都會跳過去。
- **圖表和數學式：**Mermaid 和 KaTeX 直接畫在預覽裡，和原始碼並排（⌘2），兩邊一起捲動。
- **讀到一半被改寫：**agent 改寫檔案時，MarsDawn 會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改。
- **好幾個檔案：**用「檔案 ▸ 打開資料夾⋯」（⇧⌘O）打開 agent 工作的資料夾，新檔案大約一秒內就會出現在「檔案」分頁；如果是 git 檢出，清單上方會標出分支或工作樹。
- **回饋要準：**「編輯 ▸ 拷貝引用」（⌥⌘C）把目前位置拷貝成 `docs/plan.md:42`，「拷貝給 AI」（⌃⌥⌘C）會在下面附上你選取的文字，直接貼給 agent 就好。

另外兩件事也和這個循環有關：agent 可以執行 `marsdawn open plan.md:42`，在 MarsDawn 裡幫你打開檔案，直接停在第 42 行，也就是它想先讓你看的那一行；審完的檔案可以從 app 輸出 PDF，也可以用免費的 `marsdawn export` 指令。

MarsDawn 裡沒有 AI 模型。它不會幫你摘要計畫、打分數，也不會告訴你哪裡錯了。讀的人是你，它負責讓又長又會變的檔案保持好讀，讓你能準確指出是哪一行。

## 五分鐘審完一份 agent 計畫

用什麼編輯器都適用。

1. 先只看標題。大綱和你要求的對得上嗎？少一段，通常就是少做一件事。
2. 找出所有寫著「完成」「通過」「已驗證」的地方，挑一個自己查：打開那個檔案、跑那個測試、數一下筆數。
3. 找出做了就回不去的步驟：刪資料、資料庫遷移、force push，還有任何會寄出、付款或發佈的動作。這些要等你明確點頭。
4. 圖表要看畫出來的樣子，逐一對照每個箭頭和文字說的是不是同一回事。
5. 列出計畫會動到的檔案和系統。你沒要求的部分，執行前先問清楚。
6. 回饋寫成「位置、問題、改法」：「`plan.md:88`：回填排在刪表之後，第 4、5 步對調。」一行只講一個問題。

時間只夠做一步的話，就做第 2 步吧。以為自己已經做完的 agent，多半是在這一步被抓到的。完整版本、附實際例子：[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。app 上架之後，agent 也能用 `marsdawn open` 在 MarsDawn 裡幫你打開檔案。

[命令列工具](/zh-hant/cli/) · [給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- 為什麼 AI 寫的東西需要人讀，短一點的版本：[為什麼 AI 寫的東西還是需要人讀過](/zh-hant/reviewing-ai-output/)。
- 審閱時不佔用 agent 的 context：[節省 token 的審閱方式](/zh-hant/token-efficient-review/)。
- agent 為什麼要把計畫攤開：[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)
- 上面那份清單一步一步來，附實際例子：[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)。
- 不同類型的 agent 會交給你什麼文件：[四種 agent 設計模式，各自會交給你什麼文件](/zh-hant/agent-design-patterns/)。

## 資料來源

- Erik S. 與 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) （引文依 2026-09-26 的線上版本；該文現已註明，文中提到的工具生態自 2024 年 12 月以來已有很多改變）
- Chip Huyen，〈Agents〉，2025 年 1 月 7 日：[https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng，〈Agentic Design Patterns Part 4, Planning〉，The Batch，2024 年 4 月 10 日：[https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

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
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
