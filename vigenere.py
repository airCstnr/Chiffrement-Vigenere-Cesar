#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from string import *


# ----------------------------
# FONCTIONS DE VIGENERE
# ----------------------------

def afficherGrille():
    """ Affiche la grille de codage/décodage """
    # première ligne
    print ' ',
    for l in ascii_uppercase:
        print l,
    print
    # reste de la grille
    for cle in ascii_lowercase:
        print cle.upper(),
        for lettre in ascii_lowercase:
            print coderLettre(cle, lettre),
        print

def coderLettre(lettre_cle, lettre_a_coder):
    """ Renvoie une lettre à coder codée par la lettre clé """
    # ne coder que les lettres de l'alphabet, pas les espaces ou autre caractère
    assert string.find(ascii_letters, lettre_a_coder) > -1

    index_lettre_a_coder = string.find(ascii_lowercase, lettre_a_coder.lower())
    index_lettre_cle = string.find(ascii_lowercase, lettre_cle.lower())
    index = index_lettre_a_coder + index_lettre_cle
    # gérer les majuscules
    if(lettre_a_coder.isupper()):
        return ascii_uppercase[index % len(ascii_uppercase)]
    else:
        return ascii_lowercase[index % len(ascii_lowercase)]

def decoderLettre(lettre_cle, lettre_a_decoder):
    """ Renvoie une lettre à décoder décodée par la lettre clé """
    # ne décoder que les lettres de l'alphabet, pas les espaces ou autre caractère
    assert string.find(ascii_letters, lettre_a_decoder) > -1

    index_lettre_a_decoder = string.find(ascii_lowercase, lettre_a_decoder.lower())
    index_lettre_cle = string.find(ascii_lowercase, lettre_cle.lower())
    index = index_lettre_a_decoder - index_lettre_cle

    # gérer les majuscules
    if(lettre_a_decoder.isupper()):
        return ascii_uppercase[index % len(ascii_uppercase)]
    else:
        return ascii_lowercase[index % len(ascii_lowercase)]

def coderMessage(cle, message_clair):
    message_code = ''
    index_cle = 0
    for lettre_claire in message_clair:
        # ignorer les caractères non chiffrés
        if lettre_claire not in ascii_letters:
            message_code += lettre_claire
            continue
        lettre_cle    = cle[index_cle % len(cle)]
        lettre_codee  = coderLettre(lettre_cle, lettre_claire)
        message_code += lettre_codee
        index_cle    += 1
    return message_code

def decoderMessage(cle, message_code):
    message_clair = ''
    index_cle = 0
    for lettre_codee in message_code:
        # ignorer les caractères non chiffrés
        if lettre_codee not in ascii_letters:
            message_clair += lettre_codee
            continue
        lettre_cle     = cle[index_cle % len(cle)]
        lettre_claire  = decoderLettre(lettre_cle, lettre_codee)
        message_clair += lettre_claire
        index_cle     += 1
    return message_clair

