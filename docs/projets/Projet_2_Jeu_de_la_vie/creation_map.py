# -*- coding: utf-8 -*-

'''
:titre: Mappeur de grille
:auteur: L. Conoir
:date: mai 2020
'''

# Import de la librairie Tkinter
from tkinter import *

NB_CASES_LARGEUR = 20
NB_CASES_HAUTEUR = 20
DIM_CASES = 20              # dimension d'une case carrée en pixels

dico_item = {}      # dictionnaire définissant la position de toutes les cases créées dans la grille
                    # [clé] est la valeur affectée par tkinter lors de la création de la case sur la grille
                    # valeur est un tuple précisant la position de la case dans la grille (colonne, ligne)

synthese_dico = {}     # dictionnaire définissant les cases noircies
                       # [clé] est la position de la case dans la grille (colonne, ligne)
                       # valeur 1 , précisant que la case est noircie


#############################################################################################################
def info(event):
    '''La fonction affiche la position de la case située en dessous de la souris.

:param: event, événement détecté
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    objet = zone_grille.find_closest(event.x,event.y)
    
    position = dico_item.get(objet[0])
    
    if position != None :
        texte = str(position[0]) + '                 ' + str(position[1])
        valeurs_position.config(text = texte)
    
#############################################################################################################
def alterne_couleur(event) :
    '''La fonction change la couleur intérieure de la case se trouvant en-dessous de la souris.

:param: event, événement détecté
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    objet = zone_grille.find_closest(event.x, event.y)
    
    if objet[0] in dico_item.keys() :
    
        fill = zone_grille.itemcget(objet, 'fill')
        position = dico_item[objet[0]]
        
        if fill == 'white' :
            zone_grille.itemconfig(objet, fill = 'black')
            synthese_dico[position] = 1
        else :
            zone_grille.itemconfig(objet, fill = 'white')
            del synthese_dico[position]

#############################################################################################################
def couleur_noir(event) :
    '''La fonction change la couleur intérieure en noir pour la case se trouvant en-dessous de la souris.

:param: event, événement détecté
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    objet = zone_grille.find_closest(event.x, event.y)
    
    if objet[0] in dico_item.keys() :
        position = dico_item[objet[0]]
        synthese_dico[position] = 1
        zone_grille.itemconfig(objet, fill = 'black')
        
#############################################################################################################
def couleur_blanc(event) :
    '''La fonction change la couleur intérieure en blanc pour la case se trouvant en-dessous de la souris.

:param: event, événement détecté
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    objet = zone_grille.find_closest(event.x, event.y)
    
    if objet[0] in dico_item.keys() :
    
        position = dico_item[objet[0]]
        
        if position in synthese_dico :
            del synthese_dico[position]
            zone_grille.itemconfig(objet, fill = 'white')

#############################################################################################################
def table() :
    '''La fonction affiche dans la console la valeur d'un tableau de tableaux représentant la grille complète.
Chaque tableau représente une ligne de la grille. Les items des tableaux sont des entiers :
        0 pour pour une case blanche
        1 pour une case noircies
Le nombre d'item d'un tableau correspond aux nombre de colonnes de la grille.

:param: None
:return: None
:CU: None
:bord_effect: Affichage dans la console
'''
    synthese_table = [[0 for largeur in range(NB_CASES_LARGEUR)] for hauteur in range(NB_CASES_HAUTEUR)]
    
    for position in synthese_dico.keys() :
        synthese_table[position[1]][position[0]] = 1
    
    print('Table :')
    dernier_rang = len(synthese_table)
    print('[' + str(synthese_table[0]) + ',')
    
    for rang in range(1, dernier_rang - 1) :
        print(str(synthese_table[rang]) + ',')
    
    print(str(synthese_table[dernier_rang - 1]) + ']')

#############################################################################################################
def tableau() :
    '''La fonction affiche dans la console la valeur d'un tableau représentant les cases noircies sur la grille.
Chaque item du tableau correspond à la position d'une case sous forme de tuple.

:param: None
:return: None
:CU: None
:bord_effect: Affichage dans la console
'''
    tableau = list(synthese_dico.keys())
    tableau.sort()
    print('Tableau :\n', tableau)

#############################################################################################################
def dictionnaire() :
    '''La fonction affiche dans la console la valeur d'un dictionnaire représentant les cases noircies sur la grille.
La clé est la position d'une case sous forme de tuple. La valeur associée est 1. Les cases blanches ne sont pas référencée.

:param: None
:return: None
:CU: None
:bord_effect: Affichage dans la console
'''
    print('Dictionnaire :\n', synthese_dico)


#############################################################################################################
def effacer() :
    '''La fonction efface toutes les cases noircies.

:param: None
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    for case in zone_grille.find_withtag('case') :
    
        zone_grille.itemconfig(case, fill = 'white')   
    
#############################################################################################################
def creation_grille() :
    '''La fonction crée une grille dans le zone_grille de la fenêtre. Cette grille est composée de cases référencées
dans deux dictionnaires.

:param: None
:return: None
:CU: None
:bord_effect: Modification de la fenêtre d'affichage
'''
    
    dico = {}
    
    for y in range(NB_CASES_HAUTEUR):                                            # en hauteur

        for x in range(NB_CASES_LARGEUR):                                        # en largeur
            
                   # creation d'une case rectangulaire dans "zone_grille"
            item = zone_grille.create_rectangle((5 + x * DIM_CASES, 5 + y * DIM_CASES),                           # coin supérieur gauche
                                                (x * DIM_CASES + DIM_CASES + 5, y * DIM_CASES + DIM_CASES + 5),   # coin inférieur droit
                                                outline = 'light grey',                 # couleur  bordure
                                                fill = 'white',                         # couleur intérieure                   
                                                tag = 'case',                           # étiquetée 'case'
                                                activefill = 'light grey')              # couleur intérieure si la case est survolée par la souris
            
            dico[item] = (x,y)                  # affectation de la valeur 'position' pour la clé 'item'
        
    for x in range(0, NB_CASES_LARGEUR + 1, 5) :                                 # quadrillage secondaire en noir
        zone_grille.create_line((5 + x * DIM_CASES, 5),
                           (5 + x * DIM_CASES, 5 + NB_CASES_HAUTEUR * DIM_CASES),
                           fill = 'black')
            
    for y in range(0, NB_CASES_HAUTEUR + 1, 5) :
        zone_grille.create_line((5, 5 + y * DIM_CASES),
                           (5 + NB_CASES_LARGEUR * DIM_CASES, 5 + y * DIM_CASES),
                           fill = 'black')
        
    return dico


#############################################################################################################
fenetre = Tk()      # création d'une fenêtre

taille_fenetre = str(NB_CASES_LARGEUR * DIM_CASES + 10 + 300) + 'x' + str(NB_CASES_HAUTEUR * DIM_CASES + 20)
fenetre.geometry(taille_fenetre)          # définition de sa taille sous la forme '800x600'

fenetre.title('Mappeur de grille')       

zone_grille = Canvas(fenetre, bg="white",                # création dans la fenêtre d'un espace graphique appelée zone_grille
                     width = NB_CASES_LARGEUR * DIM_CASES + 10,
                     height = NB_CASES_HAUTEUR * DIM_CASES + 10)

dico_item = creation_grille()

zone_grille.grid(column = 0, row = 0, rowspan = 60)     # placement de la zone_grille dans la fenêtre, colonne 0, ligne 0, sur une hauteur de 60 lignes

texte_position = Label(fenetre, text = 'Position sur grille :\n\nLargeur        Hauteur')  
texte_position.grid(column = 1, row = 2)                # placement de texte_position dans la fenêtre, colonne 1, ligne 2
                    
valeurs_position = Label(fenetre, text = '')
valeurs_position.grid(column = 1, row = 3)              # placement de valeurs_position dans la fenêtre, colonne 1, ligne 3

for item_id in zone_grille.find_withtag('case'):                      # établissement des événements repérées sur les cases
    zone_grille.tag_bind(item_id, '<Button-1>', alterne_couleur)      # clic gauche ----> fonction alterne_couleur
    zone_grille.tag_bind(item_id, '<B1-Motion>', couleur_noir)        # clic gauche et déplacement souris ----> fonction couleur_noir
    zone_grille.tag_bind(item_id, '<Button-3>', alterne_couleur)      # clic droit ----> fonction alterne_couleur
    zone_grille.tag_bind(item_id, '<B3-Motion>', couleur_blanc)       # clic droit et déplacement souris ----> fonction couleur_blanc
    zone_grille.tag_bind(item_id, '<Motion>', info)                   # survol de la souris (sans clic) ----> fonction info

texte_legende = Label(fenetre, text = 'Format de sortie')
texte_legende.grid(column = 1, row = 15)              # placement de valeurs_position dans la fenêtre, colonne 1, ligne 10

bouton_efface = Button(fenetre, text = 'Tout effacer', command = effacer)    # création d'un "bouton_efface" dont la 'command' est la fonction effacer()
bouton_efface.grid(column = 1, row = 7)

bouton_table = Button(fenetre, text = 'Table', command = table)    # création d'un "bouton_table" dont la 'command' est la fonction table()
bouton_table.grid(column = 2, row = 14, sticky = 'w')

bouton_tableau = Button(fenetre, text = 'Tableau', command = tableau)    # création d'un "bouton_tableau" dont la 'command' est la fonction tableau()
bouton_tableau.grid(column = 2, row = 15, sticky = 'w')

bouton_dico = Button(fenetre, text = 'Dictionnaire', command = dictionnaire)    # création d'un "bouton_efface" dont la 'command' est la fonction dictionnaire()
bouton_dico.grid(column = 2, row = 16, sticky = 'w')

fenetre.mainloop()