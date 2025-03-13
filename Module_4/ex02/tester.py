from ex02.callLimit import callLimit
from printer import print_title, print_success


def main():
    print_title("Ex02 ➜ Tester callLimit")

    @callLimit(2)
    def greet():
        print_success("Hello, world!")

    greet()
    greet()
    greet()  # Limite atteinte


if __name__ == "__main__":
    main()
