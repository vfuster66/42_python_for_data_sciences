from ex00.ft_statistics import ft_statistics
from printer import print_title


def main():
    print_title("Ex00 ➜ Tester ft_statistics")

    print_title("Exemple 1")
    ft_statistics(1, 42, 360, 11, mean="mean", median="median")

    print_title("Exemple 2")
    ft_statistics(1, 42, 360, 11, quart="quartile")

    print_title("Exemple 3")
    ft_statistics(1, 42, 360, 11, wrong="unknown")


if __name__ == "__main__":
    main()
