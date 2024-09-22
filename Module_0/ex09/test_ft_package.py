import unittest
import subprocess
from ft_package import count_in_list

class TestFtPackage(unittest.TestCase):
    
    def test_count_in_list(self):
        # Cas 1 : L'élément est présent plusieurs fois
        print("Cas 1: Élément 'toto' présent plusieurs fois dans la liste ['toto', 'tata', 'toto']")
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "toto"), 2, "Erreur dans le comptage des occurrences multiples")

        # Cas 2 : L'élément n'est pas présent
        print("Cas 2: Élément 'tutu' non présent dans la liste ['toto', 'tata', 'toto']")
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "tutu"), 0, "Erreur dans le cas où l'élément est absent")
        
        # Cas 3 : L'élément est présent une seule fois
        print("Cas 3: Élément 'tutu' présent une fois dans la liste ['toto', 'tata', 'tutu']")
        self.assertEqual(count_in_list(["toto", "tata", "tutu"], "tutu"), 1, "Erreur dans le comptage de l'occurrence unique")
        
        # Cas 4 : Liste vide
        print("Cas 4: Liste vide")
        self.assertEqual(count_in_list([], "toto"), 0, "Erreur dans le cas d'une liste vide")
        
        # Cas 5 : Elément non string
        print("Cas 5: Élément numérique dans la liste [1, 2, 2, 3]")
        self.assertEqual(count_in_list([1, 2, 2, 3], 2), 2, "Erreur dans le comptage des éléments non string")
        self.assertEqual(count_in_list([1, 2, 2, 3], 4), 0, "Erreur dans le cas où l'élément non string est absent")

class TestFtPackageInstallation(unittest.TestCase):
    
    def test_package_installed(self):
        print("Vérification que 'ft_package' est installé.")
        result = subprocess.run(['pip', 'show', 'ft_package'], capture_output=True, text=True)
        self.assertIn("ft_package", result.stdout, "Le package 'ft_package' n'est pas installé.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
