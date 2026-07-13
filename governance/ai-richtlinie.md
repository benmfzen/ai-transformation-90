# AI-Richtlinie NORDWERK GmbH (Muster)

**Prinzip: Leitplanken statt Verbote.** Diese Richtlinie legalisiert und kanalisiert KI-Nutzung, statt sie in den Untergrund zu treiben. Sie wird in Phase 3 mit echten Pilot-Erfahrungen finalisiert und mit Betriebsrat und Datenschutz verabschiedet — nicht abstrakt am Programmstart.

> Muster-Dokument im Rahmen des Showcase — vor realem Einsatz juristisch prüfen lassen.

## 1. Grundsätze

1. **KI-Nutzung ist erwünscht** — mit freigegebenen Tools, innerhalb dieser Leitplanken.
2. **Der Mensch verantwortet das Ergebnis.** Jede KI-Ausgabe wird vor Verwendung fachlich geprüft. „Die KI hat gesagt" ist keine Begründung.
3. **Transparenz statt Schatten-Nutzung.** Wer ein neues Tool oder einen neuen Anwendungsfall will, meldet ihn ans AI-Office — Freigabe-Antwort binnen 5 Arbeitstagen (sonst wandern die Leute zurück in den Schatten).

## 2. Datenklassifizierung — was darf in welches Tool?

| Datenklasse | Beispiele | Freigegebene Unternehmens-Tools | Öffentliche/private KI-Tools |
|---|---|---|---|
| Öffentlich | Website-Texte, Broschüren | ✅ | ✅ |
| Intern | Prozessbeschreibungen, interne Doku | ✅ | ❌ |
| Vertraulich | Preise, Kalkulationen, Konstruktionsdaten | ✅ nur mit Freigabe je Use Case | ❌ |
| Personenbezogen | Kunden-, Bewerber-, Mitarbeiterdaten | ✅ nur mit DSGVO-Kurzcheck | ❌ |

Faustregel für alle: **Würde ich es einem externen Dienstleister ohne Vertrag mailen? Nein → gehört es nicht in ein nicht freigegebenes Tool.**

## 3. Rote Linien (nicht verhandelbar)

- ❌ **Keine Leistungs- oder Verhaltenskontrolle** einzelner Beschäftigter durch KI. Pilot-Metriken werden ausschließlich auf Team-/Prozessebene gemessen. *(Zusage an den Betriebsrat, Grundlage der Zusammenarbeit.)*
- ❌ **Kein KI-Screening oder -Ranking von Bewerbern oder Beschäftigten** — EU-AI-Act-Hochrisikobereich (Anhang III: Beschäftigung). Entwürfe für Stellenanzeigen und Korrespondenz sind ok; Bewertung von Menschen nicht.
- ❌ **Keine automatisierten Entscheidungen ohne menschliche Prüfung** bei Rechtsfolgen für Personen (Art. 22 DSGVO).
- ❌ **Keine Eingabe von Geschäftsgeheimnissen** in nicht freigegebene Tools.

## 4. EU AI Act — was NORDWERK konkret betrifft

| Risikoklasse | Bei uns | Konsequenz |
|---|---|---|
| Hochrisiko (Anhang III) | Alles rund um Bewerbung/Beschäftigten-Bewertung | Nicht einsetzen (rote Linie oben) |
| Begrenzt/Transparenzpflicht | Chat-Assistenten, generierte Inhalte | Kennzeichnung, wo Externe interagieren |
| Minimal | Interne Entwurfs-/Extraktions-Use-Cases (P1–P3) | Nutzung innerhalb dieser Richtlinie |
| Zusätzlich | **AI Literacy (Art. 4):** Schulungspflicht | Abgedeckt durch das 3-Stufen-Schulungsprogramm |

## 5. Freigabeprozess für neue Use Cases

1. [Use-Case-Canvas](../templates/use-case-canvas.md) ausfüllen (inkl. Daten-Check)
2. AI-Office prüft: Datenklasse, rote Linien, Tool-Eignung — bei Personenbezug zusätzlich Datenschutz, bei Beschäftigtenbezug zusätzlich Betriebsrat
3. Freigabe / Auflagen / Ablehnung binnen 5 Arbeitstagen, dokumentiert im Use-Case-Register

## 6. Rollen

| Rolle | Verantwortung |
|---|---|
| AI-Office | Tool-Freigaben, Use-Case-Register, Schulungen, diese Richtlinie |
| IT/Security | Technische Freigabe, Verträge (AVV!), Zugriffskontrolle |
| Datenschutz | DSGVO-Checks, AVV-Prüfung |
| Betriebsrat | Mitbestimmung bei Beschäftigtenbezug, Sitz im Governance-Board |
| Jede/r Beschäftigte | Prüfpflicht für KI-Ausgaben, Meldung neuer Bedarfe |

## 7. Bei Vorfällen

Datenpanne oder versehentliche Eingabe sensibler Daten → sofort ans AI-Office + IT, **ohne Sanktionsangst** (Vorbild: der Vertriebs-Vorfall aus Phase 1 wurde zur besten Governance-Schulung des Hauses). Vertuschte Vorfälle sind das Problem, gemeldete sind der Normalbetrieb.
