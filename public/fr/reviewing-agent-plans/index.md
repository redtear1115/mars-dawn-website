# Relire le plan d’un agent en cinq minutes

Votre agent a rédigé un plan et attend votre feu vert. Vous avez cinq minutes, pas une heure. Voici une façon de les utiliser qui fonctionne dans n’importe quel éditeur, même un simple éditeur de texte. MarsDawn aide pour certaines étapes, et nous dirons lesquelles. Il n’aide pas pour la plus importante.

**Ne lisez pas le plan de haut en bas. Vérifiez sa structure, vérifiez une affirmation, repérez ce qui est irréversible, regardez les diagrammes et le périmètre, puis rédigez un retour exploitable par l’agent. Six étapes, cinq minutes environ.**

## Pourquoi s’en soucier avant l’exécution

Chip Huyen, expliquant pourquoi la planification doit rester séparée de l’exécution, chiffre le coût sans détour : « Sans supervision, un agent peut exécuter ces étapes pendant des heures, gaspillant temps et argent en appels d’API, avant que vous ne vous rendiez compte qu’il n’aboutit à rien. » Notre ajout : un plan est l’endroit le moins coûteux pour repérer une erreur. Corriger une ligne de `plan.md` coûte une phrase. Corriger ce que l’agent a fait après coup coûte un après-midi.

## L’exemple

Vous avez demandé à un agent de déplacer les avatars des utilisateurs vers un stockage objet sans casser les liens existants. Il vous rend ceci :

```
# Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. ✅ done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.
```

Cela se lit bien. Cela supprimerait aussi tous les avatars avant d’en avoir copié un seul.

## Les six étapes

**1. Lisez seulement les titres.** *(une minute environ)* Le plan correspond-il à ce que vous avez demandé ? Une section manquante signifie généralement du travail manquant. Ici : Goal, Steps, Status. Vous avez demandé que les liens existants continuent de fonctionner, et aucun titre ne parle des anciens liens ni de la façon d’annuler le changement. C’est votre premier commentaire.

Dans un terminal, `grep -n '^#' plan.md` affiche uniquement les titres, et la plupart des éditeurs savent aussi afficher un plan. Dans MarsDawn, l’onglet Plan de la barre latérale (Présentation ▸ Afficher la barre latérale, ⌃⌘S) les liste, et un clic y mène.

**2. Repérez chaque endroit qui affirme que quelque chose est fait, réussi ou vérifié, et vérifiez-en un vous-même.** *(une minute environ)* Ouvrez le fichier, lancez le test, comptez les lignes. Chip Huyen décrit un échec où « l’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas ». Dans son exemple, un agent chargé de loger 50 personnes dans 30 chambres d’hôtel en place 40 et affirme avoir terminé.

```
grep -n -i -E 'done|pass|verified|✅' plan.md
```

Ici, cela trouve « ✅ done » et « All tests pass. » Quels tests ? L’un d’eux touche-t-il aux avatars ? Lancez-les, ou demandez. MarsDawn ne peut pas faire cette étape à votre place. Personne d’autre que vous ne le peut.

**3. Cherchez les étapes irréversibles.** *(une minute environ)* Suppression de données, migrations, force-push, tout ce qui envoie, paie ou publie. Celles-là attendent votre accord explicite. Chip Huyen décrit la même idée du côté du système : « Si un plan comporte des opérations risquées, comme mettre à jour une base de données ou fusionner une modification de code, le système peut demander une approbation humaine explicite avant de les exécuter, ou laisser des humains les exécuter. » Ici, l’étape 4 supprime les originaux, et elle vient avant l’étape 5, la copie.

**4. Lisez les diagrammes rendus, et confrontez chaque flèche au texte.** Un organigramme qui dit « copier → vérifier → supprimer » alors que les étapes disent autre chose, c’est une trouvaille. Ce plan n’a pas de diagramme : on passe pour aujourd’hui. Quand il y en a un, regardez l’image, pas le source Mermaid : beaucoup d’éditeurs ont un aperçu, et [Comment afficher un fichier Markdown sur Mac](/fr/view-markdown-on-mac/) et [Afficher du Markdown ailleurs](/fr/vs/markdown-preview-tools/) présentent les options. Dans MarsDawn, le diagramme rendu se trouve à côté de son source (⌘2), et un diagramme cassé affiche son source avec l’erreur en dessous, ce qui mérite un commentaire à part entière.

**5. Listez les fichiers et systèmes que le plan touche, et posez des questions sur tout ce que vous n’avez pas demandé.** *(étapes 4 et 5 ensemble, une minute environ)* Ici : la configuration du stockage, les templates, un dossier sur le serveur, un bucket. Qui peut lire le bucket ? Vous n’avez pas dit qu’il devait être public. Si vous avez ouvert le dossier de travail de l’agent dans MarsDawn (Fichier ▸ Ouvrir un dossier…, ⇧⌘O), les nouveaux fichiers qu’il écrit apparaissent dans l’onglet Fichiers en une seconde environ, et l’en-tête indique la branche git ou le worktree, pour que vous sachiez quel checkout vous relisez.

**6. Rédigez vos retours sous la forme endroit, problème, correction, un problème par ligne.** *(la dernière minute)*

```
plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.
```

N’importe quel éditeur avec des numéros de ligne fait l’affaire. Dans MarsDawn, Édition ▸ Copier la référence (⌥⌘C) copie votre position sous la forme `plan.md:10`, et Copier pour l’IA (⌃⌥⌘C) ajoute le texte sélectionné en dessous.

## Si vous avez une minute

Faites l’étape 2. C’est là qu’on prend en défaut un agent qui se croit fini.

## Quand cinq minutes ne suffisent pas

Parfois, vous ne pouvez pas savoir si une étape est juste, parce qu’elle sort de votre domaine. Jess Ou, dans l’article explicatif de LangChain sur les agents paru en 2026, le dit en deux phrases : « Ne déléguez pas un jugement que vous ne pouvez pas évaluer. Si vous ne reconnaîtriez pas une bonne réponse, l’agent non plus. » Notre conclusion : si vous ne pouvez pas juger une étape, ce n’est pas une raison pour l’approuver plus vite. C’est une raison pour demander à quelqu’un qui le peut.

## Ce que MarsDawn fait ici, et ce qu’il ne fait pas

MarsDawn n’embarque aucun modèle d’IA. Il ne trouvera pas les problèmes de ce plan, et il ne fait ni l’étape 2 ni l’étape 3. Il garde le fichier lisible pendant que vous travaillez : le plan pour l’étape 1, les diagrammes rendus pour l’étape 4, l’onglet Fichiers pour l’étape 5, les références de ligne pour l’étape 6. Et si l’agent révise le plan pendant votre lecture, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.

Une fois le plan arrêté, si quelqu’un d’autre doit le voir, [Partager des PDF exportés](/fr/sharing-exported-pdfs/) et [Markdown en PDF](/fr/markdown-to-pdf/) expliquent comment le transmettre en PDF.

## Essayer

MarsDawn est sur le [Mac App Store](https://apps.apple.com/app/id6812925073). Il existe aussi l’outil en ligne de commande gratuit `marsdawn` :

```
brew install redtear1115/tap/marsdawn
```

Il exporte le Markdown en PDF sans l’app.

[Ligne de commande](/fr/cli/) · À savoir avant d’acheter : [Ce que MarsDawn ne fait pas](/fr/limits/)

## Pour aller plus loin

- Pourquoi ce que rend un agent est difficile à lire : [Lire ce que votre agent vous rend](/fr/reading-agent-output/).
- Pourquoi les agents exposent leurs plans : [Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?](/fr/agent-transparency/)
- Les plans ne sont pas la seule chose que rendent les agents : [Quatre modèles de conception d’agents et les documents que chacun vous remet](/fr/agent-design-patterns/).

## Sources

- Chip Huyen, « Agents », 7 janvier 2025 : [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou, « What is an AI agent? », LangChain, 31 juillet 2026 : [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): MarsDawn est un éditeur Markdown natif pour Mac : aperçu en direct côte à côte, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Quick Look pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
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
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [Deutsch](https://marsdawn.southern-light.dev/de/reviewing-agent-plans/index.md): Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.
- [Español](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
- [한국어](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
