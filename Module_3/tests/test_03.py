import unittest
from ex03.ft_calculator import calculator
from printer import print_title, print_info, print_success


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé\n")

    def test_add(self):
        print_title("Test ➜ Addition (+ scalar)")
        v = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        result = v + 5
        self.assertEqual(result, [5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
        print_success("Addition OK ✅")

    def test_mul(self):
        print_title("Test ➜ Multiplication (* scalar)")
        v = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        result = v * 5
        self.assertEqual(result, [0.0, 5.0, 10.0, 15.0, 20.0, 25.0])
        print_success("Multiplication OK ✅")

    def test_sub(self):
        print_title("Test ➜ Subtraction (- scalar)")
        v = calculator([10.0, 15.0, 20.0])
        result = v - 5
        self.assertEqual(result, [5.0, 10.0, 15.0])
        print_success("Subtraction OK ✅")

    def test_truediv(self):
        print_title("Test ➜ Division (/ scalar)")
        v = calculator([10.0, 15.0, 20.0])
        result = v / 5
        self.assertEqual(result, [2.0, 3.0, 4.0])
        print_success("Division OK ✅")

    def test_division_by_zero(self):
        print_title("Test ➜ Division by Zero (/ 0)")
        v = calculator([10.0, 15.0, 20.0])
        with self.assertRaises(ZeroDivisionError):
            v / 0
        print_success("ZeroDivisionError raised ✅")


if __name__ == "__main__":
    unittest.main(verbosity=2)
