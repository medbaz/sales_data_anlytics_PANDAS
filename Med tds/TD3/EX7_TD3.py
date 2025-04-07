# 1. Listes initiales
nombres = [3, 8, 1, 15, 6]
autres_nombres = [7, 11, 19, 24, 33]

# 2. Fusion et tri manuel
def fusionner_et_trier(liste1, liste2):
    fusion = []
    for elt in liste1:
        fusion.append(elt)
    for elt in liste2:
        fusion.append(elt)
    fusion.sort()
    return fusion

# 3. Test de la fonction
fusion = fusionner_et_trier(nombres, autres_nombres)
print("Fusion triée :", fusion)
