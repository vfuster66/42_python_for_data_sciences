import sys
import string


def count_characters(text: str) -> dict:
    """
    Compte les majuscules, minuscules, ponctuations,
    chiffres et espaces dans le texte fourni.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1

    return counts


def main():
    """
    Programme principal : récupère une chaîne (argument ou input),
    affiche le nombre total de caractères et les stats par type.
    """
    try:
        if len(sys.argv) < 2:
            print("What is the text to count?")
            text = sys.stdin.readline()  # <-- garde le \n
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        counts = count_characters(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
