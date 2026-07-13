# Phase 1 — Verstehen (Tag 1–30)

**Leitfrage:** Wo ist der größte AI-Hebel, und wer in der Organisation will ihn ziehen?

**Deliverables:** vollständige Abteilungsprofile · Impact-/Readiness-Scoring · [Impact-Matrix](../methodik/impact-matrix.md) · Champion-Shortlist · GF-Entscheidung über 3 Piloten

---

## Woche 1 (Tag 1–7): Aufsetzen & Org-Scan

- [ ] Kick-off mit Geschäftsführung: Programmziel, Zeitplan, Entscheidungspunkte (Tag 30/60/90) verbindlich machen
- [ ] Betriebsrat informieren — **vor** dem ersten Interview, nicht danach
- [ ] Org-Chart und Kerndaten je Abteilung erheben: Headcount, Kernprozesse, Systeme, bekannte Schmerzpunkte → [Abteilungsprofil-Struktur](../org/abteilungen/)
- [ ] Bestandsaufnahme Schatten-KI: Wer nutzt heute schon was? (anonym, straffrei — es geht um ein Lagebild, nicht um Schuldige)
- [ ] Interview-Termine mit allen 9 Heads buchen (45 Min, [Leitfaden](../templates/interview-leitfaden.md))

## Woche 2–3 (Tag 8–19): Head-Interviews

- [ ] 9 Interviews führen — pro Gespräch: Kernprozesse, Zeitfresser, Datenlage, Haltung zu KI, „Was würdest du automatisieren, wenn es einfach ginge?"
- [ ] Direkt nach jedem Interview: Abteilungsprofil vervollständigen und **vorläufig scoren** (Eindrücke verblassen schnell)
- [ ] Parallel: IT-Deep-Dive — Systemlandschaft, Datenzugänglichkeit, Security-Anforderungen, bestehende Verträge (M365? Cloud?)
- [ ] Quick-Win-Kandidaten notieren: alles, was mit Bordmitteln in < 2 Wochen ginge

**Worauf im Interview wirklich achten:** Nicht was der Head über KI *sagt*, sondern ob er/sie konkrete eigene Prozessprobleme benennen kann. „KI ist die Zukunft" ist ein schwaches Signal. „Meine Leute verbringen 30 % der Zeit mit dem Abtippen von Lieferscheinen" ist ein starkes.

## Woche 4 (Tag 20–30): Scoring & Entscheidung

- [ ] Finales Scoring aller Abteilungen auf den [6 Dimensionen](../methodik/champion-scoring.md) — im Vieraugenprinzip mit einer zweiten Person kalibrieren
- [ ] [Impact-Matrix](../methodik/impact-matrix.md) erstellen und Pilotreihenfolge herleiten
- [ ] Champion-Shortlist: max. 3 Namen, mit Begründung aus den Interviews
- [ ] Use-Case-Ideen der Top-Abteilungen als [Canvas](../templates/use-case-canvas.md) ausarbeiten (je 1 Seite)
- [ ] **GF-Review (Tag 30):** Matrix präsentieren, 3 Piloten + Champions beschließen, Phase-2-Budget freigeben

## Abbruch-/Warnsignale in Phase 1

| Signal | Bedeutung | Reaktion |
|---|---|---|
| GF verschiebt das Tag-30-Review | Programm hat keinen echten Sponsor | Eskalieren — ohne Entscheidungstermin keine Phase 2 |
| Kein Head schafft es über Readiness 3 | Org ist nicht reif für Piloten | Phase 2 durch Enablement-Sprint ersetzen (Schulung statt Pilot) |
| IT blockiert jeden Datenzugang | Governance-Problem, kein Technik-Problem | CISO/GF-Gespräch vorziehen, [Richtlinie](../governance/ai-richtlinie.md) zuerst |

## Ergebnis im Case (NORDWERK)

Das durchgespielte Scoring aller 9 Abteilungen steht in der [Impact-Matrix](../methodik/impact-matrix.md). Kurzfassung: **Kundenservice** (Impact 4,7 / Readiness 4,3) und **Vertrieb** (4,3 / 3,7) sind die klaren Pilot-Kandidaten, **Finanzen & Controlling** (3,7 / 4,0) der solide dritte. Produktion hat den größten Langfrist-Hebel, aber die schlechteste Datenlage — bewusst auf Phase 3 vertagt.
