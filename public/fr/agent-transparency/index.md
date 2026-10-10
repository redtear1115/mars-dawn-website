# Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?

En décembre 2024, Anthropic a publié « Building Effective Agents », un guide destiné à ceux qui construisent des agents IA. Son résumé énonce trois principes, dont la transparence. Cet article s’intéresse à l’autre bout de ce principe : dès qu’un agent expose ses étapes, quelqu’un doit les lire.

**La transparence, c’est l’agent qui la fournit. La lecture, c’est vous. Anthropic demande aux concepteurs de montrer les étapes de planification d’un agent ; pour la plupart des personnes qui pilotent un agent de code, ces étapes arrivent dans un fichier Markdown que quelqu’un doit lire au bon moment.**

## Ce que dit le guide

Erik S. et Barry Zhang résument leurs conseils ainsi :

> « Quand nous implémentons des agents, nous essayons de suivre trois principes fondamentaux : garder une conception simple. Privilégier la transparence en montrant explicitement les étapes de planification de l’agent. Soigner l’interface agent-ordinateur (ACI) par une documentation et des tests approfondis des outils. »

Ce sont des principes de conception pour ceux qui construisent des agents, pas des consignes pour la personne qui en utilise un. Le principe demande que les étapes soient montrées. Il ne dit pas qui les lit.

Le même article décrit ce que fait un agent une fois qu’il a une tâche : « Une fois la tâche claire, les agents planifient et agissent de façon autonome, en revenant éventuellement vers l’humain pour obtenir des informations ou un avis. » Et : « Les agents peuvent alors faire une pause pour obtenir un retour humain à des points de contrôle ou face à un blocage. » Regardez les mots *éventuellement* et *peuvent*. Les points de contrôle sont décrits comme quelque chose qu’un agent peut avoir, pas quelque chose qu’il doit avoir.

## L’essentiel de la vérification ne se fait pas par vous

Il est facile d’en exagérer la portée, alors voici ce que le guide place réellement en premier. L’agent se vérifie lui-même face au monde : « Pendant l’exécution, il est crucial que les agents obtiennent à chaque étape une “vérité terrain” de l’environnement (comme les résultats d’appels d’outils ou d’exécution de code) pour évaluer leur progression. » Dans cette phrase, la vérité terrain désigne des résultats de tests et des sorties d’outils. Pas une personne.

Le guide est aussi direct sur le risque : « La nature autonome des agents implique des coûts plus élevés et un risque d’erreurs qui s’accumulent. » Sa réponse : des tests approfondis dans des environnements isolés, avec des garde-fous. Il ne dit pas « lisez plus attentivement ».

Une personne intervient plus loin, dans l’annexe sur les agents de code : « Cependant, si les tests automatisés aident à vérifier le fonctionnement, la relecture humaine reste cruciale pour garantir que les solutions répondent aux exigences plus larges du système. » Cette phrase porte sur du code. Mais le manque qu’elle désigne est familier avec n’importe quel agent : un test peut vous dire que quelque chose fonctionne, pas que c’est ce que vous vouliez.

## Où finissent les étapes

**À partir d’ici, c’est notre lecture, pas celle d’Anthropic.**

Si vous utilisez un agent de code au quotidien, ses étapes de planification n’apparaissent généralement pas dans un tableau de bord. Elles apparaissent sous forme de fichiers : `plan.md`, une liste de tâches à cocher, un fichier d’avancement que l’agent réécrit sans cesse, un résumé à la fin. La transparence, de votre côté, signifie davantage à lire.

Montrer les étapes, c’est la part de l’agent. L’autre part, c’est une personne qui les lit au moment où cela compte : avant que la migration ne s’exécute, avant que la branche ne soit fusionnée, avant que « terminé » ne soit accepté. Un agent qui expose tout dans un fichier de 600 lignes que personne n’ouvre est transparent sur le papier et sans surveillance dans les faits.

Harrison Chase a fait une remarque voisine en 2024, à propos du fonctionnement des frameworks d’agents plutôt que des documents : « Vous voudrez pouvoir observer ce qui se passe à l’intérieur, puisque les étapes exactes ne sont peut-être pas connues à l’avance. » Il parlait d’outillage pour ceux qui construisent des agents. Si c’est vous qui pilotez l’agent, le simple fichier qu’il ne cesse d’écrire est souvent la partie que vous pouvez observer.

Aucun de ces auteurs ne mentionne MarsDawn, et aucun ne le recommande, pas plus qu’aucun autre outil Markdown.

## Pourquoi cette lecture est plus difficile qu’il n’y paraît

Le fichier est long, et ce qui compte se trouve rarement en haut. Le diagramme qui explique la modification est du source Mermaid, pas une image (pour le voir dessiné, consultez [Comment afficher un fichier Markdown sur Mac](/fr/view-markdown-on-mac/)). L’agent réécrit peut-être le fichier alors que vous en êtes à la moitié. Il y a souvent plus d’un fichier, parfois sur différentes branches ou worktrees. Et quand vous repérez un problème, « la partie sur le cache a l’air bizarre » laisse l’agent deviner. La version longue se trouve sur [Lire ce que votre agent vous rend](/fr/reading-agent-output/).

## Ce que MarsDawn apporte, et ce qu’il n’apporte pas

MarsDawn est une app Mac pour cette lecture. Il ne rend pas un agent plus transparent, et il n’embarque aucun modèle d’IA : il ne résumera pas le plan et ne vous dira pas s’il est juste. Ce qu’il fait :

- **Fichiers longs :** Présentation ▸ Afficher la barre latérale (⌃⌘S) ouvre l’onglet Plan, qui liste les titres. Cliquez sur l’un d’eux pour y sauter.
- **Diagrammes et maths :** la source et la page rendue sont côte à côte (⌘2) et défilent ensemble, avec Mermaid et KaTeX dessinés. Si un diagramme est cassé, l’aperçu affiche sa source avec l’erreur en dessous.
- **Réécrit pendant que vous lisez :** quand l’agent réécrit le fichier, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.
- **Plusieurs fichiers :** ouvrez le dossier de l’agent avec Fichier ▸ Ouvrir un dossier… (⇧⌘O). Les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, et pour un checkout git, l’en-tête indique la branche ou le worktree.
- **Désigner une ligne :** Édition ▸ Copier la référence (⌥⌘C) copie votre position sous la forme `docs/plan.md:42`, et Copier pour l’IA (⌃⌥⌘C) ajoute le texte sélectionné en dessous, prêt à coller dans la conversation avec l’agent.

C’est toujours vous qui lisez. MarsDawn garde lisible un fichier long qui change pendant que vous le faites.

## Essayer

MarsDawn est sur le [Mac App Store](https://apps.apple.com/app/id6812925073). Il existe aussi l’outil en ligne de commande gratuit `marsdawn` :

```
brew install redtear1115/tap/marsdawn
```

Il exporte le Markdown en PDF sans l’app.

[Ligne de commande](/fr/cli/) · À savoir avant d’acheter : [Ce que MarsDawn ne fait pas](/fr/limits/)

## Pour aller plus loin

- Pourquoi ce que rend un agent est difficile à lire, avec une liste de vérification : [Lire ce que votre agent vous rend](/fr/reading-agent-output/).
- La liste, étape par étape avec un exemple : [Relire le plan d’un agent en cinq minutes](/fr/reviewing-agent-plans/).
- Quels documents vous remettent les différents types d’agents : [Quatre modèles de conception d’agents et les documents que chacun vous remet](/fr/agent-design-patterns/).
- L’argument court pour lire ce que produit l’IA : [Pourquoi ce que produit l’IA a toujours besoin d’un lecteur humain](/fr/reviewing-ai-output/).

## Sources

- Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (cité d’après la version en ligne le 26/09/2026 ; l’article précise désormais qu’une grande partie des outils décrits a changé depuis décembre 2024).
- Harrison Chase, « What is an agent? », LangChain, 28 juin 2024, copie archivée : [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (l’adresse d’origine affiche désormais un autre article, de 2026).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Éditeur Markdown natif pour Mac : aperçu en direct à côté de la source, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, 4,99 USD une fois.
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
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Español](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
