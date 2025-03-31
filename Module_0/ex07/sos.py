import sys

NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}


def encode_to_morse(text: str) -> str:
    """
    Encode une chaîne de texte en morse.
    Lève une AssertionError si un caractère est invalide.
    """
    try:
        return " ".join(NESTED_MORSE[char.upper()] for char in text)
    except KeyError as e:
        raise AssertionError("the arguments are bad") from e


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        morse = encode_to_morse(text)
        print(morse)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
