___
# La plus simple

!!! note "Structure"
    ```python
    if condition :
        instruction1
        instruction2
        ....
    ```
### Algorithme

**si** la conditon est vrai **:**
<dd>l'instruction1 est réalisée</dd>
<dd>l'instruction2 est réalisée</dd>
<dd>...</dd>

!!! example "si un nombre est pair, on le divise par 2"
    ```python
    if n % 2 == 0:
        print("n est un nombre pair")
        n = n // 2
    ```
 
### Erreurs classiques

- oubli des 2 points **:**
- mauvaise **indentation** : décalage du bloc d'instructions par rapport à `if`


___
# Autre forme courante

!!! note "Structure"
    ```python
    if condition :
        instruction1
        instruction2
    else :
        instruction3
        instruction4
    ```

### Algorithme :

**si** la conditon est vrai **:**
<dd>l'instruction1 est réalisée</dd>
<dd>l'instruction2 est réalisée</dd>
<dd>...</dd>

**sinon** :
<dd>l'instruction3 est réalisée</dd>
<dd>l'instruction4 est réalisée</dd>
<dd>...</dd>

!!! example "si un nombre est pair, on le divise par 2, sinon on ajoute 1 avant de le diviser par 2"
    ```python
    if n % 2 == 0:
        print("n est un nombre pair")
        n = n // 2
    else :
        print("n est un nombre impair")
        n = (n + 1) // 2
    ```
 

