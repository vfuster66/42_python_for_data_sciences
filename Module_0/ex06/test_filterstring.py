import subprocess
from ft_filter import ft_filter

def test_ft_filter():
    """
    Test la fonction personnalisée ft_filter pour s'assurer qu'elle fonctionne comme prévu.
    """

    # Cas 1 : Test de ft_filter avec une fonction qui retourne True pour les nombres pairs
    input_data = [1, 2, 3, 4, 5, 6]
    print(f"Cas 1 - Input : {input_data} (filtrer les nombres pairs)")
    result = list(ft_filter(lambda x: x % 2 == 0, input_data))
    expected_output = [2, 4, 6]
    print(f"Résultat attendu : {expected_output}")
    print(f"Résultat obtenu : {result}")
    assert result == expected_output, f"Erreur dans ft_filter avec les nombres pairs : {result}"
    print("Cas 1 réussi !\n")

    # Cas 2 : Test de ft_filter avec None (filtre les éléments 'truthy' uniquement)
    input_data = [0, 1, 2, '', 'Hello', None]
    print(f"Cas 2 - Input : {input_data} (filtrer les éléments 'truthy')")
    result = list(ft_filter(None, input_data))
    expected_output = [1, 2, 'Hello']
    print(f"Résultat attendu : {expected_output}")
    print(f"Résultat obtenu : {result}")
    assert result == expected_output, f"Erreur dans ft_filter avec None comme fonction : {result}"
    print("Cas 2 réussi !\n")

    print("Tous les tests de ft_filter sont passés avec succès !\n")


def test_filterstring():
    """
    Test le programme filterstring.py pour s'assurer qu'il fonctionne correctement dans différents cas.
    """

    # Cas 1 : Test avec une chaîne valide et un entier (filtre les mots de longueur > 4)
    input_string = 'Hello the World'
    input_length = '4'
    print(f"Cas 1 - Input : '{input_string}' et longueur {input_length}")
    result = subprocess.run(['python3', 'filterstring.py', input_string, input_length], capture_output=True, text=True)
    expected_output = "['Hello', 'World']\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur dans filterstring.py avec '{input_string}' et {input_length} : {result.stdout}"
    print("Cas 1 réussi !\n")

    # Cas 2 : Aucun mot ne dépasse la longueur donnée
    input_string = 'Hello the World'
    input_length = '99'
    print(f"Cas 2 - Input : '{input_string}' et longueur {input_length}")
    result = subprocess.run(['python3', 'filterstring.py', input_string, input_length], capture_output=True, text=True)
    expected_output = "[]\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur dans filterstring.py avec '{input_string}' et {input_length} : {result.stdout}"
    print("Cas 2 réussi !\n")

    # Cas 3 : Arguments dans le mauvais ordre (entier en premier)
    input_string = 'Hello the World'
    input_length = '3'
    print(f"Cas 3 - Input : longueur '{input_length}' avant la chaîne '{input_string}' (ordre incorrect)")
    result = subprocess.run(['python3', 'filterstring.py', input_length, input_string], capture_output=True, text=True)
    expected_output = "AssertionError: the arguments are bad\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur dans filterstring.py avec mauvais ordre d'arguments : {result.stdout}"
    print("Cas 3 réussi !\n")

    # Cas 4 : Aucun argument fourni
    print(f"Cas 4 - Input : Aucun argument fourni")
    result = subprocess.run(['python3', 'filterstring.py'], capture_output=True, text=True)
    expected_output = "AssertionError: the arguments are bad\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur dans filterstring.py sans arguments : {result.stdout}"
    print("Cas 4 réussi !\n")

    print("Tous les tests de filterstring.py sont passés avec succès !")


if __name__ == "__main__":
    print("==== Tests pour ft_filter ====")
    test_ft_filter()
    print("\n==== Tests pour filterstring.py ====")
    test_filterstring()
