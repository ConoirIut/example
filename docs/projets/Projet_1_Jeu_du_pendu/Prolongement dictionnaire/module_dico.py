# -*- coding: utf-8 -*-
'''
:Titre : Module dictionnaire pour le Jeu du pendu
:Auteur : L. Conoir
:Date : 11/2019

Projet : Jeu du pendu
'''

##################################################################################################################
def mot_aleatoire() :
    ''' La fonction renvoie un mot choisi aléatoirement dans un fichier de mots

:param: None
:return: type str, mot choisi
:CU: le fichier texte "mots_francais_sans_accents.txt" doit être présent à côté du module
:bord_effect: None
    '''

    from random import choice 

    fichier_source = open('mots_francais_sans_accents.txt','rt')
        
    ligne = choice(fichier_source.readlines())[:-1]
    
    fichier_source.close()
    
    return ligne
