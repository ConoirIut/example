# -*- coding: utf-8 -*-
'''
:Titre : Introduction au travail préparatoire
:Auteur : L. Conoir
:Date : 12/2019

2 Méthodes de construction d'une grille de 3 lignes et de 2 colonnes, rempli de 0.
                                   -------------
      [[0, 0, 0],                  | 0 | 0 | 0 |
       [0, 0, 0]]                  -------------
                                   | 0 | 0 | 0 |
                                   -------------
'''

###################################################################################
## par compréhension : efficace pour des éléments identiques ou similaires
###################################################################################
def grille_comprehension() :
    '''La fonction renvoie une grille de 3 lignes et 2 colonnes, rempli de 0.

:param: None
:return: type list, une liste de 2 listes, chacune constituée de 3 nombres 0
:CU: None

:examples:
>>> grille_comprehension()
[[0, 0, 0], [0, 0, 0]]
'''
    grille = [[0 for nb_col in range(3)] for nb_lig in range(2)]    # grille de 2 lignes et 3 colonnes
    
    return grille


#####################################################################################
## par itération avec 2 boucles 'for' : décomposition de la construction d'une grille
#####################################################################################
def grille_iteration() :
    '''La fonction renvoie une grille de 3 lignes et 2 colonnes, rempli de 0.

:param: None
:return: type list, une liste de 2 listes, chacune constituée de 3 nombres 0
:CU: None

:examples:
>>> grille_iteration()
[[0, 0, 0], [0, 0, 0]]
'''
    grille = []                        # création, par liste, d'une grille vide
    
    for nb_lig in range(2) :           # 1ère boucle : sur le nombre de lignes
        
        ligne = []                         # création, par liste, d'une ligne vide
        
        for nb_col in range(3) :           # 2ème boucle : sur le nombre de colonnes
            ligne.append(0)                    # constitution de la ligne par ajout d'éléments
        
        grille.append(ligne)               # ajout de la ligne créée à la grille
        
    return grille
    

###################################################################################
### Vérification des tests mis en examples dans les fonctions
###################################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()