import subprocess
from ex06.ft_filter import ft_filter
from printer import print_title, print_info, print_success, print_failure


def test_ft_filter():
    """
    Teste la fonction personnalisée ft_filter.
    """
    print_title("Test ➜ ft_filter()")

    # Cas 1 : Filtrer les nombres pairs
    input_data = [1, 2, 3, 4, 5, 6]
    print_info(f"Cas 1 - Input : {input_data} (nombres pairs)")
    result = list(ft_filter(lambda x: x % 2 == 0, input_data))
    expected_output = [2, 4, 6]

    if result == expected_output:
        print_success(f"✅ Cas 1 OK : {result}")
    else:
        print_failure(f"❌ Cas 1 FAILED : {result} "
                      f"(attendu : {expected_output})")
        raise AssertionError("Erreur dans ft_filter (nombres pairs)")

    # Cas 2 : ft_filter avec None (truthy uniquement)
    input_data = [0, 1, 2, '', 'Hello', None]
    print_info(f"Cas 2 - Input : {input_data} (truthy)")
    result = list(ft_filter(None, input_data))
    expected_output = [1, 2, 'Hello']

    if result == expected_output:
        print_success(f"✅ Cas 2 OK : {result}")
    else:
        print_failure(f"❌ Cas 2 FAILED : {result} "
                      f"(attendu : {expected_output})")
        raise AssertionError("Erreur dans ft_filter (None/truthy)")

    print_success("✅ Tous les tests de ft_filter sont passés !\n")


def test_filterstring():
    """
    Teste le programme filterstring.py dans différents cas.
    """
    print_title("Test ➜ filterstring.py")

    # Cas 1 : Texte valide, filtre sur longueur > 4
    input_string = 'Hello the World'
    input_length = '4'
    print_info(f"Cas 1 - Input : '{input_string}', n = {input_length}")

    result = subprocess.run(
        ['python3', 'ex06/filterstring.py', input_string, input_length],
        capture_output=True, text=True
    )
    expected_output = "['Hello', 'World']\n"

    if expected_output.strip() in result.stdout.strip():
        print_success(f"✅ Cas 1 OK : {result.stdout.strip()}")
    else:
        print_failure(
            f"❌ Cas 1 FAILED : {result.stdout.strip()} "
            f"(attendu : {expected_output.strip()})"
        )
        raise AssertionError("Erreur sur Cas 1 (longueur > 4)")

    # Cas 2 : Aucun mot ne passe le filtre (>99)
    input_length = '99'
    print_info(f"Cas 2 - Input : '{input_string}', n = {input_length}")

    result = subprocess.run(
        ['python3', 'ex06/filterstring.py', input_string, input_length],
        capture_output=True, text=True
    )
    expected_output = "[]\n"

    if expected_output.strip() in result.stdout.strip():
        print_success(f"✅ Cas 2 OK : {result.stdout.strip()}")
    else:
        print_failure(
            f"❌ Cas 2 FAILED : {result.stdout.strip()} "
            f"(attendu : {expected_output.strip()})"
        )
        raise AssertionError("Erreur sur Cas 2 (longueur > 99)")

    # Cas 3 : Mauvais ordre d'arguments
    input_length = '3'
    print_info(
        f"Cas 3 - Mauvais ordre : n = {input_length}, texte = '{input_string}'"
    )

    result = subprocess.run(
        ['python3', 'ex06/filterstring.py', input_length, input_string],
        capture_output=True, text=True
    )
    expected_output = "AssertionError: the arguments are bad\n"

    if expected_output.strip() in result.stdout.strip():
        print_success("✅ Cas 3 OK : mauvais ordre détecté")
    else:
        print_failure(
            f"❌ Cas 3 FAILED : {result.stdout.strip()} "
            f"(attendu : {expected_output.strip()})"
        )
        raise AssertionError("Erreur sur Cas 3 (mauvais ordre arguments)")

    # Cas 4 : Aucun argument fourni
    print_info("Cas 4 - Aucun argument fourni")

    result = subprocess.run(
        ['python3', 'ex06/filterstring.py'],
        capture_output=True, text=True
    )
    expected_output = "AssertionError: the arguments are bad\n"

    if expected_output.strip() in result.stdout.strip():
        print_success("✅ Cas 4 OK : aucun argument détecté")
    else:
        print_failure(
            f"❌ Cas 4 FAILED : {result.stdout.strip()} "
            f"(attendu : {expected_output.strip()})"
        )
        raise AssertionError("Erreur sur Cas 4 (aucun argument fourni)")

    print_success("✅ Tous les tests de filterstring.py sont passés !\n")


def main():
    """
    Lance tous les tests pour EX06.
    """
    print_title("EX06 ➜ Tests ft_filter + filterstring")
    test_ft_filter()
    test_filterstring()


if __name__ == "__main__":
    main()
