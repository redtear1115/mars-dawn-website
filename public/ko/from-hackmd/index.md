# HackMD에서 Mac으로

노트는 이미 Markdown이므로 변환할 필요가 없습니다. 옮길 양에 맞춰 방법을 고르세요. 이미지는 따로 처리해야 하니, HackMD에서 무엇이든 삭제하기 전에 ‘이미지’ 부분을 읽어 보세요.

이 페이지는 2026년 11월에 HackMD 무료 계정으로 확인한 내용입니다. HackMD는 바뀔 수 있으며, 유료 요금제와 팀 워크스페이스는 확인하지 않았습니다.

| 하고 싶은 일 | 방법 |
|---|---|
| 노트를 모두 옮기기 | 모든 노트 다운로드 |
| GitHub에 있는 노트 옮기기 | 저장소 clone |
| 한두 개만 옮기기 | 노트 하나 다운로드 |

## 모든 노트 다운로드

HackMD의 노트 설정에 Download all notes가 있습니다. 개인 공간과 팀 공간 모두에서 쓸 수 있습니다. 노트마다 .md 파일이 하나씩 든 .zip 파일 하나를 받게 되며, 파일 이름은 노트 제목입니다.

- 폴더는 유지되지 않습니다. 모든 노트가 최상위에 들어갑니다.
- 이미지는 포함되지 않습니다. .md 안에는 URL이 그대로 남습니다.
- 제목과 태그를 포함하는 옵션은 기본으로 켜져 있으며, 각 노트 맨 앞에 front matter 블록을 추가합니다. 끄면 노트 원문과 같습니다.

압축을 푼 뒤 MarsDawn에서 파일 ▸ 폴더 열기…를 선택해 그 폴더를 엽니다.

## 저장소 clone

HackMD의 GitHub 동기화는 노트 하나를 파일 하나에 연결합니다. 푸시한 노트는 이미 저장소에 있습니다. clone한 뒤 파일 ▸ 폴더 열기…로 열면 사이드바에 저장소와 브랜치가 표시됩니다.

아직 GitHub에 연결하지 않은 노트는 옮기려고 일부러 연결할 필요가 없습니다. 노트마다 따로 연결해야 하고, 무료 요금제의 푸시는 한 달에 20번까지입니다. 무료 개인 계정에서는 워크스페이스 전체를 한 번에 푸시하는 방법을 찾지 못했습니다.

옮긴 뒤에는 저장소를 원본으로 삼으세요. HackMD에서 푸시하면 GitHub의 내용을 그대로 덮어씁니다. GitHub 쪽이 더 최신이어도 마찬가지이며, 경고도 없습니다.

## 노트 하나 다운로드

노트 메뉴에서 .md나 .html로 내려받을 수 있습니다. .md를 선택해 MarsDawn에서 여세요.

## 이미지

HackMD에 올린 이미지의 주소는 `https://hackmd.io/_uploads/...`입니다. 누가 볼 수 있는지는 노트의 권한을 따릅니다.

| 노트 | Mac으로 옮긴 뒤 | 처리 방법 |
|---|---|---|
| 공개 | 이미지를 HackMD에서 불러옵니다 | 미리보기에서 이미지 불러오기를 클릭하거나, 설정 ▸ 이미지 ▸ 원격 이미지 자동으로 불러오기를 켜세요 |
| 비공개 | MarsDawn이 HackMD에 로그인되어 있지 않아 이미지가 오류를 냅니다 | 로그인한 브라우저에서 이미지를 저장해 .md 옆에 두고 경로를 바꾸세요. 모두가 봐도 된다면 노트를 공개로 바꿔도 됩니다 |

- **오래된 노트** 의 이미지는 `i.imgur.com` 주소일 수 있습니다.
- **노트를 삭제하면 이미지도 쓸 수 없게 됩니다.** 주소가 더 이상 열리지 않으니, 이미지를 먼저 옮기세요.

파일 옆의 이미지를 MarsDawn이 읽지 못하면, 미리보기의 버튼으로 그 폴더에 접근을 허용하세요.

## 어떻게 보이나요

HackMD 문법은 대부분 그대로 읽을 수 있습니다. `==강조==`, `^위첨자^`, `~아래첨자~`, `[TOC]`, `=300x200` 같은 이미지 크기, Mermaid, KaTeX를 지원합니다. `{%youtube %}`는 링크로 표시됩니다. HackMD처럼 모든 줄바꿈을 유지하려면 설정 ▸ 화면 모드 ▸ 단일 줄 바꿈 유지를 켜세요.

`:::` 블록도 지원합니다. `:::info`, `:::success`, `:::warning`, `:::danger`는 색 막대와 제목이 있는 블록으로 표시되며, 제목 기본값은 참고, 팁, 경고, 위험입니다. 이름 뒤에 제목을 직접 쓰면 그 제목이 쓰입니다. `:::spoiler`는 클릭하면 열리는 접을 수 있는 블록으로 표시됩니다. 다른 이름의 `:::` 블록이나 닫는 `:::` 줄이 없는 블록은 쓴 그대로 표시됩니다.

몇 가지는 다르게 보입니다.

- `++밑줄++`과 `:sparkles:` 같은 이모지 코드는 쓴 그대로 표시됩니다.
- `{%hackmd id %}`는 펼쳐지지 않습니다.
- `<i class="fa ...">` 아이콘은 표시되지 않습니다.

## 스크립트로: hackmd-cli

`hackmd-cli`에는 모든 노트를 한 번에 내보내는 명령이 없습니다. 한 번에 노트 하나를 내보내 화면에 출력하므로, 노트 목록을 뽑은 뒤 반복문을 돌려야 합니다. Node.js, `jq`, HackMD 설정에서 만든 API 토큰이 필요합니다. 스크립트가 필요 없다면 Download all notes가 더 간단합니다.

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<내 토큰>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **폴더는 옮겨지지 않습니다.** 노트 목록에 폴더 정보가 없어서 모든 파일이 한곳에 들어갑니다.
- **이미지는 `hackmd.io` 링크 그대로입니다.** 위의 ‘이미지’ 부분대로 처리하세요.
- **파일 이름은 노트 ID입니다.** 제목이 아닙니다.
- **무료 요금제의 API는 30일에 400번까지입니다.** 목록에 1번, 노트 하나마다 1번 씁니다.

노트가 적은 계정에서만 시도해 봤기 때문에, 목록이 아주 길 때 어떻게 되는지는 모릅니다. 끝나면 HackMD 설정에서 토큰을 삭제하세요.

## 함께 쓰려면

MarsDawn에는 여러 사람이 동시에 편집하는 기능이 없습니다. 함께 써야 한다면 HackMD를 계속 쓰세요. 팀이 문서를 git으로 관리한다면 각자 자기 MarsDawn으로 같은 저장소를 열어 같은 문서를 함께 완성할 수 있습니다. 팀이 git으로 문서 함께 검토하기를 참고하세요.

## 자주 묻는 질문

### HackMD 노트를 한 번에 모두 내려받을 수 있나요?

네. Download all notes를 쓰면 .md 파일이 든 .zip 파일 하나를 받습니다. 폴더는 유지되지 않고 이미지도 포함되지 않습니다.

### MarsDawn에서 이미지가 보이지 않는 이유는 무엇인가요?

MarsDawn은 웹 이미지를 기본으로 불러오지 않습니다. 이미지 불러오기를 클릭하세요. 비공개 노트의 이미지는 불러올 수 없으니 파일 옆에 저장하세요.

### HackMD를 꼭 떠나야 하나요?

아닙니다. 함께 쓸 때는 HackMD가 여전히 더 좋은 선택입니다. MarsDawn은 Mac에서 읽고 검토하기 위한 앱입니다.

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown, JSON, YAML을 검토하는 Mac 네이티브 앱. 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료 체험 후 한 번만 USD 4.99.
- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown, JSON, YAML 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 회의와 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [프린트 및 PDF](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 미리 본 뒤 Markdown을 프린트하거나 PDF로 저장하세요. 문서·설명서·프린트물 레이아웃을 지원하고 다이어그램과 코드 색도 그대로 남습니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone·iPad에서의 편집도, 플러그인도, 계정도 없습니다. 테마는 바꿀 수 있지만 사용자 지정 CSS는 없습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [AI용으로 복사](https://marsdawn.southern-light.dev/ko/copy-for-ai/index.md): 선택한 텍스트를 파일 경로, 줄 번호와 함께 복사해 Claude Code나 다른 에이전트에 붙여 넣습니다. Mac에서 바로 되며, IDE도 플러그인도 필요 없습니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다(MarsDawn의 PDF 칸은 2026년 11월 7일에 업데이트). 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [Mac용 Markdown 뷰어 추천 (2026)](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [테마](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크를 각각 갖춘 기본 미리보기 테마 네 가지와, Mac용 MarsDawn 설정에서 여는 엄선된 테마 갤러리. 훑어보기도 고른 테마를 씁니다.
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
- [English](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/from-hackmd/index.md): Lade deine HackMD-Notizen als .md herunter und lies sie in MarsDawn auf dem Mac. Alle Notizen herunterladen, ein GitHub-Repository nutzen und Bilder retten.
- [Français](https://marsdawn.southern-light.dev/fr/from-hackmd/index.md): Téléchargez vos notes HackMD en .md et lisez-les dans MarsDawn sur votre Mac. Comment tout télécharger, partir d’un dépôt GitHub et garder vos images.
- [Español](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
