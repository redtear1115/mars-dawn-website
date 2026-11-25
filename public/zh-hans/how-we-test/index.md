# 在一台 Mac 上通过的测试，不一定在测你以为的东西。

黑色星期五特价：一次解锁只要半价 USD 2.49（原价 USD 4.99），优惠到 11 月 30 日，12 月 1 日起恢复 USD 4.99。 <!-- sale-line -->

vibe coding 不是坏事，MarsDawn 也是用代理开发的。但让人长期依赖的软件，看的是第一版之后的事：多年的维护和安全，而这要从确认改动没有改坏东西开始。

**同一个测试，在 Mac mini 上通过，在 MacBook Air 上失败。产品没坏。是测试通过屏幕的颜色描述文件在读颜色，它在 Mac mini 上通过只是运气好。换一台机器，抓到的是测试的 bug，不是代码的 bug。**

只想知道 MarsDawn 会拿哪些极端或恶意的文件来测试？可以直接跳到“[我们丢给它的东西](#inputs)”。

## 只在 MacBook Air 上失败的测试

导出引擎的测试，在 GitHub 的 macOS 15 机器上完整跑一次将近一小时：debug 版约 32 分钟，release 版约 25 分钟。为了缩短时间，我们试着把 macOS 26 那一半移到自己的 MacBook Air 上跑（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)）。

在那台机器上第一次跑，就有一个测试失败。这个测试会导出一份带提示框（Note、Tip、Warning）的 PDF，检查每个提示框边上的色条颜色对不对，也就是色差要小于 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。换到 Mac mini，同一个 commit、同样的 macOS 和 Xcode，测试通过。

我们第一个怀疑是导出坏了。结果不是：PDF 本身没问题，两台机器不一样的，是测试读它的方式。

这个测试会把 PDF 每一页画成图像再读像素，而 macOS 画这张图时，用的是主显示器的色彩空间。Mac mini 接的是普通的外接显示器，MacBook Air 用的是内建显示屏。我们拿一张填满同一种橙色的图像读回来：(0.784, 0.278, 0.106) 在 Mac mini 上读成 (0.822, 0.335, 0.179)，在 MacBook Air 上读成 (0.782, 0.395, 0.221)。

关键在这里：在 Mac mini 上，测试读到的颜色其实也不对，最多差了 0.128，只是刚好落在 0.16 的上限内。它能通过，靠的是那台显示器，而不是真的量对了色条。

修复（[kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)）只改测试：把页面画进一张固定使用 sRGB 色彩空间的图像，完全不经过屏幕。现在两台机器都能准确读出色条的颜色：无论是 MacBook Air 的内建显示屏还是 Mac mini，色差都是 0.0。这个 pull request 的 CI 全部通过（[run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)），修复并入 MacBook Air 测试分支后，那台机器上的完整测试也全部通过（[run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)）。接着我们故意让它失败：把每个预期颜色都改成蓝色，五个提示框全部变红。

它还有一个已知的漏洞：Note 和 Caution 用的两种橙色只差约 0.119，在 0.16 的上限内，所以这两个颜色如果对调，测试多半发现不了。我们把这件事记了下来，没有假装这个测试已经完整。

一个不会失败的测试，什么也保护不了；因为错误的理由而失败的测试（比如屏幕的颜色描述文件）也一样。一台机器上的绿灯，只说明测试在那台机器上通过，不说明它测的就是名字上写的那件事。

## 测试是一层一层的网

没有哪个测试能抓到所有问题。每一层都是一张网眼不同的网，从这一层漏掉的错，应该被下一层接住：

- **参考 PDF：**导出引擎（开源的 [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)，`marsdawn` 命令也用它）把一组样本文稿导出成 PDF，每一页的文字都和事先记录的版本比对。抓内容悄悄丢失，或页数突然改变。
- **不同的系统和版本：**引擎在 macOS 15（支持的最低版本）和 macOS 26（App 实际发布的版本）上都要跑，各跑 debug 和 release 两种版本。App 的完整测试则跑四种组合：签名与不签名，各自再分付费墙开与关。抓只在旧系统上出错，或只在用户实际拿到的版本里出错的问题。
- **真实硬件：**App 的 CI 跑在我们自己的 Mac 上（Mac mini 和 MacBook Air 两台都跑）；把引擎的测试搬到那台 MacBook Air 试跑（[kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)，目前仍是实验草稿），就是抓到上面那个颜色描述文件问题的契机。换一台机器，能抓到只因为跑在某台机器上才通过的测试。
- **红灯对照组：**App 的 CI 固定放着 22 份故意弄坏的清理脚本和 20 份故意弄坏的测试执行脚本，每份都去掉一道安全检查，测试碰到每一份都必须失败。清理脚本会删除 Mac 上旧的构建和工作副本，少一道检查就可能删错东西。只要有一份弄坏的通过，坏掉的就是测试本身。
- **另一双眼睛：**我们的做法是合并前把改动交给另一个代理验证，像 kit #242 那样；涉及使用流程的改动，会先做情境审查。抓“说做完了其实没做完”，以及代码能跑、却用错了场合。
- **最后由人合并。**每个改动都由 MarsDawn 的开发者本人审过、亲手合并；代理和 bot 都不会合并。

## 我们丢给它的东西

网好不好，要看丢进去的是什么。下面是引擎测试会喂给它的几种输入，以及每个测试确保会发生的事：

- **超大的文件。**在我们的测试机上、以 release 版来测：2 MB 的文稿在一秒半内显示完；5 MB、复杂到排不了版的文稿照样能打开，一秒内以纯文本显示。超过 16 MB 的文件完全不解析，直接以文本显示。
- **几十万行。**大约 3 MB、每行只有一个词的文稿，将近 80 万行，读到一半就会被判定太多：引擎在那里停下来，改以纯文本显示。
- **永远不闭合的标记。**1 MB 只开不关的区块标记，或叠了几万层的区块，花的时间不能超过同样 1 MB 纯文本的两倍左右；超过八层的部分不再往下嵌套。
- **数学公式。**写错的公式就在原处显示错误，不会让整页坏掉。超过一万个字符的公式保留原样；一份文稿一次最多渲染前 1,000 个；公式里的内容也不会变成链接、图像或网页标签。
- **藏在 Markdown 里的恶意 HTML。**脚本会被移除，绝不执行；嵌入的框架在页面显示前就被拿掉。远程图像默认不加载，即使你允许，也只加载安全连接（HTTPS）的图像。另有一份去掉脚本过滤的对照版本，测试碰到它必须失败。
- **恶意的主题文件。**会被拒绝，错误信息也不会重复文件里隐藏的控制字符或链接。超过 16 KB 的主题文件直接不读。

这些都有代价。引擎单次运行的时间上限从 30 分钟拉到 45、50、70，现在已经拉到 90 分钟；macOS 15 曾在测试全部通过的情况下两次撞上 50 分钟上限，后来又在最后一步撞上 70 分钟，前面所有步骤都已经通过。

## 你也能照做的四个习惯

1. **写的代理和验的代理分开。**只给验证的那个改动本身和“怎样才算完成”，不要附上写代码那个代理的解释，请它自己跑测试，并列出没验到的地方。验 kit #242 时，验证的代理先在 MacBook Air 上跑旧测试、亲眼看它失败，才让新测试过关。代价是多一个会话的 token。
2. **每个测试都要看它失败一次。**只有见过同一个测试在它检查的东西真的出错时亮红灯，绿灯才有意义。所以相信绿灯之前，先把它守着的东西弄坏（或请代理弄坏），看它变红；再改回来，看它变绿。代理很会写出能通过的测试，正因为这样，你才需要看到它失败。
3. **测试至少在第二个环境跑一次。**没有第二台 Mac 也没关系，CI 里跑两个系统版本，或 debug 和 release 各跑一次，就是不错的起点。要找的是那些靠运气才通过的测试。
4. **“一个测试都没跑”要算失败。**Python 3.9 的 `unittest` 一个测试都没找到时，还是会报告成功，所以路径打错一个字，你照样拿到绿灯。我们的 CI 会读测试数量，是 0 就失败，也会检查摘要写的是“0 failed”，不只看退出码。这道检查，是一次独立验证在我们自己的 CI 里抓到这个漏洞之后才加上的。

## 一句话

一个 App 是不是 vibe coding 做的，没那么重要；重要的是有没有人持续在测试、在维护。选软件的时候值得看一眼：它有没有说明自己怎么测试？最近一次更新是什么时候？

速度交给代理，把关留给真正量对东西的测试，以及读过结果的人。

## 接下来

- 为什么代理写的东西还是要有人读过：[为什么 AI 写的东西还是需要人读过](/zh-hans/reviewing-ai-output/)。
- 怎么读代理交回来的计划和报告：[读懂代理交回来的 Markdown](/zh-hans/reading-agent-output/)。

## 资料来源

- 失败的测试和原因：[mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241)。
- 修复和独立验证：[mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)。
- 在 MacBook Air 试跑 CI（实验草稿），附运行时间：[mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)。
- 导出引擎的 CI，时间上限的调整历史写在注释里：[ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml)。
- App 的代码仓库不公开；上面关于 App 的内容，来自它的 CI 配置和测试脚本。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 检查代理写的 Markdown、JSON、YAML：Mac 原生 app，实时预览、Mermaid、KaTeX、快速查看、PDF。免费试用，之后一次 USD 2.49。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown、JSON、YAML 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可拿去开会或存档。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 2.49 解锁一次就好。没有订阅，也不需要账户。
- [打印与 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上先预览，再把 Markdown 打印或存储为 PDF；有文稿、手册、讲义三种布局，Mermaid 图表和代码高亮都会保留。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、iPhone 和 iPad 上不能编辑、没有插件、不需要账户；可以换主题，但不能自定义 CSS。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [Mac 上怎么打开 md 文件](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [在 Mac 上预览 Mermaid](https://marsdawn.southern-light.dev/zh-hans/mermaid-preview-mac/index.md): 在 Mac 上预览 Mermaid 图表：源代码旁边实时画出来，快速查看和导出 PDF 也看得到。图表写错时，会显示错误信息和出错的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [拷贝给 AI](https://marsdawn.southern-light.dev/zh-hans/copy-for-ai/index.md): 选中文本，连同文件路径和行号一起拷贝，粘贴到 Claude Code 或任何代理。在 Mac 上就能做，不用打开 IDE，也不用装插件。
- [从 HackMD 搬到 Mac](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MarsDawn 对比：VS Code 预览、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日（MarsDawn 的 PDF 格子更新于 2026 年 11 月 7 日）；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 2.49 解锁一次。逐项比较，附来源。
- [2026 Mac Markdown 查看器推荐](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM 代理把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI 代理的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI 代理与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给代理的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的代理把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个代理写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回代理的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [主题](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 内置四种预览主题，各有浅色与深色；在 Mac 版 MarsDawn 的设置里打开主题图库，还能安装更多。快速查看也会用你选的主题。
- [打造一个主题](https://marsdawn.southern-light.dev/zh-hans/themes/new/index.md): 挑选颜色和几个样式选项，实时看它们套用在范例文档上，再把主题送出成一个 GitHub issue。不用安装，也不用 git。
- [和代理一起做主题](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [主题图库](https://marsdawn.southern-light.dev/zh-hans/themes/gallery/index.md): 浏览 MarsDawn 的预览主题，每一个都经过开发者审核；可以按场景筛选，也可以举报有问题的主题。在浏览器里打造自己的主题，不用安装，也不用 git。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把代理写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂代理交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI 代理把工作成果交成 Markdown：计划、规格、进度报告。做代理的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [代理的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造代理的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [审代理计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): 代理交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [代理设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种代理设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [路线图](https://marsdawn.southern-light.dev/zh-hans/roadmap/index.md): MarsDawn 在 Mac、iPhone 与 iPad 上正在做和接下来要做的功能，按版本列出。不写日期，未排期的项目另行标明。
- [编者的阅读笔记](https://marsdawn.southern-light.dev/zh-hans/reading-notes/index.md): 六篇短笔记，谈打造 AI 代理的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读代理交回来的东西”的人分别意味着什么。
- [阅读笔记：Anthropic](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和代理分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [阅读笔记：Chip Huyen](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把代理的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM 代理描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对代理的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测代理的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给代理写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给代理的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。代理来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。代理来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
