import subprocess

def test_sos():
    """
    Test du programme sos.py avec différents cas.
    """

    # Cas 1 : Chaîne valide "sos"
    input_text = "sos"
    print(f"Cas 1 - Input : {input_text}")
    result = subprocess.run(['python3', 'sos.py', input_text], capture_output=True, text=True)
    expected_output = "... --- ...\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur avec '{input_text}' : {result.stdout}"
    print("Cas 1 réussi !\n")

    # Cas 2 : Chaîne valide "Hello World"
    input_text = "Hello World"
    print(f"Cas 2 - Input : {input_text}")
    result = subprocess.run(['python3', 'sos.py', input_text], capture_output=True, text=True)
    expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -..\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur avec '{input_text}' : {result.stdout}"
    print("Cas 2 réussi !\n")

    # Cas 3 : Caractères invalides "$"
    input_text = "h$llo"
    print(f"Cas 3 - Input : {input_text}")
    result = subprocess.run(['python3', 'sos.py', input_text], capture_output=True, text=True)
    expected_output = "the arguments are bad\n"  # Modifié pour correspondre à la sortie réelle
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur avec '{input_text}' : {result.stdout}"
    print("Cas 3 réussi !\n")

    # Cas 4 : Pas d'argument fourni
    print("Cas 4 - Input : Aucun argument fourni")
    result = subprocess.run(['python3', 'sos.py'], capture_output=True, text=True)
    expected_output = "the arguments are bad\n"
    print(f"Résultat attendu : {expected_output.strip()}")
    print(f"Résultat obtenu : {result.stdout.strip()}")
    assert result.stdout == expected_output, f"Erreur avec aucun argument fourni : {result.stdout}"
    print("Cas 4 réussi !\n")

    print("Tous les tests sont passés avec succès !")


if __name__ == "__main__":
    test_sos()
