# Les chaînes de caractères
___

Les chaînes de caractères sont des variables **itérables**, que l'on peut décomposer par indiçage.

!!! example "Différents indiçages"
    === "Indices positifs"
        !!! warning inline end
            Le premier indice est $0$
        ```python
        >>> mot = 'Exemples'
        >>> mot[0]
        'E'
        >>> mot[3]
        'm'
        ```
    === "Indices négatifs"
        !!! warning inline end
            On compte de droite à gauche.
        ```python
        >>> mot = 'Exemples'
        >>> mot[-1]
        's'
        >>> mot[-5]
        'm'
        ```
    === "Indices groupés : slice"
        !!! warning inline end
            Le dernier indice n'est pas inclus.
            _Similaire à `range`_
        ```python
        >>> mot = 'Exemples'
        >>> mot[1:4]
        'xem'
        >>> mot[:2]
        'Ex'
        >>> mot[4:]
        'ples'
        >>> mot[-3:]
        'les'
        ```
        
Elles ne sont pas **mutables** : elles ne peuvent être modifiées après création.  
Les **méthodes** associées aux chaînes de caractères n'affectent donc pas leur valeur.

!!!example "Mise en majuscules"
    ```python
    >>> mot = 'Exemples'
    >>> mot.upper()
    'EXEMPLES'
    >>> mot
    'Exemples'
    ```
    
On retrouve toutes les méthodes dans la documentation officielle de Python : [https://docs.python.org/fr/3.7/library/stdtypes.html#string-methods](https://docs.python.org/fr/3.7/library/stdtypes.html#string-methods){target=_blank}
