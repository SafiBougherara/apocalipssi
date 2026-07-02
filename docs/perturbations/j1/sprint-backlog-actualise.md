# Sprint Backlog actualisé — Suite perturbation J1

**Date :** 29/06/2026 14h30 · **Équipe :** EduTutor Groupe 14
**Motif de la mise à jour :** Prise en compte du persona Mme Lefèvre

---

## Ce qui change

Le persona Mme Lefèvre ne modifie pas les tâches techniques de R1 : ses besoins de base sont couverts par F1-F6. En revanche, il renforce la priorité de deux tâches déjà au backlog :

| Tâche | Avant J1 | Après J1 | Justification |
|-------|----------|----------|---------------|
| T-10 · Pages légales RGPD | Should | **Must** | Mme Lefèvre exige une mention RGPD explicite avant tout usage |
| T-06 · Qualité génération QCM | Important | **Critique** | Une erreur factuelle dans le quiz de Mme Lefèvre = risque réputationnel fort |

## Nouvelles tâches ajoutées

| ID | Tâche | Points | Priorité |
|----|-------|--------|----------|
| T-14 | Ajouter mention "Données traitées localement — RGPD" visible dans l'interface (footer ou page upload) | 1 | Must |
| T-15 | Valider la qualité des questions générées sur un cours de biologie lycée (test manuel Mme Lefèvre) | 1 | Should |

## Sprint Backlog mis à jour

| ID | Tâche | Points | Statut |
|----|-------|--------|--------|
| T-01 | Auth : inscription + validation email | 3 | A faire |
| T-02 | Auth : connexion + reset mot de passe | 2 | A faire |
| T-03 | Upload PDF avec validation 5 Mo | 2 | A faire |
| T-04 | Saisie texte avec validation 200 chars | 1 | A faire |
| T-05 | Bascule llama3.1 → llama3.2 (ADR-001) | 2 | A faire |
| T-06 | Génération 10 QCM JSON valide + test qualité | 3 | A faire |
| T-07 | Soumission + correction côté serveur | 2 | A faire |
| T-08 | Score /10 + détail réponses | 2 | A faire |
| T-09 | Historique persisté par utilisateur | 2 | A faire |
| T-10 | Pages légales RGPD (4 pages) | 2 | **Must** |
| T-11 | Protection anti-prompt injection | 3 | A faire |
| T-12 | Endpoint SAR RGPD | 2 | A faire |
| T-13 | Benchmark LLM + ADR-001 | 1 | **Terminé** |
| T-14 | Mention RGPD visible dans l'interface | 1 | A faire |
| T-15 | Test qualité cours biologie lycée | 1 | A faire |

**Total :** 29 pts
