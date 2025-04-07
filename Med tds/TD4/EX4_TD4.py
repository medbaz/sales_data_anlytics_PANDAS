# 1. Créer un fichier texte avec des noms et des notes
def creer_fichier():
    with open("notes_etudiants.txt", "w") as f:
        f.write("Hamza,10\n")
        f.write("Ziko,20\n")
        f.write("Med,18\n")
        

# 2. Lire le fichier et stocker les données dans un dictionnaire
def lire_fichier():
    etudiants = {}
    try:
        with open("notes_etudiants.txt", "r") as f:
            for ligne in f:
                nom, note = ligne.strip().split(',')
                etudiants[nom] = float(note)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    return etudiants

# 3. Calculer la moyenne des notes
def calculer_moyenne(etudiants):
    total = sum(etudiants.values())
    moyenne = total / len(etudiants) if etudiants else 0
    return moyenne

# 4. Afficher les étudiants ayant une note supérieure à la moyenne
def afficher_etudiants_sup_moyenne(etudiants, moyenne):
    print(f"Note moyenne des étudiants : {moyenne:.2f}")
    print("\nÉtudiants ayant une note supérieure à la moyenne :")
    for nom, note in etudiants.items():
        if note > moyenne:
            print(f"{nom}: {note}")

# Programme principal
def menu():
    creer_fichier() 
    
    etudiants = lire_fichier()  
    moyenne = calculer_moyenne(etudiants)  
    
    afficher_etudiants_sup_moyenne(etudiants, moyenne)  
# Lancer le programme
menu()
