# Historique des versions

Ce qui a changé dans chaque version de l’app MarsDawn du Mac App Store et de l’outil en ligne de commande gratuit marsdawn. Pour l’app, la date est le jour où la version est parue sur le Mac App Store.

Ce qui arrive ensuite figure dans la [feuille de route](/fr/roadmap/).

## App MarsDawn

### MarsDawn 1.1.1

15 octobre 2026

- En allemand, en japonais, en espagnol et en français, Réglages > Apparence > « Obtenir plus de thèmes… » affiche désormais le filtre de scénario sous forme de menu local intitulé « Scénario », pour que les cinq choix tiennent. L’anglais, le coréen et le chinois utilisent toujours le contrôle segmenté.
- Lorsqu’un thème est retiré de la galerie, l’avis dans « Obtenir plus de thèmes… » affiche maintenant le nom du thème (par exemple Inkwell Ivory) au lieu de son identifiant interne.
- Les sections details repliables écrites à la manière de GitHub s’affichent désormais repliées, avec leur résumé visible, dans l’aperçu et dans Coup d’œil, et s’ouvrent d’un clic. L’export PDF imprime toujours le contenu de chaque section.
- Les documents ouverts depuis le Finder, le Dock, Fichier > « Ouvrir… » ou la commande marsdawn open s’ouvrent désormais en onglets dans la fenêtre au premier plan, tout comme les nouveaux documents. Pour conserver l’ancien comportement, choisissez « Suivre le réglage système » dans Réglages > Apparence.

Les versions précédentes ne sont décrites qu’en anglais : [voir l’historique en anglais](/changelog/).

## Outil en ligne de commande marsdawn

Les versions antérieures à 0.5.1 ne sont pas listées.

### marsdawn 0.7.2

20 octobre 2026. La mise en page Guide, les encadrés et les polices japonaises.

- La valeur de `--layout` devient `handbook`, la mise en page Guide de l’app : `marsdawn export --layout handbook`. `--layout manual` fonctionne toujours, mais est obsolète.
- Les encadrés s’affichent, dans l’aperçu et dans les PDF exportés : les alertes GitHub comme `> [!NOTE]` et `> [!WARNING]`, et les conteneurs HackMD comme `:::info` et `:::warning`. `:::spoiler` crée une section repliable.
- Un document en japonais utilise des polices japonaises pour ses kana et ses kanji. marsdawn déduit la langue de `lang: ja` dans le front matter, ou de la part de kana dans le texte.
- Après un `export` ou un `open` réussi dans un terminal, marsdawn affiche une fois un conseil sur stderr quand la skill pour agents est absente ou périmée. La sortie sur stdout et avec `--json` ne change pas. Définissez `MARSDAWN_NO_SKILL_HINT=1` pour ne plus l’afficher.

### marsdawn 0.7.1

20 octobre 2026. Une mise en page Guide, et une taille maximale.

- `marsdawn export --layout manual` produit un guide : marges plus larges, côté de reliure de 25 mm et chaque titre de premier niveau sur une nouvelle page, plus une couverture tirée des champs title, subtitle, version, date, author et logo du front matter, une table des matières des titres de niveaux 1 et 2 avec numéros de page, des numéros de page `n / N` et des signets PDF. `--toc-title` définit le titre de la page de table des matières. `--layout document` reste la valeur par défaut.
- `<!--BREAK-->` seul sur une ligne commence une nouvelle page, dans les deux mises en page.
- `marsdawn export` refuse un fichier de plus de 16 Mio : il se termine avec le code 5, indique `input_too_large` avec `--json` et n’écrit rien.
- La page d’aperçu retire les éléments script et noscript ; un diagramme Mermaid redessiné garde son propre SVG.
- Une référence de caractère qui se décode en `=` ou `^`, comme `&#61;`, ne s’associe plus à une marque HackMD.

### marsdawn 0.7.0

18 octobre 2026. Le Markdown de HackMD, les retours à la ligne et des limites pour les très gros documents.

- Les marques en ligne de HackMD s’affichent : `==mark==`, `^sup^` et `~sub~`. Un paragraphe `[TOC]` seul devient une table des matières, les tailles d’image de HackMD s’appliquent, les balises d’intégration deviennent de simples liens https, et la langue d’un bloc de code est lue avant les options HackMD comme `js=`.
- `marsdawn export --breaks` transforme chaque retour à la ligne d’un paragraphe en saut de ligne, comme HackMD. Sans cette option, un retour à la ligne entre deux caractères chinois ou japonais disparaît, et les lignes se lisent comme une seule phrase. Le coréen garde son espace, car il sépare ses mots par des espaces.
- Les très gros documents ont des limites, dans l’aperçu et dans les PDF exportés. Un bloc de code de plus de 128K caractères n’est pas coloré, et la coloration s’arrête après 256K caractères au total. Jusqu’à 100 diagrammes Mermaid et 1 000 formules sont rendus par mise à jour ; les autres diagrammes affichent leur source, avec une note, même s’ils avaient déjà été dessinés.
- Dans un diagramme de séquence, le libellé d’un message dans un bloc `rect` prend un contour de la couleur du bloc.
- Une référence de note de bas de page juste au-dessus d’un tableau ne fait plus planter `marsdawn export`.
- `marsdawn skill --install` se termine avec le code 7 (`skill_install_failed`) quand il ne peut pas créer le dossier ou écrire le fichier, et laisse intact un SKILL.md existant.

### marsdawn 0.6.4

13 octobre 2026. Blocs `<details>` repliables.

- Un bloc `<details>` à la manière de GitHub, avec des lignes vides à l’intérieur, s’affiche comme un seul élément repliable, dans l’aperçu et dans les PDF exportés. Avant, il se coupait à la première ligne vide.
- L’export PDF ouvre chaque bloc `<details>` avant l’impression, sauf le front matter.
- L’aperçu garde sa position de défilement quand vous ouvrez ou fermez un bloc `<details>`.

### marsdawn 0.6.3

6 octobre 2026. MarsDawn est sur le Mac App Store.

- Quand l’app n’est pas installée, `marsdawn open` renvoie vers MarsDawn sur le Mac App Store.
- Le README et la skill pour agents expliquent `marsdawn open .` et `--folder` : MarsDawn 1.0.0 affiche le dossier dans la barre latérale de la fenêtre.

### marsdawn 0.6.1

29 septembre 2026. Vérifier un thème.

- `marsdawn theme validate` vérifie un `theme.json` selon les règles de l’app. Il se termine avec le code 0 si le thème est valide et 1 sinon, en listant chaque problème. `--require-complete` exige aussi les couleurs de syntaxe et de diagramme.
- `marsdawn theme css` affiche le CSS que l’aperçu utilise pour un thème valide, et `marsdawn theme preview` rend avec lui un document d’exemple dans un PNG, clair ou sombre.

### marsdawn 0.5.4

26 septembre 2026. Corrections Mermaid, lignes des erreurs de diagramme et installation de la skill.

- Dans un diagramme de séquence, le libellé d’un message qui croise les lignes de vie d’autres participants reste lisible, dans l’aperçu comme dans les PDF exportés.
- `marsdawn export` gère les documents remplis de diagrammes Mermaid. Un document de 50 diagrammes, qui échouait auparavant avec le code 5, s’exporte désormais.
- `marsdawn export --json` ajoute `diagramErrorDetails`, avec les numéros de ligne de chaque erreur de diagramme : où le diagramme commence dans votre document et, quand Mermaid en indique une, la ligne de l’erreur elle-même.
- `marsdawn skill --install` installe la skill pour Claude Code dans `~/.claude/skills/marsdawn/SKILL.md`, ou dans un autre dossier avec `--dir`. Il laisse intact un fichier identique et ne remplace un fichier différent qu’avec `--force`. Sinon, il se termine avec le code 64 (`skill_differs`) sans rien modifier.

### marsdawn 0.5.3

25 septembre 2026. État du dossier, erreurs Mermaid complètes et petites corrections.

- `marsdawn open --folder` peut indiquer ce qu’il est advenu du dossier. Avec une app qui répond, il attend jusqu’à `--wait` secondes (2 par défaut), et `--json` donne un état comme `attached` ou `needsUser`.
- Un diagramme Mermaid qui ne s’analyse pas affiche le message d’erreur complet de Mermaid au lieu de sa seule première ligne, avec le numéro de ligne compté depuis le début de votre document.
- La recherche de la fin d’un bloc front matter s’arrête après 1 000 lignes : un bloc non fermé n’entraîne plus le parcours du reste d’un long document.
- Une app peut donner au lien de retour d’une note de bas de page un libellé traduit pour l’export PDF et l’impression. Le libellé n’est pas imprimé sur la page, et `marsdawn export` garde le libellé anglais.
- La copie intégrée de highlight.js est désormais épinglée par version, source et SHA-256, comme KaTeX et Mermaid.

### marsdawn 0.5.2

24 septembre 2026. Notes de bas de page, contraste et dossiers.

- Les notes de bas de page s’affichent dans les PDF exportés : appels numérotés, avec les notes après le corps du texte.
- Chaque thème respecte le contraste WCAG AA, en clair comme en sombre. Classique est désormais en noir et blanc.
- `marsdawn skill` affiche la skill pour agents qui correspond au marsdawn installé.
- `marsdawn open` se termine avec le code 6 (`app_cannot_open_folders`) quand le MarsDawn trouvé ne peut pas afficher de dossier, au lieu d’annoncer un succès.
- Les espaces réservés dessinés dans les pages exportées existent aussi en allemand, français, espagnol et coréen.
- Un espace réservé d’image n’affiche plus le chemin absolu caché derrière un très long chemin relatif.
- `MARSDAWN_APP_PATH` n’est utilisé que s’il pointe vers une app MarsDawn.

### marsdawn 0.5.1

19 septembre 2026. Export PDF, et ouverture d’un fichier depuis la ligne de commande.

- La couche de texte d’un PDF exporté est réparée pour le chinois, le japonais et le coréen.
- `marsdawn open --background` ouvre un fichier sans faire passer MarsDawn au premier plan.
- `marsdawn open` accepte un dossier, et MarsDawn l’affiche dans la barre latérale de la fenêtre (MarsDawn 1.0.0 et versions ultérieures).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Des thèmes, mais pas de CSS personnalisé. À savoir avant d’acheter.
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
