"""The /templates/ pages (#95): a hub and one page per template, in every locale.

Each template page has the same order: the H1 and lede, a loop animation (loop_anim's scene
engine), the template itself (copy it, or download it), how it looks (the first page of a real
`marsdawn export` PDF, from tools/templates/render_images.sh), a prompt for the agent, sharing it as
a PDF, what it doesn't do, two questions, and the other templates.

English was approved on #97 (2026-09-25). zh-Hant is written from it; zh-Hans and ja are machine
drafts, labelled needs-i18n until reviewed (owner, 2026-09-25).

The downloads are the TEMPLATES below, byte for byte, one per locale:
`/<locale>/templates/<case>/<case>.md`.
"""
import html
import struct
from pathlib import Path

import loop_anim

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://marsdawn.southern-light.dev"
LOCALE_ROOT = {"en": "/", "zh-hant": "/zh-hant/", "zh-hans": "/zh-hans/", "ja": "/ja/"}
CASES = ["spec", "flowchart", "meeting-notes"]
FILES = {case: f"{case}.md" for case in CASES}
SLUGS = ["templates"] + [f"templates/{case}" for case in CASES]
LOOP_MARK = "<!--loop:{case}-->"
IMAGE_DIR = ROOT / "public" / "assets" / "templates"

# The outline row labels on the site's other pages (UI keys), for build_pages' UI tables.
UI_LABELS = {
    "en": {"templates": "Templates", "templates-spec": "Spec template",
           "templates-flowchart": "Flowchart template", "templates-meeting-notes": "Meeting notes template"},
    "zh-hant": {"templates": "範本", "templates-spec": "規格文件範本",
                "templates-flowchart": "流程圖範本", "templates-meeting-notes": "會議記錄範本"},
    "zh-hans": {"templates": "模板", "templates-spec": "规格文档模板",
                "templates-flowchart": "流程图模板", "templates-meeting-notes": "会议记录模板"},
    "ja": {"templates": "テンプレート", "templates-spec": "仕様書テンプレート",
           "templates-flowchart": "フローチャートテンプレート", "templates-meeting-notes": "議事録テンプレート"},
}

LABELS = {
    "en": {"template": "The template", "download": "Download {file}", "looks": "How it looks",
           "ask": "Ask your agent", "share": "Share it as a PDF", "doesnt": "What it doesn't do",
           "faq": "Questions", "more": "More templates", "sep": ": ",
           "img_alt": "The first page of {file}, exported as a PDF with marsdawn export."},
    "zh-hant": {"template": "範本", "download": "下載 {file}", "looks": "長什麼樣子",
                "ask": "交給 agent", "share": "輸出 PDF 分享", "doesnt": "做不到的事",
                "faq": "常見問題", "more": "其他範本", "sep": "：",
                "img_alt": "{file} 用 marsdawn export 輸出的 PDF 第一頁。"},
    "zh-hans": {"template": "模板", "download": "下载 {file}", "looks": "长什么样子",
                "ask": "交给 agent", "share": "输出 PDF 分享", "doesnt": "做不到的事",
                "faq": "常见问题", "more": "其他模板", "sep": "：",
                "img_alt": "{file} 用 marsdawn export 输出的 PDF 第一页。"},
    "ja": {"template": "テンプレート", "download": "{file} をダウンロード", "looks": "見た目",
           "ask": "エージェントに頼む", "share": "PDF で共有する", "doesnt": "できないこと",
           "faq": "よくある質問", "more": "ほかのテンプレート", "sep": "：",
           "img_alt": "{file} を marsdawn export で書き出した PDF の 1 ページ目。"},
}

HUB = {
    "en": {"title": "Markdown templates · MarsDawn",
           "description": "Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.",
           "h1": "Markdown templates",
           "lede": "For the documents an agent writes and you read. Each template comes with a prompt for your agent. Open the filled file in MarsDawn to read what it wrote.",
           "items": {"spec": ("Spec (PRD)", "problem, goals, requirements, a flow diagram and acceptance criteria."),
                     "flowchart": ("Flowchart", "a Mermaid diagram with the steps written out below it."),
                     "meeting-notes": ("Meeting notes", "decisions and action items, with owners.")}},
    "zh-hant": {"title": "Markdown 範本 · MarsDawn",
                "description": "給 agent 寫、你來讀的文件用的 Markdown 範本：規格文件、流程圖和會議記錄，每份都附一段給 agent 的提示詞。",
                "h1": "Markdown 範本",
                "lede": "給 agent 寫、你來讀的文件。每份範本都附一段給 agent 的提示詞。把填好的檔案用 MarsDawn 打開，讀讀它寫了什麼。",
                "items": {"spec": ("規格文件（PRD）", "問題、目標、需求、流程圖和驗收條件。"),
                          "flowchart": ("流程圖", "一張 Mermaid 圖，下方把每個步驟寫出來。"),
                          "meeting-notes": ("會議記錄", "決議和行動項目，每項都有負責人。")}},
    "zh-hans": {"title": "Markdown 模板 · MarsDawn",
                "description": "给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。",
                "h1": "Markdown 模板",
                "lede": "给 agent 写、你来读的文档。每份模板都附一段给 agent 的提示词。把填好的文件用 MarsDawn 打开，读读它写了什么。",
                "items": {"spec": ("规格文档（PRD）", "问题、目标、需求、流程图和验收标准。"),
                          "flowchart": ("流程图", "一张 Mermaid 图，下方把每个步骤写出来。"),
                          "meeting-notes": ("会议记录", "决议和行动项，每项都有负责人。")}},
    "ja": {"title": "Markdown テンプレート · MarsDawn",
           "description": "エージェントが書き、あなたが読む文書のための Markdown テンプレート。仕様書、フローチャート、議事録。それぞれにエージェントへのプロンプトが付きます。",
           "h1": "Markdown テンプレート",
           "lede": "エージェントが書き、あなたが読む文書のために。各テンプレートにはエージェントへのプロンプトが付いています。書き上がったファイルを MarsDawn で開いて、何を書いたか読んでください。",
           "items": {"spec": ("仕様書（PRD）", "課題、目標、要件、フロー図、受け入れ基準。"),
                     "flowchart": ("フローチャート", "Mermaid の図と、その下に書き出した各ステップ。"),
                     "meeting-notes": ("議事録", "決定事項とアクションアイテム。それぞれに担当者。")}},
}

# Per page: title, description, h1, lede, caption, prompt ({url} is the template's own URL),
# share, doesnt, and two questions. Captions, share and FAQ answers may carry <code>.
PAGES = {
    "en": {
        "spec": {
            "title": "Markdown spec (PRD) template · MarsDawn",
            "description": "A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.",
            "h1": "Markdown spec (PRD) template",
            "lede": "A spec your agent can fill in and you can read in one sitting: the problem, goals, requirements, a flow diagram and acceptance criteria. When you change a requirement, ask the agent to bring the rest in line.",
            "caption": "Exported with <code>marsdawn export spec.md</code>. The free command-line tool renders like MarsDawn's preview, diagram included.",
            "prompt": "Write a spec for [the feature] in spec.md, using the template at {url}. Give every requirement an ID, and use the same IDs in the flow and the acceptance criteria. When it's written, run marsdawn open spec.md.",
            "share": "<code>marsdawn export spec.md</code> writes spec.pdf beside it, for someone who doesn't read Markdown.",
            "doesnt": "MarsDawn shows the spec, the table and the diagram. It doesn't check that the acceptance criteria cover every requirement. That's the agent's job, and your read.",
            "faq": [("Does the flow diagram need anything installed?", "No. MarsDawn and <code>marsdawn export</code> draw Mermaid themselves, offline."),
                    ("Can I edit the spec in MarsDawn?", "Yes. It's a Markdown editor with the preview beside the source. The agent sees your edit the next time it reads the file.")],
        },
        "flowchart": {
            "title": "Markdown flowchart template (Mermaid) · MarsDawn",
            "description": "A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.",
            "h1": "Markdown flowchart template",
            "lede": "A Mermaid flowchart with the steps spelled out underneath, so the diagram and the words can be checked against each other. Take a step out, and ask the agent to fix the rest.",
            "caption": "Exported with <code>marsdawn export flowchart.md</code>. The free command-line tool renders like MarsDawn's preview, diagram included.",
            "prompt": "Draw the flow for [the process] in flowchart.md, using the template at {url}. Keep one numbered step per node, in the same order. When it's written, run marsdawn open flowchart.md.",
            "share": "<code>marsdawn export flowchart.md</code> — the diagram is drawn into the PDF.",
            "doesnt": "MarsDawn draws what the Mermaid says. It doesn't lay the diagram out by hand, and it doesn't keep the numbered steps in sync with the nodes. If the Mermaid has an error, the preview shows the error instead of a diagram.",
            "faq": [("Which diagrams work?", "Anything Mermaid draws: flowcharts, sequence diagrams, state diagrams and more."),
                    ("Why write the steps out as well?", "A reader who skims sees the diagram; a reader who checks needs the words. The agent can keep both in step.")],
        },
        "meeting-notes": {
            "title": "Markdown meeting notes template · MarsDawn",
            "description": "A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.",
            "h1": "Markdown meeting notes template",
            "lede": "Decisions first, then action items, each with an owner. Let your agent write the notes from the transcript, and read them before they go out. When a decision changes, ask the agent to bring the action items in line.",
            "caption": "Exported with <code>marsdawn export meeting-notes.md</code>. The free command-line tool renders like MarsDawn's preview.",
            "prompt": "Write up this meeting in meeting-notes.md, using the template at {url}. Decisions first, one line each; every action item gets one owner and a date. When it's written, run marsdawn open meeting-notes.md.",
            "share": "<code>marsdawn export meeting-notes.md</code> writes a PDF you can attach to the follow-up mail.",
            "doesnt": "MarsDawn doesn't record or transcribe the meeting, and it doesn't track the action items. It shows the notes as they'll be read.",
            "faq": [("Do the checkboxes work?", "They show as checkboxes in the preview and the PDF. Tick one by changing <code>[ ]</code> to <code>[x]</code> in the source."),
                    ("Can the agent keep the notes and the action items in step?", "Yes, that's the point of the loop: change one, and ask it to update the rest. MarsDawn shows you the result.")],
        },
    },
    "zh-hant": {
        "spec": {
            "title": "Markdown 規格文件（PRD）範本 · MarsDawn",
            "description": "Markdown 規格文件範本，含需求、Mermaid 流程圖和驗收條件。agent 來填，你在 MarsDawn 裡審閱。",
            "h1": "Markdown 規格文件（PRD）範本",
            "lede": "一份 agent 能填、你一次就能讀完的規格文件：問題、目標、需求、流程圖和驗收條件。改了一條需求，就請 agent 把其他部分跟著改好。",
            "caption": "用 <code>marsdawn export spec.md</code> 輸出。免費的命令列工具排版和 MarsDawn 的預覽一樣，圖表也一起畫出來。",
            "prompt": "用 {url} 這份範本，把［功能］的規格寫進 spec.md。每條需求都要有編號，流程圖和驗收條件用同樣的編號。寫好之後執行 marsdawn open spec.md。",
            "share": "<code>marsdawn export spec.md</code> 會在旁邊寫出 spec.pdf，給不讀 Markdown 的人。",
            "doesnt": "MarsDawn 會顯示規格、表格和流程圖，但不會檢查驗收條件有沒有涵蓋每一條需求。那是 agent 的工作，也要靠你讀。",
            "faq": [("流程圖需要另外安裝什麼嗎？", "不用。MarsDawn 和 <code>marsdawn export</code> 自己就會畫 Mermaid，離線也能畫。"),
                    ("可以在 MarsDawn 裡改規格嗎？", "可以。它是 Markdown 編輯器，原始碼旁邊就是預覽。agent 下次讀這個檔案時，就會看到你的修改。")],
        },
        "flowchart": {
            "title": "Markdown 流程圖範本（Mermaid）· MarsDawn",
            "description": "Markdown 的 Mermaid 流程圖範本，圖的下方把步驟寫出來。在 Mac 上預覽，也能輸出成 PDF。",
            "h1": "Markdown 流程圖範本",
            "lede": "一張 Mermaid 流程圖，下方把每個步驟寫清楚，圖和文字可以互相對照。拿掉一個步驟，再請 agent 把其他部分改好。",
            "caption": "用 <code>marsdawn export flowchart.md</code> 輸出。免費的命令列工具排版和 MarsDawn 的預覽一樣，圖表也一起畫出來。",
            "prompt": "用 {url} 這份範本，把［流程］畫進 flowchart.md。每個節點對應一個編號步驟，順序相同。寫好之後執行 marsdawn open flowchart.md。",
            "share": "<code>marsdawn export flowchart.md</code>：流程圖會畫進 PDF 裡。",
            "doesnt": "MarsDawn 照 Mermaid 寫的內容畫圖，不能手動排版，也不會讓編號步驟和節點保持一致。Mermaid 有錯的話，預覽會顯示錯誤訊息，而不是圖。",
            "faq": [("哪些圖可以用？", "Mermaid 畫得出來的都可以：流程圖、循序圖、狀態圖等等。"),
                    ("為什麼還要把步驟寫出來？", "快速瀏覽的人看圖；要仔細確認的人需要文字。agent 可以讓兩者保持一致。")],
        },
        "meeting-notes": {
            "title": "Markdown 會議記錄範本 · MarsDawn",
            "description": "Markdown 會議記錄範本，列出決議和行動項目，每項都有負責人。agent 來寫，你在 MarsDawn 裡確認。",
            "h1": "Markdown 會議記錄範本",
            "lede": "先寫決議，再列行動項目，每項都有負責人。讓 agent 從逐字稿整理出會議記錄，寄出之前先讀一遍。決議改了，就請 agent 把行動項目跟著改好。",
            "caption": "用 <code>marsdawn export meeting-notes.md</code> 輸出。免費的命令列工具排版和 MarsDawn 的預覽一樣。",
            "prompt": "用 {url} 這份範本，把這場會議整理進 meeting-notes.md。先寫決議，一項一行；每個行動項目都要有一位負責人和日期。寫好之後執行 marsdawn open meeting-notes.md。",
            "share": "<code>marsdawn export meeting-notes.md</code> 會輸出一份 PDF，可以附在會後的信裡。",
            "doesnt": "MarsDawn 不會錄音或轉逐字稿，也不會追蹤行動項目。它只把會議記錄呈現成讀者會看到的樣子。",
            "faq": [("勾選框能用嗎？", "在預覽和 PDF 裡都會顯示成勾選框。要打勾，就在原始碼裡把 <code>[ ]</code> 改成 <code>[x]</code>。"),
                    ("agent 能讓會議記錄和行動項目保持一致嗎？", "可以，這就是這個循環的用意：改其中一個，再請它更新其他部分。MarsDawn 讓你看到結果。")],
        },
    },
    "zh-hans": {
        "spec": {
            "title": "Markdown 规格文档（PRD）模板 · MarsDawn",
            "description": "Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。",
            "h1": "Markdown 规格文档（PRD）模板",
            "lede": "一份 agent 能填、你一次就能读完的规格文档：问题、目标、需求、流程图和验收标准。改了一条需求，就请 agent 把其他部分跟着改好。",
            "caption": "用 <code>marsdawn export spec.md</code> 输出。免费的命令行工具排版和 MarsDawn 的预览一样，图表也一起画出来。",
            "prompt": "用 {url} 这份模板，把［功能］的规格写进 spec.md。每条需求都要有编号，流程图和验收标准用同样的编号。写好之后运行 marsdawn open spec.md。",
            "share": "<code>marsdawn export spec.md</code> 会在旁边写出 spec.pdf，给不读 Markdown 的人。",
            "doesnt": "MarsDawn 会显示规格、表格和流程图，但不会检查验收标准有没有覆盖每一条需求。那是 agent 的工作，也要靠你读。",
            "faq": [("流程图需要另外安装什么吗？", "不用。MarsDawn 和 <code>marsdawn export</code> 自己就会画 Mermaid，离线也能画。"),
                    ("可以在 MarsDawn 里改规格吗？", "可以。它是 Markdown 编辑器，源代码旁边就是预览。agent 下次读这个文件时，就会看到你的修改。")],
        },
        "flowchart": {
            "title": "Markdown 流程图模板（Mermaid）· MarsDawn",
            "description": "Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能输出成 PDF。",
            "h1": "Markdown 流程图模板",
            "lede": "一张 Mermaid 流程图，下方把每个步骤写清楚，图和文字可以互相对照。去掉一个步骤，再请 agent 把其他部分改好。",
            "caption": "用 <code>marsdawn export flowchart.md</code> 输出。免费的命令行工具排版和 MarsDawn 的预览一样，图表也一起画出来。",
            "prompt": "用 {url} 这份模板，把［流程］画进 flowchart.md。每个节点对应一个编号步骤，顺序相同。写好之后运行 marsdawn open flowchart.md。",
            "share": "<code>marsdawn export flowchart.md</code>：流程图会画进 PDF 里。",
            "doesnt": "MarsDawn 按 Mermaid 写的内容画图，不能手动排版，也不会让编号步骤和节点保持一致。Mermaid 有错误时，预览会显示错误信息，而不是图。",
            "faq": [("哪些图可以用？", "Mermaid 画得出来的都可以：流程图、时序图、状态图等等。"),
                    ("为什么还要把步骤写出来？", "快速浏览的人看图；要仔细确认的人需要文字。agent 可以让两者保持一致。")],
        },
        "meeting-notes": {
            "title": "Markdown 会议记录模板 · MarsDawn",
            "description": "Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。",
            "h1": "Markdown 会议记录模板",
            "lede": "先写决议，再列行动项，每项都有负责人。让 agent 从逐字稿整理出会议记录，发出之前先读一遍。决议改了，就请 agent 把行动项跟着改好。",
            "caption": "用 <code>marsdawn export meeting-notes.md</code> 输出。免费的命令行工具排版和 MarsDawn 的预览一样。",
            "prompt": "用 {url} 这份模板，把这场会议整理进 meeting-notes.md。先写决议，一项一行；每个行动项都要有一位负责人和日期。写好之后运行 marsdawn open meeting-notes.md。",
            "share": "<code>marsdawn export meeting-notes.md</code> 会输出一份 PDF，可以附在会后的邮件里。",
            "doesnt": "MarsDawn 不会录音或转写，也不会跟踪行动项。它只把会议记录呈现成读者会看到的样子。",
            "faq": [("复选框能用吗？", "在预览和 PDF 里都会显示成复选框。要打勾，就在源代码里把 <code>[ ]</code> 改成 <code>[x]</code>。"),
                    ("agent 能让会议记录和行动项保持一致吗？", "可以，这就是这个循环的用意：改其中一个，再请它更新其他部分。MarsDawn 让你看到结果。")],
        },
    },
    "ja": {
        "spec": {
            "title": "Markdown 仕様書（PRD）テンプレート · MarsDawn",
            "description": "要件、Mermaid のフロー図、受け入れ基準を含む Markdown の仕様書テンプレート。エージェントが埋め、あなたが MarsDawn で確認します。",
            "h1": "Markdown 仕様書（PRD）テンプレート",
            "lede": "エージェントが埋められて、あなたが一度で読み通せる仕様書。課題、目標、要件、フロー図、受け入れ基準。要件をひとつ変えたら、残りを合わせるようエージェントに頼みます。",
            "caption": "<code>marsdawn export spec.md</code> で書き出したもの。無料のコマンドラインツールは MarsDawn のプレビューと同じ見た目で、図もそのまま描きます。",
            "prompt": "{url} のテンプレートを使って、［機能］の仕様を spec.md に書いてください。要件にはすべて ID を付け、フローと受け入れ基準でも同じ ID を使ってください。書き終えたら marsdawn open spec.md を実行してください。",
            "share": "<code>marsdawn export spec.md</code> を実行すると、隣に spec.pdf ができます。Markdown を読まない人に渡せます。",
            "doesnt": "MarsDawn は仕様、表、図を表示します。受け入れ基準がすべての要件を網羅しているかは確かめません。それはエージェントの仕事で、あなたが読んで確かめることです。",
            "faq": [("フロー図のために何かインストールが必要ですか？", "いいえ。MarsDawn と <code>marsdawn export</code> は Mermaid を自分で描きます。オフラインでも描けます。"),
                    ("MarsDawn で仕様を編集できますか？", "はい。ソースの隣にプレビューがある Markdown エディタです。エージェントは次にファイルを読むときに、あなたの編集を目にします。")],
        },
        "flowchart": {
            "title": "Markdown フローチャートテンプレート（Mermaid）· MarsDawn",
            "description": "Markdown で書く Mermaid フローチャートのテンプレート。図の下に各ステップを書き出します。Mac でプレビューし、PDF に書き出せます。",
            "h1": "Markdown フローチャートテンプレート",
            "lede": "Mermaid のフローチャートと、その下に書き出した各ステップ。図と文章を突き合わせて確かめられます。ステップをひとつ外したら、残りの修正をエージェントに頼みます。",
            "caption": "<code>marsdawn export flowchart.md</code> で書き出したもの。無料のコマンドラインツールは MarsDawn のプレビューと同じ見た目で、図もそのまま描きます。",
            "prompt": "{url} のテンプレートを使って、［プロセス］のフローを flowchart.md に描いてください。ノードごとに番号付きのステップをひとつ、同じ順番で書いてください。書き終えたら marsdawn open flowchart.md を実行してください。",
            "share": "<code>marsdawn export flowchart.md</code>：図は PDF に描き込まれます。",
            "doesnt": "MarsDawn は Mermaid に書かれたとおりに図を描きます。手でレイアウトすることはできず、番号付きのステップとノードをそろえることもしません。Mermaid に誤りがあると、プレビューには図の代わりにエラーが表示されます。",
            "faq": [("どの図が使えますか？", "Mermaid で描けるものなら何でも。フローチャート、シーケンス図、状態遷移図などです。"),
                    ("なぜステップも書き出すのですか？", "ざっと見る人は図を見て、確かめる人は文章を読みます。エージェントに両方をそろえてもらえます。")],
        },
        "meeting-notes": {
            "title": "Markdown 議事録テンプレート · MarsDawn",
            "description": "決定事項と、担当者付きのアクションアイテムをまとめる Markdown の議事録テンプレート。エージェントが書き、あなたが MarsDawn で確かめます。",
            "h1": "Markdown 議事録テンプレート",
            "lede": "まず決定事項、次にアクションアイテム。それぞれに担当者を付けます。文字起こしからエージェントに議事録を書かせ、送る前に読んでください。決定が変わったら、アクションアイテムを合わせるようエージェントに頼みます。",
            "caption": "<code>marsdawn export meeting-notes.md</code> で書き出したもの。無料のコマンドラインツールは MarsDawn のプレビューと同じ見た目です。",
            "prompt": "{url} のテンプレートを使って、この会議を meeting-notes.md にまとめてください。決定事項を先に、一行ずつ。アクションアイテムにはそれぞれ担当者と期日をひとつ付けてください。書き終えたら marsdawn open meeting-notes.md を実行してください。",
            "share": "<code>marsdawn export meeting-notes.md</code> で PDF ができます。会議後のメールに添付できます。",
            "doesnt": "MarsDawn は会議を録音も文字起こしもせず、アクションアイテムの管理もしません。読む人が目にするとおりに議事録を表示します。",
            "faq": [("チェックボックスは使えますか？", "プレビューでも PDF でもチェックボックスとして表示されます。チェックを入れるには、ソースの <code>[ ]</code> を <code>[x]</code> に変えます。"),
                    ("議事録とアクションアイテムをエージェントにそろえてもらえますか？", "はい。それがこのループの目的です。どちらかを変えて、残りの更新を頼みます。MarsDawn で結果を確かめられます。")],
        },
    },
}

FENCE = "```"

TEMPLATES = {
    "en": {
        "spec": f"""# Spec: Feature name

Status: draft · Owner: name · Updated: date

## Problem

_What is wrong today, for whom, and how we know._

## Goals

- _What will be true when this ships._

## Non-goals

- _What this deliberately doesn't do._

## Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| R1 | _Requirement_ | Must |
| R2 | _Requirement_ | Should |

## Flow

{FENCE}mermaid
flowchart LR
  A[Start] --> B[Step] --> C[Result]
{FENCE}

## Acceptance criteria

- [ ] R1: _How we check it._
- [ ] R2: _How we check it._

## Open questions

- _Question._
""",
        "flowchart": f"""# Flow name

_One sentence: what goes in, what comes out._

## Diagram

{FENCE}mermaid
flowchart LR
  A[First step] --> B[Second step]
  B --> C[Third step]
  C --> D[Done]
{FENCE}

## Steps

1. **First step:** _who does it, and what they hand on._
2. **Second step:** _…_
3. **Third step:** _…_
4. **Done:** _what "done" means here._
""",
        "meeting-notes": """# Meeting name, date

Attendees: _names_

## Decisions

- _What was decided, in one line each._

## Action items

- [ ] Name: _what, by when._
- [ ] Name: _what, by when._

## Notes

- _Anything worth keeping that isn't a decision or an action._
""",
    },
    "zh-hant": {
        "spec": f"""# 規格：功能名稱

狀態：草稿 · 負責人：姓名 · 更新：日期

## 問題

_現在哪裡有問題、影響誰、我們怎麼知道。_

## 目標

- _上線後會成立的事。_

## 不做的事

- _這次刻意不做的事。_

## 需求

| 編號 | 需求 | 優先度 |
|------|------|--------|
| R1 | _需求_ | 必要 |
| R2 | _需求_ | 應該 |

## 流程

{FENCE}mermaid
flowchart LR
  A[開始] --> B[步驟] --> C[結果]
{FENCE}

## 驗收條件

- [ ] R1：_怎麼確認。_
- [ ] R2：_怎麼確認。_

## 待決問題

- _問題。_
""",
        "flowchart": f"""# 流程名稱

_一句話：輸入什麼，產出什麼。_

## 圖

{FENCE}mermaid
flowchart LR
  A[第一步] --> B[第二步]
  B --> C[第三步]
  C --> D[完成]
{FENCE}

## 步驟

1. **第一步**：_誰來做，交給下一步什麼。_
2. **第二步**：_……_
3. **第三步**：_……_
4. **完成**：_這裡的「完成」是什麼意思。_
""",
        "meeting-notes": """# 會議名稱，日期

出席：_姓名_

## 決議

- _決定了什麼，一項一行。_

## 行動項目

- [ ] 姓名：_做什麼，何時完成。_
- [ ] 姓名：_做什麼，何時完成。_

## 備註

- _值得留下、但不是決議也不是行動項目的內容。_
""",
    },
    "zh-hans": {
        "spec": f"""# 规格：功能名称

状态：草稿 · 负责人：姓名 · 更新：日期

## 问题

_现在哪里有问题、影响谁、我们怎么知道。_

## 目标

- _上线后会成立的事。_

## 不做的事

- _这次刻意不做的事。_

## 需求

| 编号 | 需求 | 优先级 |
|------|------|--------|
| R1 | _需求_ | 必须 |
| R2 | _需求_ | 应该 |

## 流程

{FENCE}mermaid
flowchart LR
  A[开始] --> B[步骤] --> C[结果]
{FENCE}

## 验收标准

- [ ] R1：_怎么确认。_
- [ ] R2：_怎么确认。_

## 待定问题

- _问题。_
""",
        "flowchart": f"""# 流程名称

_一句话：输入什么，产出什么。_

## 图

{FENCE}mermaid
flowchart LR
  A[第一步] --> B[第二步]
  B --> C[第三步]
  C --> D[完成]
{FENCE}

## 步骤

1. **第一步**：_谁来做，交给下一步什么。_
2. **第二步**：_……_
3. **第三步**：_……_
4. **完成**：_这里的“完成”是什么意思。_
""",
        "meeting-notes": """# 会议名称，日期

出席：_姓名_

## 决议

- _决定了什么，一项一行。_

## 行动项

- [ ] 姓名：_做什么，何时完成。_
- [ ] 姓名：_做什么，何时完成。_

## 备注

- _值得留下、但不是决议也不是行动项的内容。_
""",
    },
    "ja": {
        "spec": f"""# 仕様：機能名

ステータス：下書き · 担当：名前 · 更新：日付

## 課題

_いま何が問題で、誰が困っていて、なぜそうとわかるか。_

## 目標

- _リリース後に成り立っていること。_

## やらないこと

- _今回あえてやらないこと。_

## 要件

| ID | 要件 | 優先度 |
|----|------|--------|
| R1 | _要件_ | 必須 |
| R2 | _要件_ | 推奨 |

## フロー

{FENCE}mermaid
flowchart LR
  A[開始] --> B[ステップ] --> C[結果]
{FENCE}

## 受け入れ基準

- [ ] R1：_どう確かめるか。_
- [ ] R2：_どう確かめるか。_

## 未決事項

- _問い。_
""",
        "flowchart": f"""# フロー名

_一文で：何が入り、何が出るか。_

## 図

{FENCE}mermaid
flowchart LR
  A[最初のステップ] --> B[次のステップ]
  B --> C[三つ目のステップ]
  C --> D[完了]
{FENCE}

## ステップ

1. **最初のステップ**：_誰がやり、次に何を渡すか。_
2. **次のステップ**：_……_
3. **三つ目のステップ**：_……_
4. **完了**：_ここでの「完了」の意味。_
""",
        "meeting-notes": """# 会議名、日付

出席者：_名前_

## 決定事項

- _決まったことを一行ずつ。_

## アクションアイテム

- [ ] 名前：_何を、いつまでに。_
- [ ] 名前：_何を、いつまでに。_

## メモ

- _決定でもアクションでもないが、残しておくこと。_
""",
    },
}


def _spec_scene(t: dict) -> dict:
    return {
        "file": "spec.md", "active": t["req"],
        "source": [("h1", t["title"]), ("h2", t["req"]), ("li", t["r1"]), ("li", t["r2"]), ("li", t["r3"], "u"),
                   ("h2", t["flow"]), ("code", FENCE + "mermaid"), ("code", "flowchart LR"),
                   ("code", f"  A[{t['n1']}] --> B[{t['n2']}]"), ("code", f"  B --> C[{t['n3']}]", "a"),
                   ("code", f"  {{b}} --> D[{t['n4']}]"), ("code", FENCE),
                   ("h2", t["acc"]), ("task", t["a1"]), ("task", t["a3"], "c")],
        "preview": [("h3", t["title"]), ("h4", t["req"]), ("li", t["r1"]), ("li", t["r2"]), ("li", t["r3"], "u"),
                    ("h4", t["flow"]), ("flow", [t["n1"], t["n2"], (t["n3"], "a"), t["n4"]]),
                    ("h4", t["acc"]), ("task", t["a1"]), ("task", t["a3"], "c")],
        "swaps": {"b": ("C", "B")},
        "ask": t["ask"], "reply": t["reply"], "alt": t["alt"],
    }


def _flow_scene(t: dict) -> dict:
    return {
        "file": "flowchart.md", "active": t["diagram"],
        "source": [("h1", t["title"]), ("h2", t["diagram"]), ("code", FENCE + "mermaid"), ("code", "flowchart LR"),
                   ("code", f"  A[{t['n1']}] --> B[{t['n2']}]"), ("code", f"  B --> C[{t['n3']}]", "u"),
                   ("code", f"  {{a}} --> D[{t['n4']}]"), ("code", FENCE),
                   ("h2", t["steps"]), ("text", t["s1"]), ("text", t["s2"]), ("text", t["s3"], "b"), ("text", t["s4"])],
        "preview": [("h3", t["title"]), ("h4", t["diagram"]), ("flow", [t["n1"], t["n2"], (t["n3"], "u"), t["n4"]]),
                    ("h4", t["steps"]), ("p", t["s1"]), ("p", t["s2"]), ("p", t["s3"], "b"), ("p", t["s4"])],
        "swaps": {"a": ("C", "B"), "c": ("4", "3")},
        "ask": t["ask"], "reply": t["reply"], "alt": t["alt"],
    }


def _meeting_scene(t: dict) -> dict:
    return {
        "file": "meeting-notes.md", "active": t["decisions"],
        "source": [("h1", t["title"]), ("h2", t["decisions"]), ("li", t["d1"]), ("li", t["d2"]),
                   ("h2", t["actions"]), ("task", t["t1"]), ("task", t["t2"]), ("task", t["t3"])],
        "preview": [("h3", t["title"]), ("h4", t["decisions"]), ("li", t["d1"]), ("li", t["d2"]),
                    ("h4", t["actions"]), ("task", t["t1"]), ("task", t["t2"]), ("task", t["t3"])],
        "swaps": {k: ("50", "80") for k in "uabc"},
        "ask": t["ask"], "reply": t["reply"], "alt": t["alt"],
    }


SCENE_TEXT = {
    "en": {
        "spec": {"title": "Spec: Sign-in codes", "req": "Requirements", "flow": "Flow", "acc": "Acceptance",
                 "r1": "R1: Email a six-digit code.", "r2": "R2: The code expires in 10 min.",
                 "r3": "R3: Ask for a second factor.", "n1": "Email", "n2": "Code", "n3": "Second factor",
                 "n4": "Signed in", "a1": "R1: A code arrives in a minute.", "a3": "R3: Asked once per device.",
                 "ask": "I dropped R3. Make the flow and the acceptance criteria agree.",
                 "reply": "Done. The flow skips the second factor, and R3's check is gone.",
                 "alt": "A terminal opens spec.md in MarsDawn. The reader deletes requirement R3, and the agent removes its step from the flow diagram and its acceptance check."},
        "flowchart": {"title": "Publishing flow", "diagram": "Diagram", "steps": "Steps",
                      "n1": "Draft", "n2": "Review", "n3": "Legal", "n4": "Publish",
                      "s1": "1. Draft: the writer's first go.", "s2": "2. Review: an editor reads it.",
                      "s3": "3. Legal: checks the claims.", "s4": "{c}. Publish: it goes live.",
                      "ask": "I took Legal out of the diagram. Fix the edge and the steps.",
                      "reply": "Done. Review goes straight to Publish, and the steps are renumbered.",
                      "alt": "A terminal opens flowchart.md in MarsDawn. The reader removes the Legal step from the Mermaid diagram, and the agent reconnects the diagram and renumbers the steps below it."},
        "meeting-notes": {"title": "Weekly sync, 5 Oct", "decisions": "Decisions", "actions": "Action items",
                          "d1": "Open the beta to {u} people.", "d2": "Ship it on Friday.",
                          "t1": "Mia: send {a} invites.", "t2": "Leo: add {b} seats.", "t3": "Ana: support {c} users.",
                          "ask": "The beta is 80 people now. Update the action items.",
                          "reply": "Done. All three action items say 80.",
                          "alt": "A terminal opens meeting-notes.md in MarsDawn. The reader changes a decision from 50 to 80 people, and the agent updates the three action items to match."},
    },
    "zh-hant": {
        "spec": {"title": "規格：驗證碼登入", "req": "需求", "flow": "流程", "acc": "驗收",
                 "r1": "R1：寄出六位數驗證碼。", "r2": "R2：驗證碼 10 分鐘後失效。",
                 "r3": "R3：要求第二道驗證。", "n1": "Email", "n2": "驗證碼", "n3": "第二道驗證",
                 "n4": "登入完成", "a1": "R1：一分鐘內收到驗證碼。", "a3": "R3：每台裝置只問一次。",
                 "ask": "我拿掉了 R3，請讓流程和驗收條件一致。",
                 "reply": "好了，流程跳過第二道驗證，R3 的驗收也拿掉了。",
                 "alt": "終端機用 MarsDawn 打開 spec.md。讀者刪掉需求 R3，agent 把它在流程圖裡的步驟和驗收條件一起拿掉。"},
        "flowchart": {"title": "發布流程", "diagram": "圖", "steps": "步驟",
                      "n1": "草稿", "n2": "審閱", "n3": "法務", "n4": "發布",
                      "s1": "1. 草稿：作者的第一版。", "s2": "2. 審閱：編輯讀一遍。",
                      "s3": "3. 法務：確認說法。", "s4": "{c}. 發布：正式上線。",
                      "ask": "我把法務從圖裡拿掉了，請把連線和步驟改好。",
                      "reply": "好了，審閱直接接到發布，步驟也重新編號了。",
                      "alt": "終端機用 MarsDawn 打開 flowchart.md。讀者從 Mermaid 圖裡拿掉法務這一步，agent 把圖重新接好，並替下方的步驟重新編號。"},
        "meeting-notes": {"title": "每週同步，10/5", "decisions": "決議", "actions": "行動項目",
                          "d1": "Beta 開放給 {u} 人。", "d2": "週五上線。",
                          "t1": "Mia：寄出 {a} 份邀請。", "t2": "Leo：加開 {b} 個席位。", "t3": "Ana：準備支援 {c} 人。",
                          "ask": "Beta 改成 80 人了，請更新行動項目。",
                          "reply": "好了，三個行動項目都改成 80。",
                          "alt": "終端機用 MarsDawn 打開 meeting-notes.md。讀者把一項決議從 50 人改成 80 人，agent 把三個行動項目都跟著改好。"},
    },
    "zh-hans": {
        "spec": {"title": "规格：验证码登录", "req": "需求", "flow": "流程", "acc": "验收",
                 "r1": "R1：发送六位数验证码。", "r2": "R2：验证码 10 分钟后失效。",
                 "r3": "R3：要求第二重验证。", "n1": "Email", "n2": "验证码", "n3": "第二重验证",
                 "n4": "登录完成", "a1": "R1：一分钟内收到验证码。", "a3": "R3：每台设备只问一次。",
                 "ask": "我去掉了 R3，请让流程和验收标准一致。",
                 "reply": "好了，流程跳过第二重验证，R3 的验收也去掉了。",
                 "alt": "终端用 MarsDawn 打开 spec.md。读者删掉需求 R3，agent 把它在流程图里的步骤和验收标准一起去掉。"},
        "flowchart": {"title": "发布流程", "diagram": "图", "steps": "步骤",
                      "n1": "草稿", "n2": "审阅", "n3": "法务", "n4": "发布",
                      "s1": "1. 草稿：作者的第一版。", "s2": "2. 审阅：编辑读一遍。",
                      "s3": "3. 法务：确认说法。", "s4": "{c}. 发布：正式上线。",
                      "ask": "我把法务从图里去掉了，请把连线和步骤改好。",
                      "reply": "好了，审阅直接接到发布，步骤也重新编号了。",
                      "alt": "终端用 MarsDawn 打开 flowchart.md。读者从 Mermaid 图里去掉法务这一步，agent 把图重新接好，并给下方的步骤重新编号。"},
        "meeting-notes": {"title": "每周同步，10/5", "decisions": "决议", "actions": "行动项",
                          "d1": "Beta 开放给 {u} 人。", "d2": "周五上线。",
                          "t1": "Mia：发出 {a} 份邀请。", "t2": "Leo：加开 {b} 个席位。", "t3": "Ana：准备支持 {c} 人。",
                          "ask": "Beta 改成 80 人了，请更新行动项。",
                          "reply": "好了，三个行动项都改成 80。",
                          "alt": "终端用 MarsDawn 打开 meeting-notes.md。读者把一项决议从 50 人改成 80 人，agent 把三个行动项都跟着改好。"},
    },
    "ja": {
        "spec": {"title": "仕様：コードでサインイン", "req": "要件", "flow": "フロー", "acc": "受け入れ",
                 "r1": "R1：6桁のコードをメールで送る。", "r2": "R2：コードは10分で失効。",
                 "r3": "R3：二要素目を求める。", "n1": "Email", "n2": "コード", "n3": "二要素目",
                 "n4": "サインイン完了", "a1": "R1：1分以内にコードが届く。", "a3": "R3：端末ごとに一度だけ。",
                 "ask": "R3 を外した。フローと受け入れ基準を合わせて。",
                 "reply": "完了。フローは二要素目を飛ばし、R3 の確認も消した。",
                 "alt": "ターミナルが MarsDawn で spec.md を開く。読み手が要件 R3 を消し、エージェントがフロー図のステップと受け入れ基準から R3 を取り除く。"},
        "flowchart": {"title": "公開フロー", "diagram": "図", "steps": "ステップ",
                      "n1": "下書き", "n2": "レビュー", "n3": "法務", "n4": "公開",
                      "s1": "1. 下書き：書き手の初稿。", "s2": "2. レビュー：編集者が読む。",
                      "s3": "3. 法務：表現を確認する。", "s4": "{c}. 公開：公開される。",
                      "ask": "図から法務を外した。つなぎ方とステップを直して。",
                      "reply": "完了。レビューから公開へ直接つなぎ、番号も振り直した。",
                      "alt": "ターミナルが MarsDawn で flowchart.md を開く。読み手が Mermaid の図から法務のステップを外し、エージェントが図をつなぎ直して、下のステップの番号を振り直す。"},
        "meeting-notes": {"title": "週次定例、10/5", "decisions": "決定事項", "actions": "アクションアイテム",
                          "d1": "ベータを {u} 人に公開する。", "d2": "金曜にリリース。",
                          "t1": "Mia：招待を {a} 通送る。", "t2": "Leo：席を {b} 追加。", "t3": "Ana：{c} 人分のサポート。",
                          "ask": "ベータは80人になった。アクションアイテムを更新して。",
                          "reply": "完了。3つのアクションアイテムをすべて80にした。",
                          "alt": "ターミナルが MarsDawn で meeting-notes.md を開く。読み手が決定事項を50人から80人に変え、エージェントが3つのアクションアイテムを合わせる。"},
    },
}

SCENE_BUILDERS = {"spec": _spec_scene, "flowchart": _flow_scene, "meeting-notes": _meeting_scene}


def scene(locale: str, case: str) -> dict:
    return {**SCENE_BUILDERS[case](SCENE_TEXT[locale][case]), "long": True}


def loop_html(locale: str, case: str) -> str:
    return loop_anim.scene_html(scene(locale, case), locale)


def page_url(locale: str, case: str = "") -> str:
    return LOCALE_ROOT[locale] + "templates/" + (f"{case}/" if case else "")


def download_url(locale: str, case: str) -> str:
    return page_url(locale, case) + FILES[case]


def _image(case: str, locale: str) -> tuple:
    """The rendered first page, and its pixel size from the PNG header."""
    name = f"{case}-{locale}.png"
    data = (IMAGE_DIR / name).read_bytes()[:24]
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"{name}: not a PNG (run tools/templates/render_images.sh)"
    width, height = struct.unpack(">II", data[16:24])
    return f"/assets/templates/{name}", width, height


def _page_body(locale: str, case: str) -> str:
    p, lab = PAGES[locale][case], LABELS[locale]
    file = FILES[case]
    src, width, height = _image(case, locale)
    faq = "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q, a in p["faq"])
    others = [c for c in CASES if c != case]
    more = "\n".join(f'  <li><a href="{page_url(locale, c)}">{HUB[locale]["items"][c][0]}</a>{lab["sep"]}{HUB[locale]["items"][c][1]}</li>'
                     for c in others)
    prompt = html.escape(p["prompt"].format(url=BASE_URL + download_url(locale, case)))
    return f"""
<section class="intro">
  <h1>{p["h1"]}</h1>
  <p>{p["lede"]}</p>
</section>

{LOOP_MARK.format(case=case)}

<h2>{lab["template"]}</h2>
<p><a href="{download_url(locale, case)}" download>{lab["download"].format(file=file)}</a></p>
<pre><code>{html.escape(TEMPLATES[locale][case])}</code></pre>

<h2>{lab["looks"]}</h2>
<p class="tpl-shot"><img src="{src}" width="{width}" height="{height}" loading="lazy" alt="{html.escape(lab["img_alt"].format(file=file))}"></p>
<p>{p["caption"]}</p>

<h2>{lab["ask"]}</h2>
<pre class="tpl-prompt"><code>{prompt}</code></pre>

<h2>{lab["share"]}</h2>
<p>{p["share"]}</p>

<h2>{lab["doesnt"]}</h2>
<p>{p["doesnt"]}</p>

<h2>{lab["faq"]}</h2>
{faq}

<h2>{lab["more"]}</h2>
<ul>
{more}
  <li><a href="{page_url(locale)}">{HUB[locale]["h1"]}</a></li>
</ul>
"""


def _hub_body(locale: str) -> str:
    h, lab = HUB[locale], LABELS[locale]
    items = "\n".join(f'  <li><a href="{page_url(locale, c)}">{h["items"][c][0]}</a>{lab["sep"]}{h["items"][c][1]}</li>'
                      for c in CASES)
    return f"""
<section class="intro">
  <h1>{h["h1"]}</h1>
  <p>{h["lede"]}</p>
</section>

<ul>
{items}
</ul>
"""


def pages() -> dict:
    """{(locale, slug): page} for the hub and every template page, in every locale."""
    out = {}
    for locale in LOCALE_ROOT:
        out[(locale, "templates")] = {"title": HUB[locale]["title"], "description": HUB[locale]["description"],
                                      "body": _hub_body(locale)}
        for case in CASES:
            p = PAGES[locale][case]
            out[(locale, f"templates/{case}")] = {"title": p["title"], "description": p["description"],
                                                  "body": _page_body(locale, case)}
    return out


def expand_loops(locale: str, html_text: str) -> str:
    """Put each page's loop where its mark is. Only the HTML page gets it; the Markdown twin keeps the
    mark out (html_to_markdown drops comments), so an agent reading the twin gets no drawing."""
    for case in CASES:
        mark = LOOP_MARK.format(case=case)
        if mark in html_text:
            html_text = html_text.replace(mark, loop_html(locale, case))
    return html_text


def downloads() -> dict:
    """{path under public/: text} for every template file."""
    return {download_url(locale, case).lstrip("/"): TEMPLATES[locale][case]
            for locale in LOCALE_ROOT for case in CASES}
