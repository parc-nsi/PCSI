# -*- coding: utf-8 -*-

import sqlite3


def ecrire_resultat(row, curseur, fichier):
    """Fonction d'écriture des résultats de la requete reponse
    dans le fichier texte de  correction.
    Idée originale de S.Gonnord.
    """
    exo, idbase, question, enonce, reponse, nb  = row
    fichier.write('Exo %s : %s \n\n'%(exo, enonce))
    fichier.write(reponse+'\n\n')
    res = curseur.execute(reponse).fetchall()
    if res != None:
        for ligne in res[ : min(nb, len(res))]:
            l= '('
            if len(ligne)>0:
                l+= str(ligne[0])
            for x in ligne[1:]:
                l+=', '+str(x)
            l+=')\n'
            fichier.write(l)
        if len(res)>nb:
            fichier.write('... (%i de plus)'%(len(res)-nb))
    else:
        fichier.write('Aucun résultat \n')
    #si c'est une insertion ou une suppression de ligne
    #on l'enregistre dans la base
    if 'insert' or 'delete' in reponse.lower():
        dconnexion[dbase[idbase]].commit()
    fichier.write('\n'+'-'*70+'\n\n')


correc_path = 'tp14-corrige.db'

print('Connexion au fichier de base de données des corrigés ', correc_path)

#cree la connexion à la base de données
correc_conn = sqlite3.connect(correc_path)

#cree le curseur pour exécuter les requetes SQL
correc_cursor = correc_conn.cursor()

#dictionnaires pour ranger les objets
#les connexions aux base de données
dconnexion = { 'correc' : correc_conn }
#les curseurs correspondants
dcursor = {'correc' : correc_cursor }
#les descripteurs de fichiers textes pour les corrigés
dcorrige = {}
#recupération des noms des fichiers de bases de données
correc_cursor.execute("SELECT * FROM base")
res = correc_cursor.fetchall()
#stockage de ces noms dans un dictionnaire
#pour simplifier on suppose que toutes les ressources
#sont dans le répertoire courant
dbase = {r[0] : r[1] for r in res}

#variables pour mémoriser la base et l'exo courant
base, exo = '', 0

correc_cursor.execute("SELECT * FROM requete ORDER BY exo, question ASC")
for row in correc_cursor.fetchall():
    if row[0] != exo:
        exo = row[0]
        if exo not in dcorrige:
            dcorrige[exo] = open('TP14-correc-'+str(exo)+'.txt', 'w')
    if dbase[row[1]] != base:
        base = dbase[row[1]]
        if base not in dconnexion:
            #cree la connexion à la base de données de l'exo
            dconnexion[base] = sqlite3.connect(base)
            #cree le curseur correspondant
            dcursor[base]  = dconnexion[base].cursor()
    ecrire_resultat(row, dcursor[base], dcorrige[exo])

#fermeture des curseurs
for clef in dcursor:
    dcursor[clef].close()

#fermeture des connexions aux base de donnees
for clef in dconnexion:
    dconnexion[clef].close()

#femeture des fichiers textes
for clef in dcorrige:
    dcorrige[clef].close()
         
