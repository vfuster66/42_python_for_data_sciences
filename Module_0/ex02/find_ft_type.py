from printer import print_info, print_success, print_failure


def all_thing_is_obj(object: any) -> int:
    """
    Affiche le type de l'objet passé en paramètre et retourne 42.
    """
    if isinstance(object, list):
        print_success(f"✅ List : {type(object)}")
    elif isinstance(object, tuple):
        print_success(f"✅ Tuple : {type(object)}")
    elif isinstance(object, set):
        print_success(f"✅ Set : {type(object)}")
    elif isinstance(object, dict):
        print_success(f"✅ Dict : {type(object)}")
    elif isinstance(object, str):
        print_info(f"{object} is in the kitchen : {type(object)}")
    else:
        print_failure("❌ Type not found")
    return 42
