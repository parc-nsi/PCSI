# -*- coding: utf-8 -*-
"""Exo1 TP 14 Bases de donnees"""

##Exo 1

def lecture(fichier):
    """Ouvre un fichier texte où chaque ligne est constituee de champs
    separes par des tabulations et se termine par un saut de ligne.
    Lit le fichier ligne par ligne et collecte les differents champs dans
    un tuple puis insere ce tuple dans une liste"""
    f = open(fichier)
    collecteur = []
    for ligne in f:
        champs = tuple(ligne.rstrip().split('\t'))
        collecteur.append(champs)
    f.close()
    return collecteur
        


def requete1():
    """Retourne la liste des personnes dont le prenom est John"""
    pass

"""
In [8]: requete1()
Out[8]: [('05', 'Travolta', 'John'), ('12', 'Wayne', 'John'), ('18', 'Glen', 'John')]
"""

def requete2():
    """Retourne la liste de tous les prenoms dans l'ordre alphabetique"""
    pass
    
"""
In [14]: requete2()
Out[14]: 
['Angelina',
 'Bruce',
 'Clint',
 'David',
 'Emily',
 'Grace',
 'Holly',
 'James',
 'Jeremy',
 'John',
 'John',
 'John',
 'Kevin',
 'Lars',
 'Nicole',
 'Paul',
 'Paul',
 'Quentin',
 'Rosanna',
 'Sam',
 'Samuel',
 'Stellan']
 """
 
def requete3():
    """Retourne la liste de tous les prenoms dans l'ordre alphabetique
    sans doublons"""
    pass

"""
In [2]: len(requete2())
Out[2]: 22

In [3]: len(requete3())
Out[3]: 19

In [4]: requete3()
Out[4]: 
['Angelina',
 'Bruce',
 'Clint',
 'David',
 'Emily',
 'Grace',
 'Holly',
 'James',
 'Jeremy',
 'John',
 'Kevin',
 'Lars',
 'Nicole',
 'Paul',
 'Quentin',
 'Rosanna',
 'Sam',
 'Samuel',
 'Stellan']
"""
 
def requete4():
    """Retourne la liste de tous les films realises par Lars Von trier"""
    pass

"""
In [17]: requete4()
Out[17]: ['Breaking the waves', 'Dogville']
"""

 