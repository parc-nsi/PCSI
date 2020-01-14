# -*- coding: utf-8 -*-


mon_fichier = open('tagada.txt','r')
s = 0
for L in mon_fichier:
    s += len(L)
mon_fichier.close()


from math import sqrt

def est_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for k in range(2, 1+int(sqrt(n))):
        if n%k == 0:
            return False
    return True
