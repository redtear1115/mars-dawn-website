# MacMD Viewer와 MarsDawn.

둘 다 Markdown을 완성된 페이지로 읽는 Mac 앱입니다. MacMD Viewer는 `.md` 파일을 열어 보여 줍니다. 설계상 읽기 전용이라 파일에 대한 변경 사항을 저장하지 않습니다. MarsDawn은 같은 종류의 렌더링된 미리보기 옆에 편집기를 두어, 한 창에서 쓰고 검토할 수 있게 합니다. 이 페이지는 둘을 항목별로 나란히 놓고, MacMD Viewer에 관한 모든 사실에 출처를 달았으며, MacMD Viewer가 더 나은 선택인 경우도 알려 줍니다.

MacMD Viewer 자체 사이트와 저장소를 기준으로 2026년 10월 15일에 확인했습니다(버전 1.7.0, 2026년 10월 10일 출시). 오래된 내용이 있으면 [지원 페이지](/ko/support/)의 주소로 알려 주세요.

## 무엇이고, 무엇을 하는가

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 정체 | 뷰어: “읽기 전용이며 원본 파일에 대한 변경 사항을 저장하지 않음” [[S1](#s1), [S9](#s9)] | 실시간 미리보기가 있는 편집기: 왼쪽에 Markdown, 오른쪽에 렌더링된 페이지, 세 가지 레이아웃(소스, 분할, 미리보기) |
| 편집 | 불가 [[S1](#s1), [S7](#s7), [S9](#s9)] | 가능. 렌더링된 페이지 자체는 편집할 수 없고, 옆의 소스를 편집함 |
| 실시간 미리보기 | 파일을 렌더링함. 다른 편집기가 파일을 저장하면 다시 불러옴 [[S9](#s9)] | 입력하는 동안 업데이트됩니다. 다른 앱이 파일을 바꾸면 MarsDawn이 다시 불러오고 위치를 유지합니다(저장하지 않은 본인의 편집이 없는 경우). |
| Mermaid | 지원: 순서도, 시퀀스, 상태, 간트 다이어그램, 파이 차트 등, 오프라인 [[S1](#s1), [S3](#s3), [S7](#s7)] | 지원 |
| 수식 | 미지원: README에 “수식(LaTeX/KaTeX)을 렌더링하지 않음”이라고 적혀 있음 [[S7](#s7)] | 지원, KaTeX |
| 코드 강조 | 지원 [[S1](#s1), [S9](#s9)] | 지원 |
| 테마 | 문서 테마 12종 [[S1](#s1), [S7](#s7)] | 기본 4종(새벽, 클래식, 모던, 비비드), 각각 라이트와 다크 팔레트, 테마 갤러리에 더 많음 |
| 탭 | 지원, 선택 사항이며 기본값은 꺼짐(1.6.0부터) [[S5](#s5), [S8](#s8)] | 지원 |
| PDF 내보내기 | 지원, 연속된 한 페이지, 현재 테마, 워터마크 없음 [[S3](#s3), [S9](#s9)] | 지원, 쪽이 나뉜 페이지, 테마의 라이트 팔레트. 쪽 나누기는 짧은 코드 블록이 잘리지 않게 함 |
| 프린트 | 지원, macOS 프린트 대화상자 사용 [[S3](#s3), [S9](#s9)] | 지원 |
| Finder 훑어보기 | 지원, 포함되어 있음. 시스템 설정에서 켬. 선택한 테마 사용 [[S4](#s4)] | 지원, 체험 중이든 아니든 작동. 선택한 테마 사용 |
| 훑어보기의 Mermaid와 수식 | Mermaid: 지원 [[S4](#s4)]. 수식: 미지원, 렌더링하지 않음 [[S7](#s7)] | 지원, 둘 다 그려짐 |
| 명령줄 | 독립된 명령줄 도구는 기재되어 있지 않음. `markdownviewer://` URL 스킴과, 뷰어에서 파일을 여는 Claude Code 플러그인 및 훅이 있음 [[S6](#s6)] | 무료 `marsdawn` 도구: `marsdawn export`는 앱 없이 PDF를 만들고, `marsdawn open`은 지정한 줄에서 파일을 엶 |
| 인터페이스 언어 | 자체 자료에 기재되어 있지 않음 [[S1](#s1), [S3](#s3), [S7](#s7)] | 영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어 |
| 요구 사항 | macOS 14(Sonoma) 이상, Apple 실리콘과 Intel [[S1](#s1), [S7](#s7)] | macOS 26(Tahoe) 이상 |
| 다른 플랫폼 | Mac 전용 [[S1](#s1)] | Mac 전용. iPhone이나 iPad 앱은 없음 |

## 가격과 구입 방법

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 구입처 | 자체 사이트, Homebrew 또는 Setapp. Mac App Store에는 없음 [[S2](#s2), [S7](#s7)] | Mac App Store에서만 |
| 가격 | 사용 중인 Mac 1대당 USD 19.99 일회성(다른 Mac으로 옮길 수 있음). Family Pack은 3개 키에 USD 39.99, 키 10개는 USD 129 [[S2](#s2)] | 무료 다운로드 후 USD 4.99 일회성 |
| 먼저 사용해 보기 | 체험판도 무료 버전도 없음. 직접 구입 시 14일 이내 전액 환불 [[S2](#s2)] | 14일 무료 체험, 모든 기능 사용 가능 |
| 환불 | 14일 이내, 자체 지원을 통해 [[S2](#s2)] | Apple을 통해 |
| 업데이트 | 현재 메이저 버전 안의 업데이트는 무료 [[S2](#s2)]. 직접 내려받은 버전은 Sparkle로 자동 업데이트 [[S7](#s7)] | Mac App Store를 통해 |
| 계정 필요 | 아니요 [[S2](#s2)] | 아니요 |
| 구독 | 없음 [[S1](#s1), [S2](#s2)] | 없음 |

## 체험이나 구입 기간이 끝나면 달라지는 것

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| 그 이후 | 체험판 없음. 구입하면 계속 작동함 | 14일 뒤에도 잠금을 해제하지 않으면 문서는 열리지만 내용이 가려집니다. 파일은 그대로이고, 훑어보기와 무료 `marsdawn` 내보내기는 계속 작동합니다 |

## 출처

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## 어느 쪽을 고를까

**MacMD Viewer를 고르세요.** Markdown을 읽기만 하고, 파일이 절대 바뀌지 않는다는 보장을 원한다면 말입니다. 파일에 대한 변경 사항을 저장하지 않습니다 [[S1](#s1)]. 다음 경우에도 더 잘 맞습니다. Mac이 macOS 14나 15인 경우(MarsDawn은 macOS 26이 필요) [[S1](#s1), [S7](#s7)], Mac App Store보다 개발자 사이트, Homebrew, Setapp에서 사고 싶은 경우 [[S2](#s2), [S7](#s7)], 에이전트가 편집한 파일이 뷰어에서 자동으로 열리길 원하는 경우(Claude Code, Cursor, Windsurf용 훅으로 가능) [[S6](#s6)], 쪽이 나뉜 PDF보다 연속된 한 페이지 PDF를 원하는 경우 [[S9](#s9)]. 체험판은 없지만 14일 환불이 있습니다 [[S2](#s2)].

**MarsDawn을 고르세요.** Markdown을 읽고 나서 한 번 더 손봐야 한다면 말입니다. 에이전트가 쓴 계획, README, 사양은 보통 한 곳을 고치거나, 한 줄을 다시 쓰거나, 한 절을 추가해야 하는데, MarsDawn에서는 이미 읽고 있는 창에서 바로 할 수 있습니다. 수식(KaTeX)도 지원하는데, MacMD Viewer는 렌더링하지 않는다고 밝히고 있습니다 [[S7](#s7)]. 인터페이스는 8개 언어이고, 앱 없이 PDF를 내보내는 무료 `marsdawn` 명령줄 도구가 있으며, 가격은 모든 기능을 쓸 수 있는 14일 체험 후 USD 4.99입니다.

**둘 다 괜찮습니다.** 비교적 최신 Mac에서 Markdown을 읽고, Mermaid 다이어그램이 제대로 그려지길 원하고, Finder 훑어보기를 쓰고 싶다면요. 둘 다 됩니다.

**둘 다 쓸 수도 있습니다.** 서로 배타적이지 않습니다. 읽기만 하는 파일에는 읽기 전용 뷰어를, 쓰는 파일에는 편집기를 쓰는 데 아무 문제가 없습니다.

## 자주 묻는 질문

### MacMD Viewer는 파일을 편집하나요?

아니요. 읽기 전용이며, 자체 설명대로 원본 파일에 대한 변경 사항을 저장하지 않습니다 [[S1](#s1), [S9](#s9)]. 파일을 사용자의 텍스트 편집기에서 열 수 있지만(파일 메뉴, ⇧⌘E, 1.7.0부터), 이는 파일을 다른 앱에 넘기는 기능입니다 [[S5](#s5)].

### MacMD Viewer는 Mac App Store에 있나요?

자체 페이지에는 사이트, Homebrew, Setapp이 나와 있고 Mac App Store는 언급되어 있지 않습니다 [[S2](#s2), [S7](#s7)]. MarsDawn은 Mac App Store에서만 받을 수 있습니다.

### MarsDawn도 같은 파일을 열 수 있나요?

네. `.md` 파일은 물론 일반 텍스트 파일과 PDF도 엽니다. 텍스트는 UTF-8로 바로 편집할 수 있게 열리고, PDF는 뷰어로 열립니다.

### macOS 14나 15를 쓰면요?

MacMD Viewer는 macOS 14 이상에서 실행됩니다 [[S1](#s1)]. MarsDawn은 macOS 26 이상이 필요하지만, 무료 `marsdawn` 명령줄 도구로는 여전히 PDF를 내보낼 수 있습니다.

### 왜 하나는 USD 19.99이고 다른 하나는 USD 4.99인가요?

얻는 것과 결제 방식이 다릅니다. MacMD Viewer는 14일 환불이 있고 체험판이 없는 일회성 구입입니다 [[S2](#s2)]. MarsDawn은 무료로 다운로드해 14일 체험한 뒤 한 번 잠금을 해제합니다. 둘 다 구독이 아닙니다.

## 지금 무료로 사용해 보세요

MarsDawn은 Mac App Store에 있습니다. 무료 `marsdawn` 명령줄 도구도 어떤 Markdown 파일이든 Mermaid 다이어그램과 강조 표시된 코드를 포함한 PDF로 렌더링하며, 다른 것은 아무것도 설치할 필요가 없습니다.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## 다음

- 전체 안내: [Markdown을 PDF로](/ko/markdown-to-pdf/).
- MarsDawn이 하지 않는 일: [목록](/ko/limits/).
- 명령줄 도구의 모든 옵션: [명령줄](/ko/cli/).
- VS Code, 브라우저, Claude Desktop에서 Markdown을 읽는 경우와 비교: [비교해 보기](/ko/vs/markdown-preview-tools/).
- MarsDawn의 모든 기능을 한 페이지에: [기능 한눈에 보기](/ko/features/).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
