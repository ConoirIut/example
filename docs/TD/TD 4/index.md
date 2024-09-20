# Découverte des "listes Python"
___
## Introduction

Une "liste Python" est un **type construit** de données qui correspond à un **tableau**.

Chaque variable de type ```list``` est un ensemble ordonné d’éléments de même type : les **items**.

!!! example "Exemples"
    ```python
    tableau_courses = ['eau', 'lait', 'chocolat', 'poireaux', 'pain']
    notes = [12, 13, 5, 12, 13, 14]
    tableau_vide = []
    ```

Comme pour les chaînes de caractères, les tableaux sont **itérables** et chaque item possède un **indice** (le premier indice est 0).

!!! example "Exemples"
    ```python
    >>> tableau_courses[2]
    'chocolat'
    >>> notes[-2]
    13
    ```

Les tableaux sont **mutables** (modifiables, mais attention à la copie d’un tableau)

!!! example "Exemples"
    ```python
    >>> tableau_courses[2] = 'banane'
    >>> tableau_courses
    ['eau', 'lait', 'banane', 'poireaux', 'pain']
    ```
    L’item ```'chocolat'``` devient ```'banane'```

___
## Travail préliminaire à effectuer :

- Faire une copie naïve :	```tableau_aliments = tableau_courses```

- Vérifier le contenu du nouveau tableau   ```tableau_aliments``` :

- Modifier un élément de ```tableau_aliments``` : 

- Vérifier la modification sur le tableau ```tableau_aliments```, en affichant son contenu :

- Afficher également le contenu de ```tableau_courses``` :


!!! warning "Conclusion"
    L’affectation d’une nouvelle variable de type ```list``` sur un tableau existant ne fait que créer un nouveau nom de variable à ce tableau : la valeur du tableau est la même.
    Autrement dit, c’est un tableau avec deux noms.

    Pour faire une copie sans modification ultérieure : 
    
    1. on utilise la méthode ```copy()``` : ```tableau_aliments = tableau_courses.copy()```
    2. on recrée avec ```list()``` : ```tableau_aliments = list(tableau_courses)```

    Ainsi défini, le tableau ```tableau_aliments``` ne sera pas altéré par des modifications du tableau ```tableau_courses``` (et vice versa).

___
## Exercices
!!! question "Exercice 1 : Création de tableaux"

1. par affectation : créer les tableaux énoncées dans les exemples de l'introduction.

2. par transformation de types : utiliser l’instruction ```list()``` dans quelques cas et observer le résultat :  
```python
list('alphabet')
list(True)
list(2019)
list(range(1,20,2))
```

3. par la méthode `append()` : en partant d’un tableau vide, ajouter des items :  
```python
ville = []
ville.append('Rome')
ville.append('Athènes')
ville.append('Londres')
```

4. par compréhension : l’instruction est de la forme `[expression(i)  for i in objet]`
```python
notes_avec_coeff2 = [2 * notes[i]  for i in range(len(notes))]
```
Après avoir tester l’instruction précédente, établir le tableau des 30 premiers nombres pairs.


???+ tip "Quelques méthodes dédiées :"

    |Méthode|Valeur renvoyée|Principe|
    |:--|:--:|:--|
    |tableau.append(x)|None|Ajoute l’item x à la fin de tableau.|
    |tableau.count(x)|int()|Renvoie le nombre d’occurrence de l’item x   dans tableau.|
    |tableau.extend(L)|None|Ajoute tous les items du tableau L à tableau.|
    |tableau.index(x)|int()|Renvoie l’indice de la première occurrence de l’item x dans tableau.|
    |tableau.insert(index int, x objet)|None|Insère l’item x à un indice index dans tableau.|
    |tableau.pop(i)|item|Supprime de tableau l’item à l’indice i et le renvoie. Le paramètre i est facultatif. En l’absence de la valeur de i, cela supprime et renvoie le dernier item de tableau.|
    |tableau.remove(x objet)|None|Supprime la première occurrence de l’item x dans tableau.|
    |tableau.reverse()|None|Inverse les items de tableau.|
    |tableau.sort()|None|Trie les items de tableau en ordre croissant.|


!!! question "Exercice 2 : Jours de la semaine"

Constituez un tableau `semaine` contenant les 7 jours de la semaine.

1. À partir de cette tableau, comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux du week-end d'autre part ? Utilisez pour cela l'indiçage. 

2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage). 

3. Trouvez deux manières pour accéder au dernier jour de la semaine. 

4. Inversez les jours de la semaine en une commande. 


!!! question "Exercice 3 :  Repas de la semaine"

1. Écrire une fonction ```repas(jour)```, qui demande à l’utilisateur le repas du jour précisé en paramètre et le renvoie

2. A partir du tableau ```semaine``` de l’exercice 3 et de la fonction précédente, établir le tableau ```repas_semaine``` contenant les repas de l’utilisateur pour tous les jours de la semaine.

!!! question "Exercice 4 :   tableau de tableaux"

1. Créez 4 tableaux ```hiver```, ```printemps```, ```ete``` et ```automne``` contenant les mois correspondants à ces saisons.
2. Créez ensuite un tableau ```saisons``` contenant les tableaux ```hiver```, ```printemps```, ```ete``` et ```automne```.
3. Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans l'interpréteur :

    ```python
    saisons[2]
    saisons[1][0]
    saisons[1:2]
    saisons[:][1]
    ```

Comment expliquez-vous ce dernier résultat ? 



!!! question "Exercice 5 :   Distribution de cartes"

Etablir un programme qui partage aléatoirement un jeu de 32 cartes en 4 joueurs.

??? tip "Aide"
    ```python
    import random```   # (pour la fonction fonction ```random.choice()```)
    couleur = ['Trefle', 'Carreau', 'Coeur', 'Pique']
    valeur = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    ```

!!! question "Exercice 6 :   Rendu monnaie"

1. Etablir un tableau ordonnée des pièces et billets en euros.
2. Etablir une fonction `rendu` qui prend en paramètre un prix et renvoie le rendu monnaie sous forme d'un tableau.

