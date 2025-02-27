---
title: Approches non linéaires
---
## Decision Tree

L'algorithme des arbres de décision (Decision Tree) est une méthode d'apprentissage supervisé utilisée pour la classification et la régression. Il repose sur une structure arborescente où chaque nœud représente une question sur une caractéristique des données, chaque branche correspond à une réponse possible, et chaque feuille donne une prédiction.

 ### Principe de fonctionnement :

1. Création de l'arbre : L'algorithme divise les données en fonction de la caractéristique qui maximise la séparation des classes ou minimise l'erreur de prédiction. Ce choix se fait souvent avec des mesures comme l'entropie (pour l'indice de Gini ou l'information gain en classification) ou l'erreur quadratique moyenne (en régression).


2. Parcours de l'arbre : Pour prédire une nouvelle observation, on part de la racine et on suit les branches en fonction des valeurs des caractéristiques jusqu'à atteindre une feuille.


3. Prédiction :

Classification : L'étiquette de la classe la plus fréquente dans la feuille est assignée.

Régression : La valeur moyenne des observations contenues dans la feuille est utilisée comme prédiction.

:::{admonition} Définition : Critères de division en classification
:class: note  
 ### 1.Entropie

L’entropie mesure l’homogénéité d’un ensemble. Elle est définie par :
$$ H(S) = - p_1 \log_2 p_1 - p_2 \log_2 p_2$$

où :

 et $ p_i $ sont les proportions des classes dans l’ensemble .

Une entropie de 0 signifie que tous les éléments appartiennent à une seule classe (ensemble pur).

Une entropie de 1 signifie que les classes sont réparties de manière égale (ensemble totalement incertain).


Le gain d’information () est utilisé pour choisir la meilleure caractéristique qui permet la meilleu séparation des classes en mesurant la réduction d'entropie après chaque division, il est donné par la formule suivante:

$$ IG(S, A) = H(S) - \sum_{v \in V} \frac{|S_v|}{|S|} H(S_v) $$

où $S_v$ est le sous-ensemble des données ayant la valeur $v$ pour l’attribut .

### 2. Indice de Gini

L'indice de Gini est une alternative à l'entropie et mesure l’impureté d’un ensemble :

$$ Gini(S) = 1 - p_1^2 - p_2^2 $$

où $p_i$  et  sont les proportions des classes dans l’ensemble .
L’indice de Gini est minimal (0) lorsque l’ensemble est homogène et maximal (0.5 en classification binaire) lorsque les classes sont équilibrées.

De la même manière, on peut calculer la réduction d’impureté(gain d’information) avec l’indice de Gini :

$$ \Delta Gini = Gini(S) - \sum_{v \in V} \frac{|S_v|}{|S|} Gini(S_v)$$



:::

## AdaBoost (Adaptive Boosting)

L'algorithme AdaBoost (Adaptive Boosting) est une méthode d’apprentissage supervisé utilisée principalement pour la classification. Il appartient à la famille des méthodes d’ensemble (ensemble learning) et fonctionne en combinant plusieurs classificateurs faibles (souvent des arbres de décision de profondeur 1, appelés stumps) pour créer un modèle puissant et robuste.

AdaBoost fonctionne en attribuant un poids à chaque observation et en entraînant une série de classificateurs faibles de manière itérative. À chaque itération, les erreurs des modèles précédents sont amplifiées : les observations mal classées reçoivent un poids plus élevé pour que le modèle suivant se concentre davantage sur elles. La prédiction finale est obtenue par un vote pondéré des classificateurs.

:::{image}  C:\Users\HP\Downloads\guillaume\classification-experiments\assets\Schematic-diagram-of-AdaBoost-algorithm.png
:width: 450px
:alt: Pipeline of model training
:::

Avantages :

-Améliore la précision en combinant plusieurs modèles faibles.

-Fonctionne bien sur des données bruitées et complexes.

-Peut être utilisé avec différents modèles de base (arbres, SVM, etc.).


Inconvénients :

-Sensible aux données bruitées et aux outliers, qui peuvent être sur-appris.

-Peut être lent si le nombre d’itérations est élevé.

-Nécessite un bon choix de l’algorithme de base pour éviter l’overfitting.


## Early Stopping AdaBoost

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