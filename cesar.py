"""
Tutoriel simple de déchiffrement de message CESAR.

Auteur : Raphaël Castanier
Date   : Juillet 2020
"""

# ordre de la lettre A dans la table ASCII
init = 65

# message chiffré
ciphertext = "RMACQADMVCRIQDCRIQDIQVKC"


# ------------------------------------------------------------------------------
print("ETAPE 1")

# affichage du message chiffré
print("Message chiffré:", ciphertext)

print()


# ------------------------------------------------------------------------------
print("ETAPE 2")

# affichage de toutes les lettres du message
for index, letter in enumerate(ciphertext):
    print("Lettre {} : {} ({})".format(index, letter, ord(letter)-init))

print()


# ------------------------------------------------------------------------------
print("ETAPE 3")

# affichage du message avec un décalage de 3
dec = 3
for index, letter in enumerate(ciphertext):
    order = ord(letter)-init # indice de la lettre chiffrée dans l'alphabet
    clearorder = (order - dec) % 26 # indice de la lettre déchiffrée dans l'alphabet
    clearletter = chr(clearorder+init) # lettre déchiffrée
    print("Lettre {} : {} ({}) -> {} ({})".format(index, letter, order, clearletter, clearorder))

print()


# ------------------------------------------------------------------------------
print("ETAPE 4")

# affichage du message avec 26 décalages
for dec in range(26):
    print("Décalage :", dec, "->", end=' ')
    for index, letter in enumerate(ciphertext):
        order = ord(letter)-init # indice de la lettre chiffrée dans l'alphabet
        clearorder = (order - dec) % 26 # indice de la lettre déchiffrée dans l'alphabet
        clearletter = chr(clearorder+init) # lettre déchiffrée
        print(clearletter, end='')
    print()

print()


# ------------------------------------------------------------------------------
print("ETAPE 5")

# on identifie le décalage qui permet de déchiffrer le message
# affichage du message déchiffré
dec = 8
print("Message déchiffré (clé={}) : ".format(dec), end='')
for index, letter in enumerate(ciphertext):
    order = ord(letter)-init # indice de la lettre chiffrée dans l'alphabet
    clearorder = (order - dec) % 26 # indice de la lettre déchiffrée dans l'alphabet
    clearletter = chr(clearorder+init) # lettre déchiffrée
    print(clearletter, end='')

print()


print("Terminé")

