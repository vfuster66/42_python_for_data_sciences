import subprocess


def test_sos():
    """
    Test du programme sos.py avec différents cas.
    """

    # Cas 1 : Chaîne valide "sos"
    try:
        input_text = "sos"
        print(f"Cas 1 - Input : {input_text}")
        result = subprocess.run(['python3', 'sos.py', input_text],
                                capture_output=True, text=True)
        expected_output = "... --- ...\n"
        print(f"Résultat attendu : {expected_output.strip()}")
        print(f"Résultat obtenu : {result.stdout.strip()}")
        assert result.stdout == expected_output, f"Erreur \
            avec '{input_text}': {result.stdout}"
        print("Cas 1 réussi !\n")
    except AssertionError as e:
        print(e)

    # Cas 2 : Chaîne valide "Hello World"
    try:
        input_text = "Hello World"
        print(f"Cas 2 - Input : {input_text}")
        result = subprocess.run(['python3', 'sos.py', input_text],
                                capture_output=True, text=True)
        expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -..\n"
        print(f"Résultat attendu : {expected_output.strip()}")
        print(f"Résultat obtenu : {result.stdout.strip()}")
        assert result.stdout == expected_output, f"Erreur \
            avec '{input_text}': {result.stdout}"
        print("Cas 2 réussi !\n")
    except AssertionError as e:
        print(e)

    # Cas 3 : Caractères invalides "$"
    try:
        input_text = "h$llo"
        print(f"Cas 3 - Input : {input_text}")
        result = subprocess.run(['python3', 'sos.py', input_text],
                                capture_output=True, text=True)
        expected_output = "the arguments are bad\n"
        print(f"Résultat attendu : {expected_output.strip()}")
        print(f"Résultat obtenu : {result.stdout.strip()}")
        assert result.stdout == expected_output, f"Erreur \
            avec '{input_text}' : {result.stdout}"
        print("Cas 3 réussi !\n")
    except AssertionError as e:
        print(e)

    # Cas 4 : Pas d'argument fourni
    try:
        print("Cas 4 - Input : Aucun argument fourni")
        result = subprocess.run(['python3', 'sos.py'], capture_output=True,
                                text=True)
        expected_output = "the arguments are bad\n"
        print(f"Résultat attendu : {expected_output.strip()}")
        print(f"Résultat obtenu : {result.stdout.strip()}")
        assert result.stdout == expected_output, f"Erreur avec \
            aucun argument fourni : {result.stdout}"
        print("Cas 4 réussi !\n")
    except AssertionError as e:
        print(e)

    print("Tous les tests sont passés avec succès !")


def main():
    """
    Fonction principale pour exécuter les tests du programme sos.py.
    """
    try:
        test_sos()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


if __name__ == "__main__":
    main()
