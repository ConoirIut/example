# -*- coding: utf-8 -*-

'''
:titre: Affichage du contenu d'une grille dans une fenêtre
:author: L. Conoir
:date: mars 2018, maj décembre 2019

Voir exemple() en fin de script
'''

# Import de la librairie Tkinter
from tkinter import *

# Définition de variables
TAILLE_MAX = 600               # taille maximale de la fenêtre (en pixels)
BORDURE = 10                   # taille de la bordure entre la grille et la fenêtre (en pixels)
CONTOUR = 2                    # épaisseur du trait de contour de la grille (en pixels)

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
## Tracé de la grille
#####################################################################################################
def trace_grille(ligne, colonne, dessin) :
    
    # définition de la taille d'une case
    cote = taille_case(ligne,colonne)
    
    # tracé de la bordure de la grille
    dessin.create_rectangle(BORDURE-CONTOUR//2, BORDURE-CONTOUR//2, BORDURE + colonne * cote + CONTOUR//2, BORDURE + ligne * cote + CONTOUR//2, width = CONTOUR, tags = 'black')
        
    # tracé des lignes et colonnes de la grille
    for x in range(1,colonne) :
        dessin.create_line (BORDURE + x * cote, BORDURE, BORDURE + x * cote, BORDURE + ligne * cote, width = 1, fill = 'light grey')
    for y in range(1,ligne) :
        dessin.create_line (BORDURE, BORDURE + y * cote, BORDURE + colonne * cote, BORDURE + y * cote, width = 1, fill = 'light grey')
        
    dessin.update()
    


#####################################################################################################
## Création d'un widget Canvas de la bibilothèque Tkinter
#####################################################################################################
def creation_grille(grille) :
    '''La fonction affiche et renvoie un widget Canvas (bibliothèque Tkinter) permettant de dessiner une grille vide
correspondant à la taille de la grille donné en paramètre.

:param: grille, type list, liste de listes représentant une grille en 2 D
:CU: grille est de type list
:bord_effect: affichage d'une fenêtre à l'écran
:return: type Canvas, taille de la case en pixels
'''
    ligne, colonne = len(grille), len(grille[0])
    
    # définition de la taille d'une case
    cote = taille_case(ligne,colonne)
   
   
    # titre de la fenêtre Tkinter
    fenetre.title("Grille " + str(ligne) + " x " + str(colonne))
    
    # création du widget Canvas
    canevas = Canvas(fenetre, width = colonne * cote + 2 * BORDURE - CONTOUR, height = ligne * cote + 2 * BORDURE - CONTOUR, bg = 'white', borderwidth = 0)
    
    # affichage du widget Canvas
    canevas.pack(side = LEFT, padx = 5, pady = 5)
    
    
#    
#    btn0 = Button(fenetre, text = 'texte0')
#    btn1 = Button(fenetre, text = 'texte1')
#    btn2 = Button(fenetre, text = 'texte2')
#    btn0.pack(side = TOP, padx = 5, pady = 5)
#    btn1.pack(side = BOTTOM, padx = 5, pady = 5)
#    btn2.pack(side = RIGHT, padx = 5, pady = 5)
    
    # tracé de la grille
    trace_grille(ligne,colonne,canevas)
    
    return canevas
 

#####################################################################################################
## Remplissage des cases de la grille en fonction de son contenu
#####################################################################################################
def coloration(grille,dessin) :
    '''La fonction affiche le widget Canvas 'dessin' en remplissant les cases de la grille,
suivant les valeurs contenus dans celle-ci.

:param: grille, type list, liste de listes représentant une grille en 2 D
:param: type Canvas, dessin de la grille
:CU: grille est de type list, dessin est de type Canvas
:bord_effect: mise à jour d'une fenêtre à l'écran
:return: None
'''
    ligne, colonne = len(grille), len(grille[0])
    cote = taille_case(ligne,colonne)
    
    dessin.delete(ALL)
    
    for lig in range(ligne) :
        for col in range(colonne) :
            
            x = BORDURE + col * cote    # abscisse du coin supérieur gauche de la case
            y = BORDURE + lig * cote    # ordonéee du .....
            
            if grille[lig][col] == 1 :                                                         # si la case contient le nombre 1
                
                dessin.create_rectangle(x, y, x + cote, y + cote, width = 0, fill = 'black')    # tracé et coloration de la case en noir
            else :
                dessin.create_rectangle(x, y, x + cote, y + cote, width = 0, fill = 'white')    # tracé et coloration de la case en blanc
    
    # tracé de la grille
    trace_grille(ligne,colonne,dessin)
    
    
#####################################################################################################
## Exemple d'utilisation de ce module
#####################################################################################################
def exemple() :
    tab = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
    dessin = creation_grille(tab)    # création de la fenêtre contenant la grille
    coloration(tab,dessin)           # coloration, sur le dessin, des cases en fonction de la grille