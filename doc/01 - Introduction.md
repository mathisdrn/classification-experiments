---
title: Classification binaire
---

### Introduction

L’apprentissage supervisé est une méthode d’apprentissage automatique où un modèle est entraîné à partir de données étiquetées pour apprendre à faire des prédictions. Il consiste à établir une relation entre des entrées (features) et une sortie (label), afin que le modèle puisse généraliser cette relation à de nouvelles données.

Parmi les tâches les plus courantes en apprentissage supervisé, on retrouve la classification, qui est un type de problème de machine learning supervisé dans lequel l'objectif est de classer les données au sein de catégories distinctes. Chaque exemple dans les données est ainsi étiqueté comme appartenant à l'une des catégories appelée classe et un modèle de classification est entraîné pour prédire la classe d'un nouvel exemple en fonction de ses caractéristiques.

La classification est largement utilisée dans de nombreux domaines, tels que la reconnaissance de caractères, la détection de spam, la détection de fraudes, la reconnaissance d'images, la détection de maladies, etc. Elle est souvent utilisée pour résoudre des problèmes de classification binaire (deux classes) ou multiclasse (plus de deux classes).

Dans ce projet, nous nous concentrons sur la classification binaire :
- prédire si un patient est malade ou non malade
- prédire si un email est un spam ou non spam
- prédire si un client va acheter un produit ou non
- etc.

### Les principaux types de modèles de classification

Il existe de nombreux algorithmes de classification, chacun ayant ses propres avantages et inconvénients. Ces algorithmes peuvent être classés en plusieurs catégories en fonction de leur approche de modélisation :
- **Approches paramétriques** : ces modèles supposent que les données d'entraînement sont générées par une distribution de probabilité paramétrique. Les paramètres de cette distribution sont estimés à partir des données d'entraînement et utilisés pour prédire la classe d'un nouvel exemple. Les modèles de régression logistique et les machines à vecteurs de support (SVM) sont des exemples d'approches paramétriques.
- **Approches non paramétriques** : ces modèles n'imposent pas de contraintes sur la forme de la distribution des données. Ils apprennent directement à partir des données sans supposer une forme particulière pour la distribution. Les arbres de décision, les forêts aléatoires et les k plus proches voisins (k-NN) sont des exemples d'approches non paramétriques.
- **Approches non linéaires** : ces modèles sont capables de modéliser des relations non linéaires entre les caractéristiques et la classe cible. Ils utilisent des transformations non linéaires des caractéristiques pour apprendre des frontières de décision complexes. Les réseaux de neurones et les machines à vecteurs de support avec noyaux non linéaires sont des exemples d'approches non linéaires.


### Problématique principale abordée.
La classification est une tâche importante en machine learning, mais chaque algorithme a ses propres forces et faiblesses. L’un des principaux défis est donc d’identifier la méthode la plus efficace en fonction des caractéristiques des données.  

Dans cette étude, nous chercherons à répondre à plusieurs questions :  

- Quelle famille d’algorithmes de classification est la plus performante selon les types de données ?  
- Comment optimiser les modèles pour améliorer leurs résultats ?  
- Quels compromis doit-on faire entre précision, temps de calcul et complexité des modèles ?

### Importance et motivation du projet

Ce projet joue un rôle clé dans l’analyse des différentes méthodes de classification afin de mieux en comprendre les forces et les limites. Il vise à :  

- Améliorer le choix des algorithmes en fonction du contexte et des caractéristiques des données.  
- Étudier l’impact de techniques d’optimisation, comme la réduction de dimensions, l’ajustement des hyperparamètres et les méthodes d’échantillonnage.  
- Explorer des variantes des algorithmes classiques afin d’améliorer la qualité de la classification.  
- Proposer une méthodologie rigoureuse et reproductible pour évaluer objectivement les performances des modèles.


### Objectifs principaux du projet.

Ce projet a pour objectif de comparer et d’analyser différentes approches de classification afin de mieux comprendre leur efficacité et leurs limites. Pour cela, nous étudierons trois grandes catégories d’algorithmes : les méthodes non paramétriques, les approches paramétriques linéaires et les approches non linéaires. L’évaluation de ces modèles se fera selon plusieurs critères, tels que la précision des résultats, le temps d’apprentissage et leur capacité à s’adapter aux variations des données. L’objectif est d’identifier la famille d’algorithmes la plus performante et d’optimiser les modèles en fonction des types de données et des domaines d’application.  

Ces méthodes seront appliquées à plusieurs secteurs. En **cybersécurité et communication numérique**, elles permettront d’améliorer la classification et la détection automatique des menaces. Dans l’**industrie agroalimentaire**, elles serviront à analyser la qualité des produits. Le **marketing et la finance** les utiliseront pour segmenter les clients et évaluer les risques financiers des emprunteurs. En **santé et biomédecine**, elles contribueront à la détection et au diagnostic de maladies, notamment des pathologies cardiaques et des troubles thyroïdiens. Enfin, en **vision par ordinateur et reconnaissance de formes**, elles permettront d’optimiser l’identification automatique d’objets et de structures complexes.


### Description des jeux de données utilisés (caractéristiques, taille, équilibre des classes, etc.).

#### Sources des jeux de données
Les jeux de données utilisés dans cette étude proviennent principalement de sources académiques et ouvertes, souvent intégrées dans des bibliothèques de R et Python, garantissant ainsi leur qualité et leur diversité pour l’évaluation des algorithmes de classification. Le UCI Machine Learning Repository constitue l’une des principales références, hébergeant des bases largement utilisées en machine learning, telles que Spambase, Wine Quality, Bank Marketing, Pima Indians Diabetes et Heart Disease. Par ailleurs, plusieurs jeux de données sont directement accessibles via les packages de RStudio disponibles sur le CRAN, comme datasets (avec iris et mtcars), MASS (qui inclut Boston housing et Pima Indians Diabetes), mlbench (contenant Glass, Sonar, Ionosphere), et ElemStatLearn. La plateforme Kaggle constitue également une source précieuse pour le téléchargement de jeux de données sous format CSV, facilitant leur exploitation dans RStudio. En complément, OpenML permet l’importation de jeux de données directement dans R via le package OpenML, tandis que d’autres bases sont accessibles à partir de StatLib (Carnegie Mellon University) et de référentiels institutionnels tels que Eurostat et la Banque mondiale, qui proposent des bases économiques exploitables via les packages eurostat et WDI. Enfin, des jeux de données structurés issus du Tidyverse, comme diamonds et gapminder, offrent des ressources supplémentaires pour l’analyse de données dans R.

#### Nombre d’échantillons et dimensions principales
::: {table}
:name: bases-de-donnees
:align: center

| Nom de la base           | Nombre de lignes | Type de classification                            | Variables principales                                      |
|--------------------------|-----------------|--------------------------------------------------|-----------------------------------------------------------|
| Spambase                | 4601            | Classification binaire (Spam / Non-Spam)         | Fréquence de mots spécifiques, présence de caractères spéciaux |
| Wine Quality            | 6497            | Classification multiclasse (Qualité du vin)      | Acidité, pH, teneur en alcool, sucre résiduel             |
| Bank Marketing          | 45211           | Classification binaire (Souscription / Non)      | Âge, profession, état civil, solde bancaire, contact      |
| Pima Indians Diabetes   | 768             | Classification binaire (Diabète / Non)           | Glucose, pression sanguine, âge, indice de masse corporelle |
| Heart Disease           | 303             | Classification binaire (Maladie cardiaque / Non) | Âge, cholestérol, pression artérielle, fréquence cardiaque |
| Newthyroid              | 215             | Classification binaire (Trouble thyroïdien / Non)| TSH, T3, T4, âge, sexe                                     |
| Vehicle                 | 846             | Classification multiclasse (Type de véhicule)    | Compacité, circularité, distance, variation d'intensité   |
| Glass                   | 214             | Classification multiclasse (Type de verre)       | Indice de réfraction, sodium, magnésium, aluminium        |
| Segmentation            | 2310            | Classification multiclasse (Type d'objet)        | Textures, couleurs, intensités lumineuses                 |
| Page-Blocks             | 5473            | Classification multiclasse (Type de bloc)        | Surface, compacité, alignement horizontal et vertical     |
| Auto-MPG                | 398             | Régression (Consommation de carburant)          | Nombre de cylindres, poids, puissance, année du modèle    |
| Balance Scale           | 625             | Classification multiclasse (Balance stable / instable) | Poids gauche, poids droit, distance de pivot             |
| German Credit           | 1000            | Classification binaire (Crédit accepté / Non)    | Durée du crédit, âge, historique bancaire                 |
| Bupa                    | 345             | Classification binaire (Maladie hépatique / Non) | Gamma-GT, alcool, enzyme du foie                          |
| Ionosphere              | 351             | Classification binaire (Objet détecté / Non)     | Réflexion des signaux radar                               |
| Sonar                   | 208             | Classification binaire (Mine / Roche)           | Amplitude et fréquence des signaux acoustiques           |
| Yeast                   | 1484            | Classification multiclasse (Type de protéine)    | Taille, charge électrique, hydrophobicité                |
| Abalone                 | 4177            | Régression (Âge de l'abalone)                    | Longueur, diamètre, hauteur, poids                       |
| Australian Credit       | 690             | Classification binaire (Crédit accepté / Non)    | Revenus, historique de crédit, dettes                    |

:::


### Prétraitement éventuel des données (normalisation, gestion des valeurs manquantes).

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/classification-experiments) sous licence MIT.
+++