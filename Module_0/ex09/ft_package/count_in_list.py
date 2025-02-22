def count_in_list(lst, item):
    """
    Compte combien de fois 'item' apparaît dans la liste 'lst'.

    Args:
        lst (list): La liste où chercher les éléments.
        item (any): L'élément à compter.

    Returns:
        int: Le nombre de fois où 'item' apparaît dans 'lst'.

    Raises:
        TypeError: Si 'lst' n'est pas une liste ou un itérable.
    """
    try:
        return lst.count(item)
    except AttributeError:
        raise TypeError(f"'{type(lst).__name__}' object is not iterable")
