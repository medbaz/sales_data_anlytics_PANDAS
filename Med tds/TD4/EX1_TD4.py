# Fonction pour afficher le menu et obtenir le choix de l'utilisateur
def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter une personne")
    print("2. Rechercher une personne")
    print("3. Supprimer une personne")
    print("4. Quitter")
    return input("Choisissez une option (1/2/3/4) : ")

# 1. Création d'un dictionnaire pour stocker les informations
personnes = {}

# Boucle pour continuer à exécuter le programme jusqu'à ce que l'utilisateur choisisse de quitter
while True:
    choix = afficher_menu()

    if choix == '1':  # Ajouter une personne
        nom = input("Entrez le nom de la personne : ")
        age = input(f"Entrez l'âge de {nom} : ")

        if age.isdigit():  # Vérifie si l'âge est un nombre
            personnes[nom] = int(age)
            print(f"{nom} a été ajouté avec succès.")
        else:
            print("Veuillez entrer un âge valide.")

    elif choix == '2':  # Rechercher une personne
        nom = input("Entrez le nom de la personne à rechercher : ")
        if nom in personnes:
            print(f"{nom} a {personnes[nom]} ans.")
        else:
            print(f"{nom} n'est pas dans le dictionnaire.")

    elif choix == '3':  # Supprimer une personne
        nom = input("Entrez le nom de la personne à supprimer : ")
        if nom in personnes:
            del personnes[nom]
            print(f"{nom} a été supprimé du dictionnaire.")
        else:
            print(f"{nom} n'est pas dans le dictionnaire.")

    elif choix == '4':  # Quitter
        print("Au revoir!")
        break

    else:
        print("Option invalide, veuillez réessayer.")
