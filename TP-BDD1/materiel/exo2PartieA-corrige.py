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
        
film = lecture('film.txt')
jouer = lecture('jouer.txt')
projection = lecture('projection.txt')
personne = lecture('personne.txt')

"""
In [1]: film[0]
Out[1]: ('01', '15', 'Crash', 'Drame', '1996')

In [2]: jouer[0]
Out[2]: ('01', '05', 'Grace')

In [3]: projection[0]
Out[3]: ('02', '05', '01-05-2002')

In [4]: personne[0]
Out[4]: ('01', 'Kidman', 'Nicole')
"""

def requete1():
    """Retourne la liste des personnes dont le prenom est John"""
    t = []
    for p in personne:
        if p[-1] == 'John':
            t.append(p)
    return t

"""
In [8]: requete1()
Out[8]: [('05', 'Travolta', 'John'), ('12', 'Wayne', 'John'), 
('18', 'Glen', 'John')]
"""

def requete2():
    """Retourne la liste de tous les prenoms dans l'ordre alphabetique"""
    prenom = []
    for p in personne:
        prenom.append(p[-1])
    prenom.sort()
    return prenom
    
"""
In [14]: requete2()
Out[14]: 
['Angelina', 'Bruce',... ,'Stellan']
 """
 
def requete3():
    """Retourne la liste de tous les prenoms dans l'ordre alphabetique
    sans doublons"""
    prenom = requete2()
    newprenom = [prenom[0]]
    #on utilise le fait que prenom est deja dans l'ordre alphabetique
    for p in prenom[1:]:
        if p != newprenom[-1]:
            newprenom.append(p)
    return newprenom

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
    #recherche de l'identifiant de Lars Von Trier
    for p in personne:
        if p[1] == 'von Trier':
            id = p[0]
    filmTrier = []
    for f in film:
        if f[1] == id:
            filmTrier.append(f[2])
    return filmTrier

"""
In [17]: requete4()
Out[17]: ['Breaking the waves', 'Dogville']
"""

 
