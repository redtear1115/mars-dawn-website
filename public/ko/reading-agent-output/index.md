# 에이전트의 작업은 Markdown 파일로 돌아옵니다.

코딩 에이전트에게 마이그레이션 계획, 사양서 작성, 버그 추적을 맡깁니다. 에이전트는 한동안 혼자 일한 다음 파일 하나를 건넵니다. `plan.md`, `SPEC.md`, 진행 보고서, 조사 요약. 여러분이 작업을 확인할 수 있는 범위에서는 그 파일이 곧 작업입니다.

**에이전트가 제대로 했는지는 에이전트가 돌려준 것을 읽어 봐야 압니다. MarsDawn은 그 읽기를 위한 Mac 앱입니다.**

## 에이전트를 만드는 사람들이 하는 말

쓰인 그대로 인용하고, 우리의 해석은 그 뒤에 적습니다.

- Anthropic의 “Building Effective Agents”(Erik S., Barry Zhang, 2024년 12월)는 에이전트를 만드는 세 가지 핵심 원칙을 제시합니다. 그중 하나는 “에이전트의 계획 단계를 명시적으로 보여 줌으로써 투명성을 우선하라”입니다. 이 글은 에이전트를 만드는 사람을 위해 쓰였습니다. 여러분 쪽에서 보면 그 투명성은 결국 여러분이 읽게 되는 계획입니다.
- 같은 글에서: “그러면 에이전트는 체크포인트에서 또는 장애물을 만났을 때 사람의 피드백을 받기 위해 멈출 수 있다.” 동사에 주목하세요. *할 수 있다*입니다.
- Chip Huyen은 “Agents”(2025년 1월)에서 계획을 실행과 분리해야 하는 이유를 이렇게 설명합니다. “감독이 없으면 에이전트는 그 단계들을 몇 시간 동안 실행하며 API 호출에 시간과 돈을 낭비할 수 있고, 여러분은 그제야 그것이 아무 데도 가지 못하고 있음을 깨닫는다.” 또 “에이전트가 작업을 끝내지 않았는데도 끝냈다고 확신하는” 실패도 설명합니다. 50명을 호텔 객실 30개에 배정하라고 하면 40명만 배정하고 다 했다고 우깁니다.
- Andrew Ng은 The Batch(2024년 4월)에서 계획 설계 패턴에 대해 이렇게 말합니다. “한편으로 계획은 매우 강력한 능력이지만, 다른 한편으로는 결과를 덜 예측 가능하게 만든다.” 이는 예측 가능성에 관한 지적이지 사람의 검토를 요구하는 말이 아니며, 그는 계획 능력이 빠르게 나아질 것으로 봅니다.

**그들의 말이 아니라 우리의 추론입니다.** 에이전트가 계획을 펼쳐 보이고 체크포인트에서 멈춘다면, 누군가는 그 체크포인트에서 계획을 읽어야 하고, 대개 그 사람은 여러분입니다. 에이전트가 끝나지 않았는데도 끝났다고 생각할 수 있다면, ‘완료’ 보고에도 읽는 사람이 필요합니다. 이 저자들 중 누구도 MarsDawn을 언급하거나 MarsDawn 또는 다른 Markdown 도구를 추천하지 않습니다.

## 보기보다 읽기 어려운 이유

파일은 길고, 중요한 부분은 위쪽에 있는 경우가 드뭅니다. 소스로는 따라가기 어려운 Mermaid 다이어그램과 수식이 들어 있습니다. 여러분이 절반쯤 읽는 동안에도 에이전트가 파일을 고쳐 쓰고 있을 수 있습니다. 여러 파일 중 하나인 경우가 많고, 때로는 여러 브랜치나 워크트리에 흩어져 있습니다. 그리고 문제를 발견했을 때 “캐시 부분이 좀 이상해”라고 하면 에이전트는 짐작할 수밖에 없지만, “`docs/plan.md:42`에서 백필이 끝나기 전에 이전 테이블을 삭제함”이라고 하면 그렇지 않습니다.

## MarsDawn이 돕는 부분

- **긴 파일:** 사이드바의 개요 탭(⌃⌘S)에 제목이 나열됩니다. 하나를 클릭하면 두 패널이 모두 그곳으로 이동합니다.
- **다이어그램과 수식:** Mermaid와 KaTeX가 소스 옆 미리보기에 그려지고(⌘2), 두 패널이 함께 스크롤됩니다.
- **읽는 동안 고쳐 쓰일 때:** 에이전트가 파일을 고쳐 쓰면 MarsDawn이 다시 불러오고 읽던 위치를 유지합니다. 여러분이 저장하지 않은 편집이 없는 한 그렇습니다.
- **여러 파일:** 파일 ▸ 폴더 열기…(⇧⌘O)로 에이전트의 폴더를 여세요. 새 파일은 약 1초 안에 파일 탭에 나타나고, git 체크아웃이라면 헤더에 브랜치나 워크트리 이름이 표시됩니다.
- **정확한 피드백:** 편집 ▸ 참조 복사(⌥⌘C)는 현재 위치를 `docs/plan.md:42` 형식으로 복사합니다. AI용으로 복사(⌃⌥⌘C)는 그 아래에 선택한 텍스트를 덧붙입니다. 어느 쪽이든 에이전트와의 채팅에 붙여 넣으세요.

반복 과정에 쓸 것이 두 가지 더 있습니다. 에이전트는 `marsdawn open plan.md:42`를 실행해 여러분이 가장 먼저 봤으면 하는 42번째 줄에서 MarsDawn으로 파일을 열 수 있고, 검토를 마친 파일은 앱에서 또는 무료 `marsdawn export` 명령으로 PDF로 내보낼 수 있습니다.

MarsDawn 안에는 AI 모델이 없습니다. 계획을 요약하거나, 평가하거나, 무엇이 틀렸는지 알려 주지 않습니다. 읽는 것은 여러분이고, MarsDawn은 길고 계속 바뀌는 파일을 읽기 좋게 유지하며 정확한 줄을 가리킬 수 있게 해 줍니다.

## 에이전트의 계획을 5분 만에 검토하기

어떤 편집기에서든 쓸 수 있는 방법입니다.

1. 제목만 읽으세요. 개요가 요청한 내용과 맞나요? 빠진 섹션은 대개 빠진 작업을 뜻합니다.
2. 무언가가 완료되었다, 통과했다, 확인했다고 말하는 곳을 모두 찾아 하나는 직접 확인하세요. 파일을 열고, 테스트를 실행하고, 행을 세어 보세요.
3. 되돌릴 수 없는 단계를 찾으세요. 데이터 삭제, 마이그레이션, 강제 푸시, 무언가를 보내거나 결제하거나 게시하는 모든 것. 이런 단계는 여러분의 명시적인 승인을 기다려야 합니다.
4. 다이어그램을 렌더링된 상태로 읽고, 화살표 하나하나를 본문과 대조하세요.
5. 계획이 건드리는 파일과 시스템을 나열하세요. 요청하지 않은 것이 있으면 실행되기 전에 물어보세요.
6. 피드백은 위치, 문제, 해결책 순서로 쓰세요. “`plan.md:88`: 백필이 삭제 다음에 실행됨. 4단계와 5단계를 바꿀 것.” 한 줄에 문제 하나씩.

시간이 없다면 2단계만 하세요. 끝났다고 착각하는 에이전트는 거기서 잡힙니다. 실제 예시를 곁들인 긴 버전: [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/).

## 사용해 보기

MarsDawn은 [Mac App Store](https://apps.apple.com/app/id6812925073)에 있습니다. 무료 `marsdawn` 명령줄 도구도 있습니다.

```
brew install redtear1115/tap/marsdawn
```

앱 없이 Markdown을 PDF로 내보내며, `marsdawn open`을 쓰면 에이전트가 여러분 대신 MarsDawn에서 파일을 열 수 있습니다.

[명령줄](/ko/cli/) · [에이전트를 위한 marsdawn](/ko/cli/agents/) · 구입 전에 알아 두세요: [MarsDawn이 하지 않는 일](/ko/limits/)

## 다음

- AI의 결과물을 왜 읽어야 하는지 짧게: [AI의 결과물에 여전히 사람 독자가 필요한 이유](/ko/reviewing-ai-output/).
- 검토하는 동안 에이전트의 컨텍스트를 작게 유지하기: [토큰을 아끼는 검토](/ko/token-efficient-review/).
- 에이전트가 애초에 계획을 펼쳐 보이는 이유: [Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?](/ko/agent-transparency/)
- 위 체크리스트를 예시와 함께 단계별로: [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/).
- 여러 종류의 에이전트가 건네는 문서: [네 가지 에이전트 설계 패턴과 각각이 건네는 문서](/ko/agent-design-patterns/).

## 출처

- Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (2026-09-26 기준 온라인 버전에서 인용. 현재 이 글에는 설명된 도구 중 상당수가 2024년 12월 이후 바뀌었다는 안내가 붙어 있습니다.)
- Chip Huyen, “Agents”, 2025년 1월 7일: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning”, The Batch, 2024년 4월 10일: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 Mermaid 다이어그램, KaTeX 수식, 강조된 코드까지 렌더링된 모습으로 읽을 수 있습니다. MarsDawn의 훑어보기는 체험 기간의 제한을 받지 않습니다.
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
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
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
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Français](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Español](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
