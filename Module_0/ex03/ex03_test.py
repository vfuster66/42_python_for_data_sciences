import subprocess


def test_NULL_not_found():
    print("\nTest du script tester.py")

    # Exécuter le script tester.py
    print("\nExécution du script tester.py...")
    result = subprocess.run(
        ['python3', 'tester.py'], capture_output=True, text=True
    )

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

    # Afficher les résultats attendus et obtenus en blocs séparés
    print("\n--- Sortie attendue ---")
    for expected in expected_output:
        print(expected)

    print("\n--- Sortie obtenue ---")
    for line in lines:
        print(line)

    # Comparaison des lignes
    success = True  # Flag pour vérifier si tout est correct
    for i in range(len(expected_output)):
        if lines[i] != expected_output[i]:
            success = False
            print(
                f"\nErreur à la ligne {i + 1} : "
                f"Attendu : {expected_output[i]} | Reçu : {lines[i]}"
            )

    if success:
        print("\nToutes les sorties correspondent : OK")
    else:
        print("\nUne ou plusieurs lignes ne correspondent pas : FAILED")

    # Test supplémentaire pour vérifier l'exécution de NULL_not_found.py seul
    print("\nTest de NULL_not_found.py exécuté seul...")
    result_null_not_found = subprocess.run(
        ['python3', 'NULL_not_found.py'], capture_output=True, text=True
    )

    # Il ne devrait y avoir aucune sortie pour NULL_not_found.py exécuté seul
    if result_null_not_found.stdout.strip() == "":
        print("Test pour NULL_not_found.py seul : OK")
    else:
        print(
            "Erreur : NULL_not_found.py ne doit pas produire de sortie "
            "lorsqu'il est exécuté seul. Sortie obtenue : "
            f"{result_null_not_found.stdout}"
        )


if __name__ == "__main__":
    test_NULL_not_found()
