# Story Map — EduTutor IA

**Date :** 02/07/2026 (mis à jour J4) · **Équipe :** EduTutor Groupe 14

---

## Colonne vertébrale (activités utilisateur)

```
SE CONNECTER → FOURNIR UN COURS → GÉNÉRER UN QUIZ → PASSER LE QUIZ → CONSULTER SES RÉSULTATS → SUIVRE SA PROGRESSION
```

---

## Décomposition par release

### RELEASE 1 — MVP (mercredi 01/07 17h45)

| Activité | User Stories incluses |
|----------|-----------------------|
| **Se connecter** | S'inscrire avec email · Valider son email · Se connecter · Réinitialiser son mot de passe · Gérer son profil |
| **Fournir un cours** | Uploader un PDF ≤ 5 Mo · Saisir un texte ≥ 200 caractères |
| **Générer un quiz** | Lancer la génération de 10 QCM via LLM local · Voir un feedback pendant la génération |
| **Passer le quiz** | Répondre aux 10 questions une par une · Soumettre ses réponses |
| **Consulter ses résultats** | Voir son score /10 · Voir le détail bonnes/mauvaises réponses |
| **Suivre sa progression** | Consulter l'historique des quizz (date, cours, score) |

### RELEASE 2 — Évolutions enseignant + engagement (jeudi 02/07 17h45)

| Activité | User Stories envisagées |
|----------|-------------------------|
| **Mode enseignant** | Créer un compte enseignant · Générer un quiz pour ses élèves · Relire et modifier les questions · Exporter en PDF |
| **Révision ciblée** | Revoir uniquement les questions ratées · Repasser un quiz sur ses erreurs |
| **Dashboard progression** | Graphique d'évolution du score dans le temps · Identification des notions faibles |
| **Mode sombre** | Basculer entre thème clair et sombre |
| **Génération haute qualité** | Choisir entre génération rapide (llama3.2) et haute qualité (llama3.1, mode différé) |

### RELEASE 3 — Scale · RGAA · i18n (J4 — perturbation adoption nationale)

| Axe | Activité | User Stories |
|-----|----------|-------------|
| **[a11y]** | Accessibilité RGAA | Audit RGAA niveau AA · Correctifs contrastes & focus visible · Navigation clavier complète · Labels ARIA sur tous les éléments interactifs |
| **[i18n]** | Internationalisation | Externaliser les textes en fichiers de langue (fr/en/es) · Détecter la langue du navigateur · Paramètre de langue transmis au LLM à la volée · Interface traduite en espagnol |
| **[scale]** | Passage à l'échelle | Tests de charge (10 000 utilisateurs simultanés) · Cache Redis sur les réponses LLM · Autoscaling horizontal · Fournisseur LLM de secours |
| **[risk]** | Résilience & monitoring | Monitoring disponibilité (Prometheus/Grafana) · Alertes automatiques · Politique de rétention des données |

---

## Priorisation MoSCoW par release

| Release | Must | Should | Could | Won't |
|---------|------|--------|-------|-------|
| **R1** | F1 Auth · F2 Upload · F3 Génération · F4 Correction · F5 Score · F6 Historique | Pages légales RGPD · Feedback génération | Mode sombre (fourni) | Mode enseignant · Export PDF |
| **R2** | Mode enseignant (Mme Lefèvre) | Dashboard · Révision erreurs | Mode sombre · HQ différé | Mobile natif · SSO |
| **R3 [J4]** | Audit RGAA + correctifs · Externalisation i18n (fr/en/es) · Tests de charge + cache | Paramètre langue LLM · Monitoring · Alertes | LLM de secours · Autoscaling | Conformité WCAG 2.2 AAA |
