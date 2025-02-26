---
title: Approches non paramétriques
---
## Algorithme des k plus proches voisins
L'algorithme k-Nearest Neighbors (KNN) est une méthode d'apprentissage supervisé utilisée pour la classification et la régression. Il est basé sur le principe que des objets proches dans l’espace des caractéristiques ont tendance à appartenir à la même classe ou à avoir des valeurs similaires.

KNN fonctionne en attribuant une classe à un point inconnu en fonction des  voisins les plus proches dans l’ensemble d’entraînement. La classification se fait par vote majoritaire (la classe la plus fréquente parmi les  voisins), tandis que la régression prend généralement la moyenne des valeurs des voisins.

Avantages :

-Simple à comprendre et à implémenter.

-Aucune phase d’apprentissage : l’algorithme s’adapte directement aux nouvelles données.

-Performant sur des jeux de données de petite taille et bien séparables.


Inconvénients :

-Sensible au choix de  et à la métrique de distance.

-Lourd en calcul pour de grands ensembles de données, car il nécessite le calcul des distances à chaque prédiction.

-Moins performant si les données contiennent beaucoup de dimensions non pertinentes.


## Distance-Weighted k-Nearest Neighbors (DW-KNN)

L'algorithme Distance-Weighted k-Nearest Neighbors (DW-KNN) est une variante du k-Nearest Neighbors (KNN).

DW-KNN fonctionne en attribuant un poids aux voisins les plus proches en fonction de leur distance au point à prédire. Contrairement au KNN classique, où chaque voisin contribue également à la décision finale, DW-KNN accorde une importance plus grande aux voisins les plus proches en utilisant une fonction de pondération basée sur la distance, comme l'inverse de la distance () ou une fonction gaussienne.

Avantages :

-Donne plus d'importance aux voisins les plus proches, réduisant l'impact des points éloignés.

-Améliore la précision dans les zones où les classes sont mélangées.

-Peut mieux gérer les données bruitées par rapport au KNN classique.


Inconvénients :

-Plus coûteux en calcul, car il nécessite le calcul des poids pour chaque voisin.

-Sensible au choix de la métrique de distance et au paramètre .

-Moins efficace pour les ensembles de données très grands en raison du recalcul des distances pour chaque prédiction.

## Algorithme des plus proches voisins condensés:

L'algorithme Condensed Nearest Neighbor (CNN) est une autre variante du KNN utilisée pour réduire la taille de l’ensemble d’entraînement tout en conservant une bonne précision de classification. Il fait partie des méthodes de réduction de prototypes qui visent à alléger le coût de stockage et de calcul de KNN en sélectionnant un sous-ensemble représentatif des données.

CNN fonctionne en construisant un ensemble de prototypes à partir des données d’entraînement. Il commence avec un échantillon minimal et ajoute uniquement les points qui sont mal classés par cet échantillon. Ainsi, seule une fraction des données est conservée, ce qui permet d’accélérer les prédictions sans trop affecter la précision.

Avantages :

-Réduit considérablement le nombre de points de référence, améliorant l'efficacité de KNN.

-Diminue le temps de calcul et l’espace mémoire requis.

-Permet d’éliminer les redondances dans l’ensemble d’entraînement.


Inconvénients :

-Peut ne pas bien fonctionner si les classes sont fortement entremêlées.

-La phase de réduction peut être coûteuse en temps de calcul.

-Risque de perdre des informations importantes si les prototypes sélectionnés ne sont pas bien représentatifs.

## Locally Adaptive k-Nearest Neighbors (LA-KNN)


L'algorithme Locally Adaptive k-Nearest Neighbors (LA-KNN) est  aussi une autre variante du KNN qui adapte dynamiquement le nombre de voisins  en fonction des caractéristiques locales des données. Contrairement au KNN classique où  est fixé pour toutes les observations, LA-KNN ajuste  en fonction de la densité locale des points, permettant une meilleure flexibilité dans les régions où les classes sont plus difficiles à séparer.

LA-KNN fonctionne en augmentant  dans les zones de faible densité (où les points sont plus dispersés) et en le réduisant dans les zones denses pour éviter les erreurs de classification dues au bruit. L’adaptation peut se faire à l’aide de métriques comme l’entropie locale ou la variance des distances entre les voisins.

Avantages :

-Améliore la robustesse du KNN dans les zones de densité variable.

-Réduit le risque d’overfitting dans les zones très peuplées et d’underfitting dans les zones clairsemées.

-Peut mieux gérer les classes déséquilibrées en ajustant  selon la distribution locale.


Inconvénients :

-Plus complexe à implémenter que le KNN classique.

-Nécessite un calcul supplémentaire pour ajuster , ce qui augmente le temps d’exécution.

-Sensible au choix de la méthode d’adaptation et à la métrique de distance utilisée.
