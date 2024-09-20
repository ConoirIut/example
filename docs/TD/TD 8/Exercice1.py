# -*- coding: utf-8 -*-
'''
:Titre : Création d'une table de données
:Auteur : 
:Date : 05/2020

Exercice n°1 du TD n°8
'''


##################################################################################################################
## Question a)
##################################################################################################################
with open(emplacement/fichier, 'r', encoding = 'UTF-8') as fichier :    # ouverture du fichier en mode lecture
    lignes =                       # lire les lignes
    
descripteurs =                     # prendre la première ligne en enlevant le retour à la ligne et en séparant les descripteurs

donnees = []                       # liste contenant les enregistrements (données des lignes suivantes)

for ligne in lignes[1:] :          # pour chaque ligne suivante
    # à vous de continuer




##################################################################################################################
## Question b)
##################################################################################################################
def correction_majuscules() :
    '''La fonction vérifie et corrige la majuscule de chaque nom et prénom dans la variable 'donnees'.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    pass   # à effacer


##################################################################################################################
## Question c)
##################################################################################################################
def doublons() :
    '''La fonction élimine de la variable 'donnees' les enregistrements en double.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    pass   # à effacer


##################################################################################################################
## Question d)
##################################################################################################################
def tri_age() :
    '''La fonction ordonne les enregistrements de la variable 'donnees' par age décroissant.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    pass   # à effacer

    
##################################################################################################################
## Question e)
##################################################################################################################
