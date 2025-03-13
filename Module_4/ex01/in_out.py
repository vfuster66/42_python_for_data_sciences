from printer import print_title, print_info


def outer(value):
    print_title(f"Outer received: {value}")

    def inner():
        print_info(f"Inner is using the outer value: {value}")
        return value * 2

    return inner
