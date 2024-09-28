import unittest
from ft_calculator import calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Affiche un message avant chaque test."""
        print(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        """Affiche un message après chaque test."""
        print(f"{self._testMethodName} - Test terminé\n")

    def test_add(self):
        """Test de l'addition d'un scalaire au vecteur."""
        print("Test de l'addition d'un scalaire au vecteur...")
        v = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        result = v + 5
        self.assertEqual(result, [5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

    def test_mul(self):
        """Test de la multiplication du vecteur par un scalaire."""
        print("Test de la multiplication du vecteur par un scalaire...")
        v = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        result = v * 5
        self.assertEqual(result, [0.0, 5.0, 10.0, 15.0, 20.0, 25.0])

    def test_sub(self):
        """Test de la soustraction d'un scalaire au vecteur."""
        print("Test de la soustraction d'un scalaire au vecteur...")
        v = calculator([10.0, 15.0, 20.0])
        result = v - 5
        self.assertEqual(result, [5.0, 10.0, 15.0])

    def test_truediv(self):
        """Test de la division du vecteur par un scalaire."""
        print("Test de la division du vecteur par un scalaire...")
        v = calculator([10.0, 15.0, 20.0])
        result = v / 5
        self.assertEqual(result, [2.0, 3.0, 4.0])

    def test_division_by_zero(self):
        """Test de la division par zéro (devrait lever une exception)."""
        print("Test de la division par zéro...")
        v = calculator([10.0, 15.0, 20.0])
        with self.assertRaises(ZeroDivisionError):
            v / 0


if __name__ == "__main__":
    print("Début des tests pour l'exercice 03\n")
    unittest.main(verbosity=2)
