---
title: Classification binaire
---

+++ {"part": "abstract"}
Ce document vise à présenter, implémenter et comparer divers algorithmes de classification binaire. Leur évaluation est réalisée sur un ensemble de 28 jeux de données, en tenant compte de critères de performance ainsi que du temps d'exécution.
+++

## Introduction

La **classification** est une tâche fondamentale en apprentissage automatique qui consiste à prédire la classe d'un objet en fonction de ses caractéristiques. Il s'agit par exemple de prédire:
- la nature d'un email (spam ou non-spam) à partir du contenu du mail
- la maladie d'un patient (malade ou en bonne santé) à partir de ses symptômes

Ces exemples illustrent des problèmes de **classification binaire** où les données sont séparées en deux classes distinctes : la classe positive (1) qui représente l'événement à prédire et la classe négative (0) qui représente l'absence de l'événement à prédire. Il existe également des problèmes de **classification multiclasse** où les données sont séparées en plusieurs classes distinctes:
- la reconnaissance de caractères (26 classes pour les lettres de l'alphabet)
- la reconnaissance d'images (1000 classes pour les images de la base de données ImageNet)

## Méthodes de classification

Dans le cadre de la classification et plus générallement du machine learning supervisé, on distingue deux familles d'approches pour construire un modèle prédictif:
- **Approches paramétriques** : ces modèles supposent que les données d'entraînement sont générées par une distribution de probabilité paramétrique. Les paramètres de cette distribution sont estimés à partir des données d'entraînement et utilisés pour prédire la classe d'un nouvel exemple. Le modèle de régression logistique est un exemple d'approche paramétrique.
- **Approches non paramétriques** : ces modèles n'imposent pas de contraintes sur la forme de la distribution des données. Ils apprennent directement à partir des données sans supposer une forme particulière pour la distribution. Les arbres de décision, les forêts aléatoires et les k plus proches voisins (k-NN) sont des exemples d'approches non paramétriques.

Parmis ces deux familles, on distingue également les modèles linéaires et non linéaires :
- **Approches linéaires** : ces modèles supposent que la relation entre les caractéristiques et la classe cible est linéaire. Ils utilisent des fonctions linéaires pour modéliser cette relation et apprennent les coefficients de ces fonctions à partir des données d'entraînement. La régression logistique et l'analyse discriminante linéaire sont des exemples d'approches linéaires.
- **Approches non linéaires** : ces modèles sont capables de modéliser des relations non linéaires entre les caractéristiques et la classe cible. Ils utilisent des transformations non linéaires des caractéristiques pour apprendre des frontières de décision complexes. Les réseaux de neurones et les machines à vecteurs de support avec noyaux non linéaires sont des exemples d'approches non linéaires.


## Motivation du projet

Ce projet vise à mieux comprendre les performances, forces et faiblesses de différentes méthodes de classification:
- Améliorer le choix des algorithmes en fonction du contexte et des caractéristiques des données.  
- Étudier l’impact de techniques d’optimisation, comme la réduction de dimensions, l’ajustement des hyperparamètres et les méthodes d’échantillonnage.  
- Explorer des variantes des algorithmes classiques afin d’améliorer la qualité de la classification.  
- Proposer une méthodologie rigoureuse et reproductible pour évaluer objectivement les performances des modèles.

Pour cela, nous étudierons ces algorithmes au travers de ces trois familles d'algorithmes : les approches non paramétriques, les approches paramétriques et les approches non linéaires.

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/classification-experiments) sous licence MIT.
+++