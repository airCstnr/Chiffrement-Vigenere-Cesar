#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

from string import ascii_lowercase # liste des lettres de l'alphabet en minuscule

# ----------------------------
# FONCTIONS DE TEST
# ----------------------------
def testerVigenere():
    print "Grille de Vigenere :"
    afficherGrille()
    print
    print "Test de Codage :"
    testerCodage()
    print
    # print "Test de Décodage :"
    # testerDecodage()
    # print
    print "Tests OK"

def afficherGrille():
    # première ligne
    print ' ',
    for l in ascii_lowercase :
        print l.upper(),
    print
    # grille
    for cle in ascii_lowercase:
        print cle.upper(), # premier caractère
        for lettre in ascii_lowercase:
            print coderLettre(cle, lettre),
        print

def testerCodage():
    message_clair = "message clair"
    cle = "cle"
    for index in range(len(message_clair)):
        lettre_claire = message_clair[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        print lettre_claire, lettre_cle, lettre_codee

def testerCodage():
    message_clair = "message clair"
    cle = "cle"
    for index in range(len(message_clair)):
        lettre_claire = message_clair[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        print lettre_claire, lettre_cle, lettre_codee

# ----------------------------
# FONCTIONS DE VIGENERE
# ----------------------------
def coderLettre(cle, lettre):
    if string.find(ascii_lowercase, lettre) > -1:
        index = string.find(ascii_lowercase, cle) + string.find(ascii_lowercase, lettre)
        return ascii_lowercase[index % len(ascii_lowercase)]
    else:
        return lettre

def decoderLettre(cle, lettre):
    if string.find(ascii_lowercase, lettre) > -1:
        index = string.find(ascii_lowercase, cle) - string.find(ascii_lowercase, lettre)
        return ascii_lowercase[index % len(ascii_lowercase)]
    else:
        return lettre

# ----------------------------
# UTL
# ----------------------------
if __name__ == "__main__":
    testerVigenere()
