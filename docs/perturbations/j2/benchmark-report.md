# Rapport de Benchmark LLM — EduTutor IA

**Perturbation J2 · Décision technique**
Date : 30/06/2026 · Équipe EduTutor IA Groupe 14

---

## Contexte

Suite au retour beta-test reçu le 30/06 au matin, un étudiant M2 a signalé une latence de 45 secondes lors de la génération d'un quiz à partir d'un cours d'algorithmie. Le sponsor exige un temps de génération acceptable (objectif : **p95 ≤ 15 secondes**) avant la fin de la journée.

Ce benchmark vise à identifier le modèle LLM local offrant le meilleur compromis latence / qualité tout en respectant la contrainte RGPD (Ollama local, aucune donnée sortant du serveur).

---

## Protocole

| Paramètre           | Valeur                                           |
| ------------------- | ------------------------------------------------ |
| Serveur             | Ubuntu 22.04 LTS                                 |
| GPU                 | NVIDIA RTX 4090 · 24 Go VRAM                     |
| Backend             | Ollama 0.30.11 · CUDA 12.2                       |
| Nombre de runs      | 5 par modèle                                     |
| Cours de référence  | Photosynthèse · ~150 mots · texte brut           |
| Prompt              | Génération de 10 QCM en JSON (quiz complet)      |
| Métrique principale | Latence p50 (médiane) et p95 (pire cas réaliste) |

> Le p95 est retenu comme métrique de référence : il représente l'expérience des 5 % d'utilisateurs les moins bien servis, donc le vrai plancher de qualité perçue.

---

## Modèles testés

| Modèle    | Paramètres | Taille disque | VRAM requise |
| --------- | ---------- | ------------- | ------------ |
| llama3.1  | 8B         | 4.7 Go        | ~6.5 Go      |
| llama3.2  | 3B         | 2.0 Go        | ~2.8 Go      |
| phi3:mini | 3.8B       | 2.3 Go        | ~3.1 Go      |

---

## Résultats

### Latences mesurées (génération 10 QCM, quiz complet)

| Modèle    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **p50**   | **p95**   |
| --------- | ----- | ----- | ----- | ----- | ----- | --------- | --------- |
| llama3.1  | 18.2s | 17.6s | 19.1s | 21.4s | 18.8s | **18.8s** | **21.4s** |
| llama3.2  | 6.8s  | 6.3s  | 6.5s  | 7.9s  | 6.6s  | **6.6s**  | **7.9s**  |
| phi3:mini | 7.4s  | 7.1s  | 7.6s  | 9.2s  | 7.3s  | **7.4s**  | **9.2s**  |

### Tableau récapitulatif

| Modèle    | p50   | p95   | Objectif ≤ 15s      | Qualité /5 |
| --------- | ----- | ----- | ------------------- | ---------- |
| llama3.1  | 18.8s | 21.4s | **✗ HORS OBJECTIF** | 4.5/5      |
| llama3.2  | 6.6s  | 7.9s  | **✓ OK**            | 3.8/5      |
| phi3:mini | 7.4s  | 9.2s  | **✓ OK**            | 3.5/5      |

### Qualité subjective (3 testeurs, grille 5 critères)

Critères évalués : pertinence des questions, correction des réponses, clarté des formulations, cohérence avec le cours, format JSON valide.

| Modèle    | Testeur 1 | Testeur 2 | Testeur 3 | Moyenne   |
| --------- | --------- | --------- | --------- | --------- |
| llama3.1  | 4.6/5     | 4.4/5     | 4.5/5     | **4.5/5** |
| llama3.2  | 3.9/5     | 3.8/5     | 3.7/5     | **3.8/5** |
| phi3:mini | 3.6/5     | 3.4/5     | 3.5/5     | **3.5/5** |

---

## Analyse des trade-offs

**llama3.1 (8B)**
Meilleure qualité de génération (4.5/5) mais p95 à 21.4s — hors objectif. Trop lourd pour une utilisation interactive. Éliminé du flux temps réel.

**phi3:mini (3.8B)**
Rapide (p95 = 9.2s) et léger (2.3 Go). Qualité légèrement inférieure à llama3.2 sur des cours complexes : tendance à générer des distracteurs peu crédibles sur les questions de niveau Master.

**llama3.2 (3B)**
Meilleur ratio vitesse / qualité : p95 = 7.9s (2× sous l'objectif), qualité 3.8/5 — acceptable pour le MVP. Empreinte mémoire raisonnable (2.8 Go VRAM), compatible avec un déploiement multi-tenant.

---

## Décision

**Modèle retenu : llama3.2**

p50 = 6.6s · p95 = 7.9s · qualité 3.8/5 · VRAM 2.8 Go

---

## Points de vigilance

- La qualité de llama3.2 sur des cours techniques très spécialisés (droit, médecine) devra être réévaluée avant la Release 2.
- llama3.1 reste pertinent comme option qualité pour un mode "génération différée" (non-interactif) à explorer en Release 2.
- Les mesures sont à rejouer après tout changement d'infrastructure (changement de GPU, montée de version Ollama).
