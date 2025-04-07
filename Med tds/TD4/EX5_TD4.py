# 1. Définir la classe Etudiant avec les attributs nom, âge et note
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    # 2. Implémenter la méthode afficher_info() pour afficher les informations de l'étudiant
    def afficher_info(self):
        print(f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}")
    
    # 3. Méthode statique pour calculer la moyenne des notes
    @staticmethod
    def calculer_moyenne(etudiants):
        if len(etudiants) == 0:
            return 0
        total_notes = sum(etudiant.note for etudiant in etudiants)
        return total_notes / len(etudiants)

# Création d'objets Etudiant
etudiant2 = Etudiant("Zakaria", 22, 12)
etudiant1 = Etudiant("Hamza", 20, 15)
etudiant3 = Etudiant("Mohamed", 21, 18)

# Afficher les informations des étudiants
etudiant1.afficher_info()
etudiant2.afficher_info()
etudiant3.afficher_info()

# Liste d'étudiants
etudiants = [etudiant1, etudiant2, etudiant3]

# Calculer la moyenne des notes
moyenne = Etudiant.calculer_moyenne(etudiants)
print(f"\nLa moyenne des notes est : {moyenne:.2f}")
