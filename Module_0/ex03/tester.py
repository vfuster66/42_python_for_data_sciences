from ex03.NULL_not_found import NULL_not_found
from printer import print_title, print_success


def main():
    print_title("=== EX03 ➜ Tester NULL_not_found ===")

    test_objects = {
        "Nothing": None,
        "Cheese": float('NaN'),
        "Zero": 0,
        "Empty": '',
        "Fake": False,
        "Unknown": "Brian"
    }

    for name, obj in test_objects.items():
        result = NULL_not_found(obj)
        print_success(f"✅ ✅ Test '{name}' exécuté : Retour = {result}")


if __name__ == "__main__":
    main()
