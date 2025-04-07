# 1. Créer un fichier texte avec des noms et des âges
def creer_fichier():
    with open("noms_ages.txt", "w") as f:
        f.write("Zakaria,22\n")
        f.write("Mohamed,24\n")
        f.write("Hamza,20\n")
        

# 2. Lire le fichier et stocker les données dans un dictionnaire
def lire_fichier():
    personnes = {}
    try:
        with open("noms_ages.txt", "r") as f:
            for ligne in f:
                nom, age = ligne.strip().split(',')
                personnes[nom] = int(age)
    except FileNotFoundError:
        print("Le fichier n'existe pas encore.")
    return personnes

# 3. Ajouter ou modifier un enregistrement
def ajouter_ou_modifier_enregistrement(personnes):
    nom = input("Entrez le nom à ajouter ou modifier : ")
    age = input(f"Entrez l'âge de {nom} : ")
    
    if age.isdigit():
        personnes[nom] = int(age)
        # Mettre à jour le fichier
        with open("noms_ages.txt", "w") as f:
            for nom, age in personnes.items():
                f.write(f"{nom},{age}\n")
        print(f"L'enregistrement pour {nom} a été ajouté/modifié avec succès.")
    else:
        print("Veuillez entrer un âge valide.")

# Programme principal
def menu():
    creer_fichier()  # Créer le fichier au départ (si besoin)
    
    personnes = lire_fichier()  # Lire le fichier et stocker dans un dictionnaire
    print("Dictionnaire des personnes :", personnes)
    
    while True:
        print("\nMenu :")
        print("1. Ajouter ou modifier un enregistrement")
        print("2. Quitter")
        choix = input("Choisissez une option (1/2) : ")
        
        if choix == '1':
            ajouter_ou_modifier_enregistrement(personnes)
        elif choix == '2':
            print("Au revoir!")
            break
        else:
            print("Option invalide, réessayez.")

# Lancer le programme
menu()
