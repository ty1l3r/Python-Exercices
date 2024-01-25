"""
. Crée une classe `Film` avec les attributs suivants :
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
"""

class Film:
    def __init__(self, titre, realisateur, annee_sortie, genre, duree, disponible):
        self.titre = titre
        self.realisateur = realisateur
        self.annee_sortie = annee_sortie
        self.genre = genre
        self.duree = duree
        self.disponible = disponible

    def afficher_details(self):
        print(self.titre + " - " + self.realisateur + " - " + str(self.annee_sortie) + " - " + self.genre + " - " + str(self.duree) + " - Disponible: " + str(self.disponible))


class Videoclub:
    def __init__(self):
        self.liste_films = []

    def add(self, film):
        self.liste_films.append(film)

    def afficher_details(self):
        for film in self.liste_films:
            film.afficher_details()


# Exemple d'utilisation
ex1 = Film("Inception", "Noal", 2010, "Science-Fiction", "148 minutes", True)
ex2 = Film("La La Land", "Chazelle", 2016, "Comédie Musicale", "128 minutes", False)

videoclub = Videoclub()
videoclub.add(ex1)
videoclub.add(ex2)

videoclub.afficher_details()
