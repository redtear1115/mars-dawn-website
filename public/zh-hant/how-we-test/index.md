# 在一台 Mac 上通過的測試，不一定在測你以為的東西。

黑色星期五特價：一次解鎖只要半價 USD 2.49（原價 USD 4.99），優惠到 11 月 30 日，12 月 1 日起恢復 USD 4.99。 <!-- sale-line -->

vibe coding 不是壞事，MarsDawn 也是用 agent 開發的。但要讓人長期依賴的軟體，看的是第一版之後的事：多年的維護和安全，而這要從確認改動沒有改壞東西開始。

**同一個測試，在 Mac mini 上通過，在 MacBook Air 上失敗。產品沒壞。是測試透過螢幕的色彩描述檔在讀顏色，它在 Mac mini 上通過只是運氣好。換一台機器，抓到的是測試的 bug，不是程式的 bug。**

只想知道 MarsDawn 會拿哪些極端或惡意的檔案來測試？可以直接跳到〈[我們丟給它的東西](#inputs)〉。

## 只在 MacBook Air 上失敗的測試

輸出引擎的測試，在 GitHub 的 macOS 15 機器上完整跑一次將近一小時：debug 版約 32 分鐘，release 版約 25 分鐘。為了縮短時間，我們試著把 macOS 26 那一半移到自己的 MacBook Air 上跑（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)）。

在那台機器上第一次跑，就有一個測試失敗。這個測試會輸出一份帶有提示框（Note、Tip、Warning）的 PDF，檢查每個提示框邊上的色條顏色對不對，也就是色差要小於 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。換到 Mac mini，同一個 commit、同樣的 macOS 和 Xcode，測試通過。

我們第一個懷疑是輸出壞了。結果不是：PDF 本身沒問題，兩台機器不一樣的，是測試讀它的方式。

這個測試會把 PDF 每一頁畫成圖片再讀像素，而 macOS 畫這張圖時，用的是主螢幕的色彩空間。Mac mini 接的是一般的外接螢幕，MacBook Air 用的是內建螢幕。我們拿一張填滿同一種橘色的圖片讀回來：(0.784, 0.278, 0.106) 在 Mac mini 上讀成 (0.822, 0.335, 0.179)，在 MacBook Air 上讀成 (0.782, 0.395, 0.221)。

重點在這裡：在 Mac mini 上，測試讀到的顏色其實也不對，最多差了 0.128，只是剛好落在 0.16 的上限內。它會通過，靠的是那台螢幕，不是因為它真的量對了色條。

修正（[kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)）只改測試：把頁面畫進一張固定使用 sRGB 色彩空間的圖片，完全不經過螢幕。現在兩台機器都能準確讀出色條的顏色：不論是 MacBook Air 的內建螢幕還是 Mac mini，色差都是 0.0。這個 pull request 的 CI 全部通過（[run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)），修正併入 MacBook Air 測試分支後，那台機器上的完整測試也全部通過（[run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)）。接著我們故意讓它失敗：把每個預期顏色都改成藍色，五個提示框全部變紅。

它還有一個已知的漏洞：Note 和 Caution 用的兩種橘色只差約 0.119，在 0.16 的上限內，所以這兩個顏色如果對調，測試多半不會發現。我們把這件事記了下來，沒有假裝這個測試已經完整。

一個不會失敗的測試，什麼也保護不了；因為錯的理由而失敗的測試（例如螢幕的色彩描述檔）也一樣。一台機器上的綠燈，只代表測試在那台機器上通過，不代表它測的就是名字上寫的那件事。

## 測試是一層一層的網子

沒有一個測試能抓到所有問題。每一層都是一張網目不同的網，從這一層漏掉的錯，應該要被下一層接住：

- **參考 PDF：**輸出引擎（開源的 [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)，`marsdawn` 指令也用它）把一組樣本文件輸出成 PDF，每一頁的文字都和事先記錄的版本比對。抓內容悄悄不見，或頁數突然改變。
- **不同的系統和版本：**引擎在 macOS 15（支援的最舊版本）和 macOS 26（App 實際出貨的版本）上都要跑，各跑 debug 和 release 兩種版本。App 的完整測試則跑四種組合：簽章與不簽章，各自再分付費牆開與關。抓只在舊系統上壞掉，或只在使用者實際拿到的版本裡壞掉的問題。
- **真的硬體：**App 的 CI 跑在我們自己的 Mac 上（Mac mini 和 MacBook Air 兩台都跑）；把引擎的測試搬到那台 MacBook Air 試跑（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)，目前仍是實驗草稿），就是抓到上面那個色彩描述檔問題的契機。換一台機器，能抓到只因為跑在某台機器上才通過的測試。
- **紅燈對照組：**App 的 CI 固定放著 22 份故意弄壞的清理腳本和 20 份故意弄壞的測試執行腳本，每份都拿掉一道安全檢查，測試碰到每一份都必須失敗。清理腳本會刪掉 Mac 上舊的建置和工作副本，少一道檢查就可能刪錯東西。只要有一份弄壞的通過，壞掉的就是測試本身。
- **另一雙眼睛：**我們的做法是合併前把改動交給另一個 agent 驗證，像 kit #242 那樣；牽涉到使用流程的改動，會先做情境審查。抓「說做完了其實沒做完」，以及程式能跑、卻用錯了場合。
- **最後由人合併。**每個改動都由 MarsDawn 的開發者本人審過、親手合併；agent 和 bot 都不會合併。

## 我們丟給它的東西

網子好不好，要看丟進去的是什麼。下面是引擎測試會餵給它的幾種輸入，以及每個測試確保會發生的事：

- **超大的檔案。**在我們的測試機上、以 release 版來量：2 MB 的文件在一秒半內顯示完；5 MB、複雜到排不了版的文件照樣打得開，一秒內以純文字顯示。超過 16 MB 的檔案完全不解析，直接以文字顯示。
- **幾十萬行。**大約 3 MB、每行只有一個字的文件，將近 80 萬行，讀到一半就會被判定太多：引擎在那裡停下來，改以純文字顯示。
- **永遠不關的標記。**1 MB 只開不關的區塊標記，或疊了幾萬層的區塊，花的時間不能超過同樣 1 MB 純文字的兩倍左右；超過八層的部分不再往下巢狀。
- **數學公式。**寫錯的公式就在原處顯示錯誤，不會讓整頁壞掉。超過一萬個字元的公式保留原樣；一份文件一次最多畫前 1,000 個；公式裡的內容也不會變成連結、圖片或網頁標籤。
- **藏在 Markdown 裡的惡意 HTML。**指令碼會被移除，絕不執行；內嵌的框架在頁面顯示前就被拿掉。遠端圖片預設不載入，就算你允許，也只載入安全連線（HTTPS）的圖片。另有一份拿掉指令碼過濾的對照版本，測試碰到它必須失敗。
- **惡意的主題檔。**會被拒絕，錯誤訊息也不會重複檔案裡隱藏的控制字元或連結。超過 16 KB 的主題檔直接不讀。

這些都有代價。引擎單次執行的時間上限從 30 分鐘拉到 45、50、70，現在已經拉到 90 分鐘；macOS 15 曾在測試全部通過的情況下兩次撞到 50 分鐘上限，後來又在最後一步撞到 70 分鐘，前面所有步驟都已經通過。

## 你也能照做的四個習慣

1. **寫的 agent 和驗的 agent 分開。**只給驗證的那個改動本身和「怎樣才算完成」，不要附上寫程式那個 agent 的解釋，請它自己跑測試，並列出沒驗到的地方。驗 kit #242 時，驗證的 agent 先在 MacBook Air 上跑舊測試、親眼看它失敗，才讓新測試過關。代價是多一個 session 的 token。
2. **每個測試都要看它失敗一次。**只有看過同一個測試在它檢查的東西真的出錯時亮紅燈，綠燈才有意義。所以相信綠燈之前，先把它守著的東西弄壞（或請 agent 弄壞），看它變紅；再改回來，看它變綠。agent 很會寫出會通過的測試，正因為這樣，你才需要看到它失敗。
3. **測試至少在第二個環境跑一次。**沒有第二台 Mac 也沒關係，CI 裡跑兩個 OS 版本，或 debug 和 release 各跑一次，就是不錯的起點。要找的是那些靠運氣才通過的測試。
4. **「一個測試都沒跑」要算失敗。**Python 3.9 的 `unittest` 一個測試都沒找到時，還是會回報成功，所以路徑打錯一個字，你照樣拿到綠燈。我們的 CI 會讀測試數量，是 0 就失敗，也會檢查摘要寫的是「0 failed」，不只看結束代碼。這道檢查，是一次獨立驗證在我們自己的 CI 裡抓到這個漏洞之後才加上的。

## 一句話

一個 App 是不是 vibe coding 做的，沒那麼重要；重要的是有沒有人持續在測試、在維護。選軟體的時候值得看一眼：它有沒有說明自己怎麼測試？最近一次更新是什麼時候？

速度交給 agent，把關留給真的量對東西的測試，以及讀過結果的人。

## 接下來

- 為什麼 agent 寫的東西還是要有人讀過：[為什麼 AI 寫的東西還是需要人讀過](/zh-hant/reviewing-ai-output/)。
- 怎麼讀 agent 交回來的計畫和報告：[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。

## 資料來源

- 失敗的測試和原因：[mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241)。
- 修正和獨立驗證：[mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)。
- 在 MacBook Air 試跑 CI（實驗草稿），附執行時間：[mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)。
- 輸出引擎的 CI，時間上限的調整歷史寫在註解裡：[ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml)。
- App 的程式碼庫不公開；上面關於 App 的內容，來自它的 CI 設定和測試腳本。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 檢查 agent 寫的 Markdown、JSON、YAML：Mac 原生 app，即時預覽、Mermaid、KaTeX、快速查看、PDF。免費試用，之後一次 USD 2.49。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown、JSON、YAML 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可拿去開會或存檔。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 2.49 解鎖一次就好。沒有訂閱，也不需要帳號。
- [列印與 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上先預覽，再把 Markdown 列印或儲存為 PDF；有文件、手冊、講義三種版面，Mermaid 圖表和程式碼上色都會保留。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、iPhone 和 iPad 上不能編輯、沒有外掛、不需要帳號；可以換主題，但不能自訂 CSS。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [Mac 怎麼開 md 檔](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hant/quicklook/index.md): MarsDawn 的快速查看讓你在 Finder 按空白鍵就看到排版後的 Markdown，Mermaid 圖表、KaTeX 數學式和程式碼上色都在。試用期結束後，快速查看照常可用。
- [拷貝給 AI](https://marsdawn.southern-light.dev/zh-hant/copy-for-ai/index.md): 選取文字，連同檔案路徑和行號一起拷貝，貼進 Claude Code 或任何 agent。在 Mac 上就能做，不用開 IDE，也不用裝外掛。
- [從 HackMD 搬到 Mac](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MarsDawn 比較：VS Code 預覽、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日（MarsDawn 的 PDF 格子更新於 2026 年 11 月 7 日）；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 2.49 解鎖一次。逐項比較，附來源。
- [2026 Markdown 閱讀器推薦：只想看、不想改，Mac 和 iPhone 怎麼選](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): Markdown 閱讀器推薦：只想讀、不想改的話，Mac 和 iPhone 各用哪一款。比較 10 款的價格、iPhone／iPad、唯讀、Mermaid、數學式和 PDF，依情境分組。
- [命令列工具](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 輸出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [給 AI agent 的 marsdawn 參考](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [給 agent 的 skill](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 輸出成 PDF，並讀懂 JSON 結果。
- [MCP 伺服器](https://marsdawn.southern-light.dev/zh-hant/cli/mcp/index.md): marsdawn 沒有自己的 AI 模型，是哪個 agent 寫出 Markdown 都無所謂。可以從 CLI、skill 檔案，或 marsdawn-mcp 這個 MCP 伺服器呼叫，三者最後都執行同一個 export。
- [節省 token 的審閱方式](https://marsdawn.southern-light.dev/zh-hant/token-efficient-review/index.md): 人在 MarsDawn 裡讀排版後的頁面，不會被讀回 agent 的 context。工具呼叫本身回傳的也只是精簡的 JSON，不是排版內容，呼叫本身就很便宜。
- [在別處看 Markdown，對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/markdown-preview-tools/index.md): MarsDawn 對比在 VS Code 內建預覽、瀏覽器擴充功能，或 Claude Desktop 檔案預覽裡看 Markdown：各自能排版出什麼，打開一個檔案要花多少功夫。
- [主題](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 內建四種預覽主題，各有淺色與深色；在 Mac 版 MarsDawn 的設定裡打開主題庫，還能安裝更多。快速查看也會用你選的主題。
- [打造一個主題](https://marsdawn.southern-light.dev/zh-hant/themes/new/index.md): 挑選顏色和幾個樣式選項，即時看它們套用在範例文件上，再把主題送出成一個 GitHub issue。不用安裝，也不用 git。
- [和 agent 一起做主題](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [主題庫](https://marsdawn.southern-light.dev/zh-hant/themes/gallery/index.md): 瀏覽 MarsDawn 的預覽主題，每一個都經過開發者審核；可以依情境篩選，也可以檢舉有問題的主題。在瀏覽器裡打造自己的主題，不用安裝，也不用 git。
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
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
