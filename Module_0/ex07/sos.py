from printer import print_title, print_info, print_success, print_failure

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

BASH_INTERPRETED_CHARS = ['$', '!', '&', '*', '|', '<', '>', '?', '`', '\\',
                          '"', ';', '(', ')']


def encode_to_morse(text: str) -> str:
    """
    Encode le texte en code Morse.
    """
    invalid_chars = [char for char in text if char.upper() not in NESTED_MORSE]

    if invalid_chars:
        raise AssertionError(
            f"the arguments are bad: invalid character(s) {invalid_chars}"
        )

    morse_code_list = [NESTED_MORSE[char.upper()] for char in text]
    return " ".join(morse_code_list)


def morse_runner(text: str) -> str:
    """
    Fonction qui exécute l'encodage et retourne
    le résultat ou un message d'erreur.
    """
    print_title("EX07 ➜ SOS (Morse Code Encoder)")

    try:
        if any(char in text for char in BASH_INTERPRETED_CHARS):
            print_failure("⚠️ Attention : caractères spéciaux détectés.")
            print_info("💡 Utilisez des quotes simples :")
            print_info("➡️ Exemple : python3 sos.py 'H$llo'")
            return ""

        print_info(f"Texte à encoder : '{text}'")

        morse_code = encode_to_morse(text)
        print_success(f"✅ Morse : {morse_code}")

        return morse_code

    except AssertionError as e:
        print_failure(f"AssertionError: {e}")
        return ""
