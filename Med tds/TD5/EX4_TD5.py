import numpy as np

# 1. Créer un tableau aléatoire (5x5)
tableau = np.random.rand(5, 5)
print("Tableau aléatoire (5x5) :\n", tableau)

# Moyenne par ligne et par colonne
moyenne_lignes = np.mean(tableau, axis=1)
moyenne_colonnes = np.mean(tableau, axis=0)

# Écart-type par ligne et par colonne
ecart_type_lignes = np.std(tableau, axis=1)
ecart_type_colonnes = np.std(tableau, axis=0)

# Minimum et maximum par ligne et par colonne
min_lignes = np.min(tableau, axis=1)
max_lignes = np.max(tableau, axis=1)
min_colonnes = np.min(tableau, axis=0)
max_colonnes = np.max(tableau, axis=0)

print("\nMoyenne par ligne :", moyenne_lignes)
print("Moyenne par colonne :", moyenne_colonnes)
print("Écart-type par ligne :", ecart_type_lignes)
print("Écart-type par colonne :", ecart_type_colonnes)
print("Minimum par ligne :", min_lignes)
print("Maximum par ligne :", max_lignes)
print("Minimum par colonne :", min_colonnes)
print("Maximum par colonne :", max_colonnes)

# 2. Trier un tableau aléatoire et trouver l'indice du max
tableau_aleatoire = np.random.rand(10)
print("\nTableau aléatoire 1D :", tableau_aleatoire)

# Tri croissant
tableau_trie = np.sort(tableau_aleatoire)
print("Tableau trié :", tableau_trie)

# Indice de l'élément maximum dans le tableau d'origine
indice_max = np.argmax(tableau_aleatoire)
print("Indice de l'élément max dans le tableau original :", indice_max)

# 3. Broadcasting : multiplication tableau 1D (4) avec tableau 2D (3x4)
vecteur = np.array([1, 2, 3, 4])
matrice = np.random.randint(1, 5, (3, 4))

print("\nTableau 1D :", vecteur)
print("Tableau 2D (3x4) :\n", matrice)

# Multiplication par broadcasting
resultat = matrice * vecteur
print("Résultat de la multiplication (broadcasting) :\n", resultat)
