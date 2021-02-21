# autocomplete
Test ANSSI - autocomplete

## Structure de donnée
- La structure de donnée choisie est un TRIE. ( Arbre n-aire stockant les lettres a-z à chaque niveau de l'arbre, et permettant un parcours du dictionnaire aisé). La complexité liée à la recherche du motif X est O(n), où n est la longueur de la chaîne X.

## Ameliorations
### Mémoire
- Utilisation d'un arbre ternaire semble être moins coûteux en mémoire
### Prediction
- Utilisation d'un dictionnaire intermédiaire regroupant les recherches les plus courantes
### BFS versus DFS 
- Evaluer les résultats avec un parcours en largeur de l'arbre au lieu d'un parcours en profondeur

## Serveur HTTP
- Le serveur est un simple http.server de la librairie standard Python

## Execution

### Serveur (ecoute sur le port 8000 par défaut)
$ python3 server.py

### Client
 - wget http://localhost:8000/autocomplete?query=crypt
 - curl http://localhost:8000/autocomplete?query=crypt
 - navigateur web

## Dictionnaires

- "dic" contient les mots du sujet
- "dic2" comprends plus de 450.000 mots
