import unittest
from ex04.ft_calculator import calculator
from printer import print_title, print_info, print_success


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé\n")

    def test_dot_product(self):
        print_title("Test ➜ Ex04 dotproduct()")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.dotproduct(a, b)
        expected = 56.0
        self.assertEqual(result, expected)
        print_success(
            f"Dot product OK ✅ | Expected: {expected} | Got: {result}"
        )

    def test_add_vec(self):
        print_title("Test ➜ Ex04 add_vec()")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.add_vec(a, b)
        expected = [7.0, 14.0, 5.0]
        self.assertEqual(result, expected)
        print_success(
            f"Add vectors OK ✅ | Expected: {expected} | Got: {result}"
        )

    def test_sous_vec(self):
        print_title("Test ➜ Ex04 sous_vec()")
        a = [5, 10, 2]
        b = [2, 4, 3]
        result = calculator.sous_vec(a, b)
        expected = [3.0, 6.0, -1.0]
        self.assertEqual(result, expected)
        print_success(
            f"Sous vectors OK ✅ | Expected: {expected} | Got: {result}"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
