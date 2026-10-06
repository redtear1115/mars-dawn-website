# Anthropic 說 agent 要透明，那攤開的東西誰來讀？

Anthropic 在 2024 年 12 月發表了〈Building Effective Agents〉，寫給打造 AI agent 的人。文章的總結列出三個原則，其中一個是透明。這篇要談的是這個原則的另一端：agent 把步驟攤開之後，總得有人去讀。

**透明是 agent 要做到的事，讀是你要做的事。Anthropic 要求開發者把 agent 的規劃步驟攤開；對大多數在驅動 coding agent 的人來說，這些步驟最後會變成一份 Markdown 檔案，要有人在對的時間點讀它。**

## 指南裡寫了什麼

Erik S. 與 Barry Zhang 在總結裡這樣寫：

> “When implementing agents, we try to follow three core principles: Maintain simplicity in your agent's design. Prioritize transparency by explicitly showing the agent’s planning steps. Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing.”

（實作 agent 時，我們盡量遵守三個核心原則：讓 agent 的設計保持簡單；優先重視透明度，明確展示 agent 的規劃步驟；透過完整的工具文件與測試，仔細打造 agent 與電腦之間的介面（ACI）。）

這些是寫給開發 agent 的人的設計原則，不是給使用者的操作指示。原則要求把步驟攤開，但沒有說誰來讀。

同一篇也描述了 agent 拿到任務之後會做什麼：「Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement.」（任務明確之後，agent 會自己規劃、獨立運作，必要時回頭找人類要更多資訊或判斷。）還有：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」（Agent 可以在檢查點或遇到阻礙時暫停，等待人類回饋。）注意用詞：*potentially*（必要時）和 *can*（可以）。檢查點是 agent 可以有的設計，不是一定要有。

## 大部分的檢查，不是你在做

這裡很容易講過頭，所以先看指南真正放在前面的是什麼。agent 會拿外界的結果來檢查自己：「During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress.」（執行過程中，agent 必須在每一步從環境取得「ground truth」，例如工具呼叫的結果或程式執行的結果，用來評估自己的進度。）這句話裡的 ground truth 指的是測試結果和工具輸出，不是人。

指南對風險也講得很直接：「The autonomous nature of agents means higher costs, and the potential for compounding errors.」（Agent 的自主性意味著更高的成本，以及錯誤不斷累積的可能。）它給的解方是在沙盒環境裡大量測試、加上適當的防護，並沒有說「要讀得更仔細」。

人真正出場，是在附錄談 coding agent 的段落：「However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.」（然而，自動化測試雖然有助於驗證功能，但要確保解法符合更廣泛的系統需求，人工審閱仍然至關重要。）這句講的是程式碼。不過它點出的落差，用過 agent 的人都不陌生：測試能告訴你東西能動，不能告訴你那是不是你要的。

## 攤開的步驟，最後去了哪裡

**以下是我們的解讀，不是 Anthropic 的主張。**

如果你每天都在用 coding agent，它的規劃步驟通常不會出現在什麼儀表板上，而是變成檔案：`plan.md`、一份有勾選框的待辦清單、一個 agent 一直在改寫的進度檔，最後再來一份總結。從你這邊看，透明的意思就是要讀的東西變多了。

把步驟攤開，是 agent 那一半的責任。另一半，是有人在關鍵時刻讀它：資料庫遷移執行之前、分支合併之前、接受「做完了」之前。一個 agent 把所有東西都寫進一份 600 行、沒人打開的檔案，紙面上很透明，實際上沒人在看。

Harrison Chase 在 2024 年也講過類似的話，不過他談的是 agent 框架該怎麼設計，不是文件：「You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.」（你會希望能觀察系統內部發生了什麼，因為它實際採取的步驟事先可能無法得知。）他講的是給開發 agent 的人用的工具。如果你是驅動 agent 的那個人，它一直在寫的那份純文字檔，常常就是你看得到的部分。

以上幾位作者都沒有提到 MarsDawn，也沒有推薦 MarsDawn 或任何 Markdown 工具。

## 比看起來難讀

檔案很長，重要的地方很少在最上面。說明這次改動的那張圖，是一段 Mermaid 原始碼，不是圖（想在 Mac 上看到排好的樣子，可以先看[在 Mac 上怎麼看 Markdown 檔案](/zh-hant/view-markdown-on-mac/)）。你讀到一半，agent 可能正在改寫它。檔案常常不只一份，有時還分散在不同的分支或 worktree。等你真的找到問題，說「快取那段怪怪的」，agent 只能用猜的。完整的說明在[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。

## MarsDawn 幫得上、幫不上的地方

MarsDawn 是為這種閱讀做的 Mac app。它不會讓 agent 變得更透明，裡面也沒有 AI 模型：它不會幫你摘要計畫，也不會告訴你計畫對不對。它做的是：

- **檔案很長：**「顯示方式 ▸ 顯示側邊欄」（⌃⌘S）打開「大綱」分頁，列出所有標題，點一下就跳過去。
- **圖表和數學式：**原始碼和排好的頁面並排（⌘2），兩邊一起捲動，Mermaid 和 KaTeX 直接畫出來。圖表寫錯時，預覽會顯示它的原始碼，下方附上錯誤訊息。
- **讀到一半被改寫：**agent 改寫檔案時，MarsDawn 會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改。
- **好幾個檔案：**用「檔案 ▸ 打開資料夾⋯」（⇧⌘O）打開 agent 工作的資料夾，新檔案大約一秒內就會出現在「檔案」分頁；如果是 git 檢出，清單上方會標出分支或工作樹。
- **指出是哪一行：**「編輯 ▸ 拷貝引用」（⌥⌘C）把目前位置拷貝成 `docs/plan.md:42`，「拷貝給 AI」（⌃⌥⌘C）會在下面附上你選取的文字，直接貼給 agent 就好。

讀的人還是你。MarsDawn 負責讓一份又長又會變的檔案，在你讀的時候保持好讀。

## 試試看

MarsDawn 已在 [Mac App Store](https://apps.apple.com/app/id6812925073) 上架。另外還有免費的 `marsdawn` 命令列工具：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- agent 的產出為什麼難讀，以及一份檢查清單：[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。
- 那份清單一步一步來，附實際例子：[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)。
- 不同類型的 agent 會交給你什麼文件：[四種 agent 設計模式，各自會交給你什麼文件](/zh-hant/agent-design-patterns/)。
- 為什麼 AI 寫的東西需要人讀，短一點的版本：[為什麼 AI 寫的東西還是需要人讀過](/zh-hant/reviewing-ai-output/)。

## 資料來源

- Erik S. 與 Barry Zhang，〈Building Effective Agents〉，Anthropic，2024 年 12 月 19 日：[https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) （引文依 2026-09-26 的線上版本；該文現已註明，文中提到的工具生態自 2024 年 12 月以來已有很多改變）
- Harrison Chase，〈What is an agent?〉，LangChain，2024 年 6 月 28 日，存檔版本：[http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) （原網址現在顯示的是 2026 年的另一篇文章）

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [預覽主題與 PDF 輸出](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 四種主題，各有淺色與深色，一套輸出對應你正在看的主題。更多可匯入的主題，和讓大家投稿主題的主題庫，都在規劃中。
- [分享輸出的 PDF](https://marsdawn.southern-light.dev/zh-hant/sharing-exported-pdfs/index.md): 把 agent 寫的 Markdown 輸出成 PDF，交給不寫 Markdown、也不會安裝任何東西的同事。不用懂語法，不用裝 app，也不需要帳號就能打開。
- [為什麼 AI 寫的東西還是需要人讀過](https://marsdawn.southern-light.dev/zh-hant/reviewing-ai-output/index.md): AI 寫的 Markdown 還是得由人來理解，不能因為讀起來通順就直接相信。MarsDawn 把排版後的頁面和原始碼並排，也把 Mermaid 圖表與 KaTeX 數學式畫出來，讓結構一眼就看得懂。
- [讀懂 agent 交回來的 Markdown](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [審 agent 計畫](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
