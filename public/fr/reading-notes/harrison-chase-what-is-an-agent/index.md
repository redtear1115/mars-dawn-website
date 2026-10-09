# Le spectre de Harrison Chase : plus c’est agentic, plus vous voudrez regarder

**En juin 2024, Harrison Chase de LangChain a ouvert une nouvelle série avec une question trompeusement petite — « What is an agent ? » — et y a répondu par une définition technique et un spectre de comportement « agentic ». Plus un système occupe ce spectre, avance-t-il, plus il faut pouvoir voir à l’intérieur pendant qu’il tourne.**

## Ce que le billet avance

La propre définition de Chase, offerte avec la réserve qu’elle est plus technique, et plus large, que l’idée que se font la plupart des gens d’un agent :

> “An agent is a system that uses an LLM to decide the control flow of an application.”

Le control flow, c’est simplement quelle étape un programme lance ensuite. Il admet aussitôt que la définition est imparfaite — un système simple où un LLM route entre deux chemins compte comme agent selon sa définition, mais ne collerait pas à l’intuition de « agent » de la plupart des gens. Plutôt que de se battre sur l’étiquette, il reprend une suggestion d’Andrew Ng, dont il cite et crédite directement le tweet : « rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic. » Le commentaire de Chase : « I really agree with this viewpoint and I think Andrew expressed it nicely. » De là : un système est d’autant plus « agentic » qu’un LLM décide davantage de son comportement, d’un routeur fixe jusqu’à un agent pleinement autonome qui construit et mémorise ses propres outils. Son argument pratique suit de ce spectre — plus un système est agentic, plus certains types d’infrastructure comptent, l’observabilité en tête :

> “You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.”

Il étend cela à l’intervention, pas seulement à l’observation : vous voudrez aussi pouvoir modifier l’état ou les instructions d’un agent en cours à un point donné, pour le ramener sur la voie s’il dérive. Chase ne mentionne MarsDawn nulle part dans ce billet et ne recommande aucun outil Markdown.

## Notre lecture, pas celle de Chase

Chase écrit sur les outils pour qui construit des frameworks d’agents — LangGraph et LangSmith, nommément — pas sur une personne qui lit un document fini. Mais son spectre donne une façon utile de calibrer ce que vous allez lire avant de commencer : plus le système qui a produit un fichier est agentic, moins vous devez vous attendre à ce que ses étapes soient prévisibles à partir du seul prompt, et plus le fichier devant vous mérite d’être traité comme un enregistrement de ce qui s’est vraiment passé plutôt que de ce qui était censé se passer. Son « observe what is going on inside » porte sur l’intérieur d’un système en cours — traces (un journal enregistré de tout ce que l’agent a fait pendant une exécution), étapes intermédiaires, appels d’outils — pas sur la lecture d’un plan Markdown après coup. Mais la raison sous-jacente qu’il donne, que les étapes exactes peuvent ne pas être connues à l’avance, s’applique tout autant au document qu’un agent vous tend une fois terminé : si les étapes n’étaient pas prévisibles en entrée, le rapport en sortie est le seul endroit restant pour les vérifier.

## Où MarsDawn aide, et où non

MarsDawn n’observe pas l’intérieur d’un agent en cours — il n’a aucun modèle d’IA à l’intérieur et aucune connexion au framework qui a produit le fichier, donc il ne peut pas vous dire où sur le spectre de Chase un agent donné se situait. Il travaille sur le document qui atterrit ensuite : l’onglet Plan (Présentation ▸ Afficher la barre latérale, ⌃⌘S) pour la forme d’un long rapport, la source et l’aperçu rendu côte à côte (⌘2) pour les diagrammes et les maths, et le rechargement en direct qui garde votre place quand l’agent réécrit le fichier, tant que vous n’avez pas de modifications non enregistrées — la version au niveau fichier de regarder quelque chose qui bouge encore. Édition ▸ Copier la référence (⌥⌘C) et Copier pour l’IA (⌃⌥⌘C) vous laissent montrer exactement où une étape a dérapé — l’équivalent documentaire de ramener un agent en cours sur la voie.

## Essayer

MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit `marsdawn` fonctionne déjà :

```
brew install redtear1115/tap/marsdawn
```

Il exporte le Markdown en PDF sans l’app.

[Ligne de commande](/fr/cli/) · Avant d’acheter : [Ce que MarsDawn ne fait pas](/fr/limits/)

## Ensuite

- Le traitement plus complet de la transparence et des checkpoints dans cette série : [Anthropic dit que les agents doivent être transparents. Qui lit ce qu’ils exposent ?](/fr/agent-transparency/)
- Le billet LangChain de 2026 à la même adresse, avec une définition presque identique : [Le pipeline d’evals de Jess Ou, et l’étape qui reste encore la vôtre](/fr/reading-notes/langchain-what-is-an-agent/)
- Retour à la série : [Notes de lecture de la rédaction](/fr/reading-notes/)

## Sources

- Harrison Chase, “What is an agent?,” LangChain, June 28, 2024, copie archivée : [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (récupéré et cité le 2026-09-26 via la Wayback Machine ; l’adresse d’origine montre maintenant un article 2026 de Jess Ou).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Éditeur Markdown natif pour Mac : aperçu en direct à côté de la source, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, 4,99 USD une fois.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Quick Look pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Appuyez sur Espace sur un fichier Markdown dans le Finder pour le lire mis en forme, avec diagrammes Mermaid, formules KaTeX et code coloré. Coup d’œil de MarsDawn n’est pas verrouillé par l’essai.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu proposés par la communauté pour MarsDawn, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur, sans installation ni git.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [Notes de lecture de la rédaction](https://marsdawn.southern-light.dev/fr/reading-notes/index.md): Six courtes notes sur ce que les gens qui construisent des agents IA avancent réellement — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain et Andrew Ng — et ce que cela signifie pour la personne qui doit lire ce qu’un tel agent rend.
- [Notes de lecture : Anthropic](https://marsdawn.southern-light.dev/fr/reading-notes/anthropic-building-effective-agents/index.md): Le guide d’Anthropic de décembre 2024 pour qui construit des agents sépare workflows et agents et décrit cinq patrons de workflow, dont un où un second appel LLM relit le premier. Ce que cela signifie pour ce qui atterrit dans votre dossier.
- [Notes de lecture : Chip Huyen](https://marsdawn.southern-light.dev/fr/reading-notes/chip-huyen-agents/index.md): L’essai « Agents » de Chip Huyen de janvier 2025 partage les actions d’un agent en read-only et write. Pourquoi cette distinction est un moyen rapide de repérer, dans un plan, la ligne qui mérite un regard plus attentif avant d’approuver.
- [Notes de lecture : Lilian Weng](https://marsdawn.southern-light.dev/fr/reading-notes/lilian-weng-llm-agents/index.md): L’enquête très citée de Lilian Weng en 2023 décrit un agent LLM comme un cerveau plus planification, mémoire et usage d’outils. Ce que chaque partie tend à vous laisser à lire, et la limite qu’elle nomme dans les plans qui ne s’ajustent pas aux surprises.
- [Notes de lecture : LangChain (Jess Ou)](https://marsdawn.southern-light.dev/fr/reading-notes/langchain-what-is-an-agent/index.md): Le « What is an AI agent ? » de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.
- [Notes de lecture : Andrew Ng](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年對 agent 的定義，以及他自己的 agentic 光譜；他主張系統愉往自主那端走，就愉需要可觀測性——從讀那份檔案的人的角度重新看一遍。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对 agent 的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase による 2024 年のエージェントの定義と、彼自身の agentic なふるまいのスペクトラム。システムがそのスペクトラムを進むほど観測可能性が重要になるという彼の主張を、そのファイルを読む人の側から見直す。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chases Definition eines Agenten von 2024 und sein Spektrum agentischen Verhaltens, und sein Plädoyer für Beobachtbarkeit, je weiter ein System darauf wandert — gelesen von der Seite der Person, die die Datei liest, die er zurückgibt.
- [Español](https://marsdawn.southern-light.dev/es/reading-notes/harrison-chase-what-is-an-agent/index.md): La definición de agente de Harrison Chase de 2024 y su espectro de comportamiento agentic, y su argumento a favor de la observabilidad a medida que un sistema avanza por él — leído desde quien lee el archivo que te devuelve.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
