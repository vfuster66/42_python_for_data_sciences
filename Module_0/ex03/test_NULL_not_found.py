import subprocess

def test_NULL_not_found():
    # Exécuter le script tester.py
    result = subprocess.run(['python3', 'tester.py'], capture_output=True, text=True)
    
    # Séparer les lignes du résultat pour analyse
    lines = result.stdout.strip().split('\n')

    # Sortie attendue
    expected_output = [
        "Nothing: None <class 'NoneType'>",
        "Cheese: nan <class 'float'>",
        "Zero: 0 <class 'int'>",
        "Empty:  <class 'str'>",
        "Fake: False <class 'bool'>",
        "Type not Found",
        "1"
    ]

    # Comparer chaque ligne de sortie avec la sortie attendue
    for i in range(len(expected_output)):
        assert lines[i] == expected_output[i], f"Erreur : sortie incorrecte à la ligne {i + 1}. Attendu : {expected_output[i]}, Reçu : {lines[i]}"

    # Test supplémentaire pour vérifier l'exécution de NULL_not_found.py seul
    result_null_not_found = subprocess.run(['python3', 'NULL_not_found.py'], capture_output=True, text=True)
    
    # Il ne devrait y avoir aucune sortie pour NULL_not_found.py exécuté seul
    assert result_null_not_found.stdout == "", "Erreur : NULL_not_found.py ne doit pas produire de sortie lorsqu'il est exécuté seul"

    print("Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_NULL_not_found()
