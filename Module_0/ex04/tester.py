"""
Script tester.py : Appelle la fonction check_even_odd avec gestion des erreurs.
"""

import sys
from whatis import check_even_odd
from printer import print_info, print_success, print_failure, print_title


def main():
    print_title("EX04 ➜ Tester check_even_odd()")

    try:
        # Pas d'argument ➡️ on affiche un message spécifique
        if len(sys.argv) == 1:
            print_failure("❌ Aucun argument fourni !")
            print_info("🔎 Usage : python tester.py <number>")
            return

        # Trop d'arguments ➡️ erreur
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # Vérifie que l'argument est un entier
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        # Appel de la fonction
        result = check_even_odd(number)
        print_success(f"✅ ✅ {result}")

    except AssertionError as e:
        print_failure(f"❌ ❌ {e}")


if __name__ == "__main__":
    main()
