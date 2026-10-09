Des outils de pionnier pour ceux qui construisent

# Prenez la carte. Lisez l’aube.

Du Markdown pour les humains qui pilotent le travail des agents.

MarsDawn est un éditeur Markdown natif pour macOS avec aperçu en direct à côté de la source, diagrammes Mermaid, formules KaTeX, Coup d’œil (Quick Look) et export PDF, à essayer gratuitement 14 jours puis à déverrouiller une fois pour 4,99 USD.

La page montre une fenêtre MarsDawn interactive qui affiche un extrait du guide de bienvenue de l’app. Dans son menu de palette, vous choisissez une apparence (Système, Clair, Sombre) et, pour le clair comme pour le sombre, l’un des quatre thèmes d’aperçu (Aube, Classique, Moderne, Vif). Sa barre d’outils propose trois dispositions (Source, Partagé, Aperçu).

## Lisez ce que votre agent a écrit.

1. **L’agent écrit.** Votre agent de code ou votre assistant d’écriture rédige le Markdown : un README, une spécification, des notes.
2. **Vous relisez dans MarsDawn.** Ouvrez le fichier et lisez-le mis en forme, avec les diagrammes Mermaid et le code en couleur, à côté de la source.
3. **L’agent corrige.** Demandez des modifications. Ouvrez le fichier révisé et lisez-le de la même façon.

[Comment relire ce que votre agent vous rend](/fr/reading-agent-output/).

## À faire dès maintenant

L’outil en ligne de commande gratuit `marsdawn` est disponible dès aujourd’hui. Installez-le avec Homebrew :

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` transforme un fichier Markdown en PDF, rendu comme l’aperçu de MarsDawn. Il n’a pas besoin de l’app.
- `marsdawn open` ouvre des fichiers dans l’app MarsDawn pour que vous les relisiez.
- `--json` donne aux scripts et aux agents des résultats qu’ils peuvent analyser.

[Ligne de commande](/fr/cli/) · [marsdawn pour les agents](/fr/cli/agents/) · [Skill pour agents](/fr/cli/skill/) · [Serveur MCP](/fr/cli/mcp/)

## Ce que vous pouvez attendre de MarsDawn

- [Une app Mac](/fr/native/) : Fenêtres et onglets natifs, enregistrement automatique, Coup d’œil.
- [Vos textes restent sur votre Mac](/fr/yours/) : Pas de compte, pas de synchronisation, pas de cloud.
- [Essai gratuit, achat unique](/fr/pay-once/) : Gratuit pendant 14 jours, puis 4,99 USD une seule fois. Sans abonnement.

À savoir avant d’acheter. [Ce que MarsDawn ne fait pas](/fr/limits/)

## Questions et réponses

### Qu’est-ce que MarsDawn ?

MarsDawn est un éditeur Markdown natif pour Mac. Il affiche un aperçu en direct à côté de la source, dessine les diagrammes Mermaid et les formules KaTeX, affiche les fichiers Markdown dans le Finder avec Coup d’œil (Quick Look) et exporte en PDF.

### MarsDawn est-il un abonnement ?

Non. MarsDawn se télécharge gratuitement, avec 14 jours d’essai de toutes les fonctions. Ensuite, un seul achat intégré de 4,99 USD le déverrouille pour de bon. Rien ne se renouvelle, et il n’y a pas de compte.

### MarsDawn fonctionne-t-il sur iPhone ou iPad ?

Non. MarsDawn est une app Mac et demande macOS 26 ou une version ultérieure. Il n’existe pas d’app pour iPhone ou iPad.

### Claude Code peut-il ouvrir des fichiers dans MarsDawn ?

Oui. L’outil en ligne de commande gratuit marsdawn a une commande open qui ouvre un fichier Markdown dans MarsDawn, donc Claude Code, ou tout agent capable d’exécuter une commande shell, peut l’appeler. Un hook Claude Code facultatif peut ouvrir chaque fichier Markdown que Claude écrit ou modifie.

### Coup d’œil fonctionne-t-il encore après la fin de l’essai ?

Oui. Coup d’œil (Quick Look) dans le Finder continue d’afficher vos fichiers Markdown, que l’essai soit en cours ou non. Une fois l’essai terminé et tant que vous n’avez pas déverrouillé, les documents s’ouvrent dans MarsDawn avec leur contenu masqué.

## L’app, telle qu’elle est

### [Une app Mac](/fr/native/)

![MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

Sur cette capture d’écran :

1. Une fenêtre Mac native.
2. L’éditeur de texte du Mac, avec la coloration Markdown.
3. ⌘1 source, ⌘2 partagé, ⌘3 aperçu.
4. La page se met à jour pendant la saisie.

### [Export PDF](/fr/pdf/)

![Un PDF exporté depuis MarsDawn, ouvert dans sa visionneuse PDF avec les vignettes des pages.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

Sur cette capture d’écran :

1. Les diagrammes Mermaid, dessinés dans le PDF.
2. Le code garde sa coloration.

## Plus

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
- [Notes de lecture : Harrison Chase](https://marsdawn.southern-light.dev/fr/reading-notes/harrison-chase-what-is-an-agent/index.md): La définition d’un agent de Harrison Chase en 2024 et son spectre de comportement agentic, et son plaidoyer pour l’observabilité à mesure qu’un système avance dessus — lu du côté de qui lit le fichier qu’il rend.
- [Notes de lecture : LangChain (Jess Ou)](https://marsdawn.southern-light.dev/fr/reading-notes/langchain-what-is-an-agent/index.md): Le « What is an AI agent ? » de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.
- [Notes de lecture : Andrew Ng](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/index.md): Native Markdown editor for Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, $4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): Mac 原生 Markdown 編輯器：即時分割預覽、Mermaid、KaTeX、快速查看、PDF 輸出。免費試用，只需買一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): Mac 原生 Markdown 编辑器：实时分栏预览、Mermaid、KaTeX、快速查看、PDF 导出。免费试用，只需买一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): Mac 向けネイティブ Markdown エディタ。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Editor de Markdown nativo para Mac: vista previa en vivo junto al código, Mermaid, KaTeX, Vista rápida, exportación a PDF. Pruébalo gratis, 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
