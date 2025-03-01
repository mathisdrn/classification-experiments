---
title: Approches paramétriques linéaires
---

## Régression logistique

La régression logistique est une méthode d'apprentissage supervisé largement utilisée pour la classification binaire. Elle modélise la probabilité qu'une observation appartienne à une des deux classes en utilisant une fonction logistique (ou sigmoïde) pour transformer une combinaison linéaire des caractéristiques en une probabilité. La fonction sigmoïde prend une valeur comprise entre 0 et 1, ce qui permet de prédire l'appartenance à une classe en appliquant un seuil, généralement 0,5. L'objectif de l'algorithme est d'ajuster les coefficients de la combinaison linéaire en maximisant la vraisemblance des observations données.

:::{image} ./../assets/logistique regression.png

:width: 550px
:alt: logistique_regression
:::
Avantages :

- Facile à interpréter grâce aux coefficients qui indiquent l'influence des variables explicatives.
- Efficace pour des problèmes de classification linéairement séparables.
- Performant même lorsque les classes sont partiellement chevauchées, tant que la relation est linéaire.

Inconvénients :

- Ne fonctionne pas bien lorsque la relation entre les variables explicatives et la probabilité d'appartenance à une classe est non linéaire.
- Peut être sensible aux valeurs aberrantes, nécessitant un nettoyage préalable des données.
- Peut nécessiter une régularisation (comme la pénalisation L1 ou L2) pour éviter le surajustement dans le cas de nombreuses variables explicatives.


## Régression Logistique avec Pénalisation Élastique

L’Elastic Net Logistic Regression est une variante de la régression logistique classique qui intègre une régularisation mixte combinant les pénalités L1 (Lasso) et L2 (Ridge). Cette approche permet de contrôler la complexité du modèle, d’éviter le sur-apprentissage, et de sélectionner les variables les plus pertinentes.

Avantages :

- Modélise des relations complexes entre les variables explicatives.

- Améliore la séparation des classes lorsque la frontière de décision n’est pas linéaire.


Inconvénients :

-Risque de sur-apprentissage si trop de termes polynomiaux sont ajoutés.

-Difficulté d’interprétation car les coefficients sont moins intuitifs qu’en régression logistique simple.

-Coût computationnel plus élevé surtout avec des degrés polynomiaux élevés.



## Support Vector Machine
:::{image} ./../assets/svm.png
:width: 550px
:alt: svm

:::

L'algorithme Support Vector Machine (SVM) est une méthode d'apprentissage supervisé utilisée pour résoudre des problèmes de régression et de classification. En découle deux implémentations algorithmiques : l'une pour la régression (SVR) et l'autre pour la classification (SVC).

L'algorithme SVM repose sur le concept des marges maximales, c'est-à-dire qu'il cherche à séparer deux classes dans l'espace des caractéristiques en traçant un hyperplan qui maximise la distance (ou la marge) entre les points de chaque classe les plus proches de cette hyperplan, appelés vecteurs de support. Lorsque les classes ne sont pas linéairement séparables, l'algorithme utilise des noyaux pour projeter les données dans un espace de dimension supérieure où elles peuvent être séparées.

L’objectif du SVM classique est de minimiser la fonction de coût suivante :  

$$\min_{w, b} \frac{1}{2} ||w||^2 + C \sum_{i=1}^{n} \xi_i$$

où :  
- $||w||^2 $ contrôle la marge du classificateur,  
- $ C$ est un paramètre de régularisation qui équilibre la maximisation de la marge et la minimisation des erreurs,  
- $\xi_i$ est la variable d’erreur pour chaque point mal classé. 
Avantages :

- Efficace dans des espaces de grande dimension.
- Peut être modifié pour des cas non linéaires grâce aux fonctions noyau.
- Utilise seulement les vecteurs de support, ce qui le rend plus économe en mémoire.

Inconvénients :

- Peut être sensible aux choix des paramètres (comme C et le type de noyau).
- Moins performant avec de très grands ensembles de données ou quand les classes sont fortement chevauchées.

### One-Class SVM  

Le One-Class SVM est une version du Support Vector Machine utilisée principalement pour la détection d’anomalies et le traitement des déséquilibres de classes. Contrairement aux SVM classiques qui séparent plusieurs classes, le One-Class SVM apprend uniquement à partir des données d’une seule classe et identifie les observations qui ne s’y conforment pas.  

### Principe de fonctionnement
Le modèle cherche à apprendre une fonction de décision $f(x)$ qui sépare la majorité des données normales  de celles considérées comme anomalies en maximisant la marge.  

L'objectif est de résoudre :  

$$
\min_{w, \rho} \frac{1}{2} ||w||^2 + \frac{1}{\nu n} \sum_{i=1}^{n} \xi_i - \rho $$

sous contrainte :  

$$ w \cdot \phi(x_i) \geq \rho - \xi_i, \quad \xi_i \geq 0, \quad \forall i$$

où :  
- $\phi(x)$ est la transformation dans un espace de dimension supérieure via un noyau (ex. gaussien),  
- $\nu$ est un hyperparamètre qui contrôle la proportion d’anomalies détectées,  
- $\rho$ définit la frontière entre les points normaux et les anomalies,  
- $\xi_i$ sont des variables d’erreur permettant d’autoriser quelques points à être mal classés.  

Avantages :

- Utile pour détecter des valeurs aberrantes dans un jeu de données fortement déséquilibré.  
- Fonctionne bien avec un noyau gaussien pour capturer des structures non linéaires.  
- Peut être utilisé pour identifier des classes rares dans un dataset.  

Inconvénients : 

- Sensible au choix de $\nu $ et du noyau utilisé.  
- Peut produire **beaucoup de faux positifs** si mal calibré.  

### Combinaison SVM avec des méthodes de sous/sur-échantillonnage  

Lorsque les données sont fortement déséquilibrées, un SVM classique a tendance à favoriser la classe majoritaire. Pour éviter cela, on peut rééquilibrer les données avant d’entraîner le modèle en utilisant des techniques de sous-échantillonnage ou de sur-échantillonnage.  

   

#### 1. Sous-échantillonnage (UnderSampling)  
On réduit la taille de la classe majoritaire pour équilibrer le dataset. Cela permet de :  
- Réduire le biais du modèle en l’empêchant de trop favoriser la classe majoritaire.  
- Accélérer le temps d’apprentissage car il y a moins d’exemples.  

Cependant, cela peut perdre des informations importantes si les données supprimées contiennent des modèles significatifs.  

#### 2. Sur-échantillonnage (OverSampling)  
On augmente artificiellement la taille de la classe minoritaire, par exemple en utilisant SMOTE (Synthetic Minority Over-sampling Technique) qui génère de nouvelles observations synthétiques en interpolant les points existants.  

L’algorithme SMOTE fonctionne comme suit :  
1. Sélectionner un point minoritaire aléatoire.  
2. Trouver ses $k$ plus proches voisins.  
3. Générer un nouveau point interpolé entre le point sélectionné et un de ses voisins.  

Avantages : 

- Évite que le SVM soit biaisé vers la classe majoritaire.  
- SMOTE permet de générer des données sans simple duplication.  
- Sous-échantillonnage permet d’accélérer les calculs.  

Inconvénients :

- Sous-échantillonnage risque de perdre de l’information utile.  
- Sur-échantillonnage peut ajouter du bruit et mener à du surajustement si mal utilisé.  



## Support Vector Machine à noyau gaussien
Le SVM gaussien est une version du Support Vector Machine (SVM) qui utilise le noyau gaussien (RBF - Radial Basis Function) pour résoudre des problèmes où les classes ne sont pas séparables par une simple ligne droite(séparation non linéaires). Ce noyau transforme les données en les projetant dans un espace de dimension supérieure, où elles deviennent plus faciles à séparer.

L'équation du noyau gaussien est :
 
$$ K(x, x') = \exp\left(-\gamma ||x - x'||^2\right) $$

où :  
- $ x, x' $ sont deux observations,  
- $||x - x'||^2$ est la distance euclidienne au carré entre ces points,  
- $\gamma$ est un paramètre qui contrôle l’influence d’un point donné. Une valeur de $ \gamma $ trop grande peut entraîner un surapprentissage car le modèle se focalise sur des voisins proches(modèle trop complexe), tandis qu’une valeur trop faible peut mener à une sous-apprentissage (modèle trop simple). 

Avantages 

 - Modélise des relations complexes et non linéaires.  
 - Moins sensible aux dimensions élevées grâce aux vecteurs de support.  
- Convient aux jeux de données de taille moyenne à grande.  

Inconvénients  

- Sensible aux choix des hyperparamètres \( C \) et \( \gamma \), nécessitant une optimisation.  
- Coût computationnel élevé pour de très grands ensembles de données.  
 - Moins interprétable qu'un modèle linéaire.  

Le **SVM à noyau gaussien** est particulièrement efficace lorsque les frontières de décision sont complexes et non linéaires, mais nécessite un réglage précis des paramètres pour éviter le surajustement.


### Cost-sensitive SVM 

Le Cost-sensitive SVM est une version du Support Vector Machine qui attribue une pénalité différente $C$ à chaque classe afin de mieux gérer le déséquilibre des classes. Il ajuste $C$ différemment de SVM classique  pour chaque classe :  

$$\min_{w, b} \frac{1}{2} ||w||^2 + C_+ \sum_{i \in \mathcal{C}_+} \xi_i + C_- \sum_{i \in \mathcal{C}_-} \xi_i$$

où :  
- $C_+$ et $ C_-$ sont les pénalités spécifiques pour la classe positive et la classe négative,  
- $\mathcal{C}_+$ et $\mathcal{C}_-$ représentent les ensembles d’indices des échantillons de chaque classe.  

Avantages 

- Il améliore la classification des classes sous-représentées.  
- Il empêche le modèle de favoriser la classe majoritaire.  

Inconvénients  

- Il faut **optimiser les valeurs de \( C_+ \) et \( C_- \)** pour éviter le sur-ajustement.  
- Peut être instable si les classes sont extrêmement déséquilibrées.  



### Ensemble de SVMs avec Bagging

L’ensemble de SVMs avec bagging est une approche où plusieurs SVMs sont entraînés sur des sous-échantillons différents des données, puis combinés pour améliorer la robustesse du modèle.  

### Principe de fonctionnement

1. On génère $M$ sous-ensembles de données $D_1, D_2, ..., D_M$ en effectuant un bootstrap.  
2. Un SVM est entraîné sur chaque sous-ensemble $D_m$:  

$$h_m(x) = \text{SVM}(D_m)$$

3. La prédiction finale est obtenue par **vote majoritaire** en classification :  

$$\hat{y} = \arg\max_{y} \sum_{m=1}^{M} \mathbb{1}(h_m(x) = y)$$


Avantages 

- Il réduit la variance et améliore la stabilité du modèle.  
- Il est moins sensible aux données bruitées et aux outliers.  

Inconvénients  

- Il est plus coûteux en calcul, car il faut entraîner plusieurs SVMs.  
- Le choix du nombre de modèles $M$ influence les performances.  

