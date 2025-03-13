from ex02.DiamondTrap import King
from printer import print_title, print_info, print_success


def main():
    print_title("Ex02 ➜ Tester King Class")

    joffrey = King("Joffrey")
    print_info(f"Initial: {joffrey.__dict__}")

    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")

    print_info(f"Eyes: {joffrey.get_eyes()}")
    print_info(f"Hairs: {joffrey.get_hairs()}")
    print_success(f"After set_eyes/set_hairs: {joffrey.__dict__}")


if __name__ == "__main__":
    main()
