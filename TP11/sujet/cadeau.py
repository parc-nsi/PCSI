"""TP 11 Pivot de Gauss
Fonctions cadeaux : 
1)copie de matrice 
2)matrice identite
3) a propos des booleens
4) operateurs booleens de base (tables de verite)
5) expressions booleennes avec des litteraux et application 
(matrice identite, matrice de virginie etc ...)
"""

##Copie de matrice 
def copie(m):
    """retourne une copie de la matrice m"""
    nlines,ncols = len(m),len(m[0])
    cp = [[0]*ncols for _ in range(nlines)]
    for i in range(nlines):
        for j in range(ncols):
            cp[i][j]=m[i][j]
    return  cp


def matrice_nulle(n,p):
    """Retourne la matrice nulle de n lignes et p colonnes"""
    return [[0 for j in range(p)] for i in range(n)]
    

def dimensions(m):
    """dimensions d'une matrice"""
    return len(m),len(m[0])
     
def copie2(m):
    """retourne une copie de la matrice m"""
    nlines,ncols = dimensions(m)
    cp = matrice_nulle(nlines,ncols) # matrice copie
    for i in range(nlines):
        for j in range(ncols):
            cp[i][j]=m[i][j]
    return  cp

##Matrice identite
def identite1(n):
    """Retourne une matrice carree identite de dimensions n*n"""
    return [[0]*i + [1] + [0]*(n - i -1 ) for i in range(n)]
    
def identite2(n):
    """Retourne une matrice carree identite de dimensions n*n"""
    return [[int(i == j)  for j in range(n)] for i in range(n)]

def identite3(n):
    """Retourne une matrice carree identite de dimensions n*n"""
    return [[(i == j and 1) or 0 for j in range(n)] for i in range(n)]

""""
>>> identite1(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

>>> identite2(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

>>> identite3(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
"""


##A propos des booleens

"""
Les expressions de tout type (ou littéraux) ont une évaluation
booléeenne. Elles sont toutes évaluées à True sauf les constructions
vides et l'entier 0. Attention [] est une liste vide mais pas [[]] :

>>> bool(None)
False
>>> bool([])  #liste vide
False
>>> bool({})  #dictionnaire vide
False
>>> bool(()) #tuple vide
False
>>> bool('') #chaine vide
False
>>> bool(set()) #ensemble vide
False
>>> bool(0)  #entier nul
False
>>> bool(0.)  #flottant nul
False
>>> 2**(-1023-52)
0.0
>>> bool(2**(-1023-52)) #un autre flottant nul
False
>>> bool([[]])  # ce n'est pas une liste vide
True
"""



##Opérateurs booléens de base


def ou(x,y):
    """ou inclusif """
    return x or y

def et(x,y):
    """et"""
    return x and y

def xou(x,y):
    """ou exclusif"""
    return (x and not y) or (not x and y)

def non(x):
    """non"""
    return not x

def table(f):#table de verite d'une fonction booleenne à 2 arguments
    print('Table de vérité de la fonction %s'%f.__name__)
    for x in [True,False]:
        if f.__name__ != 'non':
            for y in [True,False]:
                print('x=',x,'y=',y,'%s(x,y)='%f.__name__,f(x,y),sep=' ')
        else:
            print('x=',x,'%s(x)='%f.__name__,f(x),sep=' ')

for f in [non, et, ou, xou]:
    table(f)
    print()

"""
Table de vérité de la fonction non
x= True non(x)= False
x= False non(x)= True

Table de vérité de la fonction et
x= True y= True et(x,y)= True
x= True y= False et(x,y)= False
x= False y= True et(x,y)= False
x= False y= False et(x,y)= False

Table de vérité de la fonction ou
x= True y= True ou(x,y)= True
x= True y= False ou(x,y)= True
x= False y= True ou(x,y)= True
x= False y= False ou(x,y)= False

Table de vérité de la fonction xou
x= True y= True xou(x,y)= False
x= True y= False xou(x,y)= True
x= False y= True xou(x,y)= True
x= False y= False xou(x,y)= False
"""

##utilisation des opérateurs booléens avec les littéraux

"""
Lorsqu'on écrit une expression booléenne complexe comprenant plusieurs
opérandes dont des  littéraux isolés, ceux-ci seront remplacés par leur évaluation booléenne dans l'évaluation booléenne de l'expression totale.
Si l'expression totale est True, le premier opérande  qui la rend True
est renvoyé (le dernier s'il n'y a que des and et le premier s'il n'y a
que des or). 
Si l'expression totale est False, le premier opérande  qui la rend False
est renvoyé (le premier s'il n'y a que des and et le dernier s'il n'y a
que des or). 
Si c'est un littéral, sa valeur est littérale est renvoyée:

Cas du or :

>>> True or 2
True
>>> 2 or True
2
>>> 0 or True  #0 a une evaluation booléeene False
True
>>> True or 0
True
>>> False or 0
0
>>> 0 or False
False
>>> False or []
[]
>>> [] or False
False

Cas du and :

>>> True and 1
1
>>> 1 and True
True
>>> 0 and True
0
>>> '' and True
''
>>> True and 0
0
>>> False and 0
False
"""

""" Application 1 :

Si on veut un littéral uniquement si une condition
est True on écrit  :

condition and litteral 

>>> 1 == 2 and 'coefficient diagonal'
False

>>> 2 == 2 and 'coefficient diagonal'
'coefficient diagonal'
"""

"""Application 2 :

Si on veut un littéral1 uniquement si une condition
est True et sinon on veut un litteral2 on écrit :

condition and litteral1 or litteral2

>>> 1 == 2 and 'coefficient diagonal' or 'coefficient non diagonal'
'coefficient non diagonal'

>>> 2 == 2 and 'coefficient diagonal' or 'coefficient non diagonal'
'coefficient diagonal'
"""

"""
On peut utiliser ce genre de constructions dans des listes en compréhensions pour remplacer des structures conditionnelles 
du type if elif else  et construire ainsi facilemnt la matrice
identité (voir plus haut) ou la matrice de virginie de dimensions n*n

"""

def virginie2(n):
    """Retourne une matrice de Virginie de dimensions  nxn"""
    assert str(type(n))=="<class 'int'>" and n>=2,"n doit etre un entier >=2"
    return [[(i == j-1 and -1) or (i == j and 2) or (i == j+1 and -1) or 0 for j in range(n)] for i in range(n)]

def virginie3(n):
    """Retourne une matrice de Virginie de dimensions  nxn"""
    assert str(type(n))=="<class 'int'>" and n>=2,"n doit etre un entier >=2"
    return [[ (i == j and 2) or ((i == j+1 or i == j - 1) and -1) or 0 for j in range(n)] for i in range(n)]



"""
>>> virginie2(6)
[[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, 0],
 [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
>>> virginie3(6)
[[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, 0], 
[0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
"""
