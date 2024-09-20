# -*- coding: utf-8 -*-
'''
:Titre : Travail préparatoire au projet 2
:Auteur : L. Conoir
:Date : 12/2019

Correction des activités
'''

######################################################################
### Activité 1 : Construction d'une grille vide
######################################################################
def creer_grille(horizontal, vertical) :
    '''La fonction renvoie renvoie un tableau de tableaux correspondant
à une grille aux dimensions souhaitées (horizontal, vertical)

:param: horizontal, type int, nombre de cases horizontales
:param: vertical, type int, nombre de cases verticales
:return: type list, la grille créé
:CU: horizontal et vertical sont 2 entiers positifs, non nuls

:examples:
>>> creer_grille(3, 4)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> creer_grille(5, 4)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''
    return [[0 for nb_col in range(horizontal)] for nb_lig in range(vertical)]


######################################################################
### Activité 2 : Dimensions d'une grille
######################################################################
def hauteur_grille(grille) :
    '''La fonction renvoie le nombre de cases verticales d'une grille.

:param: grille, type list, une grille formée d'un tableau de tableaux
:return , type int, le nombre de cases verticales
:CU: grille est de type list

:examples:
>>> hauteur_grille([[0, 1, 0], [1, 0, 1]])
2
>>> hauteur_grille(creer_grille(4, 5))
5
'''
    return len(grille)     # le tableau de tableaux 'grille' sont les lignes


def largeur_grille(grille) :
    '''La fonction renvoie le nombre de cases horizontales d'une grille.

:param: grille, type list, une grille formée d'un tableau de tableaux
:return , type int, le nombre de cases horizontales
:CU: grille est de type list

:examples:
>>> largeur_grille([[0, 1, 0], [1, 0, 1]])
3
>>> largeur_grille(creer_grille(4, 5))
4
'''
    if len(grille) > 0 :        # si grille contient au moins une ligne
        
        return len(grille[0])   # dans le tableau de tableaux 'grille' se trouvent les éléments de chaque colonne
                                 # grille[0] correspond à la première ligne
    else :
        return 0                 # pas de ligne --> pas de colonne

######################################################################
### Activité 3 : Initialisation d'une grille
######################################################################
def creer_grille_aleatoire(horizontal, vertical, p) :
    '''La fonction renvoie un tableau de tableaux correspondant
à une grille aux dimensions souhaitées (horizontal, vertical).
Chaque case de la grille a une parpobabilité p d'être occupée.

:param: horizontal, type int, nombre de cases horizontales
:param: vertical, type int, nombre de cases verticales
:param: p, type float, probabilité
:return: type list, la grille créée
:CU: horizontal et vertical sont 2 entiers positifs, non nuls

:examples:
>>> creer_grille_aleatoire(3, 2, 1)
[[1, 1, 1], [1, 1, 1]]
>>> creer_grille_aleatoire(3, 2, 0)
[[0, 0, 0], [0, 0, 0]]
'''
    from random import random                       # de la biblio. random, on importe la fonction random
    
    grille = creer_grille(horizontal, vertical)   # on crée une grille vide
    
    for nb_lig in range(vertical) :                 # ligne par ligne
        
        for nb_col in range(horizontal) :           # colonne par colonne dans la ligne 'nb_lig'
        
            if random() <= p :                      # si un nombre pris aléatoirement entre 0 et 1 (compris)
                                                    # est inférieur à la probabilité
                grille[nb_lig][nb_col] = 1         # on déclare remplie la case
    
    return grille

## Version par compréhension, sans utiliser la fonction 'creer_grille',
## et en utilisant le principe :  int(True) = 1     (case occupée)
##                                int(False) = 0    (case vide)

    return [[int(random() < p) for nb_col in range(horizontal)] for nb_lig in range(vertical)]


######################################################################
### Activité 4 : Afficher une grille
######################################################################
def afficher_grille(grille) :
    '''La fonction affiche une grille de cette manière :
- les cases vides seront affichées avec un tiret bas (`_`) et les cases
  contenant quelque chose seront affichées avec un O majuscule (`O`).
- le contenu des cases sera séparé par un espace.
- chaque ligne de la grille sera affichée sur une ligne distincte.

:param: grille, type list, une grille formé d'un tableau de tableaux
:return: None
:CU: grille est de type list
:bord effect: affichage sur l'écran

:examples:
>>> grille = [[0, 1, 0],[1, 0, 0],[1, 1, 1]]
>>> afficher_grille(grille)
_ O _
O _ _
O O O
>>> afficher_grille(creer_grille(3, 2))
_ _ _
_ _ _
>>> afficher_grille(creer_grille_aleatoire(3, 2, 1))
O O O
O O O
'''   
    for nb_lig in range(hauteur_grille(grille)) :        # ligne par ligne
        
        ligne_affichee = ''                                # préparation d'une ligne d'affichage
        
        for nb_col in range(largeur_grille(grille)) :      # colonne par colonne
            
            if grille[nb_lig][nb_col] == 0 :
                ligne_affichee = ligne_affichee + '_ '       # on ajoute à 'ligne_affichee'
            else :                                           # en fonction du contenu de la case
                ligne_affichee = ligne_affichee + 'O '       # et en ajoutant un espace
        
        print(ligne_affichee[:-1])                         # on affiche la ligne en retirant le dernier espace


######################################################################
### Activité 5 : Voisins d'une case
######################################################################
def voisins_case(grille, x, y) :
    '''La fonction prend en paramètre une grille ainsi que les coordonnées
en abscisse et en ordonnée d'une case (0,0 étant la case en haut à gauche).
La fonction renvoie alors un tableau contenant la valeur des cases voisines
de la case donnée en paramètre.

:param: grille, type list, une grille formé d'un tableau de tableaux
:param: x, type int, abscisse de la case
:param: y, type int, ordonnée de la case
:return: type list, le tableau du contenu des cases voisines
:CU: grille est de type list, x et y sont entiers positifs
:bord effect: None

:examples:
>>> grille = [[0, 1, 0],[1, 0, 0],[1, 1, 1]]
>>> voisins_case(grille, 1, 1)
[0, 1, 0, 1, 0, 1, 1, 1]
>>> voisins_case(grille, 2, 2)
[0, 0, 1]
>>> voisins_case(grille, 0, 2)
[1, 0, 1]
'''
    tableau = []                              # préparation du tableau des cases voisines
    largeur = largeur_grille(grille)
    hauteur = hauteur_grille(grille)
    
    if y > 0 :                              # si la case n'est pas sur la première ligne
        
        if x > 0 :                              # si la case n'est pas dans la première colonne
            tableau.append(grille[y-1][x-1])         # ajout de la case au dessus, à gauche
        
        tableau.append(grille[y-1][x])           # ajout de la case au dessus
        
        if x + 1 < largeur :                    # si la case n'est pas dans la dernière colonne
            tableau.append(grille[y-1][x+1])         # ajout de la case au dessus, à droite
            
    if x > 0 :                              # si la case n'est pas dans la première colonne
        tableau.append(grille[y][x-1])           # ajout de la case à gauche
    
    if x + 1 < largeur :                    # si la case n'est pas dans la dernière colonne
        tableau.append(grille[y][x+1])           # ajout de la case à droite
    
    if y + 1 < hauteur :                    # si la case n'est pas dans la dernière ligne
        
        if x > 0 :                              # si la case n'est pas dans la première colonne
            tableau.append(grille[y+1][x-1])         # ajout de la case en dessous, à gauche
        
        tableau.append(grille[y+1][x])           # ajout de la case en dessous
        
        if x + 1 < largeur :                    # si la case n'est pas dans la dernière colonne
            tableau.append(grille[y+1][x+1])         # ajout de la case en dessous, à droite
    
    return tableau


######################################################################
### Activité 6 : Nombre de cases occupées dans le voisinage
######################################################################
def nb_cases_voisins_occup(grille, x, y) :
    '''La fonction prend en paramètre une grille ainsi que les coordonnées
d'une case et renvoie le nombre de cases occupées dans les cases voisines
de la case passée en paramètre.

:param: grille, type list, une grille formé d'un tableau de tableaux
:param: x, type int, abscisse de la case
:param: y, type int, ordonnée de la case
:return: type int, le nombre de cases voisines occupées
:CU: grille est de type list, x et y sont entiers positifs
:bord effect: None

:examples:
>>> grille = [[0, 1, 0],[1, 0, 0],[1, 1, 1]]
>>> nb_cases_voisins_occup(grille, 1, 1)
5
>>> nb_cases_voisins_occup(grille, 2, 2)
1
'''
    somme = 0
    for element in voisins_case(grille, x, y) :      # pour chaque élément du tableau renvoyéepar 'voisins_case'
        somme = somme + element
    return somme
    
## ou plus rapidement avec la fonction sum() pour les tableaux de nombres
    return sum(voisins_case(grille, x, y))


######################################################################
### Vérification des tests mis en examples dans les fonctions
######################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()