# 给 AI agent 的 marsdawn 参考

给调用 `marsdawn` 命令行工具的 AI agent 与脚本参考。本页每个范例都用目前源代码构建的工具实际运行过。

**要把 Markdown 文件转成 PDF，运行 `marsdawn export notes.md --json`，再从 stdout 读取一个 JSON 对象。**Mermaid 图表与代码高亮的呈现方式和 MarsDawn app 相同。`export` 不需要 app，`open` 需要。

## 能做什么

- `export`：用和 MarsDawn app 相同的导出程序，把一个 Markdown 文件输出成分页的 PDF，不会打开任何窗口。
- `open`：在 MarsDawn app 中打开一或多个 Markdown 文件，让人审阅，也可以指定每个文件要定位的行。

## 不做什么

- 不从 stdin 读取 Markdown，请传入文件路径。
- 不把 PDF 写到 stdout。PDF 一律写成文件，stdout 只输出结果。
- 文件已存在时不会覆盖，除非加上 `--force`。
- 不加载网络图片，除非加上 `--allow-remote-images`，而且只走 https。
- 没有安装 MarsDawn 时，`open` 无法使用，会以代码 3 结束。`export` 不需要 app。App 已在 [Mac App Store](https://apps.apple.com/app/id6812925073) 上架。
- 只能在 macOS 上运行。

## export

```
marsdawn export notes.md --json
```

在 `notes.md` 旁写出 `notes.pdf`。选项：

- `-o, --output <path>`：PDF 的写入位置。默认为输入文件路径，扩展名换成 `.pdf`。
- `--theme <dawn|classic|modern|vivid>`：使用主题的浅色调色板。默认为 `$MARSDAWN_THEME`，其次是 `dawn`。
- `--paper <a4|letter>`：纸张大小。默认为 `a4`。
- `--allow-remote-images`：渲染时加载网络上的 https 图片。
- `--force`：输出文件已存在时覆盖。
- `--json`：在 stdout 输出一个 JSON 对象，而不是文本。

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

成功，退出代码 0：

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`：写出的 PDF 的绝对路径。
- `pages`：页数。
- `theme` 与 `paper`：实际使用的值。
- `diagramErrors`：每个渲染失败的 Mermaid 图表各一则消息。PDF 仍会写出。

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open notes.md --background --json
```

- `path:line` 指定要定位的行。后面再接列号，例如 `notes.md:120:8`，会被忽略。如果参数本身就是一个存在的文件名，就一律当成那个文件，所以名为 `weird:12` 的文件会照原名打开。
- `--line <n>` 为单一文件指定行号，包括文件名本身以冒号加数字结尾的情况。只能搭配一个文件。
- 行号范围是 1 到 999999999，超出范围是用法错误。
- 行号从 marsdawn 0.3.0 开始提供。
- `--background` 打开时不把 MarsDawn 带到最前面，适合在用户做别的事时打开文件的 agent。两种情况的 JSON 都一样。
- `--background` 从 marsdawn 0.5.1 开始提供。

成功，退出代码 0：

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`：每个文件一个对象，顺序与传入时相同。`path` 是文件的绝对路径；只有指定了行号时才有 `line`。
- `app`：打开它们的 MarsDawn app 路径。

marsdawn 0.2.x 的 `opened` 是路径字符串的清单。如果需要同时处理两种格式，请先查看 `marsdawn --version`。

## 在 Claude Code 编辑时打开文件

一个需要自行启用的 [Claude Code hook](https://code.claude.com/docs/en/hooks)：Claude 写入或编辑 Markdown 文件之后，在后台用 MarsDawn 打开那个文件，每个 session 每个文件只打开一次。除非你添加它，否则不会启用，而且要一个项目一个项目地添加，因为你没要求就弹出来的窗口会打断注意力。它运行的是 shell 命令，不花模型 token。

需要 marsdawn 0.5.1 或更新版本，才有 `--background`，以及 MarsDawn app。

把下面的内容保存为项目里的 `.claude/hooks/marsdawn-open.sh`，再用 `chmod +x` 让它可以执行：

```
#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2>/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2>/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || { [ -x /opt/homebrew/bin/marsdawn ] && echo /opt/homebrew/bin/marsdawn; }) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${TMPDIR:-/tmp}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2>/dev/null && exit 0
echo "$file" >> "$seen"

"$marsdawn" open --background "$file" >/dev/null 2>&1 || true
exit 0
```

然后把 hook 加到项目的 `.claude/settings.json`；如果只想自己用，改加到 `.claude/settings.local.json`：

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/marsdawn-open.sh" }
        ]
      }
    ]
  }
}
```

- 它在 Claude 的 Write 和 Edit 工具之后运行。扩展名不是 `.md` 或 `.markdown` 的文件不会处理。
- 在同一个 Claude Code session 里，每个文件只打开一次，不管 Claude 编辑几次。清单保存在 `$TMPDIR/marsdawn-hook/`，每个 session 一个文件，所以开新的 session 会再打开一次。
- `--background` 让 MarsDawn 不会跳到最前面：你正在用的窗口会保持焦点。
- 它不会妨碍 Claude。每条路径都以 0 退出；如果没有安装 marsdawn 或 MarsDawn app，就什么都不做。
- 它用 `/usr/bin/jq` 读取 hook 的输入。macOS 26 自带这个工具，而 MarsDawn app 也需要 macOS 26。
- 要关掉，从设置文件里删除这一项即可。

## 失败

加上 `--json` 时，失败会在 stdout 输出一个 JSON 对象，并以对应的代码结束：

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`，`input_not_found`：输入文件不存在、是文件夹，或不是 UTF-8 文本。
- `3`，`app_not_installed`：没有安装 MarsDawn。只有 `open` 会返回这个代码。
- `4`，`output_exists`：输出文件已存在，请加上 `--force`。
- `5`，`export_failed`：导出本身失败。
- `6`，`app_cannot_open_folders`：这个版本的 MarsDawn 还不能显示文件夹，所以没有打开任何东西。只有 `open` 会返回这个代码。
- `64`：用法错误，例如未知的选项、无效的值、行号超出范围，或 `--line` 搭配了多个文件。这种错误一律以文本输出到 stderr，即使加了 `--json` 也一样。

## JSON Schema

每种 `--json` 结果的 JSON Schema（draft 2020-12）：

- [export.v1.json](/schemas/cli/export.v1.json): export 成功
- [open.v3.json](/schemas/cli/open.v3.json): open 成功，marsdawn 0.5.1 以后
- [error.v2.json](/schemas/cli/error.v2.json): 两个命令的失败结果，marsdawn 0.5.2 以后
- [open.v2.json](/schemas/cli/open.v2.json): open 成功，marsdawn 0.3.0 到 0.5.0
- [open.v1.json](/schemas/cli/open.v1.json): open 成功，marsdawn 0.2.x，当时 `opened` 是路径清单
- [error.v1.json](/schemas/cli/error.v1.json): 两个命令的失败结果，marsdawn 0.5.1 以前

## 环境变量

- `MARSDAWN_THEME`：没有传入 `--theme` 时，`export` 使用的主题。未知的值会直接改用 `dawn`，不会报错。

## 系统需求

- 这个工具需要 macOS 15 以上。在 Apple 芯片的 Mac 上，Homebrew 会安装预先构建好的版本，不需要其他东西。自己构建时（在 Intel Mac 上，或从源代码构建），需要 Swift 6.2 以上，也就是 Xcode 26 以上。
- MarsDawn app 需要 macOS 26 以上。

## 安装

使用 Homebrew。在 Apple 芯片的 Mac 上，会直接安装预先构建好的版本，几秒就完成，不需要 Xcode。在 Intel Mac 上则会从源代码编译 marsdawn，需要几分钟，也需要 Xcode 26 以上。

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

也可以从[源代码](https://github.com/redtear1115/mars-dawn-kit)构建。第一次构建会下载依赖项并编译，同样需要几分钟。

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` 会输出版本号，例如 `0.3.0`，并以代码 0 结束。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 给要掌舵 agentic 开发的人用的 Markdown：原生的 Mac 编辑器，有实时预览、Mermaid 图表和 PDF 输出。已在 Mac App Store 上架。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [输出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 输出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码和表格，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户，内置四种主题。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [在 Mac 上看 Markdown](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): md 文件是加上格式记号的纯文本。这页说明怎么在 Mac 上看到排版后的样子：现在可以用免费的 marsdawn 命令行工具转成 PDF，也可以用 Mac App Store 上的 MarsDawn app。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 agent 的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个 agent 写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回 agent 的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。更多可导入的主题，和让大家投稿主题的主题库，都在规划中。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把 agent 写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
