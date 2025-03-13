from ex01.array2D import slice_me
from printer import print_title, print_info, print_success


def main():
    print_title("Ex01 ➜ Tester slice_me")

    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print_info("Découpage de 0 à 2")
    result_1 = slice_me(family, 0, 2)
    print_success(f"Résultat : {result_1}")

    print_info("Découpage de 1 à -2")
    result_2 = slice_me(family, 1, -2)
    print_success(f"Résultat : {result_2}")


if __name__ == "__main__":
    main()
