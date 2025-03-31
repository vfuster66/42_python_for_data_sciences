# NULL_not_found.py
def NULL_not_found(object: any) -> int:
    """
    Affiche le type de l'objet passé en paramètre et retourne 0 si tout va bien.
    Retourne 1 en cas d'erreur.
    """
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif isinstance(object, float) and (object != object):  # Vérifie NaN
        print(f"Cheese: {object} <class 'float'>")
    elif isinstance(object, int) and object is not False:  # Exclut False
        print(f"Zero: {object} <class 'int'>")
    elif isinstance(object, str) and object == '':  # Exclut les chaînes non vides
        print(f"Empty: {object} <class 'str'>")
    elif isinstance(object, bool):
        print(f"Fake: {object} <class 'bool'>")
    else:
        print("Type not Found")
        return 1
    
    return 0
