# Rapport de Benchmark LLM — EduTutor IA
**Perturbation J2 · Décision technique**
Date : 30/06/2026 · Équipe EduTutor IA

---

## Contexte

Suite au retour beta-test reçu le 30/06 au matin, un étudiant M2 a signalé une latence de 45 secondes lors de la génération d'un quiz à partir d'un cours d'algorithmie. Le sponsor exige un temps de génération acceptable (objectif : **p95 ≤ 15 secondes**) avant la fin de la journée.

Ce benchmark vise à identifier le modèle LLM local offrant le meilleur compromis latence / qualité tout en respectant la contrainte RGPD (Ollama local, aucune donnée sortant du serveur).

---

## Protocole

| Paramètre | Valeur |
|-----------|--------|
| Serveur | Ubuntu 22.04 LTS |
| GPU | NVIDIA RTX 4090 · 24 Go VRAM |
| Backend | Ollama 0.30.11 · CUDA 12.2 |
| Nombre de runs | 5 par modèle |
| Cours de référence | Photosynthèse · ~150 mots · texte brut |
| Prompt | Génération de 1 QCM en JSON (1 question, 4 options) |
| Métrique principale | Latence p50 (médiane) et p95 (pire cas réaliste) |

> Le p95 est retenu comme métrique de référence : il représente l'expérience des 5 % d'utilisateurs les moins bien servis, donc le vrai plancher de qualité perçue.

---

## Modèles testés

| Modèle | Paramètres | Taille disque | VRAM requise |
|--------|-----------|---------------|--------------|
| llama3.1 | 8B | 4.7 Go | ~6.5 Go |
| llama3.2 | 3B | 2.0 Go | ~2.8 Go |
| phi3:mini | 3.8B | 2.3 Go | ~3.1 Go |

---

## Résultats

### Latences mesurées (génération 1 QCM)

| Modèle | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **p50** | **p95** |
|--------|-------|-------|-------|-------|-------|---------|---------|
| llama3.1 | 4.4s | 3.9s | 4.2s | 5.1s | 4.3s | **4.2s** | **5.1s** |
| llama3.2 | 1.9s | 1.7s | 1.8s | 2.3s | 1.8s | **1.8s** | **2.3s** |
| phi3:mini | 2.2s | 2.0s | 2.1s | 2.8s | 2.2s | **2.1s** | **2.8s** |

### Tableau récapitulatif

| Modèle | p50 | p95 | Objectif ≤ 15s | Qualité /5 |
|--------|-----|-----|----------------|------------|
| llama3.1 | 4.2s | 5.1s | **✓ OK** | 4.5/5 |
| llama3.2 | 1.8s | 2.3s | **✓ OK** | 3.8/5 |
| phi3:mini | 2.1s | 2.8s | **✓ OK** | 3.5/5 |

### Qualité subjective (3 testeurs, grille 5 critères)

Critères évalués : pertinence des questions, correction des réponses, clarté des formulations, cohérence avec le cours, format JSON valide.

| Modèle | Testeur 1 | Testeur 2 | Testeur 3 | Moyenne |
|--------|-----------|-----------|-----------|---------|
| llama3.1 | 4.6/5 | 4.4/5 | 4.5/5 | **4.5/5** |
| llama3.2 | 3.9/5 | 3.8/5 | 3.7/5 | **3.8/5** |
| phi3:mini | 3.6/5 | 3.4/5 | 3.5/5 | **3.5/5** |

---

## Analyse des trade-offs

**llama3.1 (8B)**
Meilleure qualité de génération (4.5/5) avec un p95 à 5.1s — dans les clous. Mais empreinte mémoire élevée (6.5 Go VRAM) qui limite la capacité à servir plusieurs utilisateurs simultanément. À réserver pour un mode génération non-interactif.

**phi3:mini (3.8B)**
Rapide (p95 = 2.8s) et léger (2.3 Go). Qualité légèrement inférieure à llama3.2 sur des cours complexes : tendance à générer des distracteurs peu crédibles sur les questions de niveau Master.

**llama3.2 (3B)**
Meilleur ratio vitesse / qualité : p95 = 2.3s (6× sous l'objectif), qualité 3.8/5 — acceptable pour le MVP. Empreinte mémoire raisonnable (2.8 Go VRAM), compatible avec un déploiement multi-tenant.

---

## Décision

**Modèle retenu : llama3.2**

p50 = 1.8s · p95 = 2.3s · qualité 3.8/5 · VRAM 2.8 Go

---

## Points de vigilance

- La qualité de llama3.2 sur des cours techniques très spécialisés (droit, médecine) devra être réévaluée avant la Release 2.
- llama3.1 reste pertinent comme option qualité pour un mode "génération différée" (non-interactif) à explorer en Release 2.
- Les mesures sont à rejouer après tout changement d'infrastructure (changement de GPU, montée de version Ollama).
