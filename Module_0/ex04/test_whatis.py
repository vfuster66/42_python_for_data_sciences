

import subprocess

def test_whatis():
    # Cas 1 : Nombre pair
    result = subprocess.run(['python3', 'whatis.py', '14'], capture_output=True, text=True)
    assert result.stdout.strip() == "I'm Even.", f"Erreur avec un nombre pair : {result.stdout}"

    # Cas 2 : Nombre impair
    result = subprocess.run(['python3', 'whatis.py', '-5'], capture_output=True, text=True)
    assert result.stdout.strip() == "I'm Odd.", f"Erreur avec un nombre impair : {result.stdout}"

    # Cas 3 : Zéro (pair)
    result = subprocess.run(['python3', 'whatis.py', '0'], capture_output=True, text=True)
    assert result.stdout.strip() == "I'm Even.", f"Erreur avec zéro : {result.stdout}"

    # Cas 4 : Aucun argument fourni
    result = subprocess.run(['python3', 'whatis.py'], capture_output=True, text=True)
    expected_output = "Usage: python whatis.py <number>\nno argument is provided"
    assert result.stdout.strip() == expected_output, f"Erreur quand aucun argument n'est fourni : {result.stdout}"

    # Cas 5 : Plusieurs arguments fournis
    result = subprocess.run(['python3', 'whatis.py', '13', '5'], capture_output=True, text=True)
    expected_output = "Usage: python whatis.py <number>\nmore than one argument is provided"
    assert result.stdout.strip() == expected_output, f"Erreur quand plusieurs arguments sont fournis : {result.stdout}"

    # Cas 6 : Argument non entier
    result = subprocess.run(['python3', 'whatis.py', 'Hi!'], capture_output=True, text=True)
    assert result.stdout.strip() == "argument is not an integer", f"Erreur avec un argument non entier : {result.stdout}"

    print("Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_whatis()
