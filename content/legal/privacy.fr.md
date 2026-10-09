# Politique de confidentialité

Comment MarsDawn, l’éditeur Markdown pour macOS, traite vos informations.

Dernière mise à jour : 2026-09-28

> **L’app MarsDawn ne collecte aucune donnée vous concernant.** Il n’y a ni compte, ni publicité, ni suivi. Vos documents et vos réglages restent sur votre Mac.

## Le site web

L’app et ce site web sont deux choses distinctes. L’app ne collecte rien. Une visite ne peut être enregistrée qu’ici, sur marsdawn.southern-light.dev.

Ce site utilise **Google Analytics 4**, chargé via **Google Tag Manager**. Pour chaque visiteur, la mesure d’audience est d’abord refusée : le mode Consentement (Consent Mode) de Google n’envoie qu’un ping sans cookie, sans cookie de mesure et sans identifiant persistant, jusqu’à ce que vous choisissiez *Accepter* dans le bandeau. Si vous choisissez *Refuser*, ou si vous ne faites aucun choix, rien ne change. Choisir *Refuser* après avoir accepté désactive immédiatement la mesure d’audience et supprime les cookies ci-dessous. Vous pouvez modifier votre choix à tout moment avec le lien « Réglages des cookies » en pied de chaque page. Ce choix est enregistré uniquement dans le stockage local de votre navigateur, jamais dans un cookie de notre part.

Une fois que vous avez accepté, Google Analytics dépose ses propres cookies (`_ga` et `_ga_<measurement id>`) et enregistre :

- **Pages vues et référent.** La page consultée et, lorsque le navigateur l’envoie, l’adresse de provenance.
- **Localisation approximative, appareil et navigateur.** Une localisation grossière déduite de votre adresse IP (au plus au niveau de la ville), votre type d’appareil, votre système d’exploitation et votre navigateur. Rien de tout cela n’est assez précis pour vous identifier.
- **Clics sortants et profondeur de défilement.** Les mesures améliorées de Google Analytics enregistrent les clics qui quittent le site, comme le lien vers le Mac App Store, ainsi que la distance que vous faites défiler sur une page.
- **Adresses IP.** Google Analytics 4 ne journalise ni ne stocke les adresses IP.
- **Ce qui n’est pas enregistré.** Aucun compte, puisque le site n’en a pas. Aucun document, et rien de ce que vous saisissez. Aucune publicité intersites, et aucun profil de vous. Les requêtes de l’app pour les fichiers de thème sous `/themes/` sont ignorées et ne sont pas transmises. Le simulateur de thèmes et la galerie sur `/themes/new/` et `/themes/gallery/` s’exécutent entièrement dans votre navigateur et n’envoient aucune donnée de thème à Google Analytics non plus.
- **Conservation.** Google conserve ces données pendant 14 mois, puis les supprime.
- **Lieu de traitement.** Google Tag Manager et Google Analytics sont exploités par Google ; vos données peuvent être traitées aux États-Unis ainsi que dans d’autres pays où Google exerce ses activités.
- **L’hébergeur.** Cloudflare héberge le site et, comme tout hébergeur, voit votre adresse IP pendant qu’il répond à la requête. Ce journal appartient à l’hébergeur. Il ne s’agit pas de la mesure d’audience décrite ci-dessus.

## Ce qui reste sur votre Mac

- **Vos documents.** MarsDawn lit et écrit uniquement les fichiers et dossiers que vous ouvrez, enregistrez ou choisissez. L’app ne les envoie jamais nulle part.
- **Vos réglages.** L’apparence, le thème de l’aperçu, la disposition des fenêtres et la préférence pour les images sont stockés dans les préférences propres de l’app, sur votre Mac.
- **L’accès aux dossiers que vous autorisez.** Lorsque vous laissez MarsDawn afficher des images ou des fichiers de page provenant d’un dossier, ou que vous choisissez un dossier de notes, l’app conserve un signet macOS afin de pouvoir rouvrir ce dossier. Un dossier que vous ouvrez dans la barre latérale reste accessible en lecture et en écriture par MarsDawn jusqu’à ce que vous le supprimiez dans les Réglages, et pas seulement tant que sa fenêtre est ouverte. Vous pouvez supprimer des dossiers à tout moment dans MarsDawn › Réglages.

## Quand MarsDawn utilise Internet

MarsDawn fonctionne entièrement hors ligne. L’app ne se connecte à Internet **que si vous le choisissez**, pour un document qui fait référence au web ou pour la galerie de thèmes. Pour les documents :

- **Documents Markdown.** Les images web sont bloquées par défaut. Elles ne se chargent qu’après un clic sur *Charger les images* dans l’aperçu, ou si vous activez *Charger automatiquement les images distantes* dans les Réglages. Rien d’autre de ce à quoi un document Markdown fait référence n’est chargé depuis le web.
- **Documents HTML.** Un document HTML s’ouvre de façon statique : son code ne s’exécute pas et rien n’est chargé depuis le web. Si un document contient du code exécutable, vous pouvez choisir *Présentation › Exécuter ce document* pour ce document. Son propre code s’exécute alors jusqu’à ce que vous l’arrêtiez, que le document se recharge ou que vous fermiez la fenêtre. Ce choix n’est jamais mémorisé, et ce n’est pas un réglage. Pendant l’exécution, le document peut envoyer des données sur le réseau, et lire les images, feuilles de style, polices et médias de son dossier et des dossiers qu’il contient. Le code téléchargé depuis le web ne s’exécute jamais.

MarsDawn charge le contenu web uniquement en https. Une adresse en http simple n’est jamais chargée, quel que soit le réglage, et MarsDawn ne la réécrit pas en https. Dans un document Markdown, l’aperçu affiche un espace réservé à sa place.

Lorsqu’un contenu web se charge, votre Mac le demande directement aux serveurs qui l’hébergent. Comme pour toute requête web, ces serveurs voient alors votre adresse IP et ce qui a été demandé. Le développeur de MarsDawn ne reçoit aucune de ces informations.

Les liens sur lesquels vous cliquez dans l’aperçu s’ouvrent dans votre navigateur web par défaut, selon les pratiques de confidentialité de ce navigateur. L’audio et la vidéo ne se lancent jamais d’eux-mêmes.

<!-- MACHINE DRAFT (needs-i18n): translated from the English paragraph by Claude; native review required before this ships. -->

Si vous ouvrez *Réglages › Apparence › Obtenir plus de thèmes…*, choisissez *Rechercher des mises à jour de thèmes* ou installez ou mettez à jour un thème, MarsDawn télécharge la liste des thèmes, les aperçus et les fichiers de thème depuis marsdawn.southern-light.dev. Les thèmes ne se mettent à jour automatiquement que pendant ces téléchargements, jamais en arrière-plan. La requête ne contient ni compte, ni identifiant, ni cookie, ni donnée de document ; comme pour toute requête web, notre hébergeur Cloudflare voit votre adresse IP et les fichiers demandés. *Signaler le thème…* n’envoie aucune requête depuis l’app : cette action ouvre seulement un lien GitHub ou e-mail dans votre navigateur ou votre app de messagerie.

## Siri, Raccourcis et Spotlight

MarsDawn propose des actions pour Siri, l’app Raccourcis et Spotlight, comme créer un document ou ajouter une note. Lorsque vous les utilisez, le texte que vous fournissez est transmis à MarsDawn sur votre Mac et enregistré uniquement à l’endroit indiqué par l’action (un nouveau document, ou le fichier `Inbox.md` du dossier de notes que vous avez choisi). Ce que vous dictez à Siri est traité par Apple conformément à la [politique de confidentialité d’Apple](https://www.apple.com/legal/privacy/).

## Export et impression

L’export PDF et l’impression se font sur votre Mac. Le PDF est enregistré à l’endroit que vous choisissez. L’impression passe par macOS vers l’imprimante que vous sélectionnez.

## L’outil en ligne de commande marsdawn

L’outil en ligne de commande facultatif `marsdawn`, distribué séparément, s’exécute lui aussi entièrement sur votre Mac. Il lit le fichier Markdown que vous indiquez et écrit le PDF que vous demandez. Il ne charge les images web que si vous passez `--allow-remote-images`.

## Enfants

L’app MarsDawn ne collecte de données auprès de personne, y compris les enfants. Une visite enregistrée sur le site web n’est pas un compte, et elle ne sert pas à identifier qui que ce soit.

## Achats

MarsDawn est vendu sur le Mac App Store. Apple traite l’achat selon ses propres conditions, et le développeur ne reçoit jamais vos informations de paiement.

## Modifications de cette politique

Si MarsDawn venait à traiter les données différemment, cette page serait mise à jour avant la sortie de la version concernée, et la date en haut de page changerait.

## Contact

Questions relatives à la confidentialité : [support@southern-light.dev](mailto:support@southern-light.dev)
