# Quatre modèles de conception d’agents et les documents que chacun vous remet

En mars 2024, Andrew Ng a décrit dans sa newsletter, The Batch, quatre modèles de conception pour les agents IA : la réflexion, l’utilisation d’outils, la planification et la collaboration multi-agents. On les aborde généralement du point de vue de ceux qui construisent les agents, comme des moyens d’obtenir de meilleurs résultats d’un modèle. Cet article se place de l’autre côté. Si vous utilisez un agent fondé sur l’un de ces modèles, qu’est-ce qui atterrit dans votre dossier, et que devez-vous lire en premier ?

**Les quatre modèles sont d’Andrew Ng. Les documents que chacun tend à vous remettre, et ce qu’il faut y vérifier, relèvent de notre propre déduction. Il n’écrit sur aucun des deux points, et il ne plaide pas pour la relecture humaine dans cette série.**

## Les quatre modèles, en bref

Ng les décrit dans « Agentic Design Patterns Part 1 ». En résumé : avec la **réflexion**, le modèle relit son propre travail et l’améliore. Avec l’**utilisation d’outils**, il peut appeler des outils comme la recherche web ou l’exécution de code. Avec la **planification**, il élabore un plan en plusieurs étapes et l’exécute. Avec la **collaboration multi-agents**, plusieurs agents se répartissent le travail et en discutent.

Dans la partie 1, il montre le gain sur un benchmark de code, HumanEval, avec des résultats que son équipe a rassemblés auprès de plusieurs groupes de recherche : « GPT-3.5 (zero-shot) obtenait 48,1 % de réponses correctes. GPT-4 (zero-shot) fait mieux, avec 67,0 %. Cependant, le progrès de GPT-3.5 à GPT-4 est éclipsé par l’intégration d’un workflow agentique itératif. De fait, intégré à une boucle d’agent, GPT-3.5 atteint jusqu’à 95,1 %. » Ces chiffres portent sur un seul benchmark de code, et 95,1 % est le meilleur cas (« jusqu’à »). Ils montrent que les workflows d’agents peuvent améliorer le résultat. Ils ne disent rien de qui le vérifie.

**À partir d’ici, les documents et les vérifications sont notre lecture, pas celle de Ng.** Les vrais agents mélangent d’ailleurs les modèles. Un agent de code peut planifier, lancer des outils et relire son propre travail dans une même session : vous recevrez donc souvent les quatre types de fichiers.

## 1. Réflexion : un brouillon qui s’est déjà relu

L’article de Ng sur la réflexion la présente comme l’automatisation du retour qu’une personne donnerait sinon : « Et si l’on automatisait l’étape du retour critique, pour que le modèle critique automatiquement sa propre sortie et améliore sa réponse ? »

**Ce qu’il tend à vous remettre :** un document révisé, parfois avec une section d’autoévaluation ou des lignes comme « cas limites revérifiés ».

**Ce qu’il faut vérifier :** le résultat par rapport à *votre* demande, pas par rapport à l’autocritique de l’agent. L’autoévaluation peut se tromper à sa façon. Chip Huyen : « Un mode intéressant d’échec de planification provient d’erreurs de réflexion. L’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas. » Lilian Weng, sur son blog Lil’Log en juin 2023, alors chez OpenAI, à propos des modèles de l’époque : « Le manque d’expertise peut empêcher les LLM de connaître leurs défauts, et donc de bien juger de la justesse des résultats d’une tâche. » (Dans l’étude qu’elle décrivait, l’évaluation des résultats par un LLM et celle d’experts humains ne concordaient pas.) S’il est écrit « vérifié », vérifiez une chose vous-même.

## 2. Utilisation d’outils : un compte rendu de ce qui a tourné

**Ce qu’il tend à vous remettre :** un résumé de ce que l’agent a lancé ou recherché et de ce qui en est ressorti. « Suite de tests lancée : tout passe. » Un tableau de résultats. Des liens trouvés.

Le guide d’Anthropic présente les résultats d’outils comme la vérification que l’agent fait de lui-même : « Pendant l’exécution, il est crucial que les agents obtiennent à chaque étape une “vérité terrain” de l’environnement (comme les résultats d’appels d’outils ou d’exécution de code) pour évaluer leur progression. » Cette vérification se fait à l’intérieur de l’agent. Ce qui vous parvient, c’est le récit qu’il en fait.

**Ce qu’il faut vérifier :** que chaque affirmation remonte à une sortie que vous pouvez voir. Comparez un chiffre du résumé à la vraie sortie. Ouvrez l’un des liens.

## 3. Planification : `plan.md`

**Ce qu’il tend à vous remettre :** un plan, une spécification, une liste de tâches que l’agent coche au fur et à mesure.

Ng est franc sur ce modèle dans la partie 4 :

> « D’un côté, la planification est une capacité très puissante ; de l’autre, elle produit des résultats moins prévisibles. D’après mon expérience, si j’arrive à faire fonctionner de façon fiable les modèles agentiques de réflexion et d’utilisation d’outils et à améliorer ainsi les performances de mes applications, la planification est une technologie moins mûre, et j’ai du mal à prévoir à l’avance ce qu’elle va faire. »

Il est aussi optimiste : « Mais le domaine continue d’évoluer rapidement, et je suis convaincu que les capacités de planification vont progresser vite. »

**Ce qu’il faut vérifier :** le plan avant qu’il ne s’exécute, avec [la relecture en cinq minutes](/fr/reviewing-agent-plans/) : structure, une affirmation, étapes irréversibles, diagrammes, périmètre. Si l’agent réécrit le plan en cours de route, comparez-le à la version que vous avez approuvée ; s’il est dans git, `git diff plan.md` montre ce qui a changé. Dans MarsDawn, l’onglet Plan montre la structure d’un long plan, et un plan réécrit se recharge sans vous faire perdre votre position, tant que vous n’avez pas de modifications non enregistrées.

## 4. Collaboration multi-agents : plusieurs fichiers, plusieurs auteurs

**Ce qu’il tend à vous remettre :** une spécification d’un agent, des notes d’implémentation d’un deuxième, une relecture d’un troisième, et des résumés qui circulent entre eux. Parfois, chacun travaille dans sa propre branche ou son propre worktree.

**Ce qu’il faut vérifier :** les passations. Là où un agent résume le travail d’un autre, cherchez une exigence qui ne serait pas passée. Cherchez deux fichiers qui se contredisent, et décidez lequel fait foi avant que quiconque ne s’appuie sur l’autre. Dans MarsDawn, ouvrez le dossier partagé avec Fichier ▸ Ouvrir un dossier… (⇧⌘O) : les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, à mesure que les agents les écrivent, et pour un checkout git, l’en-tête indique la branche ou le worktree, pour que deux fenêtres affichant le même nom de fichier sur des branches différentes ne se ressemblent pas. Quand le résultat doit parvenir à des personnes qui ne lisent pas le Markdown, [Partager des PDF exportés](/fr/sharing-exported-pdfs/) couvre cette étape.

## En un coup d’œil

| Modèle (Ng) | Ce qu’il tend à vous remettre (notre déduction) | À lire en premier (notre suggestion) |
|---|---|---|
| Réflexion | Un brouillon révisé, peut-être avec une autoévaluation | Le résultat par rapport à votre demande ; vérifier un « vérifié » |
| Utilisation d’outils | Un compte rendu de ce qui a tourné et de ce qui en est ressorti | Une affirmation remontée jusqu’à la vraie sortie |
| Planification | `plan.md`, une spécification, une liste de tâches | La relecture en cinq minutes, avant l’exécution |
| Collaboration multi-agents | Plusieurs fichiers de plusieurs agents, peut-être sur plusieurs branches | Les passations, et le fichier qui fait foi |

Aucun des auteurs cités ici ne mentionne MarsDawn, et aucun ne le recommande, pas plus qu’aucun autre outil Markdown. MarsDawn n’embarque aucun modèle d’IA : il ne sait pas quel modèle a produit un fichier, et il ne fera pas ces vérifications à votre place. Il garde les fichiers lisibles pendant que vous les faites.

## Essayer

MarsDawn est sur le [Mac App Store](https://apps.apple.com/app/id6812925073). Il existe aussi l’outil en ligne de commande gratuit `marsdawn` :

```
brew install redtear1115/tap/marsdawn
```

Il exporte le Markdown en PDF sans l’app : voir [Markdown en PDF](/fr/markdown-to-pdf/).

[Ligne de commande](/fr/cli/) · À savoir avant d’acheter : [Ce que MarsDawn ne fait pas](/fr/limits/)

## Pour aller plus loin

- Pourquoi ce que rend un agent est difficile à lire, avec une liste de vérification : [Lire ce que votre agent vous rend](/fr/reading-agent-output/).
- La vérification du plan en entier : [Relire le plan d’un agent en cinq minutes](/fr/reviewing-agent-plans/).
- Ce que la transparence vous demande, et ce qu’elle ne vous demande pas : [Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?](/fr/agent-transparency/)

## Sources

- Andrew Ng, « Agentic Design Patterns Part 1 », The Batch, 20 mars 2024 : [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, « Agentic Design Patterns Part 2, Reflection », The Batch, 27 mars 2024 : [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, « Agentic Design Patterns Part 4, Planning », The Batch, 10 avril 2024 : [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, « Agents », 7 janvier 2025 : [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, « LLM Powered Autonomous Agents », Lil’Log, 23 juin 2023 : [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (cité d’après la version en ligne le 26/09/2026).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. D’autres thèmes importables et une galerie pour partager les vôtres sont prévus.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Español](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
