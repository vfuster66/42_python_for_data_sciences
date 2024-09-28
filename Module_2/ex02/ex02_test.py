import os
from load_csv import load
from aff_stats import plot_population


def test_valid_countries():
    """
    Teste la génération d'un graphique pour deux pays valides.
    """
    print("\n--- Test : Génération d'un graphique pour des pays valides ---")
    data = load("population_total.csv")
    if data is None:
        print("Erreur : Le fichier CSV est introuvable ou mal formaté.")
        return

    country1 = "France"
    country2 = "Belgium"

    plot_population(country1, country2, data)

    # Vérifier que le fichier a été créé
    filename = f"population_{country1}_{country2}.png"
    if os.path.exists(filename):
        print(f"Test réussi : Le fichier '{filename}' a été créé avec succès.")
    else:
        print(f"Erreur : Le fichier '{filename}' n'a pas été créé.")

    # Supprimer le fichier après le test
    if os.path.exists(filename):
        os.remove(filename)


def test_invalid_country():
    """
    Teste la gestion d'un pays inexistant dans le dataset.
    """
    print("\n--- Test : Gestion d'un pays inexistant ---")
    data = load("population_total.csv")
    if data is None:
        print("Erreur : Le fichier CSV est introuvable ou mal formaté.")
        return

    country1 = "France"
    country2 = "Atlantis"  # Pays inexistant

    plot_population(country1, country2, data)

    # Pas de fichier créé pour un pays inexistant
    filename = f"population_{country1}_{country2}.png"
    if not os.path.exists(filename):
        print("Test réussi : Aucun fichier créé pour un pays inexistant.")
    else:
        print(f"Erreur : Fichier '{filename}' créé alors que pays inexistant.")
        # Supprimer le fichier s'il a été créé par erreur
        if os.path.exists(filename):
            os.remove(filename)


def test_missing_csv():
    """
    Teste le comportement lorsque le fichier CSV est introuvable.
    """
    print("\n--- Test : Fichier CSV introuvable ---")

    try:
        # Charger un fichier inexistant
        data = load("fichier_inexistant.csv")
        if data is None:
            print("Test réussi : Le fichier n'existe pas.")
        else:
            print("Erreur : Dataset chargé alors que le fichier n'existe pas.")
    except Exception as e:
        print(f"Erreur lors du test : {e}")


def run_tests():
    """
    Exécute tous les tests définis pour l'exercice 02.
    """
    test_valid_countries()
    test_invalid_country()
    test_missing_csv()


if __name__ == "__main__":
    run_tests()
