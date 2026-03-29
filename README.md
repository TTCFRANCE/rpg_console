# RPG Console (Python)

## Description
Ce projet est un mini jeu de combat en console réalisé en Python.  
Il met en scène un joueur et un ennemi qui s'affrontent automatiquement jusqu'à la victoire de l'un des deux.

## Objectif
J'ai réalisé ce projet pour apprendre :
- la programmation orientée objet (classes, attributs, méthodes)
- la gestion de la logique d'un jeu simple
- les conditions et boucles en Python

## Fonctionnalités
- Création d'un personnage avec des statistiques (vie, attaque)
- Système de combat automatique
- Vérification de l'état (vivant ou mort)
- Affichage du déroulement du combat

## Fonctionnement
- Deux personnages sont créés : un joueur et un ennemi
- À chaque tour :
  - le joueur attaque
  - si l'ennemi est encore vivant, il riposte
- Le combat continue jusqu'à ce que l'un des deux meure

## Structure du code
- Classe `Personnage`
  - `attaquer(cible)` : inflige des dégâts
  - `est_vivant()` : vérifie si le personnage est encore en vie

## Technologies utilisées
- Python

## Lancer le projet
1. Installer Python
2. Exécuter le fichier :
```bash
python rpg_console.py
