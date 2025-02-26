---
title: Approches non linéaires
---

## AdaBoost (Adaptive Boosting)

L'algorithme AdaBoost (Adaptive Boosting) est une méthode d’apprentissage supervisé utilisée principalement pour la classification. Il appartient à la famille des méthodes d’ensemble (ensemble learning) et fonctionne en combinant plusieurs classificateurs faibles (souvent des arbres de décision de profondeur 1, appelés stumps) pour créer un modèle puissant et robuste.

AdaBoost fonctionne en attribuant un poids à chaque observation et en entraînant une série de classificateurs faibles de manière itérative. À chaque itération, les erreurs des modèles précédents sont amplifiées : les observations mal classées reçoivent un poids plus élevé pour que le modèle suivant se concentre davantage sur elles. La prédiction finale est obtenue par un vote pondéré des classificateurs.

Avantages :

-Améliore la précision en combinant plusieurs modèles faibles.

-Fonctionne bien sur des données bruitées et complexes.

-Peut être utilisé avec différents modèles de base (arbres, SVM, etc.).


Inconvénients :

-Sensible aux données bruitées et aux outliers, qui peuvent être sur-appris.

-Peut être lent si le nombre d’itérations est élevé.

-Nécessite un bon choix de l’algorithme de base pour éviter l’overfitting.


##Early Stopping AdaBoost

L'algorithme Early Stopping AdaBoost est une variante d'AdaBoost qui introduit un critère d’arrêt anticipé pour éviter l’overfitting. Dans la version classique d'AdaBoost, le modèle continue d'ajouter des classificateurs faibles jusqu'à atteindre un nombre prédéfini d’itérations, même si la performance commence à se dégrader sur les données de validation.

Early Stopping AdaBoost surveille la performance du modèle à chaque itération et arrête l'entraînement lorsqu'une dégradation est détectée, généralement en suivant l'erreur sur un ensemble de validation. Cette approche permet d'éviter une complexité inutile et améliore la généralisation sur de nouvelles données.

Avantages :

-Réduit le risque d'overfitting en arrêtant l'entraînement au bon moment.

-Diminue le temps d'exécution en évitant des itérations inutiles.

-Peut améliorer la performance sur des données bruitées.


Inconvénients :

-Nécessite un ensemble de validation pour surveiller la performance.

-Le choix du critère d'arrêt peut être délicat et nécessite des ajustements.

-Peut ne pas être optimal si l'arrêt est déclenché trop tôt, empêchant le modèle d'atteindre son plein potentiel.