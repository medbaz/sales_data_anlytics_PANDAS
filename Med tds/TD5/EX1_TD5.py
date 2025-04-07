import numpy as np

# 1. Création des tableaux

# Tableau 1D de 0 à 9
tableau_1D = np.arange(10)
print("Tableau 1D :", tableau_1D)

# Tableau 2D (3x3) avec des nombres aléatoires entre 0 et 1
tableau_2D = np.random.rand(3, 3)
print("\nTableau 2D :\n", tableau_2D)

# Tableau 3D (2x3x4) rempli de zéros
tableau_3D = np.zeros((2, 3, 4))
print("\nTableau 3D :\n", tableau_3D)

# 2. Accès et modification des éléments

# Troisième élément du tableau 1D (index 2 car les indices commencent à 0)
print("\nTroisième élément du tableau 1D :", tableau_1D[2])

# Deuxième ligne (index 1), première colonne (index 0) du tableau 2D
print("Élément [1][0] du tableau 2D :", tableau_2D[1, 0])

# Modification d'un élément du tableau 3D
tableau_3D[0, 1, 2] = 7
print("\nTableau 3D après modification :\n", tableau_3D)
