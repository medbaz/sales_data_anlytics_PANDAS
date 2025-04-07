import math  # pour utiliser math.pi

# Saisie des rayons
Rg = float(input("Entrez le rayon du grand disque (Rg) : "))
Rp = float(input("Entrez le rayon du trou central (Rp) : "))

# Vérification que Rp < Rg
if Rp >= Rg:
    print("Erreur : Le rayon du trou (Rp) doit être inférieur au rayon du disque (Rg).")
else:
    # Calcul de la surface utile
    surface = math.pi * (Rg**2 - Rp**2)
    print("La surface utile du disque découpé est :", round(surface, 2), "unités carrées.")
