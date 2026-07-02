# ADR — Choix du modèle LLM pour la génération de quiz

**Date :** 30/06/2026
**Status :** Attente validation PO
**Auteurs :** Équipe EduTutor Groupe 14

---

## Contexte

Lors du beta-test du 29/06/2026, un utilisateur a signalé un temps d'attente de 45 secondes pour la génération d'un quiz à partir d'un cours uploadé. Le sponsor a fixé un objectif de latence strict : **p95 ≤ 15 secondes pour la génération du quiz complet (10 questions)**.

Le kit initial embarque `llama3.1` (8B paramètres) comme modèle par défaut. Un benchmark méthodologique a été conduit le 30/06/2026 pour évaluer 3 modèles compatibles Ollama sur le même serveur de référence (Ubuntu 22.04, NVIDIA RTX 4090, CUDA 12.2), protocole : 5 runs × même cours de référence × même machine.

---

## Options envisagées

| Modèle            | p50      | p95      | Qualité /5 | VRAM       |
| ----------------- | -------- | -------- | ---------- | ---------- |
| llama3.1 (8B)     | 18.8s    | 21.4s    | 4.5/5      | 6.5 Go     |
| **llama3.2 (3B)** | **6.6s** | **7.9s** | **3.8/5**  | **2.8 Go** |
| phi3:mini (3.8B)  | 7.4s     | 9.2s     | 3.5/5      | 3.1 Go     |

---

## Décision retenue

**Basculer de `llama3.1` vers `llama3.2`** pour la génération de quiz en production.

---

## Justification

`llama3.2` offre le meilleur ratio vitesse / qualité / empreinte mémoire :

- **Latence** : p95 = 7.9s, soit 2× sous l'objectif fixé — marge confortable pour absorber les pics de charge.
- **Qualité** : 3.8/5 — suffisant pour le MVP, les questions générées sont cohérentes avec le cours fourni.
- **VRAM** : 2.8 Go, contre 6.5 Go pour `llama3.1` — permet de servir plusieurs utilisateurs en parallèle sur le même serveur.

`phi3:mini` a été écarté malgré une latence similaire : qualité inférieure (3.5/5) sur les cours de niveau Master, avec des distracteurs parfois peu crédibles.

`llama3.1` est écarté du flux interactif en raison de son empreinte mémoire, mais reste une option pertinente pour un mode génération différée (non-interactif) à explorer en Release 2.

---

## Conséquences

**Positives**

- Latence divisée par 2 par rapport à `llama3.1` en conditions de charge.
- Déploiement multi-tenant facilité grâce à la faible empreinte VRAM.
- Conformité RGPD maintenue : Ollama local, aucune donnée ne quitte le serveur.

**Négatives**

- Légère baisse de qualité de génération par rapport à `llama3.1` (3.8/5 vs 4.5/5).
- Risque de questions moins pertinentes sur des cours très spécialisés (droit, médecine).

**À surveiller**

- Qualité perçue par les utilisateurs lors des prochains beta-tests.
- Réévaluation de `llama3.1` en mode différé pour les enseignants souhaitant une qualité maximale (Release 2).
