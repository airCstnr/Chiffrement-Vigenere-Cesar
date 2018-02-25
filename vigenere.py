#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

from string import ascii_lowercase # liste des lettres de l'alphabet en minuscule

# ----------------------------
# FONCTIONS DE TEST
# ----------------------------
def testerVigenere():
    titres = [ \
        "Grille de Vigenere :", \
        "Test de Codage de lettre :", \
        "Test de Decodage de lettre :", \
        "Test de Codage de message :", \
        "Test de Decodage de message :"
        ]

    tests = [ \
        afficherGrille, \
        testerCodageLettre, \
        testerDecodageLettre, \
        testerCodageMessage, \
        testerDecodageMessage
        ]

    for titre, test in map(None, titres, tests):
        print
        print titre
        test()

    print "Tests OK"

def testerCodageLettre():
    message_clair = "message clair"
    cle = "cle"
    for index in range(len(message_clair)):
        lettre_claire = message_clair[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        print lettre_claire, lettre_cle, lettre_codee

def testerDecodageLettre():
    message_code = "opwulkg gnlmt"
    cle = "cle"
    for index in range(len(message_code)):
        lettre_codee  = message_code[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_claire = decoderLettre(lettre_cle, lettre_codee)
        print lettre_codee, lettre_cle, lettre_claire

def testerCodageMessage():
    message_clair = "message clair"
    cle = "cle"
    print message_clair, " : ", message_clair
    print cle, " : ", cle
    print "message code : ", coderMessage(cle, message_clair)

def testerDecodageMessage():
    message_code = "opwulkg gnlmt"
    cle = "cle"
    print message_code, " : ", message_code
    print cle, " : ", cle
    print "message clair : ", decoderMessage(cle, message_code)

# ----------------------------
# FONCTIONS DE VIGENERE
# ----------------------------

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

def coderLettre(cle, lettre):
    if string.find(ascii_lowercase, lettre) > -1:
        index = string.find(ascii_lowercase, lettre) + string.find(ascii_lowercase, cle)
        return ascii_lowercase[index % len(ascii_lowercase)]
    else:
        return lettre

def decoderLettre(cle, lettre):
    if string.find(ascii_lowercase, lettre) > -1:
        index = string.find(ascii_lowercase, lettre) - string.find(ascii_lowercase, cle)
        return ascii_lowercase[index % len(ascii_lowercase)]
    else:
        return lettre

def coderMessage(cle, message_clair):
    message_code = ''
    for index in range(len(message_clair)):
        lettre_claire = message_clair[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        message_code += lettre_codee
    return message_code

def decoderMessage(cle, message_code):
    message_clair = ''
    for index in range(len(message_code)):
        lettre_codee  = message_code[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_claire = decoderLettre(lettre_cle, lettre_codee)
        message_clair += lettre_claire
    return message_clair

# ----------------------------
if __name__ == "__main__":
    testerVigenere()
