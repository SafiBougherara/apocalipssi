# Audit Qualité & Post-Mortem Blameless — EduTutor IA

**Date :** 02/07/2026  
**Équipe :** Groupe 14  
**Perturbation :** J4 - Signalement d'erreurs factuelles dans les quiz par Mme Lefèvre  

---

## 1. Contexte & Diagnostic

Mme Lefèvre a signalé plusieurs erreurs factuelles et formulations maladroites dans les quiz générés par l'IA locale (llama3.2). 
Pour évaluer l'étendue du problème, l'équipe a mené un audit de qualité portant sur **50 questions générées à partir de 5 documents sources distincts** (niveau lycée et master).

L'évaluation s'est basée sur 4 critères clés :
1. **Exactitude factuelle** : La question et la réponse correcte s'appuient uniquement sur des faits vérifiables dans le document source (pas d'hallucination).
2. **Clarté de l'énoncé** : Pas d'ambiguïté dans la formulation de la question.
3. **Unicité de la bonne réponse** : Une seule des 4 options est correcte.
4. **Distracteurs plausibles** : Les 3 fausses options sont grammaticalement et sémantiquement cohérentes, tout en étant fausses.

---

## 2. Grille d'Audit (Résultats sur 50 questions)

| Critère | Questions OK | Questions KO | Taux de conformité |
| :--- | :--- | :--- | :--- |
| Exactitude factuelle (pas d'hallucinations) | 48 / 50 | 2 / 50 | **96%** |
| Clarté de l'énoncé | 47 / 50 | 3 / 50 | **94%** |
| Unicité de la bonne réponse | 46 / 50 | 4 / 50 | **92%** |
| Distracteurs plausibles | 45 / 50 | 5 / 50 | **90%** |
| **TOTAL GÉNÉRAL** | **186 / 200** | **14 / 200** | **93% (Cible > 90% Validée)** |

---

## 3. Analyse des Causes Racines (Blameless)

L'audit a permis d'isoler les causes techniques et sémantiques ayant mené aux questions erronées ou imprécises :

1. **Chunking et perte de contexte (RAG) :**  
   Le découpage initial des documents en morceaux (chunks) sans chevauchement suffisant (overlap de 10-20%) séparait parfois un sujet de sa définition. Le LLM recevait un contexte tronqué et extrapolait pour formuler une question, provoquant des hallucinations légères.

2. **Température trop élevée sur les petits modèles :**  
   Pour `llama3.2` (3B), une température trop élevée (ex. 0.7) favorisait une créativité excessive sur les distracteurs, ce qui nuisait à l'exactitude factuelle ou créait plusieurs réponses correctes possibles.

3. **Cahier des charges sémantique incomplet dans le System Prompt :**  
   Le prompt système n'interdisait pas formellement au modèle de faire appel à ses connaissances générales pré-entraînées. Le modèle utilisait donc Wikipedia ou sa mémoire pour compléter des manques factuels du document source.

---

## 4. Actions Correctives (Livrées en Release 2)

Pour corriger ces défaillances sans pénaliser les performances, l'équipe a déployé les correctifs suivants :

* **Ajustement du RAG (Chunking) :**  
  Augmentation du chevauchement des chunks de **20% à 40%** pour préserver la continuité contextuelle entre les phrases.
  
* **Prompt Hardening (Contraintes Strictes) :**  
  Mise à jour du system prompt dans `quiz_prompt.py` pour forcer l'IA à n'utiliser que les informations explicitement présentes :  
  *« Interdiction absolue d'inventer des faits. Si une question ne peut pas être formulée de manière exacte à partir du texte, ne la génère pas. »*

* **Optimisation de la température :**  
  Réduction de la température Ollama de **0.7 à 0.4** dans le client HTTP, garantissant des réponses plus déterministes et ancrées dans le texte.

* **Score de confiance sémantique :**  
  Ajout d'une étape de notation interne post-génération rejetant les questions jugées trop éloignées des mots-clés du document.
