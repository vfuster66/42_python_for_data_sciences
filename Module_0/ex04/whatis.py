

import sys

def main():
    try:
        # Vérification du nombre d'arguments
        if len(sys.argv) != 2:
            raise AssertionError(
                "Usage: python whatis.py <number>\n"
                + ("no argument is provided" if len(sys.argv) == 1 else "more than one argument is provided")
            )

        # Vérification que l'argument est un entier
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        # Vérification si le nombre est pair ou impair
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        # Affichage du message d'erreur propre sans Traceback
        print(e)

if __name__ == "__main__":
    main()
