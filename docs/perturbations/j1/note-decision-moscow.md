# Note de décision MoSCoW — Suite perturbation J1 (Mme Lefèvre)

**Date :** 29/06/2026 · **Équipe :** EduTutor Groupe 14
**Décision validée par :** Product Owner

---

## Contexte

L'émergence du persona Mme Lefèvre (enseignante) en J1 pose la question : faut-il intégrer ses besoins au MVP (Release 1) ou les reporter en Release 2 ?

---

## Analyse

| Besoin Mme Lefèvre | Déjà couvert R1 ? | Effort additionnel | Décision |
|--------------------|-------------------|--------------------|---------|
| Upload PDF + génération QCM | Oui (F2, F3) | Nul | **R1 — gratuit** |
| Conformité RGPD visible | Partiellement (pages légales à compléter) | Faible | **R1 — à finir** |
| Relire/modifier les questions avant usage | Non | Moyen-fort | **R2** |
| Compte enseignant distinct (rôle dédié) | Non | Fort | **R2** |
| Export quiz en PDF pour les élèves | Non | Moyen | **R2** |
| Questions calibrées niveau lycée (prompt métier) | Non | Moyen | **R2** |

---

## Décision retenue

**Mme Lefèvre peut utiliser le MVP R1 tel quel** : les features F1-F6 couvrent ses besoins de base (upload cours, génération QCM, correction). La différence par rapport à Lucas est uniquement dans l'usage, pas dans les fonctionnalités.

**Le mode enseignant complet** (relecture, export, prompt métier, rôle dédié) est formellement classé **Should/Could en Release 2**.

### MoSCoW actualisé

| Priorité | Feature |
|----------|---------|
| **Must R1** | F1-F6 inchangés · Pages légales RGPD · Conformité RGPD visible |
| **Should R2** | Mode enseignant (relecture + export) · Prompt métier lycée |
| **Could R2** | Compte enseignant avec rôle distinct · Calibrage niveau |
| **Won't** | SSO ENT · Application mobile |

---

## Justification

Intégrer le mode enseignant complet en R1 représente 2-3 jours de développement supplémentaires non planifiés. Dans le contexte d'un sprint de 3 jours avec 5 perturbations actives, ce serait un risque de livraison inacceptable. Le PO valide cette décision.
