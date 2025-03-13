from printer import print_title, print_info, print_success, print_failure


def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe un tableau 2D en fonction des indices start et end.
    Imprime la forme initiale et la forme après découpage.
    """
    print_title("Découpe du tableau 2D")

    # Vérification si la liste est un tableau 2D
    if not all(isinstance(row, list) for row in family):
        print_failure("❌ Tous les éléments doivent être des listes.")
        raise ValueError("Tous les éléments doivent être des listes.")

    # Récupérer la taille initiale du tableau
    original_shape = (len(family), len(family[0]) if family else 0)
    print_info(f"My shape is : {original_shape}")

    # Découper le tableau 2D
    sliced_family = family[start:end]

    # Récupérer la nouvelle taille du tableau
    new_shape = (len(sliced_family), len(sliced_family[0]) if sliced_family
                 else 0)
    print_info(f"My new shape is : {new_shape}")

    print_success(f"✅ Découpe réussie : {sliced_family}")

    return sliced_family
