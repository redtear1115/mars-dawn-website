# Le travail de votre agent revient sous forme de fichier Markdown.

Vous demandez à un agent de code de planifier une migration, de rédiger une spécification ou de traquer un bug. Il travaille seul un moment, puis vous remet un fichier : `plan.md`, `SPEC.md`, un rapport d’avancement, un résumé de recherche. Pour autant que vous puissiez vérifier le travail, ce fichier est le travail.

**Pour savoir si l’agent a vu juste, il faut lire ce qu’il vous rend. MarsDawn est une app Mac pour cette lecture.**

## Ce que disent ceux qui construisent des agents

Citations telles qu’écrites ; notre lecture suit.

- « Building Effective Agents » d’Anthropic (Erik S. et Barry Zhang, décembre 2024) donne trois principes fondamentaux pour construire des agents. L’un d’eux : « Privilégiez la transparence en montrant explicitement les étapes de planification de l’agent. » Ce texte s’adresse à ceux qui construisent des agents. De votre côté, cette transparence, c’est le plan que vous finissez par lire.
- Le même article : « Les agents peuvent alors faire une pause pour obtenir un retour humain à des points de contrôle ou face à un blocage. » Notez le verbe : *peuvent*.
- Chip Huyen, dans « Agents » (janvier 2025), explique pourquoi la planification doit rester séparée de l’exécution : « Sans supervision, un agent peut exécuter ces étapes pendant des heures, gaspillant temps et argent en appels d’API, avant que vous ne vous rendiez compte qu’il n’aboutit à rien. » Elle décrit aussi un échec où « l’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas ». Chargé de loger 50 personnes dans 30 chambres d’hôtel, il en place 40 et affirme avoir terminé.
- Andrew Ng, sur le modèle de conception de la planification, dans The Batch (avril 2024) : « D’un côté, la planification est une capacité très puissante ; de l’autre, elle produit des résultats moins prévisibles. » C’est une remarque sur la prévisibilité, pas un appel à la relecture humaine, et il s’attend à ce que la planification progresse vite.

**Notre déduction, pas la leur :** si un agent expose son plan et s’arrête à des points de contrôle, quelqu’un lit ce plan au point de contrôle, et c’est généralement vous. Si un agent peut se croire fini alors qu’il ne l’est pas, son rapport « terminé » a lui aussi besoin d’un lecteur. Aucun de ces auteurs ne mentionne MarsDawn ni ne le recommande, pas plus qu’aucun autre outil Markdown.

## Pourquoi c’est plus difficile à lire qu’il n’y paraît

Le fichier est long, et la partie importante se trouve rarement en haut. Il contient des diagrammes Mermaid et des formules difficiles à suivre sous forme de source. L’agent est peut-être encore en train de le réécrire alors que vous en êtes à la moitié. C’est souvent un fichier parmi d’autres, parfois répartis sur plusieurs branches ou worktrees. Et quand vous trouvez un problème, « la partie sur le cache a l’air bizarre » laisse l’agent deviner ; « `docs/plan.md:42` supprime l’ancienne table avant la fin du backfill », non.

## Là où MarsDawn aide

- **Fichiers longs :** l’onglet Plan de la barre latérale (⌃⌘S) liste les titres. Cliquez sur l’un d’eux et les deux volets y sautent.
- **Diagrammes et maths :** Mermaid et KaTeX sont dessinés dans l’aperçu à côté de la source (⌘2), et les deux volets défilent ensemble.
- **Réécrit pendant que vous lisez :** quand l’agent réécrit le fichier, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.
- **Plusieurs fichiers :** ouvrez le dossier de l’agent avec Fichier ▸ Ouvrir un dossier… (⇧⌘O). Les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, et pour un checkout git, l’en-tête indique la branche ou le worktree.
- **Un retour précis :** Édition ▸ Copier la référence (⌥⌘C) copie votre position sous la forme `docs/plan.md:42`. Copier pour l’IA (⌃⌥⌘C) ajoute le texte sélectionné en dessous. Collez l’un ou l’autre dans la conversation avec l’agent.

Deux de plus pour la boucle : un agent peut lancer `marsdawn open plan.md:42` pour ouvrir le fichier dans MarsDawn à la ligne 42, celle qu’il veut vous montrer en premier, et un fichier relu s’exporte en PDF depuis l’app ou avec la commande gratuite `marsdawn export`.

MarsDawn n’embarque aucun modèle d’IA. Il ne résume pas le plan, ne le note pas et ne vous dit pas ce qui ne va pas. C’est vous qui lisez ; il garde lisible un fichier long qui change, et vous permet de désigner la ligne exacte.

## Relire le plan d’un agent en cinq minutes

Cela marche dans n’importe quel éditeur.

1. Lisez seulement les titres. Le plan correspond-il à ce que vous avez demandé ? Une section manquante signifie généralement du travail manquant.
2. Repérez chaque endroit qui affirme que quelque chose est fait, réussi ou vérifié, et vérifiez-en un vous-même : ouvrez le fichier, lancez le test, comptez les lignes.
3. Cherchez les étapes irréversibles : suppression de données, migrations, force-push, tout ce qui envoie, paie ou publie. Celles-là attendent votre accord explicite.
4. Lisez les diagrammes rendus, et confrontez chaque flèche au texte.
5. Listez les fichiers et systèmes que le plan touche. Posez des questions sur tout ce que vous n’avez pas demandé avant que cela s’exécute.
6. Rédigez vos retours sous la forme endroit, problème, correction : « `plan.md:88` : le backfill s’exécute après la suppression. Inversez les étapes 4 et 5. » Un problème par ligne.

Peu de temps ? Faites l’étape 2. C’est là qu’on prend en défaut un agent qui se croit fini. La version longue, avec un exemple détaillé : [Relire le plan d’un agent en cinq minutes](/fr/reviewing-agent-plans/).

## Essayer

MarsDawn est sur le [Mac App Store](https://apps.apple.com/app/id6812925073). Il existe aussi l’outil en ligne de commande gratuit `marsdawn` :

```
brew install redtear1115/tap/marsdawn
```

Il exporte le Markdown en PDF sans l’app, et `marsdawn open` permet à votre agent d’ouvrir des fichiers dans MarsDawn pour vous.

[Ligne de commande](/fr/cli/) · [marsdawn pour les agents](/fr/cli/agents/) · À savoir avant d’acheter : [Ce que MarsDawn ne fait pas](/fr/limits/)

## Pour aller plus loin

- L’argument court pour lire ce que produit l’IA : [Pourquoi ce que produit l’IA a toujours besoin d’un lecteur humain](/fr/reviewing-ai-output/).
- Garder le contexte de l’agent réduit pendant la relecture : [une relecture économe en tokens](/fr/token-efficient-review/).
- Pourquoi les agents exposent leurs plans : [Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?](/fr/agent-transparency/)
- La liste ci-dessus, étape par étape avec un exemple : [Relire le plan d’un agent en cinq minutes](/fr/reviewing-agent-plans/).
- Quels documents vous remettent les différents types d’agents : [Quatre modèles de conception d’agents et les documents que chacun vous remet](/fr/agent-design-patterns/).

## Sources

- Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (cité d’après la version en ligne le 26/09/2026 ; l’article précise désormais qu’une grande partie des outils décrits a changé depuis décembre 2024).
- Chip Huyen, « Agents », 7 janvier 2025 : [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, « Agentic Design Patterns Part 4, Planning », The Batch, 10 avril 2024 : [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.
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
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu proposés par la communauté pour MarsDawn, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur, sans installation ni git.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [Notes de lecture de la rédaction](https://marsdawn.southern-light.dev/fr/reading-notes/index.md): Six courtes notes sur ce que les gens qui construisent des agents IA avancent réellement — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain et Andrew Ng — et ce que cela signifie pour la personne qui doit lire ce qu’un tel agent rend.
- [Notes de lecture : Anthropic](https://marsdawn.southern-light.dev/fr/reading-notes/anthropic-building-effective-agents/index.md): Le guide d’Anthropic de décembre 2024 pour qui construit des agents sépare workflows et agents et décrit cinq patrons de workflow, dont un où un second appel LLM relit le premier. Ce que cela signifie pour ce qui atterrit dans votre dossier.
- [Notes de lecture : Chip Huyen](https://marsdawn.southern-light.dev/fr/reading-notes/chip-huyen-agents/index.md): L’essai « Agents » de Chip Huyen de janvier 2025 partage les actions d’un agent en read-only et write. Pourquoi cette distinction est un moyen rapide de repérer, dans un plan, la ligne qui mérite un regard plus attentif avant d’approuver.
- [Notes de lecture : Lilian Weng](https://marsdawn.southern-light.dev/fr/reading-notes/lilian-weng-llm-agents/index.md): L’enquête très citée de Lilian Weng en 2023 décrit un agent LLM comme un cerveau plus planification, mémoire et usage d’outils. Ce que chaque partie tend à vous laisser à lire, et la limite qu’elle nomme dans les plans qui ne s’ajustent pas aux surprises.
- [Notes de lecture : Harrison Chase](https://marsdawn.southern-light.dev/fr/reading-notes/harrison-chase-what-is-an-agent/index.md): La définition d’un agent de Harrison Chase en 2024 et son spectre de comportement agentic, et son plaidoyer pour l’observabilité à mesure qu’un système avance dessus — lu du côté de qui lit le fichier qu’il rend.
- [Notes de lecture : LangChain (Jess Ou)](https://marsdawn.southern-light.dev/fr/reading-notes/langchain-what-is-an-agent/index.md): Le « What is an AI agent ? » de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.
- [Notes de lecture : Andrew Ng](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Español](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
