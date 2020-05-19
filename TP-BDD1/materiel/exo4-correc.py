import sqlite3
base = sqlite3.connect('base_triangles.db')
curseur = base.cursor()
res = curseur.execute("""SELECT * FROM triangles WHERE ab+bc+ac=100""")
foo = res.fetchall()
base.close()
print('res=',res,end='\n\n')
print('foo=',foo,end='\n\n')
print(len(foo),end='\n\n')

"""
res= <sqlite3.Cursor object at 0xb44a09e0>

foo= [(24, 51, 12, 37), ..., (99955, 24, 72, 4)]

474
"""