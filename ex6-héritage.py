""" Considère les deux classes suivantes :

La classe Forme avec un attribut :
couleur (chaîne de caractères) : la couleur de la forme.

La classe Cercle qui hérite de Forme et ajoute un attribut supplémentaire :
rayon (nombre flottant) : le rayon du cercle.

La classe Carre qui hérite également de Forme et ajoute un attribut supplémentaire :
cote (nombre flottant) : la longueur du côté du carré.

Ajoute une méthode afficher_details à la classe Forme qui affiche la couleur de la forme.

----> Surcharge la méthode afficher_details dans les classes Cercle et Carre pour inclure également le rayon/côté respectif lors de l'affichage.

Crée une instance de la classe Cercle avec les détails suivants :
Couleur: "Rouge"
Rayon: 5.0

Crée une instance de la classe Carre avec les détails suivants :
Couleur: "Bleu"
Côté: 4.0

Appelle la méthode afficher_details sur les instances de Cercle et Carre pour afficher les détails complets de chaque forme. """

class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def afficher_details(self):
        print("Forme - Couleur:", self.couleur)


class Cercle(Forme):
    def __init__(self, couleur, rayon):
        # Appel du constructeur de la classe parente
        Forme.__init__(self, couleur)
        self.rayon = rayon

    def afficher_details(self):
        # Surcharge de la méthode afficher_details de la classe parente
        Forme.afficher_details(self)
        print("Cercle - Rayon:", self.rayon)


class Carre(Forme):
    def __init__(self, couleur, cote):
        # Appel du constructeur de la classe parente
        Forme.__init__(self, couleur)
        self.cote = cote

    def afficher_details(self):
        # Surcharge de la méthode afficher_details de la classe parente
        Forme.afficher_details(self)
        print("Carre - Cote:", self.cote)


# Création d'instances
ex1 = Cercle("Rouge", 5)
ex2 = Carre("Bleu", 4.0)

# Appel des méthodes
ex1.afficher_details()
ex2.afficher_details()
