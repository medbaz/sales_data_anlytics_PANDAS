import math  # Pour utiliser la constante math.pi

# Saisie des valeurs
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume
volume = (1/3) * math.pi * rayon**2 * hauteur
print("Le volume du cône est :", round(volume, 2), "unités cubes")
