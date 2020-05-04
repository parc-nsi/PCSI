#imports pour tout le TP
import os.path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

REPERTOIRE = 'jolis-dessins' #nom du répertoire de stockage des jolis dessins

def euler(F, a, y0, b, n):
    """Retourne le tableau des approximations
    de y'=F(t,y) avec y(a)=y0 par la methode d'Euler avec un pas  de 1/n
    """
    les_yk = [y0]         # la liste des valeurs calculées
    t = a                # le temps du dernier calcul
    h = float(b-a) / n  # le pas
    dernier = y0          # la dernière valeur calculée
    for i in range(n):
        suivant = dernier + h*F(dernier, t) # le nouveau terme
        les_yk.append(suivant)  # on le place à la fin des valeurs calculées
        t = t+h                 # le nouveau temps
        dernier = suivant       # et on met à jour le dernier terme calculé
    return les_yk  # c'est fini

##    
    
def heun(F, a, y0, b, n):
    """Retourne le tableau des approximations
    de y'=F(t,y) avec y(a)=y0 par la methode de Heun avec un pas  de 1/n
    """
    les_yk = [y0]         #la liste des valeurs calculées
    t = a                #le temps du dernier calcul
    h = float(b-a) / n  #le pas
    dernier = y0          # la dernière valeur calculée
    
    for i in range(n):
        eul = dernier + h*F(dernier, t) # ce que propose Euler
        suivant = dernier + h/2*(F(dernier, t) + F(eul, t+h)) #nouveau terme
        les_yk.append(suivant)  #on le place à la fin des valeurs calculées
        t = t+h                 #nouveau temps
        dernier = suivant       #on met à jour le dernier terme calculé
    return les_yk
    
def RK4(F, a, y0, b, n):
    """Retourne le tableau des approximations
    de y'=F(t,y) avec y(a)=y0 par la methode de RK4 avec un pas  de 1/n
    """
    les_yk = [y0]         # la liste des valeurs calculées
    t = a                # le temps du dernier calcul
    h = float(b-a) / n  # le pas
    dernier = y0          # la dernière valeur calculée
    for i in range(n): 
        alpha = dernier + h/2*F(dernier, t)
        beta = dernier + h/2*F(alpha, t+h/2)
        gamma = dernier + h*F(beta, t+h/2)
        suivant = dernier + h/6*(F(dernier, t) + 2*F(alpha, t+h/2) +
                        2*F(beta, t+h/2) + F(gamma,t+h)) # le nouveau terme
        les_yk.append(suivant)  # on le place à la fin des valeurs calculées
        t = t+h                 # le nouveau temps
        dernier = suivant       # et on met à jour le dernier terme calculé
    return les_yk 
    
##    

def f_pendule(z, t):
    y, yp = z  #y=z[0] et yp=z[1]
    return np.array([yp, -31.36*np.sin(y)])

##

def exo4():
    """Fonction test de l'exo 4
    Approximation de la solution de y'' = -(omega_0)^2*sin(y) sur [0;2]
    avec y(0)=0 et y'(0)=8"""
    #Y est un tableau d'array qui sont les approximations
    #de (y,y') aux temps tk=10k/100  (0<=k<=100)
    Y = euler(f_pendule, 0, np.array([0,8]), 2, 100)
    t = np.linspace(0, 2, 101)
    Yarray = np.array(Y)
    plt.plot(t, Yarray[:, 0]) #on extrait la première colonne de Y
    plt.title(u"Résolution (Euler) de  $y''=-\omega_{0}^{2}\sin(y)$ avec \n $y(0)=0$ et $y'(0)=8,0$ sur $[0;2]$, $100$ pas")
    plt.savefig(os.path.join(REPERTOIRE,'exo4-pendule-amorti.png'), dpi=200)
    # plt.show()
    plt.clf() # faire de la place pour une nouvelle figure
    
##    

def exo5():
    """Fonction test de l'exo 5
    Solutions  de y'' = -(omega_0)^2*sin(y) sur [0;2]
    avec y(0)=0 et y'(0)=8
    pour n dans {20,100,1000}"""
    #Y est un tableau d'array qui sont les approximations
    #de (y,y') aux temps tk=10/k  (0<=k<=100)
    methode = [euler, heun, RK4, odeint]
    #couleur = ['red', 'blue', 'green',  'black']
    style = ['--','-.','-','-']
    width = [2, 2, 2, 4]
    etiquette = ['Euler', 'Heun', 'RK4', 'odeint']
    for n in [20, 100, 1000]:
        t = np.linspace(0, 2, n+1)  
        for i in range(4):
            if i < 3:                  
                Y = methode[i](f_pendule, 0, np.array([0,8]), 2, n)
                Yarray = np.array(Y)
                #on extrait la première colonne de Y
                plt.plot(t, Yarray[:, 0], linestyle=style[i],
                                        linewidth=width[i], label=etiquette[i])
            else:
                Y = odeint(f_pendule, np.array([0,8]), t)
                Yarray = np.array(Y)
                #on extrait la première colonne de Y
                plt.plot(t, Yarray[:, 0], linestyle=style[i],
                                        linewidth=width[i], label=etiquette[i])
        plt.title(u"Résolution de  $y''=-\omega_{0}^{2}\sin(y)$ \n avec $y(0)=0$ et $y'(0)=8,0$ sur $[0;2]$, %d pas"%n)
        plt.legend(loc = 'upper left')
        plt.savefig(os.path.join(REPERTOIRE,'exo5-%d-pas.png'%n), dpi=200)
        plt.clf() # faire de la place pour une nouvelle figure
        
##

def exo6():
    """Fonction test de l'exo 6
    Solutions  de y'' = -(omega_0)^2*sin(y) sur [0;6]
    avec y(0)=0 et y'(0)=11.2
    La solution théorique est strictement croissante
    et converge vers pi
    """
    #Y est un tableau d'array qui sont les approximations
    #de (y,y') aux temps tk=10/k  (0<=k<=100)
    methode = [euler, heun, RK4, odeint]
    #couleur = ['red', 'blue', 'green',  'black']
    style = ['--','-.','-','-']
    width = [2, 2, 2, 4]
    n = 1000
    etiquette = ['Euler', 'Heun', 'RK4', 'odeint']
    t = np.linspace(0, 6, 1+n)  
    for i in range(4):
        if i < 3:        
            Y = methode[i](f_pendule, 0, np.array([0,11.2]), 6, n)
        else:
            Y = methode[i](f_pendule, np.array([0,11.2]), t)
        Yarray = np.array(Y) #conversion en array pour le slicing
        #on extrait la première colonne de Y
        plt.plot(t, Yarray[:, 0], linestyle=style[i],
                                linewidth=width[i], label=etiquette[i])
    plt.legend(loc = 'upper left')
    plt.title(u"Résolution de  $y''=-\omega_{0}^{2}\sin(y)$ avec \n $y(0)=0$ et $y'(0)=11.2$ sur $[0;6]$, $1000$ pas")
    plt.savefig(os.path.join(REPERTOIRE,'exo6-pendule-limite.png'), dpi=200)
    plt.clf() # faire de la place pour une nouvelle figure