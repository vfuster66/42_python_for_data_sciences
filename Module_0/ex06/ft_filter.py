def ft_filter(function, iterable):
    """
    Recode de la fonction filter().
    Applique 'function' à chaque élément de 'iterable' et retourne un itérable
    des éléments pour lesquels 'function' renvoie True.
    """
    # Si la fonction est None, on filtre simplement les éléments "truthy"
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))
