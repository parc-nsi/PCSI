# -*- coding: utf-8 -*-
from random import randint
import sqlite3


com = sqlite3.connect('base_triangles.db')
curseur = com.cursor()

curseur.execute("""DROP TABLE IF EXISTS triangles""")
curseur.execute("""CREATE TABLE triangles
                    (idt integer,
                     ab integer,
                     bc integer,
                     ac integer)""")

nb = 100000

for i in range(nb):
    if i % (nb//42) == 0:
        a = randint(10, 20)
        b = randint(1, a-1)
        ab, ac, bc = a**2-b**2, 2*a*b, a**2+b**2
    else:
        ab, bc, ac = randint(1, 100), randint(1, 100), randint(1, 100)
        while ab > bc + ac or ac > ab + bc or bc > ab + ac :
            ab, bc, ac = randint(1, 100), randint(1, 100), randint(1, 100)
    curseur.execute("""INSERT INTO triangles VALUES """+str((i, ab, bc, ac)))


com.commit()
com.close()