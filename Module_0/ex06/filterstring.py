import sys
from ft_filter import ft_filter

def main():
    """
    Le programme filtre les mots d'une chaîne (S) qui ont une longueur supérieure à N.
    """
    try:
        # Vérification du nombre d'arguments et de leur type
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")

        # Séparer les mots de la chaîne S
        words = s.split()

        # Utilisation de ft_filter et d'une lambda pour filtrer les mots
        filtered_words = list(ft_filter(lambda word: len(word) > n, words))

        # Affichage du résultat
        print(filtered_words)

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
