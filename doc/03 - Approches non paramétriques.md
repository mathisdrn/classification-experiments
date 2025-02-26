---
title: Approches non paramétriques
---
## Algorithme des k plus proches voisins
L'algorithme des k plus proches voisins (KNN) est une méthode d'apprentissage supervisé utilisée pour résoudre des problèmes de classification et de régression. Il fonctionne en identifiant les k instances du jeu de données d'entraînement les plus proches d'une nouvelle observation, puis en déterminant la sortie en fonction des valeurs de ces voisins.

Le principe fondamental du KNN est que des données similaires se trouvent à proximité les unes des autres dans l'espace des caractéristiques. Pour mesurer la proximité, l'algorithme utilise généralement des métriques de distance telles que la distance euclidienne ou la distance de Manhattan. Le choix du nombre de voisins, k, est crucial : une valeur trop petite peut rendre le modèle sensible au bruit, tandis qu'une valeur trop grande peut diluer la distinction entre les classes.

Avantages:

-Simplicité et facilité d'implémentation : KNN est intuitif et ne nécessite pas de phase d'entraînement explicite, ce qui le rend facile à mettre en œuvre.

-Adaptabilité : L'algorithme s'ajuste facilement à de nouvelles données, car il conserve l'ensemble des données d'entraînement.

Inconvénients :

-Coût computationnel élevé : Pour chaque prédiction, KNN calcule la distance entre l'observation à prédire et toutes les observations du jeu de données, ce qui peut être lent pour de grands ensembles de données.

-Sensibilité aux données bruitées et aux caractéristiques non pertinentes : La performance de KNN peut être affectée si les données contiennent du bruit ou des caractéristiques non informatives.

## Algorithme des plus proches voisins condensés:
L'algorithme des plus proches voisins condensés ( en anglais Condensed Nearest Neighborest, CNN) est une méthode d'apprentissage supervisé visant à réduire la taille de l'ensemble d'entraînement pour les tâches de classification. Il sélectionne un sous-ensemble représentatif des données originales, permettant ainsi de diminuer les besoins en stockage et en calcul lors de la phase de classification.

Le principe fondamental du CNN de conserver uniquement les échantillons essentiels pour définir les frontières de décision entre les classes. L'algorithme commence avec un sous-ensemble vide ou contenant un échantillon de chaque classe, puis parcourt l'ensemble d'entraînement : chaque point mal classé par le sous-ensemble actuel est ajouté à ce dernier. Ce processus itératif se poursuit jusqu'à ce que tous les points de l'ensemble d'entraînement soient correctement classés par le sous-ensemble condensé.

Avantages :

-Réduction de la complexité : En diminuant le nombre de points de référence, le CNN réduit les coûts de stockage et accélère le processus de classification.

-Simplicité d'implémentation : L'algorithme est facile à mettre en œuvre et ne nécessite pas de paramètres complexes.

-Maintien de la performance : En conservant les points critiques pour la classification, le CNN préserve généralement la précision du classificateur.

Inconvénients :

-Sensibilité à l'ordre des données : Les résultats du CNN peuvent varier en fonction de l'ordre de présentation des échantillons, ce qui peut affecter la cohérence du sous-ensemble condensé.

-Efficacité limitée sur de grands ensembles de données : Pour des ensembles de données volumineux, le processus itératif peut être long et moins efficace.