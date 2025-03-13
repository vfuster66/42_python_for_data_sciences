from typing import Any


def NULL_not_found(obj: Any) -> int:
    """
    Vérifie si l'objet est un des types 'null' et affiche son type.
    Retourne 0 si trouvé, 1 sinon.
    """
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} {type(obj)}")
    elif obj == 0:
        print(f"Zero: {obj} {type(obj)}")
    elif obj == '':
        print(f"Empty: {type(obj)}")
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
    else:
        print("Type not Found")
        return 1
    return 0
