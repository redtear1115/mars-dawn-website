# Lire du Markdown sur Mac : MarsDawn et les autres options

Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur [Assistance](/fr/support/).

|  | MarsDawn | Aperçu VS Code | Obsidian | QLMarkdown | LynxOffice |
|---|---|---|---|---|---|
| Ouvrir un .md local | Oui, modifie le fichier sur place [app 1.1.1] | Oui, aperçu avec ⇧⌘V [[8](#v8)] | Non précisé par le fournisseur [[21](#v21)] | Aperçu seulement: "for viewing Markdown files" [[22](#v22)] | "Markdown opens rendered and saves back verbatim." [[3](#v3)] |
| Mermaid | Intégré [[1](#v1)] | Intégré [[8](#v8)] | Intégré, syntaxe des notes [[16](#v16)] | Intégré, blocs `mermaid` [[22](#v22)] | "diagram blocks are not rendered" [[3](#v3)] |
| Formules | KaTeX, `$…$` et `$$…$$` [[kit](#kit)] | KaTeX [[8](#v8)] | MathJax [[16](#v16)] | MathJax [[22](#v22)] | "Footnotes, math, and diagram blocks are not rendered." [[3](#v3)] |
| Relire le plan d’un agent / aller à une ligne | `marsdawn open file:line` ; mise à jour depuis le disque ; Copier la référence [/cli/, /features/] | Aperçu diff Markdown, lignes modifiées surlignées [[8](#v8)] ; `code -g file:line` [[14](#v14)] | Pas de paramètre de ligne dans `obsidian://open` [[20](#v20)] | Non précisé par le fournisseur | CLI et serveur MCP ; saut à une ligne non précisé [[4](#v4), [5](#v5)] |
| PDF : sauts de page, numéros de page | Les sauts ne coupent pas les blocs de code courts [/pdf/] ; pas de numéros de page [vérif.] | Non précisé par le fournisseur [[8](#v8)] | Format du papier, marges ; sauts et numéros non précisés [[17](#v17)] | Non précisé par le fournisseur [[22](#v22)] | PDF "including tables" ; sauts et numéros non précisés [[3](#v3)] |
| Prix | Téléchargement gratuit ; déverrouillage 4,99 USD une fois ; essai de 14 jours [[1](#v1)] | Non précisé par le fournisseur [[12](#v12), [13](#v13)] | Personnel : "Free without limits" ; licence commerciale facultative [[15](#v15)] | Gratuit, GPL-3.0 [[22](#v22)] | "Free while in early release." [[2](#v2)] |
| Configuration requise | macOS 26.0 ou ultérieur [[1](#v1)] | "the latest release and the two previous versions" [[9](#v9)] | Non précisé par le fournisseur [[18](#v18)] | macOS 12.0 ou ultérieur [[23](#v23)] | macOS 13 ou ultérieur [[2](#v2)] |
| Compte requis | Non [/privacy/] | Non précisé par le fournisseur | "No sign-up required" [[15](#v15)] | Non précisé par le fournisseur | Non [[2](#v2)] |

Chaque cellule a été vérifiée le 16 octobre 2026 auprès de la source entre crochets (les numéros V sont listés plus bas ; [vérif.] est notre propre export avec marsdawn 0.6.4). Les citations des fournisseurs restent telles quelles. « Non précisé par le fournisseur » signifie que les pages lues n’en disent rien, pas que la fonction manque. Aucune cellule ne classe les produits.

## Sources

- 1 · [Mac App Store](https://apps.apple.com/app/id6812925073)
- 2 · [https://lynxoffice.com/](https://lynxoffice.com/)
- 3 · [https://lynxoffice.com/markdown/](https://lynxoffice.com/markdown/)
- 4 · [https://lynxoffice.com/cli/](https://lynxoffice.com/cli/)
- 5 · [https://lynxoffice.com/mcp/](https://lynxoffice.com/mcp/)
- 6 · [https://lynxoffice.com/release-notes/](https://lynxoffice.com/release-notes/)
- 8 · [https://code.visualstudio.com/docs/languages/markdown](https://code.visualstudio.com/docs/languages/markdown)
- 9 · [https://code.visualstudio.com/docs/supporting/requirements](https://code.visualstudio.com/docs/supporting/requirements)
- 11 · [https://code.visualstudio.com/updates/v1_142](https://code.visualstudio.com/updates/v1_142)
- 12 · [https://code.visualstudio.com/license](https://code.visualstudio.com/license)
- 13 · [https://code.visualstudio.com/](https://code.visualstudio.com/)
- 14 · [https://code.visualstudio.com/docs/configure/command-line](https://code.visualstudio.com/docs/configure/command-line)
- 15 · [https://obsidian.md/pricing](https://obsidian.md/pricing)
- 16 · [https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax](https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax)
- 17 · [https://obsidian.md/help/pdf](https://obsidian.md/help/pdf)
- 18 · [https://obsidian.md/download](https://obsidian.md/download)
- 19 · [https://obsidian.md/changelog/](https://obsidian.md/changelog/)
- 20 · [https://obsidian.md/help/uri](https://obsidian.md/help/uri)
- 21 · [https://obsidian.md/help/Getting+started/Create+a+vault](https://obsidian.md/help/Getting+started/Create+a+vault)
- 22 · [https://github.com/sbarex/QLMarkdown](https://github.com/sbarex/QLMarkdown)
- 23 · [https://github.com/sbarex/QLMarkdown/releases](https://github.com/sbarex/QLMarkdown/releases)
- 24 · [https://api.github.com/repos/sbarex/QLMarkdown/releases](https://api.github.com/repos/sbarex/QLMarkdown/releases)
- kit · [https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7](https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7)

Ce qui manque à MarsDawn. Il faut macOS 26 ou ultérieur. Il n’y a pas d’app pour iPhone ou iPad ; MarsDawn est fait pour le Mac. Pas d’édition partagée, pas de synchronisation, pas de compte. L’aperçu ne se modifie pas ; vous modifiez la source Markdown à côté. Pas d’export Word, pas de plug-ins. Les PDF n’ont pas de numéros de page. Pas de vue diff : quand un agent enregistre une modification, la fenêtre ouverte se met à jour depuis le disque en une étape que vous pouvez annuler, mais elle ne surligne pas ce qui a changé. Après l’essai de 14 jours, les documents s’ouvrent avec leur contenu masqué jusqu’au déverrouillage.

## Quand vous n’avez pas besoin de MarsDawn

- Vous vivez dans VS Code et un volet d’aperçu suffit : il affiche Mermaid et KaTeX, propose un aperçu diff Markdown et va à une ligne avec code -g.
- Vous voulez seulement un aperçu à la barre d’espace dans le Finder : QLMarkdown est une extension Coup d’œil gratuite pour le Markdown.
- Votre Mac a un macOS plus ancien : QLMarkdown demande la 12.0 ou ultérieure, LynxOffice la 13 ou ultérieure. L’outil gratuit marsdawn demande macOS 15 et exporte en PDF sans l’app.
- Vous tenez un coffre (vault) de notes liées : c’est pour cela qu’Obsidian est fait.
- Il vous faut une app iPhone ou iPad, l’édition partagée ou l’export Word.
- Vous voulez qu’un agent traite tableurs, fichiers Word et PDF : LynxOffice documente un serveur MCP pour cela.

- [MacMD Viewer ou MarsDawn](/fr/vs/macmd-viewer/) : une visionneuse en lecture seule face à MarsDawn, cellule par cellule, avec quand choisir l’un ou l’autre.
- [Outils d’aperçu Markdown](/fr/vs/markdown-preview-tools/) : l’aperçu de VS Code, une extension de navigateur et l’aperçu de fichiers de Claude Desktop.
- [Meilleur lecteur Markdown pour Mac (2026)](/fr/best-markdown-viewer-mac/)

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Ouvrir un fichier .md sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Coup d’œil pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Meilleur lecteur Markdown pour Mac (2026)](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Créer un thème avec votre agent](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu proposés par la communauté pour MarsDawn, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur, sans installation ni git.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
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
- [English](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [Español](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
