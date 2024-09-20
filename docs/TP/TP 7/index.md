# Les algorithmes gloutons
___
## Problème du rendu de monnaie

Les commerçants ont à leur disposition un nombre supposé illimité de pièces de :
 
    - 1 centime
    - 2 centimes 
    - 5 centimes 
    - 10 centimes 
    - 20 centimes 
    - 50 centimes 
    - 1 € 
    - 2 € 
    
Nous devons rendre la monnaie à un client à l'aide de ces pièces. La contrainte est d'utiliser le moins de pièces possible. 

Vous devez rendre la somme de 2,63 €. Combien de pièces avez-vous utilisées ? 

Quelle méthode peut-on utiliser ?


___
## Problème du sac à dos

Un cambrioleur possède un sac à dos d'une contenance maximum de 30 Kg.  
Au cours d'un de ses cambriolages, il a la possibilité de dérober 4 objets A, B, C et D.

Voici un tableau qui résume les caractéristiques de ces objets : 

|objetA|B|C|D|
|:---:|:---:|:---:|:---:|
|masse|13 Kg|12 Kg|8 Kg|10 Kg|
|valeur marchande|700 €|400 €|300 €|300 €|

1. Déterminez les objets que le cambrioleur aura intérêt à dérober, sachant que :

- tous les objets dérobés devront tenir dans le sac à dos (30 Kg maxi) 
- le cambrioleur cherche à obtenir un gain maximum.
    
2. Réaliser une fonction `sac` qui prend en paramètre la capacité du sac et la liste d’objets (masse + valeur) et qui renvoie une liste des objets à choisir.
