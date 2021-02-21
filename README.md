# autocomplete
Test ANSSI - autocomplete

## Structure de donnée
- La structure de donnée choisie est un TRIE. ( Arbre n-aire stockant les lettres a-z à chaque niveau de l'arbre, et permettant un parcours du dictionnaire aisé)

### Amelioration
- L'utilisation d'un arbre ternaire 

## Serveur HTTP
- Le serveur est un simple http.server de la librairie standard Python

## Execution

### Serveur (ecoute sur le port 8000 par défaut)
$ python3 server.py

### Client
 - wget http://localhost:8000/autocomplete?query=crypt
 - curl http://localhost:8000/autocomplete?query=crypt
 - navigateur web

### Dictionnaires

- "dic" contient les mots du sujet
- "dic2" comprends plus de 450.000 mots
