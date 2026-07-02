# Product Vision Board — EduTutor IA

**Date :** 02/07/2026 (mis à jour J4) · **Équipe :** EduTutor Groupe 14

---

## Vision

> Permettre à tout étudiant — partout dans le monde, quelle que soit sa situation de handicap — de transformer son cours en quiz personnalisé en moins de 15 secondes, sans jamais exposer ses données à un tiers.

---

## Cible

| Segment | Description |
|---------|-------------|
| Primaire | Étudiant·e du supérieur (BTS, Licence, Master) qui veut réviser à partir de ses propres cours |
| Secondaire émergente | Enseignant·e (persona Mme Lefèvre) qui veut créer des supports d'évaluation pour sa classe |
| Nouveau J4 — International | Lycéen·ne francophone ou hispanophone à l'étranger (persona Lucia) |
| Nouveau J4 — Institutionnel | Établissements publics français soumis au RGAA (lycées, universités) |

---

## Besoins

| Problème | Solution EduTutor IA |
|----------|----------------------|
| Créer des QCM à la main est trop long | Génération automatique en < 15s à partir d'un PDF ou texte |
| Les banques de questions génériques sont hors-sujet | Questions ancrées dans le cours réel de l'étudiant |
| Les outils concurrents envoient les données aux USA | Ollama local : aucune donnée ne quitte le serveur |
| L'étudiant ne sait pas où il en est | Historique des scores et révision des erreurs |
| **[J4] Les services publics doivent être accessibles à tous** | Conformité RGAA : navigation clavier, contrastes, lecteurs d'écran |
| **[J4] Des millions d'utilisateurs simultanés = risque de panne** | Architecture scalable : cache, autoscaling, LLM de secours |
| **[J4] Les élèves internationaux ne lisent pas le français** | i18n : interface et quiz générés dans la langue de l'élève |

---

## Proposition de valeur unique

**Enseignant-first · RGPD local-first · Accessible · International**

Là où Quizlet, Wilgo et Khanmigo sont étudiant-first et cloud-first, EduTutor IA est la seule plateforme à combiner des prompts métier pensés pour les enseignants, une génération ancrée dans le document fourni, une conformité RGPD native (Ollama local), une accessibilité RGAA complète et un support multilingue natif.

---

## Objectifs produit

| Release | Objectif | Indicateur de succès |
|---------|----------|----------------------|
| R1 — MVP | Générer un quiz de 10 QCM | p95 < 15s |
| R1 — MVP | Authentification sécurisée | Validation email fonctionnelle |
| R1 — MVP | Historique utilisateur | Score et date persistés par compte |
| R1 — MVP | Conformité RGPD | Aucune donnée transmise hors serveur |
| R2 | Mode enseignant + dashboard | Mme Lefèvre peut générer et exporter |
| **R3 [J4]** | **Accessibilité RGAA niveau AA** | **Audit RGAA : 0 critère bloquant** |
| **R3 [J4]** | **Internationalisation** | **Interface + quiz disponibles en fr/en/es** |
| **R3 [J4]** | **Scalabilité** | **10 000 utilisateurs simultanés sans dégradation** |

---

## Périmètre Release 1 (Must have)

F1 · Inscription/connexion email avec validation
F2 · Upload PDF ≤ 5 Mo ou texte ≥ 200 caractères
F3 · Génération 10 QCM via LLM local (llama3.2)
F4 · Soumission et correction automatique
F5 · Score /10 + détail des réponses
F6 · Historique des quizz par utilisateur

## Périmètre Release 2 (Should/Could)

- Mode enseignant avancé (Mme Lefèvre)
- Dashboard progression (graphiques)
- Révision ciblée des erreurs
- Export quiz en PDF

## Périmètre Release 3 — J4 (Scale · RGAA · i18n)

- [a11y] Audit RGAA + correctifs (contrastes, focus, navigation clavier, ARIA)
- [i18n] Externalisation des textes + support fr / en / es
- [i18n] Paramètre de langue transmis au LLM à la volée
- [scale] Tests de charge + cache Redis + autoscaling
- [scale] Fournisseur LLM de secours (résilience)
- [risk] Monitoring et alertes de disponibilité
