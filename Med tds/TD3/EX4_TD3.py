# 1. Fonction qui vérifie si un élément existe dans la liste
def element_existe(liste, element):
    return element in liste

# Liste des nombres
nombres = [4, 8, 15, 16, 23, 42]

# 2. Test de la fonction avec l'élément 15 et l'élément 50
test_1 = element_existe(nombres, 15)  # Test avec l'élément 15
test_2 = element_existe(nombres, 50)  # Test avec l'élément 50

# Affichage des résultats
print("L'élément 15 existe-t-il dans la liste ? :", test_1)
print("L'élément 50 existe-t-il dans la liste ? :", test_2)
