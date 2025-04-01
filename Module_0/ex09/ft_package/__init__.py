def count_in_list(lst, item):
    """Compte le nombre d'occurrences de 'item' dans 'lst'."""
    if not isinstance(lst, list):
        raise TypeError("Le premier argument doit être une liste.")
    return lst.count(item)


