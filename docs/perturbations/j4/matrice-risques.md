# Analyse de risques — Perturbation J4

**Date :** 02/07/2026 · **Équipe :** EduTutor Groupe 14
**Contexte :** adoption nationale, millions d'utilisateurs, condition RGAA de l'État

---

## Matrice probabilité × impact

Échelle : **1** (faible) → **3** (élevé) · Score = Probabilité × Impact

| # | Risque | Probabilité | Impact | Score | Niveau |
|---|--------|-------------|--------|-------|--------|
| R1 | Surcharge serveur lors d'un pic de trafic (passage télé, rentrée) | 3 | 3 | **9** | Critique |
| R2 | Qualité des quiz dégradée en i18n (hallucinations dans d'autres langues) | 3 | 2 | **6** | Élevé |
| R3 | Non-conformité RGAA bloquant l'adoption institutionnelle | 2 | 3 | **6** | Élevé |
| R4 | Panne Ollama en production sans mécanisme de secours | 2 | 3 | **6** | Élevé |
| R5 | Coûts d'infrastructure non maîtrisés post-levée de fonds | 1 | 3 | **3** | Modéré |
| R6 | Fuite de données utilisateurs (violation RGPD à grande échelle) | 1 | 3 | **3** | Modéré |

---

## Détail des risques prioritaires (score ≥ 6)

### R1 — Surcharge serveur lors d'un pic de trafic · Score 9 · Critique

**Description :** Un passage médiatique (TV, presse) ou la rentrée scolaire peut générer des pics à 50 000+ requêtes simultanées, faisant tomber le service.

**Causes racines :**
- Architecture mono-instance sans autoscaling
- Ollama ne supporte pas la parallélisation native
- Aucun cache sur les requêtes LLM identiques

**Actions préventives :**

| Action | US associée | Estimation | MoSCoW |
|--------|-------------|-----------|--------|
| Tests de charge avec k6 (simulation 10 000 utilisateurs) | US-30 | 5 pts | Must |
| Cache Redis sur les réponses LLM (TTL 24h) | US-31 | 8 pts | Must |
| Autoscaling horizontal (Kubernetes HPA) | — | 13 pts | Should |

---

### R2 — Qualité des quiz dégradée en i18n · Score 6 · Élevé

**Description :** Les LLM open-source (llama3.2) ont des performances inégales en dehors du français et de l'anglais. Un quiz généré en espagnol peut contenir des hallucinations ou des mélanges de langues.

**Causes racines :**
- llama3.2 est optimisé pour l'anglais, moins performant en espagnol
- Aucun test de qualité multilingue n'existe aujourd'hui

**Actions préventives :**

| Action | US associée | Estimation | MoSCoW |
|--------|-------------|-----------|--------|
| Paramètre de langue explicite dans le system prompt | US-29 | 5 pts | Should |
| Jeu de tests de qualité multilingue (fr/en/es) | — | 3 pts | Should |
| Fallback sur un modèle plus performant en i18n (ex : Claude Haiku) | US-32 | 5 pts | Could |

---

### R3 — Non-conformité RGAA bloquant l'adoption institutionnelle · Score 6 · Élevé

**Description :** L'État conditionne l'adoption à la conformité RGAA (norme obligatoire pour les services publics numériques). Sans audit et correctifs, le contrat tombe.

**Causes racines :**
- L'interface a été développée sans contrainte d'accessibilité initiale
- Pas d'audit réalisé à ce jour

**Actions préventives :**

| Action | US associée | Estimation | MoSCoW |
|--------|-------------|-----------|--------|
| Audit RGAA initial + rapport priorisé | US-25 | 8 pts | Must |
| Correctifs contrastes + focus visible | US-26 | 5 pts | Must |
| Navigation clavier complète | US-27 | 3 pts | Must |

---

### R4 — Panne Ollama sans mécanisme de secours · Score 6 · Élevé

**Description :** Ollama tourne en local sur le serveur. Une panne matérielle, une mise à jour ratée ou une saturation GPU rend la génération de quiz totalement indisponible — sans fallback.

**Causes racines :**
- Dépendance unique à Ollama
- Aucun circuit breaker ni fournisseur de secours configuré

**Actions préventives :**

| Action | US associée | Estimation | MoSCoW |
|--------|-------------|-----------|--------|
| Fournisseur LLM de secours configurable (OpenAI ou Claude) | US-32 | 5 pts | Could |
| Monitoring Ollama avec alerte automatique (Prometheus) | — | 3 pts | Should |
| Health check endpoint `/api/llm/health/` | — | 1 pt | Should |

---

## Actions préventives intégrées au backlog

Récapitulatif des US créées ou enrichies suite à l'analyse de risques :

| US | Risque couvert | Estimation | MoSCoW R3 |
|----|---------------|-----------|-----------|
| US-25 Audit RGAA | R3 | 8 pts | Must |
| US-26 Contrastes + focus | R3 | 5 pts | Must |
| US-27 Navigation clavier | R3 | 3 pts | Must |
| US-28 Externalisation i18n | R2 | 8 pts | Must |
| US-29 Langue LLM à la volée | R2 | 5 pts | Should |
| US-30 Tests de charge | R1 | 5 pts | Must |
| US-31 Cache Redis | R1 | 8 pts | Must |
| US-32 LLM de secours | R4 | 5 pts | Could |
