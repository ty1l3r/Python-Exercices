""" Exercice de Programmation sur les Classes en Python

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

class Animal:
    def __init__(self, a, b, c):
        self.nom = a
        self.age = b
        self.espece = c
    def afficher_details (self):
        return self.nom, self.age, self.espece
    def anniversaire (self):
        self.age += 1 
        return 
        
ex1 = Animal("Léo", 3, "Lion")
print(ex1.afficher_details())
ex1.anniversaire()
ex1.anniversaire()
print(ex1.afficher_details())