# Q1. Créer une liste de matières et l’afficher
matieres = ["Anglais", "Physique", "Maths", "Svt"]
print("1. Liste des matières :", matieres)

# Q2. Ajouter "Histoire" et "Geographie" à la liste
matieres.append("Histoire")
matieres.append("Geographie")
print("2. Liste mise à jour avec Histoire et Geographie :", matieres)

# Afficher les 4 premiers éléments
print("Les 4 premiers éléments :", matieres[:4])

# Afficher les 3 derniers éléments
print("Les 3 derniers éléments :", matieres[-3:])

# Afficher 3 éléments depuis le second indice
print("3 éléments depuis l’indice 2 :", matieres[2:5])
