---
title: Approches non linéaires
---

## Techniques d'échantillonnage et d'ensemble

### Bootstrap / Bagging

#### Concept
Le Bagging (Bootstrap Aggregating) crée plusieurs modèles en échantillonnant avec remplacement l'ensemble de données original, puis agrège leurs prédictions pour améliorer la stabilité et la précision.

:::{image} ./../assets/randomforest.png
:width: 400px
:alt: randomforest
:::

#### Fonctionnement
Si nous avons un ensemble de données $D = \{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\}$, le bagging crée $m$ échantillons bootstrap $D_1, D_2, ..., D_m$ en tirant $n$ exemples avec remplacement de $D$. Un modèle $f_i$ est construit sur chaque échantillon $D_i$. La prédiction finale est:

Pour la régression:
$$f_{bag}(x) = \frac{1}{m} \sum_{i=1}^{m} f_i(x)$$

Pour la classification:
$$f_{bag}(x) = \text{mode}\{f_1(x), f_2(x), ..., f_m(x)\}$$

#### Avantages
* Réduit la variance sans augmenter le biais
* Parallélisable (chaque modèle peut être entraîné indépendamment)
* Efficace contre le surapprentissage

#### Inconvénients
* Ne réduit pas le biais des modèles sous-jacents
* Perte d'interprétabilité
* Coût computationnel plus élevé que les modèles individuels

### Boosting

#### Concept
Le Boosting construit séquentiellement des modèles où chaque nouveau modèle tente de corriger les erreurs des modèles précédents, donnant plus de poids aux exemples mal classifiés.

#### Fonctionnement
Pour un problème de classification binaire $y \in \{-1, 1\}$, avec des classificateurs faibles $h_t$, le boosting fonctionne ainsi:

Initialisation: $D_1(i) = \frac{1}{n}$ pour tout $i$

Pour $t = 1, 2, ..., T$:
1. Entraîner un classificateur faible $h_t$ sur la distribution $D_t$
2. Calculer l'erreur pondérée: $\epsilon_t = \sum_{i=1}^{n} D_t(i) \mathbb{1}(h_t(x_i) \neq y_i)$
3. Calculer le poids du modèle: $\alpha_t = \frac{1}{2} \ln(\frac{1-\epsilon_t}{\epsilon_t})$
4. Mettre à jour la distribution: $D_{t+1}(i) = \frac{D_t(i) \exp(-\alpha_t y_i h_t(x_i))}{Z_t}$ où $Z_t$ est un facteur de normalisation

Le classificateur final est:
$$H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t h_t(x)\right)$$

#### Avantages
* Réduit à la fois le biais et la variance
* Peut créer un modèle fort à partir de classificateurs faibles
* Très performant sur une grande variété de problèmes

#### Inconvénients
* Sensible aux valeurs aberrantes et au bruit
* Risque de surapprentissage si trop d'itérations
* Pas facilement parallélisable (nature séquentielle)

## Algorithmes non linéaires

### Arbres de décisions

#### Concept général
Un arbre de décision est un modèle qui prédit la valeur d'une variable cible en apprenant des règles de décision simples déduites des caractéristiques des données.

:::{image} ./../assets/decision tree.png
:width: 550px
:alt: decisiontree
:::

#### Fonctionnement
Pour construire un arbre, on sélectionne à chaque nœud la caractéristique qui maximise le gain d'information (ou minimise l'impureté). Pour la classification, on utilise généralement l'entropie ou l'indice de Gini:

Entropie:
$$H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

Indice de Gini:
$$G(S) = 1 - \sum_{i=1}^{c} p_i^2$$

où $p_i$ est la proportion d'éléments de classe $i$ dans l'ensemble $S$.

Le gain d'information est calculé par:
$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

où $S_v$ est le sous-ensemble où l'attribut $A$ a la valeur $v$.

#### Avantages
* Facile à comprendre et à interpréter
* Nécessite peu de préparation des données
* Peut gérer des variables numériques et catégorielles

#### Inconvénients
* Tendance à créer des arbres trop complexes (surapprentissage)
* Instabilité (petits changements dans les données peuvent entraîner un arbre très différent)
* Performance limitée sur certains problèmes complexes

### Forêts Aléatoires

#### Concept
Une forêt aléatoire combine le principe du bagging avec une sélection aléatoire de caractéristiques à chaque nœud, créant ainsi un ensemble d'arbres de décision diversifiés.

#### Fonctionnement
Une forêt aléatoire construit $B$ arbres de décision $\{T_1, T_2, ..., T_B\}$ sur des échantillons bootstrap. À chaque nœud, au lieu de considérer toutes les $p$ caractéristiques, on n'en considère qu'un sous-ensemble $m < p$ choisi aléatoirement.

La prédiction finale est:

Pour la régression:
$$f_{RF}(x) = \frac{1}{B} \sum_{b=1}^{B} T_b(x)$$

Pour la classification:
$$f_{RF}(x) = \text{mode}\{T_1(x), T_2(x), ..., T_B(x)\}$$

Pour évaluer l'importance des variables, on peut utiliser la diminution moyenne de l'impureté (MDI):
$$Imp(X_j) = \frac{1}{B} \sum_{b=1}^{B} \sum_{t \in T_b: v(t)=j} p(t) \Delta i(t)$$

où $v(t)$ est la variable utilisée pour la division au nœud $t$, $p(t)$ est la proportion d'échantillons atteignant $t$, et $\Delta i(t)$ est la diminution d'impureté.

#### Avantages
* Performance supérieure à celle des arbres individuels
* Robustesse au surapprentissage
* Gère efficacement les grandes dimensions et les données manquantes

#### Inconvénients
* Moins interprétable qu'un arbre de décision unique
* Coût computationnel et de mémoire élevé
* Difficulté à modéliser certaines relations linéaires simples

### AdaBoost

#### Concept
AdaBoost (Adaptive Boosting) est un algorithme de boosting qui ajuste les poids des exemples mal classifiés à chaque itération et combine des classificateurs faibles en un classificateur fort.

:::{image} ./../assets/Schematic-diagram-of-AdaBoost-algorithm.png
:width: 450px
:alt: Pipeline of model training
:::

#### Fonctionnement
AdaBoost fonctionne comme suit:

Initialisation: $w_i^{(1)} = \frac{1}{n}$ pour $i = 1, 2, ..., n$

Pour $t = 1, 2, ..., T$:
1. Entraîner un classificateur faible $h_t$ en utilisant les poids $w_i^{(t)}$
2. Calculer l'erreur pondérée: $\epsilon_t = \sum_{i=1}^{n} w_i^{(t)} \mathbb{1}(h_t(x_i) \neq y_i)$
3. Calculer le coefficient: $\alpha_t = \frac{1}{2} \ln(\frac{1-\epsilon_t}{\epsilon_t})$
4. Mettre à jour les poids: $w_i^{(t+1)} = w_i^{(t)} \exp(-\alpha_t y_i h_t(x_i))$
5. Normaliser: $w_i^{(t+1)} = \frac{w_i^{(t+1)}}{\sum_{j=1}^{n} w_j^{(t+1)}}$

Le classificateur final est:
$$H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t h_t(x)\right)$$

#### Avantages
* Simple à implémenter
* Bonne performance sur de nombreux jeux de données
* S'adapte automatiquement à l'importance relative des caractéristiques

#### Inconvénients
* Sensible aux valeurs aberrantes et au bruit
* Peut être surpassé par d'autres algorithmes de boosting (comme XGBoost)
* Peut conduire au surapprentissage sur des données bruitées