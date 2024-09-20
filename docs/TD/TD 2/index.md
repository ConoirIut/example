# Opérateurs et expressions booléennes

___
## Méthode de travail

Un module python devra être créé pour chaque exercice avec le module

??? tip "`Modele.py` (TD 1)"
    ```python
    # -*- coding: utf-8 -*-
    '''
    :Titre :
    :Auteur : 
    :Date : 
    
    Exercice n°.. du TD n°..
    '''
    ```
Renommer le avant d'écrire du code : Fichier -> Save As

___
## Exercices

!!! question "Exercice 1 :  Maximum de 2 nombres"

1. Demander à l'utilisateur un premier nombre. Affecter sa réponse à la variable `nombre1`.

2. Faites de même avec un deuxième nombre : variable `nombre2`.

3. En utilisant une instruction conditionnelle, afficher un texte précisant le plus grand des deux.


!!! question "Exercice 2 :   Maximum de 3 nombres"

En vous inspirant de l'exercice précédent, réaliser un programme précisant le plus grand de trois nombres.


!!! question "Exercice 3 : Nombre de jours depuis le début de l'année"

1. Déclarer la date d'aujourd'hui en utilisant les variables `jour`, `mois`, `annee`, de type `int()`.

2. Vérifier si l'année est bissextile et déclarer une variable booléenne `est_bissextile` dont la valeur précise si c'est le cas.

3. Déclarer une variable `nb_jours_debut`, initialisée à `0`, qui permettra d'accumuler les jours comptés.

4. A l'aide d'une boucle `for`, passer en revue tous les mois entiers depuis le début de l'année et jusqu'au mois précédent.
Ajouter au fur et à mesure le nombre de jours, en tenant compte de chaque mois.

5. Finir de compter avec le mois actuel et afficher alors le nombre de jours écoulés depuis le début de l'année.


!!! question "Exercice 4 :  Nombre de jours jusqu'à la fin de l'année"

En vous inspirant de l'exercice précédent, réaliser un programme déterminant le nombre restant avant la fin de l'année, que l'on affectera à la variable `nb_jours_fin`.


!!! question "Exercice 5 :  Nombre de jours entre deux dates"

1. Demander à l'utilisateur une première date (sous forme de nombres entiers) :
    • demander le jour et affecter sa réponse à la variable `jour1`.
    • demander le mois et affecter sa réponse à la variable `mois1`.
    • demander l'année et affecter sa réponse à la variable `annee1`.

2. Faites la même chose pour une deuxième date : `jour2, mois2, annee2`

3. Déterminer la date la plus ancienne des deux en déclarant les variables suivantes :
	`date1_jour, date1_mois, date1_annee` : pour la date la plus ancienne
	`date2_jour, date2_mois, date2_annee` : pour la date la plus récente

4. Déterminer le nombre de jours entre ces deux dates


!!! question "Exercice 6 :   Nombre de mots"

    Voici un texte :
    
    !!! cite "Définition de l'ordinateur ([selon Wikipedia](https://fr.wikipedia.org/wiki/Ordinateur){:target = _blank})"
        Un ordinateur est un système de traitement de l'information programmable tel que défini par Alan Turing et qui fonctionne par la lecture séquentielle d'un ensemble d'instructions, organisées en programmes, qui lui font exécuter des opérations logiques et arithmétiques. Sa structure physique actuelle fait que toutes les opérations reposent sur la logique binaire et sur des nombres formés à partir de chiffres binaires. Dès sa mise sous tension, un ordinateur exécute, l'une après l'autre, des instructions qui lui font lire, manipuler, puis réécrire un ensemble de données déterminées par une mémoire morte d'amorçage. Des tests et des sauts conditionnels permettent de passer à l'instruction suivante et donc d'agir différemment en fonction des données ou des nécessités du moment ou de l'environnement.  
        Le mot ordinateur fut introduit par IBM France en 19556,7 après que François Girard, alors responsable du service publicité de l'entreprise, eut l'idée de consulter son ancien professeur de lettres à Paris, Jacques Perret. Avec Christian de Waldner, alors président d'IBM France, ils demandèrent au professeur Perret, de suggérer un nom français pour sa nouvelle machine électronique destinée au traitement de l'information (IBM 650), en évitant d'utiliser la traduction littérale du mot anglais computer (calculateur ou calculatrice), qui était à cette époque plutôt réservé aux machines scientifiques.  
        En 1911, une description de la machine analytique de Babbage utilisait le mot ordonnateur pour en décrire son organe moteur :  Pour aller prendre et reporter les nombres… et pour les soumettre à l’opération demandée, il faut qu'il y ait dans la machine un organe spécial et variable : c'est l'ordonnateur. Cet ordonnateur est constitué simplement par des feuilles de carton ajourées, analogues à celle des métiers Jacquard… .  
        Le professeur proposa un mot composé centré autour d'ordonnateur : celui qui met en ordre et qui avait aussi la notion d'ordre ecclésiastique dans l'église catholique (ordinant). Il suggéra plus précisément ordinatrice électronique, le féminin ayant pu permettre, selon lui, de mieux distinguer l'usage religieux de l'usage comptable du mot.  
        IBM France retint le mot ordinateur et chercha au début à protéger ce nom comme une marque. Mais le mot fut facilement et rapidement adopté par les utilisateurs et IBM France décida au bout de quelques mois de le laisser dans le domaine public.  

Ecrire un programme qui détermine le nombre de mots dans le texte.

!!! info "Qu'est-ce qu'un mot ?"
    Une lettre avec apostrophe est un mot  
    ...
   
