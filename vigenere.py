#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from string import *

message_clair_a_coder  = "Message Clair"
message_code_a_decoder = "Opwulkg Gnlmt"
cle                    = "Cle"

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
        afficherTitre(titre)
        test()

    afficherTitre("Tests OK")

def afficherTitre(titre):
    print
    print "-----------------------"
    print titre
    print "-----------------------"
    print

def testerCodageLettre():
    for index in range(len(message_clair_a_coder)):
        lettre_claire = message_clair_a_coder[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        print lettre_claire, lettre_cle, lettre_codee

def testerDecodageLettre():
    for index in range(len(message_code_a_decoder)):
        lettre_codee  = message_code_a_decoder[index]
        lettre_cle    = cle[index % len(cle)]
        lettre_claire = decoderLettre(lettre_cle, lettre_codee)
        print lettre_codee, lettre_cle, lettre_claire

def testerCodageMessage():
    print "Message clair :", message_clair_a_coder
    print "Message code  :", coderMessage(cle, message_clair_a_coder)

def testerDecodageMessage():
    print "Message code  :", message_code_a_decoder
    print "Message clair :", decoderMessage(cle, message_code_a_decoder)

# ----------------------------
# FONCTIONS DE VIGENERE
# ----------------------------

def afficherGrille():
    # première ligne
    print ' ',
    for l in ascii_uppercase :
        print l,
    print
    # grille
    for cle in ascii_lowercase:
        print cle.upper(),
        for lettre in ascii_lowercase:
            print coderLettre(cle, lettre),
        print

def coderLettre(cle, lettre):
    if string.find(ascii_letters, lettre) > -1:
        index = string.find(ascii_lowercase, lettre.lower()) + string.find(ascii_lowercase, cle.lower())
        if(lettre.isupper()):
            return ascii_uppercase[index % len(ascii_uppercase)]
        else:
            return ascii_lowercase[index % len(ascii_lowercase)]
    else:
        return lettre

def decoderLettre(cle, lettre):
    if string.find(ascii_letters, lettre) > -1:
        index = string.find(ascii_lowercase, lettre.lower()) - string.find(ascii_lowercase, cle.lower())
        if(lettre.isupper()):
            return ascii_uppercase[index % len(ascii_uppercase)]
        else:
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
