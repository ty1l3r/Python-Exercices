"""Crée une classe CompteBancaire avec les attributs suivants :

titulaire (chaine de caractères) : le nom du titulaire du compte.
solde (nombre à virgule flottante) : le solde actuel du compte.
Ajoute une méthode __init__ à la classe CompteBancaire qui initialise les attributs titulaire et solde. Le solde doit être initialisé à 0 par défaut.

Ajoute une méthode deposer à la classe CompteBancaire qui prend un montant en paramètre et l'ajoute au solde du compte.

Ajoute une méthode retirer à la classe CompteBancaire qui prend un montant en paramètre et le retranche du solde du compte, à condition que le solde soit suffisant. Si le solde n'est pas suffisant, affiche un message approprié.

Ajoute une méthode afficher_solde à la classe CompteBancaire qui affiche le solde actuel du compte.

Crée une instance de la classe CompteBancaire avec les détails suivants :

Titulaire: "Alice"
Solde initial: 1000.0
Effectue quelques opérations sur le compte, telles que le dépôt, le retrait, et affiche le solde après chaque opération."""

class CompteBancaire:
    def __init__ (self, a, b):
        self.nom = a
        self.solde = b
    def deposer (self, depot):
        self.solde += depot
        return
    def retirer (self, retrait):
        self.solde -= retrait
        return
    def afficher_solde (self):
        return print(self.solde)
    
#instance de la classe CompteBancaire

alice = CompteBancaire("Alice", 1000.0)
alice.afficher_solde()
alice.deposer(500)
alice.afficher_solde()
alice.retirer(500)
alice.afficher_solde()
alice.deposer(1000)
alice.afficher_solde()
