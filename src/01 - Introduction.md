---
title: Classification experiements
---

### Introduction

[...]

### Contexte et problématique

[...]

### Introduction à la classification binaire et son importance.

### Classification binaire

La classification binaire est un type de problème de machine learning supervisé dans lequel l'objectif est de classer les données en deux catégories distinctes. Chaque exemple dans les données est ainsi étiqueté comme appartenant à l'une des deux classes possibles.

### Classes déséquilibrées

L'un des enjeux liés aux problèmes de classification est la présence de classes déséquilibrées. On parle de classes déséquilibrées lorsque les données d'entraînement contiennent un grand déséquilibre entre le nombre d'exemples de chaque classe. C'est par exemple le cas de notre jeu de données où seulement $15 \%$ des mail sont des spams.

Ce déséquilibre peut poser plusieurs défis pour l'apprentissage automatique :

- Apprentissage insuffisant : avec moins de données d’apprentissage pour la classe minoritaire, le modèle ne parvient pas à reconnaître efficacement les caractéristiques distinctives de la classe minoritaire.
- Le modèle favorise la bonne classification de la classe majoritaire, car il minimise l'erreur globale en classant la plupart des exemples dans la classe majoritaire.
- Les métriques de performance du modèle sur-représente la performance du modèle à évaluer la classe majoritaire.

Plusieurs solutions peuvent être mises en place pour pallier ces problèmes, comme le sur-échantillonnage de la classe minoritaire, le sous-échantillonnage de la classe majoritaire, ou la création de données synthétiques à l'aide d'interpolation afin de rééquilibrer les classes. Certains modèles permettent aussi de donner plus de poids aux exemples de la classe minoritaire pour les rendre plus importants lors de l'apprentissage.

Il faut aussi noter que tous les modèles ne sont pas affectés de la même manière à ces problématiques, SVM et Naïve Bayes sont considérés comme plus robustes face à des classes déséquilibrées.

### Prétraitement des données

Le pré-traitement des données répond à de nombreux objectifs :

- Nettoyer les données inutiles, redondantes ou même nuisible pour l'entraînement du modèle
- Transformer les données textuelles en données numériques exploitables par les algorithmes de machine learning. Ici en particulier, les données d'entrées du classifieur doivent être de même dimension.
- Réduire la dimensionnalité des données pour améliorer les performances des modèles
- Normaliser les données pour les rendre comparables et cohérentes
- Équilibrer les classes pour éviter les biais de prédiction

Ces étapes d'entraînement seront appliquées aux données d'entraînement lors de la phase d'entraînement du modèle et aux données de test lors de la phase d'évaluation du modèle.

:::{attention}
Certaines étapes de pré-traitement utilisent des informations des données fournies pour appliquer des transformations au jeu de données. C'est par exemple le cas lorsque l'on normalise des valeurs numériques : on a besoin de connaître la moyenne et l'écart-type des données pour les normaliser. 

Si on applique ces transformations sur l'ensemble des données (entraînement et test) avant de séparer les données, on risque de biaiser les résultats du modèle car il aura accès à des informations des données de test lors de l'entraînement. Il est donc important de séparer les données en deux jeux distincts : un jeu d'entraînement et un jeu de test. Le jeu d'entraînement est utilisé pour entraîner le modèle, tandis que le jeu de test est utilisé pour évaluer les performances du modèle sur des données non vues.
:::

Ces étapes de pré-traitement sont réalisées au sein d'une pipeline `scikit-learn` qui permet de chaîner les différentes étapes de traitement des données et de les appliquer de manière cohérente. Et ainsi de réduire le risque de fuites de données entre les jeux d'entraînement et de test.

Ci-dessous sont présentées les différentes étapes de pré-traitement des données textuelles appliquées dans ce projet.

### Objectifs principaux du projet.

### Présentation des données

### Description des jeux de données utilisés (caractéristiques, taille, équilibre des classes, etc.).

### Prétraitement éventuel des données (normalisation, gestion des valeurs manquantes).

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/classification-experiments) sous licence MIT.
+++