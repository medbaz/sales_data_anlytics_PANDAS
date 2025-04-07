#Q1
# Saisie des notes
anglais = float(input("Note en Anglais : "))
physique = float(input("Note en Physique : "))
maths = float(input("Note en Maths : "))
svt = float(input("Note en SVT : "))

# Saisie des coefficients
coef_ang = int(input("Coefficient Anglais : "))
coef_phy = int(input("Coefficient Physique : "))
coef_math = int(input("Coefficient Maths : "))
coef_svt = int(input("Coefficient SVT : "))

# Calcul de la moyenne pondérée
somme_notes = (anglais * coef_ang + physique * coef_phy + maths * coef_math + svt * coef_svt)
somme_coefs = (coef_ang + coef_phy + coef_math + coef_svt)
moyenne = somme_notes / somme_coefs

print("La moyenne des notes est :", round(moyenne, 2))

#Q2
budget = float(input("Entrez votre budget : "))
achats = float(input("Montant des achats : "))

if budget >= achats:
    print(f"Achat possible. Il vous restera {budget - achats:} DH.")
else:
    print(f"Achat impossible. Il vous manque {achats - budget:} DH.")

