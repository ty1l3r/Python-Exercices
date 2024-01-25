
""" Exercice de Programmation sur l'Héritage en Python

Considère les deux classes suivantes :

La classe Personne avec les attributs :

nom (chaine de caractères) : le nom de la personne.
age (entier) : l'âge de la personne.
La classe Employe qui hérite de la classe Personne et ajoute un attribut supplémentaire :

poste (chaine de caractères) : le poste occupé par l'employé.
Voici les étapes de l'exercice :

Crée la classe Personne avec un constructeur qui initialise les attributs nom et age. Ajoute une méthode afficher_details qui affiche le nom et l'âge de la personne.

Crée la classe Employe qui hérite de Personne. 

Ajoute un constructeur qui appelle explicitement le constructeur de Personne pour initialiser les attributs hérités. 

Ajoute un nouvel attribut poste et une méthode afficher_details dans la classe Employe qui affiche le nom, l'âge et le poste de l'employé.

Crée une instance de la classe Employe avec les détails suivants :

Nom: "Alice"
Âge: 30
Poste: "Ingénieur"
Appelle la méthode afficher_details sur l'instance de la classe Employe pour afficher les détails complets de l'employé. """


class Personne:
    def __init__ (self, nom, age):
        self.nom = nom
        self.age = age
    def afficher_details(self):
        print(self.nom, self.age)
               
class Employe(Personne):
    def __init__ (self, nom, age, poste):
        Personne.__init__(self, nom, age)  
        self.poste = poste     
         
    def aficher_detail1(self):
        print(self.nom, self.age, self.poste)

test1 = Employe("Alice", 30, "ingenieur")
test1.aficher_detail1()