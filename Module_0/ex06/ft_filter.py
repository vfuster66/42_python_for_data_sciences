def ft_filter(function, iterable):
    """
    Recode de la fonction filter().
    Applique 'function' à chaque élément de 'iterable' et retourne un itérable
    des éléments pour lesquels 'function' renvoie True.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
