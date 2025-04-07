# 1. Fonction qui retourne la somme des éléments d'une liste
def somme_liste(liste):
    return sum(liste)

# 2. Fonction qui retourne la moyenne des éléments d'une liste
def moyenne_liste(liste):
    return sum(liste) / len(liste) if len(liste) > 0 else 0  # Eviter la division par 0

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# Calcul et affichage de la somme et de la moyenne des éléments de la liste
somme = somme_liste(nombres)
moyenne = moyenne_liste(nombres)

print("Somme des éléments :", somme)
print("Moyenne des éléments :", moyenne)
