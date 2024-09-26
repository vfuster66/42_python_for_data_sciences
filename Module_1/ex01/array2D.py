# array2D.py

def slice_me(family: list, start: int, end: int) -> list:
    """
    Découpe un tableau 2D en fonction des indices start et end.
    Imprime la forme initiale et la forme après découpage.
    """
    # Vérification si la liste est un tableau 2D
    if not all(isinstance(row, list) for row in family):
        raise ValueError("Tous les éléments doivent être des listes.")

    # Récupérer la taille initiale du tableau
    original_shape = (len(family), len(family[0]) if family else 0)
    print(f"My shape is : {original_shape}")

    # Découper le tableau 2D
    sliced_family = family[start:end]

    # Récupérer la nouvelle taille du tableau
    new_shape = (len(sliced_family),
                 len(sliced_family[0]) if sliced_family else 0)
    print(f"My new shape is : {new_shape}")

    return sliced_family
