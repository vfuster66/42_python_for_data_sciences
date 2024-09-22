

import sys
import string

def count_characters(text: str) -> dict:
    """
    Compte les majuscules, minuscules, ponctuations, chiffres et espaces dans le texte fourni.
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
    Point d'entrée principal du programme.
    Prend un argument en ligne de commande et affiche les informations statistiques sur la chaîne.
    Gère les erreurs lorsqu'il n'y a pas ou trop d'arguments.
    """
    try:
        if len(sys.argv) == 1:  # Aucun argument fourni
            text = input("What is the text to count?\n")
        elif len(sys.argv) == 2:  # Un seul argument
            text = sys.argv[1]
        else:  # Trop d'arguments fournis
            raise AssertionError("Please provide only one argument.")
        
        counts = count_characters(text)
        total_characters = len(text)
        
        print(f"The text contains {total_characters} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
