import sys
from ft_filter import ft_filter
from printer import print_title, print_info, print_success, print_failure


def main():
    """
    Le programme filtre les mots d'une chaîne (S)
    qui ont une longueur supérieure à N.
    """
    print_title("EX06 ➜ Tester filterstring.py")

    print("DEBUG sys.argv:", sys.argv)

    try:
        # Vérification du nombre d'arguments
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        s = sys.argv[1]

        # Vérification que le second argument est un entier
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")

        print_info(f"Texte fourni : '{s}'")
        print_info(f"Longueur minimale : {n}")

        # Découpe la string en mots
        words = s.split()
        print_info(f"Mots extraits : {words}")

        # Applique la lambda avec ft_filter (lambda obligatoire !)
        filtered_words = [
            word for word in ft_filter(lambda word: len(word) > n, words)
        ]

        print_success(f"Résultat : {filtered_words}")

    except AssertionError as e:
        print_failure(str(e))


if __name__ == "__main__":
    main()
