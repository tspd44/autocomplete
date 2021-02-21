# autocomplete
Test ANSSI - autocomplete

## Structure de donnée
La structure de donnée choisie est un TRIE. ( Arbre n-aire stockant les lettres a-z à chaque niveau de l'arbre, et permettant un parcours de la clef recherché en O(n), n étant la taille de la chaine caractère)

## Serveur
Le serveur est un simple http.server de la librairie standard Python

# Execution serveur :
$ python3 server.py

# Exetution client :
$ wget http://localhost:8000/autocomplete?query=crypt

