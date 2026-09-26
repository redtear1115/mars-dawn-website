# 五分钟审完一份 agent 计划

agent 写好一份计划，正等你点头。你手上只有五分钟，不是一个小时。下面这套做法用什么编辑器都行，连纯文字编辑器也可以。其中几步 MarsDawn 帮得上忙，我们会讲清楚是哪几步；最重要的那一步，它帮不上。

**不要从头读到尾。先看架构，再查一个宣称，找出做了就回不去的步骤，看图表和影响范围，最后写出 agent 看得懂、改得动的反馈。六个步骤，大约五分钟。**

## 为什么要在执行前审

Chip Huyen 解释为什么规划要和执行分开时，把代价讲得很白：“Without oversight, an agent can run those steps for hours, wasting time and money on API calls, before you realize that it’s not going anywhere.”（没有监督的话，agent 可能执行那些步骤好几个小时，在 API 呼叫上浪费时间和金钱，你才发现它根本没有进展。）我们补一句：计划是抓错最便宜的地方。在 `plan.md` 里改一行，只要一句话；等 agent 跑完再收拾，可能要花掉一个下午。

## 范例

你请 agent 把使用者头像搬到物件储存，而且旧链接不能坏。它交回来的是这份：

```
# 计划：把使用者头像搬到物件储存

## 目标
头像改由物件储存提供，不再放在 app 服务器上。

## 步骤
1. 加入储存用的 client 与设定。✅ 完成
2. 写一支脚本，把现有头像复制到 bucket。
3. 把模板里的头像网址换掉。
4. 从服务器删除 `public/avatars/`。
5. 执行复制脚本。

## 状态
所有测试都通过。
```

读起来很顺。照做的话，它也会在复制任何一张头像之前，先把全部头像删光。

## 六个步骤

**1. 先只看标题。**（大约一分钟）大纲和你要求的对得上吗？少一段，通常就是少做一件事。这份只有“目标”“步骤”“状态”。你要求旧链接不能坏，可是没有任何一段讲旧链接，也没有讲出问题时怎么退回去。这就是你的第一条意见。

在终端机跑 `grep -n '^#' plan.md`，就只会印出标题；大部分编辑器也有大纲预览。在 MarsDawn 里，侧边栏（“显示 ▸ 显示边栏”，⌃⌘S）的“大纲”标签页会列出所有标题，点一下就跳过去。

**2. 找出所有写着“完成”“通过”“已验证”的地方，挑一个自己查。**（大约一分钟）打开那个文件、跑那个测试、数一下笔数。Chip Huyen 描述过一种失败：“The agent is convinced that it’s accomplished a task when it hasn’t.”（Agent 深信自己已完成任务，但其实并没有。）她举的例子是：请 agent 把 50 个人分到 30 间饭店房间，它只排了 40 人，还坚称做完了。

```
grep -n -E '完成|通过|验证|✅' plan.md
```

在这份计划里，会找到“✅ 完成”和“所有测试都通过”。是哪些测试？有任何一个碰到头像吗？自己跑一次，或直接问。这一步 MarsDawn 没办法替你做，除了你，没有人能替你做。

**3. 找出做了就回不去的步骤。**（大约一分钟）删资料、数据库迁移、force push，还有任何会寄出、付款或发布的动作。这些要等你明确点头。Chip Huyen 从系统设计的角度讲过同一件事：“If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing or defer to humans to execute these operations.”（如果计划牵涉有风险的操作，例如更新数据库或合并代码变更，系统可以在执行前要求人类明确核准，或交给人类自己执行。）这份计划的第 4 步会删掉原始文件，而且排在第 5 步复制之前。

**4. 图表要看画出来的样子，逐一对照每个箭头和文字说的是不是同一回事。**流程图画着“复制 → 检查 → 删除”，步骤却不是这个顺序，这本身就是一个发现。这份计划没有图，今天可以跳过。有图的时候，请看画出来的图，不要看 Mermaid 原始码：很多编辑器都有预览，〈[在 Mac 上怎么看 Markdown 文件](/zh-hans/view-markdown-on-mac/)〉和〈[在别处看 Markdown，对比 MarsDawn](/zh-hans/vs/markdown-preview-tools/)〉整理了各种做法。在 MarsDawn 里，画好的图就在原始码旁边（⌘2）；图表写错时，预览会显示原始码、下方附上错误信息，这也值得单独写一条意见。

**5. 列出计划会动到的文件和系统，你没要求的部分，先问清楚。**（第 4、5 步合起来大约一分钟）这份会动到：储存设定、模板、服务器上的一个文件夹、一个 bucket。这个 bucket 谁读得到？你没说它要公开。如果你用 MarsDawn 打开 agent 工作的文件夹（“文件 ▸ 打开文件夹⋯”，⇧⌘O），它新写的文件大约一秒内就会出现在“文件”标签页，清单上方也会标出 git 分支或工作树，你就知道自己审的是哪一份检出。

**6. 反馈写成“位置、问题、改法”，一行只讲一个问题。**（最后一分钟）

```
plan.md:10：第 5 步还没复制，这里就先删了。先复制、核对数量，再删；删之前等我确认。
plan.md:14：是哪些测试？加一个切换后加载旧头像网址的测试。
plan.md:6：没有处理旧链接。加一步让旧链接继续能用，也写出怎么退回去。
```

有行号的编辑器都能做到。在 MarsDawn 里，“编辑 ▸ 拷贝引用”（⌥⌘C）会把目前位置拷贝成 `plan.md:10`，“拷贝给 AI”（⌃⌥⌘C）会在下面附上你选取的文字。

## 只有一分钟的话

就做第 2 步吧。以为自己已经做完的 agent，多半是在这一步被抓到的。

## 五分钟不够的时候

有时候你判断不了某一步对不对，因为它超出你熟悉的范围。Jess Ou 在 LangChain 2026 年介绍 agent 的文章里，用两句话讲完：“Do not outsource judgment you cannot evaluate. If you wouldn't recognize a correct answer, neither will the agent.”（无法评估的判断，就不要外包出去。如果你自己认不出正确答案，agent 也认不出来。）我们的看法是：判断不了，不是赶快核准的理由，而是该去找懂的人问一下的理由。

## MarsDawn 在这里做什么、不做什么

MarsDawn 里没有 AI 模型。它不会帮你找出这份计划的问题，第 2、3 步也不会替你做。它做的是让文件在你审的时候保持好读：第 1 步有大纲，第 4 步有画好的图，第 5 步有“文件”标签页，第 6 步有行号引用。你读到一半 agent 改了计划，MarsDawn 会重新加载，停在你原本读到的位置，前提是你自己没有未储存的修改。

计划定案、要给别人看的时候，〈[把 agent 写的东西交出去，不用教对方 Markdown](/zh-hans/sharing-exported-pdfs/)〉和〈[Markdown 转 PDF 工具](/zh-hans/markdown-to-pdf/)〉说明了怎么转成 PDF 交出去。

## 试试看

MarsDawn 即将在 Mac App Store 上架。免费的 `marsdawn` 命令行工具现在就能用：

```
brew install redtear1115/tap/marsdawn
```

它不需要 app 就能把 Markdown 导出成 PDF。

[命令行工具](/zh-hans/cli/) · 买之前先看：[MarsDawn 做不到的事](/zh-hans/limits/)

## 接下来

- agent 的产出为什么难读：[读懂 agent 交回来的 Markdown](/zh-hans/reading-agent-output/)。
- agent 为什么要把计划摊开：[Anthropic 说 agent 要透明，那摊开的东西谁来读？](/zh-hans/agent-transparency/)
- agent 交回来的不只有计划：[四种 agent 设计模式，各自会交给你什么文件](/zh-hans/agent-design-patterns/)。
- Chip Huyen 的 read-only／write action 分类，更深入的一篇：[Chip Huyen 的 read-only／write action 分类，核准前为什么要看它](/zh-hans/reading-notes/chip-huyen-agents/)
- Andrew Ng 自己怎么帮设计模式排序，更深入的一篇：[Andrew Ng 自己帮四种设计模式的可预测程度排序](/zh-hans/reading-notes/andrew-ng-design-patterns/)

## 资料来源

- Chip Huyen，〈Agents〉，2025 年 1 月 7 日：[https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou，〈What is an AI agent?〉，LangChain，2026 年 7 月 31 日：[https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 导出。即将在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，之后可以用即将在 Mac App Store 上架的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI agent 的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 学会安装 marsdawn、确认它能用、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂 agent 交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [agent 的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [agent 设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [编者的阅读笔记](https://marsdawn.southern-light.dev/zh-hans/reading-notes/index.md): 六篇短笔记，谈打造 AI agent 的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读 agent 交回来的东西”的人分别意味着什么。
- [阅读笔记：Anthropic](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和 agent 分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [阅读笔记：Chip Huyen](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把 agent 的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM agent 描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给 agent 写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给 agent 的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。agent 来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。agent 来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
