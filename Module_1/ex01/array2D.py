def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe un tableau 2D en fonction des indices start et end.
    Imprime la forme initiale et la forme après découpage.
    """

    # Vérification que c'est bien une liste de listes
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        print("❌ Le tableau doit être une liste de listes.")
        raise ValueError("Le tableau doit être une liste de listes.")

    # Vérification que chaque ligne a la même longueur
    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) != 1:
        print("❌ Toutes les lignes doivent avoir la même longueur.")
        raise ValueError("Toutes les lignes doivent avoir la même longueur.")

    # Vérification des types de start/end
    if not isinstance(start, int) or not isinstance(end, int):
        print("❌ Les indices start et end doivent être des entiers.")
        raise TypeError("Les indices start et end doivent être des entiers.")

    # Affichage de la forme initiale
    original_shape = (len(family), row_lengths[0])
    print(f"My shape is : {original_shape}")

    # Découpage
    sliced = family[start:end]

    # Affichage de la nouvelle forme
    new_shape = (len(sliced), row_lengths[0] if sliced else 0)
    print(f"My new shape is : {new_shape}")

    return sliced
