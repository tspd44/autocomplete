# autocomplete
Test ANSSI - autocomplete

** Structure de donnée
La structure de donnée choisie est un TRIE. ( Arbre n-aire stockant les lettres a-z à chaque niveau de l'arbre, et permettant un parcours du dictionnaire aisé)

** Serveur HTTP
Le server est un simple http.server de la librairie standard Python

** Execution

*** Serveur
$ python3 server.py

*** Client
 - wget http://localhost:8000/autocomplete?query=crypt
 - curl http://localhost/autocomplete?query=crypt

