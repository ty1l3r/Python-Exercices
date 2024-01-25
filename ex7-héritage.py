"""
Considère les deux classes suivantes :

La classe Animal avec un attribut : espece (chaîne de caractères) : l'espèce de l'animal.

La classe Oiseau qui hérite de Animal et ajoute un attribut supplémentaire : envergure (nombre flottant) : la longueur de l'envergure de l'oiseau.

La classe Chat qui hérite également de Animal et ajoute un attribut supplémentaire :couleur (chaîne de caractères) : la couleur du pelage du chat.

Ajoute une méthode afficher_details à la classe Animal qui affiche l'espèce de l'animal.

Surcharge la méthode afficher_details dans les classes Oiseau et Chat pour inclure également l'envergure ou la couleur lors de l'affichage.

Crée une instance de la classe Oiseau avec les détails suivants :

Espèce: "Aigle"
Envergure: 2.5 mètres
Crée une instance de la classe Chat avec les détails suivants :

Espèce: "Chat domestique"
Couleur: "Noir et blanc"

Appelle la méthode afficher_details sur les instances de Oiseau et Chat pour afficher les détails complets de chaque animal.
"""

class Animal:
    def __init__(self, espece):
        self.espece = espece
        
    def afficher_details(self):
        print(self.espece)
      
        
class Oiseau(Animal):
    def __init__(self, espece, envergure):
        Animal.__init__(self, espece)
        self.envergure = envergure
        
    def afficher_details(self):
        Animal.afficher_details(self)
        print(self.envergure)
        
        
class Chat(Animal):
    def __init__(self, espece, couleur):
        Animal.__init__(self, espece)
        self.couleur = couleur
        
    def afficher_details(self):
        Animal.afficher_details(self)
        print(self.couleur)
        


ex1 = Oiseau("Aigle", 2.5)
ex2 = Chat("Chat Domestique", "Noir et blanc")

ex1.afficher_details()
ex2.afficher_details()