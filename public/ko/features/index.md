# MarsDawn이 하는 모든 일을 한 페이지에.

MarsDawn은 Mac용 Markdown 편집기입니다. 한쪽에서 쓰고 다른 쪽에서 렌더링된 페이지를 읽으며, 다이어그램과 수식, 코드가 그대로 그려집니다. 자체 AI 모델은 없습니다. 에이전트가 쓴 글을 읽고 내 글을 쓰기 위해 만든 앱입니다. 그리고 작업이 책상이나 회의, 서류 보관함으로 옮겨 가면 깔끔한 페이지를 프린트하고 내보냅니다.

아래 각 절은 앱이 하는 일을 설명하고, 더 자세히 다루는 페이지로 연결합니다.

![분할 보기의 MarsDawn: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

이 스크린샷의 내용:

1. 네이티브 Mac 윈도우.
2. Markdown 하이라이트가 더해진 Mac의 텍스트 편집기.
3. ⌘1 소스, ⌘2 분할, ⌘3 미리보기.
4. 입력하는 대로 페이지가 바뀝니다.

## 에이전트가 쓴 글 읽기

### 소스와 미리보기를 나란히

Markdown 파일을 열면 렌더링된 페이지가 소스 옆에 나타납니다(⌘2). 소스만(⌘1) 또는 미리보기만(⌘3) 볼 수도 있습니다. 두 패널은 함께 스크롤되고, 페이지는 입력하는 대로 업데이트됩니다.

[Mac 앱](/ko/native/)

### 개요와 파일 사이드바

사이드바의 개요 탭에는 문서의 제목이 나열되며, 하나를 클릭하면 그 위치로 이동합니다. 폴더를 열면 파일 탭에 안에 든 파일이 나열되고, 에이전트가 쓰는 동안 새 파일이 저절로 나타납니다. 폴더가 git 체크아웃이면 머리말에 브랜치나 worktree 이름이 표시됩니다.

[에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)

### 정확한 줄 가리키기

편집 ▸ 참조 복사는 현재 위치를 `docs/plan.md:42`처럼 경로와 줄 번호로 복사합니다. AI용으로 복사는 그 아래에 선택한 텍스트를 덧붙입니다. 어느 쪽이든 에이전트의 채팅에 붙여넣으면 됩니다.

[에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)

### 파일 사이의 링크 따라가기

미리보기에서 다른 Markdown 파일로 가는 링크를 클릭하면 MarsDawn이 그 파일을 열고(이미 열려 있으면 앞으로 가져오고) 해당 제목까지 스크롤합니다.

## 종이 위에서, 사람들 사이에서

모든 작업이 화면에서만 이루어지지는 않습니다. MarsDawn이 프린트하고 내보내는 페이지는 화면에서 읽는 바로 그 페이지이므로, 사람들이 모이고, 읽고, 기록을 보관하는 곳에서도 쓸 수 있습니다.

### 회의에서

페이지를 프린트하거나 모두에게 같은 PDF를 보내면, 한 화면을 함께 보는 대신 테이블 전체가 같은 문서로 작업할 수 있습니다. 같은 파일을 가진 사람은 페이지 나눔도 같으므로 ‘3쪽의 표’가 모두에게 같은 것을 가리킵니다. 그다음 사람들이 결정 사항을 프린트한 종이나 메모에 적습니다. 회의 메모 템플릿은 결정 사항으로 시작하고 각 실행 항목에 담당자를 둡니다.

[PDF 내보내기](/ko/pdf/) · [회의록 템플릿](/ko/templates/meeting-notes/)

### 펜으로 읽기

펜으로 밑줄을 긋고 여백에 적어 가며 읽어야 머리에 잘 남는 사람도 있습니다. 문서를 프린트해서 종이 위에서 그렇게 하세요. MarsDawn에는 자체 주석 도구가 없으니, PDF에 표시하고 싶다면 이미 쓰고 있는 PDF 앱을 사용하세요.

[PDF 내보내기](/ko/pdf/)

### 종이 기록

아직도 종이로 보관하는 분야가 있으며, 회계가 그 예입니다. MarsDawn은 보관이나 규정 준수에 대해 아무것도 주장하지 않습니다. 하는 일은 깔끔하게 페이지가 나뉜 페이지를 프린트하고 내보내는 것입니다. 다이어그램이 그려지고, 짧은 코드 블록과 표는 잘리지 않으며, 테마의 라이트 색상이 쓰입니다. 종이가 여전히 기록인 곳에서 사용하세요.

[PDF 내보내기](/ko/pdf/)

### Markdown을 쓰지 않는 사람에게 전달하기

PDF는 어디서나 열리고 Markdown을 몰라도 되므로, 상사나 고객에게 보내기에도 알맞습니다.

[내보낸 PDF 공유하기](/ko/sharing-exported-pdfs/)

## 쓰기와 레이아웃

### 일반 Markdown, 구문 강조

굵게, 기울임, 취소선, 인라인 코드, 링크, 인용문, 할 일 목록이 모두 작동합니다. 편집기가 Markdown 구문에 색을 입히며, 그 색은 미리보기 테마와 어울립니다.

[Mac 앱](/ko/native/)

### 확대/축소, 행 번호, 상태 막대

소스와 미리보기를 함께 75%에서 200%까지 확대/축소할 수 있습니다. 소스 옆에는 행 번호 여백이 있고, 상태 막대에는 현재 행과 열, 그리고 문서 또는 선택 영역의 단어 수와 글자 수, 읽는 시간이 표시됩니다.

### 이미지

문서를 저장한 다음 편집기에 이미지를 끌어다 놓거나 붙여넣으세요. MarsDawn이 문서 옆의 assets 폴더에 이미지를 복사하고 링크를 작성합니다. 웹 이미지는 이미지 불러오기를 클릭할 때까지 숨겨져 있으므로, 문서를 열어도 읽었다는 사실이 어떤 서버에도 전달되지 않습니다.

[내 글은 내 Mac에](/ko/yours/)

### Front matter는 방해되지 않습니다

파일 맨 위의 front matter 블록은 미리보기와 훑어보기에서 접힌 문서 정보 섹션으로 표시되고, PDF에서는 빠집니다.

### 여덟 가지 언어

앱은 영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어로 제공됩니다.

[Mac 앱](/ko/native/)

## 다이어그램, 코드, 수식

### Mermaid 다이어그램

`mermaid`로 표시한 코드 블록은 다이어그램으로 그려집니다. 다이어그램에 오류가 있으면 미리보기에 소스와 그 아래 오류가 표시되고, 메시지를 클릭하면 해당 줄로 이동합니다.

[Mac에서 Mermaid 미리보기](/ko/mermaid-preview-mac/)

### 구문 강조된 코드

코드 블록은 대부분의 주요 언어에서 구문이 강조됩니다. 여는 ````` 뒤에 언어 이름을 적으세요.

### 수식

KaTeX 구문으로 쓴 수식은 미리보기와 훑어보기에 그려지고, 내보낸 PDF에도 반영됩니다.

[AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](/ko/reviewing-ai-output/)

## 테마, PDF, 프린트

### 네 가지 테마, 라이트와 다크

새벽, 클래식, 모던, 비비드에는 각각 라이트와 다크 버전이 있으며, 설정에서 따로 고르지 않으면 MarsDawn은 Mac의 화면 모드를 따릅니다. 보기 ▸ 미리보기 테마 또는 도구 막대의 팔레트 버튼에서 선택하세요.

[미리보기 테마와 PDF 내보내기](/ko/themes/)

### 더 많은 테마

설정 ▸ 화면 모드 ▸ 테마 더 받기…를 선택하면 추가 미리보기 테마 갤러리가 열립니다. 하나를 설치하면 보기 ▸ 미리보기 테마에 나타나고, 제거를 누르면 다시 없어집니다. 갤러리는 열려 있는 동안에만 온라인에 연결됩니다.

[테마 갤러리](/ko/themes/gallery/) · [테마 만들기](/ko/themes/new/)

### PDF로 내보내기, 또는 프린트

파일 ▸ PDF로 내보내기…는 페이지가 나뉜 PDF를 저장하고, 파일 ▸ 프린트…는 같은 페이지를 프린트합니다. Mermaid 다이어그램이 그려지고, 코드는 구문 강조를 유지하며, 페이지 나눔은 제목을 해당 절에서 떼어 놓거나 짧은 코드 블록, 표, 다이어그램을 반으로 자르지 않도록 피합니다. 다크 모드로 읽고 있었더라도 PDF에는 항상 테마의 라이트 색상이 쓰입니다.

[PDF 내보내기](/ko/pdf/)

![MarsDawn에서 내보낸 PDF를 페이지 축소판과 함께 PDF 뷰어로 연 모습.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

이 스크린샷의 내용:

1. Mermaid 다이어그램이 PDF 안에 그려집니다.
2. 코드는 하이라이트를 유지합니다.

## 파일, 탭, 훑어보기

### 윈도우와 탭

각 문서는 별도의 윈도우에서 열립니다. 윈도우 ▸ 모든 윈도우 통합을 선택하면 열려 있는 윈도우가 한 윈도우의 탭으로 모입니다. 자동 저장은 입력하는 동안 작동합니다.

[Mac 앱](/ko/native/)

### Finder의 훑어보기

Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 다이어그램을 포함해 렌더링된 상태로 읽을 수 있습니다. 훑어보기는 MarsDawn에서 고른 테마를 쓰고, MarsDawn의 화면 모드 설정을 따릅니다.

[Mac 앱](/ko/native/)

### 기타 파일

MarsDawn은 일반 텍스트 파일(`.txt`, `.log`, 소스 코드)과 PDF도 열 수 있습니다. UTF-8 텍스트는 바로 편집할 수 있으며 소스만 표시됩니다. PDF는 페이지 썸네일, 확대/축소, 검색을 지원하는 뷰어에서 열립니다.

### 내 파일은 내 것

계정도, 동기화도, 클라우드도 없습니다. 문서는 저장한 곳에 그대로 있고, MarsDawn은 나에 대한 어떤 데이터도 수집하지 않습니다.

[내 글은 내 Mac에](/ko/yours/)

## 에이전트와 스크립트용

### 무료 명령줄 도구

무료 `marsdawn` 도구는 Homebrew로 따로 설치합니다. `marsdawn export`는 Markdown 파일을 MarsDawn의 미리보기와 같은 모습의 PDF로 만들며, 앱이 필요 없습니다. `--theme`로 테마를, 용지는 A4 또는 Letter를 고를 수 있습니다. `marsdawn open`은 파일을 앱에서 열어 검토할 수 있게 해 주고, 원하면 특정 줄에서 열 수도 있으며, 앱이 설치되어 있어야 합니다.

[명령줄](/ko/cli/)

### 스크립트가 읽을 수 있는 출력

`--json`을 붙이면 두 명령 모두 에이전트나 스크립트가 파싱할 수 있는 결과를 돌려줍니다.

[에이전트를 위한 marsdawn](/ko/cli/agents/)

### 스킬과 MCP 서버

에이전트 스킬 파일은 코딩 에이전트에게 자신이 쓴 것을 MarsDawn에서 열어 검토받도록 가르칩니다. 셸이 없는 클라이언트를 위해서는 별도의 MCP 서버가 같은 export를 실행합니다.

[에이전트 스킬](/ko/cli/skill/) · [MCP 서버](/ko/cli/mcp/)

### 내부에 AI는 없습니다

MarsDawn에는 자체 AI 모델이 없습니다. 에이전트가 쓴 글을 요약하거나 평가하지 않고, 길고 계속 바뀌는 파일을 읽기 좋게 유지해 읽는 일은 내가 하게 합니다.

[MarsDawn이 하지 않는 일](/ko/limits/)

## Siri 및 단축어

단축어 앱에서 MarsDawn을 검색하면 세 가지 동작이 있습니다. 새로운 Markdown 문서(템플릿으로 시작), 수신함에 메모 추가, 최근 사용한 문서 열기입니다. 메모는 MarsDawn ▸ 설정… ▸ 메모 폴더에서 선택한 폴더의 `Inbox.md`에 추가됩니다.

[Mac 앱](/ko/native/)

## Mac에서 사용해 보세요

MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하면 됩니다. 구독도, 계정도 필요 없습니다. macOS 26 이상이 필요합니다.

[지금 다운로드하고 체험하기](https://apps.apple.com/app/id6812925073)

체험 방식: [무료로 체험하고, 한 번만 구입](/ko/pay-once/). 일부러 넣지 않은 것: [MarsDawn이 하지 않는 일](/ko/limits/).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트의 작업을 이끄는 사람을 위한 Markdown. 실시간 미리보기, Mermaid 다이어그램, PDF 내보내기를 갖춘 Mac 네이티브 편집기입니다. Mac App Store에서 구입할 수 있습니다.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지이고, 갤러리에 더 있습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Ein nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid und Formeln, Themes sowie saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Un éditeur Markdown natif pour Mac : aperçu en direct, Mermaid et formules, thèmes, plus des pages PDF et d’impression propres pour les réunions, les notes en marge et les dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Un editor de Markdown nativo para Mac: vista previa en vivo, Mermaid y fórmulas, temas, además de páginas limpias en PDF y para imprimir en reuniones, notas al margen y archivos en papel.
