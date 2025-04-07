import json
import os

class CarnetAdresses
    def __init__(self, fichier=contacts.json)
        self.fichier = fichier
        self.contacts = self.charger_contacts()

    def ajouter_contact(self, nom, email, telephone)
        self.contacts[nom] = {email email, telephone telephone}
        self.sauvegarder_contacts()

    def supprimer_contact(self, nom)
        if nom in self.contacts
            del self.contacts[nom]
            self.sauvegarder_contacts()
        else
            print(fContact '{nom}' non trouvé.)

    def rechercher_contact(self, nom)
        return self.contacts.get(nom, fContact '{nom}' non trouvé.)

    def sauvegarder_contacts(self)
        with open(self.fichier, w) as f
            json.dump(self.contacts, f)

    def charger_contacts(self)
        if os.path.exists(self.fichier)
            with open(self.fichier, r) as f
                return json.load(f)
        return {}

    def afficher_contacts(self)
        if self.contacts
            for nom, infos in self.contacts.items()
                print(f{nom}  Email={infos['email']}, Téléphone={infos['telephone']})
        else
            print(Carnet vide.)

# -----------------------
# Exemple d'utilisation 
# -----------------------

carnet = CarnetAdresses()

# Ajouter des contacts
carnet.ajouter_contact(Ali, ali@email.com, 0612345678)
carnet.ajouter_contact(Sara, sara@email.com, 0698765432)

# Afficher tous les contacts
carnet.afficher_contacts()

# Rechercher un contact
print(carnet.rechercher_contact(Ali))
print(carnet.rechercher_contact(Mehdi))

# Supprimer un contact
carnet.supprimer_contact(Sara)
carnet.afficher_contacts()
