# Les chaînes de caractères

___
## Avant de commencer

!!! info "Fonctions utiles :"

    === "`len(chaine)`"

        renvoie le nombre de **caractères** dans `chaine`

        ```python
        >>> len('banane')
        6
        >>> len('banane kiwi')
        11
        >>> len('')
        0
        ```

    === "`int(chaine)`"

        - change le type de la variable `chaine` en `int()`, si
            - la chaine est formée **uniquement de chiffres**
            - éventuellement avec un signe (positif ou négatif) placé devant
        - puis renvoie sa valeur

        ```python
        >>> int('123')
        123
        >>> int(-12')
        -12
        >>> int('3 5')
        **erreur affichée**
        ```

    === "`float(chaine)`"

        - change le type de la variable `chaine` en `float()` si
            - la chaine est formée **uniquement de chiffres**
            - éventuellement d'un point (virgule pour les nombres)
            - éventuellment avec un signe (positif ou négatif) placé devant
        - puis renvoie sa valeur

        ```python
        >>> float('123')
        123.0
        >>> float('-3.5')
        3.5
        >>> float('prix : 12.5')
        **erreur affichée**
        ```


!!! info "Méthodes dédiées aux chaines de caractères :" 

    === "`index(caractere)`"
        renvoie l’indice (index) de la première occurrence du `caractere` dans la chaîne (si il existe)
        ```python
        >>> chaine = "Portez ce vieux whisky au juge blond qui fume"
        >>> chaine.index("w")
        16
        >>> chaine.index("5")
        **erreur affichée**
        ```

    === "`find(sch)`"
        renvoie la position d’une sous-chaîne `sch` dans la chaîne
        ```python
        >>> chaine = "Cette leçon vaut bien un fromage, sans doute ?"  
        >>> sch = "fromage"  
        >>> chaine.find(sch)
        25  
        ```

    === "`count(sch)`"
        renvoie le nombre de sous-chaînes `sch` dans la chaîne
        ```python
        >>> chaine = "Le héron au long bec emmanché d'un long cou"  
        >>> sch = 'long'  
        >>> chaine.count(sch)
        2  
        ```

    === "`lower()`"
        renvoie la valeur de la chaîne en minuscules, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = 'CÉLIMÈNE est un prénom ancien'
        >>> chaine.lower()
        célimène est un prénom ancien   
        >>> chaine
        'CÉLIMÈNE est un prénom ancien'
        ```

    === "`upper()`"
        renvoie la valeur de la chaîne en majuscules, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = 'Maître Jean-Noël Hébèrt'
        >>> chaine.upper()
        MAÎTRE JEAN-NOËL HÉBÈRT
        >>> chaine
        'Maître Jean-Noël Hébèrt'
        ```

    === "`title()`"
        renvoie la valeur de la chaine avec une majuscule à l’initiale de chaque mot, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = 'albert rené élise véronique'
        >>> chaine.title()
        Albert René Élise Véronique
        >>> chaine
        'albert rené élise véronique'
        ```

    === "`capitalize()`"
        variante de la précédente : renvoie la chaine avec seulement la première lettre en majuscule, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = "quel beau temps, aujourd’hui !"  
        >>> chaine.capitalize())  
        "Quel beau temps, aujourd’hui !"
        ```

    === "`swapcase()`"
        renvoie la valeur de la chaine où toutes les majuscules sont en minuscules (et vice-versa), sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = 'Le Lièvre Et La Tortue'
        >>> chaine.swapcase()
        'lE lIÈVRE eT lA tORTUE'
        ```

    === "`strip()`"
        renvoie la valeur de la chaine en enlevant les espaces éventuels au début et à la fin de la chaîne, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = '   Monty Python   '
        >>> chaine.strip()  
        'Monty Python'
        ```

    === "`replace(c1, c2)`"
        renvoie la valeur de la chaine en remplaçant tous les caractères `c1` par des caractères `c2` dans la chaîne, sans mutation de la chaine (la variable garde sa valeur d'origine)
        ```python
        >>> chaine = "Si ce n'est toi c'est donc ton frère"  
        >>> chaine.replace(" ","*"))
        "Si*ce*n'est*toi*c'est*donc*ton*frère"
        ```
___
## Exercices

!!! question "Exercice 1 : Mot inversé"

    Écrire une fonction `inverse` qui prend en paramètre une variable de type `str()` et renvoie sa valeur inversée  
    Ainsi par exemple, « zorglub » deviendra « bulgroz ».

    !!! done "Attendus"

        === "Déclaration de la fonction"
            ```python
            def inverse(chaine)
                A vous de coder :
                instruction 1
                instruction 2
                ...
                return resultat_attendu
            ```
        === "Application de la fonction"
            ```python
            >>> inverse('zorglub')
            'bulgroz'
            ```

!!! question "Exercice 2 : Palindrome"

    En partant de l’exercice précédent, écrire une fonction `palindrome` qui prend en paramètre une variable de type `str()` et qui renvoie une variable de type `bool()` précisant si la chaîne de caractères est un _palindrome_.

    !!! done "Attendus"
    
        === "Déclaration de la fonction"
            ```python
            def palindrome(chaine)
                A vous de coder :
                instruction 1
                instruction 2
                ...
                return resultat_attendu
            ```
        === "Application de la fonction"
            ```python
            >>> palindrome('zorglub')
            False
            >>> palindrome('laval')
            True
            ```

!!! question "Exercice 3 :   Pendu"

Quelles fonctions seraient nécessaires pour établir le "jeu du pendu" ?
