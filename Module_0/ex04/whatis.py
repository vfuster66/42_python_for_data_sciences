"""
Module whatis.py : Vérifie si un nombre est pair ou impair.
"""


def check_even_odd(number: int) -> str:
    """
    Renvoie "I'm Even." si le nombre est pair, "I'm Odd." sinon.
    """
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."
