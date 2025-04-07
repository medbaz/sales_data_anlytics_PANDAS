# 1. Fonction qui vérifie si un mot est un palindrome
def est_palindrome(mot):
    return mot == mot[::-1]

# 2. Test de la fonction avec les mots "radar", "python" et "level"
mots = ["radar", "python", "level"]
for mot in mots:
    print(f"Le mot '{mot}' est un palindrome ? {est_palindrome(mot)}")
