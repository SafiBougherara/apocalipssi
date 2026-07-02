# 🗺️ Guide de la Documentation & Grille de Notation (Jury)

Ce document sert de cartographie pour le jury et l'équipe. Il permet de retrouver instantanément chaque livrable et décision technique correspondant aux critères de la grille de notation d'EduTutor IA.

---

## 📌 1. Respect du Périmètre Demandé (MVP & Release 2) · Barème : /4

* **MVP Fonctionnel (F1-F6) :**
  * **Code Backend (Django DRF) :** [backend/](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend)
    * Logique métier des QCM / scoring : [backend/quizzes/](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/quizzes)
    * Connecteur et RAG local : [backend/llm/](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm)
  * **Code Frontend (React/Vite TS) :** [frontend/src/](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src)
    * Formulaires et pages : [frontend/src/pages/](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages)
* **Release 2 Cohérente (Dashboard + SAR + Admin + Erreurs) :**
  * Mode Enseignant (Admin) : [frontend/src/pages/admin/](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages/admin)
  * Dashboard de Progression : [frontend/src/pages/DashboardPage.tsx](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages/DashboardPage.tsx)
  * Révision des erreurs (Flashcards) : [frontend/src/pages/ReviewMistakesPage.tsx](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages/ReviewMistakesPage.tsx)
* **Infrastructure Docker :**
  * Config de dev (Django + Vite + Postgres + Ollama) : [docker-compose.yml](file:///c:/Users/bough/Documents/ecole/apocalipssi/docker-compose.yml)
  * Config de prod (Caddy reverse proxy + HTTPS) : [docker-compose.prod.yml](file:///c:/Users/bough/Documents/ecole/apocalipssi/docker-compose.prod.yml)

---

## 📌 2. Qualité de l'Architecture & Justification ADR · Barème : /3

* **ADR-001 — Choix du modèle LLM local (Llama 3.2 vs 3.1) :**
  * [docs/architecture/ADR-001-choix-modele-llm.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/architecture/ADR-001-choix-modele-llm.md)
* **ADR-002 — Mise en cache des requêtes LLM via Redis 7 :**
  * [docs/architecture/ADR-002-cache-redis.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/architecture/ADR-002-cache-redis.md)
* **Schémas d'Architecture et Diagrammes UML :**
  * Diagrammes v2 (Scale, i18n, Redis cache) : [docs/perturbations/j4/uml/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j4/uml) (PlantUML) et [docs/perturbations/j4/img/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j4/img) (PNG)
  * Diagrammes v1 (MVP) : [docs/perturbations/j1-3/uml/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j1-3/uml) et [docs/perturbations/j1-3/diagrams/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j1-3/diagrams)

---

## 📌 3. Intégration & Maîtrise d'Ollama Local · Barème : /2

* **Rapport de Benchmark des modèles (llama3.1:8b, llama3.2:3b, phi3:mini) :**
  * [docs/perturbations/j2/benchmark-report.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j2/benchmark-report.md)
* **Script d'évaluation automatique de la latence (runs de test) :**
  * [scripts/benchmark.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/scripts/benchmark.py)
* **Code d'intégration d'Ollama (séparation system/user, paramétrage) :**
  * [backend/llm/services/ollama_client.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm/services/ollama_client.py)
* **Conception du System Prompt & Validation Pydantic :**
  * [backend/llm/services/quiz_prompt.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm/services/quiz_prompt.py)

---

## 📌 4. Sécurité IA & OWASP LLM-01 (Prompt Injection) · Barème : /3

* **Note de Sécurité (OWASP LLM-01, diagnostic et mitigation) :**
  * [docs/securite/note-securite-llm01.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/securite/note-securite-llm01.md)
* **Tests unitaires adversariaux (7 scénarios pytest en CI/CD) :**
  * [backend/llm/tests/adversarial/test_prompt_injection.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm/tests/adversarial/test_prompt_injection.py)
* **Implémentation du Patch 4 Couches (Sanitization, Hardening, Validation) :**
  * Filtre regex et unicode : [backend/llm/services/quiz_prompt.py#L53-L64](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm/services/quiz_prompt.py#L53-L64)
  * Détecteur statistique de distribution des index : [backend/llm/services/quiz_prompt.py#L167-L174](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/llm/services/quiz_prompt.py#L167-L174)

---

## 📌 5. Conformité RGPD & Gestion des Données · Barème : /2

* **Droit d'accès (SAR - Droit à la portabilité Art. 15) :**
  * Serializer de collecte : [backend/accounts/export.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/accounts/export.py)
  * Bouton d'export format JSON/CSV dans le profil : [frontend/src/pages/ProfilePage.tsx](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages/ProfilePage.tsx)
* **Politique de Rétention des données d'évaluation :**
  * [docs/qualite/Politique_de_Retention.docx](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/qualite/Politique_de_Retention.docx)
* **Réponse formelle à la demande d'accès (Hugo Petit) :**
  * [docs/qualite/reponse_hugo.pdf](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/qualite/reponse_hugo.pdf)
* **Droit à l'oubli (Suppression de compte conforme) :**
  * [backend/accounts/views.py](file:///c:/Users/bough/Documents/ecole/apocalipssi/backend/accounts/views.py) (méthode de suppression liant Cascade)
* **Pages Légales (CGU, Cookies, Mentions légales, Confidentialité) :**
  * [frontend/src/pages/legal/](file:///c:/Users/bough/Documents/ecole/apocalipssi/frontend/src/pages/legal)

---

## 📌 6. Gestion Agile — Les 7 Artefacts Initiaux · Barème : /3

* **Product Vision Board :** [docs/cadrage/01-product-vision-board.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/01-product-vision-board.md)
* **Personas :** [docs/cadrage/02-personas.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/02-personas.md)
* **Customer Journey Maps (Lucas & Mme Lefèvre) :** images stockées dans [docs/perturbations/j1-3/img et maquettes/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j1-3/img%20et%20maquettes)
* **Story Map :** [docs/cadrage/04-story-map.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/04-story-map.md)
* **Release Planning :** [docs/cadrage/05-release-planning.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/05-release-planning.md)
* **Product Backlog (MoSCoW/INVEST) :** [docs/cadrage/06-product-backlog.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/06-product-backlog.md)
* **Sprint Backlog S1 :** [docs/cadrage/07-sprint-backlog-s1.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/cadrage/07-sprint-backlog-s1.md)

---

## 📌 7. Réponses aux 5 Perturbations & Qualité Dépôt · Barème : /3

* **Perturbation J1 — Persona Enseignante (Mme Lefèvre) :**
  * Dossier de décision MoSCoW : [docs/perturbations/j1/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j1)
* **Perturbation J2 — Latence LLM inacceptable :**
  * Rapport + ADR-001 : [docs/perturbations/j2/benchmark-report.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j2/benchmark-report.md)
* **Perturbation J3 — Injection OWASP LLM-01 et demande SAR :**
  * Note de sécu dans [/securite/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/securite) et export technique dans [/qualite/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/qualite)
* **Perturbation J4 — Erreurs factuelles (Audit qualité & Post-mortem blameless) :**
  * [docs/qualite/audit-quiz-postmortem.md](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/qualite/audit-quiz-postmortem.md)
* **Perturbation J4-bis — Changement d'Échelle (Scale, i18n, RGAA) :**
  * Backlog mis à jour, burndown-burnup, sprint S3 et matrice des risques : [docs/perturbations/j4/](file:///c:/Users/bough/Documents/ecole/apocalipssi/docs/perturbations/j4)
* **Qualité du Dépôt GitHub :**
  * Branches : Travail collaboratif sur branche `feat/groupe14-edututor` puis intégration propre sur `main`.
  * Commits : Usage des Conventional Commits pour assurer la traçabilité.
