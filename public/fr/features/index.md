# Tout ce que fait MarsDawn, sur une seule page.

MarsDawn est un éditeur Markdown pour Mac. Vous écrivez d’un côté et vous lisez la page mise en forme de l’autre, avec les diagrammes, les formules et le code dessinés. Il n’a pas de modèle d’IA à lui : il est conçu pour lire ce qu’un agent a écrit, et pour écrire vos propres textes. Et quand le travail passe sur une table, en réunion ou dans un classeur, il imprime et exporte des pages propres.

Chaque section ci-dessous dit ce que fait l’app et renvoie vers la page qui va plus loin.

![MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

Sur cette capture d’écran :

1. Une fenêtre Mac native.
2. L’éditeur de texte du Mac, avec la coloration Markdown.
3. ⌘1 source, ⌘2 partagé, ⌘3 aperçu.
4. La page se met à jour pendant la saisie.

## Lire ce que votre agent a écrit

### Source et aperçu côte à côte

Ouvrez un fichier Markdown et lisez la page mise en forme à côté de sa source (⌘2), ou passez à la source seule (⌘1) ou à l’aperçu seul (⌘3). Les deux sous-fenêtres défilent ensemble, et la page se met à jour pendant la saisie.

[Une app Mac](/fr/native/)

### Plan et fichiers dans la barre latérale

L’onglet Plan de la barre latérale liste les titres d’un document ; cliquez sur l’un d’eux pour y aller. Ouvrez un dossier et l’onglet Fichiers liste son contenu ; les nouveaux fichiers apparaissent d’eux-mêmes pendant qu’un agent y écrit. Si le dossier est un dépôt git, l’en-tête indique la branche ou le worktree.

[Lire ce que votre agent vous rend](/fr/reading-agent-output/)

### Montrer la ligne exacte

Édition ▸ Copier la référence copie votre position sous la forme d’un chemin et d’une ligne, comme `docs/plan.md:42`. Copier pour l’IA ajoute en dessous le texte sélectionné. Collez l’un ou l’autre dans la conversation de l’agent.

[Lire ce que votre agent vous rend](/fr/reading-agent-output/)

### Suivre les liens entre fichiers

Cliquez dans l’aperçu sur un lien vers un autre fichier Markdown : MarsDawn l’ouvre, ou le met au premier plan s’il est déjà ouvert, et défile jusqu’au titre.

## Sur papier, entre les personnes

Tout le travail ne se fait pas sur un écran. Les pages que MarsDawn imprime et exporte sont celles que vous lisez à l’écran ; elles servent donc là où les gens se réunissent, lisent et conservent des traces.

### En réunion

Imprimez les pages, ou envoyez à tout le monde le même PDF : toute la table travaille alors sur le même document, et non sur un seul écran partagé. Avec le même fichier, les sauts de page sont les mêmes, si bien que « le tableau de la page 3 » désigne une seule chose. Ensuite, chacun note les décisions, sur l’imprimé ou dans des notes. Le modèle de notes de réunion commence par les décisions et donne un responsable à chaque action.

[Export PDF](/fr/pdf/) · [Modèle de compte rendu](/fr/templates/meeting-notes/)

### Lire avec un stylo

Certaines personnes retiennent mieux avec un stylo : souligner, écrire dans la marge, pour que cela reste. Imprimez le document et faites-le sur le papier. MarsDawn n’a pas d’outil d’annotation à lui ; si vous préférez annoter le PDF, utilisez l’app PDF que vous avez déjà.

[Export PDF](/fr/pdf/)

### Dossiers papier

Dans certains métiers, on classe encore du papier, la comptabilité par exemple. MarsDawn ne revendique ni archivage ni conformité. Ce qu’il fait, c’est imprimer et exporter des pages propres et paginées : diagrammes dessinés, blocs de code courts gardés d’un seul tenant, couleurs claires du thème. Servez-vous-en partout où le papier reste le dossier de référence.

[Export PDF](/fr/pdf/)

### Transmettre à quelqu’un qui n’utilise pas Markdown

Un PDF s’ouvre n’importe où et ne demande aucune connaissance de Markdown ; c’est donc aussi celui à envoyer à un responsable ou à un client.

[Partager les PDF exportés](/fr/sharing-exported-pdfs/)

## Écrire et mettre en page

### Du Markdown simple, coloré

Le gras, l’italique, le barré, le code en ligne, les liens, les citations et les listes de tâches fonctionnent tous. L’éditeur colore la syntaxe Markdown, et les couleurs correspondent au thème de votre aperçu.

[Une app Mac](/fr/native/)

### Zoom, numéros de ligne et barre d’état

Zoomez ensemble sur la source et l’aperçu, de 50 % à 300 %. Une marge de numéros de ligne longe la source, et la barre d’état indique votre ligne et votre colonne, ainsi que le nombre de mots et de caractères et le temps de lecture du document ou de votre sélection.

### Images

Enregistrez le document, puis déposez ou collez une image dans l’éditeur. MarsDawn la copie dans un dossier assets à côté du document et écrit le lien. Les images venant du web restent masquées jusqu’à ce que vous cliquiez sur Charger les images, si bien qu’ouvrir un document n’apprend à aucun serveur que vous le lisez.

[Vos textes restent sur votre Mac](/fr/yours/)

### Les métadonnées en tête restent discrètes

Un bloc de métadonnées (front matter) en tête de fichier s’affiche comme une section repliée Infos du document dans l’aperçu et dans Coup d’œil, et il est omis du PDF.

### Huit langues

L’app existe en anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen.

[Une app Mac](/fr/native/)

## Diagrammes, code et formules

### Diagrammes Mermaid

Un bloc de code marqué `mermaid` est dessiné comme un diagramme. Si le diagramme contient une erreur, l’aperçu affiche sa source avec l’erreur en dessous, et un clic sur le message mène à cette ligne.

[Aperçu Mermaid sur Mac](/fr/mermaid-preview-mac/)

### Code coloré

Les blocs de code sont colorés pour la plupart des langages courants. Indiquez le langage après la clôture d’ouverture `````.

### Formules

Les formules écrites en syntaxe KaTeX sont dessinées dans l’aperçu et dans Coup d’œil, et se retrouvent dans le PDF exporté.

[Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](/fr/reviewing-ai-output/)

## Thèmes, PDF et impression

### Quatre thèmes, clairs et sombres

Aube, Classique, Moderne et Vif existent chacun en version claire et sombre, et MarsDawn suit l’apparence de votre Mac, sauf si vous en choisissez une dans les réglages. Choisissez dans Présentation ▸ Thème de l’aperçu ou avec le bouton palette de la barre d’outils.

[Thèmes](/fr/themes/)

### Plus de thèmes

Réglages ▸ Apparence ▸ Obtenir plus de thèmes… ouvre une galerie de thèmes d’aperçu supplémentaires. Installez-en un et il apparaît sous Présentation ▸ Thème de l’aperçu ; Supprimer le retire. La galerie ne se connecte à Internet que tant qu’elle est ouverte.

[Galerie de thèmes](/fr/themes/gallery/) · [Créer un thème](/fr/themes/new/)

### Exporter en PDF, ou imprimer

Fichier ▸ Exporter au format PDF… enregistre un PDF paginé, et Fichier ▸ Imprimer… imprime les mêmes pages. Les diagrammes Mermaid sont dessinés, le code garde sa coloration, et les sauts de page évitent de séparer un titre de sa section ou de couper en deux un bloc de code court ou un diagramme. Le PDF utilise toujours les couleurs claires du thème, même si vous lisiez en mode sombre.

[Export PDF](/fr/pdf/)

![Un PDF exporté depuis MarsDawn, ouvert dans sa visionneuse PDF avec les vignettes des pages.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

Sur cette capture d’écran :

1. Les diagrammes Mermaid, dessinés dans le PDF.
2. Le code garde sa coloration.

## Écrire sur le Mac, lire en chemin

Votre agent travaille sur le Mac. Ses plans et ses rapports peuvent vous suivre sur iPhone ou iPad.

1. **Sur le Mac :** enregistrez les plans et les rapports de l’agent dans un dossier d’iCloud Drive.
2. **Sur iPhone ou iPad :** dans MarsDawn, touchez « Ouvrir » et choisissez le même fichier. Les diagrammes Mermaid, les formules, le code et les tableaux s’affichent mis en forme, avec le plan et votre thème.
3. **De retour sur le Mac :** continuez à modifier, ou exportez un PDF.

Avec le même compte Apple, un seul essai et un seul déverrouillage couvrent MarsDawn sur Mac, iPhone et iPad.

Sur iPhone et iPad, MarsDawn sert uniquement à lire : il ouvre les fichiers Markdown et texte brut, sans modification ni export PDF. Il lit les fichiers que vous gardez dans iCloud Drive ; MarsDawn n’a pas de cloud à lui.

## Fichiers, onglets et Coup d’œil

### Fenêtres et onglets

Chaque document s’ouvre dans sa propre fenêtre. Choisissez Fenêtre ▸ Fusionner toutes les fenêtres pour regrouper les fenêtres ouvertes en onglets d’une seule. L’enregistrement automatique se fait pendant la saisie.

[Une app Mac](/fr/native/)

### Coup d’œil dans le Finder

Sélectionnez un fichier Markdown dans le Finder et appuyez sur Espace pour le lire mis en forme, diagrammes compris. Coup d’œil utilise le thème que vous avez choisi dans MarsDawn et suit son réglage d’apparence.

[Une app Mac](/fr/native/) · [Coup d’œil pour Markdown](/fr/quicklook/)

### Autres fichiers

MarsDawn ouvre aussi les fichiers texte brut (`.txt`, `.log`, code source) et les PDF. Le texte UTF-8 s’ouvre prêt à être modifié, en source uniquement. Les PDF s’ouvrent dans un lecteur avec vignettes de pages, zoom et recherche.

### Vos fichiers restent les vôtres

Il n’y a ni compte, ni synchronisation, ni cloud. Les documents restent là où vous les enregistrez, et MarsDawn ne collecte aucune donnée sur vous.

[Vos textes restent sur votre Mac](/fr/yours/)

## Pour les agents et les scripts

### Un outil en ligne de commande gratuit

L’outil gratuit `marsdawn` s’installe séparément avec Homebrew. `marsdawn export` transforme un fichier Markdown en PDF, rendu comme l’aperçu de MarsDawn ; il n’a pas besoin de l’app. Choisissez un thème avec `--theme` et un format de papier, A4 ou Letter. `marsdawn open` ouvre des fichiers dans l’app pour que vous les relisiez, éventuellement à une ligne précise, et demande que l’app soit installée.

[Ligne de commande](/fr/cli/)

### Une sortie lisible par un script

Avec `--json`, les deux commandes renvoient un résultat qu’un agent ou un script peut analyser.

[marsdawn pour les agents](/fr/cli/agents/)

### Skill et serveur MCP

Un fichier de skill d’agent apprend à un agent de programmation à ouvrir dans MarsDawn ce qu’il a écrit, pour que vous le relisiez. Pour les clients sans shell, un serveur MCP distinct exécute le même export.

[Skill pour agents](/fr/cli/skill/) · [Serveur MCP](/fr/cli/mcp/)

### Pas d’IA à l’intérieur

MarsDawn n’a pas de modèle d’IA à lui. Il ne résume pas et ne note pas ce qu’un agent a écrit ; il garde lisible un long fichier qui change, pour que ce soit vous qui lisiez.

[Ce que MarsDawn ne fait pas](/fr/limits/)

## Siri et Raccourcis

Recherchez MarsDawn dans l’app Raccourcis pour trouver trois actions : Nouveau document Markdown (à partir d’un modèle), Ajouter une note à la boîte de réception et Ouvrir un document récent. Les notes vont dans `Inbox.md`, dans le dossier que vous choisissez dans MarsDawn ▸ Réglages… ▸ Dossier de notes.

[Une app Mac](/fr/native/)

## Une fois la page imprimée

Une réunion autour de pages imprimées, un stylo dans la marge, un dossier papier classé.

[Film MarsDawn (en anglais), 88 secondes](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## Essayez-le sur votre Mac

MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis débloquez-le une seule fois pour 4,99 USD. Sans abonnement ni compte. macOS 26 ou version ultérieure est requis.

[Télécharger et essayer](https://apps.apple.com/app/id6812925073)

Comment fonctionne l’essai : [Essai gratuit, achat unique](/fr/pay-once/). Ce qui est volontairement absent : [Ce que MarsDawn ne fait pas](/fr/limits/).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas de modification sur iPhone ou iPad, pas de plug-ins, pas de comptes. Des thèmes, mais pas de CSS personnalisé. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Ouvrir un fichier .md sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Coup d’œil pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MarsDawn comparé : aperçu VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Meilleur lecteur Markdown pour Mac (2026)](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu intégrés, chacun clair et sombre, et une galerie vérifiée dans les réglages de MarsDawn pour Mac. Coup d’œil utilise votre thème.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Créer un thème avec votre agent](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu pour MarsDawn, chacun relu par le développeur, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Feuille de route](https://marsdawn.southern-light.dev/fr/roadmap/index.md): Ce qui est en cours et ce qui vient ensuite pour MarsDawn sur Mac, iPhone et iPad, version par version. Sans dates ; les idées non planifiées sont signalées.
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
