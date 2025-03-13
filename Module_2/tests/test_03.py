import unittest
import os
import pandas as pd
from ex03.aff_multi_stats import display_graph
from ex00.load_csv import load
from printer import print_title, print_info, print_success


class TestEx03(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Fin du test\n")

    def test_load_valid_files(self):
        """Test du chargement des deux fichiers CSV"""
        print_title("Test ➜ Chargement de fichiers valides")

        income_file = "ex03/income_per_person_gdppercapita_ppp_inflation_"
        income_file += "adjusted.csv"
        life_file = "ex03/life_expectancy_years.csv"

        income_data = load(income_file)
        life_data = load(life_file)

        self.assertIsNotNone(income_data, f"{income_file} non chargé.")
        self.assertIsNotNone(life_data, f"{life_file} non chargé.")
        print_success(f"Fichiers chargés : {income_file}, {life_file}")

    def test_file_not_found(self):
        """Test si fichier inexistant est géré"""
        print_title("Test ➜ Fichier CSV inexistant")

        missing_file = "ex03/file_does_not_exist.csv"
        df = load(missing_file)

        self.assertIsNone(df)
        print_success(f"{missing_file} non trouvé comme prévu.")

    def test_missing_column(self):
        """Test si colonne '1900' manquante est gérée"""
        print_title("Test ➜ Colonne manquante")

        income_file = (
            "ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        income_data = load(income_file)

        self.assertIsNotNone(income_data)

        modified_data = income_data.drop(columns=["1900"], errors="ignore")
        self.assertNotIn("1900", modified_data.columns)

        print_success("Colonne '1900' absente comme attendu.")

    def test_graph_generated(self):
        """Test de génération et création du graphique"""
        print_title("Test ➜ Génération du graphique")

        # Préparer des données simulées
        merged_data = pd.DataFrame({
            "country": ["CountryA", "CountryB"],
            "gnp_1900": [3000, 4500],
            "life_expectancy_1900": [40, 50]
        })

        # Désactiver webbrowser.open
        import ex03.aff_multi_stats as stats
        stats.webbrowser.open = lambda x: None

        display_graph(merged_data)

        graph_file = "projection_life_expectancy_1900.png"
        self.assertTrue(
            os.path.exists(graph_file), f"{graph_file} non généré."
        )

        print_success(f"{graph_file} généré avec succès.")

        # Clean-up
        os.remove(graph_file)
        print_info(f"{graph_file} supprimé après test.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
