# Un test qui passe sur un Mac ne teste peut-être pas ce que vous croyez.

Le vibe coding n’a rien de mal, et MarsDawn est lui aussi développé avec des agents. Mais un logiciel sur lequel on compte se juge à ce qui vient après la première version : des années de maintenance et de sécurité, qui commencent par vérifier qu’un changement n’a rien cassé.

**Un test passait sur un Mac mini et échouait sur un MacBook Air. Le produit allait bien. Le test lisait les couleurs à travers le profil colorimétrique de l’écran, et sur le Mac mini, il passait par chance. Une deuxième machine a trouvé un bug dans le test, pas dans le code.**

Vous voulez seulement savoir avec quels fichiers extrêmes ou hostiles MarsDawn est testé ? Passez directement à [Ce que nous lui faisons subir](#inputs).

## Le test qui échouait sur un MacBook Air

Une exécution complète des tests du moteur d’export sur le runner macOS 15 de GitHub prend près d’une heure : environ 32 minutes pour le build debug et environ 25 pour le build release. Pour réduire ce temps, nous avons essayé de déplacer la moitié macOS 26 sur un MacBook Air à nous ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)).

À la première exécution, un test a échoué. Il exporte un PDF avec des encadrés (Note, Tip, Warning) et vérifie que chacun porte sur son bord une barre de la bonne couleur, c’est-à-dire avec un écart de couleur inférieur à 0,16. Sur le MacBook Air, les écarts étaient de 0,1634, 0,1648 et 0,1796. Sur un Mac mini, avec le même commit, le même macOS et le même Xcode, le test passait.

Notre première idée : l’export était cassé. Il ne l’était pas. Le PDF n’avait aucun problème ; ce qui différait d’une machine à l’autre, c’était la façon dont le test le lisait.

Le test transformait chaque page du PDF en image et en lisait les pixels, et macOS dessine cette image dans l’espace colorimétrique de l’écran principal. Le Mac mini était branché sur un moniteur externe ordinaire ; le MacBook Air utilisait son écran intégré. Nous avons rempli une image d’un seul orange et l’avons relue : (0,784 ; 0,278 ; 0,106) revenait en (0,822 ; 0,335 ; 0,179) sur le Mac mini et en (0,782 ; 0,395 ; 0,221) sur le MacBook Air.

Voici ce qui compte : sur le Mac mini non plus, le test ne lisait pas les bonnes couleurs. Il se trompait de 0,128 au plus, juste sous la limite de 0,16. Il passait grâce au moniteur, pas parce qu’il mesurait correctement la barre.

Le correctif ([kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)) ne modifie que le test : il dessine la page dans une image à l’espace colorimétrique sRGB fixe, sans aucun écran en jeu. Les deux machines lisent désormais exactement les couleurs des barres, avec un écart de 0,0, sur l’écran intégré du MacBook Air comme sur le Mac mini. La CI de la pull request est passée ([run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)), et une fois le correctif arrivé sur la branche du runner du MacBook Air, la suite complète y est passée aussi ([run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)). Puis nous l’avons fait échouer exprès : avec du bleu comme couleur attendue partout, il est passé au rouge pour les cinq encadrés.

Il lui reste une faille connue. Note et Caution utilisent deux oranges séparés d’environ 0,119, sous la limite de 0,16 : si on les intervertissait, le test ne le remarquerait probablement pas. Nous l’avons noté plutôt que de faire comme si le test était complet.

Un test qui ne peut pas échouer ne protège rien, pas plus qu’un test qui échoue pour une mauvaise raison, comme le profil colorimétrique d’un écran. Le vert sur une machine vous dit que le test y est passé, pas qu’il mesure ce que dit son nom.

## Les tests sont des filets superposés

Aucun test ne rattrape tout. Chaque couche est un filet aux mailles différentes, et une erreur qui passe à travers l’un devrait tomber dans le suivant :

- **PDF de référence :** le moteur d’export (le projet open source [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit), qui fait aussi tourner la commande `marsdawn`) exporte des documents d’exemple, et le texte de chaque page est comparé à une copie enregistrée. Cela rattrape le contenu qui disparaît sans bruit, ou un nombre de pages qui change.
- **Systèmes et builds différents :** le moteur tourne sous macOS 15, la plus ancienne version prise en charge, et sous macOS 26, celle avec laquelle l’app est livrée, chaque fois en build debug et en build release. La suite complète de l’app tourne en quatre combinaisons : signée et non signée, chacune avec le paywall désactivé puis activé. Cela rattrape ce qui ne casse que sur un système plus ancien, ou seulement dans le build que reçoivent réellement les clients.
- **Vrai matériel :** la CI de l’app tourne sur nos propres Mac (le Mac mini et le MacBook Air), et c’est en essayant la suite du moteur sur ce MacBook Air ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240), toujours un brouillon ouvert) que le bug de profil colorimétrique ci-dessus a été attrapé. Une deuxième machine rattrape les tests qui ne passent qu’à cause de la machine sur laquelle ils tournent.
- **Contrôles négatifs :** la CI de l’app garde 22 copies volontairement cassées d’un script de nettoyage et 20 d’un script d’exécution des tests, chacune privée d’une vérification de sécurité, et les tests doivent échouer sur chacune. Le script de nettoyage supprime d’anciens builds et copies de travail sur un Mac : une seule vérification manquante pourrait supprimer ce qu’il ne faut pas. Si une copie cassée passe, c’est le test qui est cassé.
- **Un deuxième regard :** notre pratique est de faire vérifier un changement par un agent distinct avant de le fusionner, comme pour kit #242, et les changements qui touchent à la façon d’utiliser l’app passent d’abord par une revue de scénarios. Cela rattrape le « terminé » qui ne l’est pas, et le code qui marche, mais dans la mauvaise situation.
- **Une personne fusionne.** Chaque changement est relu et fusionné par la personne qui développe MarsDawn ; aucun agent ni bot ne fusionne quoi que ce soit.

## Ce que nous lui faisons subir

Ces filets ne valent que ce qu’on y jette. Voici quelques-unes des entrées que les tests donnent au moteur, et ce que chaque test garantit :

- **Des fichiers très volumineux.** Mesuré sur notre machine de test, en build release : un document de 2 Mo s’affiche en moins d’une seconde et demie, et un document de 5 Mo trop complexe à mettre en page s’ouvre quand même en texte brut en moins d’une seconde. Au-delà de 16 Mo, le fichier s’affiche en texte sans être analysé du tout.
- **Des centaines de milliers de lignes.** Environ 3 Mo de lignes d’un seul mot, près de 800 000, sont repérés comme trop lourds en cours de route : le moteur arrête de lire à cet endroit et affiche le fichier en texte brut.
- **Des balises jamais fermées.** Un mégaoctet de marques d’ouverture de section sans fermeture, ou des dizaines de milliers empilées les unes dans les autres, ne doit pas prendre plus d’environ deux fois le temps d’un mégaoctet de texte brut. Au-delà de huit niveaux, plus rien ne s’imbrique.
- **Des formules.** Une formule erronée affiche une erreur à sa place au lieu de casser la page. Une formule de plus de 10 000 caractères reste telle qu’elle est écrite, seules les 1 000 premières d’un document sont dessinées à la fois, et rien dans une formule ne peut devenir un lien, une image ou du balisage de page.
- **Du HTML hostile dans le Markdown.** Les scripts sont retirés et ne s’exécutent jamais, et les cadres intégrés sont enlevés avant que la page les affiche. Les images distantes restent désactivées tant que vous ne les autorisez pas, et même alors, seules les images sécurisées (HTTPS) se chargent. Dans une copie témoin, le filtre de scripts est retiré, et le test doit échouer sur elle.
- **Un fichier de thème hostile.** Il est refusé, et le message d’erreur ne répète jamais les caractères de contrôle cachés ni les liens du fichier. Les fichiers de thème de plus de 16 Ko ne sont même pas lus.

Rien de tout cela n’est gratuit. La limite de temps d’une exécution du moteur est passée de 30 minutes à 45, puis 50, puis 70, et maintenant à 90. macOS 15 a atteint deux fois la limite de 50 minutes alors que tous les tests passaient, puis a atteint 70 minutes à sa dernière étape, toutes les étapes précédentes ayant réussi.

## Quatre habitudes à reprendre

1. **Séparez l’agent qui écrit de l’agent qui vérifie.** Donnez au vérificateur le changement et ce que « terminé » veut dire, sans joindre l’explication de l’agent qui a écrit, et demandez-lui de lancer lui-même les tests et de dire ce qu’il n’a pas vérifié. Pour kit #242, l’agent vérificateur a lancé l’ancien test sur le MacBook Air pour le voir échouer avant de valider le nouveau. Cela coûte les tokens d’une deuxième session.
2. **Voyez chaque test échouer une fois.** Le vert ne vaut quelque chose que si vous avez vu ce même test passer au rouge quand ce qu’il vérifie était vraiment faux. Avant de faire confiance à une coche verte, cassez donc ce qu’elle protège (ou demandez à l’agent de le faire), voyez-la passer au rouge, remettez en place et voyez-la repasser au vert. Les agents savent très bien écrire des tests qui passent ; c’est justement pour cela qu’il faut les voir échouer.
3. **Lancez vos tests dans un deuxième environnement.** Pas de deuxième Mac ? Une matrice de CI avec deux versions de l’OS, ou avec un build debug et un build release, est un bon début. Vous cherchez les tests qui ne passent que par hasard.
4. **Considérez « aucun test lancé » comme un échec.** L’outil `unittest` de Python 3.9 se termine avec succès quand il ne trouve aucun test, si bien qu’une faute de frappe dans un chemin vous donne une coche verte. Notre CI lit le nombre de tests et échoue à zéro, et vérifie que le résumé indique « 0 failed », sans se fier au seul code de sortie. Nous avons ajouté ce contrôle après qu’une vérification indépendante a trouvé cette faille dans notre propre CI.

## En bref

Qu’une app ait été faite en vibe coding compte moins que de savoir si quelqu’un continue de la tester et de la maintenir. Cela vaut la peine de le vérifier au moment de choisir un logiciel : dit-il comment il est testé, et quand a-t-il été mis à jour pour la dernière fois ?

Laissez l’agent aller vite. Confiez la vérification à des tests qui mesurent la bonne chose, et à une personne qui lit le résultat.

## Pour aller plus loin

- Pourquoi une personne doit encore lire ce qu’un agent a écrit : [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](/fr/reviewing-ai-output/).
- Comment lire les plans et les rapports qu’un agent vous rend : [Lire ce que votre agent vous rend](/fr/reading-agent-output/).

## Sources

- Le test qui échouait et sa cause : [mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241).
- Le correctif et sa vérification indépendante : [mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242).
- L’essai de la CI sur un MacBook Air (brouillon ouvert), avec les temps d’exécution : [mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240).
- La CI du moteur d’export, avec l’historique de sa limite de temps dans les commentaires : [ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml).
- Le dépôt de l’app est privé ; les détails sur l’app ci-dessus viennent de son workflow de CI et de ses scripts de test.

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
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
