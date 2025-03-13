import sys


def main():
    """
    Programme qui vérifie si un nombre est pair ou impair.
    """
    try:
        # Pas d'argument ➡️ rien afficher
        if len(sys.argv) == 1:
            return
        # Trop d'arguments ➡️ AssertionError
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # Vérifie que c'est bien un entier
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        # Pair / impair
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
