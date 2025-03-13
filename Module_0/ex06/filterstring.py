import sys
from ft_filter import ft_filter


def main():
    """
    Le programme filtre les mots d'une chaîne (S) qui ont une longueur
    supérieure à N.
    """
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

        # Découpe la string en mots
        words = s.split()

        # Applique la lambda avec ft_filter (lambda obligatoire !)
        filtered_words = [
            word for word in ft_filter(lambda word: len(word) > n, words)
        ]

        # Affiche la liste résultante
        print(filtered_words)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
