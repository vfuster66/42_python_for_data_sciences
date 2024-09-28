import os
import pandas as pd
from load_csv import load
import webbrowser
from aff_multi_stats import main as run_projection


def test_load_valid_files():
    """
    Teste si les fichiers CSV valides se chargent correctement.
    """
    print("\n--- Test : Chargement de fichiers CSV valides ---")

    income_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_file = "life_expectancy_years.csv"

    # Charger les fichiers CSV
    income_data = load(income_file)
    life_data = load(life_expectancy_file)

    assert income_data is not None, f"Erreur : Le fichier '{income_file}' n'a pas pu être chargé."
    assert life_data is not None, f"Erreur : Le fichier '{life_expectancy_file}' n'a pas pu être chargé."

    print(f"Test réussi : Les fichiers '{income_file}' et '{life_expectancy_file}' ont été chargés avec succès.")


def test_file_not_found():
    """
    Teste si un message d'erreur est déclenché pour un fichier CSV inexistant.
    """
    print("\n--- Test : Fichier CSV inexistant ---")

    # Charger un fichier inexistant
    missing_file = "fichier_inexistant.csv"
    df = load(missing_file)

    assert df is None, f"Erreur : Le fichier inexistant '{missing_file}' aurait dû déclencher une erreur."
    print(f"Test réussi : Le fichier inexistant '{missing_file}' a déclenché le bon message d'erreur.")


def test_missing_column():
    """
    Teste si le programme gère l'absence de la colonne '1900'.
    """
    print("\n--- Test : Colonne '1900' manquante ---")

    # Charger un fichier valide et supprimer la colonne '1900'
    income_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_data = load(income_file)

    if income_data is not None:
        modified_data = income_data.drop(columns=['1900'], errors='ignore')

        if '1900' not in modified_data.columns:
            print("Test réussi : La colonne '1900' est manquante, comme prévu.")
        else:
            print("Erreur : La colonne '1900' n'a pas été correctement supprimée.")
    else:
        print(f"Erreur : Le fichier '{income_file}' n'a pas pu être chargé.")


def test_graph_generated():
    """
    Teste si le graphique est bien généré et sauvegardé.
    """
    print("\n--- Test : Génération du graphique ---")

    # Exécuter la fonction principale pour générer le graphique
    run_projection()

    # Vérifier que le fichier du graphique a été créé
    graph_file = "projection_life_expectancy_1900.png"
    assert os.path.exists(graph_file), f"Erreur : Le fichier '{graph_file}' n'a pas été créé."

    print(f"Test réussi : Le fichier '{graph_file}' a été généré avec succès.")

    # Ouvrir l'image générée
    webbrowser.open(graph_file)

    # Nettoyage : Supprimer le fichier après le test
    os.remove(graph_file)
    print(f"Fichier '{graph_file}' supprimé après le test.")


def run_tests():
    """
    Exécute tous les tests définis pour l'exercice 03.
    """
    test_load_valid_files()
    test_file_not_found()
    test_missing_column()
    test_graph_generated()


if __name__ == "__main__":
    run_tests()
