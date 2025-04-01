from ft_package import count_in_list
from printer import print_title, print_info, print_success


def main():
    print_title("EX09 ➜ Tester count_in_list()")

    lst = ["toto", "tata", "toto"]
    item1 = "toto"
    item2 = "tutu"

    print_info(f"Liste testée : {lst}")
    print_info(f"Recherche de '{item1}' :")
    result1 = count_in_list(lst, item1)
    print_success(f"✅ Résultat : {result1}")

    print_info(f"Recherche de '{item2}' :")
    result2 = count_in_list(lst, item2)
    print_success(f"✅ Résultat : {result2}")


if __name__ == "__main__":
    main()
