import numpy as np

# 1. Opérations élément par élément
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b

print("Addition :", addition)
print("Soustraction :", soustraction)
print("Multiplication :", multiplication)
print("Division :", division)

# 2. Fonctions mathématiques sur un tableau de 0 à π
valeurs = np.linspace(0, np.pi, 5)  # 5 valeurs de 0 à π

sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentielle = np.exp(valeurs)

print("\nValeurs de 0 à π :", valeurs)
print("sin :", sinus)
print("cos :", cosinus)
print("exp :", exponentielle)

# 3. Sélection et remplacement dans un tableau d'entiers
tableau = np.arange(10)  # tableau d'entiers de 0 à 9
pairs = tableau[tableau % 2 == 0]  # sélection des éléments pairs

print("\nTableau original :", tableau)
print("Éléments pairs :", pairs)

# Remplacement des éléments impairs par -1
tableau_modifie = tableau.copy()
tableau_modifie[tableau_modifie % 2 != 0] = -1

print("Tableau après remplacement des impairs par -1 :", tableau_modifie)
