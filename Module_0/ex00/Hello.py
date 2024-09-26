# Initialisation des structures de données
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modifications des valeurs pour afficher les salutations requises

# Pour ft_list
ft_list[1] = "World!"

# Pour ft_tuple (les tuples sont immuables, donc on recrée le tuple)
ft_tuple = (ft_tuple[0], "France!")

# Pour ft_set (les sets sont non ordonnés,
# on doit donc gérer les ajouts et suppressions)
ft_set.remove("tutu!")
ft_set.add("Perpignan!")

# Pour ft_dict
ft_dict["Hello"] = "42Perpignan!"

# Affichage des résultats finaux
print(ft_list)  # Affichage de la liste modifiée
print(ft_tuple)  # Affichage du tuple modifié
print(sorted(ft_set))  # Le tri permet de garantir un ordre lors de l'affichage
print(ft_dict)  # Affichage du dictionnaire modifié
