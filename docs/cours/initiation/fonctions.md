# Les fonctions en Python
___
Python possède un certain nombre de fonctions préprogrammées ,directement accessibles ou par l'intermédiaire des librairies et modules disponibles.

Mais il est tout à fait possible d'en créer de nouvelles.

!!! note "Structure"
    ``` python
    def nom_de_la_fonction (argument1, argument2, ...) :
        '''Docstring'''
        
        instructions
        
        return resultat
    ```
    
- La première ligne de la fonction est appelée la **signature** de la fonction : nom et argument(s).

!!! note inline end "Aide : help"
    En console, le docstring s'affiche lorsqu'on demande l'aide sur la fonction :  
    `#!bash help(nom_de_la_fonction)`
    
- Plusieurs lignes de commentaires suivent  :  le **docstring** de la fonction (documentation) entre triples quotes
    - Une **phrase résume** son utilité, ses fonctionnalités.
    - Inventaire des **arguments**, avec leur type et description
    - Indications sur le **resultat** renvoyé : type, description
    - Les **conditions d'utilisations** de la fonction (si il y en a)
    - Les **effets de bord** créés (si il y en a) : modification d'un argument, écriture sur la sortie principale (écran de console), demande sur l'entrée principale (clavier),...
    - Des **exemples** d'utilisations concrêtes de la fonction. Très important : ils donnent un attendu et peuvent servir de vérification lors de tests.
    
- Le corps de la fonction avec ses **instructions**.

- Obtention d'un résultat de la fonction à l'aide du mot réservé `return`.

Il est possible qu'une fonction n'utilise pas d'**argument** (exemple : affiche seulement du texte) : on l'appelle dans ce cas une **procédure**.

Il est possible qu'une fonction ne renvoie pas de valeur attendue (idem) : pas de `return`.

Il est possible qu'une fonction utilise plusieurs fois le mot `return` dans ces instructions **MAIS** lorsque Python interprète un `return` (le premier qu'il rencontre), la fonction s'arrête à ce moment là. _La fonction renvoie qu'un seul résultat._

Lorsque la fonction est définie, on peut alors l'utiliser à tout moment dans le programme principal :

`#!python nom_de_la_fonction(paramètre1, paramètre2, ...)`
