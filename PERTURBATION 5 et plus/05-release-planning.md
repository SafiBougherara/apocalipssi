# Release Planning — EduTutor IA

**Date :** 02/07/2026 (mis à jour J4) · **Équipe :** EduTutor Groupe 14

---

## Release 1 — MVP · Tag `v1.0.0-mvp` · Deadline : mercredi 01/07 17h45

### Objectif
Livrer un produit fonctionnel de bout en bout permettant à un étudiant de s'inscrire, déposer un cours, générer un quiz, le passer et consulter son historique — avec conformité RGPD et sécurité de base.

### Features incluses

| Feature | Statut base reprise | Travail restant |
|---------|---------------------|-----------------|
| F1 · Auth email (inscription, validation, reset, profil) | Partiellement présent | Finitions, tests cas limites |
| F2 · Upload PDF / texte | Partiellement présent | Validation 5 Mo, 200 chars |
| F3 · Génération 10 QCM (llama3.2 — ADR J2) | Présent avec llama3.1 | Bascule vers llama3.2 |
| F4 · Soumission et correction | Partiellement présent | Fiabilisation |
| F5 · Score /10 + détail | Partiellement présent | Finitions UI |
| F6 · Historique par utilisateur | Partiellement présent | Persistance vérifiée |
| Pages légales RGPD | Vierges | À rédiger (J3-bis) |
| Sécurité anti-injection (OWASP LLM-01) | Absente | Implémentée (J3) |

### Critères de sortie (DoD Release 1)
- F1-F6 testables de bout en bout sans erreur
- Modèle llama3.2 actif (ADR documenté)
- Pages légales complétées
- Tests adversariaux prompt injection passants
- Tag `v1.0.0-mvp` posé sur le repo

---

## Release 2 — Évolutions · Tag `v1.1.0` · Deadline : jeudi 02/07 17h45

### Objectif
Adresser le segment enseignant (Mme Lefèvre) et améliorer l'engagement étudiant par la révision ciblée et le suivi de progression.

### Pistes retenues (à affiner avec le PO)

| Piste | Valeur | Effort estimé |
|-------|--------|---------------|
| Mode enseignant (Mme Lefèvre) | Nouveau segment, différenciation forte | Moyen |
| Dashboard progression (graphiques) | Fidélisation utilisateur | Faible (base fournie) |
| Révision des erreurs améliorée | Engagement, rétention | Faible (base fournie) |
| Génération haute qualité différée (llama3.1) | Qualité perçue enseignants | Faible (modèle déjà dispo) |
| Export quiz en PDF | Cas usage enseignant | Moyen |

### Features exclues Release 2
- Application mobile native
- Authentification SSO (ENT)
- RAG sur documents > 5 Mo

---

## Release 3 — Scale · RGAA · i18n · Tag `v2.0.0` · Perturbation J4

### Contexte
Adoption nationale par l'État français (condition : conformité RGAA) + levée de fonds + millions d'utilisateurs simultanés. Ce n'est plus un MVP : c'est un service public.

### Features incluses

| Axe | Feature | Estimation | MoSCoW |
|-----|---------|-----------|--------|
| **[a11y]** | Audit RGAA initial + rapport | 8 pts | Must |
| **[a11y]** | Correctifs contrastes (ratio ≥ 4.5:1) et focus visible | 5 pts | Must |
| **[a11y]** | Navigation clavier complète (Tab/Entrée/Échap/flèches) | 3 pts | Must |
| **[a11y]** | Labels ARIA sur tous les éléments interactifs | 3 pts | Must |
| **[i18n]** | Externalisation des textes UI en fichiers de langue (fr/en/es) | 8 pts | Must |
| **[i18n]** | Détection automatique de la langue du navigateur | 2 pts | Must |
| **[i18n]** | Paramètre de langue transmis au LLM à la volée | 5 pts | Should |
| **[scale]** | Tests de charge (10 000 utilisateurs simultanés) | 5 pts | Must |
| **[scale]** | Cache Redis sur les appels LLM identiques | 8 pts | Must |
| **[scale]** | Autoscaling horizontal (Kubernetes ou équivalent) | 13 pts | Should |
| **[scale]** | Fournisseur LLM de secours (OpenAI ou Claude en fallback) | 5 pts | Could |
| **[risk]** | Monitoring disponibilité + alertes (Prometheus/Grafana) | 3 pts | Should |

### Critères de sortie (DoD Release 3)
- Audit RGAA : 0 critère bloquant de niveau 1
- Interface disponible en français, anglais et espagnol
- Test de charge validé : p95 < 15s à 10 000 utilisateurs simultanés
- Tag `v2.0.0` posé sur le repo
