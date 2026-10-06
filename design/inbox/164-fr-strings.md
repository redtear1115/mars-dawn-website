# #164 Français (fr) — tranche 1: terms, site chrome, 404

Source: English read programmatically from `scripts/build_pages.py` / `scripts/templates_pages.py` / `public/404.html` on `main` @ `6fe8435`; app terms from `MarsDawn/Resources/Localizable.xcstrings` on app `release/1.1.0`. Legal pages are in the sibling files `164-privacy.fr.md` and `164-support.fr.md`.

## 1. Terms checked against the app (release/1.1.0)

| en (app) | fr (app) | xcstrings key |
|---|---|---|
| Window | Fenêtre | `Window` |
| Show Sidebar | Afficher la barre latérale | `Show Sidebar` |
| Preview | Aperçu | `Preview` |
| Editor | Éditeur | `Editor` |
| Source Only | Source uniquement | `Source Only` |
| Preview Only | Aperçu uniquement | `Preview Only` |
| Split | Partagé | `Split` |
| Layout | Disposition | `Layout` |
| Theme | Thème | `Theme` |
| Preview Theme | Thème de l’aperçu | `Preview Theme` |
| Appearance | Apparence | `Appearance` |
| Settings | Réglages | `Settings` |
| Export as PDF… | Exporter au format PDF… | `Export as PDF…` |
| Print… | Imprimer… | `Print…` |
| Save As… | Enregistrer sous… | `Save As…` |
| File | Fichier | `File` |
| View | Présentation | `View` |
| Open Folder… | Ouvrir un dossier… | `Open Folder…` |
| Folder Access | Accès aux dossiers | `Folder Access` |
| Grant Folder Access… | Autoriser l’accès au dossier… | `Grant Folder Access…` |
| Load Images | Charger les images | `Load Images` |
| Load remote images automatically | Charger automatiquement les images distantes | `Load remote images automatically` |
| Notes Folder | Dossier de notes | `Notes Folder` |
| Run This Document | Exécuter ce document | `Run This Document` |
| Template | Modèle | `Template` |
| Copy for AI | Copier pour l’IA | `Copy for AI` |
| About %@ | À propos de %@ | `About %@` |
| Start 14-day trial | Commencer l’essai de 14 jours | `paywall.button.startTrial` |
| Your free trial has ended | Votre essai gratuit est terminé | `paywall.ended.headline` |
| One-time unlock… | Déverrouillage unique… | `paywall.button.unlock` |
| Unlock MarsDawn… | Déverrouiller MarsDawn… | `paywall.menu.unlock` |
| MarsDawn is unlocked. Thank you. | MarsDawn est déverrouillé. Merci. | `paywall.settings.unlocked` |
| Restore Purchases | Restaurer les achats | `paywall.button.restore` |
| Quick Look | Coup d’œil | in `paywall.ended.body` |
| Shortcuts (app) | Raccourcis | in `Notes you add with Siri or Shortcuts go ` |
| trial (noun) | essai | in `paywall.unconfirmed.trialNote` |
| subscription | abonnement | in `paywall.unconfirmed.trialNote` |

## 2. Site chrome (`UI`, `STORE_CHIP`, `TRAIT_LINK`, …)

| key | en | fr |
|---|---|---|
| `home` | MarsDawn | MarsDawn |
| `privacy` | Privacy Policy | Politique de confidentialité |
| `support` | Support | Assistance |
| `cli` | Command Line | Ligne de commande |
| `agents` | marsdawn for agents | marsdawn pour les agents |
| `using_cli` | Using the CLI | Utiliser la CLI |
| `markdown-to-pdf` | Markdown to PDF | Markdown vers PDF |
| `skill` | Agent skill | Skill pour agents |
| `view-markdown-on-mac` | View Markdown on a Mac | Afficher du Markdown sur Mac |
| `vs-macmd-viewer` | MacMD Viewer vs. MarsDawn | MacMD Viewer vs MarsDawn |
| `updated` | Last updated {UPDATED} | Dernière mise à jour : {UPDATED} |
| `tagline` | Read what your agent wrote. | Lisez ce que votre agent a écrit. |
| `slogan` | A new dawn for Markdown. | Une nouvelle aube pour Markdown. |
| `footer_store` | MarsDawn is on the <a href="{LISTING_URL}">Mac App Store</a>. | MarsDawn est disponible sur le <a href="{LISTING_URL}">Mac App Store</a>. |
| `footer_nav` | Site | Site |
| `more` | More | Plus |
| `yours` | Your writing stays on your Mac | Vos textes restent sur votre Mac |
| `pay-once` | Try free, pay once | Essai gratuit, achat unique |
| `pdf` | PDF export | Export PDF |
| `native` | A Mac app | Une app Mac |
| `limits` | What MarsDawn doesn't do | Ce que MarsDawn ne fait pas |
| `mcp` | MCP server | Serveur MCP |
| `token-efficient-review` | Token-efficient review | Relire en économisant les tokens |
| `vs-markdown-preview-tools` | Viewing Markdown elsewhere vs. MarsDawn | Afficher du Markdown ailleurs vs MarsDawn |
| `themes` | Preview themes and PDF export | Thèmes de l’aperçu et export PDF |
| `sharing-exported-pdfs` | Sharing exported PDFs | Partager les PDF exportés |
| `reviewing-ai-output` | Why AI output still needs a human reader | Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain |
| `reading-agent-output` | Reading what your agent hands back | Lire ce que votre agent vous rend |
| `agent-transparency` | Agent transparency | Transparence des agents |
| `reviewing-agent-plans` | Reviewing an agent plan | Relire le plan d’un agent |
| `agent-design-patterns` | Agent design patterns | Patrons de conception d’agents |
| `changelog` | Changelog | Historique des versions |
| `consent_text` | This site uses analytics cookies to see how visitors use it. They stay off unless you accept. | Ce site utilise des cookies de mesure d’audience pour voir comment les visiteurs l’utilisent. Ils restent désactivés tant que vous n’acceptez pas. |
| `consent_accept` | Accept | Accepter |
| `consent_decline` | Decline | Refuser |
| `consent_aria` | Cookie consent | Consentement aux cookies |
| `cookie_settings` | Cookie settings | Réglages des cookies |
| `view_markdown_source` | View the Markdown source | Voir la source Markdown |
| `templates` | Templates | Modèles |
| `templates-spec` | Spec template | Modèle de spécification |
| `templates-flowchart` | Flowchart template | Modèle de diagramme de flux |
| `templates-meeting-notes` | Meeting notes template | Modèle de notes de réunion |
| `STORE_CHIP` | On the Mac App Store | Sur le Mac App Store |
| `TRAIT_LINK.yours` title | Your writing stays on your Mac | Vos textes restent sur votre Mac |
| `TRAIT_LINK.yours` line | No account, no sync, no cloud. | Pas de compte, pas de synchronisation, pas de cloud. |
| `TRAIT_LINK.pay-once` title | Try free, pay once | Essai gratuit, achat unique |
| `TRAIT_LINK.pay-once` line | Free for 14 days, then USD 4.99 once. No subscription. | Gratuit pendant 14 jours, puis 4,99 USD une seule fois. Sans abonnement. |
| `TRAIT_LINK.pdf` title | PDF export | Export PDF |
| `TRAIT_LINK.pdf` line | Diagrams, highlighted code, careful page breaks. | Diagrammes, code coloré, sauts de page soignés. |
| `TRAIT_LINK.native` title | A Mac app | Une app Mac |
| `TRAIT_LINK.native` line | Native windows, tabs, autosave, Quick Look. | Fenêtres et onglets natifs, enregistrement automatique, Coup d’œil. |
| `TRAIT_LINK.limits` title | What MarsDawn doesn't do | Ce que MarsDawn ne fait pas |
| `TRAIT_LINK.limits` line | Know before you buy. | À savoir avant d’acheter. |
| `TRAIT_NAV_HEADING` | What to expect from MarsDawn | Ce que vous pouvez attendre de MarsDawn |
| `FIGURE_LIST_LABEL` | In this screenshot | Sur cette capture d’écran |
| `SKIP_LABEL` | Skip to content | Aller au contenu |
| `TOC_LABEL.privacy` | On this page | Sur cette page |
| `TOC_LABEL.support` | Jump to a question | Aller à une question |
| `LOCALES.label` | English | Français |
| `html_lang` / `OG_LOCALE` | en / en_US | fr / fr_FR |

## 3. 404 page (`public/404.html`)

| element | en | fr |
|---|---|---|
| title | Page not found · MarsDawn | Page introuvable · MarsDawn |
| h1 | Lost among the stars. | Perdu parmi les étoiles. |
| body | This path isn’t on the map. A quiet neighbor pointed the way home. | Ce chemin ne figure sur aucune carte. Un voisin discret a montré la route du retour. |
| back | Back to MarsDawn | Retour à MarsDawn |
| alt | A small craft drifts in a Martian dawn sky while a friendly alien points toward the planet’s bright limb. | Un petit vaisseau dérive dans le ciel de l’aube martienne, tandis qu’un extraterrestre amical montre le bord lumineux de la planète. |
| aria_language | Language | Langue |
| aria_site | Site | Site |

## 4. Paste-ready for `copy_fr.py` (same shape as `copy_ja.py`)

```python
    ui = {'home': 'MarsDawn', 'privacy': 'Politique de confidentialité', 'support': 'Assistance', 'cli': 'Ligne de commande', 'agents': 'marsdawn pour les agents', 'using_cli': 'Utiliser la CLI', 'markdown-to-pdf': 'Markdown vers PDF', 'skill': 'Skill pour agents', 'view-markdown-on-mac': 'Afficher du Markdown sur Mac', 'vs-macmd-viewer': 'MacMD Viewer vs MarsDawn', 'updated': f'Dernière mise à jour\xa0: {k.UPDATED}', 'tagline': 'Lisez ce que votre agent a écrit.', 'slogan': 'Une nouvelle aube pour Markdown.', 'footer_store': f'MarsDawn est disponible sur le <a href="{k.LISTING_URL}">Mac App Store</a>.', 'footer_nav': 'Site', 'more': 'Plus', 'yours': 'Vos textes restent sur votre Mac', 'pay-once': 'Essai gratuit, achat unique', 'pdf': 'Export PDF', 'native': 'Une app Mac', 'limits': 'Ce que MarsDawn ne fait pas', 'mcp': 'Serveur MCP', 'token-efficient-review': 'Relire en économisant les tokens', 'vs-markdown-preview-tools': 'Afficher du Markdown ailleurs vs MarsDawn', 'themes': 'Thèmes de l’aperçu et export PDF', 'sharing-exported-pdfs': 'Partager les PDF exportés', 'reviewing-ai-output': 'Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain', 'reading-agent-output': 'Lire ce que votre agent vous rend', 'agent-transparency': 'Transparence des agents', 'reviewing-agent-plans': 'Relire le plan d’un agent', 'agent-design-patterns': 'Patrons de conception d’agents', 'changelog': 'Historique des versions', 'consent_text': 'Ce site utilise des cookies de mesure d’audience pour voir comment les visiteurs l’utilisent. Ils restent désactivés tant que vous n’acceptez pas.', 'consent_accept': 'Accepter', 'consent_decline': 'Refuser', 'consent_aria': 'Consentement aux cookies', 'cookie_settings': 'Réglages des cookies', 'view_markdown_source': 'Voir la source Markdown'}
    store_chip = 'Sur le Mac App Store'
    trait_link = {'yours': ['Vos textes restent sur votre Mac', 'Pas de compte, pas de synchronisation, pas de cloud.'], 'pay-once': ['Essai gratuit, achat unique', 'Gratuit pendant 14 jours, puis 4,99 USD une seule fois. Sans abonnement.'], 'pdf': ['Export PDF', 'Diagrammes, code coloré, sauts de page soignés.'], 'native': ['Une app Mac', 'Fenêtres et onglets natifs, enregistrement automatique, Coup d’œil.'], 'limits': ['Ce que MarsDawn ne fait pas', 'À savoir avant d’acheter.']}
    trait_nav_heading = 'Ce que vous pouvez attendre de MarsDawn'
    figure_list_label = 'Sur cette capture d’écran'
    # templates_pages.py UI entries
    templates_ui = {'templates': 'Modèles', 'templates-spec': 'Modèle de spécification', 'templates-flowchart': 'Modèle de diagramme de flux', 'templates-meeting-notes': 'Modèle de notes de réunion'}
```

Co-authored-by: Grok <grok@southern-light.dev>
