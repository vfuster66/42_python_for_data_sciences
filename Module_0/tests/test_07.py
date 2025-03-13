from ex07.sos import morse_runner
from printer import print_title, print_info, print_success, print_failure


def test_morse_runner():
    """
    Teste la fonction morse_runner avec différents cas d'utilisation.
    """
    print_title("Test ➜ sos.py (morse_runner)")

    # Cas 1 : texte simple
    input_text = "sos"
    print_info(f"Cas 1 - Input : {input_text}")
    expected_output = "... --- ..."
    result = morse_runner(input_text)

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
    result = morse_runner(input_text)

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
    result = morse_runner(input_text)

    if result == "":
        print_success("✅ Cas 3 OK : erreur détectée comme prévu")
    else:
        print_failure("❌ Cas 3 FAILED : résultat inattendu")
        print_failure(f"Résultat obtenu : {result}")
        raise AssertionError(
            f"Erreur avec '{input_text}' (caractère invalide)"
        )


def main():
    print_title("EX07 ➜ Tests automatiques (morse_runner)")
    try:
        test_morse_runner()
        print_success("✅ ✅ Tous les tests sont passés avec succès !")
    except AssertionError as e:
        print_failure(f"❌ Test échoué : {e}")


if __name__ == "__main__":
    main()
