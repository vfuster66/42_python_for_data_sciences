import subprocess

def test_find_ft_type():
    # Exécuter le script tester.py
    result = subprocess.run(['python3', 'tester.py'], capture_output=True, text=True)
    
    # Vérifier si la sortie est vide
    if not result.stdout:
        raise AssertionError("Erreur : Aucune sortie obtenue du script tester.py")

    # Séparer les lignes du résultat pour analyse
    lines = result.stdout.strip().split('\n')

    # Sortie attendue
    expected_output = [
        "List : <class 'list'>",
        "Tuple : <class 'tuple'>",
        "Set : <class 'set'>",
        "Dict : <class 'dict'>",
        "Brian is in the kitchen : <class 'str'>",
        "Toto is in the kitchen : <class 'str'>",
        "Type not found",
        "42"
    ]

    # Afficher les résultats obtenus avant comparaison
    print("\n--- Résultat obtenu : ---")
    for idx, line in enumerate(lines):
        print(f"Ligne {idx + 1}: {line}")

    # Vérifier que la longueur des résultats correspond à celle attendue
    assert len(lines) == len(expected_output), (
        f"Erreur : nombre de lignes inattendu. Attendu : {len(expected_output)}, Reçu : {len(lines)}"
    )

    # Comparer chaque ligne de sortie avec la sortie attendue
    for i in range(len(expected_output)):
        print(f"\nComparaison ligne {i + 1}...")
        print(f"Attendu : {expected_output[i]}")
        print(f"Reçu : {lines[i]}")
        assert lines[i] == expected_output[i], (
            f"Erreur : sortie incorrecte à la ligne {i + 1}. "
            f"Attendu : {expected_output[i]}, Reçu : {lines[i]}"
        )

    # Test supplémentaire pour vérifier l'exécution de find_ft_type.py seul
    result_find_ft_type = subprocess.run(['python3', 'find_ft_type.py'], capture_output=True, text=True)

    # Vérifier qu'il n'y a pas de sortie pour find_ft_type.py exécuté seul
    assert result_find_ft_type.stdout == "", (
        "Erreur : find_ft_type.py ne doit pas produire de sortie lorsqu'il est exécuté seul"
    )

    print("\nTous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_find_ft_type()
