import numpy as np
import matplotlib.pyplot as plt

### 1. MATRICE DE COVARIANCE ###

# Création d'un tableau aléatoire (100 échantillons, 3 variables)
donnees = np.random.rand(100, 3)

# Calcul de la matrice de covariance
covariance = np.cov(donnees.T)
print("1. Matrice de covariance (3 variables aléatoires) :\n", covariance)


### 2. TRANSFORMATION DE FOURIER ###

# Création d'un signal sinusoïdal
x = np.linspace(0, 2 * np.pi, 500)
signal = np.sin(5 * x) + 0.5 * np.sin(10 * x)

# Transformation de Fourier
spectre = np.fft.fft(signal)
frequences = np.fft.fftfreq(len(x), d=(x[1] - x[0]))

# Affichage du spectre de fréquences
plt.figure(figsize=(10, 4))
plt.plot(frequences[:250], np.abs(spectre)[:250])  # Moitié positive du spectre
plt.title("2. Spectre de fréquences (FFT)")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()


### 3. SIMULATION DE LANCERS DE DÉS ###

# Simulation de 1000 lancers de deux dés
lancer1 = np.random.randint(1, 7, 1000)
lancer2 = np.random.randint(1, 7, 1000)
somme_lancers = lancer1 + lancer2

# Affichage de l'histogramme des sommes
plt.figure(figsize=(8, 4))
plt.hist(somme_lancers, bins=range(2, 14), align='left', rwidth=0.8,
         color='skyblue', edgecolor='black')
plt.title("3. Histogramme des sommes de 2 dés (1000 lancers)")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.xticks(range(2, 13))
plt.grid(axis='y')
plt.tight_layout()
plt.show()
