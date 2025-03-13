import sys

NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}

# Caractères à problème avec bash
BASH_INTERPRETED_CHARS = ['$', '!', '&', '*', '|', '<', '>', '?', '`', '\\',
                          '"', ';', '(', ')']


def encode_to_morse(text):
    invalid_chars = [char for char in text if char.upper() not in NESTED_MORSE]

    if invalid_chars:
        raise AssertionError(
            f"the arguments are bad: invalid character(s) {invalid_chars}")

    morse_code_list = [NESTED_MORSE[char.upper()] for char in text]

    return " ".join(morse_code_list)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        if any(char in text for char in BASH_INTERPRETED_CHARS):
            # ➡️ On avertit l'utilisateur
            print("⚠️  Attention : des caractères spéciaux détectés "
                  "dans l'argument transmis.")
            print("💡 Conseil : utilisez des quotes simples (') "
                  "pour éviter l'interprétation de bash.")
            print("➡️  Exemple : python3 sos.py 'H$llo'")
            return

        morse_code = encode_to_morse(text)
        print(morse_code)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
