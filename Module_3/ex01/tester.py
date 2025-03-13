from ex01.S1E7 import Baratheon, Lannister
from printer import print_title, print_info, print_success


def main():
    print_title("Ex01 ➜ Tester Baratheon & Lannister")

    robert = Baratheon("Robert")
    print_info(f"Robert: {robert.__dict__}")
    print_info(f"__str__: {robert.__str__()}")
    print_info(f"__repr__: {robert.__repr__()}")
    print_info(f"Alive before die(): {robert.is_alive}")
    robert.die()
    print_info(f"Alive after die(): {robert.is_alive}")
    print_success(f"Docstring Baratheon: {robert.__doc__}")

    print_title("Creating Cersei...")
    cersei = Lannister("Cersei")
    print_info(f"Cersei: {cersei.__dict__}")
    print_info(f"__str__: {cersei.__str__()}")
    print_info(f"Alive: {cersei.is_alive}")

    print_title("Creating Jaine with create_lannister()...")
    jaine = Lannister.create_lannister("Jaine", True)
    print_success(f"Name: {jaine.first_name}, Alive: {jaine.is_alive}")


if __name__ == "__main__":
    main()
