import numpy as np

# Pour une reproductibilité des données
np.random.seed(0)

### 1. Créer un tableau 2D (12 mois x 3 produits) avec valeurs aléatoires entre 100 et 1000 ###
ventes = np.random.randint(100, 1001, size=(12, 3))
print("Tableau des ventes (mois x produits):\n", ventes)

produits = ['P1', 'P2', 'P3']
mois = np.array([
    'Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin',
    'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'
])

### 2. Total annuel des ventes par produit ###
total_par_produit = np.sum(ventes, axis=0)
print("\n2. Total annuel des ventes par produit :")
for i, total in enumerate(total_par_produit):
    print(f"{produits[i]} : {total}")

### 3. Moyenne mensuelle des ventes par produit ###
moyenne_par_produit = np.mean(ventes, axis=0)
print("\n3. Moyenne mensuelle des ventes par produit :")
for i, moyenne in enumerate(moyenne_par_produit):
    print(f"{produits[i]} : {moyenne:.2f}")

### 4. Mois avec ventes maximales pour chaque produit ###
mois_max_ventes = np.argmax(ventes, axis=0)
print("\n4. Mois avec les ventes maximales pour chaque produit :")
for i, mois_idx in enumerate(mois_max_ventes):
    print(f"{produits[i]} : {mois[mois_idx]} ({ventes[mois_idx, i]})")

### 5. Croissance mensuelle en % par produit ###
croissance_pourcentage = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("\n5. Croissance mensuelle en % pour chaque produit (ligne = mois N, comparé à N-1) :\n")
print(np.round(croissance_pourcentage, 2))

### 6. Mois avec la plus forte croissance pour chaque produit ###
mois_max_croissance = np.argmax(croissance_pourcentage, axis=0) + 1  # +1 car np.diff diminue d'une ligne
print("\n6. Mois avec la plus forte croissance pour chaque produit :")
for i, mois_idx in enumerate(mois_max_croissance):
    print(f"{produits[i]} : {mois[mois_idx]} ({croissance_pourcentage[mois_idx-1, i]:.2f}%)")

### 7. Somme des ventes tous produits confondus par mois ###
somme_par_mois = np.sum(ventes, axis=1)
print("\n7. Somme des ventes par mois (tous produits) :")
for i, total_mois in enumerate(somme_par_mois):
    print(f"{mois[i]} : {total_mois}")
