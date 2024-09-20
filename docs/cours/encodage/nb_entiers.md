___
## Le système décimal (base 10)

Avant de comprendre le fonctionnement du binaire, et des systèmes de comptage en général (plus communément appelés bases), comment fonctionne le système à base $10$ ?

La base 10 vient très certainement du fait qu'on possède 10 doigts :  
L'écriture repose sur l'utilisation de 10 chiffres : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.   

!!! info "Encore aujourd'hui."
    Certains peuples comptent en base 20 : mains + pieds.  
    Plus rare, d'autres comptent en base 60 (pas seulement pour les secondes et minutes) :  
        - sur une main, ils comptent les phalanges de 4 doigts avec le pouce : 3 phalanges fois 4 = 12 phalanges  
        - sur l'autre main, ils comptent les paquets de 12 obtenus avec les doigts : 5 doigts fois 12 phalanges = 60 phalanges.

Pour aller au-delà de 9, il faut considérer que l'on a atteint une **dizaine**.

Cela signifie que si le rang des unités est plein, il faut passer à celui des dizaines.  
Puis, quand celui des dizaines est rempli (ainsi que celui des unités), on obtient 10 dizaines, une **centaine** : et ainsi de suite...

!!! example "Exemple de 19"
    Ce nombre représente 1 dizaine et 9 unités.  
    Si on ajoute 1, on obtient une dizaine supplémentaire : on a alors 2 dizaines et ... 0 unités.

Un nombre entier peut être décomposé en rangs (unités, dizaines, centaines, etc).  
Pour lesquels :

- $1$ dizaine représente $10$ unités
- $1$ centaine représente $10$ dizaines = $10 \times 10$ unités  = $10^2$ unités
- $1$ millier représente $10^3$ unités
    ...
    
En résumé : chaque rang correspond à une **puissance de 10 unités** .... c'est la **base 10**

!!! example "Exemple : $(185)_{10}$"
    !!! note inline end "Notation"
        A partir de maintenant, on précisera pour chaque nombre, la base dans laquelle il est écrit.  
        185 écrit en base 10 :
        
        $$(185)_{10}$$
        
    Ce nombre occupe les 3 premiers rangs : centaines, dizaines et unités.
    
    |centaines|dizaines|unités|
    |:-:|:-:|:-:|
    |$10^2$|$10^1$|$10^0$|
    |$1$|$8$|$5$|
    
    Nous pouvons donc écrire :  $(185)_{10} = 1 \times 10^2 + 8 \times 10^1 + 5 \times 10^0$
    
    _On vient de décomposer ce nombre en puissance de 10_


Pour n'importe quel système de base $b$, la valeur d'un rang est égale à $b^n$, où $n$ la position du rang : en partant de la droite et commençant par 0.


___
## Le binaire

Le binaire est le système de comptage des ordinateurs.

!!! question "Pourquoi le binaire et pas le décimal comme les humains ?"

    Un processeur d'ordinateur est composé transistors, qui fonctionne comme des interrupteurs :  
    ON : le courant passe  
    OFF : le courant ne passe pas

    Pour compter, l'ordinateur utilise donc avec un système basé sur deux valeurs possibles :  
        le courant passe : 1  
        le courant ne passe pas : 0

En binaire (base $2$), on utilise le terme bit, qui est la contraction de "binary digit", littéralement "chiffre binaire".

Par exemple, le nombre $(10011)_2$ est composé de 5 bits.

Chaque rang en binaire ne peut avoir que deux valeurs (binaire = base 2) : 0 ou 1.  
En base 10, chaque rang représente une puissance de 10.  
En base 2, chaque rang représente donc une puissance de 2.

|Nombre en base 10|Nombre en binaire|
|:-:|:-:|
|0|0|
|1|1|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|
|7|111|
|8|1000|
|9|1001|
|10|1010|
|11|1011|
|12|1100|
|13|1101|
|14|1110|
|15|1111|

!!! question "Questions"
    Combien de valeurs peut-on coder avec 1 bit ?  
    Combien de valeurs peut-on coder avec 2 bits ?  
    Combien de valeurs peut-on coder avec 3 bits ?  
    Combien de valeurs peut-on coder avec n bits ?  


___
## Conversion décimale binaire

Pour l'instant, on n'a compté que jusqu'à 15. Mais pour les plus grands nombres, la méthode précédente peut se révéler fastidieuse...

Il existe bien sûr plusieurs méthodes de conversion, mais nous allons étudier la plus simple et la plus rapide. Il s'agit de la méthode euclidienne.

Cette méthode, en plus d'être facile à utiliser en programmation (c'est un algorithme) est l'une des meilleures lorsqu'il s'agit de traiter les grands nombres.

Voici la méthode :  
    • On prend le nombre en base 10 (forme normale).  
    • On le divise par 2 et on note le reste de la division (soit 1, soit 0)  
    • On refait la même chose avec le quotient précédent, et on met de nouveau le reste de côté.  
    • On réitère la division, jusqu'à ce que le quotient soit 0.  
    • Le nombre en binaire apparaît alors : il suffit de prendre tous les restes de bas en haut.  

!!! example "Exemple de 185"
    |Division entière|Reste de la division|
    |:-:|:-:|
	|185 / 2 =	92|reste 1|
	|92 / 2 =	46|reste 0|
	|46 / 2 =	23|reste 0|
	|23 / 2 =	11|reste 1|
	|11 / 2 =	5|reste 1|
	|5 / 2 =	2|reste 1|
	|2 / 2 =	1|reste 0|
	|1 / 2 =	0|reste 1|

    185 en base 10 vaut donc 10111001 en binaire : $(185)_{10} = (10111001)_2$

!!! question "Question"
    Comment s'écrit $(42)_{10}$ en binaire ?


___
## Conversion binaire décimale

Prenons le nombre $(11010)_2$.

Il s'étale sur 5 rangs, et chaque rang correspond à une puissance de deux :

- Le premier rang (en partant de la droite) est le rang 0, c'est le bit dont le poids est le plus faible, le « Least Significant Bit » ou LSB  
- Le second rang est le rang 1, etc ...  
- Ici, le dernier rang est le rang 4, c'est le bit dont le poids est le plus FORT, le « Most Significant Bit » ou MSB  

Pour convertir le tout en décimale, on procède de la manière suivante :

- au rang 0 : on multiplie la valeur par $2^0$
- au rang 1 : on multiplie la valeur par $2^1$
- au rang 2 : on multiplie la valeur par $2^2$
- etc ...
- on calcule la somme : Attention à bien partir de la droite

!!! question "Question"
    Convertir $(01011001)_2$ en base 10  
    Convertir $(10110010)_2$ en base 10  
    En déduire ce qui se passe si on rajoute un $0$ à droite de l'écriture d'un nombre binaire ?



___
## L'hexadécimal

Le binaire est bien pratique pour l'ordianteur et ses courants électriques.  
Mais dans la vie de tous les jours, on utilise la base $10$.  
Les nombres binaires sont longs : pour coder $(128)_{10}$, il faut 8 bits en binaire, alors que 3 chiffres suffisent en décimal... 

Pour faciliter, l'encodage des nombres, on utilise également une autre base : $16$, appelée système hexadécimal (hexa 6, déci 10, 6 + 10).

16 est un multiple de 2, et cela permet donc de représenter 8 bits avec seulement 2 chiffres.

En base 16, il faut 16 chiffres : on commence naturellement de 0 à 9 et on termine avec des lettres majuscules

$0 1 2 3 4 5 6 7 8 9 A B C D E F$

|Décimal (base 10)|Binaire (base 2)|Hexadécimal (base 16)|
|:-:|:-:|:-:|
|0|0000|0|
|1|0001|1|
|2|0010|2|
|3|0011|3|
|4|0100|4|
|5|0101|5|
|6|0110|6|
|7|0111|7|
|8|1000|8|
|9|1001|9|
|10|1010|A|
|11|1011|B|
|12|1100|C|
|13|1101|D|
|14|1110|E|
|15|1111|F|

Le plus grand chiffre en hexadécimal est $F$, il correspond à $15$ en décimal et $1111$ en binaire :

$F$ est encodé sur 4 bits $(F)_{16} = (1111)_2$

!!! warning inline end "Attention"
    Si le nombre binaire n'a pas un nombre de bits multiple de 4, il faut ajouter des zéros en tête (ce qui ne change pas sa valeur) afin de pouvoir les regrouper 4 par 4.

Pour convertir un nombre binaire en base 16, on regroupe les bits 4 à 4 en partant de la droite (poids faible), chaque groupe donnant un chiffre hexadécimal.

À l'inverse, passer d'un nombre hexadécimal à sa représentation binaire se fait en remplaçant chaque chiffre par son équivalent sur 4 bits.

!!! example "Exemples" 
    $(1101~1001)_2 = (D9)_{16}$  
    $(7F)_{16} = (0111~1111)_2$

!!! question "Questions"
    Convertir $(101111011001)_2$ en base $16$  
    Convertir $(111011)_2$ en base $16$  
    Convertir $(1A3E)_{16}$ en base $2$  


___
## Convertir un nombre décimal en hexadécimal

Pour convertir un nombre décimal en hexadécimal, la méthode est similaire au binaire : on divise par 16.

!!! example "Exemple de 185"
    |Division entière|Reste de la division|En base 16|
    |:-:|:-:|:-:|
    |185 / 16 = 11|reste 9|9|
    |11 / 16 = 0|reste 11|B|

    $185$ en base $10$ vaut donc $B9$ en hexadécimal : $(185)_{10} = (B9)_{16}$

!!! question "Question"
Convertir $(1387)_{10}$ en base $16$


___
## Convertir un nombre hexadécimal en décimal

Le principe est le même que pour la conversion de binaire en décimal, sauf qu'au lieu d'utiliser les puissances de 2, on utilise les puissances de 16.

!!! example
    $\begin{align}(12B7)_{16} &= 1 \times 16^3 + 2 \times 16^2 + 11 \times 16^1 + 7 \times 16^0\\
    &= 1 \times 4096 + 2 \times 256 + 11 \times 16 + 7\\
    &= 4791\end{align}$

!!! question "Question"
    Convertir $(1B87)_{16}$ en base $10$
