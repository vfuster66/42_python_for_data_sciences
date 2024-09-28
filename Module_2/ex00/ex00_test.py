import os
from load_csv import load


def test_load_csv_valid_file():
    """
    Teste le chargement d'un fichier CSV valide et vérifie les dimensions.
    """
    print("\n--- Test : Chargement d'un fichier CSV valide ---")

    # Chemin vers un fichier CSV valide
    valid_csv_path = "life_expectancy_years.csv"

    # Charger le fichier
    df = load(valid_csv_path)

    if df is not None:
        print("Test réussi : Le dataset a été chargé avec succès.")
        # Vérification des dimensions attendues
        assert df.shape == (195, 302), (
            "Les dimensions du dataset sont incorrectes."
        )
        print(f"Dimensions vérifiées : {df.shape}")
    else:
        print("Erreur : Le dataset n'a pas pu être chargé.")


def test_load_csv_non_existent_file():
    """
    Teste le chargement d'un fichier CSV inexistant.
    """
    print("\n--- Test : Chargement d'un fichier CSV inexistant ---")

    # Chemin vers un fichier inexistant
    non_existent_csv_path = "fichier_inexistant.csv"

    # Charger le fichier
    df = load(non_existent_csv_path)

    assert df is None, (
        "Erreur : Le fichier inexistant n'a pas déclenché le bon message."
    )
    print("Test réussi : Le fichier inexistant a déclenché le bon message.")


def test_load_csv_empty_file():
    """
    Teste le chargement d'un fichier CSV vide ou mal formaté.
    """
    print("\n--- Test : Chargement d'un fichier CSV vide ou mal formaté ---")

    # Créer un fichier vide pour le test
    empty_csv_path = "fichier_vide.csv"
    with open(empty_csv_path, "w") as f:
        f.write("")

    # Charger le fichier vide
    df = load(empty_csv_path)

    assert df is None, (
        "Erreur : Le fichier vide n'a pas déclenché le bon message d'erreur."
    )
    print("Test réussi : Le fichier vide a déclenché le bon message.")

    # Nettoyer le fichier vide après le test
    if os.path.exists(empty_csv_path):
        os.remove(empty_csv_path)


def run_tests():
    """
    Exécute tous les tests définis pour l'exercice 00.
    """
    test_load_csv_valid_file()
    test_load_csv_non_existent_file()
    test_load_csv_empty_file()


if __name__ == "__main__":
    run_tests()
