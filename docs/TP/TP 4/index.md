# Anagrammes
___
[Souce wikipédia](https://fr.wikipedia.org/wiki/Anagramme){:target = _blank} : Une anagramme (le mot est féminin) est une construction qui inverse ou permute les lettres d'un mot ou d'un groupe de mots pour en extraire un sens ou un mot nouveau. Il est sous-entendu que ce nouveau mot existe dans un dictionnaire. 

___
## Consignes de travail

- Pour le TP, nous ne vérifierons pas si les mots existent dans un dictionnaire.
- Un exercice au choix est à traiter.


___
## Exercices
!!! question "Exercice 1"

Écrire une fonction `est_anagramme` qui précise si deux mots sont anagrammes.

??? example "Exemples"
    ```python
    >>> est_anagramme('mot','tom')
    True
    >>> est_anagramme('mot','tomo')
    False
    >>> est_anagramme('moto','tom')
    False
    >>> est_anagramme('moto','mott')
    False
    ```


!!! question "Exercice 2"

Écrire une fonction `anagramme` qui détermine tous les anagrammes d'un mot.

??? example "Exemples"
    ```python
    >>> anagramme('')
    ''
    >>> anagramme('m')
    'm'
    >>> anagramme('mo')
    'mo,om'
    >>> anagramme('mot')
    'mot,mto,omt,otm,tmo,tom'
    >>> anagramme('moto')
    'moto,moot,mtoo,omto,omot,otmo,otom,oomt,ootm,tmoo,tomo,toom'
    ```

!!! tip "Conseils" 
    Prévoir des fonctions annexes.
    Attention aux doublons.
