""" Crée une classe de base Vehicule avec les attributs suivants :

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
Appelle la méthode afficher_details sur l'instance de la classe Voiture pour afficher les détails complets de la voiture. """

class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_details(self):
        print(f"Vehicule: {self.marque} {self.modele}, Année: {self.annee}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nombre_portes):
        # Appel du constructeur de la classe parente
        Vehicule.__init__(self, marque, modele, annee)
        # Ajout de l'attribut spécifique à la classe Voiture
        self.nombre_portes = nombre_portes
    
    # Surcharge de la méthode afficher_details
    def afficher_details(self):
        # Appel de la méthode afficher_details de la classe parente
        Vehicule.afficher_details(self)
        print(f"Nombre de portes: {self.nombre_portes}")

# Création d'une instance de la classe Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2022, 4)

# Appel de la méthode afficher_details de la classe Voiture (surcharge)
ma_voiture.afficher_details()

