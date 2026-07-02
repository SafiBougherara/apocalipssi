# Product Backlog — EduTutor IA

**Date :** 02/07/2026 (mis à jour J4) · **Équipe :** EduTutor Groupe 14
**Méthode :** MoSCoW · Critères INVEST · DoR / DoD définis

---

## Définition of Ready (DoR)
Une story est prête à être prise en sprint si :
- [ ] Elle est rédigée au format "En tant que... je veux... afin de..."
- [ ] Elle a des critères d'acceptation clairs et testables
- [ ] Elle est estimée (points de complexité)
- [ ] Elle ne dépend pas d'une story non terminée

## Définition of Done (DoD)
Une story est terminée si :
- [ ] Le code est commité sur GitHub avec un message Conventional Commits
- [ ] Les critères d'acceptation sont tous vérifiés manuellement
- [ ] Aucune régression sur les stories précédentes
- [ ] La feature est déployable via `docker compose up`

---

## Backlog Release 1 — Must Have

### US-01 · Inscription par email
**En tant qu'** étudiant, **je veux** créer un compte avec mon email, **afin de** pouvoir accéder à EduTutor IA.
- CA1 : L'inscription échoue si l'email est déjà utilisé
- CA2 : Un email de validation est envoyé après inscription
- CA3 : Le compte est inutilisable avant validation de l'email
- **Estimation :** 3 pts · **MoSCoW :** Must

### US-02 · Validation email
**En tant qu'** étudiant inscrit, **je veux** valider mon adresse email via un lien, **afin de** sécuriser mon compte.
- CA1 : Le lien expire après 24h
- CA2 : Un bouton "Renvoyer le lien" est disponible depuis l'app
- **Estimation :** 2 pts · **MoSCoW :** Must

### US-03 · Connexion / Déconnexion
**En tant qu'** étudiant, **je veux** me connecter avec email + mot de passe, **afin d'** accéder à mon espace personnel.
- CA1 : 5 tentatives échouées → blocage temporaire 15 min
- CA2 : La déconnexion invalide le token JWT
- **Estimation :** 2 pts · **MoSCoW :** Must

### US-04 · Réinitialisation du mot de passe
**En tant qu'** étudiant, **je veux** recevoir un lien de réinitialisation par email, **afin de** retrouver l'accès à mon compte.
- CA1 : Le lien expire après 1h
- CA2 : L'ancien mot de passe est invalidé dès le reset
- **Estimation :** 2 pts · **MoSCoW :** Must

### US-05 · Upload d'un cours PDF
**En tant qu'** étudiant, **je veux** uploader un PDF de cours (≤ 5 Mo), **afin de** générer un quiz à partir de son contenu.
- CA1 : Fichiers > 5 Mo refusés avec message d'erreur explicite
- CA2 : Seuls les fichiers .pdf sont acceptés
- CA3 : Le texte est extrait et transmis au LLM
- **Estimation :** 3 pts · **MoSCoW :** Must

### US-06 · Saisie d'un cours en texte
**En tant qu'** étudiant, **je veux** coller mon cours directement dans un champ texte, **afin de** ne pas avoir à créer un PDF.
- CA1 : Minimum 200 caractères requis (validation côté serveur)
- CA2 : Message d'erreur si le champ est trop court
- **Estimation :** 1 pt · **MoSCoW :** Must

### US-07 · Génération de 10 QCM
**En tant qu'** étudiant, **je veux** que l'app génère automatiquement 10 questions QCM, **afin de** me tester sur mon cours.
- CA1 : Exactement 10 questions avec 4 options chacune (A/B/C/D)
- CA2 : Une seule bonne réponse par question
- CA3 : Génération en moins de 15s (p95) sur serveur de référence
- CA4 : Modèle llama3.2 utilisé (cf. ADR-001)
- **Estimation :** 5 pts · **MoSCoW :** Must

### US-08 · Soumission et correction
**En tant qu'** étudiant, **je veux** soumettre mes réponses et obtenir la correction, **afin de** savoir lesquelles sont correctes.
- CA1 : Toutes les questions doivent avoir une réponse avant soumission
- CA2 : La correction est calculée côté serveur (non falsifiable)
- **Estimation :** 3 pts · **MoSCoW :** Must

### US-09 · Affichage du score
**En tant qu'** étudiant, **je veux** voir mon score /10 et le détail des bonnes/mauvaises réponses, **afin de** comprendre mes erreurs.
- CA1 : Score affiché sous forme X/10
- CA2 : Chaque question indique si la réponse était juste ou fausse
- CA3 : La bonne réponse est révélée pour les questions ratées
- **Estimation :** 2 pts · **MoSCoW :** Must

### US-10 · Historique des quizz
**En tant qu'** étudiant, **je veux** consulter la liste de mes quizz passés, **afin de** suivre ma progression.
- CA1 : Chaque entrée affiche : date, nom du cours, score
- CA2 : L'historique est filtré par utilisateur connecté (isolation des données)
- CA3 : Trié par date décroissante
- **Estimation :** 3 pts · **MoSCoW :** Must

---

## Backlog Release 1 — Should Have

| ID | User Story | Estimation | MoSCoW |
|----|-----------|-----------|--------|
| US-11 | Pages légales RGPD complétées (CGU, Politique de confidentialité, Mentions légales, Cookies) | 2 pts | Should |
| US-12 | Feedback visuel pendant la génération (loader + message) | 1 pt | Should |
| US-13 | Gestion du profil utilisateur (modifier email, supprimer compte) | 2 pts | Should |

---

## Backlog Release 2 — Could Have / Won't (Release 1)

| ID | User Story | MoSCoW R1 | Cible |
|----|-----------|-----------|-------|
| US-20 | Mode enseignant : génération de quiz pour une classe | Won't R1 | R2 |
| US-21 | Dashboard progression avec graphiques | Could | R2 |
| US-22 | Révision ciblée des erreurs (mode flashcard) | Could | R2 |
| US-23 | Génération haute qualité différée (llama3.1) | Won't R1 | R2 |
| US-24 | Export quiz en PDF | Won't R1 | R2 |

---

## Backlog Release 3 — J4 (Scale · RGAA · i18n)

### [a11y] Accessibilité RGAA

### US-25 · [a11y] Audit RGAA + rapport
**En tant qu'** administrateur, **je veux** un audit RGAA complet de l'interface, **afin de** connaître les écarts à corriger avant l'adoption institutionnelle.
- CA1 : Rapport listant tous les critères RGAA de niveau 1 évalués
- CA2 : Chaque critère bloquant est associé à un ticket de correctif
- CA3 : Rapport disponible dans le repo (`docs/`)
- **Estimation :** 8 pts · **MoSCoW :** Must · **R3**

### US-26 · [a11y] Contrastes et focus visible
**En tant que** Lucia (malvoyante), **je veux** que tous les textes respectent un ratio de contraste ≥ 4.5:1 et que le focus clavier soit toujours visible, **afin de** lire et naviguer sans effort.
- CA1 : Ratio de contraste texte/fond ≥ 4.5:1 sur tous les composants (RGAA 3.2)
- CA2 : Focus visible sur chaque élément interactif (outline non supprimé)
- CA3 : Vérifiable avec l'outil axe-core en CI
- **Estimation :** 5 pts · **MoSCoW :** Must · **R3**

### US-27 · [a11y] Navigation clavier complète
**En tant que** Lucia, **je veux** naviguer dans toute l'interface avec le clavier (Tab, Entrée, Échap, flèches), **afin de** ne pas utiliser la souris.
- CA1 : Tous les éléments interactifs sont atteignables au Tab dans un ordre logique
- CA2 : Les modales et menus sont fermables à l'Échap
- CA3 : Aucun "piège de focus" (focus coincé dans un composant)
- **Estimation :** 3 pts · **MoSCoW :** Must · **R3**

### [i18n] Internationalisation

### US-28 · [i18n] Externalisation des textes UI
**En tant que** développeur, **je veux** que tous les textes de l'interface soient externalisés dans des fichiers de traduction (fr/en/es), **afin de** permettre le changement de langue sans modifier le code.
- CA1 : Bibliothèque i18n intégrée (ex : i18next)
- CA2 : Fichiers de traduction pour fr, en, es disponibles dans le repo
- CA3 : Aucun texte en dur dans les composants React
- **Estimation :** 8 pts · **MoSCoW :** Must · **R3**

### US-29 · [i18n] Paramètre de langue du LLM à la volée
**En tant que** Lucia, **je veux** que le quiz soit généré dans la langue que j'ai sélectionnée dans l'interface, **afin de** réviser dans ma langue maternelle.
- CA1 : Un paramètre `lang` est ajouté au system prompt Ollama (ex : "Génère le quiz en espagnol")
- CA2 : Le changement de langue est effectif sans redémarrage du serveur
- CA3 : Testé pour fr, en, es
- **Estimation :** 5 pts · **MoSCoW :** Should · **R3**

### [scale] Scalabilité

### US-30 · [scale] Tests de charge
**En tant qu'** administrateur, **je veux** un rapport de tests de charge validant la tenue à 10 000 utilisateurs simultanés, **afin de** garantir la disponibilité lors de pics nationaux.
- CA1 : Scénario de charge simulé avec k6 ou Locust
- CA2 : p95 < 15s maintenu jusqu'à 10 000 utilisateurs simultanés
- CA3 : Rapport disponible dans le repo
- **Estimation :** 5 pts · **MoSCoW :** Must · **R3**

### US-31 · [scale] Cache Redis sur les appels LLM
**En tant qu'** administrateur, **je veux** que les requêtes LLM identiques soient mises en cache (Redis), **afin de** réduire la charge sur Ollama et améliorer la latence à grande échelle.
- CA1 : Un quiz généré pour un texte source identique est servi depuis le cache en < 100ms
- CA2 : Le cache expire après 24h (TTL configurable)
- CA3 : La désactivation du cache est possible via variable d'environnement
- **Estimation :** 8 pts · **MoSCoW :** Must · **R3**

### US-32 · [risk] Fournisseur LLM de secours
**En tant qu'** administrateur, **je veux** configurer un LLM de secours (ex : OpenAI GPT-4o mini) qui prend le relais automatiquement si Ollama est indisponible, **afin de** garantir la continuité de service.
- CA1 : Si Ollama répond avec une erreur ou timeout, le fallback est déclenché automatiquement
- CA2 : Le fournisseur de secours est configurable via variable d'environnement
- CA3 : Un log `WARNING` indique chaque basculement
- **Estimation :** 5 pts · **MoSCoW :** Could · **R3**
