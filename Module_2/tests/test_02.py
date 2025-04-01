import unittest
import os
from ex00.load_csv import load
from ex02.aff_stats import plot_population
from printer import print_title, print_info, print_success


class TestEx02(unittest.TestCase):
    def setUp(self):
        print_title(self._testMethodName + " - Début du test")

    def tearDown(self):
        print_info(self._testMethodName + " - Test terminé\n")

    def test_valid_countries(self):
        """Test avec deux pays valides"""
        data = load("ex02/population_total.csv")
        self.assertIsNotNone(data, "Le fichier CSV est introuvable")

        country1, country2 = "France", "Belgium"
        filename = os.path.join(
            "ex02", f"population_{country1}_{country2}.png"
        )

        plot_population(country1, country2, data)

        self.assertTrue(
            os.path.exists(filename), f"{filename} n'a pas été créé"
        )
        print_success(f"Graphique créé : {filename}")
        os.remove(filename)

    def test_invalid_country(self):
        """Test avec un pays inexistant"""
        data = load("ex02/population_total.csv")
        self.assertIsNotNone(data, "Le fichier CSV est introuvable")

        country1, country2 = "France", "Atlantis"
        # Modifier le chemin du fichier ici aussi
        filename = os.path.join(
            "ex02", f"population_{country1}_{country2}.png"
        )

        plot_population(country1, country2, data)

        self.assertFalse(
            os.path.exists(filename), f"{filename} ne devrait pas être créé"
        )
        print_success("Aucun graphique créé pour pays inexistant")

    def test_missing_csv(self):
        """Test avec un fichier CSV inexistant"""
        data = load("ex02/fichier_inexistant.csv")
        self.assertIsNone(
            data, "Dataset chargé alors que le fichier est inexistant"
        )
        print_success("Fichier inexistant géré correctement")


if __name__ == "__main__":
    unittest.main(verbosity=2)
