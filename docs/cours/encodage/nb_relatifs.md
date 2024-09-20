___
## Les additions et multiplications en système binaire

Ce sont les 2 opérations de base. Elles reposent sur deux tables élémentaires :

Table d’addition binaire (A compléter)

0 + 0 =  
0 + 1 =  
1 + 0 =  
1 + 1 =  



Table de multiplication binaire (A compléter)

0 x 0 =  
0 x 1 =  
1 x 0 =  
1 x 1 =  

!!! example "Exemples (A compléter)"

    === "addition binaire"
        $\dfrac{\begin{align}10&111001\\
        +~~~~&101110\end{align}}{}$
        
    === "addition en base $10$"
        $\dfrac{\begin{align}1&85\\
        +~~&46\end{align}}{}$
        
    === "multiplication binaire"
        $\dfrac{\begin{align}&1100\\
        \times~~~~&1101\end{align}}{}$

    === "multiplication en base $10$"
        $\dfrac{\begin{align}&12\\
        \times~~~~&13\end{align}}{}$


___
## L’ajout du signe négatif dans l’encodage

### Méthode du bit signé

La première idée qui pourrait venir à l'esprit est, sur un nombre comportant n bits, d'utiliser 1 bit pour représenter le signe et (n-1) bit pour représenter la valeur absolue du nombre à représenter.  
Le bit de signe étant le bit dit de poids fort (MSB) (c'est à dire le bit le plus à gauche), ce bit de poids fort serait à 0 dans le cas d'un nombre positif et à 1 dans le cas d'un nombre négatif.

!!! example "Exemple de $- 5$"
    - on représente l'entier $5$ sur 8 bits par $00000101$
    - $- 5$ serait donc représenté par $10000101$

Inconvénients de cette méthode :  
    - l'existence de deux zéros, un zéro positif $(00000000)$ et un zéro négatif $(10000000)$  
    - l’addition ne fonctionne pas  


### Le complément à deux
Avant de représenter un entier relatif, il est impératif de définir le nombre de bits qui seront utilisés pour cette représentation (souvent 8, 16 , 32 ou 64 bits)

!!! example "Déterminons la représentation de $- 12$ sur 8 bits"
    - Commençons par représenter $12$ sur 8 bits : $00001100$
    - Inversons tous les bits (les bits à 1 passent à 0 et vice versa) : $11110011$
    - Ajoutons $1$ au nombre obtenu à l'étape précédente :
    - La représentation de $-12$ sur 8 bits est donc : $11110100$
    - Vérification avec le complément à 2, sur 8 bits, de $-3$ :  
        - $3$ est représenté en binaire par : $00000011$  
        - inversion des bits : $11111100$  
        - ajout de $1$ : $11111101$  
        - On retrouve bien le résultat précédent.


___
## Questions

!!! question "Question 1"
En utilisant le complément à $2$, représenter $-15$ (représentation sur 8 bits).  
Réaliser l’opération $12 – 15$.

!!! question "Question 2"
Représenter sur 8 bits l'entier $4$.
Représenter, toujours sur 8 bits, l'entier $-5$.
Additionner ces 2 nombres (en binaire ).
Vérifier que vous obtenez bien $-1$.

!!! question "Question 3"
Quel est le plus petit entier négatif que l'on peut représenter sur 8 bits ?

!!! question "Question 4"
Quel est le plus grand entier positif que l'on peut représenter sur 8 bits ?

