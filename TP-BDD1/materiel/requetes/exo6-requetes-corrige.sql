/* ******************  Exo 6  ********************************* */

/* 1)  Quels sont les titres des films réalisés par Lars von Trier ? */

SELECT film.titre FROM film 
	JOIN personne
		ON personne.idp = film.idr
			WHERE personne.nom = 'von Trier' AND personne.prenom = 'Lars'
 
/* 2)  Quels sont les titres des films où Kevin Spacey a joué ?  */

SELECT film.titre FROM personne 
	JOIN jouer ON personne.idp = jouer.ida 
		JOIN film ON jouer.idf = film.idf
		WHERE personne.prenom = 'Kevin' AND personne.nom = 'Spacey'

 
/* 3)  Quels sont les drames que l'on a pu voir après le 1er janvier 2002 ? */

SELECT film.titre, film.genre, projection.jour
	FROM film JOIN projection
		ON film.idf = projection.idf
			WHERE film.genre = 'Drame'
				AND projection.jour >= '2002-01-01'
 
/* 4) Quels sont les noms et prénoms des personnes  qui sont des acteurs ?
Ordonner la liste par ordre alphabétique croissant des noms. */

SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN jouer
		ON personne.idp = jouer.ida		
			ORDER BY personne.nom
 
/*  5) Quels sont les noms et prénoms des personnes qui sont des réalisateurs ?
 */
 
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr			
 

/* 6) Quels sont les noms et prénoms des personnes qui sont à la fois des acteurs
 et des réalisateurs 
 Faire l'intersection des  tables générées par les deux requetes précédentes
 à l'aide du mot clef INTERSECT */
 
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN jouer
		ON personne.idp = jouer.ida		
INTERSECT
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr

 /* 7)  Quels sont les noms et prénoms des acteurs  qui ne sont pas des 
réalisateurs ?  
 Faire  la différence entre deux tables  à l'aide du mot clef EXCEPT */

SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN jouer
		ON personne.idp = jouer.ida		
EXCEPT
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr

 
 
/* 8) Quels sont les noms et prénoms des réalisateurs qui ont réalisé des films 
policier ? */

SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr
			WHERE genre = 'Policier'
  
/* 9) Quels sont les noms et prénoms des réalisateurs qui ont réalisé des 
films policier et des films dramatiques ? */

SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr
			WHERE genre = 'Policier'
INTERSECT
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN film
		ON personne.idp = film.idr
			WHERE genre = 'Drame'

  
/* 10) Quelle est  la liste de toutes les interprétations possibles en précisant
le nom et le prénom de l'acteur ainsi que le role et le titre du film ?
 La liste doit etre classée dans l'ordre alphabétique décroissant des noms. */
 
SELECT personne.nom, personne.prenom, film.titre, jouer.role
	FROM personne JOIN jouer ON personne.idp = jouer.ida
		JOIN film ON jouer.idf = film.idf
			ORDER BY personne.nom DESC
 
/* 11)  Quels sont les titres des films réalisés par David Cronenberg 
qui ont été projetés au cinéma UGC ? */

SELECT film.titre, personne.nom, personne.prenom, cinema.nom, projection.jour
	FROM personne JOIN film ON personne.idp = film.idr
			JOIN projection ON film.idf = projection.idf
				JOIN cinema ON projection.idc = cinema.idc
					WHERE personne.nom = 'Cronenberg'
						AND personne.prenom = 'David'
							AND cinema.nom = 'UGC'

/* 12) Quels sont les acteurs qui ont joué dans des films projetés au cinéma UGC
 depuis l'an 2000 ? */
 
SELECT DISTINCT personne.nom, personne.prenom
	FROM personne JOIN jouer ON personne.idp = jouer.ida 
		JOIN projection ON jouer.idf = projection.idf
			JOIN cinema ON projection.idc = cinema.idc
				WHERE cinema.nom = 'UGC'
					AND projection.jour >= '2000-01-01'
						ORDER BY personne.nom
 
 
/*  13) Quels sont les titres des films où Stellan Skarsgard a joué un role et  
qui ont été projetés au cinéma UGC ? */

SELECT DISTINCT film.titre, personne.nom, personne.prenom
	FROM personne JOIN jouer ON personne.idp = jouer.ida
		JOIN film ON jouer.idf = film.idf
			JOIN projection ON jouer.idf = projection.idf
				JOIN cinema ON projection.idc = cinema.idc 
					WHERE personne.nom = 'Skarsgard'
						AND personne.prenom = 'Stellan'
							AND cinema.nom = 'UGC'
								ORDER BY film.titre
