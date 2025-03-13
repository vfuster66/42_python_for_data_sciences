import sys
from ex07.sos import morse_runner
from printer import print_title, print_info, print_failure


def main():
    """
    Fonction principale d'exécution du module ex07.
    """
    print_title("EX07 ➜ Tester sos.py")

    if len(sys.argv) != 2:
        print_failure("❌ ❌ Aucun texte fourni !")
        print_info("🔎 👉 Exemple : make ex07 text='Hello World'")
        return

    text = sys.argv[1]
    morse_runner(text)


if __name__ == "__main__":
    main()
