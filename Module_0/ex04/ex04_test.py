import re
import subprocess


def test_whatis():
    print("\nTest du script whatis.py")

    # Cas 1 : Nombre pair
    print("\n--- Cas 1 : Test avec un nombre pair (14) ---")
    result = subprocess.run(
        ['python3', 'whatis.py', '14'], capture_output=True, text=True
    )
    print(f"Sortie obtenue : {result.stdout.strip()}")
    assert result.stdout.strip() == "I'm Even.", (
        f"Erreur avec un nombre pair : {result.stdout}"
    )

    # Cas 2 : Nombre impair
    print("\n--- Cas 2 : Test avec un nombre impair (-5) ---")
    result = subprocess.run(
        ['python3', 'whatis.py', '-5'], capture_output=True, text=True
    )
    print(f"Sortie obtenue : {result.stdout.strip()}")
    assert result.stdout.strip() == "I'm Odd.", (
        f"Erreur avec un nombre impair : {result.stdout}"
    )

    # Cas 3 : Zéro (pair)
    print("\n--- Cas 3 : Test avec zéro (0) ---")
    result = subprocess.run(
        ['python3', 'whatis.py', '0'], capture_output=True, text=True
    )
    print(f"Sortie obtenue : {result.stdout.strip()}")
    assert result.stdout.strip() == "I'm Even.", (
        f"Erreur avec zéro : {result.stdout}"
    )

    # Cas 4 : Aucun argument fourni
    print("\n--- Cas 4 : Aucun argument fourni ---")
    result = subprocess.run(
        ['python3', 'whatis.py'], capture_output=True, text=True
    )
    expected_output = (
        "Usage: python whatis.py <number>\nno argument is provided"
    )
    print(f"Sortie obtenue : {result.stdout.strip()}")
    assert result.stdout.strip() == expected_output, (
        f"Erreur quand aucun argument n'est fourni : {result.stdout}"
    )

    # Cas 5 : Plusieurs arguments fournis
    print("\n--- Cas 5 : Plusieurs arguments fournis (13 et 5) ---")
    result = subprocess.run(
        ['python3', 'whatis.py', '13', '5'], capture_output=True, text=True
    )
    expected_output = (
        "Usage: python whatis.py <number>\n"
        "more than one argument is provided"
    )

    # Remplacer plusieurs espaces par un seul espace dans la sortie
    cleaned_output = re.sub(r'\s+', ' ', result.stdout.strip())
    cleaned_expected = re.sub(r'\s+', ' ', expected_output.strip())

    print(f"Sortie obtenue : {cleaned_output}")
    assert cleaned_output == cleaned_expected, (
        f"Erreur quand plusieurs arguments sont fournis : {result.stdout}"
    )

    # Cas 6 : Argument non entier
    print("\n--- Cas 6 : Argument non entier (Hi!) ---")
    result = subprocess.run(
        ['python3', 'whatis.py', 'Hi!'], capture_output=True, text=True
    )
    print(f"Sortie obtenue : {result.stdout.strip()}")
    assert result.stdout.strip() == "argument is not an integer", (
        f"Erreur avec un argument non entier : {result.stdout}"
    )

    print("\nTous les tests sont passés avec succès !")


if __name__ == "__main__":
    test_whatis()
