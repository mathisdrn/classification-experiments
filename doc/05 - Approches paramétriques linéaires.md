---
title: Approches paramétriques linéaires
---

## Introduction

Décrire ce que sont les approches paramètriques linéaires

## Régression logistique

La régression logistique est une méthode d'apprentissage supervisé largement utilisée pour la classification binaire. Elle modélise la probabilité qu'une observation appartienne à une des deux classes en utilisant une fonction logistique (ou sigmoïde) pour transformer une combinaison linéaire des caractéristiques en une probabilité. La fonction sigmoïde prend une valeur comprise entre 0 et 1, ce qui permet de prédire l'appartenance à une classe en appliquant un seuil, généralement 0,5. L'objectif de l'algorithme est d'ajuster les coefficients de la combinaison linéaire en maximisant la vraisemblance des observations données.

Avantages :

- Facile à interpréter grâce aux coefficients qui indiquent l'influence des variables explicatives.
- Efficace pour des problèmes de classification linéairement séparables.
- Performant même lorsque les classes sont partiellement chevauchées, tant que la relation est linéaire.

Inconvénients :

- Ne fonctionne pas bien lorsque la relation entre les variables explicatives et la probabilité d'appartenance à une classe est non linéaire.
- Peut être sensible aux valeurs aberrantes, nécessitant un nettoyage préalable des données.
- Peut nécessiter une régularisation (comme la pénalisation L1 ou L2) pour éviter le surajustement dans le cas de nombreuses variables explicatives.

## Support Vector Machine

L'algorithme Support Vector Machine (SVM) est une méthode d'apprentissage supervisé utilisée pour résoudre des problèmes de régression et de classification. En découle deux implémentations algorithmiques : l'une pour la régression (SVR) et l'autre pour la classification (SVC).

L'algorithme SVM repose sur le concept des marges maximales, c'est-à-dire qu'il cherche à séparer deux classes dans l'espace des caractéristiques en traçant un hyperplan qui maximise la distance (ou la marge) entre les points de chaque classe les plus proches de cette hyperplan, appelés vecteurs de support. Lorsque les classes ne sont pas linéairement séparables, l'algorithme utilise des noyaux pour projeter les données dans un espace de dimension supérieure où elles peuvent être séparées.

Avantages :

- Efficace dans des espaces de grande dimension.
- Peut être modifié pour des cas non linéaires grâce aux fonctions noyau.
- Utilise seulement les vecteurs de support, ce qui le rend plus économe en mémoire.

Inconvénients :

- Peut être sensible aux choix des paramètres (comme C et le type de noyau).
- Moins performant avec de très grands ensembles de données ou quand les classes sont fortement chevauchées.