import numpy as np

# 1. Création d'un tableau 1D de 12 éléments
tableau = np.arange(12)
print("Tableau 1D :", tableau)

# Transformation en tableau 2D de dimensions (3, 4)
tableau_2D = tableau.reshape(3, 4)
print("\nTableau 2D (3x4) :\n", tableau_2D)

# Transformation en tableau 3D de dimensions (2, 2, 3)
tableau_3D = tableau.reshape(2, 2, 3)
print("\nTableau 3D (2x2x3) :\n", tableau_3D)

# 2. Transposer le tableau 2D (3x4 devient 4x3)
transpose = tableau_2D.T
print("\nTransposé du tableau 2D :\n", transpose)

# Utilisation de swapaxes
swap = np.swapaxes(tableau_2D, 0, 1)
print("\nSwapaxes (0 <-> 1) sur le tableau 2D :\n", swap)

# 3. Création de deux tableaux 2D (2x3)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("\nTableau a :\n", a)
print("Tableau b :\n", b)

# Concaténation verticale (résultat : 4x3)
concat_vert = np.vstack((a, b))
print("\nConcaténation verticale :\n", concat_vert)

# Concaténation horizontale (résultat : 2x6)
concat_horiz = np.hstack((a, b))
print("\nConcaténation horizontale :\n", concat_horiz)

# Découpage du tableau concaténé verticalement en deux tableaux (2 lignes chacun)
subarrays = np.vsplit(concat_vert, 2)
print("\nSous-tableaux après vsplit :")
for i, sub in enumerate(subarrays):
    print(f"Sous-tableau {i+1}:\n{sub}")
