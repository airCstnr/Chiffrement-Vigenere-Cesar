#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from string import *

from vigenere import *


message_clair_a_coder  = "Message Clair ',?-.!"
message_code_a_decoder = "Opwulkg Npctv ',?-.!"
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
    index_cle = 0
    for lettre_claire in message_clair_a_coder:
        if lettre_claire not in ascii_letters:
            lettre_cle    = ' '
            lettre_codee  = lettre_claire
        else:
            lettre_cle    = cle[index_cle % len(cle)]
            lettre_codee  = coderLettre(lettre_cle, lettre_claire)
            index_cle    += 1
        print lettre_claire, lettre_cle, lettre_codee

def testerDecodageLettre():
    index_cle = 0
    for lettre_codee in message_code_a_decoder:
        if lettre_codee not in ascii_letters:
            lettre_cle    = ' '
            lettre_claire = lettre_codee
        else:
            lettre_cle    = cle[index_cle % len(cle)]
            lettre_claire = decoderLettre(lettre_cle, lettre_codee)
            index_cle    += 1
        print lettre_codee, lettre_cle, lettre_claire

def testerCodageMessage():
    print "Message clair :", message_clair_a_coder
    print "Message codé  :", coderMessage(cle, message_clair_a_coder)

def testerDecodageMessage():
    print "Message codé  :", message_code_a_decoder
    print "Message clair :", decoderMessage(cle, message_code_a_decoder)

# ----------------------------
if __name__ == "__main__":
    testerVigenere()
