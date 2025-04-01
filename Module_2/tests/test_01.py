import unittest
import os
from ex01.aff_life import display_life_expectancy
from ex00.load_csv import load
from printer import print_title, print_info, print_success


class TestAffLife(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")
        self.csv_path = "ex01/life_expectancy_years.csv"
        self.data = load(self.csv_path)

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé\n")

    def test_valid_country_graph(self):
        print_title("Test ➜ Affichage France (valide)")
        country = "France"
        display_life_expectancy(country, self.data)

        filename = os.path.join("ex01", f"life_expectancy_{country}.png")
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)
        print_success("✅ Graphique France généré et supprimé ✅")

    def test_invalid_country(self):
        print_title("Test ➜ Pays inexistant (Narnia)")
        country = "Narnia"
        display_life_expectancy(country, self.data)

        filename = f"life_expectancy_{country}.png"
        self.assertFalse(os.path.exists(filename))
        print_success("Aucun graphique généré pour pays inexistant")

    def test_csv_file_not_found(self):
        print_title("Test ➜ CSV non trouvé")
        backup = self.csv_path + ".bak"

        os.rename(self.csv_path, backup)

        data = load(self.csv_path)
        self.assertIsNone(data)
        print_success("Erreur détectée avec fichier manquant")

        os.rename(backup, self.csv_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
