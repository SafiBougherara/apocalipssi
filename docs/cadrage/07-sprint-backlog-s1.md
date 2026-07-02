# Sprint Backlog S1 — EduTutor IA

**Sprint 1 :** 29/06/2026 → 01/07/2026 (3 jours)
**Sprint Goal :** Livrer F1-F6 fonctionnels, llama3.2 actif, sécurité de base intégrée
**Équipe :** EduTutor Groupe 14 · **Vélocité cible :** 25 pts

---

## Tâches du sprint

| ID | Tâche | User Story | Assigné | Statut | Points |
|----|-------|-----------|---------|--------|--------|
| T-01 | Finir et tester F1 : inscription + validation email | US-01, US-02 | — | A faire | 3 |
| T-02 | Finir et tester F1 : connexion + reset mot de passe | US-03, US-04 | — | A faire | 2 |
| T-03 | Finir F2 : upload PDF avec validation 5 Mo | US-05 | — | A faire | 2 |
| T-04 | Finir F2 : saisie texte avec validation 200 chars | US-06 | — | A faire | 1 |
| T-05 | Basculer llama3.1 → llama3.2 (ADR-001) | US-07 | — | A faire | 2 |
| T-06 | Vérifier et tester F3 : génération 10 QCM JSON valide | US-07 | — | A faire | 3 |
| T-07 | Finir F4 : soumission + correction côté serveur | US-08 | — | A faire | 2 |
| T-08 | Finir F5 : affichage score + détail réponses | US-09 | — | A faire | 2 |
| T-09 | Finir F6 : historique persisté par utilisateur | US-10 | — | A faire | 2 |
| T-10 | Rédiger les 4 pages légales RGPD | US-11 | — | A faire | 2 |
| T-11 | Implémenter protection anti-prompt injection (J3) | — | — | A faire | 3 |
| T-12 | Endpoint SAR RGPD (export données utilisateur) | — | — | A faire | 2 |
| T-13 | Benchmark LLM + rédaction ADR-001 | — | — | Terminé | 1 |

**Total points :** 27 pts

---

## Impediments identifiés

| Impediment | Impact | Action |
|------------|--------|--------|
| ROCm non fonctionnel (Vulkan fallback) | Benchmark local lent | Résultats extrapolés serveur CUDA — documenté dans rapport |
| Pages légales à rédiger (contenu juridique) | Blocage J3-bis | Templates RGPD à compléter avec le PO |

---

## Burndown cible

| Fin de journée | Points restants cible |
|---------------|----------------------|
| J1 soir | 20 pts |
| J2 soir | 12 pts |
| J3 17h45 | 0 pts (MVP livré) |
