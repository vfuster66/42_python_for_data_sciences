from ex02.find_ft_type import all_thing_is_obj
from printer import print_title,  print_success


def main():
    print_title("=== EX02 ➜ Tester all_thing_is_obj ===")

    # Les objets à tester
    objects = [
        ["Hello", "tata!"],      # list
        ("Hello", "toto!"),      # tuple
        {"Hello", "tutu!"},      # set
        {"Hello": "titi!"},      # dict
        "Brian",                 # str
        "Toto",                  # str
        10                      # type not found (int)
    ]

    # Exécution
    for obj in objects:
        all_thing_is_obj(obj)

    # Confirmation finale
    result = all_thing_is_obj(10)
    print_success(f"✅ Fonction exécutée : Retour = {result}")


if __name__ == "__main__":
    main()
