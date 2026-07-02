# ADR-002 — Mise en cache des requêtes LLM avec Redis

Date : 2026-07-02 | Statut : Accepté | Décideurs : Équipe EduTutor Groupe 14

## Contexte

Dans le cadre de la perturbation J4 (échelle et adoption nationale), l'application doit être capable d'absorber jusqu'à 10 000 utilisateurs simultanés sans dégradation de la latence (cible : p95 < 15s). 
Ollama étant un service gourmand en CPU/GPU et gérant difficilement la parallélisation massive nativement, appeler le LLM pour chaque génération de quiz sur un même texte de cours sature rapidement les ressources serveur.
De nombreux étudiants travaillent souvent sur les mêmes cours au même moment (par exemple, avant un examen ou pendant un cours).

## Options évaluées

1. **Option 1 : Cache applicatif en mémoire Django (Local Memory Cache)**
   - *Avantages :* Très simple à configurer (aucun service externe requis).
   - *Inconvénients :* Non persistant, non partagé entre plusieurs processus/workers Gunicorn ou conteneurs répliqués.

2. **Option 2 : Base de données PostgreSQL pour le cache**
   - *Avantages :* Pas de nouveau service à maintenir (Postgres est déjà dans la stack).
   - *Inconvénients :* Les opérations d'écriture/lecture de textes volumineux rajoutent de la charge sur la base relationnelle principale, ralentissant les autres opérations transactionnelles.

3. **Option 3 : Cache distribué en mémoire avec Redis (Retenu)**
   - *Avantages :* Très performant (< 10ms d'accès), persistant, partagé entre tous les conteneurs Django, expire automatiquement via TTL, soulage totalement Ollama pour les cours déjà traités.
   - *Inconvénients :* Ajoute un nouveau conteneur `redis` à la stack Docker Compose et demande de gérer les dépendances `django-redis` et les connexions réseau.

## Décision

Nous choisissons d'intégrer **Redis 7** comme service de cache distribué pour les réponses LLM.
La clé de cache est calculée par le hash SHA-256 de la combinaison : `hash(source_text + preferred_language)`.
Le Time-To-Live (TTL) est fixé par défaut à **24 heures** (configurable via les variables d'environnement).

## Conséquences

### Positives
- **Réduction drastique de la latence :** Pour un cours déjà traité (Cache Hit), le quiz est renvoyé en < 100ms au lieu de 7.9s.
- **Préservation des ressources serveur :** Soulagement du GPU/CPU qui fait tourner Ollama.
- **Autoscaling facilité :** Plusieurs instances Django partagent le même cache Redis.

### Négatives
- Ajout d'un service Redis dans `docker-compose.yml` (complexité d'infrastructure augmentée).
- Ajout de la dépendance `django-redis` dans `requirements.txt`.
