# Mac 怎麼開 md 檔。

雙擊就能打開。如果你的 Mac 用文字編輯器打開，看到的是 `#` 和 `**`，而不是標題和粗體，檔案沒有壞：`.md` 檔本來就是純文字，編輯器只是照原樣顯示。改用會排版 Markdown 的 app（例如 MarsDawn）打開，再把它設成預設 app，之後每個 `.md` 檔都會在那裡打開。

`.md` 檔案是純文字。標題、粗體、表格和圖表，都是用記號寫成的：`#` 代表標題，`**` 包住粗體，直線符號畫出表格，`mermaid` 程式碼區塊則是一張圖。用純文字編輯器打開，看到的就是這些記號。想照作者的意思讀到排好的頁面，就需要有東西把它排版出來。

## 在 Mac 上打開 md 檔

1. **雙擊檔案。** 檔案會用你的 Mac 為 `.md` 設定的 app 打開。如果沒有任何 Markdown app，常常就是純文字編輯器，看到的是記號，不是排好的頁面。
2. **自己選 app。** 按住 Control 點檔案，選「打開檔案的應用程式」，再選 app。或者選「檔案 ▸ 取得資訊」（⌘I），在「打開檔案的應用程式：」選一個 app，再按「全部更改⋯」，以後這類檔案都會用它打開。MarsDawn 能打開 `.md`、`.markdown`、`.mdown`、`.mkd` 和 `.mkdn`。
3. **不打開，直接預覽。** 在 Finder 選取檔案，按空白鍵。裝了 MarsDawn 的話，「快速查看」會顯示排版後的頁面，圖表也在。

## 在 MarsDawn 裡讀

MarsDawn 是為 Mac 做的 Markdown 編輯器，可以在 Mac App Store 免費下載：先免費試用全部功能 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。需要 macOS 26 以上。

[到 Mac App Store 免費下載 MarsDawn](https://apps.apple.com/app/id6812925073)

打開 `.md` 檔案，排好的頁面就在原始碼旁邊：

- 預覽會隨著你打字即時更新，兩邊的窗格一起捲動。
- [Mermaid](/zh-hant/mermaid-preview-mac/) 流程圖和循序圖直接畫在預覽裡，程式碼區塊也會上色。
- 想改的時候，原始碼就在旁邊。MarsDawn 是編輯器，不只是檢視器。

如果這份檔案是 AI agent 寫的，這正是 MarsDawn 要支援的循環：agent 寫，你讀排好的頁面，agent 再修改。請看[首頁](/zh-hant/)，想讓 agent 幫你開檔案，請看[給 AI agent 的 marsdawn 參考](/zh-hant/cli/agents/)。為什麼這樣的閱讀重要、怎麼審一份計畫，請看[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)和[五分鐘審完一份 agent 計畫](/zh-hant/reviewing-agent-plans/)。

## 不裝 app 也行：轉成 PDF

免費的 `marsdawn` 命令列工具，能把 Markdown 檔案排版成 PDF，任何一台 Mac 都打得開。表格、數學式、Mermaid 圖表和程式碼上色都會排好，而且不需要安裝其他東西，連 MarsDawn app 都不用。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` 會在 Markdown 檔案旁邊寫出 `notes.pdf`，`open` 會用你的 PDF 檢視器打開它。這個工具需要 macOS 15 以上。完整步驟和一頁實際匯出的結果，請看[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。

## 常見問題

### md 檔是什麼？

`.md` 檔是用 Markdown 寫成的純文字檔。Markdown 用簡單的字元標記文字：`#` 是標題，`**` 包住的是粗體，直線符號畫出表格。`.markdown`、`.mdown`、`.mkd`、`.mkdn` 是同樣的東西。開發者拿它寫 README 和文件，AI agent 也常把計畫和報告寫成 `.md` 檔交回來。

### 為什麼 md 檔打開是純文字，滿是 # 和 ** ？

因為它本來就是純文字，純文字編輯器只會照原樣顯示，檔案沒有壞。想看到標題、粗體、表格和圖表，要用會排版 Markdown 的 app 打開。在 MarsDawn 裡，排好的頁面就在原始碼旁邊。

### 為什麼打開是亂碼？

亂碼通常是因為檔案存成 UTF-8 以外的文字編碼，而打開它的 app 猜錯了。解法是另存一份 UTF-8 的副本。MarsDawn 打開不是 UTF-8 的純文字檔時會以唯讀開啟，並在視窗上方的提示列寫出它當成哪種編碼來讀；那裡的「儲存為 UTF-8⋯」，或「檔案 ▸ 儲存為⋯」（⌥⇧⌘S），可以存出一份能編輯的 UTF-8 副本。

### md 檔可以轉成 PDF 嗎？

可以。在 MarsDawn 選「檔案 ▸ 輸出為 PDF⋯」（⌥⌘E）或「檔案 ▸ 列印⋯」，頁面會自動分頁，圖表畫進去，程式碼保留上色，使用主題的淺色配色。不裝 app 的話，免費的 `marsdawn export` 命令列工具能輸出同樣的 PDF：`marsdawn export notes.md`。請看[輸出 PDF](/zh-hant/pdf/)和[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。

### AI agent 寫的 md 檔也能這樣打開嗎？

可以，MarsDawn 就是為這個做的。打開檔案，排好的頁面就在原始碼旁邊；agent 改好之後，再打開來讀一次。agent 也可以執行 `marsdawn open plan.md`，在 MarsDawn 裡把檔案打開給你。請看[讀懂 agent 交回來的 Markdown](/zh-hant/reading-agent-output/)。

## 接下來

- 命令列工具的所有選項：[命令列工具](/zh-hant/cli/)。
- MarsDawn 做不到的事：[這份清單](/zh-hant/limits/)。
- 改用 VS Code、瀏覽器或 Claude Desktop 看 Markdown：[比較一下](/zh-hant/vs/markdown-preview-tools/)。
- Markdown 檔裡的圖表：[在 Mac 上預覽 Mermaid](/zh-hant/mermaid-preview-mac/)。

## 其他頁面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hant/index.md): 給要掌舵 agentic 開發的人用的 Markdown：原生的 Mac 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出。已在 Mac App Store 上架。
- [功能一覽](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [你寫的內容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hant/yours/index.md): MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。
- [免費試用，買一次就好](https://marsdawn.southern-light.dev/zh-hant/pay-once/index.md): MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。
- [輸出 PDF](https://marsdawn.southern-light.dev/zh-hant/pdf/index.md): 在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。
- [為 Mac 而做](https://marsdawn.southern-light.dev/zh-hant/native/index.md): 真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hant/limits/index.md): 沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號。內建四種主題，主題庫還有更多。購買前先知道。
- [支援](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [隱私權政策](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [在 Mac 上預覽 Mermaid](https://marsdawn.southern-light.dev/zh-hant/mermaid-preview-mac/index.md): 在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。
- [Markdown 轉 PDF](https://marsdawn.southern-light.dev/zh-hant/markdown-to-pdf/index.md): 免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。
- [MacMD Viewer 對比 MarsDawn](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
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
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI agent 写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [日本語](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App festlegen, Übersicht im Finder. Von einem KI-Agenten geschriebene .md-Dateien liest du gerendert in MarsDawn.
- [Français](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Comment ouvrir un fichier .md sur Mac : double-clic, app par défaut, coup d’œil dans le Finder. Pour les .md écrits par un agent IA, lisez-les rendus dans MarsDawn.
- [Español](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Los .md que escribió un agente de IA, léelos renderizados en MarsDawn.
- [한국어](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
