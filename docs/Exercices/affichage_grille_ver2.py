# -*- coding: utf-8 -*-
'''
:titre: Affichage du contenu d'un tableau ou d'un dictionnaire dans une fenêtre graphique
:author: L. Conoir
:date: mars 2018, maj février 2020


Exemples d'utilisation du module :

Exemple 1 : avec un tableau

    tab = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]   # exemple de tableau
    dessin = creation_grille(tab)             # création de la fenêtre contenant la grille (un seul appel nécessaire)
    coloration(tab,dessin)                    # coloration, sur le dessin, des cases en fonction du tableau

Exemple 2 : avec un dictionnaire

    dico = {(0, 1): 1,                        # exemple de dictionnaire
            (1, 0): 1,
            (2, 0): 1, (2, 1): 1, (2, 2): 1}
    dessin = creation_grille_col_lig(3, 3)    # création de la fenêtre contenant la grille 3 x 3 (un seul appel nécessaire)
    coloration_dict(dico, 3, 3, dessin)       # coloration, sur le dessin, des cases en fonction du dictionnaire
    
'''

# Import de la librairie Tkinter
from tkinter import *

# Définition de variables
TAILLE_MAX = 400               # taille maximale de la fenêtre (en pixels)
BORDURE = 10                   # taille de la bordure entre le tableau et la fenêtre (en pixels)
CONTOUR = 2                    # épaisseur du trait de contour du tableau (en pixels)

# Création de la fenêtre d'affichage (bibliothèque Tkinter)
fenetre = Tk()

#####################################################################################################
## Taille des cases carrées de la grille
#####################################################################################################
def taille_case(nb_ligne,nb_colonne) :
    '''La fonction renvoie la taille optimale, en pixels, d'une case carrée pour une grille comportant 'nb_ligne' lignes
et 'nb_colonne' colonne, dans une fenêtre dont la taille ne dépasse pas 'TAILLE_MAX' pixels.

:param: nb_ligne, type int, nombre de lignes de la grille
:param: nb_colonne, type int, nombre de colonnes de la grille
:CU: nb_ligne et nb_colonne sont des nombres entiers positifs
:bord_effect: None
:return: type int, taille de la case en pixels

:examples:
>>> TAILLE_MAX, BORDURE, CONTOUR = 600, 10, 2
>>> taille_case(10,10)
61
>>> taille_case(50,40)
12
'''
    return (TAILLE_MAX + 2 * BORDURE - 2 * CONTOUR) // max(nb_ligne, nb_colonne)


#####################################################################################################
## Tracé du tableau
#####################################################################################################
def trace_tableau(ligne, colonne, dessin) :
    
    # définition de la taille d'une case
    cote = taille_case(ligne,colonne)
    
    # tracé de la bordure du tableau
    dessin.create_rectangle(BORDURE-CONTOUR//2, BORDURE-CONTOUR//2, BORDURE + colonne * cote + CONTOUR//2, BORDURE + ligne * cote + CONTOUR//2, width = CONTOUR, tags = 'black')
        
    # tracé des lignes et colonnes de la grille
    for x in range(1,colonne) :
        dessin.create_line (BORDURE + x * cote, BORDURE, BORDURE + x * cote, BORDURE + ligne * cote, width = 1, fill = 'light grey')
    for y in range(1,ligne) :
        dessin.create_line (BORDURE, BORDURE + y * cote, BORDURE + colonne * cote, BORDURE + y * cote, width = 1, fill = 'light grey')
        
    dessin.update()
    


#####################################################################################################
## Création d'un widget Canvas de la bibilothèque Tkinter à partir d'un tableau
#####################################################################################################
def creation_grille(tableau) :
    '''La fonction affiche et renvoie un widget Canvas (bibliothèque Tkinter) permettant de dessiner une grille vide
correspondant à la taille du tableau donné en paramètre.

:param: tableau, type list, liste de listes représentant un tableau en 2 D
:CU: tableau est de type list
:bord_effect: affichage d'une fenêtre à l'écran
:return: type Canvas, taille de la case en pixels
'''
    ligne, colonne = len(tableau), len(tableau[0])
    
    # définition de la taille d'une case
    cote = taille_case(ligne,colonne)
   
   
    # titre de la fenêtre Tkinter
    fenetre.title("Grille " + str(ligne) + " x " + str(colonne))
    
    # création du widget Canvas
    canevas = Canvas(fenetre, width = colonne * cote + 2 * BORDURE - CONTOUR, height = ligne * cote + 2 * BORDURE - CONTOUR, bg = 'white', borderwidth = 0)
    
    # affichage du widget Canvas
    canevas.pack(side = LEFT, padx = 5, pady = 5)
    
    # tracé du tableau
    trace_tableau(ligne,colonne,canevas)
    
    return canevas



#####################################################################################################
## Création d'un widget Canvas de la bibilothèque Tkinter à partir d'un tuple (ligne, colonne)
#####################################################################################################
def creation_grille_col_lig(colonne, ligne) :
    '''La fonction affiche et renvoie un widget Canvas (bibliothèque Tkinter) permettant de dessiner une grille vide
correspondant à la taille du tableau donné en paramètre.

:param: tableau, type list, liste de listes représentant un tableau en 2 D
:CU: tableau est de type list
:bord_effect: affichage d'une fenêtre à l'écran
:return: type Canvas, taille de la case en pixels
'''
    # définition de la taille d'une case
    cote = taille_case(ligne, colonne)
   
   
    # titre de la fenêtre Tkinter
    fenetre.title("Grille " + str(ligne) + " x " + str(colonne))
    
    # création du widget Canvas
    canevas = Canvas(fenetre, width = colonne * cote + 2 * BORDURE - CONTOUR, height = ligne * cote + 2 * BORDURE - CONTOUR, bg = 'white', borderwidth = 0)
    
    # affichage du widget Canvas
    canevas.pack(side = LEFT, padx = 5, pady = 5)
    
    # tracé du tableau
    trace_tableau(ligne,colonne,canevas)
    
    return canevas



#####################################################################################################
## Remplissage des cases du dessin en fonction du contenu d'un tableau
#####################################################################################################
def coloration(tableau,dessin) :
    '''La fonction affiche le widget Canvas 'dessin' en remplissant les cases de la grille,
suivant les valeurs contenus dans le tableau.

:param: tableau, type list, liste de listes représentant un tableau en 2 D
:param: dessin, type Canvas, dessin de la grille
:CU: tableau est de type list, dessin est de type Canvas
:bord_effect: mise à jour d'une fenêtre à l'écran
:return: None
'''
    ligne, colonne = len(tableau), len(tableau[0])
    cote = taille_case(ligne,colonne)
        
    dessin.delete(ALL)
    
    
    for lig in range(ligne) :
        for col in range(colonne) :
            
            x = BORDURE + col * cote    # abscisse du coin supérieur gauche de la case
            y = BORDURE + lig * cote    # ordonéee du .....
            
            if tableau[lig][col] == 1 :                                                         # si la case contient le nombre 1
                
                dessin.create_rectangle(x, y, x + cote, y + cote, width = 0, fill = 'black')    # tracé et coloration de la case en noir
            else :
                dessin.create_rectangle(x, y, x + cote, y + cote, width = 0, fill = 'white')    # tracé et coloration de la case en blanc
                
    # tracé du tableau
    trace_tableau(ligne, colonne, dessin)



#####################################################################################################
## Remplissage des cases du dessin en fonction du contenu d'un dictionnaire
#####################################################################################################
def coloration_dict(dico, colonne, ligne, dessin) :
    '''La fonction affiche le widget Canvas 'dessin' en remplissant les cases de la grille,
suivant les valeurs contenus dans le dictionnaire.

:param: tableau, type list, liste de listes représentant un tableau en 2 D
:param: dessin, type Canvas, dessin de la grille
:CU: tableau est de type list, dessin est de type Canvas
:bord_effect: mise à jour d'une fenêtre à l'écran
:return: None
'''
    cote = taille_case(ligne,colonne)
    couleurs = {0:'white', 1:'black', 2:'light grey'}     # dictionnaire de couleurs appliquées
    
    dessin.delete(ALL)
    
    
    for (col, lig), valeur in dico.items() :
        
        x = BORDURE + (col-1) * cote    # abscisse du coin supérieur gauche de la case
        y = BORDURE + (lig-1) * cote    # ordonéee du .....
            
        dessin.create_rectangle(x, y, x + cote, y + cote, width = 0, fill = couleurs[valeur])    # tracé et coloration de la case en fonction du dict. de couleurs
            
    # tracé du tableau
    trace_tableau(ligne, colonne, dessin)



#####################################################################################################
## Exemples d'utilisation de ce module
#####################################################################################################
def exemple1() :
    tab = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
    dessin = creation_grille(tab)    # création de la fenêtre contenant la grille
    coloration(tab,dessin)           # coloration, sur le dessin, des cases en fonction du tableau
    
def exemple2() :
    dico = {(0, 1): 1,                        # exemple de dictionnaire
            (1, 0): 1,
            (2, 0): 1, (2, 1): 1, (2, 2): 1}
    dessin = creation_grille_col_lig(3, 3)    # création de la fenêtre contenant la grille 3 x 3 (un seul appel nécessaire)
    coloration_dict(dico, 3, 3, dessin)       # coloration, sur le dessin, des cases en fonction du dictionnaire