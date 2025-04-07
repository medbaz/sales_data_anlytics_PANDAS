# 1. Modifier le premier élément, afficher le deuxième
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print("1. Élément à l'indice 1 :", mylist[1])  

# 2. Modifier 'apple' en 'kiwi'
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print("2. Liste après modification :", fruits)  

# 3. Remplacer un élément par deux éléments
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print("3. Élément à l'indice 2 :", mylist[2])  

# 4. Insérer 'orange' au début de la liste et afficher le 2e élément
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print("4. Élément à l'indice 1 :", mylist[1])  

# 5. Ajouter 'orange' à la fin de la liste avec append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("5. Liste après append :", fruits)  

# 6. Insérer 'lemon' à la 2e position avec insert()
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print("6. Liste après insertion de 'lemon' :", fruits)  
