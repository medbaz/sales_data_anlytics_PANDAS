import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



url = "https://raw.githubusercontent.com/intern2grow/sales-data-analysis/main/sales_data.csv"
df = pd.read_csv(url)



print("Les 5 premières lignes :")
print(df.head())


print("\nInfos générales :")
print(df.info())


print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())


df["revenue"] = df["revenue"].fillna(df["quantity"] * df["price"])
df["price"] = df["price"].fillna(0)
df["quantity"] = df["quantity"].fillna(1)







electronique = df[df["category"] == "Electronics"]
print("\nVentes de produits électroniques :")
print(electronique)


df_sorted = df.sort_values(by="revenue", ascending=False)
print("\nTop 5 des ventes en termes de revenu :")
print(df_sorted.head())

df["Revenu_TVA"] = df["revenue"] * 1.20


revenu_par_categorie = df.groupby("category")["revenue"].sum()
print("\nRevenu total par catégorie :")
print(revenu_par_categorie)





print("\nStatistiques générales des ventes :")
print(df["revenue"].describe())

print(f"\nRevenu minimum : {df['revenue'].min()}")
print(f"Revenu maximum : {df['revenue'].max()}")




print(f"\nMoyenne du revenu : {df['revenue'].mean()}")
print(f"Médiane du revenu : {df['revenue'].median()}")

print(f"\nÉcart-type du revenu : {df['revenue'].std()}")
print(f"Variance du revenu : {df['revenue'].var()}")


revenu_par_categorie = df.groupby("category")["revenue"].sum()
print("\nRevenu total par catégorie :")
print(revenu_par_categorie)






plt.figure(figsize=(8, 5))
sns.histplot(df["revenue"], bins=10, kde=True)
plt.title("Distribution des revenus")
plt.xlabel("revenue")
plt.ylabel("Nombre de ventes")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="category", y="revenue", data=df)
plt.xticks(rotation=45)
plt.title("Répartition des revenus par catégorie")
plt.show()

plt.figure(figsize=(8, 5))
revenu_par_categorie.plot(kind="bar", color="skyblue")
plt.title("Revenu total par catégorie")
plt.xlabel("category")
plt.ylabel("Revenu total")
plt.show()
