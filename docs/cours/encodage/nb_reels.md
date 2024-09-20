___
## Représentation de la partie décimale d'un nombre

!!! question "Comment représenter $5,1875$ en binaire ?"

Pour représenter $5$ :  $(101)_2$

Mais comment faire pour  "$,1875$"  ?

- on multiplie $0,1875$ par $2$ :	$0,1875	\times 2 = 0,375 = 0 + 0,375$  
- on multiplie $0,375$ par $2$ :	$0,375 \times 2 = 0,75 = 0 + 0,75$  
- on multiplie $0,75$ par $2$ :	$0,75 \times 2 = 1,5 = 1 + 0,5$  
- on multiplie $0,5$ par $2$ :	$0,5 \times 2 = 1,0 = 1 + 0,0$  

(la partie décimale arrive à 0, on arrête le processus)

On obtient une succession de "$a + 0,b$" :   ("$0 + 0,375$", "$0+ 0,75$", "$1 + 0,5$" et "$1 + 0,0$")

Il suffit maintenant de "prendre" tous les valeurs "a" (dans l'ordre de leur obtention) afin d'obtenir la partie décimale de notre nombre : $0011$

Nous avons alors   $(101,0011)_2$  qui est la représentation binaire de $(5,1875)_{10}$


!!! question "Question 1 : Trouver la représentation binaire de $(4,125)_{10}$"


Il est possible de retrouver une représentation décimale en base $10$ à partir d'une représentation en binaire.

Partons de $(100,0101)_2$

Partie entière  $(100)_2$, nous obtenons $4$.

Pour la partie décimale nous devons écrire : 

$0 \times 2^{-1} + 1 \times 2^{-2} + 0 \times 2^{-3} + 1 \times 2^{-4} =  0 \times \dfrac{1}{2} + 1 \times \dfrac{1}{4} + 0 \times \dfrac{1}{8} + 1 \times \dfrac{1}{16} = 0,3125$

Nous avons donc $(4,3125)_{10}$


!!! question "Question 2 : Trouver la représentation en base 10 de $(100,001)_2$"

!!! question "Question 3 : Trouver la représentation binaire de $(0,1)_{10}$"
    Que remarquez-vous ?


Dans l'exemple ci-dessus, nous remarquons que le processus de "conversion" ne s'arrête pas, nous obtenons :
"0,0001100110011...", le motif "0011" se répète à l'infini...

C'est la même chose en base dix pour la valeur $\dfrac{1}{3} = 0,333333...33333....$

En base dix, il est possible d'écrire les très grands nombres et les très petits nombres grâce aux "puissances de dix" :

Exemples : $6,02 \times 10^{23}$ ou $6,67 \times 10^{-11}$

Il est possible de faire exactement la même chose avec une représentation binaire.
En base 2, nous utiliserons des "puissances de deux" à la place des "puissances dix" :

Exemple :  $101,1101 \times 2^8$

Pour passer d'une écriture sans "puissance de deux" à une écriture avec "puissance de deux", il suffit décaler la virgule : 

Exemple : $1101,1001 = 1,1011001\times 2^3$         pour passer de $1101,1001$ à $1,1011001$ nous avons décalé la virgule de 3 rangs vers la gauche, d'où le $2^3$

Si l'on désire décaler la virgule vers la gauche, il va être nécessaire d'utiliser des "puissances de deux négatives" :  
Exemple : $0,0110 = 1,10\times2^{-2}$  (décalage de la virgule de 2 rangs vers la droite) 


___
## Représentation des flottants dans un ordinateur
La norme **IEEE 754** est la norme la plus employée pour la représentation des nombres à virgule flottante dans le domaine informatique. La première version de cette norme date de 1985.

Nous allons étudier deux formats associés à cette norme : le format dit "simple précision" et le format dit "double précision".

Le format "**simple précision**" utilise **32 bits** pour écrire un nombre flottant alors que le format "**double précision**" utilise **64 bits**.  
Dans la suite nous travaillerons principalement sur le format 32 bits.

!!! note "Que ce soit en simple précision ou en double précision, la norme IEEE754 utilise :"
    !!! done inline end "Précision"
        === "simple"
            $1 + 8 + 23 = 32$ bits
        === "double"
            $1 + 11 + 52 = 64$ bits

    - 1 bit de signe (1 si le nombre est négatif et 0 si le nombre est positif)
    - des bits consacrés à l'exposant (8 bits pour la simple précision et 11 bits pour la double précision)
    - des bits consacrés à la mantisse (23 bits pour la simple précision et 52 bits pour la double précision)
    
        |bit de signe|bits exposant|bits mantisse|
        |:-:|:-:|:-:|
        |-|- - - - - - - -|- - - - - - - - - - - - - - - - - - - - -|

### Méthode

Pour écrire un nombre flottant en respectant la norme IEEE754, il est nécessaire de commencer par écrire le nombre sous la forme : 

$$1, \text{XXXXX}	\times2^e ~~~~~~~~~~~~ \text{(avec **e** l'**exposant**)}$$

Il faut obligatoirement qu'il y ait un seul chiffre à gauche de la virgule et il faut que ce chiffre soit un $1$. 

!!! example inline end "Exemple"
    Le nombre $1010,11001$ devra être écrit $1,01011001	\times2^3$

La partie "$\text{XXXXXX}$" constitue la **mantisse**  
(dans notre exemple $1010,11001$, la mantisse est $01011001$). 

Comme la mantisse comporte 23 bits en simple précision, il faudra compléter avec le nombre de zéro nécessaire afin d'atteindre les 23 bits.  
(si nous avons $01011001$, il faudra ajouter $23 - 8 = 15$ zéros à droite ce qui donnera en fin de compte une mantisse de $01011001000000000000000$ )

La première intuition serait de dire que la partie "exposant" correspond simplement au "e" de "$1, \text{XXXXX}	\times2^e$" 
(dans notre exemple $1010,11001$, nous aurions $00000011$ :  $3$ en binaire sur 8 bits). 

En fait, c'est un peu plus compliqué que cela...
En effet, comment représenter les exposants négatifs ? 
Aucun bit pour le signe de l'exposant n'avait été prévu dans le norme IEEE754...


Une autre solution a donc été choisie :

Pour le format simple précision, 8 bits sont consacrés à l'exposant, il est donc possible de représenter 256 valeurs.  
Nous allons pouvoir représenter des exposants compris entre $(-126)_{10}$ et $(+127)_{10}$ 

Pour avoir des valeurs uniquement positives, il va falloir procéder à un décalage qui consiste à ajouter systématiquement 127 à la valeur de l'exposant.


Exemple :  $1010,11001$   donne   $1,01011001	\times2^3$  
On effectue le décalage en ajoutant $127$ à $3$ : $1,01011001 2130$
soit en passant l'exposant en base $2$ : $1,01011001	\times210000010$. 

Ce qui nous donne donc pour $1010,11001$ : 

- une **mantisse** = $01011001000000000000000$

- un **exposant** = $10000010$

!!! note "Remarque"
    Même si ce n'est pas le cas ici, il peut être nécessaire d'ajouter des zéros pour arriver à 8 bits).

À noter que pour le format double précision le décalage est de $1023$ pour l'exposant (il faut systématiquement ajouter $1023$ à l'exposant afin d'obtenir uniquement des valeurs positives)



### Application de la méthode

Nous sommes maintenant prêts à écrire notre premier nombre au format simple précision :

Représentons le nombre $(-10,125)_{10}$ au format simple précision :

- $(10)_{10} = (1010)_2$
- $(0,125)_{10} = (0,001)_2$
- donc   $(10,125)_{10} = (1010,001)_2$
- Décalons la virgule : $1010,001 = 1,010001 \times 2^3$, soit avec le décalage de l'exposant $1,010001 \times 2^{130}$, en écrivant l'exposant en base $2$, nous obtenons $1,010001 \times 2^{10000010}$
- Nous avons donc :  
	1 bit de signe = $1$ (nombre négatif)  
	8 bits d'exposant = $10000010$  
	23 bits de mantisse = $01000100000000000000000$  
- Soit en "collant" tous les "morceaux" :
$11000001001000100000000000000000$

$(-10,125)_{10}$  sera représenté par $(11000001001000100000000000000000)_2$

Cette écriture étant un peu grande, il est possible de l'écrire en hexadécimal : $(C1220000)_{16}$


!!! question "Question 4 :  Déterminer la représentation au format simple précision de $(0,25)_{10}$ en binaire et en hexadécimal"



### Passage du format IEEE 754 au décimal

Il est aussi possible de passer d'une représentation au format IEEE 754 à une représentation "classique" en base $10$

Soit le nombre flottant encodé au format simple précision : $00111110100000000000000000000000$

- Si on décompose ce nombre :

    |1 chiffre|8 chiffres|23 chiffres|
    |:-:|:-:|:-:|
    |$0$|$01111101$|$00000000000000000000000$|

- On peut déjà dire que ce nombre est positif (bit de signe à $0$).

- Les 8 bits suivants $(01111101)$ nous donnent l'exposant décalé : 

    $(01111101)_2 = (125)_{10}$ , soit une fois le décalage supprimé, $125 - 127 = - 2$

- Les 23 bits suivants (la mantisse) sont uniquement des zéros

Ce qui nous donne en fin de compte : $(1,000 \times 2^{-2})_{10}$ , soit $(0,25)_{10}$

!!! question "Question 5"
    Déterminer la représentation au format simple précision de $(0,1)_{10}$ en binaire.

    ???- done "Solution"
        Nous avons ici un problème : comme déjà évoqué plus haut, nous nous retrouvons avec une "conversion" qui ne s'arrête jamais (le schéma "$0011$" se répète à l'infini) ...

        Problème, en simple précision, la mantisse est limitée à 23 bits.

        On devrait donc obtenir : $00111101110011001100110011001100$


!!! question "Question 6"
    Soit le nombre flottant au format simple précision :    
        $00111101110011001100110011001100$

    Trouver la représentation en base $10$ de ce nombre.
    
    ???- done "Solution"
        La réponse à la question posée ci-dessus est $(0,099999994)_{10}$ , or, en toute logique, nous devrions trouver $(0,1)_{10}$ .

        Cette "légère" erreur est logique quand on y réfléchit un peu.  
        Avec la limitation de la mantisse à 23 bits, on a dû "tronquer" le résultat (de toutes les façons, même avec une mantisse beaucoup plus grande, on aurait aussi eu le problème, car le schéma "$0011$" se répète à l'infini).

Cette représentation avec un nombre limité de bits des nombres flottants est un problème classique en informatique. Cela peut entrainer des erreurs d'arrondi dans les calculs qui peuvent être très gênants si on n'y prend pas garde.

Dans une console Python, si on saisit les instructions suivantes :

```python
>>> .1 + .2 == .3

>>> .1 + .1 + .1 == .3

>>> .25 + .05 == .3
```


___
## Conclusion
**En Python, Il ne faut pas tester une égalité entre deux nombres flottants mais utiliser une marge d'erreur relative**.

Ce problème est directement lié à la limitation du nombre de bits utilisés pour représenter les nombres flottants évoquée ci-dessus.
