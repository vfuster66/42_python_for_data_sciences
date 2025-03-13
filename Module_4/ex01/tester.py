from ex01.in_out import outer
from printer import print_title, print_success


def main():
    print_title("Ex01 ➜ Tester outer/inner")

    my_inner_function = outer(10)
    result = my_inner_function()
    print_success(f"Result of inner(): {result}")


if __name__ == "__main__":
    main()
