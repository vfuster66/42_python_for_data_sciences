import os
from load_csv import load
from aff_life import display_life_expectancy


def test_load_csv():
    """
    Teste le chargement du fichier CSV et vérifie ses dimensions.
    """
    print("\n--- Test : Chargement du fichier CSV ---")

    # Charger le fichier
    data = load("life_expectancy_years.csv")

    # Vérifier si le fichier a été chargé correctement
    if data is not None:
        print("Test réussi : Le dataset a été chargé avec succès.")
        # Vérification des dimensions attendues
        assert data.shape == (195, 302), \
            "Les dimensions du dataset sont incorrectes."
        print(f"Dimensions vérifiées : {data.shape}")
    else:
        print("Erreur : Le dataset n'a pas pu être chargé.")


def test_display_life_expectancy():
    """
    Teste l'affichage de l'espérance de vie et la sauvegarde du graphique.
    """
    print("\n--- Test : Affichage de l'espérance de vie ---")

    # Charger le fichier CSV
    data = load("life_expectancy_years.csv")
    if data is None:
        print("Erreur lors du chargement des données.")
        return

    # Choisir un pays pour le test
    country = "France"

    # Appeler la fonction pour afficher et sauvegarder le graphique
    display_life_expectancy(country, data)

    # Vérifier si le fichier graphique a été créé
    filename = f"life_expectancy_{country}.png"
    if os.path.exists(filename):
        print(f"Test réussi : Le fichier '{filename}' a été créé avec succès.")
        os.remove(filename)  # Supprimer le fichier après le test
    else:
        print(f"Erreur : Le fichier '{filename}' n'a pas été créé.")


def test_country_not_in_dataset():
    """
    Teste le comportement lorsque le pays n'existe pas dans le dataset.
    """
    print("\n--- Test : Pays inexistant dans le dataset ---")

    # Charger le fichier CSV
    data = load("life_expectancy_years.csv")
    if data is None:
        print("Erreur lors du chargement des données.")
        return

    # Choisir un pays qui n'existe pas dans le dataset
    country = "Narnia"

    # Appeler la fonction pour afficher et sauvegarder le graphique
    display_life_expectancy(country, data)

    # Vérifier qu'aucun fichier graphique n'a été créé
    filename = f"life_expectancy_{country}.png"
    if os.path.exists(filename):
        print(f"Erreur : Le fichier '{filename}' ne devrait pas etre créé.")
    else:
        print("Test réussi : Aucun fichier créé pour un pays inexistant.")


def test_csv_file_not_found():
    """
    Teste le comportement lorsque le fichier CSV est introuvable.
    """
    print("\n--- Test : Fichier CSV introuvable ---")

    # Renommer temporairement le fichier CSV pour simuler l'absence
    if os.path.exists("life_expectancy_years.csv"):
        os.rename("life_expectancy_years.csv",
                  "life_expectancy_years_backup.csv")

    # Tenter de charger un fichier CSV inexistant
    data = load("life_expectancy_years.csv")

    # Vérifier que le chargement a échoué
    if data is None:
        print("Test réussi : Le fichier CSV manquant a déclenché une erreur.")
    else:
        print("Erreur : Le fichier CSV manquant n'a pas déclenché la bonne "
              "erreur.")

    # Restaurer le fichier CSV après le test
    if os.path.exists("life_expectancy_years_backup.csv"):
        os.rename("life_expectancy_years_backup.csv",
                  "life_expectancy_years.csv")


def run_tests():
    """
    Exécute tous les tests définis pour l'exercice 01.
    """
    test_load_csv()
    test_display_life_expectancy()
    test_country_not_in_dataset()
    test_csv_file_not_found()


if __name__ == "__main__":
    run_tests()
