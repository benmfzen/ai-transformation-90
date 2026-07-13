# Template: KPI-Definitionsblatt Jahr 1

**Einsatz:** Wird in Phase 3 (Tag 75–84) ausgefüllt und mit der GF am Tag 90 verabschiedet. Regel: **Jede Kennzahl hat Formel, Quelle, Owner und Kadenz — sonst ist sie keine Kennzahl, sondern eine Meinung.** Alle Messungen auf Team-/Prozessebene, nie pro Person (BR-Zusage).

---

## Wert-KPIs (was das Programm wirtschaftlich bringt)

| KPI | Formel | Quelle | Owner | Kadenz | Ziel Jahr 1 |
|---|---|---|---|---|---|
| **Validierter Jahreswert** | Σ je Pilot: gemessene Verbesserung × Volumen × Kostensatz, annualisiert — erst NACH bestandenem Pilot-Review zählbar | Pilot-Messungen + Controlling-Kostensätze | Programmleitung | monatlich | |
| **Realisierter Wert** | Anteil des validierten Werts, der eingetreten ist (vermiedene Stelle formal gestrichen, Agentur-Rechnung real gesunken, Output real gestiegen) | Controlling | Programmleitung + CFO | quartalsweise | |
| **AI-Kosten gesamt** | Lizenzen + Nutzung (Token) + externe Unterstützung + AI-Office-Kapazität | Tool-Register + Controlling | AI-Office | monatlich | |
| **Wert/Kosten-Verhältnis** | realisierter Wert ÷ AI-Kosten | abgeleitet | Programmleitung | quartalsweise | > 2 ab Q3 |

**Die wichtigste Regel steht im Kleingedruckten:** Zeitersparnis zählt erst als realisierter Wert, wenn dokumentiert ist, *wohin* die Zeit geflossen ist (Mehrvolumen ohne Neueinstellung, kürzere Antwortzeiten, verlagerte Aufgaben). Sonst ist es eine Excel-Zahl.

## Adoption-KPIs (ob die Organisation wirklich anders arbeitet)

| KPI | Formel | Quelle | Owner | Kadenz | Ziel Jahr 1 |
|---|---|---|---|---|---|
| **Aktive Nutzung je Rollout-Abteilung** | wöchentlich aktive Nutzer ÷ Teamgröße | Tool-Analytics (Teamebene!) | Champion | monatlich | > 70 % |
| **Prozessabdeckung** | Vorgänge, die durch den neuen Prozess laufen ÷ alle Vorgänge des Typs | Fachsystem (Ticket-/ERP-Report) | Team Lead | monatlich | je Charter |
| **Produktive Use Cases** | Anzahl Use Cases im Register mit Status „im Betrieb" | Use-Case-Register | AI-Office | quartalsweise | |
| **Schulungsquote** | geschulte MA (Stufe 1) ÷ alle MA | Teilnahmelisten | AI-Office | quartalsweise | 100 % bis Q2 |

## Qualitäts- & Risiko-KPIs (ob es gut und sicher bleibt)

| KPI | Formel | Quelle | Owner | Kadenz | Schwelle |
|---|---|---|---|---|---|
| **Qualität je Use Case** | Rubrik-Score der Stichprobe (aus dem jeweiligen [Charter](pilot-charter.md)) | wöchentliche Blind-Stichprobe | Team Lead | monatlich | ≥ Baseline |
| **Nacharbeitsquote** | korrigierte/wiedereröffnete Vorgänge ÷ alle | Fachsystem | Team Lead | monatlich | ≤ Baseline |
| **Gemeldete Vorfälle** | Anzahl + Zeit bis Behebung | Vorfall-Log | AI-Office | monatlich | Meldeweg wird GENUTZT — 0 Meldungen bei breiter Nutzung ist ein Warnsignal, kein Erfolg |
| **Schatten-Nutzung** | nicht freigegebene Tools im Einsatz (Stichprobe/Netzwerk) | IT | IT | quartalsweise | sinkend |

## Berichtswege

| Ebene | Format | Inhalt |
|---|---|---|
| GF, monatlich | 1 Seite im [Status-Report](status-report.md)-Stil | Wert, Kosten, Adoption, Blocker, anstehende Entscheidungen |
| Portfolio-Runde, monatlich | KPI-Tabelle vollständig | Basis für Re-Scoring und Slot-Entscheidungen |
| Champions, monatlich | eigene Abteilungs-KPIs | Coaching-Grundlage, nie Ranking |

**Anti-Patterns:** KPIs pro Person ausweisen (BR-Bruch) · Ziele nachträglich an Ist-Werte anpassen · „Anzahl Prompts" oder „Tool-Logins" als Wert-KPI verkaufen (Aktivität ≠ Wirkung) · mehr als ~12 KPIs (dann liest sie niemand mehr).
