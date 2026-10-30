# 기본 테마 네 가지. 갤러리에 더 있습니다.

MarsDawn에는 새벽, 클래식, 모던, 비비드 네 가지 미리보기 테마가 기본으로 들어 있으며, 각각 라이트와 다크 팔레트를 갖추고 있습니다. 버전 1.1부터는 앱 안의 테마 갤러리에서 테마를 더 추가할 수 있고, Finder의 훑어보기도 고른 테마로 문서를 보여 줍니다.

## 네 가지 테마

- ![분할 화면의 새벽 테마: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.](/assets/screens/01-split-800.png) **새벽(기본 테마)**
- ![미리보기가 윈도우 전체를 채운 클래식 테마.](/assets/screens/02-classic-800.png) **클래식**
- ![분할 화면의 비비드 테마.](/assets/screens/04-vivid-800.png) **비비드**
- ![다크 모드의 MarsDawn, 분할 화면.](/assets/screens/03-dark-800.png) **다크 모드**

모던은 아직 스크린샷이 없어서, 네 번째 이미지는 대신 다크 모드를 보여 줍니다.

- **새벽**, 기본 테마: 이 사이트를 이루는 것과 같은 따뜻한 종이 색과 Mars Rust 강조색.
- **클래식**: 더 담백하고 문서다운 팔레트.
- **모던**: 더 차분하고 현대적인 팔레트.
- **비비드**: 더 밝고 대비가 강한 팔레트.

테마마다 라이트와 다크 변형이 따로 있어서, Mac의 화면 모드를 바꾸면 인터페이스만이 아니라 테마의 팔레트도 함께 바뀝니다.

## 앱 안의 테마 갤러리

MarsDawn에서 설정 ▸ 화면 모드를 열고 테마 더 받기…를 클릭합니다. 테마 갤러리는 열릴 때 목록을 불러옵니다. 열려 있는 동안에만 온라인에 연결되며, 연결이 없으면 안내를 표시하고 기본 테마 네 가지는 그대로 작동합니다.

- 설치는 라이트 테마와 다크 테마 선택 메뉴 및 보기 ▸ 미리보기 테마에 테마를 추가합니다. 제거는 테마를 삭제합니다.
- 테마 업데이트 확인은 갤러리에 새 버전이 있는지 다시 확인합니다.
- 테마의 용도별로 걸러 볼 수 있습니다: 에이전트 결과물 검토, 기술 문서, 공식 출력물, 노트 및 공유.
- 테마 신고…는 내용이 미리 채워진 GitHub 이슈나 저희에게 보내는 이메일을 엽니다.

## 갤러리에 있는 테마

현재 여덟 가지 테마가 있으며, 모두 저희가 만들고 검토했습니다. 잘 알려진 팔레트를 바탕으로 가독성을 손본 Dracula, Gruvbox, Nord, Solarized에 더해, 사용자 가이드, 예산표, PRD, 스프린트 노트를 위해 만든 Guide, Ledger, Spec, Story가 있습니다.

## 검토를 거치며, 오직 데이터뿐

모든 테마는 저희가 검토하고 병합한 뒤에야 갤러리에 나타납니다. 테마는 색상과 범위가 제한된 몇 가지 옵션으로 이루어진 작은 JSON 파일입니다. 스크립트도, CSS도, 작성자의 이미지도 없으며, MarsDawn은 설치하기 전에 모든 값을 검사합니다. 신고된 테마는 24시간 안에 갤러리에서 내려갑니다. 유해한 테마라면, 설치한 Mac에서 다음에 갤러리를 열 때 함께 제거되며, 사용 중이었다면 MarsDawn이 새벽으로 되돌립니다.

갤러리는 `marsdawn.southern-light.dev/themes/v1/`에만 요청을 보내며, 갤러리를 열거나 업데이트를 확인하거나 테마를 설치할 때만 연결됩니다. 계정, 식별자, 쿠키는 물론 문서의 어떤 내용도 보내지 않습니다.

## 훑어보기도 고른 테마를 씁니다

Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르세요. 훑어보기는 설치한 테마를 포함해 고른 테마로 파일을 보여 주며, MarsDawn의 화면 모드 설정을 따릅니다. 라이트와 다크는 고른 대로 유지되고, 시스템은 Mac을 따릅니다.

## PDF 내보내기와 프린트

PDF로 내보내거나 프린트하면 페이지는 라이트용으로 고른 테마를 씁니다. Mermaid 다이어그램이 그대로 그려지고, 코드 블록은 구문 강조를 유지하며, 페이지 나눔은 제목과 본문을 떼어 놓거나 표나 다이어그램을 반으로 자르지 않도록 피합니다. 무료 [marsdawn 명령줄 도구](/ko/cli/)도 같은 내보내기 엔진을 쓰며, `--theme`으로 네 가지 기본 테마 중 어느 것이든 지정할 수 있습니다.

## 페이지를 프린트한 뒤

프린트한 페이지를 둘러싼 회의, 여백에 펜으로 쓰는 글씨, 서류철에 보관되는 종이 기록.

[MarsDawn 영상(영어), 88초](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## 직접 만들기

[브라우저에서 테마를 만드세요](/ko/themes/new/): 색상과 몇 가지 스타일 옵션을 고르고, 실시간으로 적용된 모습을 본 뒤, 검토용 GitHub 이슈로 제출하면 됩니다. GitHub 계정은 필요하지만, 설치도 git도 필요 없습니다. 제출만으로는 아무것도 게시되지 않으며, 저희가 검토하고 병합한 뒤에야 [갤러리](/ko/themes/gallery/)에 나타납니다.

에이전트와 작업하고 있나요? [에이전트에게 테마를 만들게 하고](/ko/themes/agents/) 브라우저에서 다듬으세요.

## 다음

- 명령줄에서 PDF로 내보내는 전체 안내: [Markdown을 PDF로](/ko/markdown-to-pdf/).
- MarsDawn이 아직 하지 않는 일: [목록](/ko/limits/).
- Markdown을 쓰지 않는 사람에게 내보낸 PDF 전달하기: [PDF 공유하기](/ko/sharing-exported-pdfs/).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록을 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone·iPad에서의 편집도, 플러그인도, 계정도 없습니다. 테마는 바꿀 수 있지만 사용자 지정 CSS는 없습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [Mac용 Markdown 뷰어 추천 (2026)](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [에이전트와 함께 테마 만들기](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 개발자가 검토한 MarsDawn 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만들 수 있습니다. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
- [로드맵](https://marsdawn.southern-light.dev/ko/roadmap/index.md): Mac, iPhone, iPad용 MarsDawn에서 개발 중인 기능과 다음에 나올 기능을 버전별로 정리했습니다. 날짜는 적지 않고, 일정이 없는 항목은 따로 표시합니다.
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
- [English](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/index.md): 內建四種預覽主題，各有淺色與深色；在 Mac 版 MarsDawn 的設定裡打開主題庫，還能安裝更多。快速查看也會用你選的主題。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 内置四种预览主题，各有浅色与深色；在 Mac 版 MarsDawn 的设置里打开主题图库，还能安装更多。快速查看也会用你选的主题。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/index.md): それぞれライトとダークを備えた4種類の内蔵プレビューテーマに加え、Mac 版 MarsDawn の設定から開ける厳選ギャラリーも。クイックルックにも選んだテーマが反映されます。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/index.md): Vier integrierte Vorschauthemen in Hell und Dunkel sowie eine kuratierte Galerie in den Einstellungen von MarsDawn für Mac. Die Übersicht nutzt das Thema.
- [Français](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu intégrés, chacun clair et sombre, et une galerie vérifiée dans les réglages de MarsDawn pour Mac. Coup d’œil utilise votre thème.
- [Español](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa integrados, en claro y oscuro, y una galería revisada que abres desde Ajustes en MarsDawn para Mac. Vista rápida usa tu tema.
