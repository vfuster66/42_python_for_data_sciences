

import subprocess

def test_building():
    # Cas 1 : Texte fourni en argument
    input_text_1 = "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
    result = subprocess.run(['python3', 'building.py', input_text_1], capture_output=True, text=True)
    expected_output = (
        "The text contains 171 characters:\n"
        "2 upper letters\n"
        "121 lower letters\n"
        "8 punctuation marks\n"
        "25 spaces\n"
        "15 digits\n"
    )
    print(f"Cas 1 - Input passé en argument :\n{input_text_1}")
    print(f"Cas 1 - Résultat obtenu :\n{result.stdout}")
    assert result.stdout == expected_output, f"Erreur avec texte fourni : {result.stdout}"

    # Cas 2 : Aucun argument fourni, la chaîne sera saisie via input()
    input_text_2 = "Python 3.0, released in 2008..."
    result = subprocess.run(['python3', 'building.py'], input=input_text_2, capture_output=True, text=True)
    print(f"Cas 2 - Aucune chaîne passée en argument, la chaîne suivante a été saisie via input() :\n{input_text_2}")
    print(f"Cas 2 - Résultat obtenu :\n{result.stdout}")
    assert "The text contains" in result.stdout, f"Erreur avec aucun argument : {result.stdout}"

    # Cas 3 : Plusieurs arguments fournis
    input_text_3 = ['Test', 'Another', 'Third']
    result = subprocess.run(['python3', 'building.py', *input_text_3], capture_output=True, text=True)
    print(f"Cas 3 - Plusieurs arguments fournis :\n{', '.join(input_text_3)}")
    print(f"Cas 3 - Résultat obtenu :\n{result.stdout}")
    assert "Please provide only one argument." in result.stdout, f"Erreur avec plusieurs arguments : {result.stdout}"

    print("Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_building()
