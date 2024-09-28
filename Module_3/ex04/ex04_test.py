import unittest
from ft_calculator import calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Affiche un message avant chaque test."""
        print(f"\n{self._testMethodName} - Début du test")

    def tearDown(self):
        """Affiche un message après chaque test."""
        print(f"{self._testMethodName} - Test terminé")

    def test_dot_product(self):
        """Test du produit scalaire de deux vecteurs."""
        print("Test du produit scalaire...")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.dotproduct(a, b)
        expected = 56.0
        print(f"Attendu: {expected}, Obtenu: {result}")
        self.assertEqual(result, expected)

    def test_add_vec(self):
        """Test de l'addition de deux vecteurs."""
        print("Test de l'addition de deux vecteurs...")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.add_vec(a, b)
        expected = [7.0, 14.0, 5.0]
        print(f"Attendu: {expected}, Obtenu: {result}")
        self.assertEqual(result, expected)

    def test_sous_vec(self):
        """Test de la soustraction de deux vecteurs."""
        print("Test de la soustraction de deux vecteurs...")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.sous_vec(a, b)
        expected = [3.0, 6.0, -1.0]
        print(f"Attendu: {expected}, Obtenu: {result}")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    print("Début des tests pour l'exercice 04\n")
    unittest.main(verbosity=2)
