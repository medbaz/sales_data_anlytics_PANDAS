# Fonction pour fusionner deux dictionnaires
def fusionner_dictionnaires(d1, d2):
    # Fusionner les deux dictionnaires
    d3 = d1.copy()  # Copier d1 pour éviter de modifier l'original
    
    for key, value in d2.items():
        if key in d3:
            if isinstance(d3[key], (int, float)) and isinstance(value, (int, float)):
                d3[key] += value  # Ajouter si les deux valeurs sont numériques
            elif isinstance(d3[key], str) and isinstance(value, str):
                d3[key] += value  # Concaténer si les deux valeurs sont des chaînes
        else:
            d3[key] = value  # Ajouter la clé et sa valeur si elle n'existe pas dans d3

    # Retourner le dictionnaire trié par ordre alphabétique des clés
    return dict(sorted(d3.items()))

# Exemple d'utilisation
d1 = {"a": 10, "b": "test"}
d2 = {"a": 5, "c": "data"}

# Fusionner les dictionnaires
resultat = fusionner_dictionnaires(d1, d2)

# Affichage du résultat
print(resultat)
