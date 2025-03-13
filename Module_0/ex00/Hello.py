from printer import print_title, print_success


def display_hello():
    """
    Modifie et affiche les structures de données avec les valeurs demandées.
    """
    print_title("=== EX00 ➜ First Python Script ===")

    # Initialisation des structures de données
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # Modifications
    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_set.remove("tutu!")
    ft_set.add("Perpignan!")
    ft_dict["Hello"] = "42Perpignan!"

    # Affichage des résultats
    print_success(f"✅ Liste : {ft_list}")
    print_success(f"✅ Tuple : {ft_tuple}")
    print_success(f"✅ Set   : {sorted(ft_set)}")
    print_success(f"✅ Dict  : {ft_dict}")

    # Retourne les structures pour test éventuel
    return ft_list, ft_tuple, sorted(ft_set), ft_dict
