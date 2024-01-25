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