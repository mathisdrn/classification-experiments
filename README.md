# Classification Experiment

This repository hosts the code and markdown that present and implement several classification techniques. The page is hosted at [https://mathisdrn.github.io/classification-experiments/](https://mathisdrn.github.io/classification-experiments/).

More information about the project can be found below or in [PROJECT.pdf](https://mathisdrn.github.io/classification-experiments/blob/main/PROJET.pdf).

## Description du projet

Ce projet porte sur l’apprentissage dans un contexte de classification binaire.
Ce travail se composera d’un dossier retraçant vos démarches et résultats entrepris pour traiter le sujet, de plus amples explications vous sont données ci-dessous.

### Travail à effectuer

Votre travail se décomposera en trois parties. Pour les différentes phases de votre travail, vous devrez :

- présenter les algorithmes/méthodes employé(e)s
- le protocole expérimental afin que la présentation permette la reproduction des résultats obtenus
- concevoir des variantes personnelles des algorithmes standards (i.e. combinaison avec des méthodes d’échantillonnage, cost-sensitive, etc.)
- évaluer le temps d’apprentissage des algorithmes

On prendra par exemple soin de préciser quelles sont les mesures de performances employées ou encore les loss optimisées dans le cas où cette dernière est personnalisée.

#### 1. Approches non paramétrique

Dans cette première partie, vous concentrerez sur des approches basées sur l’algorithme des k-plus proches voisins uniquement.
Vous devrez rappeler le fonctionnement de l’algorithme et la comparer au moins avec sa variante présentée en cours : Condensed Nearest Neighbor.

#### 2 Approches paramétrique linéaires

Dans cette deuxième partie, on va chercher à comparer les algorithmes qui apprennent des classifieurs linéaires

- SVM linéaire (ou noyau linéaire, éventuellement gaussien, mais ce n’est pas très fair en pratique)
- Régression logistique

A nouveau, on proposera au moins deux variantes pour ces deux algorithmes qui permettent d’améliorer les performances de base de ces algorithmes.

#### 3 Approches non linéaires

Dans cette dernière partie, on va chercher à tester les approches non linéaires ou par boosting :
- Arbres de décisions / Forêts aléatoires
- Adaboost

### Quelques suggestions

N’hésitez pas à regarder sur internet quelques exemples d’utilisations des algorithmes sus-mentionnés et votre objectif sera de les adapter au contexte des données.

#### Introduction

Vous présenterez rapidement le contexte du projet les objectifs et vous pourrez également présenter les caractéristiques des jeux de données considérées.

#### Méthodologie

Pour chaque partie, vous procéderez de la façon suivante
Vous commencerez par présenter les notations que vous allez employer tout au long de la rédaction de votre rapport.
Vous présenterez ensuite les outils que vous allez utiliser dans la partie expérimentale. On commencera par parler de ce que l’on souhaite maximiser : ici l’accuracy par exemple, en la définissant avant de s’attaquer à la présentation des algorithmes.
Par exemple, si vous faites une contribution basée sur du boosting et que vous combinez avec des méthodes à noyaux, il faudra rappeler ce qu’est le boosting, ce que sont les méthodes à noyaux (ce sont les approches de bases) et ensuite vous expliquerez comment vous combinez les deux pour résoudre le problème confié.
Il ne faut pas hésiter à présenter le processus de façon abstraite, c’est-à-dire avec des notations mathématiques et ne pas être uniquement verbeux.
Un pseudo-code est également appréciable pour synthétiser l’approche proposée.
Dans le cas ou vous proposez plusieurs approches à des fins de comparaisons, il faudra prendre soin de présenter les différentes approches et de justifier pourquoi vous intéressez à ces approches là.

Remarque : il n’est pas nécessaire de présenter tous les algorithmes employés, mais uniquement ceux qui servent à l’élaboration d’une version "exotique".

#### Expériences

Vous dresserez ensuite votre protocole expérimentale qui présentera la ou les méthodes sélectionnées pour répondre à la tache demandée. Celui-ci comprend en général trois parties.

#### Protocole expérimental

Pour chaque partie, vous procéderez de la façon suivante

Vous présentez rapidement les expériences que vous allez faire, i.e. les différents algorithmes testés, le range des hyper-paramètres employés ainsi que la façon dont sont optimisées ces hyper-paramètres (cross-validation en k-folds, simple validation ou est-ce que vous faites le choix de les fixer). Quels sont vos ensembles d’entraînement/validation/test ?
Les informations que vous fournissez dans cette section doivent permettre au lecteur de pouvoir reproduire les résultats que vous allez présenter dans la sous-section suivante.

#### Résultats

Ici vous allez présenter et analyser les résultats obtenus à l’aide de graphiques et/ou tableaux. Outre les performances, on pourra aussi s’intéresser au critère de rapidité d’un algorithme.
L’analyse doit aussi permettre de mettre en exergue les avantages inconvénients des méthodes proposées. Cela peut passer par l’utilisation d’autres mesures de performances/critères pour évaluer/comparer vos algorithmes.

#### Conclusions

Il s’agit de conclure quant à votre étude. Reprendre le travail proposé et les principales conclusions. Il est également important de proposer des perspectives à votre travail en fonction des résultats obtenus et de l’approche proposée


## Usage

To run the code in this repository, you need to install dependencies from the `uv.lock` or `pyproject.toml` file.

Once the environment is installed and activated, you can serve a static webpage of these documents by running the following command in your terminal:

```bash
myst start
```