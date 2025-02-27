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

## Forêt Aléatoire 

L’algorithme Forêt Aléatoire(Random Forest en anglais) est une extension des arbres de décision, utilisée pour la classification et la régression. Il repose sur un principe d’apprentissage ensembliste (ensemble learning), combinant plusieurs arbres pour améliorer la robustesse et la précision des prédictions.

Principe de fonctionnement :

1. Construction d’une forêt d’arbres de décision

L’algorithme génère plusieurs arbres en effectuant un échantillonnage aléatoire avec remise sur le jeu de données (bootstrap).

À chaque division dans un arbre, un sous-ensemble aléatoire de caractéristiques est sélectionné pour éviter que tous les arbres se construisent de la même manière.



2. Prédiction par agrégation des arbres

Classification : Chaque arbre vote pour une classe, et la classe majoritaire est retenue (vote majoritaire).

Régression : La prédiction finale est la moyenne des prédictions des différents arbres.

:::{admonition} Note : Bootstrap
:class: note  

Le bootstrap est une méthode de rééchantillonnage avec remise qui crée plusieurs sous-ensembles à partir d’un même jeu de données. Dans Random Forest, il est utilisé pour entraîner chaque arbre sur un échantillon aléatoire, introduisant de la diversité et réduisant le sur-apprentissage. Cette technique améliore la robustesse et la généralisation du modèle.
:::

Avantages :

-plus précis et généralisable sans risque de surapprentissage qu’un arbre unique.

-Peu sensible aux valeurs aberrantes grâce à l’agrégation des arbres.

-robustesse : Une petite variation dans les données n’impacte pas fortement le modèle.


-Gère bien les données manquantes, les grands ensembles de données grâce à la sélection aléatoire des caractéristiques et il fonctionne bien même avec de nombreuses variables.


Inconvénients :

-Moins interprétable qu’un arbre unique, car le résultat final résulte de plusieurs modèles.

-Temps de calcul plus long pour de grands ensembles de données.

-Performances limitées sur des données très haute dimension par rapport à d’autres modèles avancés comme Adaboost, XGBoost ou LightGBM.
 
##  Forêt Aléatoire Sensible au Coût

L’algorithme Forêt Aléatoire Sensible au Coût (Cost-Sensitive Random Forest en anglais) est une adaptation du Random Forest conçue pour prendre en compte des coûts différents d’erreur lors de la classification. Il est particulièrement utile lorsque les classes sont déséquilibrées ou que certaines erreurs ont un impact plus important que d’autres, comme en détection de fraude ou en diagnostic médical.

Principe de fonctionnement :

1. Pondération des erreurs

Contrairement au Random Forest classique, qui minimise simplement le taux d’erreur global, le Cost-Sensitive Random Forest attribue un coût à chaque type d’erreur.

Une matrice de coûts est définie pour pénaliser différemment les erreurs en fonction de leur importance.



2. Construction d’une forêt de décision pondérée

Comme dans Random Forest, plusieurs arbres sont générés sur des échantillons bootstrap des données.

À chaque division, le critère de sélection (comme l’indice de Gini ou l’entropie) est ajusté pour tenir compte des coûts des erreurs.



3. Prédiction avec prise en compte des coûts

 Plutôt que d’utiliser un vote majoritaire simple entre les arbres, la classe prédite est celle qui minimise le coût d’erreur attendu.

Avantages :

Meilleure prise en compte des déséquilibres de classe: Dans un problème où une classe est beaucoup moins fréquente que l’autre, Random Forest peut privilégier la classe majoritaire. En intégrant un coût plus élevé pour les erreurs sur la classe minoritaire, l’algorithme devient plus équitable.



Plus adapté aux contextes où certaines erreurs coûtent plus cher que d’autres : Par exemple, dans une détection de fraude bancaire, une fausse alerte (prédire une fraude inexistante) est moins grave qu’un faux négatif (ne pas détecter une fraude réelle).


Garde la robustesse du Random Forest tout en améliorant la gestion des erreurs critiques.


Inconvénients :

Nécessite de bien définir la matrice de coûts, ce qui peut être délicat en l’absence d’informations précises sur l’impact des erreurs.

Peut être plus long à entraîner, car l’arbre doit ajuster ses critères de sélection en fonction des coûts d’erreur.

Moins intuitif que le Random Forest standard, car les décisions ne sont plus basées uniquement sur des votes majoritaires.


## AdaBoost (Adaptive Boosting)

L'algorithme AdaBoost (Adaptive Boosting) est une méthode d’apprentissage supervisé utilisée principalement pour la classification. Il appartient à la famille des méthodes d’ensemble et fonctionne en combinant plusieurs classificateurs faibles (souvent des arbres de décision de profondeur 1, appelés stumps) pour créer un modèle puissant et robuste.

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