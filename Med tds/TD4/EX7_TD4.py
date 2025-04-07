# Définition de la classe Livre
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.statut = "disponible"  # Le livre est disponible par défaut

    def __str__(self):
        return f"{self.titre} de {self.auteur} - Statut: {self.statut}"

# Définition de la classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste des livres dans la bibliothèque

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.statut == "disponible":
                livre.statut = "emprunté"
                print(f"Le livre '{titre}' a été emprunté.")
                return
        print(f"Le livre '{titre}' est soit introuvable, soit déjà emprunté.")

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.statut == "emprunté":
                livre.statut = "disponible"
                print(f"Le livre '{titre}' a été rendu.")
                return
        print(f"Le livre '{titre}' n'est pas emprunté ou introuvable.")

    def lister_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.statut == "disponible"]
        if livres_disponibles:
            print("Livres disponibles :")
            for livre in livres_disponibles:
                print(f"- {livre}")
        else:
            print("Aucun livre disponible.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de livres
    livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre2 = Livre("1984", "George Orwell")
    livre3 = Livre("Les Misérables", "Victor Hugo")
    
    # Création de la bibliothèque
    bibliotheque = Bibliotheque()
    
    # Ajouter des livres à la bibliothèque
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.ajouter_livre(livre3)
    
    # Lister les livres disponibles
    bibliotheque.lister_livres_disponibles()
    
    # Emprunter un livre
    bibliotheque.emprunter_livre("1984")
    
    # Lister les livres disponibles après emprunt
    bibliotheque.lister_livres_disponibles()
    
    # Rendre un livre
    bibliotheque.rendre_livre("1984")
    
    # Lister les livres disponibles après retour
    bibliotheque.lister_livres_disponibles()
