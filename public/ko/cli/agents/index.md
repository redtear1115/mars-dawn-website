# 에이전트를 위한 marsdawn

`marsdawn` 명령줄 도구를 호출하는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 이 페이지의 모든 예시는 현재 소스로 빌드한 도구에서 실제로 실행했습니다.

**Markdown 파일을 PDF로 바꾸려면 `marsdawn export notes.md --json`을 실행하고 stdout에서 JSON 객체 하나를 읽으세요.** Mermaid 다이어그램과 강조 표시된 코드는 MarsDawn 앱에서와 똑같이 렌더링됩니다. `export`에는 앱이 필요 없고, `open`에는 필요합니다.

## 하는 일

- `export`는 MarsDawn 앱과 같은 내보내기 엔진으로 Markdown 파일 하나를 페이지가 나뉜 PDF로 렌더링합니다. 윈도우는 열리지 않습니다.
- `open`은 사람이 검토할 수 있도록 하나 이상의 Markdown 파일을 MarsDawn 앱에서 엽니다. 각 파일이 열릴 줄을 지정할 수 있고, 윈도우 사이드바에 폴더를 표시할 수도 있습니다.

## 하지 않는 일

- stdin에서 Markdown을 읽지 않습니다. 파일 경로를 전달하세요.
- PDF를 stdout에 쓰지 않습니다. PDF는 항상 파일로 저장되고, stdout에는 결과만 나옵니다.
- `--force`를 주지 않으면 기존 파일을 덮어쓰지 않습니다.
- `--allow-remote-images`를 주지 않으면 웹에서 이미지를 불러오지 않으며, 줄 때도 https로만 불러옵니다.
- `open`은 MarsDawn 앱이 설치되어 있지 않으면 동작하지 않고 코드 3으로 종료합니다. `export`에는 앱이 필요 없습니다. 앱은 [Mac App Store](https://apps.apple.com/app/id6812925073)에 있습니다.
- MarsDawn 1.0은 `open`이 지정한 줄에서 파일을 엽니다.
- macOS에서만 실행됩니다.

## export

```
marsdawn export notes.md --json
```

`notes.md` 옆에 `notes.pdf`를 씁니다. 옵션:

- `-o, --output <path>`: PDF를 쓸 위치. 기본값은 입력 경로에 확장자 `.pdf`를 붙인 것입니다.
- `--theme <dawn|classic|modern|vivid>`: 테마의 라이트 팔레트. 기본값은 `$MARSDAWN_THEME`, 그것도 없으면 `dawn`입니다.
- `--paper <a4|letter>`: 용지 크기. 기본값은 `a4`입니다.
- `--allow-remote-images`: 렌더링하는 동안 웹에서 https 이미지를 불러옵니다.
- `--force`: 출력 파일이 있으면 덮어씁니다.
- `--json`: 텍스트 대신 stdout에 JSON 객체 하나를 출력합니다.

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

성공, 종료 코드 0:

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`: 저장된 PDF의 절대 경로.
- `pages`: 페이지 수.
- `theme`과 `paper`: 실제로 사용된 값.
- `diagramErrors`: 렌더링에 실패한 Mermaid 다이어그램마다 메시지 하나. PDF는 그래도 저장됩니다.

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json
```

- `path:line`은 열릴 줄을 지정합니다. `notes.md:120:8`처럼 뒤에 붙은 열 번호는 무시됩니다. 존재하는 파일을 가리키는 인수는 항상 그 전체가 파일 이름이므로, `weird:12`라는 파일은 그 파일 자체로 열립니다.
- `--line <n>`은 파일 하나의 줄을 지정하며, 경로 자체가 콜론과 숫자로 끝나는 경우에도 쓸 수 있습니다. 파일이 정확히 하나여야 합니다.
- 줄 번호는 1부터 999999999까지입니다. 그 밖의 값은 사용법 오류입니다.
- 줄 지정은 marsdawn 0.3.0에서 추가되었습니다. MarsDawn 1.0은 그 줄에서 파일을 엽니다.
- 폴더 인수는 문서가 아니라 윈도우 사이드바에 열리므로, `marsdawn open .`은 현재 폴더를 보여 줍니다. `--folder <path>`는 파일과 함께 같은 일을 합니다. 윈도우 사이드바에는 폴더가 하나만 표시되므로, 폴더를 두 개 지정하면 사용법 오류이고, 같은 폴더라도 `--folder`를 두 번 쓰면 사용법 오류입니다. 같은 폴더를 인수로 한 번 더 주면 한 번으로 셉니다. 폴더에는 줄이 없으므로 폴더와 함께 `--line`을 쓰면 사용법 오류입니다. `-a`는 없습니다. 이를 주면 `--folder`를 안내하는 사용법 오류가 납니다.
- `--background`는 MarsDawn을 앞으로 가져오지 않고 엽니다. 사람이 다른 곳에서 일하는 동안 에이전트가 파일을 여는 경우를 위한 옵션입니다. JSON은 어느 쪽이든 같습니다.
- 폴더와 `--background`는 marsdawn 0.5.1에서 추가되었습니다.

성공, 종료 코드 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`: 파일마다 객체 하나, 주어진 순서대로. `path`는 파일의 절대 경로이고, `line`은 줄을 요청했을 때만 나타납니다.
- `app`: 파일을 연 MarsDawn 앱의 경로.

폴더를 준 경우(marsdawn 0.5.1 이상), 종료 코드 0:

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/project","requested":true},"ok":true,"opened":[{"path":"/path/to/project/notes.md"}]}
```

- `folder`: 폴더를 줬을 때만 나타납니다. `path`는 폴더의 절대 경로입니다. `requested`는 항상 `true`입니다. marsdawn은 MarsDawn에 폴더를 보여 달라고 요청했을 뿐이고, 앱이 먼저 사람에게 접근 권한을 물을 수 있으므로 사이드바에 실제로 표시됐는지는 알 수 없습니다. 완료가 아니라 요청됨으로 보고하세요.
- 폴더만 줬을 때 `opened`는 비어 있습니다.

marsdawn 0.2.x는 `opened`를 경로 문자열 목록으로 출력했습니다. 두 형식을 모두 처리해야 한다면 `marsdawn --version`을 확인하세요.

## Claude Code가 편집하는 파일 바로 열기

선택해서 쓰는 [Claude Code 훅](https://code.claude.com/docs/en/hooks)입니다. Claude가 Markdown 파일을 쓰거나 편집하면 그 파일을 MarsDawn에서 백그라운드로 엽니다. 세션마다 파일당 한 번입니다. 요청하지 않은 윈도우는 주의를 빼앗기 때문에, 직접 추가하기 전까지는 꺼져 있고 프로젝트별로 하나씩 켭니다. 셸 명령을 실행할 뿐이라 모델 토큰은 들지 않습니다.

`--background`를 쓰므로 marsdawn 0.5.1 이상과 MarsDawn 앱이 필요합니다.

다음을 프로젝트의 `.claude/hooks/marsdawn-open.sh`로 저장하고 `chmod +x`로 실행 권한을 주세요.

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

그런 다음 프로젝트의 `.claude/settings.json`에 훅을 추가하세요. 나만 쓰려면 `.claude/settings.local.json`에 추가하면 됩니다.

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

- Claude의 Write와 Edit 도구 다음에 실행됩니다. `.md`나 `.markdown`으로 끝나지 않는 파일은 건드리지 않습니다.
- Claude가 몇 번을 편집하든 각 파일은 Claude Code 세션마다 한 번만 열립니다. 목록은 `$TMPDIR/marsdawn-hook/`에 세션마다 파일 하나로 저장되므로, 새 세션에서는 파일이 다시 열립니다.
- `--background` 덕분에 MarsDawn이 앞으로 나오지 않습니다. 작업하던 윈도우가 포커스를 유지합니다.
- Claude를 방해하지 않습니다. 모든 경로가 0으로 끝나며, marsdawn이나 MarsDawn 앱이 설치되어 있지 않으면 아무 일도 일어나지 않습니다.
- 훅의 입력은 `/usr/bin/jq`로 읽습니다. jq는 MarsDawn 앱이 요구하는 macOS 26에 기본으로 들어 있습니다.
- 끄려면 설정 파일에서 해당 항목을 지우세요.

## 실패

`--json`을 주면 실패 시 stdout에 JSON 객체 하나를 출력하고 해당 코드로 종료합니다.

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: 입력이 없거나, 폴더이거나, UTF-8 텍스트가 아닙니다. 또는 `--folder` 경로가 없거나 폴더가 아닙니다.
- `3`, `app_not_installed`: MarsDawn이 설치되어 있지 않습니다. `open`만 이 코드를 반환합니다.
- `4`, `output_exists`: 출력 파일이 이미 있습니다. `--force`를 주세요.
- `5`, `export_failed`: 내보내기 자체가 실패했습니다.
- `6`, `app_cannot_open_folders`: 이 버전의 MarsDawn은 폴더를 표시할 수 없어서 아무것도 열지 않았습니다. `open`만 이 코드를 반환합니다.
- `64`: 사용법 오류. 알 수 없는 옵션, 잘못된 값, 범위를 벗어난 줄, 파일 두 개 이상이나 폴더와 함께 쓴 `--line`, 폴더 두 개 이상, `-a` 등이 해당합니다. 이 오류는 `--json`을 줘도 stderr에 텍스트로 출력됩니다.

## JSON 스키마

모든 `--json` 결과에 대한 JSON Schema(draft 2020-12):

- [export.v1.json](/schemas/cli/export.v1.json): export 성공
- [open.v3.json](/schemas/cli/open.v3.json): open 성공, marsdawn 0.5.1 이상, 사이드바에 표시되는 폴더 포함
- [error.v2.json](/schemas/cli/error.v2.json): 실패, 두 명령 공통, marsdawn 0.5.2 이상
- [open.v2.json](/schemas/cli/open.v2.json): open 성공, marsdawn 0.3.0~0.5.0
- [open.v1.json](/schemas/cli/open.v1.json): open 성공, marsdawn 0.2.x, 이때 `opened`는 경로 목록이었음
- [error.v1.json](/schemas/cli/error.v1.json): 실패, 두 명령 공통, marsdawn 0.5.1 이하

## 환경 변수

- `MARSDAWN_THEME`: `--theme`을 주지 않았을 때 `export`가 쓰는 테마. 알 수 없는 값이면 오류 없이 `dawn`으로 돌아갑니다.

## 요구 사항

- 이 도구는 macOS 15 이상에서 실행됩니다. Apple 실리콘에서는 Homebrew가 미리 빌드된 bottle을 설치하므로 다른 것은 필요 없습니다. Intel Mac에서나 소스로 직접 빌드하려면 Swift 6.2 이상이 필요하며, 이는 Xcode 26 이상에 들어 있습니다.
- MarsDawn 앱은 macOS 26 이상이 필요합니다.

## 설치

Homebrew로 설치합니다. Apple 실리콘에서는 미리 빌드된 bottle을 몇 초 만에 설치하며 Xcode가 필요 없습니다. Intel Mac에서는 marsdawn을 소스에서 컴파일하므로 몇 분이 걸리고 Xcode 26 이상이 필요합니다.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

또는 [소스](https://github.com/redtear1115/mars-dawn-kit)에서 직접 빌드하세요. 첫 빌드는 의존성을 가져와 컴파일하므로 역시 몇 분이 걸립니다.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version`은 `0.3.0` 같은 버전 번호를 출력하고 코드 0으로 종료합니다.

## 다음

- 셸 대신 지침 파일을 읽는 에이전트를 위한 파일 하나짜리 스킬: [marsdawn 스킬](/ko/cli/skill/).
- 이 `export`를 그대로 감싼 MCP 서버: [marsdawn-mcp](/ko/cli/mcp/).
- 이 JSON 결과가 에이전트 자신의 컨텍스트에 부담이 적은 이유: [토큰을 아끼는 검토](/ko/token-efficient-review/).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트의 작업을 이끄는 사람을 위한 Markdown. 실시간 미리보기, Mermaid 다이어그램, PDF 내보내기를 갖춘 Mac 네이티브 편집기입니다. Mac App Store에서 구입할 수 있습니다.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 가져올 수 있는 테마를 더 늘리고, 직접 만든 테마를 공유하는 갤러리도 계획하고 있습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Français](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Español](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
