/*
TP15 BDD3
Franz Ridde/Pierre Duclosson
*/

/*
Base de donnees
cinema.bdd
tirée du livre de Laurent Audibert
TP p 122
*/

/*
Q1
Quels sont les prénoms des personnes ? 
*/

SELECT prenom FROM personne;

/*
Requête OK
Ligne(s) retournée(s): 22 
SELECT prenom FROM personne;
*/

/*Q1
Les prénoms sans doublon ? 
*/
SELECT DISTINCT prenom FROM personne;

/*
Requête OK
Ligne(s) retournée(s): 19 
SELECT DISTINCT prenom FROM personne;
*/

/*
Q2
Quel est le nom des personnes dont le prénom est John ?
*/

SELECT nom FROM personne WHERE prenom = 'John';

/*
Requête OK
Ligne(s) retournée(s): 3 
SELECT nom FROM personne WHERE prenom = 'John';
*/


/*Q3
Quels sont les titres des films réalisés dans les années 90 ?
*/
SELECT titre FROM film where annee BETWEEN 1990 AND 1999;

/*
Requête OK
Ligne(s) retournée(s): 5 
SELECT titre FROM film where annee BETWEEN 1990 AND 1999;
*/

/*
Q4
Quelles sont les personnes qui sont des acteurs ?
*/

SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN jouer
 ON idp = ida;

/*
Requête OK
Ligne(s) retournée(s): 14 
SELECT DISTINCT idp, nom, prenom FROM Personne JOIN Jouer ON idp = ida;
*/

/*
Q5
Quelles sont les personnes qui sont des réalisateurs ?
*/

SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN film
 ON idp = idr;

/*
Requête OK
Ligne(s) retournée(s): 7 
SELECT DISTINCT idp, nom, prenom FROM personne JOIN film ON idp = idr;
*/

/*
Q6
Qui est à la fois acteur et réalisateur ?

2 possibilités :

*/

SELECT DISTINCT idp, nom, prenom FROM
  (personne JOIN film ON idp = idr  )
JOIN jouer ON idp = ida;

/*
Requête OK
Ligne(s) retournée(s): 1 
SELECT DISTINCT idp, nom, prenom FROM
  (personne JOIN film ON idp = idr  )
JOIN jouer ON idp = ida;
*/

SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN jouer
 ON idp = ida
 INTERSECT
 SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN film
 ON idp = idr;
 
 /*
 Requête OK
Ligne(s) retournée(s): 1 

SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN jouer
 ON idp = ida
 INTERSECT
 SELECT DISTINCT idp, nom, prenom FROM
 personne JOIN film
 ON idp = idr;
 */

 
 /*Q7
 Dresser la liste de toutes les interprétations possibles, 
 en précisant le nom et le prénom de l'acteur ainsi que 
 le rôle et le titre du film. La liste sera triée par ordre alphabétique du nom.
 */
 
SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
ORDER BY nom ASC;

/*
Requête OK
Ligne(s) retournée(s): 16 
 SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
ORDER BY nom ASC;
*/

/*Q8

 Quels sont les titres des films où Kevin Spacey a joué un rôle ?
 
 */
 
SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
WHERE nom = 'Spacey' AND prenom = 'Kevin';

/*
Requête OK
Ligne(s) retournée(s): 2 
SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
WHERE nom = 'Spacey' AND prenom = 'Kevin';
*/

SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
WHERE prenom || ' ' || nom = 'Kevin Spacey';


/*
Requête OK
Ligne(s) retournée(s): 2 
SELECT nom, prenom, role, titre FROM
 (personne JOIN jouer ON idp = ida  )
JOIN film ON jouer.idf = film.idf
WHERE nom = 'Spacey' AND prenom = 'Kevin';
*/

/*Q9
Quels sont les drames que l'on a pu voir après le 1er janvier 2000 ?
*/

SELECT titre, jour FROM 
film JOIN projection ON film.idf = projection.idf
WHERE film.genre = 'Drame' AND projection.jour >= '2000-01-01';

/*Q9
Requête OK
Ligne(s) retournée(s): 5 

SELECT titre, jour FROM 
film JOIN projection ON film.idf = projection.idf
WHERE film.genre = 'Drame' AND projection.jour >= '2000-01-01';
*/

/*Q10
Dresser la liste des acteurs (nom et prénom) en précisant le nombre 
de films dans lesquels ils ont joué. Le résultat doit être trié par 
ordre alphabétique des noms.
*/

SELECT  idp, nom, prenom, COUNT(*)  AS nbfilms FROM
 personne JOIN jouer  ON personne.idp = jouer.ida
 GROUP BY ida
 ORDER BY nom;
 
 /*
 Requête OK
Ligne(s) retournée(s): 14 
SELECT DISTINCT idp, nom, prenom, COUNT(*)  AS nbfilms FROM
 personne JOIN jouer
 ON personne.idp = jouer.ida
 GROUP BY personne.ida
 O;
 */

 /*Q11
 Quels sont les acteurs ayant joué dans des drames ?

 */
 
 SELECT  idp, nom, prenom FROM
 personne JOIN jouer  ON personne.idp = jouer.ida
 JOIN film ON jouer.idf = film.idf
 WHERE film.genre = 'Drame'
 GROUP BY ida ;
 
 /*
 Requête OK
Ligne(s) retournée(s): 9 
 SELECT  idp, nom, prenom FROM
 personne JOIN jouer  ON personne.idp = jouer.ida
 JOIN film ON jouer.idf = film.idf
 WHERE film.genre = 'Drame'
 GROUP BY ida ;
 */
 
 /*Q12
 Quels sont les titres des films où Kevin Spacey a joué un rôle 
 et qui ont été projetés au cinéma UGC ?
 */
 
SELECT film.titre, personne.nom, prenom,projection.jour FROM 
 personne JOIN jouer  ON personne.idp = jouer.ida
 JOIN film ON film.idf = jouer.idf
 JOIN projection ON projection.idf = jouer.idf
 JOIN cinema ON cinema.idc = projection.idc
 WHERE personne.nom = 'Spacey' AND personne.prenom = 'Kevin' AND cinema.nom = 'UGC';

/*Q13
Combien de films  ont été projetés à l'UGC ?
*/

SELECT COUNT(DISTINCT projection.idf) FROM 
projection JOIN cinema ON projection.idc = cinema.idc
GROUP BY cinema.nom
HAVING cinema.nom = 'UGC';


/*Q13 bis
Combien de films  différents ont été projetés à l'UGC ?
*/

SELECT COUNT(*) FROM
(
SELECT DISTINCT projection.idf FROM
cinema JOIN projection
On cinema.idc = projection.idc
WHERE cinema.nom = 'UGC'
);

/*Q14
calculer le nombre de films réalisés par Lars von Trier
*/

SELECT COUNT(*) FROM 
personne JOIN film ON personne.idp = film.idr
WHERE personne.prenom = 'Lars' AND personne.nom = 'von Trier';


/*Quels sont les acteurs ayant joué dans tous les films de Lars von Trier ?
*/

SELECT personne.prenom, personne.nom FROM
personne JOIN jouer ON personne.idp = jouer.ida
JOIN film ON film.idf = jouer.idf
WHERE film.idr = (
SELECT idp FROM Personne 
WHERE personne.prenom = 'Lars' AND personne.nom = 'von Trier'
)
GROUP BY personne.prenom, personne.nom
HAVING COUNT(*) = (
SELECT COUNT(*) FROM 
personne JOIN film ON personne.idp = film.idr
WHERE personne.prenom = 'Lars' AND personne.nom = 'von Trier'
);

SELECT personne.nom FROM
(
  SELECT film.idf AS i FROM
  personne JOIN film
  ON personne.idp = film.idr
  WHERE personne.nom = 'von Trier'
)
JOIN jouer 
ON jouer.idf = i
JOIN personne
ON personne.idp = jouer.ida
GROUP BY personne.idp
HAVING COUNT(*) = 
(
  SELECT COUNT(*) FROM
  film JOIN personne
  ON film.idr = personne.idp
  WHERE personne.nom = 'von Trier'
    AND personne.prenom = 'Lars'
)
