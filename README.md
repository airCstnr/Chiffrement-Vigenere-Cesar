
# Chiffrement Vigenère-César


## Sujet

L'enigme a été proposée par la page facebook Prizoners ([voir le message](https://www.facebook.com/PrizonersGrenoble/photos/a.365401677154321.1073741829.363286627365826/560102444350909/))

L'enjeu est de déchiffrer un message codé avec le code Vigènere.


## Principe du codage Vigenère

On doit premièrement faire correspondre chaque lettre de la clé avec les lettres du message à chiffrer. Si le message est plus long que la clé, on répète la clé.  
On utilise la grille suivante pour trouver la correspondance d'une lettre de la clé avec une lettre du texte en clair pour trouer la lettre chiffrée.

![grille](http://cryptotpe.free.fr/vigenere1.png)

Le déchiffrement se fait dans le sens inverse.


## Message codé et clé

Clé : **PASSION**

Message : [ici](message.txt)


## Message décodé

Lancer le script `main.py` :
`python main.py`

Le résultat est affiché dans la console.


## Code césar

Exemple de décodage du chiffrage César [ici](cesar.py)


## Auteur

Raphaël C

