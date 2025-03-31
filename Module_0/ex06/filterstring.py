import sys
from ft_filter import ft_filter


def main():
    """
    Le programme filtre les mots d'une chaîne (S)
    qui ont une longueur supérieure à N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = s.split()
        filtered_words = [word for word in ft_filter(lambda word: len(word) > n, words)]
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
