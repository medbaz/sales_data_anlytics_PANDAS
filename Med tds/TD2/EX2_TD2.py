# 1. Créer une liste de matières et l’afficher
matieres = ["Anglais", "Physique", "Maths", "Svt"]
print("1. Liste des matières :", matieres)

# 2. Ajouter "Histoire" et "Geographie" à la liste
matieres.append("Histoire")
matieres.append("Geographie")
print("2. Liste mise à jour avec Histoire et Geographie :", matieres)

# 3a. Afficher les 4 premiers éléments
print("3a. Les 4 premiers éléments :", matieres[:4])

# 3b. Afficher les 3 derniers éléments
print("3b. Les 3 derniers éléments :", matieres[-3:])

# 3c. Afficher 3 éléments depuis le second indice
print("3c. 3 éléments depuis l’indice 2 :", matieres[2:5])
