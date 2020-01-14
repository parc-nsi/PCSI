# -*- coding: utf-8 -*-

import random
from math import sqrt



def est_premier(n):
    if n <= 1:
        return False
    for k in range(2, 1+int(sqrt(n))):
        if n%k == 0:
            return False
    return True




def creer_departements(fichier, n):
    """Cree un fichier texte contenant n noms de départements
    de format *****numero_ligne où * est une lettre majuscule"""
    debut = ord('A')
    fin = ord('Z')
    f = open(fichier, 'w')
    for k in range(1, n+1):
        f.write(''.join(chr(random.randint(debut, fin)) for j in range(5)) + \
        str(k) + '\n')
    f.close()
    
def chrono(fonction):
    
    import time
    
    def fonction2(*args):
        chrono_debut = time.time()
        rep = fonction(*args)
        chrono_fin = time.time()
        print('Valeur de retour de {:s} : {:d} en {:1.6f} secondes'.format(\
        fonction.__name__, rep, chrono_fin - chrono_debut))
        
    return fonction2
    
def nettoyer_accent(infile, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    dicoTrans = { k : 'e' for k in range(232, 236)}
    #dicoTrans.update({ ord(chr(k).upper())  : 'E' for k in range(232, 236)})  
    dicoTrans.update({ k  : 'i' for k in range(236, 240)})
    #dicoTrans.update({ ord(chr(k).upper())  : 'I' for k in range(236, 240)})
    dicoTrans.update({ k : 'a' for k in range(224, 230)})
    #dicoTrans.update({ ord(chr(k).upper())  : 'A' for k in range(224, 230)})
    dicoTrans.update({ k : 'o' for k in range(242, 247)})
    #dicoTrans.update({ ord(chr(k).upper())  : 'O' for k in range(242, 247)})
    dicoTrans.update({ k : 'u' for k in range(249, 253)})
    #dicoTrans.update({ ord(chr(k).upper())  : 'U' for k in range(249, 253)})
    dicoTrans.update({ k : 'y' for k in range(253, 256)})
    #dicoTrans.update({ ord(chr(k).upper())  : 'Y' for k in range(253, 256)})
    dicoTrans.update({ 231 : 'c'})  #c avec cédille
    #dicoTrans.update({ ord(chr(231).upper()) : 'C'}) 
    #dictionnaire de translation
    dicoTrans = str.maketrans(dicoTrans)
    #dictionnaire de translation
    dicoTrans = str.maketrans(dicoTrans)
    for ligne in f:
        ligne2 = ligne.lower().translate(dicoTrans)
        g.write(ligne2)
    g.close()
    f.close()