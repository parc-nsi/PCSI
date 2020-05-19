/* *************Exo 2 Question2 ********************************* */

/* Toutes les lignes avec toutes les colonnes de la table personne*/
SELECT * FROM personne

/*Tous les prenoms de la table personne dans l'ordre croissant des 
prenoms*/
SELECT prenom FROM personne ORDER BY prenom ASC

/*Tous les prenoms de la table personne avec supression des doublons
Donne le meme resultat que
SELECT DISTINCT prenom FROM personne ORDER BY prenom ASC */
SELECT DISTINCT prenom FROM personne

/*Toutes les lignes de la table personne qui contiennent le prenom 'John'*/
SELECT * FROM personne WHERE prenom = 'John'

/*Récupère l'idp de Lars von Trier*/
SELECT idp FROM personne 
	WHERE nom = 'von Trier' AND prenom = 'Lars'

/*Liste des titres de films réalisés par Lars von Trier*/
SELECT titre FROM film 
	WHERE idr = (SELECT idp FROM personne 
		WHERE personne.nom = 'von Trier'
			AND personne.prenom = 'Lars')
			
/* *************Exo 2 Question3 ********************************* */
			
/* Question 3 a) 
Déterminer les titres de films dont le genre est Drame */

SELECT titre FROM film WHERE genre = 'Drame'

/* Question 3 b) 
 Déterminer les titres des films réalisés dans les années 80 */
 
SELECT titre FROM film
	WHERE annee BETWEEN 1980 AND 1990

SELECT titre FROM film
	WHERE  1980 <= annee AND annee <= 1990
  	
/* Question 3 c) 
Déterminer le nombre de projections de films */

SELECT COUNT(*) FROM projection

/* Question 3 d) 
Déterminer les titres de films dont le genre est Drame
et qui ont été réalisés dans les années 2000*/

SELECT titre FROM film 
	WHERE genre = 'Drame'
		AND annee >= 2000 AND annee <= 2010
		
/* Question 3 e) 
Déterminer les r\^oles joués par Kevin Spacey.*/

SELECT role FROM jouer
	WHERE ida = (SELECT idp FROM personne
			WHERE nom = 'Spacey' AND prenom = 'Kevin')
  	
