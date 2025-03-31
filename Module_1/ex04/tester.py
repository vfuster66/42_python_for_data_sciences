# ex04/tester.py

from rotate import ft_rotate
from printer import print_title, print_success, print_failure


def main():
    print_title("Ex04 ➜ Tester ft_rotate()")

    transposed = ft_rotate()

    if transposed is not None:
        print_success(f"✅ Rotation réussie : {transposed.shape}")
    else:
        print_failure("❌ Échec de la rotation")


if __name__ == "__main__":
    main()

