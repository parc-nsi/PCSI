# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 07:44:32 2013

@author: stephane
"""

from random import randint

def caractere_aleatoire():
    return ['a','c','g','t'][randint(0,3)]

def chaine_aleatoire(n):
    return ''.join([caractere_aleatoire() for _ in range(n)])
