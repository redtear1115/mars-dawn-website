# 에이전트 디자인 패턴 네 가지와 각각이 넘기는 문서

2024년 3월, Andrew Ng은 자신의 뉴스레터 The Batch에서 AI 에이전트의 디자인 패턴 네 가지를 소개했습니다. 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업입니다. 이 패턴들은 보통 에이전트를 만드는 쪽의 시각에서, 모델에서 더 나은 결과를 끌어내는 방법으로 설명됩니다. 이 글은 반대편에서 봅니다. 이런 패턴으로 만들어진 에이전트를 쓴다면, 폴더에는 무엇이 들어오고, 무엇부터 읽어야 할까요?

**네 가지 패턴은 Andrew Ng의 것입니다. 각 패턴이 보통 넘기는 문서와 그 안에서 확인할 점은 저희의 추론입니다. 그는 둘 중 어느 것에 대해서도 쓰지 않았고, 이 시리즈에서 사람의 검토를 주장하지도 않습니다.**

## 네 가지 패턴 간단히 보기

Ng은 “Agentic Design Patterns Part 1”에서 이 패턴들을 설명합니다. 요약하면 이렇습니다. **리플렉션**에서는 모델이 자기 작업을 검토하고 개선합니다. **도구 사용**에서는 웹 검색이나 코드 실행 같은 도구를 호출할 수 있습니다. **계획**에서는 여러 단계의 계획을 세워 실행합니다. **멀티 에이전트 협업**에서는 여러 에이전트가 일을 나누고 논의합니다.

Part 1에서 그는 코딩 벤치마크 HumanEval에서의 향상을, 그의 팀이 여러 연구 그룹에서 모은 결과로 보여 줍니다. “GPT-3.5(zero-shot)는 48.1%를 맞혔습니다. GPT-4(zero-shot)는 67.0%로 더 낫습니다. 그러나 GPT-3.5에서 GPT-4로의 향상은 반복적인 에이전트 워크플로를 도입했을 때의 향상에 비하면 미미합니다. 실제로 에이전트 루프로 감싸면 GPT-3.5는 최대 95.1%를 달성합니다.” 이 수치는 코딩 벤치마크 하나에 대한 것이고, 95.1%는 최선의 경우(“최대”)입니다. 에이전트 워크플로가 결과물을 개선할 수 있다는 것을 보여 줄 뿐, 그것을 누가 확인하는지에 대해서는 아무것도 말하지 않습니다.

**여기서부터 문서와 확인 사항은 Ng이 아니라 저희의 해석입니다.** 또한 실제 에이전트는 여러 패턴을 섞어 씁니다. 코딩 에이전트는 한 세션 안에서 계획을 세우고, 도구를 실행하고, 자기 작업을 검토하기도 하므로 네 종류의 파일을 모두 받게 되는 경우가 많습니다.

## 1. 리플렉션: 이미 스스로 검토를 거친 초안

리플렉션에 관한 Ng의 글은 이 패턴을, 원래라면 사람이 했을 피드백을 자동화하는 것으로 설명합니다. “비판적 피드백을 주는 단계를 자동화해서, 모델이 자기 출력을 자동으로 비판하고 응답을 개선하게 하면 어떨까요?”

**보통 넘기는 것:** 수정된 문서. 때로는 자기 평가 섹션이나 “엣지 케이스를 다시 확인함” 같은 문장이 붙어 있습니다.

**확인할 점:** 에이전트의 자기 비판이 아니라 *여러분의* 요청과 결과를 비교하세요. 자기 평가도 나름의 방식으로 틀릴 수 있습니다. Chip Huyen은 이렇게 말합니다. “흥미로운 계획 실패 유형 하나는 리플렉션의 오류에서 비롯됩니다. 에이전트가 작업을 완료하지 않았는데도 완료했다고 확신하는 것입니다.” 당시 OpenAI에 있던 Lilian Weng은 2023년 6월 블로그 Lil’Log에서 그 시기의 모델에 대해 이렇게 썼습니다. “전문 지식이 부족하면 LLM은 자기 결함을 알지 못하고, 따라서 작업 결과가 옳은지 제대로 판단하지 못할 수 있습니다.” (그가 소개한 연구에서는 LLM의 결과 평가와 인간 전문가의 평가가 일치하지 않았습니다.) “확인됨”이라고 쓰여 있다면, 하나는 직접 확인하세요.

## 2. 도구 사용: 무엇을 실행했는지에 대한 보고

**보통 넘기는 것:** 에이전트가 무엇을 실행하거나 검색했고 무엇이 나왔는지에 대한 요약. “테스트 스위트를 실행함: 모두 통과.” 결과 표. 찾아낸 링크들.

Anthropic의 가이드는 도구 결과를 에이전트가 스스로를 확인하는 수단으로 설명합니다. “실행 중에는 에이전트가 진행 상황을 평가하기 위해 각 단계에서 환경으로부터 ‘실측 정보’(도구 호출 결과나 코드 실행 등)를 얻는 것이 중요합니다.” 그 확인은 에이전트 내부에서 일어납니다. 여러분에게 도착하는 것은 그에 대한 에이전트의 설명입니다.

**확인할 점:** 모든 주장이 여러분이 볼 수 있는 출력으로 거슬러 올라가는지. 요약에 있는 숫자 하나를 실제 출력과 비교하세요. 링크 하나를 열어 보세요.

## 3. 계획: `plan.md`

**보통 넘기는 것:** 계획, 명세, 에이전트가 하나씩 체크해 나가는 작업 목록.

Ng은 Part 4에서 이 패턴에 대해 솔직하게 말합니다.

> “한편으로 계획은 매우 강력한 능력이지만, 다른 한편으로는 결과를 예측하기 어렵게 만듭니다. 제 경험상 리플렉션과 도구 사용이라는 에이전트 디자인 패턴은 안정적으로 작동시켜 애플리케이션의 성능을 높일 수 있지만, 계획은 아직 덜 성숙한 기술이라 그것이 무엇을 할지 미리 예측하기가 어렵습니다.”

그는 낙관적이기도 합니다. “하지만 이 분야는 계속 빠르게 발전하고 있으며, 계획 능력도 빠르게 향상될 것이라고 확신합니다.”

**확인할 점:** 실행되기 전의 계획. [5분 검토법](/ko/reviewing-agent-plans/)으로 구조, 주장 하나, 되돌릴 수 없는 단계, 다이어그램, 범위를 확인하세요. 에이전트가 도중에 계획을 다시 쓰면 승인한 버전과 비교하세요. git으로 관리 중이라면 `git diff plan.md`로 무엇이 바뀌었는지 볼 수 있습니다. MarsDawn에서는 개요 탭으로 긴 계획의 구조를 볼 수 있고, 다시 쓰인 계획은 저장하지 않은 변경 사항이 없는 한 읽던 위치를 잃지 않고 다시 불러옵니다.

## 4. 멀티 에이전트 협업: 여러 파일, 여러 작성자

**보통 넘기는 것:** 한 에이전트의 명세, 다른 에이전트의 구현 노트, 세 번째 에이전트의 검토, 그리고 그 사이를 오가는 요약. 각자 자기 브랜치나 worktree에서 작업하기도 합니다.

**확인할 점:** 인계 지점. 한 에이전트가 다른 에이전트의 작업을 요약한 곳에서 빠진 요구 사항이 없는지 찾아보세요. 서로 모순되는 두 파일을 찾고, 누군가 다른 쪽을 바탕으로 작업하기 전에 어느 쪽이 기준인지 정하세요. MarsDawn에서 파일 ▸ 폴더 열기…(⇧⌘O)로 공유 폴더를 열면, 에이전트가 새 파일을 쓰는 대로 1초 정도 안에 파일 탭에 나타나고, git 체크아웃에서는 헤더에 브랜치나 worktree가 표시되므로 서로 다른 브랜치에서 같은 이름의 파일을 연 두 창이 똑같아 보이지 않습니다. Markdown을 읽지 않는 사람들에게 결과를 전달해야 한다면 [내보낸 PDF 공유하기](/ko/sharing-exported-pdfs/)에서 그 단계를 다룹니다.

## 한눈에 보기

| 패턴(Ng) | 보통 넘기는 것(저희의 추론) | 먼저 읽을 것(저희의 제안) |
|---|---|---|
| 리플렉션 | 수정된 초안, 경우에 따라 자기 평가 포함 | 요청 대비 결과, “확인됨” 하나 직접 검증 |
| 도구 사용 | 무엇을 실행했고 무엇이 나왔는지에 대한 보고 | 주장 하나를 실제 출력까지 추적 |
| 계획 | `plan.md`, 명세, 작업 목록 | 실행 전 5분 검토 |
| 멀티 에이전트 협업 | 여러 에이전트의 여러 파일, 경우에 따라 여러 브랜치 | 인계 지점과 기준이 되는 파일 |

여기 인용된 저자 중 누구도 MarsDawn을 언급하거나 추천하지 않으며, 다른 어떤 Markdown 도구도 추천하지 않습니다. MarsDawn에는 AI 모델이 들어 있지 않습니다. 어떤 모델이 파일을 만들었는지 알지 못하고, 이런 확인을 대신 해 주지도 않습니다. 여러분이 확인하는 동안 파일을 읽기 쉽게 유지해 줄 뿐입니다.

## 사용해 보기

MarsDawn은 [Mac App Store](https://apps.apple.com/app/id6812925073)에 있습니다. 무료 명령줄 도구 `marsdawn`도 있습니다.

```
brew install redtear1115/tap/marsdawn
```

앱 없이 Markdown을 PDF로 내보냅니다. [Markdown을 PDF로](/ko/markdown-to-pdf/)를 참고하세요.

[명령줄](/ko/cli/) · 구매 전에 알아 두세요: [MarsDawn이 하지 않는 것](/ko/limits/)

## 더 읽어 보기

- 에이전트가 넘긴 결과물이 읽기 어려운 이유와 체크리스트: [에이전트가 넘긴 결과물 읽기](/ko/reading-agent-output/)
- 계획 확인의 전체 과정: [에이전트의 계획을 5분 안에 검토하는 법](/ko/reviewing-agent-plans/)
- 투명성이 여러분에게 요구하는 것과 요구하지 않는 것: [Anthropic은 투명한 에이전트를 원합니다. 그런데 드러낸 것은 누가 읽을까요?](/ko/agent-transparency/)

## 출처

- Andrew Ng, “Agentic Design Patterns Part 1”, The Batch, 2024년 3월 20일: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, “Agentic Design Patterns Part 2, Reflection”, The Batch, 2024년 3월 27일: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, “Agentic Design Patterns Part 4, Planning”, The Batch, 2024년 4월 10일: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, “Agents”, 2025년 1월 7일: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, “LLM Powered Autonomous Agents”, Lil’Log, 2023년 6월 23일: [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (2026년 9월 26일 기준 온라인 버전에서 인용)

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트의 작업을 이끄는 사람을 위한 Markdown. 실시간 미리보기, Mermaid 다이어그램, PDF 내보내기를 갖춘 Mac 네이티브 편집기입니다. Mac App Store에서 구입할 수 있습니다.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지이고, 갤러리에 더 있습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
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
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
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
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Français](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Español](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
