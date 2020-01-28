def f1(x, y):
    return (0, 0.16*y)

def f2(x, y):
    return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)

def f3(x, y):
    return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)

def f4(x, y):
    return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)


def exo6():
    (lesx, lesy) = marche_aleatoire(10000)
    plt.axis('equal') #repère orthonormal
    plt.plot(lesx, lesy, 'k,') #affichage sous forme de pixels noirs
    plt.show()
    plt.savefig('marche1000.png')
