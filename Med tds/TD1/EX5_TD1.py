# Saisie d'une phrase par l'utilisateur
phrase = input("Saisis une phrase : ")

# Calcul de la longueur
longueur = len(phrase)

# Vérification si la longueur est paire ou impaire
milieu = longueur // 2

if longueur % 2 == 0:
    print("La longueur est paire.")
    print("Première moitié :", phrase[:milieu])
else:
    print("La longueur est impaire.")
    print("Seconde moitié :", phrase[milieu:])
 