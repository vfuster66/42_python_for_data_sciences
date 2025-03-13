from printer import print_success, print_failure


def NULL_not_found(obj: any) -> int:
    """
    Vérifie si l'objet est un des types 'null' et affiche son type.
    Retourne 0 si trouvé, 1 sinon.
    """
    if obj is None:
        print_success(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, float) and obj != obj:
        print_success(f"Cheese: {obj} {type(obj)}")
    elif obj is False:
        print_success(f"Fake: {obj} {type(obj)}")
    elif obj == 0:
        print_success(f"Zero: {obj} {type(obj)}")
    elif obj == '':
        print_success(f"Empty: {type(obj)}")
    else:
        print_failure("Type not Found")
        return 1
    return 0
