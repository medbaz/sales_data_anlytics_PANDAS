# 1. Fonction qui retourne une liste contenant les carrés des éléments de la liste
def liste_carres(liste):
    return [element**2 for element in liste]

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Test de la fonction avec la liste nombres
carres = liste_carres(nombres)

# 3. Affichage de la liste des carrés retournée
print("Liste des carrés des éléments :", carres)
