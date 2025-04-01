from ex09.ft_package import count_in_list
from printer import print_title,  print_success, print_failure


def test_count_existing_item():
    print_title("Test ➜ Ex09 count_in_list : item existant")
    lst = ["apple", "banana", "apple", "orange"]
    item = "apple"
    expected = 2
    result = count_in_list(lst, item)

    if result == expected:
        print_success(f"✅ Test OK : {result} == {expected}")
    else:
        print_failure(f"❌ Test FAILED : {result} != {expected}")
        raise AssertionError("Erreur sur count_in_list avec item existant")


def test_count_missing_item():
    print_title("Test ➜ Ex09 count_in_list : item absent")
    lst = ["apple", "banana", "apple", "orange"]
    item = "pear"
    expected = 0
    result = count_in_list(lst, item)

    if result == expected:
        print_success(f"✅ Test OK : {result} == {expected}")
    else:
        print_failure(f"❌ Test FAILED : {result} != {expected}")
        raise AssertionError("Erreur sur count_in_list avec item absent")


def test_non_iterable_input():
    print_title("Test ➜ Ex09 count_in_list : input non itérable")
    lst = None
    item = "apple"

    try:
        count_in_list(lst, item)
    except TypeError:
        print_success("✅ Test OK : TypeError levée comme attendu")
    else:
        print_failure("❌ Test FAILED : TypeError non levée")
        raise AssertionError(
            "Erreur : aucune exception levée sur input non itérable"
        )
