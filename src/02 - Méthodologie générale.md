---
title: Approches non paramétriques
---

## Méthodologie générale

## Notations et conventions

## Définitions des notations mathématiques utilisées.

## Mesures de performance et critères d’évaluation

Dans le cadre d'une classification binaire, on peut définir les termes suivants :

Matrice de confusion
: La matrice de confusion est une matrice 2x2 qui permet de visualiser les performances d'un algorithme de classification. Elle contient quatre éléments :

- les vrais positifs (TP) : les emails correctement prédits comme spam
- les faux positifs (FP) : les emails prédits comme spam alors qu'ils sont en réalité des ham
- les vrais négatifs (TN) : les emails correctement prédits comme ham
- les faux négatifs (FN) : les emails prédits comme ham alors qu'ils sont en réalité des spam

Exactitude
: L'exactitude (ou en anglais accuracy) mesure la proportion de prédictions correctes parmi toutes les prédictions effectuées par le modèle. Elle est définie par : $ \text{Exactitude} = \frac{TP + TN}{TP + TN + FP + FN} $

Précision
: La précision (ou en anglais precision) mesure la proportion de vrais positifs parmi tous les éléments identifiés comme positifs par le modèle. Elle permet d'évaluer la capacité du modèle à éviter les faux positifs et est définie par : $ \text{Précision} = \frac{TP}{TP + FP} $

Rappel
: Le rappel (ou en anglais recall) mesure la proportion de vrais positifs correctement identifiés parmi tous les éléments réellement positifs. Il permet d'évaluer la capacité du modèle à détecter tous les cas positifs et est défini par : $ \text{Rappel} = \frac{TP}{TP + FN} $

F1-score
: Le F1-score est la moyenne harmonique de la précision et du rappel ($ \text{F1-Score} = 2 \times \frac{\text{Précision} \times \text{Rappel}}{\text{Précision} + \text{Rappel}} $). Il permet d'évaluer la performance globale d'un modèle en équilibrant ces deux métriques. Un score proche de 1 indique une excellente performance.

Weighted Average F1-score
: Le F1-score moyen pondéré est une mesure utilisée pour évaluer les performances d'un modèle de classification binaire. Il prend en compte le déséquilibre des classes en calculant une moyenne pondérée des F1-scores de chaque classe, où les poids sont proportionnels au nombre d'instances de chaque classe. Cela permet d'obtenir une évaluation plus représentative des performances globales du modèle, en particulier lorsque les classes sont déséquilibrées.

La grande partie des modèles de classifications binaires produisent en sortie un chiffre entre 0 et 1, qui peut être vu comme la probabilité que l'observation appartienne à la classe positive. 

Pour transformer ces chiffres en classes, on utilise un seuil de décision. Si la probabilité est supérieure à ce seuil, l'observation est classifiée en tant que classe positive, sinon elle est classifiée en tant que classe négative.

L'analyse des probabilités prédites par un modèle permet de déterminer le seuil de décision optimal pour maximiser les performances du modèle. La plupart des modèles de classification binaire utilisent un seuil de décision par défaut de 0.5, mais ce seuil peut être ajusté pour améliorer les performances du modèle en fonction des besoins spécifiques de l'application.

Par exemple, dans le cas de la détection de maladies, il est préférable de privilégier un taux de faux positifs élevé pour éviter de passer à côté de cas positifs. Dans ce cas, le seuil de décision peut être abaissé pour augmenter le rappel du modèle, même au détriment de la spécificité.

L'analyse des probabilités prédites par un modèle permet aussi de remarquer la capacité du modèle à distinguer plus ou moins bien les classes positives et négatives. Une probabilité de $0.9$ pour une observation positive signifie que le modèle est très sûr de sa prédiction, tandis qu'une probabilité de $0.6$ indique une prédiction moins certaine.

Certains graphiques permettent de visualiser les performances des modèles selon ce seuil :

Courbe de précision-rappel
: La courbe de précision-rappel affiche la précision et le rappel en fonction du seuil de décision. Elle permet d'évaluer la performance du modèle en fonction de ces deux métriques. Plus la courbe est proche du coin supérieur droit, meilleure est la performance du modèle.

Courbe ROC (Receiver Operating Characteristic)
: La courbe ROC permet d'évaluer la performance d'un classificateur binaire, c’est-à-dire un système conçu pour diviser des éléments en deux catégories distinctes en fonction de certaines caractéristiques. Cette mesure est illustrée par une courbe qui affiche le taux de vrais positifs en fonction du taux de faux positifs. Elle permet d'observer la capacité du modèle à correctement distinguer les classes positives et négatives et de visualier l'arbitrage réalisé entre les taux de faux positifs et de vrais négatifs. De plus l'aire sous la courbe (AUC) permet de quantifier la performance du modèle : plus la valeur est proche de 1, plus le modèle est performant pour déterminer les classes positives et négatives.

## Définitions (accuracy, F1-score, AUC-ROC, etc.).

## Explication de la pertinence des métriques choisies.

## Protocole expérimental global

Le schéma ci-dessous illustre le processus complet d'entraînement des modèles, de la préparation des données à l'évaluation des performances.

:::{image} ./assets/echantillon_entrainement.jpg
:width: 450px
:alt: Pipeline of model training
:::

## Organisation des ensembles de données

Le jeu de données est divisé en deux parties : un ensemble d'entraînement et un ensemble de test. L'ensemble d'entraînement est utilisé pour entraîner les modèles et ajuster les hyperparamètres, tandis que l'ensemble de test est utilisé pour évaluer les performances des modèles sur des données non vues.

## Validation croisée 

La validation croisée (en anglais cross-validation) est une méthode d'évaluation qui consiste à diviser l'ensemble des données en plusieurs sous-ensembles appelés "plis" (folds). À chaque itération, un pli est utilisé pour tester le modèle, tandis que les autres plis servent à l'entraîner. Ce processus se répète pour chaque pli, de sorte que chaque sous-ensemble est utilisé à la fois pour l'entraînement et pour le test. 

:::{image} ./assets/processus_validation_croisee.jpg
:width: 550px
:alt: K-Fold Cross Validation
:::

Cette méthode permet d'obtenir une évaluation plus robuste des performances du modèle en réduisant le risque de surajustement et en prenant en compte la variabilité des données. Elle est particulièrement utile lorsque l'ensemble de données est de petite taille ou que les classes sont déséquilibrées.

## Stratégie d’optimisation des hyperparamètres

Les données d'entraînement sont utilisées pour ajuster les hyperparamètres des modèles. Les hyperparamètres sont des paramètres qui ne sont pas appris par le modèle lui-même, mais qui doivent être définis par l'utilisateur avant l'entraînement. Ils permettent de contrôler le comportement du modèle et d'optimiser ses performances.

On utilise la validation croisée pour évaluer les performances du modèle pour différentes valeurs des hyperparamètres, puis on sélectionne les valeurs qui maximisent les performances du modèle. Cette approche permet de trouver les hyperparamètres optimaux pour chaque modèle et d'obtenir des performances optimales.