# Burndown & Burnup — Perturbation J4

**Date :** 02/07/2026 · **Équipe :** EduTutor Groupe 14

---

## Burndown S2 (sprint en cours au moment de la perturbation J4)

Le sprint S2 a absorbé les perturbations J1 (Mme Lefèvre / RGPD) et J3 (prompt injection + SAR RGPD). La vélocité réelle a été inférieure à la capacité initiale en raison de ces insertions non planifiées.

| Jour | Points restants (idéal) | Points restants (réel) | Événement |
|------|------------------------|----------------------|-----------|
| Début S2 | 29 | 29 | Début du sprint — 29 pts planifiés |
| J+1 | 23 | 26 | — |
| J+2 | 17 | 22 | J1 Perturbation : ajout T-14 + T-15 (+5 pts scope) |
| J+3 | 11 | 21 | — |
| J+4 | 5 | 14 | J3 Perturbation : ajout patch injection + tests adversariaux (+8 pts) |
| J+5 (fin S2) | 0 | 6 | Sprint terminé avec 6 pts non livrés (reportés en S3) |

**Constat :** 2 perturbations non planifiées ont ajouté 13 pts de scope en cours de sprint. Le déficit de 6 pts est reporté en S3.

---

## Burnup projet (périmètre cumulé vs. livré)

Le burnup illustre l'impact cumulé de chaque perturbation sur le périmètre total et la date de fin estimée.

| Jalons | Scope total (pts) | Livré cumulé (pts) | Delta |
|--------|------------------|-------------------|-------|
| Cadrage initial (J1 matin) | 47 | 0 | -47 |
| Fin S1 (J1 soir) | 47 | 27 | -20 |
| Après perturbation J1 | 52 (+5) | 27 | -25 |
| Fin S2 (J2-J3) | 52 | 46 | -6 |
| Après perturbation J3 (injection + SAR) | 60 (+8) | 46 | -14 |
| Après perturbation J4 (scale + RGAA + i18n) | 107 (+47) | 46 | -61 |

### Décomposition de l'ajout J4 (+47 pts)

| US | Axe | Pts |
|----|-----|-----|
| US-25 Audit RGAA | [a11y] | 8 |
| US-26 Contrastes + focus | [a11y] | 5 |
| US-27 Navigation clavier | [a11y] | 3 |
| US-28 Externalisation i18n | [i18n] | 8 |
| US-29 Langue LLM à la volée | [i18n] | 5 |
| US-30 Tests de charge | [scale] | 5 |
| US-31 Cache Redis | [scale] | 8 |
| US-32 LLM de secours | [scale] | 5 |
| **Total J4** | | **47** |

---

## Lecture du burnup — Impact sur la date de fin

Avec la vélocité observée (≈ 23 pts/sprint) et un scope total de 107 pts :

| Release | Scope (pts) | Sprints nécessaires | Date estimée |
|---------|------------|---------------------|-------------|
| R1 — MVP (livré) | 47 | 2 | 01/07/2026 ✓ |
| R2 — Évolutions | +13 | +1 | S3 |
| R3 — Scale·RGAA·i18n | +47 | +2 | S4-S5 |

**Conclusion pour la soutenance :** la perturbation J4 a multiplié le scope résiduel par 3. Sans priorisation stricte (Must/Should/Could), la date de livraison R3 serait repoussée de 2 sprints. La stratégie retenue est de concentrer S3 sur les Must (RGAA bloquant + i18n structurel) et de reporter l'autoscaling et le LLM de secours en S4.
