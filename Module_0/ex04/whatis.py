"""
Module whatis.py : Vérifie si un nombre est pair ou impair.
"""

import sys

def check_even_odd(number: int) -> str:
    """
    Renvoie "I'm Even." si le nombre est pair, "I'm Odd." sinon.
    """
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

def main():
    try:
        if len(sys.argv) < 2:
            return

        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        print(check_even_odd(number))

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()