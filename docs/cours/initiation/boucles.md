# Les boucles
Une **boucle** est la répétition d'une séquence d'instructions.

___
## Type de boucles
Lorsqu'on connaît le nombre de répitions qui doivent être exécutées, on utilise la **boucle bornée** `for`.

Sinon, le nombre de répitions est certainement soumis à une condition (parfois multiples). On utilise alors la **boucle non bornée** `while`.

___
## Boucle `while`
La boucle `while` est parfois appelée une boucle conditionnelle.

!!! note "Structure"
    ```python
    while condition :
        séquence d'instructions
    ```

### Algorithme
**tant que** la conditon est vrai **alors**
<dd>la séquence d'instruction est réalisée</dd>

!!! example "tant que le nombre est pair, on le divise par 2"
    ```python
    n = 64
    while n % 2 == 0:
        n = n // 2
        print(n)
    ```
!!! warning "boucle infinie"
	Si la condition est continuellement vrai, la boucle continue...
___
## Boucle `for`
Plusieurs utilisations sont possibles.

### Avec l'itérateur : `range`

!!! note "Structure basique"
    ```python
    for i in range(n):
        séquence d'instructions
    ```
Répétition de la séquence d'instructions $n$ fois.

!!! warning inline end "On compte à partir de $0$"
    de $0$ à $n - 1$, il y a bien $n$ nombres
La variable $i$ prend successivement les entiers compris dans l'intervalle $[0 ; n[$  
A chaque tour de boucle, la variable $i$ change de valeur :

- i = 0
- i = 1
- i = 2
- ...
- i = n - 1

Elle peut être utilisée ou non dans les instructions.

La fonction `range()` renvoie une séquence d'entiers qui dépend de ces paramètres :

!!! note "Utilisations possibles"
    === "Avec 1 paramètre"
        ```python
        range(10)
        ```
        correspond à la séquence de nombres 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    === "Avec 2 paramètres"
        ```python
        range(2, 8)
        ```
        correspond à la séquence de nombres 2, 3, 4, 5, 6, 7
    === "Avec 3 paramètres"
        ```python
        range(1, 18, 3)
        ```
        correspond à la séquence de nombres 1, 4, 7, 10, 13, 16

### Avec une énumération
Certains objets sont considérés comme des séquences de plusieurs éléments.

!!! note "Structure"
    ```python
    for element in objet :
        séquence d'instructions
    ```

La variable **element** prend successivement la valeur de chaque élément de l'**objet**.

Les variables de type `str` ont des valeurs composées de caractère(s).

!!! example "pour chaque lettre dans le texte, ...."
    ```python
    texte = "L'informatique est fantastique"
    for lettre in texte :
        if lettre == "i" :
            print(lettre)
    ```