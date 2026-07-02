# Perturbation J1 — Persona Mme Lefèvre

**Date :** 29/06/2026 14h00 · **Équipe :** EduTutor Groupe 14

---

## Contexte de la perturbation

Le Product Owner annonce l'émergence d'une cible secondaire prioritaire : **Mme Lefèvre**, enseignante, dont les besoins n'avaient pas été formalisés dans les artefacts initiaux. Cette perturbation oblige à étendre le périmètre des personas et à réévaluer le backlog.

---

## Persona — Mme Lefèvre, enseignante de biologie

**"Je ne veux pas que mes cours ou les données de mes élèves finissent sur des serveurs américains."**

| Attribut | Détail |
|----------|--------|
| Prénom | Marie-Christine Lefèvre |
| Âge | 44 ans |
| Poste | Professeure de biologie, lycée public, Île-de-France |
| Expérience tech | Basique-intermédiaire (ENT, PDF, emails, vidéoprojecteur) |
| Contexte | 4 classes, ~120 élèves, charge de travail élevée |
| Appareils | PC fixe salle des profs, tablette personnelle |

### Ce qu'elle cherche
- Générer des QCM à partir de **son propre cours** (PDF fourni par elle)
- Pouvoir **relire et valider** les questions avant de les donner à ses élèves
- Une solution **RGPD** : elle refuse que les données de ses élèves sortent de l'établissement
- Interface **simple** : pas de formation nécessaire

### Ses frustrations actuelles
- Les outils grand public génèrent des questions "génériques" hors-programme
- ChatGPT invente des faits biologiques incorrects (hallucinations)
- Elle n'a pas confiance dans les solutions cloud (données envoyées hors UE)

### Ses critères de succès
- Questions traçables au cours qu'elle a fourni (RAG)
- Interface en 3 clics : upload → générer → relire
- Badge ou mention RGPD visible dans l'interface

### Citation représentative
> "Si une question est fausse, c'est moi qui ai l'air incompétente devant mes élèves. Je ne peux pas me permettre ça."

---

## Impact sur le produit

Mme Lefèvre valide et renforce trois des différenciateurs d'EduTutor IA :
1. **RAG** — génération ancrée dans le document, pas dans la mémoire du LLM
2. **RGPD local-first** — Ollama local, aucune donnée hors serveur
3. **Qualité pédagogique** — questions vérifiables, pas d'hallucination
