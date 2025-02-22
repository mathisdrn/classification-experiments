---
title: Classification binaire
---

### Introduction

La classification est un type de problème de machine learning supervisé dans lequel l'objectif est de classer les données au sein de catégories distinctes. Chaque exemple dans les données est ainsi étiqueté comme appartenant à l'une des catégories appelée classe et un modèle de classification est entraîné pour prédire la classe d'un nouvel exemple en fonction de ses caractéristiques.

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

### Objectifs principaux du projet.

### Présentation des données

### Description des jeux de données utilisés (caractéristiques, taille, équilibre des classes, etc.).

### Prétraitement éventuel des données (normalisation, gestion des valeurs manquantes).

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/classification-experiments) sous licence MIT.
+++