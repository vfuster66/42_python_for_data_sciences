from ex03.ft_calculator import calculator
from printer import print_title, print_info, print_success


def main():
    print_title("Ex03 ➜ Tester calculator Class")

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print_success("Addition ✅")

    print_info("---")

    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print_success("Multiplication ✅")

    print_info("---")

    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print_success("Subtraction and Division ✅")


if __name__ == "__main__":
    main()
