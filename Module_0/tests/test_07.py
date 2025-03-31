from ex07.sos import encode_to_morse
from printer import print_title, print_info, print_success, print_failure


def test_encode_to_morse():
    """
    Teste la fonction encode_to_morse avec différents cas d'utilisation.
    """
    print_title("Test ➜ Ex07 sos.py (encode_to_morse)")

    # Cas 1 : texte simple
    input_text = "sos"
    print_info(f"Cas 1 - Input : {input_text}")
    expected_output = "... --- ..."
    result = encode_to_morse(input_text)

    if result == expected_output:
        print_success("✅ Cas 1 OK : sortie conforme")
    else:
        print_failure("❌ Cas 1 FAILED")
        print_failure(f"Résultat obtenu : {result}")
        print_failure(f"Résultat attendu : {expected_output}")
        raise AssertionError(f"Erreur avec '{input_text}'")

    # Cas 2 : texte plus complexe
    input_text = "Hello World"
    print_info(f"Cas 2 - Input : {input_text}")
    expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    result = encode_to_morse(input_text)

    if result == expected_output:
        print_success("✅ Cas 2 OK : sortie conforme")
    else:
        print_failure("❌ Cas 2 FAILED")
        print_failure(f"Résultat obtenu : {result}")
        print_failure(f"Résultat attendu : {expected_output}")
        raise AssertionError(f"Erreur avec '{input_text}'")

    # Cas 3 : caractère invalide
    input_text = "h$llo"
    print_info(f"Cas 3 - Input : {input_text}")
    try:
        result = encode_to_morse(input_text)
        print_failure("❌ Cas 3 FAILED : exception non levée")
        print_failure(f"Résultat obtenu : {result}")
        raise AssertionError("Erreur attendue non levée pour caractère invalide")
    except AssertionError:
        print_success("✅ Cas 3 OK : erreur détectée comme prévu")


def main():
    print_title("EX07 ➜ Tests automatiques (encode_to_morse)")
    try:
        test_encode_to_morse()
        print_success("✅ ✅ Tous les tests sont passés avec succès !")
    except AssertionError as e:
        print_failure(f"❌ Test échoué : {e}")


if __name__ == "__main__":
    main()
