"""French copy for the MarsDawn site (#164, tracking #168), integrated for #162's plumbing.

The text is Grok's, from draft PR #171 (design/inbox/164-fr-pages.py and 164-fr-strings.md),
carried over unchanged; only the return shape is the plumbing's (see scripts/new_locale.py). Written
here and not in Grok's material: the privacy page's description, the hero window's label and its
Markdown-twin sentence. The privacy and support titles are the legal pages' own h1. Legal pages:
content/legal/<slug>.fr.md.
"""

# True: the build checks the shape, the legal pages, the hero snapshot and the images before it serves the locale.
COMPLETE = True


def build(k) -> dict:
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn : un éditeur Markdown pour Mac, avec aperçu en direct',
        "description": 'Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.',
        "intro": """
<section class="intro hero">
  <p class="kicker">Des outils de pionnier pour ceux qui construisent</p>
  <h1><span>Prenez la carte.</span> <span>Lisez l’aube.</span></h1>
  <p>Du Markdown pour les humains qui pilotent le travail des agents.</p>
</section>
""",
        "body": """
<h2 class="loop-title">Lisez ce que votre agent a écrit.</h2>
<ol class="loop-steps">
  <li><strong>L’agent écrit.</strong> Votre agent de code ou votre assistant d’écriture rédige le Markdown : un README, une spécification, des notes.</li>
  <li><strong>Vous relisez dans MarsDawn.</strong> Ouvrez le fichier et lisez-le mis en forme, avec les diagrammes Mermaid et le code en couleur, à côté de la source.</li>
  <li><strong>L’agent corrige.</strong> Demandez des modifications. Ouvrez le fichier révisé et lisez-le de la même façon.</li>
</ol>
<p><a href="/fr/reading-agent-output/">Comment relire ce que votre agent vous rend</a>.</p>
""",
    }
    pages['yours'] = {
        "title": 'Un éditeur Markdown pour Mac sans compte ni cloud · MarsDawn',
        "description": 'MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.',
        "intro": """
<section class="intro">
  <h1>Vos textes restent sur votre Mac.</h1>
  <p>MarsDawn n’a ni compte, ni synchronisation, ni cloud. L’app ouvre un fichier, vous écrivez, et elle enregistre le fichier là où vous l’avez choisi.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<ul>
  <li>Il n’y a aucun compte à créer ni aucune connexion.</li>
  <li>Rien n’est synchronisé dans un cloud. Vos documents restent là où vous les enregistrez.</li>
  <li>Rien n’est suivi. MarsDawn ne collecte aucune donnée vous concernant, et son étiquette de confidentialité sur l’App Store indique « Aucune donnée collectée ».</li>
  <li>Les images web restent bloquées jusqu’à ce que vous choisissiez de les charger : ouvrir un document n’indique donc jamais à un serveur que vous le lisez. Quand vous les chargez, c’est uniquement en https.</li>
  <li>Les images locales s’affichent dans l’aperçu dès que vous autorisez l’accès à leur dossier.</li>
</ul>
<p>Les détails se trouvent dans la <a href="/fr/privacy/">politique de confidentialité</a>.</p>
""",
    }
    pages['pay-once'] = {
        "title": 'Essayez gratuitement, puis payez une fois · MarsDawn',
        "description": 'MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.',
        "intro": """
<section class="intro">
  <h1>Essayez tout. Puis payez une fois.</h1>
  <p>MarsDawn se télécharge gratuitement. Lancez l’essai de 14 jours et toutes les fonctionnalités sont disponibles ; pour continuer ensuite, un achat unique de 4,99 USD le déverrouille. Il n’y a ni abonnement ni compte.</p>
</section>
""",
        "body": """
<h2>Comment ça marche</h2>
<ol class="loop-steps">
  <li><strong>Téléchargez-le gratuitement.</strong> MarsDawn se télécharge gratuitement sur le Mac App Store.</li>
  <li><strong>Essayez tout pendant 14 jours.</strong> Lancez l’essai et tout MarsDawn fonctionne pendant 14 jours : tous les thèmes et toutes les dispositions, l’export PDF et l’impression, ainsi que les actions Siri et Raccourcis. Coup d’œil dans le Finder fonctionne avec ou sans essai.</li>
  <li><strong>Déverrouillez-le une fois.</strong> Pour continuer ensuite, déverrouillez-le une fois pour 4,99 USD. C’est un achat intégré, pas un abonnement : rien ne se renouvelle et rien ne vous sera facturé plus tard.</li>
</ol>
<ul>
  <li>L’essai ne vous coûte rien non plus. À la fin, rien n’est acheté, sauf si vous choisissez de déverrouiller.</li>
  <li>Il n’y a pas de compte. MarsDawn ne vous demande jamais d’en créer un.</li>
</ul>
<h2>Ce qui fonctionne, et quand</h2>
<!--compare:pay-once-states-->
<p>Avant que vous lanciez l’essai, MarsDawn affiche l’offre d’essai. La lancer ne coûte rien.</p>
<p>Les fichiers PDF ouverts dans MarsDawn sont verrouillés de la même façon à la fin de l’essai.</p>
<h2>Si vous ne déverrouillez pas</h2>
<ul>
  <li>Après 14 jours, et tant que vous ne l’avez pas déverrouillé, vous ne pouvez plus lire, modifier, exporter ni imprimer de documents dans MarsDawn. Un document s’ouvre toujours, mais son contenu est masqué.</li>
  <li>Vos fichiers ne changent pas. Ce sont des fichiers ordinaires sur votre Mac, et Coup d’œil dans le Finder continue de les afficher.</li>
  <li>L’<a href="/fr/cli/">outil en ligne de commande <code>marsdawn</code></a>, gratuit, continue de les exporter en PDF, avec ou sans essai.</li>
  <li>Si un document est ouvert dans MarsDawn à la fin de l’essai, le texte saisi n’est pas perdu : utilisez Fichier ▸ Enregistrer sous… pour le garder.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Exporter du Markdown en PDF sur Mac, diagrammes compris · MarsDawn',
        "description": 'Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.',
        "intro": """
<section class="intro">
  <h1>Le PDF ressemble à la page que vous avez écrite.</h1>
  <p>Exportez en PDF ou imprimez, dans les couleurs claires de votre thème. Les diagrammes et le code en couleur sont conservés, et les sauts de page évitent de séparer ce qui va ensemble.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<ul>
  <li>Les diagrammes Mermaid sont dessinés dans le PDF.</li>
  <li>Les blocs de code gardent leur coloration syntaxique.</li>
  <li>Les sauts de page évitent de laisser un titre en bas de page ou de couper du code, des tableaux et des diagrammes.</li>
  <li>Quelle que soit la disposition. L’export fonctionne même quand seule la source est affichée.</li>
</ul>
<p>L’<a href="/fr/cli/">outil en ligne de commande marsdawn</a>, gratuit, utilise le même moteur d’export : un script ou un agent IA obtient le même PDF.</p>
""",
    }
    pages['native'] = {
        "title": 'Une app Markdown native pour Mac : onglets, Coup d’œil · MarsDawn',
        "description": 'Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.',
        "intro": """
<section class="intro">
  <h1>Construit avec les pièces du Mac.</h1>
  <p>Les fenêtres, les onglets, les menus et l’éditeur de texte sont ceux du Mac. La page mise en forme est dessinée par WebKit, le moteur de Safari.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<h3>Édition</h3>
<ul>
  <li>Dispositions source, partagée et aperçu, à une touche l’une de l’autre (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>Les deux volets défilent ensemble : le paragraphe que vous modifiez reste visible.</li>
  <li>Coloration syntaxique Markdown dans l’éditeur, assortie à votre thème de l’aperçu.</li>
</ul>
<h3>Le reste du Mac</h3>
<ul>
  <li>Fenêtres et onglets natifs, enregistrement automatique et historique des versions.</li>
  <li>Coup d’œil : appuyez sur Espace sur un fichier Markdown dans le Finder pour un aperçu, diagrammes compris.</li>
  <li>Siri et Raccourcis : commencer un nouveau document à partir d’un modèle, ajouter une ligne à la boîte de réception de vos notes ou rouvrir un document récent.</li>
  <li>Anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'Ce que MarsDawn ne fait pas · MarsDawn',
        "description": 'Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.',
        "intro": """
<section class="intro">
  <h1>Ce que MarsDawn ne fait pas.</h1>
  <p>Certaines choses sont absentes à dessein. Si vous avez besoin de l’une d’elles, mieux vaut le savoir maintenant qu’après l’achat.</p>
</section>
""",
        "body": """
<h2>Ce qui est laissé de côté</h2>
<h3>Appareils et personnes</h3>
<ul>
  <li><strong>Synchronisation :</strong> MarsDawn ne synchronise pas vos documents. Ils restent là où vous les enregistrez ; pour en utiliser un sur un autre Mac, gardez-le dans un dossier que vous synchronisez déjà.</li>
  <li><strong>iPhone et iPad :</strong> il n’existe pas d’app pour eux ; MarsDawn est fait pour le Mac.</li>
  <li><strong>Partage :</strong> il n’y a ni comptes ni édition partagée, car MarsDawn est conçu pour une personne, sur son propre Mac.</li>
  <li><strong>Système :</strong> MarsDawn nécessite macOS 26 ou version ultérieure.</li>
</ul>
<h3>Fichiers et fonctionnalités</h3>
<ul>
  <li><strong>Édition :</strong> vous écrivez le Markdown à gauche et lisez la page à droite ; la page elle-même n’est pas modifiable.</li>
  <li><strong>Formats :</strong> MarsDawn exporte en PDF et imprime, mais n’exporte pas de fichiers Word.</li>
  <li><strong>Autres fichiers :</strong> les fichiers texte brut et les PDF s’ouvrent en lecture seule.</li>
  <li><strong>Thèmes :</strong> l’app est livrée avec Aube, Classique, Moderne et Vif, chacun en clair et en sombre. D’autres se trouvent dans la <a href="/fr/themes/gallery/">galerie de thèmes</a> : installez-en un depuis Réglages › Apparence › Obtenir plus de thèmes…, ou <a href="/fr/themes/new/">créez le vôtre</a> dans le navigateur. Un thème, ce sont des couleurs et des réglages de style, pas un plug-in.</li>
  <li><strong>Plug-ins :</strong> MarsDawn n’a ni plug-ins ni extensions.</li>
</ul>
<h2>Après l’essai</h2>
<p>Si vous ne déverrouillez pas MarsDawn à la fin de l’essai de 14 jours, vous ne pouvez plus y lire, modifier, exporter ni imprimer de documents : ils s’ouvrent avec leur contenu masqué. Vos fichiers restent tels quels, Coup d’œil les affiche toujours, et l’outil en ligne de commande gratuit les exporte toujours. La <a href="/fr/pay-once/">page sur l’essai et le déverrouillage</a> présente les trois étapes côte à côte.</p>
""",
    }
    pages['changelog'] = {
        "title": 'Historique des versions · MarsDawn',
        "description": 'Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.',
        "body": """
<section class="intro">
  <h1>Historique des versions</h1>
  <p>Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn. Une version de MarsDawn du Mac App Store n’est mentionnée ici que lorsqu’elle a sa propre ligne. Les versions antérieures à 0.5.1 ne sont pas listées.</p>
</section>

<h2>marsdawn 0.6.3</h2>
<p>6 octobre 2026. MarsDawn est sur le Mac App Store.</p>
<ul>
  <li>Quand l’app n’est pas installée, <code>marsdawn open</code> renvoie vers MarsDawn sur le Mac App Store.</li>
  <li>Le README et la skill pour agents expliquent <code>marsdawn open .</code> et <code>--folder</code> : MarsDawn 1.0.0 affiche le dossier dans la barre latérale de la fenêtre.</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>26 septembre 2026. Corrections Mermaid, lignes des erreurs de diagramme et installation de la skill.</p>
<ul>
  <li>Dans un diagramme de séquence, le libellé d’un message qui croise les lignes de vie d’autres participants reste lisible, dans l’aperçu comme dans les PDF exportés.</li>
  <li><code>marsdawn export</code> gère les documents remplis de diagrammes Mermaid. Un document de 50 diagrammes, qui échouait auparavant avec le code 5, s’exporte désormais.</li>
  <li><code>marsdawn export --json</code> ajoute <code>diagramErrorDetails</code>, avec les numéros de ligne de chaque erreur de diagramme : où le diagramme commence dans votre document et, quand Mermaid en indique une, la ligne de l’erreur elle-même.</li>
  <li><code>marsdawn skill --install</code> installe la skill pour Claude Code dans <code>~/.claude/skills/marsdawn/SKILL.md</code>, ou dans un autre dossier avec <code>--dir</code>. Il laisse intact un fichier identique et ne remplace un fichier différent qu’avec <code>--force</code>. Sinon, il se termine avec le code 64 (<code>skill_differs</code>) sans rien modifier.</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>25 septembre 2026. État du dossier, erreurs Mermaid complètes et petites corrections.</p>
<ul>
  <li><code>marsdawn open --folder</code> peut indiquer ce qu’il est advenu du dossier. Avec une app qui répond, il attend jusqu’à <code>--wait</code> secondes (2 par défaut), et <code>--json</code> donne un état comme <code>attached</code> ou <code>needsUser</code>.</li>
  <li>Un diagramme Mermaid qui ne s’analyse pas affiche le message d’erreur complet de Mermaid au lieu de sa seule première ligne, avec le numéro de ligne compté depuis le début de votre document.</li>
  <li>La recherche de la fin d’un bloc front matter s’arrête après 1 000 lignes : un bloc non fermé n’entraîne plus le parcours du reste d’un long document.</li>
  <li>Une app peut donner au lien de retour d’une note de bas de page un libellé traduit pour l’export PDF et l’impression. Le libellé n’est pas imprimé sur la page, et <code>marsdawn export</code> garde le libellé anglais.</li>
  <li>La copie intégrée de highlight.js est désormais épinglée par version, source et SHA-256, comme KaTeX et Mermaid.</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>24 septembre 2026. Notes de bas de page, contraste et dossiers.</p>
<ul>
  <li>Les notes de bas de page s’affichent dans les PDF exportés : appels numérotés, avec les notes après le corps du texte.</li>
  <li>Chaque thème respecte le contraste WCAG AA, en clair comme en sombre. Classique est désormais en noir et blanc.</li>
  <li><code>marsdawn skill</code> affiche la skill pour agents qui correspond au marsdawn installé.</li>
  <li><code>marsdawn open</code> se termine avec le code 6 (<code>app_cannot_open_folders</code>) quand le MarsDawn trouvé ne peut pas afficher de dossier, au lieu d’annoncer un succès.</li>
  <li>Les espaces réservés dessinés dans les pages exportées existent aussi en allemand, français, espagnol et coréen.</li>
  <li>Un espace réservé d’image n’affiche plus le chemin absolu caché derrière un très long chemin relatif.</li>
  <li><code>MARSDAWN_APP_PATH</code> n’est utilisé que s’il pointe vers une app MarsDawn.</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>19 septembre 2026. Export PDF, et ouverture d’un fichier depuis la ligne de commande.</p>
<ul>
  <li>La couche de texte d’un PDF exporté est réparée pour le chinois, le japonais et le coréen.</li>
  <li><code>marsdawn open --background</code> ouvre un fichier sans faire passer MarsDawn au premier plan.</li>
  <li><code>marsdawn open</code> accepte un dossier, et MarsDawn l’affiche dans la barre latérale de la fenêtre (MarsDawn 1.0.0 et versions ultérieures).</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn : un outil en ligne de commande gratuit pour passer de Markdown à PDF · MarsDawn',
        "description": 'L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.',
        "body": f"""
<section class="intro">
  <h1>Ligne de commande</h1>
  <p>L’outil en ligne de commande gratuit <code>marsdawn</code> : exportez du Markdown en PDF depuis un shell ou un agent LLM et, si l’app MarsDawn est installée, ouvrez-y des fichiers.</p>
</section>

<div class="summary"><p><strong>marsdawn est gratuit et distribué séparément du Mac App Store.</strong> Installez-le avec Homebrew : sur un Mac avec puce Apple, il arrive prêt à l’emploi. <code>export</code> fonctionne seul ; <code>open</code> nécessite l’app MarsDawn.</p></div>

<p>Vous appelez marsdawn depuis un agent IA ou un script ? Consultez <a href="/fr/cli/agents/">marsdawn pour les agents</a> pour la sortie JSON, ses schémas et tous les codes de sortie, ou <a href="/fr/cli/mcp/">le serveur MCP</a> si votre agent appelle plutôt des outils via MCP.</p>

<h2>Installation</h2>
<p>Avec <a href="https://brew.sh">Homebrew</a> :</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>Vous utilisez un agent de code ? <a href="/fr/cli/skill/">Ajoutez la skill marsdawn</a> : un seul fichier qui lui apprend à ouvrir ce qu’il a écrit dans MarsDawn pour que vous le relisiez, et à exporter des PDF.</p>
<p>Sur un Mac avec puce Apple, Homebrew installe une copie précompilée en quelques secondes, sans rien d’autre à installer. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure (Swift 6.2). L’outil fonctionne sous macOS 15 ou version ultérieure.</p>
<p>Vous pouvez aussi le compiler à partir des <a href="{k.KIT_URL}">sources</a> avec Swift Package Manager :</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Vérifiez votre version avec <code>marsdawn --version</code>.</p>

<h2>Commandes</h2>

<h3>marsdawn open</h3>
<p>Ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour les relire. L’app doit être installée : sans elle, <code>marsdawn open</code> se termine avec le code 3 et indique que MarsDawn n’est pas installé. <code>export</code> n’a pas besoin de l’app. L’app est disponible sur le <a href="{k.LISTING_URL}">Mac App Store</a>.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code> : demande à MarsDawn d’aller à cette ligne. Une colonne après, comme dans <code>notes.md:120:8</code>, est ignorée. Si un fichier portant le nom complet existe, l’argument désigne ce fichier.</li>
  <li><code>--line &lt;n&gt;</code> : la même chose pour un seul fichier, et le moyen de demander une ligne pour un chemin qui se termine lui-même par deux-points et des chiffres. Exige exactement un fichier.</li>
  <li>Les lignes vont de 1 à 999999999.</li>
  <li>MarsDawn 1.0 ouvre le fichier à cette ligne.</li>
  <li>Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre plutôt que comme un document : <code>marsdawn open .</code> affiche le dossier courant. <code>--folder &lt;path&gt;</code> fait de même en plus de fichiers. La barre latérale d’une fenêtre affiche un seul dossier, donc en nommer deux est une erreur d’utilisation.</li>
  <li><code>--background</code> : ouvrir sans faire passer MarsDawn au premier plan.</li>
  <li><code>--json</code> : afficher un résultat JSON au lieu de texte.</li>
</ul>
<p>Les lignes sont arrivées avec marsdawn 0.3.0, les dossiers et <code>--background</code> avec la 0.5.1.</p>

<h3>marsdawn export</h3>
<p>Convertit un fichier Markdown en PDF paginé, avec le même moteur d’export que celui de MarsDawn. Il n’a pas besoin de l’app MarsDawn. Les images relatives sont résolues par rapport au dossier du fichier d’entrée.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code> : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code> : la palette claire du thème de l’aperçu. Par défaut, <code>$MARSDAWN_THEME</code>, puis <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code> : format du papier. Par défaut, <code>a4</code>.</li>
  <li><code>--allow-remote-images</code> : charger les images web pendant le rendu. Désactivé par défaut.</li>
  <li><code>--force</code> : remplacer le fichier de sortie s’il existe déjà.</li>
  <li><code>--json</code> : afficher un résultat JSON au lieu de texte.</li>
</ul>

<h2>La variable $MARSDAWN_THEME</h2>
<p>Quand <code>--theme</code> n’est pas passé, <code>export</code> lit la variable d’environnement <code>$MARSDAWN_THEME</code>. Sa valeur doit être <code>dawn</code>, <code>classic</code>, <code>modern</code> ou <code>vivid</code> ; toute autre valeur revient à <code>dawn</code>. La CLI ne lit pas le réglage de thème de l’app, car lire le conteneur d’une autre app peut déclencher une demande d’autorisation de confidentialité de macOS.</p>

<h2>Écraser des fichiers</h2>
<p><code>export</code> refuse de remplacer un fichier de sortie existant, sauf si vous passez <code>--force</code>.</p>

<h2>Codes de sortie</h2>
<!--exit-table-->
<ul>
  <li><code>0</code> : succès.</li>
  <li><code>2</code> : entrée introuvable.</li>
  <li><code>3</code> : MarsDawn n’est pas installé (<code>open</code> uniquement).</li>
  <li><code>4</code> : la sortie existe déjà (passez <code>--force</code>).</li>
  <li><code>5</code> : échec de l’export.</li>
  <li><code>6</code> : ce MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert (<code>open</code> uniquement).</li>
  <li><code>64</code> : erreur d’utilisation, notamment une ligne hors limites, <code>--line</code> avec plus d’un fichier ou avec un dossier, ou plus d’un dossier.</li>
</ul>

<h2>Sortie --json</h2>
<p>En cas de succès, <code>marsdawn open --json</code> affiche <code>ok</code>, <code>opened</code> (une liste avec le <code>path</code> de chaque fichier, plus <code>line</code> quand une ligne a été demandée), <code>app</code> (le chemin de l’app) et, quand un dossier a été donné, <code>folder</code>. <code>marsdawn export --json</code> affiche <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> et <code>diagramErrors</code>. En cas d’échec, les deux affichent <code>ok</code>, <code>error</code> et <code>message</code>.</p>
""",
    }

    figures = {
        'index': {"alt": 'MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.', "callouts": []},
        'yours': {"alt": 'MarsDawn affiche un document avec le thème Classique, l’aperçu occupant toute la fenêtre.',
                  "callouts": ['Un fichier sur votre Mac, enregistré là où vous le choisissez.', 'La barre d’outils ne contient que des thèmes et des dispositions ; il n’y a rien à quoi se connecter.']},
        'pay-once': {"alt": 'MarsDawn avec le thème Vif, la source Markdown à gauche et la page mise en forme à droite.',
                     "callouts": ['Coloration Markdown dans l’éditeur, incluse.', 'Tous les thèmes et toutes les dispositions sont inclus.', 'Diagrammes Mermaid, inclus.', 'Coloration du code, incluse.']},
        'pdf': {"alt": 'Un PDF exporté depuis MarsDawn, ouvert dans sa visionneuse PDF avec les vignettes des pages.',
                "callouts": ['Les diagrammes Mermaid, dessinés dans le PDF.', 'Le code garde sa coloration.']},
        'native': {"alt": 'MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.',
                   "callouts": ['Une fenêtre Mac native.', 'L’éditeur de texte du Mac, avec la coloration Markdown.', '⌘1 source, ⌘2 partagé, ⌘3 aperçu.', 'La page se met à jour pendant la saisie.']},
        'limits': {"alt": 'MarsDawn en mode sombre, la source Markdown à gauche et la page mise en forme à droite.',
                   "callouts": ['Un document par fenêtre, sur ce Mac.', 'C’est ici que vous écrivez le Markdown.', 'La barre d’outils contient les thèmes et les dispositions, et il n’y a pas de menu de plug-ins.', 'La page sert à lire, pas à modifier.']},
    }
    home = {
        "cta_cli": 'Installer la CLI gratuite',
        "cta_try": 'Télécharger et essayer',
        "cta_store": 'Voir sur le Mac App Store',
        "install_h": 'À faire dès maintenant',
        "install_lede": 'L’outil en ligne de commande gratuit <code>marsdawn</code> est disponible dès aujourd’hui. Installez-le avec Homebrew :',
        "install_caps": [
            '<code>marsdawn export</code> transforme un fichier Markdown en PDF, rendu comme l’aperçu de MarsDawn. Il n’a pas besoin de l’app.',
            '<code>marsdawn open</code> ouvre des fichiers dans l’app MarsDawn pour que vous les relisiez.',
            '<code>--json</code> donne aux scripts et aux agents des résultats qu’ils peuvent analyser.',
        ],
        "proof_h": 'L’app, telle qu’elle est',
    }
    compare_tables = {
        'pay-once-states': {
            "head": ['', 'Essai (jours 1 à 14)', 'Essai terminé, non déverrouillé', 'Déverrouillé'],
            "rows": [
                ['Ouvrir un document dans MarsDawn', 'Oui', 'S’ouvre, contenu masqué', 'Oui'],
                ['Lire et modifier dans MarsDawn (source, aperçu, Mermaid, formules)', 'Oui', 'Non', 'Oui'],
                ['Exporter en PDF et imprimer depuis MarsDawn', 'Oui', 'Non', 'Oui'],
                ['Garder le texte saisi avec Fichier ▸ Enregistrer sous…', 'Oui', 'Oui, dans une fenêtre ouverte à la fin de l’essai', 'Oui'],
                ['Actions Siri et Raccourcis', 'Oui', 'Non', 'Oui'],
                ['Coup d’œil dans le Finder, avec diagrammes Mermaid et formules', 'Oui', 'Oui, sans changement', 'Oui'],
                ['<code>marsdawn export</code> (outil en ligne de commande gratuit) : PDF avec diagrammes et formules', 'Oui', 'Oui, sans changement', 'Oui'],
                ['Vos fichiers sur le disque', 'Tels que vous les avez enregistrés', 'Tels que vous les avez enregistrés ; le verrouillage ne les modifie jamais', 'Tels que vous les avez enregistrés'],
            ],
        },
    }
    exit_table_head = ['Code', 'Signification', 'Que faire']
    exit_remedy = {
        "0": 'Avec <code>--json</code>, lire l’unique ligne JSON sur stdout',
        "2": 'Vérifier le chemin et le nom du fichier',
        "3": 'Installer l’app, ou utiliser <code>export</code>, qui n’en a pas besoin',
        "4": 'Passer <code>--force</code> pour le remplacer, ou <code>-o</code> pour écrire ailleurs',
        "5": 'Lire <code>message</code> dans le résultat JSON',
        "64": 'Corriger l’option ou la valeur ; cette erreur est du texte sur stderr, même avec <code>--json</code>',
    }
    # markdown-to-pdf shows /assets/cli/plan-fr.png, which does not exist yet. Before this ships,
    # export example_plan with marsdawn 0.5.0 the way EXAMPLE_PLAN's comment in build_pages.py
    # describes, or fall back to plan-en.png with EXAMPLE_PLAN['en'].
    example_plan = '# Plan : des exports plus rapides\n\nUn agent a rédigé ce plan. Vous le relisez, puis vous le transformez en PDF.\n\n## Étapes\n\n| Étape | Responsable | État |\n|-------|-------------|------|\n| Mesurer les pages lentes | Agent | Fait |\n| Mettre en cache les diagrammes rendus | Agent | En relecture |\n\nL\'objectif est $t < 2\\,\\text{s}$ pour un document de 50 pages :\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Brouillon --> Relecture --> Publication\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'

    pages['markdown-to-pdf'] = {
        "title": 'Markdown en PDF sur Mac, en ligne de commande · MarsDawn',
        "description": 'Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.',
        "body": f"""
<section class="intro">
  <h1>Markdown en PDF sur Mac, en ligne de commande.</h1>
  <p>L’outil gratuit <code>marsdawn</code> transforme un fichier Markdown en PDF en une seule commande. Les tableaux, les formules, les diagrammes Mermaid et le code coloré sortent tels qu’on les lit dans la source, et rien d’autre n’est nécessaire, pas même l’app MarsDawn.</p>
</section>
<h2>L’installer</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Sur un Mac à puce Apple, Homebrew installe une copie précompilée en quelques secondes. Sur un Mac Intel, il compile à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure. L’outil fonctionne sous macOS 15 ou version ultérieure, et <code>marsdawn --version</code> affiche la version installée.</p>
<h2>Enregistrer un document</h2>
<p>Collez ceci dans un fichier nommé <code>plan.md</code> :</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>L’exporter</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>Il écrit <code>plan.pdf</code> à côté de la source et indique où il l’a placé :</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>Voici cette page, capturée lors d’une véritable exécution de <code>marsdawn</code> 0.5.0 :</p>
<p><img class="pdf-page" src="/assets/cli/plan-fr.png" alt="Le PDF exporté : le titre, un tableau d’étapes, une formule dans le texte et une formule centrée, un diagramme Brouillon, Relecture, Publication et une ligne de Swift colorée." width="989" height="930"></p>
<h2>Choisir un thème, un format de papier et un nom de fichier</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code> : dawn, classic, modern ou vivid, dans les couleurs claires du thème. Sans cette option, <code>export</code> utilise <code>$MARSDAWN_THEME</code>, sinon dawn.</li>
  <li><code>--paper</code> : a4 ou letter. La valeur par défaut est a4.</li>
  <li><code>-o</code> : où écrire le PDF, au lieu de le placer à côté de la source.</li>
  <li><code>--allow-remote-images</code> : charge les images du web pendant le rendu. Elles restent désactivées si vous ne le précisez pas.</li>
</ul>
<h2>Si ça ne fonctionne pas</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew compile <code>marsdawn</code> à partir des sources, comme sur un Mac Intel. Installez Xcode 26 ou version ultérieure depuis l’App Store, puis relancez l’installation.</li>
  <li><code>marsdawn: No such file: …</code> Le chemin ne mène pas à un fichier. Vérifiez le nom, ou lancez la commande depuis le dossier qui contient le fichier.</li>
  <li><code>… already exists. Pass --force to replace it.</code> Un PDF portant ce nom existe déjà. Ajoutez <code>--force</code> pour le remplacer, ou <code>-o</code> pour l’écrire ailleurs.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> Le thème ou le format de papier n’est pas reconnu. Les thèmes sont dawn, classic, modern et vivid ; le papier est a4 ou letter.</li>
</ul>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Toutes les options et le JSON produit : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Pour qu’un agent de code le fasse à votre place : <a href="/fr/cli/skill/">la compétence d’agent marsdawn</a>.</li>
  <li>Les quatre thèmes d’aperçu, et la direction que prend l’export PDF : <a href="/fr/themes/">thèmes d’aperçu et export PDF</a>.</li>
  <li>Remettre le PDF à quelqu’un qui n’utilise pas Markdown : <a href="/fr/sharing-exported-pdfs/">partager un PDF</a>.</li>
</ul>
""",
    }

    pages['view-markdown-on-mac'] = {
        "title": 'Comment afficher un fichier Markdown sur Mac · MarsDawn',
        "description": 'Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>Comment afficher un fichier Markdown sur Mac.</h1>
  <p>Un fichier <code>.md</code> est du texte brut. Les titres, les mots en gras, les tableaux et les diagrammes y sont écrits sous forme de marques : <code>#</code> pour un titre, <code>**</code> autour du gras, des barres verticales pour un tableau, un bloc de code <code>mermaid</code> pour un diagramme. Ouvrez-le dans un éditeur de texte brut et vous lisez les marques. Pour lire la page telle que l’auteur l’a voulue, il faut qu’un outil en fasse le rendu.</p>
</section>
<h2>Dès aujourd’hui, gratuitement : en faire un PDF</h2>
<p>L’outil en ligne de commande gratuit <code>marsdawn</code> fait le rendu d’un fichier Markdown en PDF, que n’importe quel Mac peut ouvrir. Les tableaux, les formules, les diagrammes Mermaid et le code coloré sont rendus, et rien d’autre n’est nécessaire, pas même l’app MarsDawn.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> écrit <code>notes.pdf</code> à côté du fichier Markdown, et <code>open</code> l’affiche dans votre lecteur PDF. macOS 15 ou version ultérieure est requis. Le pas-à-pas, avec une vraie page exportée, se trouve sur <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</p>
<h2>Le lire dans MarsDawn</h2>
<p>MarsDawn est un éditeur Markdown pour Mac, sur le Mac App Store. Ouvrez un fichier <code>.md</code> et lisez la page rendue à côté de la source :</p>
<ul>
  <li>L’aperçu se met à jour pendant la saisie, et les deux volets défilent ensemble.</li>
  <li>Les organigrammes et diagrammes de séquence Mermaid sont dessinés dans l’aperçu, et les blocs de code sont colorés.</li>
  <li>Dans le Finder, appuyez sur Espace sur un fichier Markdown pour un aperçu Coup d’œil, diagrammes compris.</li>
  <li>Quand vous voulez modifier quelque chose, la source est juste là. MarsDawn est un éditeur, pas seulement une visionneuse.</li>
</ul>
<p>Si un agent IA a rédigé le fichier, c’est la boucle pour laquelle MarsDawn est conçu : l’agent écrit, vous lisez le rendu, et il révise. Consultez <a href="/fr/">la page d’accueil</a>, ainsi que <a href="/fr/cli/agents/">marsdawn pour les agents</a> pour laisser un agent ouvrir des fichiers à votre place. Pour comprendre pourquoi cette lecture compte et comment relire un plan, consultez <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a> et <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</p>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Toutes les options de l’outil en ligne de commande : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Ce que MarsDawn ne fait pas : <a href="/fr/limits/">la liste</a>.</li>
  <li>Lire du Markdown plutôt dans VS Code, un navigateur ou Claude Desktop : <a href="/fr/vs/markdown-preview-tools/">la comparaison</a>.</li>
</ul>
""",
    }

    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer ou MarsDawn : une visionneuse ou un éditeur · MarsDawn',
        "description": 'MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer ou MarsDawn.</h1>
  <p>Ce sont deux apps Mac pour lire du Markdown rendu. MacMD Viewer ouvre un fichier <code>.md</code> et affiche la page finie ; il ne permet pas de la modifier. MarsDawn place un éditeur à côté du même type d’aperçu rendu, pour écrire et relire dans une seule fenêtre. Voici leurs différences, fonction par fonction.</p>
</section>
<h2>Si vous devez seulement lire, pas modifier</h2>
<p>Si votre travail consiste uniquement à lire du Markdown écrit par d’autres, sans jamais toucher à la source, MacMD Viewer est un choix raisonnable : il est conçu exactement pour cela, il est disponible dès maintenant et fonctionne sur des versions plus anciennes de macOS. MarsDawn vaut la peine dès que la lecture n’est pas tout le travail, car le Markdown d’un agent revient en général pour une nouvelle passe.</p>
<h2>Ce que fait chaque app</h2>
<!--compare:macmd-features-->
<h2>Prix et mode d’achat</h2>
<!--compare:macmd-buying-->
<h2>Essayez-le gratuitement dès aujourd’hui</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fait aussi le rendu de n’importe quel fichier Markdown en PDF, avec les diagrammes Mermaid et le code coloré, et rien d’autre n’est nécessaire :</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Le pas-à-pas complet : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Ce que MarsDawn ne fait pas : <a href="/fr/limits/">la liste</a>.</li>
  <li>Toutes les options de l’outil en ligne de commande : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Par rapport à la lecture du Markdown dans VS Code, un navigateur ou Claude Desktop : <a href="/fr/vs/markdown-preview-tools/">la comparaison</a>.</li>
</ul>
""",
    }

    compare_tables['macmd-features'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Modification', 'Lecture seule, par choix', 'Modifie la source, avec la page rendue à côté'],
            ['Thèmes d’aperçu', '12 thèmes de document', '4 thèmes, chacun avec une palette claire et une palette sombre'],
            ['Diagrammes et maths', 'Mermaid et coloration du code ; sa fiche ne mentionne pas les maths', 'Mermaid, coloration du code et maths KaTeX'],
            ['Coup d’œil dans le Finder', 'Oui', 'Oui'],
            ['PDF et impression', 'Oui', 'Oui'],
            ['Configuration requise', 'macOS 14 (Sonoma) ou version ultérieure', 'macOS 26 (Tahoe) ou version ultérieure'],
            ['Langues de l’interface', 'Non précisé dans ses propres documents', '{langs}'],
        ],
    }
    compare_tables['macmd-buying'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Où l’acheter', 'Son propre site, Homebrew ou Setapp ; pas le Mac App Store', 'Uniquement sur le Mac App Store'],
            ['Prix', '19,99 USD une seule fois, pour un Mac ; les packs multi-Mac coûtent plus cher', 'Téléchargement gratuit, puis 4,99 USD une seule fois'],
            ['L’essayer d’abord', 'Pas d’essai ; garantie de remboursement de 14 jours pour les achats directs', 'Un essai gratuit de 14 jours'],
            ['Remboursements et mises à jour', 'Via son propre site', 'Via Apple'],
            ['Compte requis', 'Non', 'Non'],
        ],
    }

    schema_notes = {
        "export": "succès de export",
        "open": "succès de open, marsdawn 0.5.1 et versions ultérieures, y compris un dossier affiché dans la barre latérale",
        "open_v2": "succès de open, marsdawn 0.3.0 à 0.5.0",
        "error": "échec, pour les deux commandes, marsdawn 0.5.2 et versions ultérieures",
        "open_v1": "succès de open, marsdawn 0.2.x, où <code>opened</code> était une liste de chemins",
        "error_v1": "échec, pour les deux commandes, marsdawn 0.5.1 et versions antérieures",
    }

    pages['cli/agents'] = {
        "title": 'marsdawn pour les agents : Markdown en PDF depuis des scripts · MarsDawn',
        "description": 'Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.',
        "body": f"""
<section class="intro">
  <h1>marsdawn pour les agents</h1>
  <p>Une référence pour les agents IA et les scripts qui appellent l’outil en ligne de commande <code>marsdawn</code>. Chaque exemple de cette page a été exécuté avec l’outil compilé à partir des sources actuelles.</p>
</section>

<div class="summary"><p><strong>Pour convertir un fichier Markdown en PDF, lancez <code>marsdawn export notes.md --json</code> et lisez un objet JSON sur stdout.</strong> Les diagrammes Mermaid et le code coloré sont rendus de la même façon que dans l’app MarsDawn. <code>export</code> n’a pas besoin de l’app ; <code>open</code>, si.</p></div>

<h2>Ce qu’il fait</h2>
<ul>
  <li><code>export</code> fait le rendu d’un fichier Markdown en un PDF paginé, avec le même moteur d’export que l’app MarsDawn. Aucune fenêtre ne s’ouvre.</li>
  <li><code>open</code> ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour qu’une personne les relise ; il peut indiquer la ligne à laquelle chaque fichier doit s’ouvrir et afficher un dossier dans la barre latérale de la fenêtre.</li>
</ul>

<h2>Ce qu’il ne fait pas</h2>
<ul>
  <li>Il ne lit pas le Markdown depuis stdin. Passez un chemin de fichier.</li>
  <li>Il n’écrit pas le PDF sur stdout. Le PDF va toujours dans un fichier ; stdout ne contient que le résultat.</li>
  <li>Il ne remplace pas un fichier existant, sauf si vous passez <code>--force</code>.</li>
  <li>Il ne charge pas d’images depuis le web, sauf si vous passez <code>--allow-remote-images</code>, et uniquement en https.</li>
  <li><code>open</code> ne fonctionne pas sans l’app MarsDawn installée ; il se termine avec le code 3. <code>export</code> n’a pas besoin de l’app. L’app est sur le <a href="{k.LISTING_URL}">Mac App Store</a>.</li>
  <li>MarsDawn 1.0 ouvre le fichier à la ligne indiquée par <code>open</code>.</li>
  <li>Il ne fonctionne que sous macOS.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Écrit <code>notes.pdf</code> à côté de <code>notes.md</code>. Options :</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code> : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code> : la palette claire du thème. Par défaut <code>$MARSDAWN_THEME</code>, sinon <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code> : format du papier. Par défaut <code>a4</code>.</li>
  <li><code>--allow-remote-images</code> : charge les images https du web pendant le rendu.</li>
  <li><code>--force</code> : remplace le fichier de sortie s’il existe.</li>
  <li><code>--json</code> : affiche un objet JSON sur stdout au lieu de texte.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Succès, code de sortie 0 :</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code> : chemin absolu du PDF écrit.</li>
  <li><code>pages</code> : nombre de pages.</li>
  <li><code>theme</code> et <code>paper</code> : les valeurs utilisées.</li>
  <li><code>diagramErrors</code> : un message par diagramme Mermaid dont le rendu a échoué. Le PDF est tout de même écrit.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> indique la ligne à laquelle s’ouvrir. Une colonne après, comme dans <code>notes.md:120:8</code>, est ignorée. Un argument qui désigne un fichier existant est toujours ce nom de fichier entier : un fichier nommé <code>weird:12</code> s’ouvre donc tel quel.</li>
  <li><code>--line &lt;n&gt;</code> indique la ligne pour un seul fichier, y compris un chemin qui se termine lui-même par deux-points et des chiffres. Il faut exactement un fichier.</li>
  <li>Les lignes vont de 1 à 999999999. Toute autre valeur est une erreur d’utilisation.</li>
  <li>Les lignes ont été ajoutées dans marsdawn 0.3.0. MarsDawn 1.0 ouvre le fichier à cette ligne.</li>
  <li>Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre et non comme document : <code>marsdawn open .</code> affiche donc le dossier courant ; <code>--folder &lt;path&gt;</code> fait de même en plus des fichiers. La barre latérale d’une fenêtre affiche un seul dossier : en indiquer deux est une erreur d’utilisation, tout comme utiliser <code>--folder</code> deux fois, même pour le même dossier ; le même dossier redonné en argument compte une seule fois. <code>--line</code> avec un dossier est une erreur d’utilisation, puisqu’un dossier n’a pas de ligne. Il n’y a pas de <code>-a</code> : le passer est une erreur d’utilisation qui renvoie à <code>--folder</code>.</li>
  <li><code>--background</code> ouvre sans faire passer MarsDawn au premier plan, pour un agent qui ouvre des fichiers pendant que la personne travaille ailleurs. Le JSON est le même dans les deux cas.</li>
  <li>Les dossiers et <code>--background</code> ont été ajoutés dans marsdawn 0.5.1.</li>
</ul>
<p>Succès, code de sortie 0 :</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code> : un objet par fichier, dans l’ordre donné. <code>path</code> est le chemin absolu du fichier ; <code>line</code> n’apparaît que si une ligne a été demandée.</li>
  <li><code>app</code> : chemin de l’app MarsDawn qui les a ouverts.</li>
</ul>
<p>Avec un dossier (marsdawn 0.5.1 et versions ultérieures), code de sortie 0 :</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code> : présent seulement si un dossier a été donné. <code>path</code> est son chemin absolu. <code>requested</code> vaut toujours <code>true</code> : marsdawn a demandé à MarsDawn d’afficher le dossier, mais ne peut pas savoir si la barre latérale l’affiche, car l’app peut d’abord demander l’accès à la personne. Signalez-le comme demandé, pas comme fait.</li>
  <li><code>opened</code> est vide si seul un dossier a été donné.</li>
</ul>
<p>marsdawn 0.2.x affichait <code>opened</code> sous forme de liste de chemins. Vérifiez <code>marsdawn --version</code> si vous devez gérer les deux.</p>

<h2>Ouvrir les fichiers à mesure que Claude Code les modifie</h2>
<p>Un <a href="https://code.claude.com/docs/en/hooks">hook Claude Code</a> facultatif : après que Claude a écrit ou modifié un fichier Markdown, il ouvre ce fichier dans MarsDawn en arrière-plan, une fois par fichier et par session. Il est désactivé tant que vous ne l’ajoutez pas, projet par projet, car une fenêtre que vous n’avez pas demandée détourne l’attention. Il exécute une commande shell et ne coûte aucun token de modèle.</p>
<p>Il nécessite marsdawn 0.5.1 ou version ultérieure, pour <code>--background</code>, ainsi que l’app MarsDawn.</p>
<p>Enregistrez ceci sous <code>.claude/hooks/marsdawn-open.sh</code> dans votre projet, et rendez-le exécutable avec <code>chmod +x</code> :</p>
<pre><code>#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2&gt;/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2&gt;/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || {{ [ -x /opt/homebrew/bin/marsdawn ] &amp;&amp; echo /opt/homebrew/bin/marsdawn; }}) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${{TMPDIR:-/tmp}}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2&gt;/dev/null &amp;&amp; exit 0
echo "$file" &gt;&gt; "$seen"

"$marsdawn" open --background "$file" &gt;/dev/null 2&gt;&amp;1 || true
exit 0</code></pre>
<p>Ajoutez ensuite le hook à <code>.claude/settings.json</code> dans le projet, ou à <code>.claude/settings.local.json</code> pour le garder pour vous :</p>
<pre><code>{{
  "hooks": {{
    "PostToolUse": [
      {{
        "matcher": "Write|Edit",
        "hooks": [
          {{ "type": "command", "command": "\\"$CLAUDE_PROJECT_DIR\\"/.claude/hooks/marsdawn-open.sh" }}
        ]
      }}
    ]
  }}
}}</code></pre>
<ul>
  <li>Il s’exécute après les outils Write et Edit de Claude. Les fichiers qui ne se terminent pas par <code>.md</code> ou <code>.markdown</code> sont ignorés.</li>
  <li>Chaque fichier s’ouvre une fois par session Claude Code, quel que soit le nombre de modifications. La liste se trouve dans <code>$TMPDIR/marsdawn-hook/</code>, un fichier par session : une nouvelle session rouvre donc le fichier.</li>
  <li><code>--background</code> empêche MarsDawn de passer au premier plan : la fenêtre dans laquelle vous travailliez garde le focus.</li>
  <li>Il ne gêne jamais Claude. Chaque chemin se termine avec 0, et si marsdawn ou l’app MarsDawn n’est pas installé, rien ne se passe.</li>
  <li>Il lit l’entrée du hook avec <code>/usr/bin/jq</code>, fourni avec macOS 26, la version dont l’app MarsDawn a besoin.</li>
  <li>Pour le désactiver, supprimez l’entrée du fichier de réglages.</li>
</ul>

<h2>Échecs</h2>
<p>Avec <code>--json</code>, un échec affiche un objet JSON sur stdout et se termine avec son code :</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code> : l’entrée n’existe pas, est un dossier ou n’est pas du texte UTF-8 ; ou un chemin <code>--folder</code> n’existe pas ou n’est pas un dossier.</li>
  <li><code>3</code>, <code>app_not_installed</code> : MarsDawn n’est pas installé. Seul <code>open</code> renvoie ce code.</li>
  <li><code>4</code>, <code>output_exists</code> : le fichier de sortie existe. Passez <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code> : l’export lui-même a échoué.</li>
  <li><code>6</code>, <code>app_cannot_open_folders</code> : cette version de MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert. Seul <code>open</code> renvoie ce code.</li>
  <li><code>64</code> : erreur d’utilisation, comme une option inconnue, une valeur non valide, une ligne hors limites, <code>--line</code> avec plus d’un fichier ou avec un dossier, plus d’un dossier, ou <code>-a</code>. Celle-ci s’affiche en texte sur stderr, même avec <code>--json</code>.</li>
</ul>

<h2>Schémas JSON</h2>
<p>JSON Schema (draft 2020-12) pour chaque résultat <code>--json</code> :</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>Variables d’environnement</h2>
<ul>
  <li><code>MARSDAWN_THEME</code> : le thème qu’utilise <code>export</code> quand <code>--theme</code> n’est pas passé. Une valeur inconnue revient à <code>dawn</code> sans erreur.</li>
</ul>

<h2>Configuration requise</h2>
<ul>
  <li>L’outil fonctionne sous macOS 15 ou version ultérieure. Sur puce Apple, Homebrew installe un bottle précompilé et rien d’autre n’est nécessaire. Le compiler vous-même, sur un Mac Intel ou à partir des sources, nécessite Swift 6.2 ou version ultérieure, fourni avec Xcode 26 ou version ultérieure.</li>
  <li>L’app MarsDawn nécessite macOS 26 ou version ultérieure.</li>
</ul>

<h2>Installation</h2>
<p>Avec Homebrew. Sur puce Apple, il installe un bottle précompilé en quelques secondes, sans Xcode. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure.</p>
<pre><code>brew tap redtear1115/tap && brew install marsdawn
marsdawn --version</code></pre>
<p>Ou compilez-le à partir <a href="{k.KIT_URL}">des sources</a>. La première compilation récupère les dépendances et compile, ce qui prend aussi quelques minutes.</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> affiche le numéro de version, par exemple <code>0.3.0</code>, et se termine avec le code 0.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Une compétence en un seul fichier pour les agents qui lisent des instructions plutôt qu’un shell : <a href="/fr/cli/skill/">la compétence marsdawn</a>.</li>
  <li>Un serveur MCP qui enveloppe ce même <code>export</code> : <a href="/fr/cli/mcp/">marsdawn-mcp</a>.</li>
  <li>Pourquoi ce résultat JSON reste économique pour le contexte de l’agent : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
</ul>
""",
    }

    pages['cli/skill'] = {
        "title": 'Une compétence d’agent de code pour convertir Markdown en PDF · MarsDawn',
        "description": 'Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.',
        "body": f"""
<section class="intro">
  <h1>Laissez votre agent vous montrer ce qu’il a écrit, et produire le PDF.</h1>
  <p>Cette compétence tient en un fichier Markdown. Elle apprend à un agent de code à ouvrir dans MarsDawn un document qu’il a écrit pour que vous le relisiez, et à installer <code>marsdawn</code>, vérifier qu’il fonctionne, exporter un document en PDF et lire le résultat.</p>
</section>
<div class="summary"><p><strong>Un seul fichier Markdown, dans <code>~/.claude/skills/marsdawn/SKILL.md</code>.</strong> Avec lui, votre agent installe <code>marsdawn</code>, exporte en PDF et lit le résultat JSON, et il demande toujours avant d’exécuter quoi que ce soit.</p></div>
<h2>L’installer dans Claude Code</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code la charge quand une tâche demande un PDF, ou quand il a écrit ou révisé un document Markdown que vous allez lire, et vous pouvez la lancer vous-même avec <code>/marsdawn</code>. C’est <a href="/cli/skill/SKILL.md">un fichier court</a> : lisez-le avant de l’installer.</p>
<p>D’autres agents peuvent utiliser le même fichier. C’est du Markdown brut, des instructions et des commandes : indiquez l’URL à votre agent ou collez le contenu.</p>
<h2>Ce qu’elle enseigne</h2>
<ul>
  <li>Installer <code>marsdawn</code> avec Homebrew s’il manque, puis le vérifier avec <code>marsdawn --version</code> au lieu de supposer une version.</li>
  <li>Exporter avec <code>marsdawn export … --json</code> et lire le résultat : où est allé le PDF, combien de pages il compte, et quel diagramme Mermaid n’a pas pu être rendu.</li>
  <li>Distinguer les échecs par leur code de sortie : fichier introuvable, PDF déjà présent, export échoué, option incorrecte.</li>
  <li>Ouvrir un document qu’il a écrit avec <code>marsdawn open file.md:line</code>, sur sa première modification, et une seule fois : les modifications suivantes apparaissent d’elles-mêmes dans la fenêtre ouverte.</li>
  <li>Si l’app MarsDawn n’est pas installée, le dire une fois et continuer, sans réessayer. Ne jamais utiliser <code>open</code> pour produire un PDF.</li>
  <li>Avec <code>--folder</code> (marsdawn 0.5.1 et versions ultérieures), signaler le dossier comme demandé, pas comme affiché : c’est l’app qui décide, et rien ne le confirme.</li>
</ul>
<h2>Ce qu’elle ne fait pas</h2>
<ul>
  <li>Elle ne s’accorde pas elle-même la permission d’exécuter quoi que ce soit. Votre agent demande toujours avant d’installer <code>marsdawn</code> ou de le lancer, comme pour n’importe quelle autre commande.</li>
  <li>Elle n’envoie vos documents nulle part. <code>marsdawn</code> fait le rendu sur votre Mac et laisse de côté les images du web, sauf si vous passez <code>--allow-remote-images</code>.</li>
</ul>
<p>Le contrat complet, chaque champ et chaque code, se trouve dans <a href="/fr/cli/agents/">marsdawn pour les agents</a>. Pour un agent qui appelle des outils via MCP plutôt que de lire un fichier de compétence, il existe aussi <a href="/fr/cli/mcp/">un serveur MCP</a>.</p>
""",
    }

    pages['cli/mcp'] = {
        "title": 'Trois façons d’appeler marsdawn : CLI, fichier de compétence, serveur MCP · MarsDawn',
        "description": 'marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.',
        "body": f"""
<section class="intro">
  <h1>Trois façons d’appeler marsdawn.</h1>
  <p>MarsDawn n’a pas de modèle d’IA à lui : il est conçu pour relire du Markdown, pas pour en écrire, donc peu importe quel agent ou quel modèle a produit le fichier. Un agent ou un script peut appeler <code>marsdawn</code> de trois façons, et toutes les trois finissent par lancer le même <code>export</code>.</p>
</section>

<div class="summary"><p><strong>Choisissez ce que vos outils prennent en charge : la CLI gratuite <code>marsdawn</code>, un fichier de compétence en Markdown brut, ou le serveur MCP <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>.</strong> Tous trois appellent le même <code>marsdawn export</code> et renvoient le même résultat JSON.</p></div>

<h2>Laquelle utiliser</h2>
<!--compare:mcp-choice-->

<h2>La CLI</h2>
<p><code>marsdawn export notes.md --json</code> peut être appelé par tout agent ou script capable de lancer une commande shell : il est indépendant du modèle par construction. Chaque champ qu’il renvoie est documenté dans <a href="/fr/cli/agents/">marsdawn pour les agents</a>, la référence pour le schéma JSON vers laquelle renvoient les deux autres options ci-dessous.</p>

<h2>Le fichier de compétence</h2>
<p>Pour un agent qui lit des instructions en Markdown brut au lieu d’appeler directement un shell (aujourd’hui, Claude Code), <a href="/fr/cli/skill/">la compétence marsdawn</a> est un fichier qui lui apprend à installer marsdawn, lancer <code>export</code> et lire le résultat. C’est du Markdown brut : d’autres agents qui chargent des fichiers d’instructions peuvent utiliser le même.</p>

<h2>Le serveur MCP</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> est un dépôt séparé, public, sous licence Apache-2.0. C’est un serveur MCP doté de deux outils, <code>export_markdown_to_pdf</code> et <code>open_in_marsdawn</code>, qui enveloppent <code>marsdawn export --json</code> et <code>marsdawn open --json</code> : pointez un client MCP vers lui, et un appel d’outil renvoie le même JSON que la CLI.</p>
<ul>
  <li><strong>Où l’obtenir :</strong> sous forme de MCP Bundle, <code>marsdawn.mcpb</code>, joint à <a href="https://github.com/redtear1115/marsdawn-mcp/releases">sa release GitHub</a>, ou en lançant le serveur depuis les sources via stdio.</li>
  <li><strong>Registre :</strong> référencé dans le <a href="https://registry.modelcontextprotocol.io/v0/servers/dev.southern-light.mcp%2Fmarsdawn/versions/latest">MCP Registry</a> sous le nom <code>dev.southern-light.mcp/marsdawn</code> (version actuelle : 0.2.4).</li>
  <li><strong>Hébergement :</strong> auto-hébergé uniquement. Il n’existe pas de service marsdawn-mcp hébergé ; le serveur tourne sur votre propre machine, à côté de marsdawn.</li>
  <li><strong>Configuration requise :</strong> macOS, marsdawn 0.5.0 ou version ultérieure, et Node.js 20 ou version ultérieure pour lancer le serveur.</li>
</ul>

<h2>Limité aux dossiers que vous autorisez</h2>
<p>Les deux outils n’accèdent qu’aux dossiers que vous autorisez : le réglage <strong>Allowed folders</strong> de l’extension, vide au départ et sans valeur prédéfinie, ou à défaut les racines que propose votre client MCP. Si aucun des deux n’est défini, chaque appel est refusé, et le message de refus explique comment y remédier. Chaque chemin doit être absolu, et <code>export_markdown_to_pdf</code> n’écrit jamais qu’un fichier <code>.pdf</code>, jamais à travers un lien symbolique.</p>
<p><strong>Sécurité :</strong> passez à la version <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>. Avec 0.1.0 et 0.2.0, un appel pouvait écrire un PDF à n’importe quel emplacement accessible en écriture à votre compte ; corrigé sous la référence <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a>.</p>

<h2>Le même export, trois portes</h2>
<p>Quelle que soit la porte d’entrée, le comportement de fond ne change pas : le même moteur d’export, les mêmes thèmes et formats de papier, les mêmes <code>diagramErrors</code> quand un diagramme Mermaid ne peut pas être rendu. Cette page ne répète pas ce contrat ; <a href="/fr/cli/agents/">marsdawn pour les agents</a> le décrit en entier.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Le schéma JSON complet et chaque code de sortie : <a href="/fr/cli/agents/">marsdawn pour les agents</a>.</li>
  <li>La compétence en un seul fichier pour Claude Code et les agents similaires : <a href="/fr/cli/skill/">la compétence marsdawn</a>.</li>
  <li>Pourquoi un résultat JSON compact compte pour le contexte de votre agent : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
</ul>
""",
    }

    pages['vs/markdown-preview-tools'] = {
        "title": 'Afficher du Markdown ailleurs ou dans MarsDawn · MarsDawn',
        "description": 'MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.',
        "body": f"""
<section class="intro">
  <h1>Afficher du Markdown ailleurs, ou dans MarsDawn.</h1>
  <p>Si VS Code, un navigateur ou Claude Desktop est déjà ouvert, il est logique de s’en servir pour jeter un œil à un fichier Markdown. Voici ce que chacun affiche réellement, et ce qu’il en coûte pour y arriver, comparé à l’ouverture du même fichier dans MarsDawn.</p>
</section>

<h2>En un coup d’œil</h2>
<!--compare:preview-tools-->

<h2>L’aperçu intégré de VS Code</h2>
<p>Appuyez sur <kbd>&#8984;&#8679;V</kbd> dans VS Code et il fait le rendu du fichier Markdown dans un volet d’aperçu intégré, gratuitement, sans rien installer. Depuis VS Code 1.121 (mai 2026), cet aperçu affiche aussi les diagrammes Mermaid nativement : Microsoft a intégré une extension Mermaid à VS Code lui-même, alors qu’il fallait auparavant une extension séparée. Ce qu’il ne fait pas : c’est un volet d’aperçu à l’intérieur d’un éditeur, pas un éditeur conçu pour la lecture. Le volet se trouve à côté d’une arborescence de fichiers, d’un terminal et de tous les autres panneaux que VS Code peut afficher, et VS Code lui-même est une app Electron qu’on installe comme un environnement de développement complet, pas quelque chose qu’on ouvre pour lire un fichier.</p>

<h2>Une extension de navigateur pour les fichiers locaux</h2>
<p>Aucune extension de navigateur ne s’impose pour lire un fichier <code>.md</code> local : Local Markdown Viewer, Markdown Viewer, MarkView et d’autres font à peu près la même chose, et aucune n’est installée par défaut. Toutes ont besoin de la même étape supplémentaire avant de pouvoir ouvrir quoi que ce soit : activer « Autoriser l’accès aux URL de fichier » pour l’extension, car les navigateurs empêchent par défaut les extensions de lire les pages <code>file://</code>. C’est une autorisation que l’on accorde une fois par extension, et on oublie facilement qu’on l’a fait, ou pourquoi. Une fois activée, le fichier s’affiche dans un onglet du navigateur : il faut donc faire tourner un navigateur complet pour regarder un fichier.</p>

<h2>L’aperçu de fichiers de Claude Desktop</h2>
<p>Claude Desktop affiche un fichier qui se trouve déjà dans un projet ou une conversation. Ce pour quoi il n’est pas conçu, c’est parcourir des fichiers quelconques sur le disque : vous pouvez regarder ce que la conversation contient déjà, pas un dossier de notes que vous gardez ouvert à côté de votre travail. La liste d’Anthropic <a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">des types de documents que l’on peut importer</a> comprend PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON et XLSX : Markdown n’y figure pas.</p>

<h2>Un moteur de navigateur pour lire un fichier</h2>
<p>VS Code est une app Electron : un Chromium et un environnement Node.js embarqués, pas une app Mac native. L’extension de navigateur, elle, tourne dans un vrai navigateur. Dans les deux cas, afficher un fichier Markdown suppose de faire tourner un moteur de navigateur complet. MarsDawn est une app AppKit native : pas de navigateur embarqué ; elle ouvre directement n’importe quel fichier local, sans extension à installer ni autorisation à retenir.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Ce que MarsDawn ne fait pas non plus : <a href="/fr/limits/">la liste</a>.</li>
  <li>Transformer n’importe quel fichier Markdown en PDF dès aujourd’hui, gratuitement : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Par rapport à une visionneuse Mac native : <a href="/fr/vs/macmd-viewer/">MacMD Viewer ou MarsDawn</a>.</li>
</ul>
""",
    }

    pages['themes'] = {
        "title": 'Thèmes d’aperçu et export PDF dans MarsDawn · MarsDawn',
        "description": 'Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.',
        "body": f"""
<section class="intro">
  <h1>Huit apparences, un seul export.</h1>
  <p>MarsDawn propose quatre thèmes d’aperçu, Aube, Classique, Moderne et Vif, chacun avec une palette claire et une palette sombre : huit combinaisons pour lire un document. Exportez en PDF ou imprimez, et la page sort dans celle que vous lisiez.</p>
</section>

<div class="summary"><p><strong>Quatre thèmes &#215; clair et sombre = huit façons de lire un document, et un seul chemin d’export qui suit votre choix.</strong> <a href="/fr/themes/new/">Créez le vôtre</a> dans le navigateur, ou <a href="/fr/themes/gallery/">parcourez la galerie</a> pour voir ce que d’autres ont proposé.</p></div>

<h2>Les quatre thèmes</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Aube</strong>, le thème par défaut : le même papier chaleureux et le même accent Mars Rust que ce site.</li>
  <li><strong>Classique</strong> : une palette plus sobre, proche d’un document.</li>
  <li><strong>Moderne</strong> : une palette plus froide et plus contemporaine.</li>
  <li><strong>Vif</strong> : une palette plus lumineuse et plus contrastée.</li>
</ul>
<p>Chacun a sa propre variante claire et sombre : changer l’apparence de votre Mac change aussi la palette du thème, pas seulement l’interface autour.</p>

<h2>L’export PDF et l’impression utilisent le même thème</h2>
<p>Exportez en PDF ou imprimez, et la page utilise la palette claire de votre thème : les diagrammes Mermaid y sont dessinés, les blocs de code gardent leur coloration syntaxique, et les sauts de page évitent de séparer un titre de sa section ou de couper un tableau ou un diagramme en deux. L’<a href="/fr/cli/">outil en ligne de commande marsdawn</a>, gratuit, utilise le même moteur d’export : un script ou un agent produit donc le même PDF, dans n’importe lequel des quatre thèmes, avec <code>--theme</code>.</p>

<h2>Créez le vôtre, et parcourez ce que d’autres ont fait</h2>
<p><a href="/fr/themes/new/">Créez un thème dans votre navigateur</a> : choisissez des couleurs et quelques options de style, voyez-les appliquées en direct, et envoyez-le en issue GitHub pour relecture &#8212; pas d’installation, pas de git. <a href="/fr/themes/gallery/">La galerie</a> montre chaque thème soumis qu’un mainteneur a relu et fusionné, filtrable selon son usage. Installez-en un dans l’app depuis Réglages › Apparence › Obtenir plus de thèmes…, et Coup d’œil l’utilise aussi dans le Finder.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Le pas-à-pas complet de l’export PDF, en ligne de commande : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Ce que MarsDawn ne fait pas encore : <a href="/fr/limits/">la liste</a>.</li>
  <li>Remettre un PDF exporté à quelqu’un qui n’utilise pas Markdown : <a href="/fr/sharing-exported-pdfs/">partager un PDF</a>.</li>
</ul>
""",
    }


    pages['themes/new'] = {
        "title": "Créer un thème MarsDawn dans votre navigateur · MarsDawn",
        "description": "Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.",
        "body": """
<section class="intro">
  <h1>Créer un thème</h1>
  <p>Choisissez ci-dessous une palette et quelques options de style. Le document d’exemple à droite se met à jour au fur et à mesure, en clair et en sombre, et chaque contrôle que la CI de la galerie exécute apparaît aussi ici &#8212; un thème qui atteint l’issue de soumission a donc en général déjà tout passé.</p>
  <p>Il vous faut un compte GitHub pour envoyer. Cette page elle-même n’exige ni installation ni git.</p>
</section>
<div id="theme-sim-app" data-locale="fr"><p>Cette page a besoin de JavaScript pour créer et prévisualiser un thème.</p></div>
""",
    }
    pages['themes/gallery'] = {
        "title": "Galerie de thèmes : thèmes communautaires pour MarsDawn · MarsDawn",
        "description": "Parcourez les thèmes d’aperçu proposés par la communauté pour MarsDawn, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur, sans installation ni git.",
        "body": f"""
<section class="intro">
  <h1>Galerie de thèmes</h1>
  <p>Thèmes d’aperçu proposés par la communauté ; chacun a été relu et fusionné par le développeur avant d’apparaître ici. Filtrez par scénario, ou <a href="/fr/themes/new/">créez le vôtre</a> dans le navigateur &#8212; pas d’installation, pas de git.</p>
</section>
<!--community-theme-gallery-->
<h2>Crédits et licence</h2>
<p>Dracula, Nord, Gruvbox et Solarized s’appuient sur des palettes open source ; voir les <a href="/themes/third-party-notices.html">mentions des tiers</a> pour le copyright et le texte complet de la licence de chaque projet.</p>
<h2>Un thème pose problème ?</h2>
<p>Utilisez le bouton « Signaler » sur sa carte (JavaScript requis), ou écrivez directement à <a href="mailto:{k.EMAIL}">{k.EMAIL}</a> avec son nom et sa version, JavaScript ou non. Les signalements sont examinés à la main ; un thème confirmé problématique est retiré sous un jour.</p>
""",
    }

    compare_tables['mcp-choice'] = {
        'head': ['Si votre agent', 'Utilisez', 'Prérequis'],
        'rows': [
            ['Peut lancer une commande shell', '<a href="{root}cli/agents/">La CLI</a>', 'macOS 15 ou version ultérieure'],
            ['Charge des fichiers d’instructions, comme Claude Code', '<a href="{root}cli/skill/">Le fichier de compétence</a>', 'La CLI, que la compétence installe'],
            ['Appelle des outils via MCP', '<a href="{mcp}">marsdawn-mcp</a>', 'marsdawn-mcp 0.2.1 ou version ultérieure, marsdawn 0.5.0 ou version ultérieure, et Node.js 20 ou version ultérieure'],
        ],
    }
    compare_tables['preview-tools'] = {
        'head': ['', 'Aperçu VS Code', 'Extension de navigateur', 'Claude Desktop', 'MarsDawn'],
        'rows': [
            ['Ouvre un fichier Markdown depuis le disque', 'Oui', 'Oui, une fois l’accès aux fichiers autorisé', 'Non : Markdown ne figure pas dans sa liste d’import', 'Oui'],
            ['Avant le premier fichier', 'Installer VS Code, un environnement de développement complet', 'Installer une extension, puis activer « Autoriser l’accès aux URL de fichier »', 'Il ne peut pas parcourir les fichiers du disque', 'Installer MarsDawn'],
            ['Conçu pour', 'Écrire du code ; l’aperçu est un volet parmi d’autres', 'Naviguer sur le web', 'Converser avec Claude', 'Lire et modifier du Markdown'],
            ['Dessine la page avec', 'Electron : un Chromium et Node.js embarqués', 'Un navigateur complet', 'L’app Claude Desktop', 'Une app AppKit native ; WebKit dessine la page'],
        ],
    }
    theme_shots = {
        '01-split': ('Aube (par défaut)', 'Le thème Aube en vue partagée : la source Markdown à gauche, la page rendue à droite.'),
        '02-classic': ('Classique', 'Le thème Classique, l’aperçu occupant toute la fenêtre.'),
        '04-vivid': ('Vif', 'Le thème Vif en vue partagée.'),
        '03-dark': ('Mode sombre', 'MarsDawn en mode sombre, en vue partagée.'),
    }
    theme_gallery_note = 'Moderne n’est pas encore illustré ; la quatrième image montre le mode sombre à la place.'

    pages['token-efficient-review'] = {
        "title": 'Relire ce que produit MarsDawn sans dépenser les tokens de votre agent · MarsDawn',
        "description": 'Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.',
        "body": f"""
<section class="intro">
  <h1>Relire sans dépenser les tokens de votre agent.</h1>
  <p>Deux choses distinctes restent économiques dans cette boucle : ce que l’agent reçoit en appelant l’outil, et ce qu’il faut pour confirmer que le résultat est correct.</p>
</section>

<div class="summary"><p><strong>L’appel d’outil renvoie un petit objet JSON, pas la page rendue, et c’est une personne qui relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent.</strong></p></div>

<h2>L’appel d’outil lui-même coûte peu</h2>
<p>Appelez <code>marsdawn export</code>, depuis la CLI, la compétence ou <a href="/fr/cli/mcp/">le serveur MCP</a>, et vous recevez <a href="/fr/cli/agents/">un objet JSON compact</a> : <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> et <code>diagramErrors</code>. Le schéma complet est <a href="/schemas/cli/export.v1.json">export.v1.json</a>. Rien de tout cela n’est le document rendu. Un PDF de 50 pages avec une douzaine de diagrammes Mermaid renvoie la même poignée de champs qu’une note d’une page.</p>

<h2>La relecture se fait à côté</h2>
<p>Une fois le PDF créé, une personne l’ouvre, dans MarsDawn ou n’importe quel lecteur PDF, et lit les diagrammes, les formules et la mise en page rendus. L’agent n’a jamais besoin de relire ce rendu dans sa propre fenêtre de contexte pour confirmer qu’il est correct : la relecture se fait dans une autre fenêtre, sur un autre écran, et non dans un nouvel aller-retour de tokens passés à décrire à quoi ressemble un diagramme.</p>

<h2>Ce que cela évite</h2>
<ul>
  <li>Recoller dans la conversation du Markdown rendu, une capture d’écran ou sa description, uniquement pour que l’agent confirme que l’export a fonctionné.</li>
  <li>Un agent qui doit reconstituer le rendu d’un diagramme Mermaid ou d’une formule KaTeX, au lieu d’une personne qui le regarde, tout simplement.</li>
  <li>Un second appel d’outil pour récupérer le contenu du PDF alors que le premier a déjà signalé un succès.</li>
</ul>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Les trois façons d’appeler marsdawn, CLI, fichier de compétence, serveur MCP : <a href="/fr/cli/mcp/">trois portes d’entrée</a>.</li>
  <li>Chaque champ du résultat JSON : <a href="/fr/cli/agents/">marsdawn pour les agents</a>.</li>
  <li>Pourquoi une personne doit encore lire ce qu’un agent a écrit : <a href="/fr/reviewing-ai-output/">pourquoi relire</a>.</li>
  <li>L’argumentaire complet pour lire ce que rend un agent, avec une liste de vérification : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
</ul>
""",
    }

    pages['sharing-exported-pdfs'] = {
        "title": 'Partager ce qu’un agent a écrit, sans enseigner le Markdown · MarsDawn',
        "description": 'Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.',
        "body": f"""
<section class="intro">
  <h1>Donnez-leur le PDF, pas le Markdown.</h1>
  <p>Un agent termine un document, vous le relisez et le révisez, puis quelqu’un en dehors de l’équipe technique doit le lire aussi : un responsable, un client, quelqu’un d’une autre équipe. Ces personnes n’ont pas besoin de savoir ce que signifient <code>##</code> ou un tableau à barres verticales. Exportez en PDF et donnez-leur cela à la place.</p>
</section>

<div class="summary"><p><strong>Exportez le document relu en PDF et envoyez ce fichier.</strong> Il s’ouvre partout, ne demande ni connaissance du Markdown ni installation, et ressemble à ce que vous avez vu dans l’aperçu, diagrammes, tableaux et mise en forme compris.</p></div>

<h2>Pourquoi ne pas simplement envoyer le fichier .md</h2>
<p>Un fichier <code>.md</code> brut ouvert dans un éditeur de texte montre les marques, pas la page : <code>#</code> pour un titre, <code>**</code> autour du gras, un bloc délimité pour un diagramme Mermaid qui n’est pas dessiné. Quelqu’un qui n’écrit pas de Markdown ne lit rien de tout cela comme prévu, et lui demander d’installer d’abord une visionneuse, c’est beaucoup demander pour un seul document.</p>

<h2>Pourquoi pas une capture d’écran</h2>
<p>Une capture d’écran fige un écran d’un document qui peut faire plusieurs pages, ne permet ni recherche ni sélection, et devient moins lisible après quelques compressions et transferts. Un PDF conserve le texte, les diagrammes et les sauts de page, quelle que soit la longueur.</p>

<h2>Ce qu’apporte un PDF</h2>
<ul>
  <li>Il s’ouvre avec ce que le destinataire a déjà, Aperçu, un navigateur, Acrobat, son téléphone, sans outil Markdown.</li>
  <li>Les diagrammes Mermaid sont dessinés, pas laissés sous forme de code ; les blocs de code gardent leur coloration.</li>
  <li>Les sauts de page sont choisis pour qu’un titre ne se retrouve pas seul en bas d’une page, et qu’un tableau ou un diagramme ne soit pas coupé sur deux pages.</li>
  <li>Le même fichier, qu’il vienne de l’app MarsDawn ou de la ligne de commande gratuite ; le pas-à-pas se trouve sur <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
</ul>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Les thèmes et mises en page dont l’export peut provenir : <a href="/fr/themes/">thèmes d’aperçu et export PDF</a>.</li>
  <li>Exporter depuis un script ou un agent plutôt que depuis l’app : <a href="/fr/cli/agents/">marsdawn pour les agents</a>.</li>
  <li>Pourquoi une personne doit d’abord lire le document : <a href="/fr/reviewing-ai-output/">pourquoi relire</a>.</li>
  <li>Les passations entre plusieurs agents produisent naturellement des PDF à partager : <a href="/fr/agent-design-patterns/">Quatre modèles de conception d’agents et les documents que chacun vous remet</a>.</li>
</ul>
""",
    }

    pages['reviewing-ai-output'] = {
        "title": 'Pourquoi ce que produit l’IA a toujours besoin d’un lecteur humain · MarsDawn',
        "description": 'Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.',
        "body": f"""
<section class="intro">
  <h1>Un agent l’écrit. Vous devez quand même le comprendre.</h1>
  <p>Un agent IA peut rédiger vite un plan, une spécification ou des notes. Ce qu’il produit doit pourtant être compris par la personne qui va agir en conséquence, et non cru parce que le texte est fluide.</p>
</section>

<div class="summary"><p><strong>MarsDawn est conçu pour cette lecture : la page rendue à côté de la source, avec les diagrammes Mermaid et les formules KaTeX dessinés au lieu de rester des marques, pour que la structure d’un document se lise d’un coup d’œil.</strong></p></div>

<h2>Fluide ne veut pas dire juste</h2>
<p>À propos du code écrit avec l’aide de l’IA et destiné à être retravaillé plutôt que jeté, Simon Willison l’a formulé ainsi : « la qualité et la compréhensibilité du code sous-jacent sont essentielles » (<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>, 2025). C’est vrai aussi d’un document : le brouillon d’un agent qui se lit sans accroc peut se tromper de structure, de chiffres ou de logique, et une prose fluide n’indique pas quelles parties vérifier.</p>

<h2>De l’inférence, pas de la compilation</h2>
<p>Birgitta Böckeler, pour Thoughtworks, pose la distinction sans détour : « les LLM ne sont PAS des compilateurs, interpréteurs, transpileurs ou assembleurs du langage naturel, ce sont des moteurs d’inférence » (<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>). Un compilateur accepte votre entrée ou signale une erreur ; un agent peut rendre quelque chose qui s’exécute, ou se lit, sans être juste. Quelqu’un doit encore vérifier.</p>

<h2>Ce que MarsDawn apporte à ce lecteur</h2>
<ul>
  <li>La page rendue à côté de la source, mise à jour quand l’un ou l’autre côté change, pour avoir sous les yeux à la fois une affirmation et la façon dont elle est structurée.</li>
  <li>Les diagrammes Mermaid dessinés : un organigramme qu’un agent a décrit en texte devient une forme que vous pouvez réellement suivre.</li>
  <li>Les formules KaTeX rendues, pas laissées sous forme de suite de barres obliques inverses : une formule se lit comme une formule.</li>
  <li>Rien ne se lance tout seul. MarsDawn ne note pas, ne résume pas et ne signale rien dans le document à votre place ; il met la structure sous vos yeux pour que vous le fassiez.</li>
</ul>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Comment cette relecture reste économique pour le contexte de l’agent : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
  <li>Remettre le document relu à quelqu’un d’autre : <a href="/fr/sharing-exported-pdfs/">partager un PDF</a>.</li>
  <li>Pourquoi c’est difficile à lire, et comment s’y prendre : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
  <li>Pourquoi les agents exposent leurs plans : <a href="/fr/agent-transparency/">Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?</a></li>
  <li>Ce qu’est MarsDawn, en une page : <a href="/fr/">la page d’accueil</a>.</li>
</ul>
""",
    }

    pages['reading-agent-output'] = {
        "title": 'Lire ce que votre agent vous rend · MarsDawn',
        "description": 'Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.',
        "body": f"""
<section class="intro">
  <h1>Le travail de votre agent revient sous forme de fichier Markdown.</h1>
  <p>Vous demandez à un agent de code de planifier une migration, de rédiger une spécification ou de traquer un bug. Il travaille seul un moment, puis vous remet un fichier : <code>plan.md</code>, <code>SPEC.md</code>, un rapport d’avancement, un résumé de recherche. Pour autant que vous puissiez vérifier le travail, ce fichier est le travail.</p>
</section>

<div class="summary"><p><strong>Pour savoir si l’agent a vu juste, il faut lire ce qu’il vous rend. MarsDawn est une app Mac pour cette lecture.</strong></p></div>

<h2>Ce que disent ceux qui construisent des agents</h2>
<p>Citations telles qu’écrites ; notre lecture suit.</p>
<ul>
  <li>« Building Effective Agents » d’Anthropic (Erik S. et Barry Zhang, décembre 2024) donne trois principes fondamentaux pour construire des agents. L’un d’eux : « Privilégiez la transparence en montrant explicitement les étapes de planification de l’agent. » Ce texte s’adresse à ceux qui construisent des agents. De votre côté, cette transparence, c’est le plan que vous finissez par lire.</li>
  <li>Le même article : « Les agents peuvent alors faire une pause pour obtenir un retour humain à des points de contrôle ou face à un blocage. » Notez le verbe : <em>peuvent</em>.</li>
  <li>Chip Huyen, dans « Agents » (janvier 2025), explique pourquoi la planification doit rester séparée de l’exécution : « Sans supervision, un agent peut exécuter ces étapes pendant des heures, gaspillant temps et argent en appels d’API, avant que vous ne vous rendiez compte qu’il n’aboutit à rien. » Elle décrit aussi un échec où « l’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas ». Chargé de loger 50 personnes dans 30 chambres d’hôtel, il en place 40 et affirme avoir terminé.</li>
  <li>Andrew Ng, sur le modèle de conception de la planification, dans The Batch (avril 2024) : « D’un côté, la planification est une capacité très puissante ; de l’autre, elle produit des résultats moins prévisibles. » C’est une remarque sur la prévisibilité, pas un appel à la relecture humaine, et il s’attend à ce que la planification progresse vite.</li>
</ul>
<p><strong>Notre déduction, pas la leur :</strong> si un agent expose son plan et s’arrête à des points de contrôle, quelqu’un lit ce plan au point de contrôle, et c’est généralement vous. Si un agent peut se croire fini alors qu’il ne l’est pas, son rapport « terminé » a lui aussi besoin d’un lecteur. Aucun de ces auteurs ne mentionne MarsDawn ni ne le recommande, pas plus qu’aucun autre outil Markdown.</p>

<h2>Pourquoi c’est plus difficile à lire qu’il n’y paraît</h2>
<p>Le fichier est long, et la partie importante se trouve rarement en haut. Il contient des diagrammes Mermaid et des formules difficiles à suivre sous forme de source. L’agent est peut-être encore en train de le réécrire alors que vous en êtes à la moitié. C’est souvent un fichier parmi d’autres, parfois répartis sur plusieurs branches ou worktrees. Et quand vous trouvez un problème, « la partie sur le cache a l’air bizarre » laisse l’agent deviner ; « <code>docs/plan.md:42</code> supprime l’ancienne table avant la fin du backfill », non.</p>

<h2>Là où MarsDawn aide</h2>
<ul>
  <li><strong>Fichiers longs :</strong> l’onglet Plan de la barre latérale (&#8963;&#8984;S) liste les titres. Cliquez sur l’un d’eux et les deux volets y sautent.</li>
  <li><strong>Diagrammes et maths :</strong> Mermaid et KaTeX sont dessinés dans l’aperçu à côté de la source (&#8984;2), et les deux volets défilent ensemble.</li>
  <li><strong>Réécrit pendant que vous lisez :</strong> quand l’agent réécrit le fichier, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.</li>
  <li><strong>Plusieurs fichiers :</strong> ouvrez le dossier de l’agent avec Fichier &#9656; Ouvrir un dossier&#8230; (&#8679;&#8984;O). Les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, et pour un checkout git, l’en-tête indique la branche ou le worktree.</li>
  <li><strong>Un retour précis :</strong> Édition &#9656; Copier la référence (&#8997;&#8984;C) copie votre position sous la forme <code>docs/plan.md:42</code>. Copier pour l’IA (&#8963;&#8997;&#8984;C) ajoute le texte sélectionné en dessous. Collez l’un ou l’autre dans la conversation avec l’agent.</li>
</ul>
<p>Deux de plus pour la boucle : un agent peut lancer <code>marsdawn open plan.md:42</code> pour ouvrir le fichier dans MarsDawn à la ligne 42, celle qu’il veut vous montrer en premier, et un fichier relu s’exporte en PDF depuis l’app ou avec la commande gratuite <code>marsdawn export</code>.</p>
<p>MarsDawn n’embarque aucun modèle d’IA. Il ne résume pas le plan, ne le note pas et ne vous dit pas ce qui ne va pas. C’est vous qui lisez ; il garde lisible un fichier long qui change, et vous permet de désigner la ligne exacte.</p>

<h2>Relire le plan d’un agent en cinq minutes</h2>
<p>Cela marche dans n’importe quel éditeur.</p>
<ol>
  <li>Lisez seulement les titres. Le plan correspond-il à ce que vous avez demandé ? Une section manquante signifie généralement du travail manquant.</li>
  <li>Repérez chaque endroit qui affirme que quelque chose est fait, réussi ou vérifié, et vérifiez-en un vous-même : ouvrez le fichier, lancez le test, comptez les lignes.</li>
  <li>Cherchez les étapes irréversibles : suppression de données, migrations, force-push, tout ce qui envoie, paie ou publie. Celles-là attendent votre accord explicite.</li>
  <li>Lisez les diagrammes rendus, et confrontez chaque flèche au texte.</li>
  <li>Listez les fichiers et systèmes que le plan touche. Posez des questions sur tout ce que vous n’avez pas demandé avant que cela s’exécute.</li>
  <li>Rédigez vos retours sous la forme endroit, problème, correction : « <code>plan.md:88</code> : le backfill s’exécute après la suppression. Inversez les étapes 4 et 5. » Un problème par ligne.</li>
</ol>
<p>Peu de temps ? Faites l’étape 2. C’est là qu’on prend en défaut un agent qui se croit fini. La version longue, avec un exemple détaillé : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le <a href="{k.LISTING_URL}">Mac App Store</a>. Il existe aussi l’outil en ligne de commande gratuit <code>marsdawn</code> :</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Il exporte le Markdown en PDF sans l’app, et <code>marsdawn open</code> permet à votre agent d’ouvrir des fichiers dans MarsDawn pour vous.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; <a href="/fr/cli/agents/">marsdawn pour les agents</a> &#183; À savoir avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>L’argument court pour lire ce que produit l’IA : <a href="/fr/reviewing-ai-output/">Pourquoi ce que produit l’IA a toujours besoin d’un lecteur humain</a>.</li>
  <li>Garder le contexte de l’agent réduit pendant la relecture : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
  <li>Pourquoi les agents exposent leurs plans : <a href="/fr/agent-transparency/">Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?</a></li>
  <li>La liste ci-dessus, étape par étape avec un exemple : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</li>
  <li>Quels documents vous remettent les différents types d’agents : <a href="/fr/agent-design-patterns/">Quatre modèles de conception d’agents et les documents que chacun vous remet</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (cité d’après la version en ligne le 26/09/2026 ; l’article précise désormais qu’une grande partie des outils décrits a changé depuis décembre 2024).</li>
  <li>Chip Huyen, « Agents », 7 janvier 2025 : <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng, « Agentic Design Patterns Part 4, Planning », The Batch, 10 avril 2024 : <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": 'Les agents doivent être transparents. Qui lit ce qu’ils montrent ? · MarsDawn',
        "description": 'Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.',
        "body": f"""
<section class="intro">
  <h1>Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?</h1>
  <p>En décembre 2024, Anthropic a publié « Building Effective Agents », un guide destiné à ceux qui construisent des agents IA. Son résumé énonce trois principes, dont la transparence. Cet article s’intéresse à l’autre bout de ce principe : dès qu’un agent expose ses étapes, quelqu’un doit les lire.</p>
</section>

<div class="summary"><p><strong>La transparence, c’est l’agent qui la fournit. La lecture, c’est vous. Anthropic demande aux concepteurs de montrer les étapes de planification d’un agent ; pour la plupart des personnes qui pilotent un agent de code, ces étapes arrivent dans un fichier Markdown que quelqu’un doit lire au bon moment.</strong></p></div>

<h2>Ce que dit le guide</h2>
<p>Erik S. et Barry Zhang résument leurs conseils ainsi :</p>
<blockquote><p>« Quand nous implémentons des agents, nous essayons de suivre trois principes fondamentaux : garder une conception simple. Privilégier la transparence en montrant explicitement les étapes de planification de l’agent. Soigner l’interface agent-ordinateur (ACI) par une documentation et des tests approfondis des outils. »</p></blockquote>
<p>Ce sont des principes de conception pour ceux qui construisent des agents, pas des consignes pour la personne qui en utilise un. Le principe demande que les étapes soient montrées. Il ne dit pas qui les lit.</p>
<p>Le même article décrit ce que fait un agent une fois qu’il a une tâche : « Une fois la tâche claire, les agents planifient et agissent de façon autonome, en revenant éventuellement vers l’humain pour obtenir des informations ou un avis. » Et : « Les agents peuvent alors faire une pause pour obtenir un retour humain à des points de contrôle ou face à un blocage. » Regardez les mots <em>éventuellement</em> et <em>peuvent</em>. Les points de contrôle sont décrits comme quelque chose qu’un agent peut avoir, pas quelque chose qu’il doit avoir.</p>

<h2>L’essentiel de la vérification ne se fait pas par vous</h2>
<p>Il est facile d’en exagérer la portée, alors voici ce que le guide place réellement en premier. L’agent se vérifie lui-même face au monde : « Pendant l’exécution, il est crucial que les agents obtiennent à chaque étape une “vérité terrain” de l’environnement (comme les résultats d’appels d’outils ou d’exécution de code) pour évaluer leur progression. » Dans cette phrase, la vérité terrain désigne des résultats de tests et des sorties d’outils. Pas une personne.</p>
<p>Le guide est aussi direct sur le risque : « La nature autonome des agents implique des coûts plus élevés et un risque d’erreurs qui s’accumulent. » Sa réponse : des tests approfondis dans des environnements isolés, avec des garde-fous. Il ne dit pas « lisez plus attentivement ».</p>
<p>Une personne intervient plus loin, dans l’annexe sur les agents de code : « Cependant, si les tests automatisés aident à vérifier le fonctionnement, la relecture humaine reste cruciale pour garantir que les solutions répondent aux exigences plus larges du système. » Cette phrase porte sur du code. Mais le manque qu’elle désigne est familier avec n’importe quel agent : un test peut vous dire que quelque chose fonctionne, pas que c’est ce que vous vouliez.</p>

<h2>Où finissent les étapes</h2>
<p><strong>À partir d’ici, c’est notre lecture, pas celle d’Anthropic.</strong></p>
<p>Si vous utilisez un agent de code au quotidien, ses étapes de planification n’apparaissent généralement pas dans un tableau de bord. Elles apparaissent sous forme de fichiers : <code>plan.md</code>, une liste de tâches à cocher, un fichier d’avancement que l’agent réécrit sans cesse, un résumé à la fin. La transparence, de votre côté, signifie davantage à lire.</p>
<p>Montrer les étapes, c’est la part de l’agent. L’autre part, c’est une personne qui les lit au moment où cela compte : avant que la migration ne s’exécute, avant que la branche ne soit fusionnée, avant que « terminé » ne soit accepté. Un agent qui expose tout dans un fichier de 600 lignes que personne n’ouvre est transparent sur le papier et sans surveillance dans les faits.</p>
<p>Harrison Chase a fait une remarque voisine en 2024, à propos du fonctionnement des frameworks d’agents plutôt que des documents : « Vous voudrez pouvoir observer ce qui se passe à l’intérieur, puisque les étapes exactes ne sont peut-être pas connues à l’avance. » Il parlait d’outillage pour ceux qui construisent des agents. Si c’est vous qui pilotez l’agent, le simple fichier qu’il ne cesse d’écrire est souvent la partie que vous pouvez observer.</p>
<p>Aucun de ces auteurs ne mentionne MarsDawn, et aucun ne le recommande, pas plus qu’aucun autre outil Markdown.</p>

<h2>Pourquoi cette lecture est plus difficile qu’il n’y paraît</h2>
<p>Le fichier est long, et ce qui compte se trouve rarement en haut. Le diagramme qui explique la modification est du source Mermaid, pas une image (pour le voir dessiné, consultez <a href="/fr/view-markdown-on-mac/">Comment afficher un fichier Markdown sur Mac</a>). L’agent réécrit peut-être le fichier alors que vous en êtes à la moitié. Il y a souvent plus d’un fichier, parfois sur différentes branches ou worktrees. Et quand vous repérez un problème, « la partie sur le cache a l’air bizarre » laisse l’agent deviner. La version longue se trouve sur <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</p>

<h2>Ce que MarsDawn apporte, et ce qu’il n’apporte pas</h2>
<p>MarsDawn est une app Mac pour cette lecture. Il ne rend pas un agent plus transparent, et il n’embarque aucun modèle d’IA : il ne résumera pas le plan et ne vous dira pas s’il est juste. Ce qu’il fait :</p>
<ul>
  <li><strong>Fichiers longs :</strong> Présentation &#9656; Afficher la barre latérale (&#8963;&#8984;S) ouvre l’onglet Plan, qui liste les titres. Cliquez sur l’un d’eux pour y sauter.</li>
  <li><strong>Diagrammes et maths :</strong> la source et la page rendue sont côte à côte (&#8984;2) et défilent ensemble, avec Mermaid et KaTeX dessinés. Si un diagramme est cassé, l’aperçu affiche sa source avec l’erreur en dessous.</li>
  <li><strong>Réécrit pendant que vous lisez :</strong> quand l’agent réécrit le fichier, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.</li>
  <li><strong>Plusieurs fichiers :</strong> ouvrez le dossier de l’agent avec Fichier &#9656; Ouvrir un dossier&#8230; (&#8679;&#8984;O). Les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, et pour un checkout git, l’en-tête indique la branche ou le worktree.</li>
  <li><strong>Désigner une ligne :</strong> Édition &#9656; Copier la référence (&#8997;&#8984;C) copie votre position sous la forme <code>docs/plan.md:42</code>, et Copier pour l’IA (&#8963;&#8997;&#8984;C) ajoute le texte sélectionné en dessous, prêt à coller dans la conversation avec l’agent.</li>
</ul>
<p>C’est toujours vous qui lisez. MarsDawn garde lisible un fichier long qui change pendant que vous le faites.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le <a href="{k.LISTING_URL}">Mac App Store</a>. Il existe aussi l’outil en ligne de commande gratuit <code>marsdawn</code> :</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; À savoir avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Pourquoi ce que rend un agent est difficile à lire, avec une liste de vérification : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
  <li>La liste, étape par étape avec un exemple : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</li>
  <li>Quels documents vous remettent les différents types d’agents : <a href="/fr/agent-design-patterns/">Quatre modèles de conception d’agents et les documents que chacun vous remet</a>.</li>
  <li>L’argument court pour lire ce que produit l’IA : <a href="/fr/reviewing-ai-output/">Pourquoi ce que produit l’IA a toujours besoin d’un lecteur humain</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (cité d’après la version en ligne le 26/09/2026 ; l’article précise désormais qu’une grande partie des outils décrits a changé depuis décembre 2024).</li>
  <li>Harrison Chase, « What is an agent? », LangChain, 28 juin 2024, copie archivée : <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (l’adresse d’origine affiche désormais un autre article, de 2026).</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": 'Relire le plan d’un agent en cinq minutes · MarsDawn',
        "description": 'Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.',
        "body": f"""
<section class="intro">
  <h1>Relire le plan d’un agent en cinq minutes</h1>
  <p>Votre agent a rédigé un plan et attend votre feu vert. Vous avez cinq minutes, pas une heure. Voici une façon de les utiliser qui fonctionne dans n’importe quel éditeur, même un simple éditeur de texte. MarsDawn aide pour certaines étapes, et nous dirons lesquelles. Il n’aide pas pour la plus importante.</p>
</section>

<div class="summary"><p><strong>Ne lisez pas le plan de haut en bas. Vérifiez sa structure, vérifiez une affirmation, repérez ce qui est irréversible, regardez les diagrammes et le périmètre, puis rédigez un retour exploitable par l’agent. Six étapes, cinq minutes environ.</strong></p></div>

<h2>Pourquoi s’en soucier avant l’exécution</h2>
<p>Chip Huyen, expliquant pourquoi la planification doit rester séparée de l’exécution, chiffre le coût sans détour : « Sans supervision, un agent peut exécuter ces étapes pendant des heures, gaspillant temps et argent en appels d’API, avant que vous ne vous rendiez compte qu’il n’aboutit à rien. » Notre ajout : un plan est l’endroit le moins coûteux pour repérer une erreur. Corriger une ligne de <code>plan.md</code> coûte une phrase. Corriger ce que l’agent a fait après coup coûte un après-midi.</p>

<h2>L’exemple</h2>
<p>Vous avez demandé à un agent de déplacer les avatars des utilisateurs vers un stockage objet sans casser les liens existants. Il vous rend ceci :</p>
<pre><code># Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. &#9989; done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.</code></pre>
<p>Cela se lit bien. Cela supprimerait aussi tous les avatars avant d’en avoir copié un seul.</p>

<h2>Les six étapes</h2>
<p><strong>1. Lisez seulement les titres.</strong> <em>(une minute environ)</em> Le plan correspond-il à ce que vous avez demandé ? Une section manquante signifie généralement du travail manquant. Ici : Goal, Steps, Status. Vous avez demandé que les liens existants continuent de fonctionner, et aucun titre ne parle des anciens liens ni de la façon d’annuler le changement. C’est votre premier commentaire.</p>
<p>Dans un terminal, <code>grep -n '^#' plan.md</code> affiche uniquement les titres, et la plupart des éditeurs savent aussi afficher un plan. Dans MarsDawn, l’onglet Plan de la barre latérale (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) les liste, et un clic y mène.</p>
<p><strong>2. Repérez chaque endroit qui affirme que quelque chose est fait, réussi ou vérifié, et vérifiez-en un vous-même.</strong> <em>(une minute environ)</em> Ouvrez le fichier, lancez le test, comptez les lignes. Chip Huyen décrit un échec où « l’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas ». Dans son exemple, un agent chargé de loger 50 personnes dans 30 chambres d’hôtel en place 40 et affirme avoir terminé.</p>
<pre><code>grep -n -i -E 'done|pass|verified|&#9989;' plan.md</code></pre>
<p>Ici, cela trouve « &#9989; done » et « All tests pass. » Quels tests ? L’un d’eux touche-t-il aux avatars ? Lancez-les, ou demandez. MarsDawn ne peut pas faire cette étape à votre place. Personne d’autre que vous ne le peut.</p>
<p><strong>3. Cherchez les étapes irréversibles.</strong> <em>(une minute environ)</em> Suppression de données, migrations, force-push, tout ce qui envoie, paie ou publie. Celles-là attendent votre accord explicite. Chip Huyen décrit la même idée du côté du système : « Si un plan comporte des opérations risquées, comme mettre à jour une base de données ou fusionner une modification de code, le système peut demander une approbation humaine explicite avant de les exécuter, ou laisser des humains les exécuter. » Ici, l’étape 4 supprime les originaux, et elle vient avant l’étape 5, la copie.</p>
<p><strong>4. Lisez les diagrammes rendus, et confrontez chaque flèche au texte.</strong> Un organigramme qui dit « copier &#8594; vérifier &#8594; supprimer » alors que les étapes disent autre chose, c’est une trouvaille. Ce plan n’a pas de diagramme : on passe pour aujourd’hui. Quand il y en a un, regardez l’image, pas le source Mermaid : beaucoup d’éditeurs ont un aperçu, et <a href="/fr/view-markdown-on-mac/">Comment afficher un fichier Markdown sur Mac</a> et <a href="/fr/vs/markdown-preview-tools/">Afficher du Markdown ailleurs</a> présentent les options. Dans MarsDawn, le diagramme rendu se trouve à côté de son source (&#8984;2), et un diagramme cassé affiche son source avec l’erreur en dessous, ce qui mérite un commentaire à part entière.</p>
<p><strong>5. Listez les fichiers et systèmes que le plan touche, et posez des questions sur tout ce que vous n’avez pas demandé.</strong> <em>(étapes 4 et 5 ensemble, une minute environ)</em> Ici : la configuration du stockage, les templates, un dossier sur le serveur, un bucket. Qui peut lire le bucket ? Vous n’avez pas dit qu’il devait être public. Si vous avez ouvert le dossier de travail de l’agent dans MarsDawn (Fichier &#9656; Ouvrir un dossier&#8230;, &#8679;&#8984;O), les nouveaux fichiers qu’il écrit apparaissent dans l’onglet Fichiers en une seconde environ, et l’en-tête indique la branche git ou le worktree, pour que vous sachiez quel checkout vous relisez.</p>
<p><strong>6. Rédigez vos retours sous la forme endroit, problème, correction, un problème par ligne.</strong> <em>(la dernière minute)</em></p>
<pre><code>plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.</code></pre>
<p>N’importe quel éditeur avec des numéros de ligne fait l’affaire. Dans MarsDawn, Édition &#9656; Copier la référence (&#8997;&#8984;C) copie votre position sous la forme <code>plan.md:10</code>, et Copier pour l’IA (&#8963;&#8997;&#8984;C) ajoute le texte sélectionné en dessous.</p>

<h2>Si vous avez une minute</h2>
<p>Faites l’étape 2. C’est là qu’on prend en défaut un agent qui se croit fini.</p>

<h2>Quand cinq minutes ne suffisent pas</h2>
<p>Parfois, vous ne pouvez pas savoir si une étape est juste, parce qu’elle sort de votre domaine. Jess Ou, dans l’article explicatif de LangChain sur les agents paru en 2026, le dit en deux phrases : « Ne déléguez pas un jugement que vous ne pouvez pas évaluer. Si vous ne reconnaîtriez pas une bonne réponse, l’agent non plus. » Notre conclusion : si vous ne pouvez pas juger une étape, ce n’est pas une raison pour l’approuver plus vite. C’est une raison pour demander à quelqu’un qui le peut.</p>

<h2>Ce que MarsDawn fait ici, et ce qu’il ne fait pas</h2>
<p>MarsDawn n’embarque aucun modèle d’IA. Il ne trouvera pas les problèmes de ce plan, et il ne fait ni l’étape 2 ni l’étape 3. Il garde le fichier lisible pendant que vous travaillez : le plan pour l’étape 1, les diagrammes rendus pour l’étape 4, l’onglet Fichiers pour l’étape 5, les références de ligne pour l’étape 6. Et si l’agent révise le plan pendant votre lecture, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées.</p>
<p>Une fois le plan arrêté, si quelqu’un d’autre doit le voir, <a href="/fr/sharing-exported-pdfs/">Partager des PDF exportés</a> et <a href="/fr/markdown-to-pdf/">Markdown en PDF</a> expliquent comment le transmettre en PDF.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le <a href="{k.LISTING_URL}">Mac App Store</a>. Il existe aussi l’outil en ligne de commande gratuit <code>marsdawn</code> :</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; À savoir avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Pourquoi ce que rend un agent est difficile à lire : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
  <li>Pourquoi les agents exposent leurs plans : <a href="/fr/agent-transparency/">Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?</a></li>
  <li>Les plans ne sont pas la seule chose que rendent les agents : <a href="/fr/agent-design-patterns/">Quatre modèles de conception d’agents et les documents que chacun vous remet</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Chip Huyen, « Agents », 7 janvier 2025 : <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou, « What is an AI agent? », LangChain, 31 juillet 2026 : <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": 'Quatre modèles de conception d’agents et les documents qu’ils vous remettent · MarsDawn',
        "description": 'Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.',
        "body": f"""
<section class="intro">
  <h1>Quatre modèles de conception d’agents et les documents que chacun vous remet</h1>
  <p>En mars 2024, Andrew Ng a décrit dans sa newsletter, The Batch, quatre modèles de conception pour les agents IA : la réflexion, l’utilisation d’outils, la planification et la collaboration multi-agents. On les aborde généralement du point de vue de ceux qui construisent les agents, comme des moyens d’obtenir de meilleurs résultats d’un modèle. Cet article se place de l’autre côté. Si vous utilisez un agent fondé sur l’un de ces modèles, qu’est-ce qui atterrit dans votre dossier, et que devez-vous lire en premier ?</p>
</section>

<div class="summary"><p><strong>Les quatre modèles sont d’Andrew Ng. Les documents que chacun tend à vous remettre, et ce qu’il faut y vérifier, relèvent de notre propre déduction. Il n’écrit sur aucun des deux points, et il ne plaide pas pour la relecture humaine dans cette série.</strong></p></div>

<h2>Les quatre modèles, en bref</h2>
<p>Ng les décrit dans « Agentic Design Patterns Part 1 ». En résumé : avec la <strong>réflexion</strong>, le modèle relit son propre travail et l’améliore. Avec l’<strong>utilisation d’outils</strong>, il peut appeler des outils comme la recherche web ou l’exécution de code. Avec la <strong>planification</strong>, il élabore un plan en plusieurs étapes et l’exécute. Avec la <strong>collaboration multi-agents</strong>, plusieurs agents se répartissent le travail et en discutent.</p>
<p>Dans la partie 1, il montre le gain sur un benchmark de code, HumanEval, avec des résultats que son équipe a rassemblés auprès de plusieurs groupes de recherche : « GPT-3.5 (zero-shot) obtenait 48,1 % de réponses correctes. GPT-4 (zero-shot) fait mieux, avec 67,0 %. Cependant, le progrès de GPT-3.5 à GPT-4 est éclipsé par l’intégration d’un workflow agentique itératif. De fait, intégré à une boucle d’agent, GPT-3.5 atteint jusqu’à 95,1 %. » Ces chiffres portent sur un seul benchmark de code, et 95,1 % est le meilleur cas (« jusqu’à »). Ils montrent que les workflows d’agents peuvent améliorer le résultat. Ils ne disent rien de qui le vérifie.</p>
<p><strong>À partir d’ici, les documents et les vérifications sont notre lecture, pas celle de Ng.</strong> Les vrais agents mélangent d’ailleurs les modèles. Un agent de code peut planifier, lancer des outils et relire son propre travail dans une même session : vous recevrez donc souvent les quatre types de fichiers.</p>

<h2>1. Réflexion : un brouillon qui s’est déjà relu</h2>
<p>L’article de Ng sur la réflexion la présente comme l’automatisation du retour qu’une personne donnerait sinon : « Et si l’on automatisait l’étape du retour critique, pour que le modèle critique automatiquement sa propre sortie et améliore sa réponse ? »</p>
<p><strong>Ce qu’il tend à vous remettre :</strong> un document révisé, parfois avec une section d’autoévaluation ou des lignes comme « cas limites revérifiés ».</p>
<p><strong>Ce qu’il faut vérifier :</strong> le résultat par rapport à <em>votre</em> demande, pas par rapport à l’autocritique de l’agent. L’autoévaluation peut se tromper à sa façon. Chip Huyen : « Un mode intéressant d’échec de planification provient d’erreurs de réflexion. L’agent est convaincu d’avoir accompli une tâche alors que ce n’est pas le cas. » Lilian Weng, sur son blog Lil’Log en juin 2023, alors chez OpenAI, à propos des modèles de l’époque : « Le manque d’expertise peut empêcher les LLM de connaître leurs défauts, et donc de bien juger de la justesse des résultats d’une tâche. » (Dans l’étude qu’elle décrivait, l’évaluation des résultats par un LLM et celle d’experts humains ne concordaient pas.) S’il est écrit « vérifié », vérifiez une chose vous-même.</p>

<h2>2. Utilisation d’outils : un compte rendu de ce qui a tourné</h2>
<p><strong>Ce qu’il tend à vous remettre :</strong> un résumé de ce que l’agent a lancé ou recherché et de ce qui en est ressorti. « Suite de tests lancée : tout passe. » Un tableau de résultats. Des liens trouvés.</p>
<p>Le guide d’Anthropic présente les résultats d’outils comme la vérification que l’agent fait de lui-même : « Pendant l’exécution, il est crucial que les agents obtiennent à chaque étape une “vérité terrain” de l’environnement (comme les résultats d’appels d’outils ou d’exécution de code) pour évaluer leur progression. » Cette vérification se fait à l’intérieur de l’agent. Ce qui vous parvient, c’est le récit qu’il en fait.</p>
<p><strong>Ce qu’il faut vérifier :</strong> que chaque affirmation remonte à une sortie que vous pouvez voir. Comparez un chiffre du résumé à la vraie sortie. Ouvrez l’un des liens.</p>

<h2>3. Planification : <code>plan.md</code></h2>
<p><strong>Ce qu’il tend à vous remettre :</strong> un plan, une spécification, une liste de tâches que l’agent coche au fur et à mesure.</p>
<p>Ng est franc sur ce modèle dans la partie 4 :</p>
<blockquote><p>« D’un côté, la planification est une capacité très puissante ; de l’autre, elle produit des résultats moins prévisibles. D’après mon expérience, si j’arrive à faire fonctionner de façon fiable les modèles agentiques de réflexion et d’utilisation d’outils et à améliorer ainsi les performances de mes applications, la planification est une technologie moins mûre, et j’ai du mal à prévoir à l’avance ce qu’elle va faire. »</p></blockquote>
<p>Il est aussi optimiste : « Mais le domaine continue d’évoluer rapidement, et je suis convaincu que les capacités de planification vont progresser vite. »</p>
<p><strong>Ce qu’il faut vérifier :</strong> le plan avant qu’il ne s’exécute, avec <a href="/fr/reviewing-agent-plans/">la relecture en cinq minutes</a> : structure, une affirmation, étapes irréversibles, diagrammes, périmètre. Si l’agent réécrit le plan en cours de route, comparez-le à la version que vous avez approuvée ; s’il est dans git, <code>git diff plan.md</code> montre ce qui a changé. Dans MarsDawn, l’onglet Plan montre la structure d’un long plan, et un plan réécrit se recharge sans vous faire perdre votre position, tant que vous n’avez pas de modifications non enregistrées.</p>

<h2>4. Collaboration multi-agents : plusieurs fichiers, plusieurs auteurs</h2>
<p><strong>Ce qu’il tend à vous remettre :</strong> une spécification d’un agent, des notes d’implémentation d’un deuxième, une relecture d’un troisième, et des résumés qui circulent entre eux. Parfois, chacun travaille dans sa propre branche ou son propre worktree.</p>
<p><strong>Ce qu’il faut vérifier :</strong> les passations. Là où un agent résume le travail d’un autre, cherchez une exigence qui ne serait pas passée. Cherchez deux fichiers qui se contredisent, et décidez lequel fait foi avant que quiconque ne s’appuie sur l’autre. Dans MarsDawn, ouvrez le dossier partagé avec Fichier &#9656; Ouvrir un dossier&#8230; (&#8679;&#8984;O) : les nouveaux fichiers apparaissent dans l’onglet Fichiers en une seconde environ, à mesure que les agents les écrivent, et pour un checkout git, l’en-tête indique la branche ou le worktree, pour que deux fenêtres affichant le même nom de fichier sur des branches différentes ne se ressemblent pas. Quand le résultat doit parvenir à des personnes qui ne lisent pas le Markdown, <a href="/fr/sharing-exported-pdfs/">Partager des PDF exportés</a> couvre cette étape.</p>

<h2>En un coup d’œil</h2>
<table>
<thead><tr><th>Modèle (Ng)</th><th>Ce qu’il tend à vous remettre (notre déduction)</th><th>À lire en premier (notre suggestion)</th></tr></thead>
<tbody>
<tr><td>Réflexion</td><td>Un brouillon révisé, peut-être avec une autoévaluation</td><td>Le résultat par rapport à votre demande ; vérifier un « vérifié »</td></tr>
<tr><td>Utilisation d’outils</td><td>Un compte rendu de ce qui a tourné et de ce qui en est ressorti</td><td>Une affirmation remontée jusqu’à la vraie sortie</td></tr>
<tr><td>Planification</td><td><code>plan.md</code>, une spécification, une liste de tâches</td><td>La relecture en cinq minutes, avant l’exécution</td></tr>
<tr><td>Collaboration multi-agents</td><td>Plusieurs fichiers de plusieurs agents, peut-être sur plusieurs branches</td><td>Les passations, et le fichier qui fait foi</td></tr>
</tbody>
</table>
<p>Aucun des auteurs cités ici ne mentionne MarsDawn, et aucun ne le recommande, pas plus qu’aucun autre outil Markdown. MarsDawn n’embarque aucun modèle d’IA : il ne sait pas quel modèle a produit un fichier, et il ne fera pas ces vérifications à votre place. Il garde les fichiers lisibles pendant que vous les faites.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le <a href="{k.LISTING_URL}">Mac App Store</a>. Il existe aussi l’outil en ligne de commande gratuit <code>marsdawn</code> :</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Il exporte le Markdown en PDF sans l’app : voir <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; À savoir avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Pourquoi ce que rend un agent est difficile à lire, avec une liste de vérification : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
  <li>La vérification du plan en entier : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</li>
  <li>Ce que la transparence vous demande, et ce qu’elle ne vous demande pas : <a href="/fr/agent-transparency/">Anthropic veut des agents transparents. Mais qui lit ce qu’ils exposent ?</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Andrew Ng, « Agentic Design Patterns Part 1 », The Batch, 20 mars 2024 : <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, « Agentic Design Patterns Part 2, Reflection », The Batch, 27 mars 2024 : <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng, « Agentic Design Patterns Part 4, Planning », The Batch, 10 avril 2024 : <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen, « Agents », 7 janvier 2025 : <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng, « LLM Powered Autonomous Agents », Lil’Log, 23 juin 2023 : <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S. et Barry Zhang, « Building Effective Agents », Anthropic, 19 décembre 2024 : <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (cité d’après la version en ligne le 26/09/2026).</li>
</ul>
""",
    }

    # /templates/ pages (scripts/templates_pages.py), one entry per table there, for #162 to merge.
    # The downloads are TEMPLATES byte for byte; Mermaid node labels are translated, as in ja.
    templates = {
        'ui_labels': {"templates": "Modèles", "templates-spec": "Modèle de spécification",
                      "templates-flowchart": "Modèle d’organigramme", "templates-meeting-notes": "Modèle de compte rendu"},
        'labels': {"template": "Le modèle", "download": "Télécharger {file}", "looks": "À quoi il ressemble",
                   "ask": "Demandez à votre agent", "share": "Le partager en PDF", "doesnt": "Ce qu’il ne fait pas",
                   "faq": "Questions", "more": "Autres modèles", "sep": " : ",
                   "img_alt": "La première page de {file}, exportée en PDF avec marsdawn export."},
        'hub': {"title": "Modèles Markdown · MarsDawn",
                "description": "Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.",
                "h1": "Modèles Markdown",
                "lede": "Pour les documents qu’un agent rédige et que vous lisez. Chaque modèle est accompagné d’un prompt pour votre agent. Ouvrez le fichier rempli dans MarsDawn pour lire ce qu’il a écrit.",
                "items": {"spec": ("Spécification (PRD)", "problème, objectifs, exigences, un diagramme de flux et des critères d’acceptation."),
                          "flowchart": ("Organigramme", "un diagramme Mermaid, avec les étapes écrites en dessous."),
                          "meeting-notes": ("Compte rendu de réunion", "décisions et actions, chacune avec un responsable.")}},
        'pages': {
            "spec": {
                "title": "Modèle de spécification (PRD) en Markdown · MarsDawn",
                "description": "Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.",
                "h1": "Modèle de spécification (PRD) en Markdown",
                "lede": "Une spécification que votre agent peut remplir et que vous pouvez lire d’une traite : le problème, les objectifs, les exigences, un diagramme de flux et les critères d’acceptation. Quand vous modifiez une exigence, demandez à l’agent d’harmoniser le reste.",
                "caption": "Exporté avec <code>marsdawn export spec.md</code>. L’outil en ligne de commande gratuit produit le même rendu que l’aperçu de MarsDawn, diagramme compris.",
                "prompt": "Rédige une spécification pour [la fonctionnalité] dans spec.md, à partir du modèle disponible à {url}. Donne un identifiant à chaque exigence, et utilise les mêmes identifiants dans le flux et dans les critères d’acceptation. Une fois que c’est écrit, lance marsdawn open spec.md.",
                "share": "<code>marsdawn export spec.md</code> écrit spec.pdf à côté, pour qui ne lit pas le Markdown.",
                "doesnt": "MarsDawn affiche la spécification, le tableau et le diagramme. Il ne vérifie pas que les critères d’acceptation couvrent chaque exigence. C’est le travail de l’agent, et celui de votre relecture.",
                "faq": [("Le diagramme de flux nécessite-t-il d’installer quelque chose ?", "Non. MarsDawn et <code>marsdawn export</code> dessinent Mermaid eux-mêmes, hors ligne."),
                        ("Puis-je modifier la spécification dans MarsDawn ?", "Oui. C’est un éditeur Markdown avec l’aperçu à côté du source. L’agent verra votre modification la prochaine fois qu’il lira le fichier.")],
            },
            "flowchart": {
                "title": "Modèle d’organigramme en Markdown (Mermaid) · MarsDawn",
                "description": "Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.",
                "h1": "Modèle d’organigramme en Markdown",
                "lede": "Un organigramme Mermaid avec les étapes détaillées en dessous, pour que le diagramme et le texte puissent se vérifier l’un l’autre. Retirez une étape, et demandez à l’agent de corriger le reste.",
                "caption": "Exporté avec <code>marsdawn export flowchart.md</code>. L’outil en ligne de commande gratuit produit le même rendu que l’aperçu de MarsDawn, diagramme compris.",
                "prompt": "Dessine le flux de [le processus] dans flowchart.md, à partir du modèle disponible à {url}. Une étape numérotée par nœud, dans le même ordre. Une fois que c’est écrit, lance marsdawn open flowchart.md.",
                "share": "<code>marsdawn export flowchart.md</code> : le diagramme est dessiné dans le PDF.",
                "doesnt": "MarsDawn dessine ce que dit le Mermaid. Il ne permet pas de disposer le diagramme à la main, et il ne synchronise pas les étapes numérotées avec les nœuds. Si le Mermaid contient une erreur, l’aperçu affiche l’erreur au lieu du diagramme.",
                "faq": [("Quels diagrammes fonctionnent ?", "Tout ce que Mermaid sait dessiner : organigrammes, diagrammes de séquence, diagrammes d’états, et plus encore."),
                        ("Pourquoi écrire aussi les étapes ?", "Qui survole regarde le diagramme ; qui vérifie a besoin du texte. L’agent peut garder les deux en phase.")],
            },
            "meeting-notes": {
                "title": "Modèle de compte rendu de réunion en Markdown · MarsDawn",
                "description": "Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.",
                "h1": "Modèle de compte rendu de réunion en Markdown",
                "lede": "D’abord les décisions, puis les actions, chacune avec un responsable. Laissez votre agent rédiger le compte rendu à partir de la transcription, et lisez-le avant qu’il ne parte. Quand une décision change, demandez à l’agent d’harmoniser les actions.",
                "caption": "Exporté avec <code>marsdawn export meeting-notes.md</code>. L’outil en ligne de commande gratuit produit le même rendu que l’aperçu de MarsDawn.",
                "prompt": "Rédige le compte rendu de cette réunion dans meeting-notes.md, à partir du modèle disponible à {url}. Les décisions d’abord, une ligne chacune ; chaque action a un seul responsable et une date. Une fois que c’est écrit, lance marsdawn open meeting-notes.md.",
                "share": "<code>marsdawn export meeting-notes.md</code> écrit un PDF que vous pouvez joindre au mail de suivi.",
                "doesnt": "MarsDawn n’enregistre pas la réunion, ne la transcrit pas et ne suit pas les actions. Il affiche le compte rendu tel qu’il sera lu.",
                "faq": [("Les cases à cocher fonctionnent-elles ?", "Elles s’affichent comme des cases à cocher dans l’aperçu et dans le PDF. Pour en cocher une, remplacez <code>[ ]</code> par <code>[x]</code> dans le source."),
                        ("L’agent peut-il garder le compte rendu et les actions en phase ?", "Oui, c’est tout l’intérêt de la boucle : modifiez l’un, et demandez-lui de mettre à jour le reste. MarsDawn vous montre le résultat.")],
            },
        },
        'templates': {
            "spec": """# Spécification : nom de la fonctionnalité

Statut : brouillon · Responsable : nom · Mise à jour : date

## Problème

_Ce qui ne va pas aujourd’hui, pour qui, et comment on le sait._

## Objectifs

- _Ce qui sera vrai une fois livré._

## Hors périmètre

- _Ce que cela ne fait pas, délibérément._

## Exigences

| ID | Exigence | Priorité |
|----|----------|----------|
| R1 | _Exigence_ | Indispensable |
| R2 | _Exigence_ | Souhaitable |

## Flux

```mermaid
flowchart LR
  A[Début] --> B[Étape] --> C[Résultat]
```

## Critères d’acceptation

- [ ] R1 : _Comment on le vérifie._
- [ ] R2 : _Comment on le vérifie._

## Questions ouvertes

- _Question._
""",
            "flowchart": """# Nom du flux

_Une phrase : ce qui entre, ce qui sort._

## Diagramme

```mermaid
flowchart LR
  A[Première étape] --> B[Deuxième étape]
  B --> C[Troisième étape]
  C --> D[Terminé]
```

## Étapes

1. **Première étape** : _qui s’en charge, et ce qu’il transmet._
2. **Deuxième étape** : _…_
3. **Troisième étape** : _…_
4. **Terminé** : _ce que « terminé » veut dire ici._
""",
            "meeting-notes": """# Nom de la réunion, date

Participants : _noms_

## Décisions

- _Ce qui a été décidé, une ligne chacune._

## Actions

- [ ] Nom : _quoi, pour quand._
- [ ] Nom : _quoi, pour quand._

## Notes

- _Tout ce qui mérite d’être gardé sans être une décision ni une action._
""",
        },
        'scene_text': {
            "spec": {"title": "Spécification : codes de connexion", "req": "Exigences", "flow": "Flux", "acc": "Acceptation",
                     "r1": "R1 : envoyer un code à six chiffres.", "r2": "R2 : le code expire en 10 min.",
                     "r3": "R3 : demander un second facteur.", "n1": "E-mail", "n2": "Code", "n3": "Second facteur",
                     "n4": "Connecté", "a1": "R1 : le code arrive en 1 min.", "a3": "R3 : une fois par appareil.",
                     "ask": "J’ai retiré R3. Mets le flux et les critères d’acceptation d’accord.",
                     "reply": "C’est fait. Le flux saute le second facteur, et la vérification de R3 a disparu.",
                     "alt": "Un terminal ouvre spec.md dans MarsDawn. Le lecteur supprime l’exigence R3, et l’agent retire son étape du diagramme de flux et sa vérification des critères d’acceptation."},
            "flowchart": {"title": "Flux de publication", "diagram": "Diagramme", "steps": "Étapes",
                          "n1": "Brouillon", "n2": "Relecture", "n3": "Juridique", "n4": "Publication",
                          "s1": "1. Brouillon : premier jet.", "s2": "2. Relecture : un éditeur le lit.",
                          "s3": "3. Juridique : vérifie les affirmations.", "s4": "{c}. Publication : mise en ligne.",
                          "ask": "J’ai retiré Juridique du diagramme. Corrige la liaison et les étapes.",
                          "reply": "C’est fait. Relecture mène directement à Publication, et les étapes sont renumérotées.",
                          "alt": "Un terminal ouvre flowchart.md dans MarsDawn. Le lecteur retire l’étape Juridique du diagramme Mermaid, et l’agent reconnecte le diagramme et renumérote les étapes en dessous."},
            "meeting-notes": {"title": "Point hebdo, 5 oct.", "decisions": "Décisions", "actions": "Actions",
                              "d1": "Ouvrir la bêta à {u} personnes.", "d2": "Livrer vendredi.",
                              "t1": "Mia : envoyer {a} invitations.", "t2": "Leo : ajouter {b} places.", "t3": "Ana : assister {c} utilisateurs.",
                              "ask": "La bêta passe à 80 personnes. Mets à jour les actions.",
                              "reply": "C’est fait. Les trois actions disent 80.",
                              "alt": "Un terminal ouvre meeting-notes.md dans MarsDawn. Le lecteur fait passer une décision de 50 à 80 personnes, et l’agent met à jour les trois actions en conséquence."},
        },
    }
    # The homepage loop (scripts/loop_anim.py COPY). Tab names follow the app's fr strings; the two
    # days have the same width (tabular digits), as the stacked swap needs.
    loop_copy = {
        "outline": "Plan", "files": "Fichiers",
        "title": "Note de lancement",
        "sections": [("Ce qui change", "La page de connexion commence par l’e-mail. Sortie le {a}."),
                     ("Date de sortie", "Le {u}, à midi."),
                     ("Qui fait quoi", "L’équipe technique active le flag le {b}.")],
        "old": "7 oct.", "new": "9 oct.",
        "ask": "J’ai déplacé le lancement. Mets les autres sections d’accord.",
        "reply": "C’est fait. Les deux sections disent maintenant 9 oct.",
        "alt": "Un terminal ouvre launch-note.md dans MarsDawn. Le lecteur déplace la date de lancement "
               "du 7 au 9 octobre, l’agent met à jour les deux autres sections en conséquence, et "
               "la boucle recommence.",
        "pause": "Mettre l’animation en pause", "pause_short": "Pause",
    }

    app_ui_languages = 'anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen'
    ui = {'home': 'MarsDawn', 'privacy': 'Politique de confidentialité', 'support': 'Assistance', 'cli': 'Ligne de commande', 'agents': 'marsdawn pour les agents', 'using_cli': 'Utiliser la CLI', 'markdown-to-pdf': 'Markdown vers PDF', 'skill': 'Skill pour agents', 'view-markdown-on-mac': 'Afficher du Markdown sur Mac', 'vs-macmd-viewer': 'MacMD Viewer vs MarsDawn', 'updated': f'Dernière mise à jour\xa0: {k.UPDATED}', 'tagline': 'Lisez ce que votre agent a écrit.', 'slogan': 'Une nouvelle aube pour Markdown.', 'footer_store': f'MarsDawn est disponible sur le <a href="{k.LISTING_URL}">Mac App Store</a>.', 'footer_nav': 'Site', 'more': 'Plus', 'yours': 'Vos textes restent sur votre Mac', 'pay-once': 'Essai gratuit, achat unique', 'pdf': 'Export PDF', 'native': 'Une app Mac', 'limits': 'Ce que MarsDawn ne fait pas', 'mcp': 'Serveur MCP', 'token-efficient-review': 'Relire en économisant les tokens', 'vs-markdown-preview-tools': 'Afficher du Markdown ailleurs vs MarsDawn', 'themes': 'Thèmes de l’aperçu et export PDF', 'themes-new': 'Créer un thème', 'themes-gallery': 'Galerie de thèmes', 'sharing-exported-pdfs': 'Partager les PDF exportés', 'reviewing-ai-output': 'Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain', 'reading-agent-output': 'Lire ce que votre agent vous rend', 'agent-transparency': 'Transparence des agents', 'reviewing-agent-plans': 'Relire le plan d’un agent', 'agent-design-patterns': 'Patrons de conception d’agents', 'changelog': 'Historique des versions', 'reading-notes': 'Notes de lecture de la rédaction', 'reading-notes-anthropic': 'Notes de lecture : Anthropic', 'reading-notes-chip-huyen': 'Notes de lecture : Chip Huyen', 'reading-notes-lilian-weng': 'Notes de lecture : Lilian Weng', 'reading-notes-harrison-chase': 'Notes de lecture : Harrison Chase', 'reading-notes-langchain': 'Notes de lecture : LangChain (Jess Ou)', 'reading-notes-andrew-ng': 'Notes de lecture : Andrew Ng', 'consent_text': 'Ce site utilise des cookies de mesure d’audience pour voir comment les visiteurs l’utilisent. Ils restent désactivés tant que vous n’acceptez pas.', 'consent_accept': 'Accepter', 'consent_decline': 'Refuser', 'consent_aria': 'Consentement aux cookies', 'cookie_settings': 'Réglages des cookies', 'view_markdown_source': 'Voir la source Markdown'}
    store_chip = 'Sur le Mac App Store'
    trait_link = {'yours': ['Vos textes restent sur votre Mac', 'Pas de compte, pas de synchronisation, pas de cloud.'], 'pay-once': ['Essai gratuit, achat unique', 'Gratuit pendant 14 jours, puis 4,99 USD une seule fois. Sans abonnement.'], 'pdf': ['Export PDF', 'Diagrammes, code coloré, sauts de page soignés.'], 'native': ['Une app Mac', 'Fenêtres et onglets natifs, enregistrement automatique, Coup d’œil.'], 'limits': ['Ce que MarsDawn ne fait pas', 'À savoir avant d’acheter.']}
    trait_nav_heading = 'Ce que vous pouvez attendre de MarsDawn'
    figure_list_label = 'Sur cette capture d’écran'


    pages['reading-notes'] = {
        "title": "Notes de lecture de la rédaction · MarsDawn",
        "description": "Six courtes notes sur ce que les gens qui construisent des agents IA avancent réellement — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain et Andrew Ng — et ce que cela signifie pour la personne qui doit lire ce qu’un tel agent rend.",
        "body": f"""
<section class="intro">
  <h1>Notes de lecture de la rédaction</h1>
  <p>Six personnes ont écrit sur le fonctionnement des agents IA : de quoi ils sont faits, ce qui rend un système « agentic », quels patrons de conception tiennent en pratique et lesquels pas encore. Aucune n’a écrit sur la lecture de ce qu’un agent rend, et aucune ne mentionne MarsDawn ni ne recommande d’outil Markdown. Nous avons lu chaque texte pour lui-même, marqué clairement où commence notre propre lecture, et posé à chaque source la même question : quel document tend à atterrir dans votre dossier à cause de ceci, et où MarsDawn aide à le lire ?</p>
</section>

<p>Si vous voulez d’abord la version courte et pratique, commencez par <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a> et <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>. Ces six notes vont plus près des sources derrière ces pages. Chacune se suffit ; lisez-les dans n’importe quel ordre.</p>

<ul>
  <li><a href="/fr/reading-notes/anthropic-building-effective-agents/">Anthropic trace une ligne entre workflows et agents. Où se situe votre lecture ?</a> &#8212; Le guide d’Anthropic pour qui construit des agents sépare un pipeline fixe d’un modèle qui dirige lui-même l’étape suivante, et décrit un workflow où le « relecteur » est un second appel LLM, pas une personne.</li>
  <li><a href="/fr/reading-notes/chip-huyen-agents/">La distinction read-only / write action de Chip Huyen, et pourquoi elle compte avant d’approuver</a> &#8212; sa définition simple d’un agent, et la différence entre actions qui ne font que regarder et actions qui changent quelque chose : c’est là qu’une relecture de cinq minutes gagne son temps.</li>
  <li><a href="/fr/reading-notes/lilian-weng-llm-agents/">Le plan d’agent de Lilian Weng en 2023, et le fichier que chaque partie laisse</a> &#8212; cerveau, planification, mémoire, usage d’outils : son propre cadre de ce dont un agent est fait, et la limite qu’elle nomme dans les plans qui ne s’ajustent pas quand quelque chose tourne mal.</li>
  <li><a href="/fr/reading-notes/harrison-chase-what-is-an-agent/">Le spectre de Harrison Chase : plus c’est agentic, plus vous voudrez regarder</a> &#8212; sa définition technique d’un agent, et son plaidoyer pour l’observabilité à mesure qu’un système avance sur ce spectre.</li>
  <li><a href="/fr/reading-notes/langchain-what-is-an-agent/">Le pipeline d’evals de Jess Ou, et l’étape qui reste encore la vôtre</a> &#8212; en juillet 2026, LangChain a publié un nouveau « What is an AI agent ? » de Jess Ou à l’adresse où se trouvait le billet 2024 de Harrison Chase ; sa définition est presque mot pour mot la sienne, et elle décrit où l’évaluation automatique s’arrête et où une personne doit intervenir.</li>
  <li><a href="/fr/reading-notes/andrew-ng-design-patterns/">Andrew Ng classe ses propres patrons de conception selon leur prévisibilité</a> &#8212; sur cinq lettres dans The Batch, il dit clairement lesquels il trouve plus fiables et lesquels il peines à prévoir.</li>
</ul>

<p>Aucun de ces six textes n’argumente qu’il faille lire plus soigneusement la sortie d’un agent, et aucun ne parle de MarsDawn. Ce lien, là où nous le traçons, est le nôtre, et chaque note le dit.</p>
""",
    }


    pages['reading-notes/anthropic-building-effective-agents'] = {
        "title": 'Anthropic trace une ligne entre workflows et agents. Où se situe votre lecture\xa0? · MarsDawn',
        "description": 'Le guide d’Anthropic de décembre 2024 pour qui construit des agents sépare workflows et agents et décrit cinq patrons de workflow, dont un où un second appel LLM relit le premier. Ce que cela signifie pour ce qui atterrit dans votre dossier.',
        "body": f"""
<section class="intro">
  <h1>Anthropic trace une ligne entre workflows et agents. Où se situe votre lecture ?</h1>
</section>

<div class="summary"><p><strong>Le guide d’Anthropic de décembre 2024 pour qui construit des agents IA commence en séparant deux choses qu’il appelle « workflows » et « agents », recommande ensuite de commencer par la solution la plus simple qui marche &#8212; éventuellement aucun système agentic &#8212; et de n’atteindre l’un de ses cinq patrons de workflow que lorsque ce n’est plus assez. L’un de ces patrons place un second appel LLM au siège du relecteur. Cette note porte sur ce patron, et sur ce que les quatre autres vous laissent à lire.</strong></p></div>

<h2>Ce que le guide avance</h2>
<p>Erik S. et Barry Zhang ont écrit « Building Effective Agents » pour des ingénieurs qui décident comment construire avec des LLM. Ça commence par une définition :</p>
<blockquote><p>&#8220;Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.&#8221;</p></blockquote>
<p>Puis le conseil commence par la retenue :</p>
<blockquote><p>&#8220;When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.&#8221;</p></blockquote>
<p>Quand plus de structure est nécessaire, ils décrivent cinq patrons de workflow : prompt chaining (une tâche découpée en une suite d’appels, avec des contrôles optionnels entre les étapes), routing, parallelization, orchestrator-workers (un LLM découpe une tâche, la confie à des LLM workers, puis combine les résultats) et evaluator-optimizer. Ce dernier :</p>
<blockquote><p>&#8220;In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.&#8221;</p></blockquote>
<p>Anthropic ne mentionne MarsDawn nulle part dans ce guide et ne recommande aucun outil Markdown. <code>/agent-transparency/</code> couvre déjà en détail le principe de transparence de ce guide et son langage de « checkpoints » &#8212; cette note ne le répète pas. C’est aussi là que vit la phrase du guide sur la relecture humaine du code, dans son contexte propre (une annexe sur les agents de codage).</p>

<h2>Notre lecture, pas celle d’Anthropic</h2>
<p>Anthropic ne dit pas qui vérifie la sortie finale d’un workflow une fois terminé, et rien de tout cela ne décrit un document &#8212; c’est une décision d’architecture pour qui construit le système. Mais les cinq patrons ne produisent pas le même genre de fichier à lire. Le prompt chaining et le routing sont en général de la plomberie invisible ; si quelque chose vous atteint, c’est la dernière sortie de la chaîne, comme n’importe quelle autre réponse unique. Orchestrator-workers est différent : si votre agent de codage utilise ce patron en interne, ce qui atterrit dans votre dossier peut être un document assemblé à partir de plusieurs appels workers cousus par l’orchestrateur, et une erreur dans la tranche d’un worker peut passer inaperçue dans un résumé qui se lit fluide de bout en bout.</p>
<p>Evaluator-optimizer mérite qu’on s’y arrête, parce que le guide met un second appel LLM là où un relecteur humain pourrait sinon s’asseoir. C’est une façon légitime d’attraper à bas coût une classe d’erreurs, mais ça reste un modèle qui vérifie un modèle selon les critères qu’on lui a donnés &#8212; la même réserve que d’autres auteurs ici soulèvent quand un modèle juge son propre travail ou celui d’un autre. Rien dans le guide ne dit qu’une personne devrait revérifier le verdict de l’évaluateur ; il ne prend aucune position là-dessus. Si vous lisez ce que tout cela rend, « la boucle l’a approuvé » et « je l’ai vérifié » ne sont pas la même phrase, même quand le fichier devant vous a l’air identique dans les deux cas.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn ne sait pas quel patron de workflow a produit un fichier, et n’a aucun modèle d’IA à l’intérieur &#8212; il ne lancera pas sa propre étape d’évaluateur, et ne vous dira pas si celle qu’Anthropic décrit a fait son travail. Ce qu’il fait : l’onglet Plan de la barre latérale (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) liste les titres d’un long fichier assemblé par un orchestrateur, et un clic y saute. La source et la page rendue côte à côte (&#8984;2) défilent ensemble, avec les diagrammes Mermaid et les maths KaTeX dessinés plutôt que laissés en source. Si l’agent révise le fichier pendant que vous lisez, MarsDawn le recharge et garde votre place, tant que vous n’avez pas de modifications non enregistrées. Édition &#9656; Copier la référence (&#8997;&#8984;C) copie votre place sous la forme <code>docs/plan.md:42</code>, prête à coller dans la conversation avec l’agent.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>Le reste du principe de transparence et du langage de checkpoints de ce guide : <a href="/fr/agent-transparency/">Anthropic dit que les agents doivent être transparents. Qui lit ce qu’ils exposent ?</a></li>
  <li>Pourquoi la sortie d’un agent est en général difficile à lire : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (récupéré et cité le 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/chip-huyen-agents'] = {
        "title": 'La distinction read-only / write action de Chip Huyen, et pourquoi elle compte avant d’approuver · MarsDawn',
        "description": 'L’essai «\xa0Agents\xa0» de Chip Huyen de janvier 2025 partage les actions d’un agent en read-only et write. Pourquoi cette distinction est un moyen rapide de repérer, dans un plan, la ligne qui mérite un regard plus attentif avant d’approuver.',
        "body": f"""
<section class="intro">
  <h1>La distinction read-only / write action de Chip Huyen, et pourquoi elle compte avant d’approuver</h1>
</section>

<div class="summary"><p><strong>L’essai « Agents » de Chip Huyen de janvier 2025 part de la définition du manuel et aboutit à quelque chose de plus précis : les actions d’un agent se partagent entre celles qui ne font que regarder le monde et celles qui le changent. Cette distinction est un bon moyen de décider, dans les cinq minutes dont vous disposez, quelles lignes d’un plan méritent un regard plus attentif avant de dire oui.</strong></p></div>

<h2>Ce que le texte avance</h2>
<p>Huyen ouvre simplement :</p>
<blockquote><p>&#8220;An agent is anything that can perceive its environment and act upon that environment.&#8221;</p></blockquote>
<p>De là elle construit ce dont un agent a besoin : un environnement où agir, et un ensemble d’outils &#8212; son « tool inventory » &#8212; qui détermine ce qu’il peut faire. Elle nomme la distinction entre les actions qui ne laissent un agent que percevoir son environnement (« read-only actions ») et celles qui lui permettent d’agir sur cet environnement (« write actions »). Sur le risque du second type, elle est directe : « Write actions enable a system to do more », mais « the prospect of giving AI the ability to automatically alter our lives is frightening » &#8212; selon ses mots, « you shouldn’t allow an unreliable AI to initiate bank transfers. » Tout aussi franche sur la partie d’un agent la plus dure à bien faire :</p>
<blockquote><p>&#8220;If you’ve ever been in any planning meeting, you know that planning is hard.&#8221;</p></blockquote>
<p>Huyen ne mentionne MarsDawn nulle part dans cet essai et ne recommande aucun outil Markdown. <code>/reviewing-agent-plans/</code> cite déjà trois de ses phrases du même essai : le coût de sauter la surveillance avant qu’un plan ne tourne, l’agent qui croit avoir fini alors qu’il n’a pas fini, et, à l’étape 3 de sa checklist, sa ligne qu’un système face à une opération risquée « can ask for explicit human approval before executing ». Cette note ne répète pas ces citations ; si vous n’avez pas lu cette page, elle est liée ci-dessous.</p>

<h2>Notre lecture, pas celle de Huyen</h2>
<p>La distinction read-only / write de Huyen n’est pas écrite comme un conseil de relecture &#8212; c’est une façon de classer ce qu’un outil fait. Mais c’est un test simple et général pour repérer exactement le genre de ligne d’opération risquée que l’étape 3 de cette checklist vous demande déjà de ralentir : lire un fichier, lancer une recherche, lister un répertoire sont en lecture seule, et une étape read-only qui rate vous coûte une reprise ; supprimer des données, forcer un push, fusionner une branche, envoyer un e-mail, débiter une carte sont des write actions, et &#8212; comme elle le dit &#8212; une étape write qui rate est le genre effrayant, et au moment où vous lisez le rapport de l’agent, elle peut déjà avoir eu lieu. Son point que la planification est dure même pour des humains dans une pièce est un contrôle utile contre le fait d’attendre d’un plan plus de précision que le format ne peut porter : un plan qui se lit avec assurance n’est pas la même chose qu’un plan juste.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn ne peut pas distinguer une étape read-only d’une write dans un plan &#8212; c’est un jugement que le texte n’étiquette pas, et rien dans l’app ne lit pour le sens. Il n’a aucun modèle d’IA à l’intérieur : il ne signalera pas la ligne risquée pour vous, ne fera pas le contrôle « la planification est dure », ni ne notera le plan. Ce qu’il fait, c’est garder le fichier lisible pendant que vous portez ce jugement vous-même : l’onglet Plan (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) laisse balayer la forme d’un plan avant de le lire ligne à ligne, la source et la page rendue côte à côte (&#8984;2) pour qu’un diagramme des étapes ne reste pas coincé en Mermaid brut, et Édition &#9656; Copier la référence (&#8997;&#8984;C) transforme votre place en <code>plan.md:10</code>, prêt à coller comme retour dès que vous repérez une write action dans le mauvais ordre.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>La checklist complète en six étapes et cinq minutes tirée du même essai : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a></li>
  <li>Pourquoi la sortie d’un agent est en général difficile à lire : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a> (récupéré et cité le 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/lilian-weng-llm-agents'] = {
        "title": 'Le plan d’agent de Lilian Weng en 2023, et le fichier que chaque partie laisse · MarsDawn',
        "description": 'L’enquête très citée de Lilian Weng en 2023 décrit un agent LLM comme un cerveau plus planification, mémoire et usage d’outils. Ce que chaque partie tend à vous laisser à lire, et la limite qu’elle nomme dans les plans qui ne s’ajustent pas aux surprises.',
        "body": f"""
<section class="intro">
  <h1>Le plan d’agent de Lilian Weng en 2023, et le fichier que chaque partie laisse</h1>
</section>

<div class="summary"><p><strong>En juin 2023, alors chez OpenAI, Lilian Weng a publié sur son blog Lil’Log une longue enquête décrivant un agent piloté par LLM comme un cerveau (le modèle) plus trois composants : planification, mémoire et usage d’outils. C’est un cadre précoce et largement cité de ce dont un agent est fait, et candid sur les endroits où ce cadre casse encore.</strong></p></div>

<h2>Ce que le billet avance</h2>
<p>L’aperçu de Weng pose le cadre de tout le texte :</p>
<blockquote><p>&#8220;In a LLM-powered autonomous agent system, LLM functions as the agent&#8217;s brain, complemented by several key components: Planning ... Memory ... Tool use&#8221;.</p></blockquote>
<p>La planification, chez elle, couvre à la fois le découpage d’une tâche en sous-objectifs et la réflexion sur les actions passées pour améliorer les suivantes. La mémoire se partage entre court terme (le contexte que le modèle voit actuellement, qu’elle appelle in-context) et long terme (en général stocké hors du modèle, dans une base vectorielle interrogeable). L’usage d’outils laisse le modèle appeler tout ce qu’un jeu de poids figé ne peut fournir seul &#8212; informations actuelles, exécution de code, autres API. Vers la fin, dans une section « Challenges », elle nomme une limite clairement :</p>
<blockquote><p>&#8220;LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.&#8221;</p></blockquote>
<p>Ailleurs, dans une étude de cas sur l’agent de chimie ChemCrow, elle signale un problème plus étroit : une évaluation basée sur un LLM le notait à peu près égal à GPT-4, tandis que des experts humains jugeaient ChemCrow bien meilleur en exactitude. Sa conclusion porte sur l’auto-évaluation, pas spécifiquement sur son composant « reflection » :</p>
<blockquote><p>&#8220;The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.&#8221;</p></blockquote>
<p>Weng ne mentionne MarsDawn nulle part dans ce billet et ne recommande aucun outil Markdown.</p>

<h2>Notre lecture, pas celle de Weng</h2>
<p>Weng décrit l’architecture d’agent en 2023, pas la lecture de la sortie d’un agent &#8212; elle ne mentionne aucune personne qui vérifierait un fichier. Mais ses trois composants se projettent sur trois choses différentes que vous pouvez vous retrouver à lire. La planification tend à vous laisser un document avant l’exécution &#8212; le plan lui-même, parfois avec une « reflection » ou une auto-revue déjà pliée dedans. La mémoire est en général invisible, sauf si l’agent tient un fichier brouillon courant comme stockage long terme ; alors ce fichier mérite d’être ouvert pour lui-même, car il peut traîner une vieille hypothèse fausse à travers bien des étapes suivantes sans le dire. L’usage d’outils tend à vous laisser un rapport de ce qui a tourné et de ce qui est revenu &#8212; plus près d’un transcript que d’un plan.</p>
<p>Son point sur les plans qui ne s’ajustent pas aux erreurs inattendues est, lu de votre côté, une raison pour qu’un plan approuvé hier soit périmé aujourd’hui : si quelque chose que le plan n’avait pas prévu est arrivé entre-temps, l’agent peut continuer plutôt que de replanifier, et le rapport final peut décrire le succès du plan d’origine sans décrire le détour. C’est notre inférence, pas une affirmation d’elle &#8212; elle écrit sur la robustesse du modèle, pas sur ce qu’un lecteur devrait surveiller.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn n’a aucun modèle d’IA à l’intérieur, donc il ne peut pas vous dire si un plan a discrètement dérivé de ce qui s’est vraiment passé, et il ne distingue pas un fichier de planification d’un fichier de mémoire ou d’un rapport d’usage d’outils &#8212; c’est une lecture du contenu, qui vous appartient. Ce qu’il fait : l’onglet Plan (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) montre d’un coup d’œil la forme d’un long plan, la source et l’aperçu rendu côte à côte (&#8984;2) avec Mermaid et KaTeX dessinés, et si l’agent réécrit le fichier en cours de lecture, MarsDawn le recharge et garde votre place, tant que vous n’avez pas de modifications non enregistrées &#8212; utile précisément parce qu’un plan silencieusement révisé est exactement le mode de défaillance que sa section « Challenges » décrit du côté du modèle.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>Quels documents les différents patrons de conception d’agents tendent à vous rendre : <a href="/fr/agent-design-patterns/">Quatre patrons de conception d’agents et les documents que chacun vous tend</a></li>
  <li>La relecture en cinq minutes d’un plan avant qu’il ne tourne : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Lilian Weng, &#8220;LLM Powered Autonomous Agents,&#8221; Lil’Log, June 23, 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a> (récupéré et cité le 2026-09-26 ; elle était alors chez OpenAI, décrite ici seulement telle qu’elle était alors).</li>
</ul>
""",
    }


    pages['reading-notes/harrison-chase-what-is-an-agent'] = {
        "title": 'Le spectre de Harrison Chase\xa0: plus c’est agentic, plus vous voudrez regarder · MarsDawn',
        "description": 'La définition d’un agent de Harrison Chase en 2024 et son spectre de comportement agentic, et son plaidoyer pour l’observabilité à mesure qu’un système avance dessus — lu du côté de qui lit le fichier qu’il rend.',
        "body": f"""
<section class="intro">
  <h1>Le spectre de Harrison Chase : plus c’est agentic, plus vous voudrez regarder</h1>
</section>

<div class="summary"><p><strong>En juin 2024, Harrison Chase de LangChain a ouvert une nouvelle série avec une question trompeusement petite &#8212; « What is an agent ? » &#8212; et y a répondu par une définition technique et un spectre de comportement « agentic ». Plus un système occupe ce spectre, avance-t-il, plus il faut pouvoir voir à l’intérieur pendant qu’il tourne.</strong></p></div>

<h2>Ce que le billet avance</h2>
<p>La propre définition de Chase, offerte avec la réserve qu’elle est plus technique, et plus large, que l’idée que se font la plupart des gens d’un agent :</p>
<blockquote><p>&#8220;An agent is a system that uses an LLM to decide the control flow of an application.&#8221;</p></blockquote>
<p>Le control flow, c’est simplement quelle étape un programme lance ensuite. Il admet aussitôt que la définition est imparfaite &#8212; un système simple où un LLM route entre deux chemins compte comme agent selon sa définition, mais ne collerait pas à l’intuition de « agent » de la plupart des gens. Plutôt que de se battre sur l’étiquette, il reprend une suggestion d’Andrew Ng, dont il cite et crédite directement le tweet : « rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic. » Le commentaire de Chase : « I really agree with this viewpoint and I think Andrew expressed it nicely. » De là : un système est d’autant plus « agentic » qu’un LLM décide davantage de son comportement, d’un routeur fixe jusqu’à un agent pleinement autonome qui construit et mémorise ses propres outils. Son argument pratique suit de ce spectre &#8212; plus un système est agentic, plus certains types d’infrastructure comptent, l’observabilité en tête :</p>
<blockquote><p>&#8220;You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.&#8221;</p></blockquote>
<p>Il étend cela à l’intervention, pas seulement à l’observation : vous voudrez aussi pouvoir modifier l’état ou les instructions d’un agent en cours à un point donné, pour le ramener sur la voie s’il dérive. Chase ne mentionne MarsDawn nulle part dans ce billet et ne recommande aucun outil Markdown.</p>

<h2>Notre lecture, pas celle de Chase</h2>
<p>Chase écrit sur les outils pour qui construit des frameworks d’agents &#8212; LangGraph et LangSmith, nommément &#8212; pas sur une personne qui lit un document fini. Mais son spectre donne une façon utile de calibrer ce que vous allez lire avant de commencer : plus le système qui a produit un fichier est agentic, moins vous devez vous attendre à ce que ses étapes soient prévisibles à partir du seul prompt, et plus le fichier devant vous mérite d’être traité comme un enregistrement de ce qui s’est vraiment passé plutôt que de ce qui était censé se passer.
Son « observe what is going on inside » porte sur l’intérieur d’un système en cours &#8212; traces (un journal enregistré de tout ce que l’agent a fait pendant une exécution), étapes intermédiaires, appels d’outils &#8212; pas sur la lecture d’un plan Markdown après coup. Mais la raison sous-jacente qu’il donne, que les étapes exactes peuvent ne pas être connues à l’avance, s’applique tout autant au document qu’un agent vous tend une fois terminé : si les étapes n’étaient pas prévisibles en entrée, le rapport en sortie est le seul endroit restant pour les vérifier.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn n’observe pas l’intérieur d’un agent en cours &#8212; il n’a aucun modèle d’IA à l’intérieur et aucune connexion au framework qui a produit le fichier, donc il ne peut pas vous dire où sur le spectre de Chase un agent donné se situait. Il travaille sur le document qui atterrit ensuite : l’onglet Plan (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) pour la forme d’un long rapport, la source et l’aperçu rendu côte à côte (&#8984;2) pour les diagrammes et les maths, et le rechargement en direct qui garde votre place quand l’agent réécrit le fichier, tant que vous n’avez pas de modifications non enregistrées &#8212; la version au niveau fichier de regarder quelque chose qui bouge encore. Édition &#9656; Copier la référence (&#8997;&#8984;C) et Copier pour l’IA (&#8963;&#8997;&#8984;C) vous laissent montrer exactement où une étape a dérapé &#8212; l’équivalent documentaire de ramener un agent en cours sur la voie.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>Le traitement plus complet de la transparence et des checkpoints dans cette série : <a href="/fr/agent-transparency/">Anthropic dit que les agents doivent être transparents. Qui lit ce qu’ils exposent ?</a></li>
  <li>Le billet LangChain de 2026 à la même adresse, avec une définition presque identique : <a href="/fr/reading-notes/langchain-what-is-an-agent/">Le pipeline d’evals de Jess Ou, et l’étape qui reste encore la vôtre</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Harrison Chase, &#8220;What is an agent?,&#8221; LangChain, June 28, 2024, copie archivée : <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (récupéré et cité le 2026-09-26 via la Wayback Machine ; l’adresse d’origine montre maintenant un article 2026 de Jess Ou).</li>
</ul>
""",
    }


    pages['reading-notes/langchain-what-is-an-agent'] = {
        "title": 'Le pipeline d’evals de Jess Ou, et l’étape qui reste encore la vôtre · MarsDawn',
        "description": 'Le «\xa0What is an AI agent\xa0?\xa0» de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.',
        "body": f"""
<section class="intro">
  <h1>Le pipeline d’evals de Jess Ou, et l’étape qui reste encore la vôtre</h1>
</section>

<div class="summary"><p><strong>En juillet 2026, LangChain a publié un nouveau « What is an AI agent ? » à l’adresse où se trouvait le billet 2024 de Harrison Chase « What is an agent ? » &#8212; celui-ci écrit par Jess Ou, avec une définition presque mot pour mot la sienne. L’essentiel de son billet porte sur quelque chose que le sien ne couvrait pas : tout un pipeline pour évaluer les agents automatiquement. Son texte est candid sur les endroits où ce pipeline a encore besoin d’une personne — et où non.</strong></p></div>

<h2>Ce que le billet avance</h2>
<p>La définition d’Ou fait écho de près à celle de Chase :</p>
<blockquote><p>&#8220;An AI agent is a system that uses a large language model to decide the control flow of an application.&#8221;</p></blockquote>
<p>Le control flow, encore une fois, c’est simplement quelle étape tourne ensuite. De là elle décrit le Agent Development Lifecycle de LangChain &#8212; build, test, deploy, monitor &#8212; et une approche en couches pour vérifier le travail d’un agent sans qu’une personne lise chaque exécution : les evals en ligne échantillonnent les traces de production (journaux enregistrés d’exécutions réelles) pour les régressions, les evals hors ligne tournent contre des jeux de données curatés pour attraper un mauvais changement avant la mise en production, et « LLM-as-a-judge » note la sortie d’une exécution selon des critères qu’une personne a définis à l’avance, à une échelle que la relecture manuelle ne peut pas atteindre. Elle est directe sur la place qui reste à une personne dans ce pipeline :</p>
<blockquote><p>&#8220;For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.&#8221;</p></blockquote>
<p>Elle a aussi une phrase sur le jugement qui ne s’évapore pas à l’échelle, quel que soit le niveau du pipeline : « Do not outsource judgment you cannot evaluate. If you wouldn’t recognize a correct answer, neither will the agent. » <code>/reviewing-agent-plans/</code> s’appuie déjà sur exactement cette phrase &#8212; cette note ne répète pas cette discussion. Ou ne mentionne MarsDawn nulle part et ne recommande aucun outil Markdown. Elle ne nomme jamais Chase non plus ; ce qui relie les deux billets, c’est que LangChain a publié le sien en 2026 à l’adresse qu’occupait le sien de 2024, avec une définition presque identique &#8212; une observation que nous faisons, pas elle.</p>

<h2>Notre lecture, pas celle d’Ou</h2>
<p>La phrase human-in-the-loop d’Ou porte sur le filtrage d’actions précises avant qu’elles ne tournent &#8212; mettre en pause une write action pour approbation, la même idée que la distinction read-only / write de Chip Huyen pointe sous un autre angle &#8212; pas sur une personne qui lit un rapport fini après coup. Lu avec soin, l’essentiel de son pipeline est conçu pour retirer une personne de la vérification de routine, pas pour en ajouter une : les evals en ligne et hors ligne et le LLM-as-a-judge existent précisément pour qu’une équipe n’ait pas à relire manuellement chaque trace.
Ce n’est pas une critique du texte &#8212; c’est son but déclaré, et un but raisonnable à l’échelle de production. Mais cela signifie que la relecture que vous faites à la main &#8212; lire un plan ou un rapport qu’un agent vous tend directement &#8212; est exactement le genre de contrôle que son pipeline est bâti pour réduire, pas remplacer. Sa propre phrase sur le jugement pose un plancher sous cette réduction : partout où vous ne pouvez pas personnellement distinguer une bonne réponse d’une mauvaise, il vous faut encore le lire vous-même.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn n’est pas un pipeline d’evals et n’a aucun modèle d’IA à l’intérieur &#8212; il ne notera pas une trace, ne lancera pas de passe LLM-as-a-judge, ni ne décidera quelles actions sont assez sensibles pour être mises en pause. Il est bâti pour le moment que son pipeline confie encore à une personne : lire la chose directement. L’onglet Plan (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) liste les titres d’un long rapport, la source et l’aperçu rendu côte à côte (&#8984;2) avec Mermaid et KaTeX dessinés, et Édition &#9656; Copier la référence (&#8997;&#8984;C) avec Copier pour l’IA (&#8963;&#8997;&#8984;C) transforment un contrôle ponctuel en retour précis sur lequel l’agent peut agir.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>La checklist complète construite en partie sur sa phrase « outsource judgment » : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a></li>
  <li>Où cette même définition a commencé, en 2024 : <a href="/fr/reading-notes/harrison-chase-what-is-an-agent/">Le spectre de Harrison Chase : plus c’est agentic, plus vous voudrez regarder</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Jess Ou, &#8220;What is an AI agent?,&#8221; LangChain, July 31, 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a> (récupéré et cité le 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/andrew-ng-design-patterns'] = {
        "title": 'Andrew Ng classe ses propres patrons de conception selon leur prévisibilité · MarsDawn',
        "description": 'Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.',
        "body": f"""
<section class="intro">
  <h1>Andrew Ng classe ses propres patrons de conception selon leur prévisibilité</h1>
</section>

<div class="summary"><p><strong>Sur cinq lettres dans The Batch début 2024, Andrew Ng a décrit quatre patrons de conception agentic &#8212; réflexion, usage d’outils, planification et collaboration multi-agents &#8212; et, chose rare, a dit clairement à ses lecteurs lesquels il trouve plus fiables et lesquels il peines à prévoir.</strong></p></div>

<h2>Ce que les lettres avancent</h2>
<p><code>/agent-design-patterns/</code> couvre déjà ce qu’est chacun des quatre patrons, quels documents chacun tend à vous laisser lire (notre inférence), et le propre verdict de Ng sur la planification, cité de la Partie 4 : « while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do. » Cette note ajoute le même classement tiré des deux lettres que cette page laisse de côté : la Partie 3, écrite une semaine avant la Partie 4, où il énonce le classement à l’avance, et la Partie 5, où il l’étend au patron que la Partie 4 ne mentionne pas &#8212; la collaboration multi-agents. En introduisant l’usage d’outils, dans la Partie 3, il écrit :</p>
<blockquote><p>&#8220;In future letters, I&#8217;ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable &#8212; albeit very exciting &#8212; technologies.&#8221;</p></blockquote>
<p>Deux semaines plus tard, en clôturant la série avec la collaboration multi-agents, il confirme le même classement de l’autre côté :</p>
<blockquote><p>&#8220;Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.&#8221;</p></blockquote>
<p>Il dit cela sur la façon dont chaque patron améliore les résultats de ses applications, pas sur le soin avec lequel une personne devrait vérifier leur sortie &#8212; rien dans cette série n’appelle à une relecture humaine, et rien ne mentionne MarsDawn ni ne recommande d’outil Markdown.</p>

<h2>Notre lecture, pas celle de Ng</h2>
<p>Le classement de Ng porte sur la qualité et la prévisibilité de la sortie depuis le fauteuil du constructeur, mais il s’aligne, grosso modo, avec le degré de scrutiny que la trace papier de chaque patron mérite probablement depuis le vôtre. La réflexion et l’usage d’outils, les deux qu’il trouve plus fiables, tendent à vous rendre quelque chose qui décrit un travail déjà fait &#8212; un brouillon révisé, un rapport de ce qui a tourné &#8212; donc vérifier une affirmation contre la vraie sortie couvre en général le risque. La planification et la collaboration multi-agents, les deux qu’il peines à prévoir, tendent à vous rendre quelque chose d’écrit avant que le travail n’arrive, ou réparti sur plusieurs fichiers de plusieurs agents :
un plan qui attend un feu vert, ou une passation entre agents que l’exécution n’a pas encore testée. De son propre aveu, ce sont exactement les documents où l’écart entre ce qui est écrit et ce qui se passera vraiment est le plus large &#8212; le même point que <code>/reviewing-agent-plans/</code> tire de l’essai de Chip Huyen, dans sa section « Pourquoi s’en soucier avant que ça tourne » : attraper un problème avant que quoi que ce soit n’ait tourné est l’endroit le moins cher pour l’attraper.</p>

<h2>Où MarsDawn aide, et où non</h2>
<p>MarsDawn ne sait pas lequel des quatre patrons de Ng a produit un fichier donné, ne classe rien par prévisibilité, et n’a aucun modèle d’IA à l’intérieur &#8212; il ne fera pas la vérification que son classement suggère de faire. Il garde le fichier lisible pendant que vous le faites vous-même : l’onglet Plan (Présentation &#9656; Afficher la barre latérale, &#8963;&#8984;S) montre la forme d’un long plan, la source et l’aperçu rendu côte à côte (&#8984;2), et pour une passation multi-agents, ouvrir le dossier partagé avec Fichier &#9656; Ouvrir le dossier&#8230; (&#8679;&#8984;O) montre les nouveaux fichiers dans l’onglet Fichiers en environ une seconde à mesure que différents agents les écrivent, l’en-tête nommant la branche git ou le worktree pour que deux fichiers du même nom venant d’agents différents ne se confondent pas.</p>

<h2>Essayer</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fonctionne déjà :</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Il exporte le Markdown en PDF sans l’app.</p>
<p><a href="/fr/cli/">Ligne de commande</a> &#183; Avant d’acheter : <a href="/fr/limits/">Ce que MarsDawn ne fait pas</a></p>

<h2>Ensuite</h2>
<ul>
  <li>Ce que chaque patron tend à vous rendre, en entier : <a href="/fr/agent-design-patterns/">Quatre patrons de conception d’agents et les documents que chacun vous tend</a></li>
  <li>La relecture en cinq minutes d’un plan avant qu’il ne tourne : <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a></li>
  <li>Retour à la série : <a href="/fr/reading-notes/">Notes de lecture de la rédaction</a></li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 1,&#8221; The Batch, March 20, 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 3: Tool Use,&#8221; The Batch, April 3, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/</a> (récupéré et cité le 2026-09-26).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 4: Planning,&#8221; The Batch, April 10, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a> (citation reprise verbatim de <code>design/inbox/276-agent-blog-series.md</code>, déjà citée sur <code>/agent-design-patterns/</code>).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 5, Multi-Agent Collaboration,&#8221; The Batch, April 17, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/</a> (récupéré et cité le 2026-09-26).</li>
</ul>
""",
    }

    pages['privacy'] = {
        "title": 'Politique de confidentialité · MarsDawn',
        "description": 'MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.',
        "body": k.render_legal_body("privacy", "fr"),
    }
    pages['support'] = {
        "title": 'Assistance · MarsDawn',
        "description": 'De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.',
        "body": k.render_legal_body("support", "fr"),
    }
    tables = {
        'app_ui_languages': app_ui_languages,
        'home': home,
        'compare': {key: {'head': t['head'], 'rows': t['rows']} for key, t in compare_tables.items()},
        'exit_table_head': exit_table_head,
        'exit_remedy': exit_remedy,
        'theme_shots': {image: {'name': name, 'alt': alt} for image, (name, alt) in theme_shots.items()},
        'theme_gallery_note': theme_gallery_note,
        'skip_label': 'Aller au contenu',
        'toc_label': {'privacy': 'Sur cette page', 'support': 'Aller à une question'},
        'not_found': {'title': 'Page introuvable · MarsDawn', 'headline': 'Perdu parmi les étoiles.', 'body': 'Ce chemin ne figure sur aucune carte. Un voisin discret a montré la route du retour.', 'home': 'Retour à MarsDawn', 'alt': 'Un petit vaisseau dérive dans le ciel de l’aube martienne, tandis qu’un extraterrestre amical montre le bord lumineux de la planète.'},
        # Not in Grok's material (the window label and the Markdown twin's sentence): written for #162.
        'hero_window_label': 'Une fenêtre MarsDawn interactive\xa0: choisissez un thème et une disposition',
        'hero_window_markdown': {'template': 'La page montre une fenêtre MarsDawn interactive qui affiche un extrait du guide de bienvenue de l’app. Dans son menu de palette, vous choisissez une apparence ({looks}) et, pour le clair comme pour le sombre, l’un des quatre thèmes d’aperçu ({themes}). Sa barre d’outils propose trois dispositions ({layouts}).', 'sep': ', '},
        'loop': loop_copy,
        'templates': templates,
    }
    return {
        'ui': ui, 'store_chip': store_chip, 'schema_notes': schema_notes, 'example_plan': example_plan,
        'trait_link': trait_link, 'trait_nav_heading': trait_nav_heading, 'figure_list_label': figure_list_label,
        'figures': figures, 'pages': pages, 'tables': tables,
    }
