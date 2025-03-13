from ex00.S1E9 import Stark
from printer import print_title, print_success, print_info


def main():
    print_title("Ex00 ➜ Tester Stark Class")

    Ned = Stark("Ned")
    print_info(f"Ned attributes: {Ned.__dict__}")
    print_info(f"Is Ned alive? {Ned.is_alive}")
    Ned.die()
    print_info(f"Is Ned alive after die()? {Ned.is_alive}")
    print_success("Stark docstring: " + str(Ned.__doc__))
    print_success("Init docstring: " + str(Ned.__init__.__doc__))
    print_success("Die docstring: " + str(Ned.die.__doc__))

    print_title("Creating Lyanna...")
    Lyanna = Stark("Lyanna", False)
    print_info(f"Lyanna attributes: {Lyanna.__dict__}")


if __name__ == "__main__":
    main()
