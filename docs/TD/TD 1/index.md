# Conditions - Boucles
___
## Méthode de travail

Un module python devra être créé pour chaque exercice avec le module `modele.py` fourni.

??? tip "`Modele.py` (TD 1)"
    ```python
    # -*- coding: utf-8 -*-
    '''
    :Titre :
    :Auteur : 
    :Date : 
    
    Exercice n°.. du TD n°..
    '''
    ```

Renommer le avant d'écrire du code : Fichier -> Save As

___
## Avant de commencer
 
L'utilisation de la fonction `input()` permettra à l'utilisateur du module de définir les valeurs des variables employées dans le programme.

Exemple : `reponse = input('Question')`
 
La `Question` sera affichée et la réponse donnée au clavier par l'utilisateur sera affectée comme valeur à la variable `reponse`.

!!! warning "La fonction input() renvoie une valeur de type str()" 
    Dans le cas où l'on souhaite recueillir une valeur entière, il faudrait plutôt écrire  
    `reponse = int(input('Question'))`  
    Afin de changer de type la réponse obtenue.  

___
## Exercices

!!! question "Exercice 1 :  Mineur ou majeur"

   1. Demander à l'utilisateur son âge. Affecter sa réponse à la variable `age`.

   2. En utilisant une instruction conditionnelle, afficher un texte précisant s'il est mineur ou majeur.


!!! question "Exercice 2 :   Joueur suivant"

1. Déclarer une variable `joueur_actuel` en y affectant la valeur `0`.

2. Déclarer une variable `nombre_tours` en y affectant la valeur `10`.  
   Un jeu se déroule en 10 tours de table, sous la direction d'un arbitre (utilisateur du programme).  
   A chaque tour, l'arbitre choisit le premier joueur (joueur1 ou joueur2) en donnant la valeur 1 ou 2.  
3. En utilisant une boucle, faire afficher le déroulement d'une partie :
	
    ```
    Tour n°1
    Quel est le premier joueur ? 1      # question posée à l'arbitre qui choisit 1, par exemple
    C'est au joueur1
    Puis au joueur2
    Tour n°2
    Quel est le premier joueur ? 2      # l'arbitre choisit ensuite 2, par exemple
    ...
    ...
    Fin de la partie.
    ```


!!! question "Exercice 3 : Identité d'une personne"

1. Compléter le module `identite.py` afin de collecter les informations suivantes :

    - date de naissance : jour, mois, année  
    - lieu de naissance : ville  
    - adresse : numéro, voie, code postal, ville

2. Écrire ensuite une structure conditionnelle utilisant la date de naissance et la date d'aujourd'hui, afin de définir l'âge de la personne. Une variable age sera créée dans ce cas.

3. Faire afficher le texte suivant, en y insérant automatiquement  les données collectées à la place des mots écrits en italique :

    **Je soussigné,** _Monsieur ou Madame (à préciser) nom prénom_**, né**_(e)_ **le** _date de naissance_ **à** _ville_**, demeurant** _adresse_, **certifie sur l'honneur l'exactitude des renseignements déclarés.**  
    **Fait le** _date d'aujourd'hui_


!!! question "Exercice 4 : Analyse et modification de texte"

    Voici un texte :
    !!! cite "[Les Creatives Commons](https://creativecommons.org/licenses/?lang=fr-FR){:target = _blank}"
         Les licences Creative Commons sont fondées sur le droit d’auteur. Alors que le régime du droit d’auteur classique vous incite à garder l’exclusivité sur la totalité de vos droits (« tous droits réservés »), ces licences vous encouragent à n’en conserver qu’une partie (« certains droits réservés »). Creative Commons travaille avec des experts en droit d’auteur dans le monde entier pour que ces licences soient valides quelle que soit la juridiction. Ces licences permettent au public d’utiliser vos œuvres, sous certaines conditions, selon vos préférences.

1. Écrire un programme permettant de compter les lettres 'a' dans ce texte.

2. Écrire un programme permettant de compter les voyelles dans ce texte.

3. Écrire un programme qui affiche ce texte après avoir **échangé** les lettres 'a' et 'e' ,  'i' et 'o'



!!! question "Exercice 5 :  Année bissextile"

    Une année est dite bissextile si c'est un multiple de 4, sauf si c'est un multiple de 100.  
    Toutefois, elle est considérée comme bissextile si c'est un multiple de 400.

1.  A partir avoir déclaré une variable `annee`, définir une suite d'instructions qui permettra de dire si la valeur de cette variable est bissextile.

2. A l'aide d'une boucle, déterminer les prochaines années bissextiles jusqu'en 2 500.


!!! question "Exercice 6 :  Quadrillage"

1. Demander à l'utilisateur un nombre entier de cases : variable `nb_cases`

2. A l'aide des caractères | (touches ++altgr++ + ++6++) et - (touche ++6++), réaliser le quadrillage de côté `nb_cases` :

```
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
|    |    |    |    |    |    |    |    |
-----------------------------------------
```
