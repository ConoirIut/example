# Les tableaux de tableaux
___
## Exercices

!!! question "Exercice 1 : Scrabble"
    Le Scrabble est un jeu de société où l'on doit former des mots avec un tirage aléatoire de lettres, chaque lettre valant un certain nombre de points. 

    Vous trouverez, dans la [règle du jeu](https://www.regles-de-jeux.com/regle-du-scrabble/){:target = _blank}, la valeur de chaque point. 

1. Créer le tableau `alphabet`, contenant les lettres de l'alphabet.  
*(Les lettres du scrabble sont exclusivement en majuscule.)*

2. Établir le tableau `points`, contenant les points de chaque lettre.  
*(dans le même ordre que alphabet)*

3. Établir le tableau `quantite`, contenant le nombre de jetons pour chaque lettre.

4. Créer une fonction `score` qui prend en paramètre un mot (type `str()`) et qui renvoie le total des points (type `int()`) pour ce mot.  
*(On ne tiendra pas compte des lettres jokers et des cases "mot compte double ou triple" du plateau. )*

5. Créer une fonction `tirage` qui renvoie une liste de sept lettres, en tenant compte des lettres déjà tirées. 
*(aide : random.choice)*


!!! question "Exercice 2 : Rendu monnaie"

1. Établir le tableau `monnaie` ordonnée des valeurs des pièces et billets en euros.

2. Établir une fonction `rendu` qui prend en paramètre une somme d'argent (type `float()`), et renvoie le tableau des pièces et billets totalisant cette somme.
