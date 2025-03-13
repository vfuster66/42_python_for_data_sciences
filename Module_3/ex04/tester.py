from ex04.ft_calculator import calculator
from printer import print_title, print_success


def main():
    print_title("Ex04 ➜ Tester calculator (dot, add, sous)")

    a = [5, 10, 2]
    b = [2, 4, 3]

    calculator.dotproduct(a, b)
    print_success("Dot product ✅")

    calculator.add_vec(a, b)
    print_success("Add vectors ✅")

    calculator.sous_vec(a, b)
    print_success("Sous vectors ✅")


if __name__ == "__main__":
    main()
