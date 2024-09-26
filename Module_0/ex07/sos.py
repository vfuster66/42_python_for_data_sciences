import sys

# Dictionnaire Morse
NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ",
    "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ",
    "S": "... ", "T": "- ", "U": "..- ", "V": "...- ",
    "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
    "7": "--... ",
    "8": "---.. ", "9": "----. ", " ": "/ "
}


def encode_to_morse(text):
    """
    Encode une chaîne de caractères en code Morse en utilisant
    le dictionnaire NESTED_MORSE.
    Si un caractère non alphanumérique ou espace est trouvé,
    lève une AssertionError.
    """
    morse_code = ""
    for char in text:
        upper_char = char.upper()

        # Vérification si le caractère est dans NESTED_MORSE
        if upper_char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")

        morse_code += NESTED_MORSE[upper_char]

    return morse_code.strip()


def main():
    """
    Fonction principale du programme.
    Prend un argument et le convertit en Morse.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        morse_code = encode_to_morse(text)
        print(morse_code)

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
