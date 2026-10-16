만드는 사람을 위한 개척자의 도구

# 지도를 손에 쥐세요. 새벽을 읽으세요.

에이전트의 작업을 이끄는 사람을 위한 Markdown.

MarsDawn은 Markdown을 읽고 검토하는 Mac 네이티브 앱으로, 분할 실시간 미리보기, Mermaid 다이어그램, KaTeX 수식, 훑어보기, PDF 내보내기를 갖추고 있으며, 14일 동안 무료로 체험한 뒤 USD 4.99 한 번으로 잠금 해제할 수 있습니다.

이 페이지에는 앱의 시작 가이드 일부를 보여 주는, 직접 조작할 수 있는 MarsDawn 창이 있습니다. 팔레트 메뉴에서 화면 모드(시스템, 라이트, 다크)를 고르고, 라이트와 다크에 각각 네 가지 미리보기 테마(새벽, 클래식, 모던, 비비드) 중 하나를 지정할 수 있으며, 도구 막대에서는 세 가지 레이아웃(소스, 분할, 미리보기) 중 하나를 고를 수 있습니다.

## 에이전트가 쓴 글을 읽으세요.

1. **에이전트가 씁니다.** 코딩 에이전트나 글쓰기 도우미가 README, 명세서, 메모 같은 Markdown 초안을 작성합니다.
2. **MarsDawn에서 검토합니다.** 파일을 열고, [Mermaid 다이어그램](/ko/mermaid-preview-mac/)과 하이라이트된 코드까지 렌더링된 페이지를 소스 옆에 두고 읽으세요.
3. **에이전트가 고칩니다.** 수정을 요청하세요. 고친 파일을 열어 같은 방식으로 읽으면 됩니다.

[에이전트가 돌려준 결과를 검토하는 방법](/ko/reading-agent-output/) · [Mac에서 .md 파일 여는 방법](/ko/view-markdown-on-mac/)

## 에이전트의 계획, 실행 전에 검토하세요.

순서가 틀린 단계를 찾아 그 줄을 짚고, 에이전트에게 돌려보냅니다.

1. 변경 사항 보기: 에이전트가 저장하면 열려 있는 윈도우가 디스크에서 업데이트되며, 한 번에 실행 취소할 수 있습니다.
2. 그 줄로 이동: marsdawn open plan-checkout-v2.md:10으로 윈도우가 10행으로 이동하고 미리보기의 해당 블록이 깜박입니다.
3. 돌려보내기: ‘참조 복사’(⌥⌘C)로 plan-checkout-v2.md:10을 복사해, 의견과 함께 에이전트 채팅에 붙여 넣습니다.

## 지금 바로 해 보세요

무료 `marsdawn` 명령줄 도구는 지금 바로 쓸 수 있습니다. Homebrew로 설치하세요.

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export`는 Markdown 파일을 MarsDawn의 미리보기처럼 렌더링된 PDF로 만듭니다. 앱은 필요 없습니다.
- `marsdawn open`은 검토할 수 있도록 MarsDawn 앱에서 파일을 엽니다.
- `--json`은 스크립트와 에이전트가 파싱할 수 있는 결과를 돌려줍니다.

[명령줄](/ko/cli/) · [에이전트를 위한 marsdawn](/ko/cli/agents/) · [에이전트 스킬](/ko/cli/skill/) · [MCP 서버](/ko/cli/mcp/)

## MarsDawn에서 기대할 수 있는 것

- [Mac 앱](/ko/native/): 네이티브 윈도우와 탭, 자동 저장, [훑어보기](/ko/quicklook/).
- [내 글은 내 Mac에](/ko/yours/): 계정도, 동기화도, 클라우드도 없습니다.
- [무료로 체험하고, 한 번만 구입](/ko/pay-once/): 14일 무료, 이후 USD 4.99 1회 구입. 구독이 아닙니다.
- [기능 한눈에 보기](/ko/features/): MarsDawn이 하는 모든 일을 한 페이지에.

구입 전에 알아 둘 점. [MarsDawn이 하지 않는 일](/ko/limits/)

## 각 부분의 역할

MarsDawn 1.1.1, marsdawn 0.6.4, marsdawn-mcp v0.2.4 기준으로 각 부분이 지금 하는 일.

| 기능 | 앱 | CLI | MCP / 스킬 | 상태 |
|---|---|---|---|---|
| 특정 줄에서 열기 | 그 줄로 이동, 미리보기 블록이 깜박임 | `marsdawn open notes.md:120` (`--background`는 포커스 유지) | `open_in_marsdawn`, 스킬은 한 번만 열기 | 제공 중 |
| PDF 내보내기 | 파일 ▸ PDF로 내보내기… (⌥⌘E) | `marsdawn export`, 앱 없이 | `export_markdown_to_pdf`, 스킬 | 제공 중 |
| JSON 결과 | — | open과 export에 `--json` | MCP가 같은 JSON 반환 | 제공 중 |
| 에이전트 스킬 | — | `marsdawn skill --install` | 한 번 열기와 내보내기를 안내 | 제공 중 |
| MCP 서버 | — | 내부에서 실행 | marsdawn-mcp: 도구 두 개, 허용한 폴더만 | 제공 중 |
| AI용으로 복사, 참조 복사 | 편집 ▸ AI용으로 복사 (⌃⌥⌘C), 참조 복사 (⌥⌘C) | — | — (어떤 에이전트에든 붙여 넣기) | 제공 중 |
| 저장 시 자동 반영 | 저장된 변경을 반영, 한 번에 실행 취소 | — | 스킬: 다시 열지 않음 | 제공 중 |
| Claude Code 훅 | — | `open --background` 사용 | /cli/agents/의 훅 스크립트 | 문서 제공, 선택 사항 |

제공 중: 위에 적은 출시 버전에 포함. 문서 제공, 선택 사항: 이 사이트의 안내에 따라 직접 추가하며 도구에는 포함되지 않음. 예정: 아직 없으며 날짜 미정. 예정: MCP `open_in_marsdawn`의 폴더 옵션. `--folder` 등 다른 옵션은 [명령줄](/ko/cli/)에 있습니다.

## 코딩 에이전트로 Mac 앱을 만든다면

개인 Mac 개발자를 위해: 에이전트가 쓴 파일을 지금 MarsDawn에서 여는 방법입니다.

| 도구 | 연결 방식 | 설정 |
|---|---|---|
| Claude Code | 스킬에 따라 쓴 파일을 한 번, 그 줄에서 엽니다: `marsdawn open plan.md:42`. 선택 사항인 훅을 켜면 쓴 .md를 매번 백그라운드에서 엽니다 | `marsdawn skill --install`, 훅 스크립트는 /cli/agents/에 |
| Codex, Cursor, Xcode | 아직 전용 설정 안내가 없습니다. 셸 명령을 실행할 수 있는 도구라면 `marsdawn open file:line --json`을 호출할 수 있고, 지침 파일을 읽는 에이전트는 SKILL.md(`--dir`)를, MCP만 쓰는 클라이언트는 marsdawn-mcp를 쓸 수 있습니다 | `brew install redtear1115/tap/marsdawn` |

훅과 명령: [에이전트를 위한 marsdawn](/ko/cli/agents/) · [에이전트 스킬](/ko/cli/skill/) · [MarsDawn이 하지 않는 일](/ko/limits/)

MarsDawn, VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice 사이에서 고민 중인가요? 비교 페이지에 각 회사의 설명, MarsDawn에 없는 것, MarsDawn이 필요 없는 경우를 정리했습니다. [비교 보기](/ko/vs/)

## 문서는 Mac에 남습니다

Mac 안에서. 읽기, 편집, 렌더링, [PDF 내보내기](/ko/privacy/#exporting-and-printing), [marsdawn 명령줄 도구](/ko/privacy/#the-marsdawn-command-line-tool)가 모두 이곳에서 오프라인으로도 실행되며, 앱은 문서를 업로드하지 않습니다.

자세히: [개인정보 처리방침](/ko/privacy/#what-stays-on-your-mac)

기본적으로 네트워크에 연결하지 않습니다. 웹 이미지는 ‘이미지 불러오기’를 클릭하거나 설정에서 ‘원격 이미지 자동으로 불러오기’를 켰을 때만 불러오고, HTML 문서는 코드가 실행되지 않는 정적인 상태로 열립니다.

자세히: [개인정보 처리방침](/ko/privacy/#when-marsdawn-uses-the-internet)

밖으로 나가는 것은 선택했을 때만. ‘AI용으로 복사’는 텍스트를 클립보드에 넣을 뿐이고 붙여 넣는 것은 사용자입니다. 테마 다운로드, ‘보기 › 이 문서 실행’으로 실행한 문서, 에이전트에게 읽게 한 파일도 사용자가 정했을 때만 밖으로 나갑니다.

자세히: [개인정보 처리방침](/ko/privacy/#when-marsdawn-uses-the-internet)

## 자주 묻는 질문

### MarsDawn은 무엇인가요?

MarsDawn은 에이전트가 쓴 Markdown을 읽고 검토하기 위한 Mac 네이티브 앱입니다. 소스 옆에 실시간 미리보기를 띄우고, Mermaid와 KaTeX를 그리며, 훑어보기로 .md 파일을 미리 보고, PDF로 내보냅니다. 소스를 직접 편집할 수도 있습니다.

### MarsDawn은 구독인가요?

아니요. MarsDawn은 무료로 다운로드할 수 있고, 14일 동안 모든 기능을 체험할 수 있습니다. 그 뒤에는 USD 4.99의 앱 내 구입 한 번으로 영구히 잠금 해제됩니다. 갱신되는 것은 없고, 계정도 없습니다.

### MarsDawn은 iPhone이나 iPad에서 쓸 수 있나요?

아니요. MarsDawn은 Mac 앱이며 macOS 26 이상이 필요합니다. iPhone용이나 iPad용 앱은 없습니다.

### Claude Code가 MarsDawn에서 파일을 열 수 있나요?

네. 무료 marsdawn 명령줄 도구에는 Markdown 파일을 MarsDawn에서 여는 open 명령이 있어서, Claude Code나 셸 명령을 실행할 수 있는 모든 에이전트가 호출할 수 있습니다. 선택적으로 켜는 Claude Code 훅은 Claude가 쓰거나 편집한 Markdown 파일을 열어 줍니다.

### MarsDawn이 내 문서를 업로드하나요?

아니요. 앱은 문서를 업로드하지 않고, 사용자에 관한 데이터를 수집하지 않으며, 계정도 없습니다. 문서와 설정은 Mac에 남습니다. 문서가 웹을 참조하고 그 내용을 불러오기로 선택한 경우에만 Mac이 해당 내용을 호스팅하는 서버에서 직접 가져오며, MarsDawn 개발자는 이 정보를 전혀 받지 않습니다.

자세히: [개인정보 처리방침](/ko/privacy/#what-stays-on-your-mac)

### MCP나 스킬을 쓰면 누가 내 파일을 볼 수 있나요?

MarsDawn 자체는 아무것도 보내지 않습니다. 스킬은 지침을 적은 텍스트 파일이고, marsdawn 명령줄 도구와 MCP 서버는 Mac에서 실행되며, MCP 서버는 허용한 폴더 안에서만 동작합니다. 파일을 읽는 것은 사용자의 에이전트이며, 그 에이전트와 모델 제공자가 파일을 어떻게 다루는지는 해당 에이전트의 정책을 따릅니다. MarsDawn은 이를 관리하지도, 설명하지도 않습니다.

자세히: [MCP](/ko/cli/mcp/)

### 다른 사람이 보낸 HTML을 열어도 안전한가요?

기본적으로 정적인 상태로 열려 코드가 실행되지 않고 웹에서 아무것도 불러오지 않습니다. ‘보기 › 이 문서 실행’을 선택하면 그 문서가 실행되어 네트워크로 데이터를 보내거나 같은 폴더의 이미지, 스타일시트, 글꼴, 미디어를 읽을 수 있습니다. 이 선택은 기억되지 않으므로 다음에 열 때는 다시 정적인 상태입니다.

자세히: [개인정보 처리방침](/ko/privacy/#when-marsdawn-uses-the-internet)

### 웹사이트의 분석 쿠키가 앱과 관련이 있나요?

아니요. 앱과 이 웹사이트는 별개입니다. 앱은 아무것도 수집하지 않으며, 방문이 기록될 수 있는 곳은 marsdawn.southern-light.dev뿐입니다. 사이트의 Google Analytics는 거부된 상태로 시작하고, 배너에서 ‘수락’을 선택한 뒤에만 쿠키를 설정하며, 하단의 ‘쿠키 설정’에서 언제든 바꿀 수 있습니다. 앱이 /themes/ 아래 테마 파일을 요청하는 것은 기록하지 않습니다.

자세히: [개인정보 처리방침](/ko/privacy/#the-website)

## 앱의 실제 모습

### [Mac 앱](/ko/native/)

![분할 보기의 MarsDawn: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

이 스크린샷의 내용:

1. 네이티브 Mac 윈도우.
2. Markdown 하이라이트가 더해진 Mac의 텍스트 편집기.
3. ⌘1 소스, ⌘2 분할, ⌘3 미리보기.
4. 입력하는 대로 페이지가 바뀝니다.

### [PDF 내보내기](/ko/pdf/)

![MarsDawn에서 내보낸 PDF를 페이지 축소판과 함께 PDF 뷰어로 연 모습.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

이 스크린샷의 내용:

1. Mermaid 다이어그램이 PDF 안에 그려집니다.
2. 코드는 하이라이트를 유지합니다.

## 더 보기

- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록을 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지이고, 갤러리에 더 있습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 브라우저에서 테마를 직접 만들고, 커뮤니티 갤러리도 둘러보세요.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [에이전트와 함께 테마 만들기](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
- [편집자의 독서 노트](https://marsdawn.southern-light.dev/ko/reading-notes/index.md): AI 에이전트를 만드는 사람들이 실제로 무엇을 주장하는지 살피는 짧은 노트 여섯 편 — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain, Andrew Ng — 그리고 각각이 그런 에이전트가 돌려준 것을 읽어야 하는 사람에게 무엇을 의미하는지.
- [독서 노트: Anthropic](https://marsdawn.southern-light.dev/ko/reading-notes/anthropic-building-effective-agents/index.md): 2024년 12월 Anthropic이 에이전트를 만드는 사람을 위해 낸 가이드는 workflow와 agent를 나누고, 그중 하나가 두 번째 LLM 호출로 첫 번째를 검토하는 다섯 가지 workflow 패턴을 설명합니다. 그게 폴더에 떨어지는 파일에 무엇을 뜻하는지.
- [독서 노트: Chip Huyen](https://marsdawn.southern-light.dev/ko/reading-notes/chip-huyen-agents/index.md): Chip Huyen의 2025년 1월 에세이 «Agents»는 에이전트 행동을 read-only와 write로 나눕니다. 그 구분이 계획에서 승인 전에 더 자세히 볼 줄을 빠르게 짚는 방법이 되는 이유.
- [독서 노트: Lilian Weng](https://marsdawn.southern-light.dev/ko/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.
- [독서 노트: Harrison Chase](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
- [독서 노트: LangChain(Jess Ou)](https://marsdawn.southern-light.dev/ko/reading-notes/langchain-what-is-an-agent/index.md): LangChain의 2026년 «What is an AI agent?»(Jess Ou)는 Harrison Chase의 2024년 정의를 이어받고, 에이전트를 자동으로 평가하는 파이프라인을 그립니다. 그 파이프라인이 아직 사람에게 넘기는 단계, 그리고 넘기지 않는 단계.
- [독서 노트: Andrew Ng](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 讀懂、檢查 agent 寫的 Markdown 的 Mac 原生 app：分割即時預覽、Mermaid、KaTeX、快速查看、PDF 輸出。可免費試用，之後一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown を読んで確かめる Mac ネイティブアプリ。分割ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、解除は一度だけ USD 4.99。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
