# Python-Class-Exercice

Exercices pour bien débuter avec PYTHON. Ces exercices peuvent être utiles à tous.

Les intitulés sont présents dans le README et les réponses dans les fichiers py correspondants.

Mes réponses ne sont pas forcément bien commentées pour le moment. Libre à vous d'en ajouter, de proposer des solutions alternatives, voire même de nouveaux exercices !

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Exercice 1 : 
Crée une classe Point qui a deux attributs, x et y, représentant les coordonnées d'un point dans l'espace. 
Ajoute une méthode distance qui calcule la distance euclidienne entre deux points.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Exercice 2 : 
Crée une classe Animal avec les attributs suivants :

nom (chaine de caractères) : le nom de l'animal.
age (entier) : l'âge de l'animal.
espece (chaine de caractères) : l'espèce à laquelle appartient l'animal.
Ajoute une méthode afficher_details à la classe Animal qui affiche les détails de l'animal, y compris son nom, son âge, et son espèce.
Crée une instance de la classe Animal avec les détails suivants :
Nom: "Léo"
Âge: 3
Espèce: "Lion"
Appelez la méthode afficher_details pour afficher les détails de l'animal.
Ajoute une nouvelle méthode anniversaire à la classe Animal qui augmente l'âge de l'animal d'un an à chaque appel.
Appelez la méthode anniversaire deux fois, puis appelez à nouveau afficher_details pour voir l'âge mis à jour de l'animal. """

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercice 3 

Crée une classe CompteBancaire avec les attributs suivants :
titulaire (chaine de caractères) : le nom du titulaire du compte.
solde (nombre à virgule flottante) : le solde actuel du compte.
Ajoute une méthode __init__ à la classe CompteBancaire qui initialise les attributs titulaire et solde. Le solde doit être initialisé à 0 par défaut.
Ajoute une méthode deposer à la classe CompteBancaire qui prend un montant en paramètre et l'ajoute au solde du compte.
Ajoute une méthode retirer à la classe CompteBancaire qui prend un montant en paramètre et le retranche du solde du compte, à condition que le solde soit suffisant. Si le solde n'est pas suffisant, affiche un message approprié.
Ajoute une méthode afficher_solde à la classe CompteBancaire qui affiche le solde actuel du compte.
Crée une instance de la classe CompteBancaire avec les détails suivants :
Titulaire: "Alice"
Solde initial: 1000.0
Effectue quelques opérations sur le compte, telles que le dépôt, le retrait, et affiche le solde après chaque opération.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Exercice 4 :

Crée une classe de base Vehicule avec les attributs suivants :

marque (chaine de caractères) : la marque du véhicule.
modele (chaine de caractères) : le modèle du véhicule.
annee (entier) : l'année de fabrication du véhicule.
Ajoute une méthode afficher_details à la classe Vehicule qui affiche les détails du véhicule, y compris la marque, le modèle et l'année.

Crée une classe dérivée Voiture qui hérite de la classe Vehicule. Ajoute un attribut spécifique à la classe Voiture :

nombre_portes (entier) : le nombre de portes de la voiture.
Surcharge la méthode afficher_details dans la classe Voiture pour inclure également le nombre de portes.

Crée une instance de la classe Voiture avec les détails suivants :

Marque: "Toyota"
Modèle: "Corolla"
Année: 2022
Nombre de portes: 4
Appelle la méthode afficher_details sur l'instance de la classe Voiture pour afficher les détails complets de la voiture.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Exercice 5 : 

Considère les deux classes suivantes :
La classe Personne avec les attributs :
nom (chaine de caractères) : le nom de la personne.
age (entier) : l'âge de la personne.
La classe Employe qui hérite de la classe Personne et ajoute un attribut supplémentaire :
poste (chaine de caractères) : le poste occupé par l'employé.
Voici les étapes de l'exercice :
Crée la classe Personne avec un constructeur qui initialise les attributs nom et age. Ajoute une méthode afficher_details qui affiche le nom et l'âge de la personne.
Crée la classe Employe qui hérite de Personne. Ajoute un constructeur qui appelle explicitement le constructeur de Personne pour initialiser les attributs hérités. Ajoute un nouvel attribut poste et une méthode afficher_details dans la classe Employe qui affiche le nom, l'âge et le poste de l'employé.
Crée une instance de la classe Employe avec les détails suivants :
Nom: "Alice"
Âge: 30
Poste: "Ingénieur"
Appelle la méthode afficher_details sur l'instance de la classe Employe pour afficher les détails complets de l'employé.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercice 6 :

Considère les deux classes suivantes :

La classe Forme avec un attribut :
couleur (chaîne de caractères) : la couleur de la forme.

La classe Cercle qui hérite de Forme et ajoute un attribut supplémentaire :
rayon (nombre flottant) : le rayon du cercle.

La classe Carre qui hérite également de Forme et ajoute un attribut supplémentaire :
cote (nombre flottant) : la longueur du côté du carré.

Ajoute une méthode afficher_details à la classe Forme qui affiche la couleur de la forme.

Surcharge la méthode afficher_details dans les classes Cercle et Carre pour inclure également le rayon/côté respectif lors de l'affichage.

Crée une instance de la classe Cercle avec les détails suivants :

Couleur: "Rouge"
Rayon: 5.0
Crée une instance de la classe Carre avec les détails suivants :

Couleur: "Bleu"
Côté: 4.0
Appelle la méthode afficher_details sur les instances de Cercle et Carre pour afficher les détails complets de chaque forme.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercice 7

Considère les deux classes suivantes :

La classe Animal avec un attribut :
espece (chaîne de caractères) : l'espèce de l'animal.

La classe Oiseau qui hérite de Animal et ajoute un attribut supplémentaire :
envergure (nombre flottant) : la longueur de l'envergure de l'oiseau.

La classe Chat qui hérite également de Animal et ajoute un attribut supplémentaire :
couleur (chaîne de caractères) : la couleur du pelage du chat.

Ajoute une méthode afficher_details à la classe Animal qui affiche l'espèce de l'animal.

Surcharge la méthode afficher_details dans les classes Oiseau et Chat pour inclure également l'envergure ou la couleur lors de l'affichage.

Crée une instance de la classe Oiseau avec les détails suivants :

Espèce: "Aigle"
Envergure: 2.5 mètres
Crée une instance de la classe Chat avec les détails suivants :

Espèce: "Chat domestique"
Couleur: "Noir et blanc"

Appelle la méthode afficher_details sur les instances de Oiseau et Chat pour afficher les détails complets de chaque animal.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercice 8 

**Exercice sur la gestion d'une vidéothèque :**

1. Crée une classe `Film` avec les attributs suivants :
   - `titre` (chaîne de caractères) : le titre du film.
   - `realisateur` (chaîne de caractères) : le réalisateur du film.
   - `annee_sortie` (entier) : l'année de sortie du film.
   - `genre` (chaîne de caractères) : le genre du film.
   - `duree` (entier) : la durée du film en minutes.
   - `disponible` (booléen) : indique si le film est disponible (True) ou emprunté (False).

2. Ajoute une méthode `afficher_details` à la classe `Film` qui affiche les détails du film (titre, réalisateur, année de sortie, genre, durée et disponibilité).

3. Crée une classe `Videoclub` qui contiendra un attribut :
   - `liste_films` (liste d'instances de type `Film`) : la liste des films dans le vidéoclub.

4. Définis dans la classe `Videoclub` une méthode `ajouter_film` qui ajoutera un objet de type `Film` à la liste des films du vidéoclub.

5. Crée une instance de la classe `Film` avec les détails suivants :
   - Titre: "Inception"
   - Réalisateur: "Christopher Nolan"
   - Année de sortie: 2010
   - Genre: "Science-fiction"
   - Durée: 148 minutes
   - Disponible: True

6. Crée une instance de la classe `Film` avec les détails suivants :
   - Titre: "La La Land"
   - Réalisateur: "Damien Chazelle"
   - Année de sortie: 2016
   - Genre: "Comédie musicale"
   - Durée: 128 minutes
   - Disponible: False

7. Ajoute ces deux films à la liste des films dans une instance de la classe `Videoclub`.

8. Affiche les détails de tous les films dans le vidéoclub à l'aide de la méthode `afficher_details`.
