# -*- coding: utf-8 -*-

"""
Lien vers un exemple

http://pythontutor.com/visualize.html#code=L+%3D+%5B0,0,0%5D*4%0AN+%3D+%5B%5B0,0,0%5D%5D*4%0AN%5B1%5D%5B1%5D+%3D+2%0AM+%3D+%5B%5B0,0,0%5D+for+i+in+range(4)%5D%0AM%5B1%5D%5B1%5D+%3D+2%0AP+%3D+%5B%5B0+for+i+in+range(3)%5D+for+j+in+range(4)%5D%0AP%5B1%5D%5B1%5D+%3D+2%0AQ+%3D+%5B%5B0%5D*3+for+j+in+range(4)%5D&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0
"""


"""Un autre exemple

http://pythontutor.com/visualize.html#code=R+%3D+%5B0,0,0%5D%0AS+%3D+%5BR%5D+%2B+%5BR%5D+%2B+%5BR%5D+%2B+%5BR%5D%0AT+%3D+%5B%5B0,0,0%5D%5D+%2B+%5B%5B0,0,0%5D%5D++%2B+%5B%5B0,0,0%5D%5D++%2B+%5B%5B0,0,0%5D%5D+&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0

"""

def matrice_nulle(n,p):
    """Retourne la matrice nulle de n lignes et p colonnes"""
    return [[0 for j in range(p)] for i in range(n)]

#On peut faire [[0]*p for _ in range(n)] mais surtout pas [[0]*p]*n
    

def dimensions(m):
    """Retourne le couple (nlignes,ncolonnes) caractérisant la matrice m"""
    return len(m),len(m[0])


"""
http://pythontutor.com/visualize.html#code=m+%3D+%5B%5Bj+for+j+in+range(i,+i+%2B3)%5D+for+i+in+range(2)%5D%0At+%3D+%5Bi+for+i+in+range(4)%5D%0A%0Adef+copie1(m)%3A%0A++++return+m%5B%3A%5D%0A++++%0Ap+%3D+copie1(m)%0As+%3D+copie1(t)%0A%0Adef+dimensions(m)%3A%0A++++%22%22%22Retourne+le+couple+(nlignes,ncolonnes)+caract%C3%A9risant+la+matrice+m%22%22%22%0A++++return+len(m),len(m%5B0%5D)%0A%0Adef+zeros(n,p)%3A%0A++++%22%22%22Retourne+la+matrice+nulle+de+n+lignes+et+p+colonnes%22%22%22%0A++++return+%5B%5B0+for+j+in+range(p)%5D+for+i+in+range(n)%5D%0A++++%0Adef+copie2(m)%3A%0A++++nline,+ncol+%3D+dimensions(m)%0A++++new+%3D+zeros(nline,+ncol)%0A++++for+i+in+range(nline)%3A%0A++++++++for+j+in+range(ncol)%3A%0A++++++++++++new%5Bi%5D%5Bj%5D+%3D+m%5Bi%5D%5Bj%5D%0A++++return+new%0A%0Aq+%3D+copie2(m)%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=84

"""

def copie(m):
    """retourne une copie de la matrice m"""
    nlines,ncols = dimensions(m)
    cp = matrice_nulle(nlines,ncols) # matrice copie
    for i in range(nlines):
        for j in range(ncols):
            cp[i][j]=m[i][j]
    return  cp

"""
>>> m1 = matrice_nulle(3, 2)
>>> m2 = copie(m1)
>>> m2
[[0, 0], [0, 0], [0, 0]]
>>> m1[1][1] = 3
>>> m1,m2
([[0, 0], [0, 3], [0, 0]], [[0, 0], [0, 0], [0, 0]])
"""

def copie1(m):
    """copie de matrice avec une liste en compréhension"""
    return [[m[i][j] for j in range(len(m[0]))] for i in range(len(m))]

"""
>>> m1=matrice_nulle(3,2)
>>> m2=copie2(m1)
>>> m2
[[0, 0], [0, 0], [0, 0]]
>>> m1[1][1]=1
>>> m1,m2
([[0, 0], [0, 1], [0, 0]], [[0, 0], [0, 0], [0, 0]])
"""

def copie2(m):
    """retourne une copie de la matrice m"""
    cp = [] #matrice copie
    nlines,ncols = dimensions(m)
    for i in range(nlines):
        ligne = [] #vecteur ligne
        for j in range(ncols):
            ligne.append(m[i][j])
        cp.append(ligne)
    return cp
    
    
#Matrice pour le sujet de Centrale 2016

conflit = [ [  0,  0,  0,100,100,  0,  0,150,  0],
            [  0,  0,  0,  0,  0, 50,  0,  0,  0],
            [  0,  0,  0,  0,200,  0,  0,300, 50],
            [100,  0,  0,  0,  0,  0,400,  0,  0],
            [100,  0,200,  0,  0,  0,200,  0,100],
            [  0, 50,  0,  0,  0,  0,  0,  0,  0],            
            [  0,  0,  0,400,200,  0,  0,  0,  0],            
            [150,  0,300,  0,  0,  0,  0,  0,  0],            
            [  0,  0, 50,  0,100,  0,  0,  0,  0] ]


