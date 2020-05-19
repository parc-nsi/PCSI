/* Ceci est un commentaire */
SELECT * FROM personne

SELECT prenom FROM personne ORDER BY prenom ASC

SELECT DISTINCT prenom FROM personne

SELECT * FROM personne 
	WHERE prenom = 'John'

SELECT idp FROM personne 
	WHERE nom = 'von Trier' AND prenom = 'Lars'

SELECT titre FROM film 
	WHERE idr = (SELECT idp FROM personne 
		WHERE personne.nom = 'von Trier'
			AND personne.prenom = 'Lars')

SELECT *FROM personne, film

SELECT film.titre FROM personne, film 
	WHERE personne.idp = film.idr 
		AND personne.nom = 'von Trier' 
			AND personne.prenom = 'Lars'