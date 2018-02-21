#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

from string import ascii_lowercase #liste des lettres de l'alphabet en minuscule

def afficherGrille():
    print(ascii_lowercase)
    for cle in ascii_lowercase:
        for lettre in ascii_lowercase:
            print(coderLettre(cle, lettre), '', ' ')
        print("\n")

def coderLettre(cle, lettre):
    index = string.find(ascii_lowercase, cle) + string.find(ascii_lowercase, lettre)
    return ascii_lowercase[index]

if __name__ == "__main__":
    afficherGrille()
