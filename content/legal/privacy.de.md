# Datenschutzrichtlinie

Wie MarsDawn, der Markdown-Editor für macOS, mit deinen Daten umgeht.

Zuletzt aktualisiert am 2026-09-28

> **Die App MarsDawn erhebt keinerlei Daten über dich.** Es gibt kein Konto, keine Werbung und kein Tracking. Deine Dokumente und Einstellungen bleiben auf deinem Mac.

## Die Website

Die App und diese Website sind zwei verschiedene Dinge. Die App erhebt nichts. Ein Besuch kann nur hier erfasst werden, auf marsdawn.southern-light.dev.

Diese Website verwendet **Google Analytics 4**, geladen über den **Google Tag Manager**. Für alle Besucher ist die Analyse zunächst abgelehnt: Der Einwilligungsmodus (Consent Mode) von Google sendet nur einen cookielosen Ping, ohne Analyse-Cookie und ohne dauerhafte Kennung, bis du im Banner *Akzeptieren* wählst. Wählst du *Ablehnen* oder triffst du gar keine Wahl, bleibt es dabei. Wählst du *Ablehnen*, nachdem du zuvor *Akzeptieren* gewählt hast, wird die Analyse sofort wieder abgeschaltet, und die unten genannten Cookies werden entfernt. Du kannst deine Wahl jederzeit über den Link „Cookie-Einstellungen“ in der Fußzeile jeder Seite ändern. Die Wahl selbst wird nur im lokalen Speicher deines Browsers abgelegt, nie in einem Cookie von uns.

Sobald du zustimmst, setzt Google Analytics eigene Cookies (`_ga` und `_ga_<measurement id>`) und erfasst:

- **Seitenaufrufe und Referrer.** Welche Seite aufgerufen wurde, und die verweisende Adresse, wenn der Browser sie mitsendet.
- **Ungefährer Standort, Gerät und Browser.** Ein grober Standort, abgeleitet aus deiner IP-Adresse (höchstens auf Stadtebene), dein Gerätetyp, dein Betriebssystem und dein Browser. Nichts davon ist genau genug, um dich zu identifizieren.
- **Klicks nach außen und Scrolltiefe.** Die erweiterten Messfunktionen von Google Analytics erfassen Klicks, mit denen du die Website verlässt, etwa auf den Link zum Mac App Store, und wie weit du auf einer Seite nach unten scrollst.
- **IP-Adressen.** Google Analytics 4 protokolliert oder speichert keine IP-Adressen.
- **Was nicht erfasst wird.** Kein Konto, denn die Website hat keine. Kein Dokument und nichts, was du eingibst. Keine websiteübergreifende Werbung und kein Profil von dir. Anfragen der App nach Themadateien unter `/themes/` werden ausgelassen und nicht weitergegeben. Der Themensimulator und die Galerie unter `/themes/new/` und `/themes/gallery/` laufen vollständig in deinem Browser und senden ebenfalls keine Themendaten an Google Analytics.
- **Aufbewahrung.** Google bewahrt diese Daten 14 Monate lang auf und löscht sie dann.
- **Wo die Daten verarbeitet werden.** Google Tag Manager und Google Analytics werden von Google betrieben. Deine Daten können in den Vereinigten Staaten sowie in anderen Ländern verarbeitet werden, in denen Google tätig ist.
- **Der Hoster.** Cloudflare hostet die Website und sieht, wie jeder Hoster, deine IP-Adresse, während die Anfrage beantwortet wird. Dieses Protokoll gehört dem Hoster. Es ist nicht die oben beschriebene Analyse.

## Was auf deinem Mac bleibt

- **Deine Dokumente.** MarsDawn liest und schreibt nur die Dateien und Ordner, die du öffnest, sicherst oder auswählst. Die App lädt sie nirgendwohin hoch.
- **Deine Einstellungen.** Erscheinungsbild, Vorschau-Thema, Fensterlayout und die Einstellung für Bilder werden in den eigenen Einstellungen der App auf deinem Mac gespeichert.
- **Ordnerzugriff, den du erlaubst.** Wenn du MarsDawn Bilder oder Seitendateien aus einem Ordner anzeigen lässt oder einen Notizordner auswählst, behält die App ein macOS-Lesezeichen, damit sie diesen Ordner wieder öffnen kann. Ein Ordner, den du in der Seitenleiste öffnest, bleibt für MarsDawn lesbar und beschreibbar, bis du ihn in den Einstellungen entfernst, nicht nur, solange sein Fenster offen ist. Du kannst Ordner jederzeit unter „MarsDawn“ › „Einstellungen“ entfernen.

## Wann MarsDawn das Internet nutzt

MarsDawn funktioniert vollständig offline. Es verbindet sich nur dann mit dem Internet, **wenn du dich dafür entscheidest**, und zwar für ein Dokument, das auf das Web verweist, oder für die Themengalerie. Für Dokumente gilt:

- **Markdown-Dokumente.** Bilder aus dem Web sind standardmäßig blockiert. Sie werden erst geladen, wenn du in der Vorschau auf *Bilder laden* klickst oder in den Einstellungen *Bilder aus dem Web automatisch laden* aktivierst. Sonst wird nichts, worauf ein Markdown-Dokument verweist, aus dem Web geladen.
- **HTML-Dokumente.** Ein HTML-Dokument öffnet sich statisch: Sein Code läuft nicht, und nichts wird aus dem Web geladen. Enthält ein Dokument Code, der laufen könnte, kannst du für dieses Dokument *Darstellung › Dieses Dokument ausführen* wählen. Sein eigener Code läuft dann, bis du ihn stoppst, das Dokument neu geladen wird oder du das Fenster schließt. Diese Wahl wird nie gespeichert, und sie ist keine Einstellung. Während der Code läuft, kann das Dokument Daten über das Netzwerk senden sowie Bilder, Stylesheets, Schriften und Medien in seinem Ordner und den darin enthaltenen Ordnern lesen. Code, der aus dem Web geladen wird, läuft nie.

MarsDawn lädt Webinhalte nur über https. Eine einfache http-Adresse wird nie geladen, bei keiner Einstellung, und MarsDawn schreibt sie auch nicht in https um. In einem Markdown-Dokument zeigt die Vorschau an ihrer Stelle einen Platzhalter.

Wenn Webinhalte geladen werden, fordert dein Mac sie direkt bei den Servern an, die sie bereitstellen. Wie bei jeder Webanfrage sehen diese Server dadurch deine IP-Adresse und was angefordert wurde. Der Entwickler von MarsDawn erhält keine dieser Informationen.

Links, auf die du in der Vorschau klickst, öffnen sich in deinem Standard-Webbrowser, nach dessen eigenen Datenschutzpraktiken. Audio und Video spielen nie von selbst ab.


Wenn du *Einstellungen › Erscheinungsbild › Weitere Themes laden …* öffnest, *Nach Theme-Updates suchen* wählst oder ein Theme installierst oder aktualisierst, lädt MarsDawn die Theme-Liste, Vorschauen und Theme-Dateien von marsdawn.southern-light.dev herunter. Themes werden nur bei diesen Downloads automatisch aktualisiert, nie im Hintergrund. Die Anfrage enthält kein Konto, keine Kennung, kein Cookie und keine Dokumentdaten; wie bei jeder Webanfrage sieht unser Hoster Cloudflare deine IP-Adresse und welche Dateien angefordert wurden. *Theme melden…* sendet keine Anfrage aus der App: Der Befehl öffnet nur einen GitHub- oder E-Mail-Link in deinem Browser oder deiner Mail-App.

## Siri, Kurzbefehle und Spotlight

MarsDawn bietet Aktionen für Siri, die App „Kurzbefehle“ und Spotlight, etwa zum Erstellen eines Dokuments oder zum Hinzufügen einer Notiz. Wenn du sie verwendest, wird der Text, den du angibst, an MarsDawn auf deinem Mac übergeben und nur dort gesichert, wo die Aktion es angibt (ein neues Dokument oder die Datei `Inbox.md` in dem von dir gewählten Notizordner). Sprache, die du Siri diktierst, verarbeitet Apple gemäß der [Datenschutzrichtlinie von Apple](https://www.apple.com/legal/privacy/).

## Exportieren und Drucken

PDF-Export und Drucken finden auf deinem Mac statt. Das PDF wird dort gesichert, wo du es festlegst. Gedruckt wird über macOS auf dem Drucker, den du auswählst.

## Das Befehlszeilenprogramm marsdawn

Das optionale Befehlszeilenprogramm `marsdawn`, das separat vertrieben wird, läuft ebenfalls vollständig auf deinem Mac. Es liest die Markdown-Datei, die du angibst, und schreibt das PDF, das du anforderst. Bilder aus dem Web lädt es nur, wenn du `--allow-remote-images` übergibst.

## Kinder

Die App MarsDawn erhebt von niemandem Daten, auch nicht von Kindern. Ein auf der Website erfasster Besuch ist kein Konto und wird nicht verwendet, um jemanden zu identifizieren.

## Käufe

MarsDawn wird über den Mac App Store verkauft. Apple wickelt den Kauf nach eigenen Bedingungen ab, und der Entwickler erhält nie deine Zahlungsdaten.

## Änderungen dieser Richtlinie

Falls MarsDawn jemals beginnt, Daten anders zu verarbeiten, wird diese Seite aktualisiert, bevor diese Version erscheint, und das Datum oben ändert sich.

## Kontakt

Fragen zum Datenschutz: [support@southern-light.dev](mailto:support@southern-light.dev)
