# Sprint Backlog S3 (Next Sprint) — Perturbation J4

**Date :** 02/07/2026 · **Équipe :** EduTutor Groupe 14
**Sprint :** S3 · **Durée :** 5 jours · **Capacité :** 30 pts
**Objectif sprint :** Poser les fondations de la Release 3 — audit RGAA lancé, i18n structuré, tests de charge planifiés

> Les sprint backlogs S1 (`docs/cadrage/07-sprint-backlog-s1.md`) et S2 (`docs/perturbations/j1/sprint-backlog-actualise.md`) sont conservés en historique.

---

## Sélection du sprint

| ID tâche | US | Description | Responsable | Estimation | Statut |
|----------|----|-------------|-------------|-----------|--------|
| T-16 | US-25 | [a11y] Audit RGAA initial : parcourir l'interface, lister les critères bloquants | Dev Front | 5 pts | A faire |
| T-17 | US-26 | [a11y] Corriger les contrastes (ratio ≥ 4.5:1 sur tous les composants) | Dev Front | 3 pts | A faire |
| T-18 | US-27 | [a11y] Rendre la navigation clavier fonctionnelle (Tab order + focus outline) | Dev Front | 3 pts | A faire |
| T-19 | US-28 | [i18n] Intégrer i18next et extraire tous les textes UI en fichiers fr/en | Dev Front | 5 pts | A faire |
| T-20 | US-28 | [i18n] Compléter le fichier de traduction espagnol (es.json) | Dev Front | 3 pts | A faire |
| T-21 | US-29 | [i18n] Ajouter le paramètre `lang` dans le system prompt Ollama | Dev Back | 2 pts | A faire |
| T-22 | US-30 | [scale] Écrire le scénario k6 de base (simulation 1 000 utilisateurs) | Dev Back | 3 pts | A faire |
| T-23 | US-31 | [scale] Intégrer Redis dans docker-compose + configurer le cache LLM | Dev Back | 5 pts | A faire |

**Total sprint :** 29 pts (capacité 30 pts)

---

## Impediments identifiés

| # | Blocage | Impact | Action |
|---|---------|--------|--------|
| I-01 | Outil d'audit RGAA à choisir (axe-core, Lighthouse, RGAA Check) | T-16 bloquée si non choisi | Décision J4 matin |
| I-02 | Licence k6 Cloud nécessaire pour tests > 100 VU | T-22 limitée en local | Utiliser k6 open-source + instance dédiée |
| I-03 | Traductions espagnoles à valider par un locuteur natif | T-20 peut être incomplète | Itération R3 avec revue externe |

---

## Burndown S3 (prévisionnel)

| Jour | Points restants (prévu) |
|------|------------------------|
| Début S3 | 29 |
| J+1 | 23 |
| J+2 | 17 |
| J+3 | 11 |
| J+4 | 5 |
| J+5 (fin) | 0 |
