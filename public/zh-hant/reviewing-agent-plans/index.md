# 五分鐘審完一份 agent 計畫

agent 寫好一份計畫，正等你點頭。你手上只有五分鐘，不是一個小時。下面這套做法用什麼編輯器都行，連純文字編輯器也可以。其中幾步 MarsDawn 幫得上忙，我們會講清楚是哪幾步；最重要的那一步，它幫不上。

**不要從頭讀到尾。先看架構，再查一個宣稱，找出做了就回不去的步驟，看圖表和影響範圍，最後寫出 agent 看得懂、改得動的回饋。六個步驟，大約五分鐘。**

## 為什麼要在執行前審

Chip Huyen 解釋為什麼規劃要和執行分開時，把代價講得很白：「Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.」（沒有監督的話，agent 可能執行那些步驟好幾個小時，在 API 呼叫上浪費時間和金錢，你才發現它根本沒有進展。）我們補一句：計畫是抓錯最便宜的地方。在 `plan.md` 裡改一行，只要一句話；等 agent 跑完再收拾，可能要花掉一個下午。

## 範例

你請 agent 把使用者頭像搬到物件儲存，而且舊連結不能壞。它交回來的是這份：

```
# 計畫：把使用者頭像搬到物件儲存

## 目標
頭像改由物件儲存提供，不再放在 app 伺服器上。

## 步驟
1. 加入儲存用的 client 與設定。✅ 完成
2. 寫一支腳本，把現有頭像複製到 bucket。
3. 把模板裡的頭像網址換掉。
4. 從伺服器刪除 `public/avatars/`。
5. 執行複製腳本。

## 狀態
所有測試都通過。
```

讀起來很順。照做的話，它也會在複製任何一張頭像之前，先把全部頭像刪光。

## 六個步驟

**1. 先只看標題。**（大約一分鐘）大綱和你要求的對得上嗎？少一段，通常就是少做一件事。這份只有「目標」「步驟」「狀態」。你要求舊連結不能壞，可是沒有任何一段講舊連結，也沒有講出問題時怎麼退回去。這就是你的第一條意見。

在終端機跑 `grep -n '^#' plan.md`，就只會印出標題；大部分編輯器也有大綱檢視。在 MarsDawn 裡，側邊欄（「顯示方式 ▸ 顯示側邊欄」，⌃⌘S）的「大綱」分頁會列出所有標題，點一下就跳過去。

**2. 找出所有寫著「完成」「通過」「已驗證」的地方，挑一個自己查。**（大約一分鐘）打開那個檔案、跑那個測試、數一下筆數。Chip Huyen 描述過一種失敗：「The agent is convinced that it’s accomplished a task when it hasn’t.」（Agent 深信自己已完成任務，但其實並沒有。）她舉的例子是：請 agent 把 50 個人分到 30 間飯店房間，它只排了 40 人，還堅稱做完了。

```
grep -n -E '完成|通過|驗證|✅' plan.md
```

在這份計畫裡，會找到「✅ 完成」和「所有測試都通過」。是哪些測試？有任何一個碰到頭像嗎？自己跑一次，或直接問。這一步 MarsDawn 沒辦法替你做，除了你，沒有人能替你做。

**3. 找出做了就回不去的步驟。**（大約一分鐘）刪資料、資料庫遷移、force push，還有任何會寄出、付款或發佈的動作。這些要等你明確點頭。Chip Huyen 從系統設計的角度講過同一件事：「If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.」（如果計畫牽涉有風險的操作，例如更新資料庫或合併程式碼變更，系統可以在執行前要求人類明確核准，或交給人類自己執行。）這份計畫的第 4 步會刪掉原始檔案，而且排在第 5 步複製之前。

**4. 圖表要看畫出來的樣子，逐一對照每個箭頭和文字說的是不是同一回事。**流程圖畫著「複製 → 檢查 → 刪除」，步驟卻不是這個順序，這本身就是一個發現。這份計畫沒有圖，今天可以跳過。有圖的時候，請看畫出來的圖，不要看 Mermaid 原始碼：很多編輯器都有預覽，〈[在 Mac 上怎麼看 Markdown 檔案](/zh-hant/view-markdown-on-mac/)〉和〈[在別處看 Markdown，對比 MarsDawn](/zh-hant/vs/markdown-preview-tools/)〉整理了各種做法。在 MarsDawn 裡，畫好的圖就在原始碼旁邊（⌘2）；圖表寫錯時，預覽會顯示原始碼、下方附上錯誤訊息，這也值得單獨寫一條意見。

**5. 列出計畫會動到的檔案和系統，你沒要求的部分，先問清楚。**（第 4、5 步合起來大約一分鐘）這份會動到：儲存設定、模板、伺服器上的一個資料夾、一個 bucket。這個 bucket 誰讀得到？你沒說它要公開。如果你用 MarsDawn 打開 agent 工作的資料夾（「檔案 ▸ 打開資料夾⋯」，⇧⌘O），它新寫的檔案大約一秒內就會出現在「檔案」分頁，清單上方也會標出 git 分支或工作樹，你就知道自己審的是哪一份檢出。

**6. 回饋寫成「位置、問題、改法」，一行只講一個問題。**（最後一分鐘）

```
plan.md:10：第 5 步還沒複製，這裡就先刪了。先複製、核對數量，再刪；刪之前等我確認。
plan.md:14：是哪些測試？加一個切換後載入舊頭像網址的測試。
plan.md:6：沒有處理舊連結。加一步讓舊連結繼續能用，也寫出怎麼退回去。
```

有行號的編輯器都能做到。在 MarsDawn 裡，「編輯 ▸ 拷貝引用」（⌥⌘C）會把目前位置拷貝成 `plan.md:10`，「拷貝給 AI」（⌃⌥⌘C）會在下面附上你選取的文字。

## 只有一分鐘的話

就做第 2 步吧。以為自己已經做完的 agent，多半是在這一步被抓到的。

## 五分鐘不夠的時候

有時候你判斷不了某一步對不對，因為它超出你熟悉的範圍。Jess Ou 在 LangChain 2026 年介紹 agent 的文章裡，用兩句話講完：「Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.」（無法評估的判斷，就不要外包出去。如果你自己認不出正確答案，agent 也認不出來。）我們的看法是：判斷不了，不是趕快核准的理由，而是該去找懂的人問一下的理由。

## MarsDawn 在這裡做什麼、不做什麼

MarsDawn 裡沒有 AI 模型。它不會幫你找出這份計畫的問題，第 2、3 步也不會替你做。它做的是讓檔案在你審的時候保持好讀：第 1 步有大綱，第 4 步有畫好的圖，第 5 步有「檔案」分頁，第 6 步有行號引用。你讀到一半 agent 改了計畫，MarsDawn 會重新載入，停在你原本讀到的位置，前提是你自己沒有未儲存的修改。

計畫定案、要給別人看的時候，〈[把 agent 寫的東西交出去，不用教對方 Markdown](/zh-hant/sharing-exported-pdfs/)〉和〈[Markdown 轉 PDF 工具](/zh-hant/markdown-to-pdf/)〉說明了怎麼轉成 PDF 交出去。

## 試試看

MarsDawn 即將在 Mac App Store 上架。免費的 `marsdawn` 命令列工具現在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 輸出成 PDF。

[命令列工具](/zh-hant/cli/) · 買之前先看：[MarsDawn 做不到的事](/zh-hant/limits/)

## 接下來

- agent 的產出為什麼難讀：[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。
- agent 為什麼要把計畫攤開：[Anthropic 說 agent 要透明，那攤開的東西誰來讀？](/zh-hant/agent-transparency/)
- agent 交回來的不只有計畫：[四種 agent 設計模式，各自會交給你什麼文件](/zh-hant/agent-design-patterns/)。

## 資料來源

- Chip Huyen，〈Agents〉，2025 年 1 月 7 日：[https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou，〈What is an AI agent?〉，LangChain，2026 年 7 月 31 日：[https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

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
- [agent 設計模式](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [更新紀錄](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [範本](https://marsdawn.southern-light.dev/zh-hant/templates/index.md): 給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。
- [規格文件範本](https://marsdawn.southern-light.dev/zh-hant/templates/spec/index.md): Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。
- [流程圖範本](https://marsdawn.southern-light.dev/zh-hant/templates/flowchart/index.md): Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。
- [會議記錄範本](https://marsdawn.southern-light.dev/zh-hant/templates/meeting-notes/index.md): Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
