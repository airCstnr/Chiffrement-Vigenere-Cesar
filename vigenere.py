#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

from string import ascii_lowercase # liste des lettres de l'alphabet en minuscule

def afficherGrille():

    # première ligne
    print ' ',
    for l in ascii_uppercase :
        print l.upper(),
    print

    # grille
    for cle in ascii_lowercase:
        print cle.upper(), # premier caractère
        for lettre in ascii_lowercase:
            print coderLettre(cle, lettre),
        print

def coderLettre(cle, lettre):
    index = string.find(ascii_lowercase, cle) + string.find(ascii_lowercase, lettre)
    return ascii_lowercase[index % len(ascii_lowercase)]

if __name__ == "__main__":
    afficherGrille()
