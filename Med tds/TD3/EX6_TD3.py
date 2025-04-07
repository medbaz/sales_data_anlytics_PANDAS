# 1. Fonction qui retourne le minimum et le maximum d'une liste sous forme de tuple
def trouver_min_max(liste):
    return (min(liste), max(liste))

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Test de la fonction avec la liste nombres
min_max = trouver_min_max(nombres)

# Affichage du minimum et du maximum retournés
print("Le minimum et le maximum de la liste sont :", min_max)
