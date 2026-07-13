# Template: Tool-Freigabe-Checkliste (Phase 2/3)

**Einsatz:** Vor jeder Tool-Einführung — auch für „nur mal testen" mit echten Daten. Abhakbar in 30–60 Minuten mit IT; die strategische Bewertung (kaufen/bauen/abschalten) läuft davor über das [Buy/Build/Deprecate-Framework](../cases/natura-foods/buy-build-deprecate.md). Ein Tool ohne vollständige Checkliste bekommt keinen Eintrag im Register und keine Freigabe.

---

## Tool: [Name] · Anbieter: [ ] · Geprüft von: [ ] am: [ ]

### 1. Bedarf (Programmleitung)

- [ ] Use-Case-Bezug: für welchen Piloten/welche Welle? ([Canvas](use-case-canvas.md) verlinken)
- [ ] Überschneidung geprüft: ersetzt/doppelt es ein Tool aus dem Register? Wenn Doppelung: was wird abgeschaltet?
- [ ] Bestehende Verträge geprüft: geht es mit dem, was wir schon bezahlen (M365, Helpdesk-Add-on …)?

### 2. Datenschutz & Recht (Datenschutz + ggf. BR)

- [ ] **AVV/DPA** verfügbar und unterschreibbar (Art. 28 DSGVO)
- [ ] **Verarbeitungsort:** EU-Region wählbar? Wenn Drittland: Transfermechanismus (SCCs) vorhanden?
- [ ] **Trainingsnutzung:** Anbieter trainiert NICHT auf unseren Eingaben (vertraglich, nicht nur Toggle) — oder Datenklassen entsprechend beschränkt
- [ ] **Datenklassen** festgelegt: welche der [4 Klassen](../governance/ai-richtlinie.md#2-datenklassifizierung--was-darf-in-welches-tool) dürfen rein?
- [ ] **Löschung:** Aufbewahrungsfristen und Löschweg geklärt (auch bei Vertragsende)
- [ ] Bei Beschäftigtenbezug: BR informiert / Mitbestimmung geklärt; keine Leistungskontroll-Funktionen aktiviert

### 3. Sicherheit (IT)

- [ ] **SSO** über unser Workspace-Login (keine Privat-Accounts, keine geteilten Logins)
- [ ] **Rollen/Rechte:** Least Privilege abbildbar; Admin-Zugänge benannt
- [ ] **Audit-Log** vorhanden und exportierbar
- [ ] API-Keys/Secrets im Secret-Store, nicht in Prompts/Dokumenten
- [ ] Offboarding: Zugang wird im Leaver-Prozess mit entzogen

### 4. Betrieb & Wirtschaftlichkeit (AI-Office)

- [ ] **Kostenmodell** verstanden (pro Seat/Nutzung/Token) + Deckel oder Alarm eingerichtet
- [ ] **TCO Jahr 1** gerechnet: Lizenz + Integration + Enablement + Pflege
- [ ] **Exit-Pfad:** Datenexport möglich? Wechselaufwand grob? (kein Exit-Pfad → keine Freigabe)
- [ ] **Eval-Haken:** Wie messen wir, ob es wirkt? (Metrik aus dem Pilot-Charter übernehmen)
- [ ] **Next-Review-Datum** gesetzt (Standard: nächstes Quartals-Landscape-Review)

### 5. Freigabe

| Rolle | Name | Datum | Ergebnis |
|---|---|---|---|
| Programmleitung | | | ☐ frei ☐ mit Auflagen ☐ abgelehnt |
| IT/Security | | | ☐ frei ☐ mit Auflagen ☐ abgelehnt |
| Datenschutz | | | ☐ frei ☐ mit Auflagen ☐ abgelehnt |

Auflagen: …

→ Bei Freigabe: Eintrag ins Tool-Register (Kosten, Adoption-Messung, DPA-Status, Next Review, Exit-Pfad) und Aufnahme in die Stufe-1-Schulungsunterlagen.
