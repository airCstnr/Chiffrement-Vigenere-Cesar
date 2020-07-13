#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from string import *

from vigenere import *


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
if __name__ == "__main__":
    testerVigenere()
