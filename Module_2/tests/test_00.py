import unittest
import os
from ex00.load_csv import load
from printer import print_title, print_info, print_success


class TestLoadCSV(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé\n")

    def test_valid_file(self):
        print_title("Test ➜ Chargement CSV valide")
        path = "ex00/life_expectancy_years.csv"
        df = load(path)
        self.assertIsNotNone(df)
        self.assertEqual(df.shape, (195, 302))
        print_success(f"Chargement OK ✅ avec shape {df.shape}")

    def test_file_not_found(self):
        print_title("Test ➜ Fichier inexistant")
        path = "ex00/fichier_inexistant.csv"
        df = load(path)
        self.assertIsNone(df)
        print_success("Fichier inexistant géré ✅")

    def test_empty_file(self):
        print_title("Test ➜ Fichier vide")
        path = "ex00/fichier_vide.csv"

        # Création d'un fichier vide
        open(path, "w").close()

        df = load(path)
        self.assertIsNone(df)
        print_success("Fichier vide géré ✅")

        # Suppression
        os.remove(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
