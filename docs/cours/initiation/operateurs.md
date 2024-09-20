# Opérateurs et expressions booléennes
___
Python peut évaluer certaines expressions en vérifiant si elles sont vraies (True) ou fausses (False).
Ce sont des expressions booléennes. Elles s'utilisent avec des opérateurs.

## Opérateurs de comparaison

|Expressions|Significations|
|:-:|:-|
|`a == b`|a est égal à b|
|`a != b`|a est différent de b|
|`a > b`|a est strictement supérieur à b|
|`a >= b`|a est supérieur ou égal à b|
|`a < b`|a est strictement inférieur à b|
|`a <= b`|a est inférieur ou égal à b|

## Opérateurs booléens

|Expressions|Significations|
|:-:|:-|
|`bool1 and bool2`|bool1 ET bool2 sont évalués True (tous les deux)|
|`bool1 or bool2`|bool1 OU bool2 est évalué True (au moins un, bool1 en premier|
|`bool1 xor bool2`|bool1 OU bool2 est évalué True (seulement un sur les deux)|
|`not(bool1)`|contraire de bool1|

L'action de ces expressions booléennes peut se résumer dans des tables.

Dans une table, on simplifie l'écriture de `True` par $1$ et `False` par $0$.
_(cette simplification prendra tout son sens lors de l'étude du fonctionnement logique du processeur dans un ordinateur)_

## Table `and`

|`bool1`|`bool2`|`bool1 and bool2`|
|:-:|:-:|:-:|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

## Table `or`

|`bool1`|`bool2`|`bool1 or bool2`|
|:-:|:-:|:-:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

## Table `xor`

|`bool1`|`bool2`|`bool1 xor bool2`|
|:-:|:-:|:-:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

## Table `not`

|`bool1`|`not bool1`|
|:-:|:-:|
|0|1|
|1|0|
