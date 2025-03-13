import sys
from building import count_characters
from printer import print_title, print_info, print_success, print_failure


def main():
    """
    Exécute le programme en récupérant soit un argument,
    soit une saisie input().
    Affiche les stats de caractères dans le texte fourni.
    """
    print_title("EX05 ➜ Character counter")

    try:
        if len(sys.argv) == 1:
            print_info("Aucun argument détecté, demande de saisie "
                       "utilisateur.")
            text = input("What is the text to count?\n")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print_failure("❌ more than one argument is provided")
            print_info("👉 Usage : make ex05 text=\"your text here\"")
            raise AssertionError("more than one argument is provided")

        counts = count_characters(text)
        total_characters = len(text)

        print_success(f"Le texte contient {total_characters} caractères :")
        print_info(f"{counts['upper']} upper letters")
        print_info(f"{counts['lower']} lower letters")
        print_info(f"{counts['punctuation']} punctuation marks")
        print_info(f"{counts['spaces']} spaces")
        print_info(f"{counts['digits']} digits")

    except AssertionError as e:
        print_failure(f"❌ {e}")
    except Exception as e:
        print_failure(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
