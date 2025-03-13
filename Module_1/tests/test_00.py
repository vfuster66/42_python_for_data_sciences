import unittest
from ex00.give_bmi import give_bmi, apply_limit
from printer import print_title, print_info, print_success


class TestEx00(unittest.TestCase):

    def setUp(self):
        print_title(f"Test ➜ {self._testMethodName} - Début")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin\n")

    def test_bmi_normal(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        expected = [22.507863455018317, 29.0359168241966]

        print_info("Test ➜ Normal BMI calculation")
        result = give_bmi(height, weight)

        self.assertAlmostEqual(result[0], expected[0], places=5)
        self.assertAlmostEqual(result[1], expected[1], places=5)
        print_success(f"✅ BMI OK : {result}")

    def test_apply_limit(self):
        bmi = [22.5, 29.0]
        limit = 26
        expected = [False, True]

        print_info("Test ➜ apply_limit")
        result = apply_limit(bmi, limit)

        self.assertEqual(result, expected)
        print_success(f"✅ apply_limit OK : {result}")

    def test_different_list_lengths(self):
        height = [2.71, 1.15]
        weight = [165.3]

        print_info("Test ➜ Different list lengths")
        with self.assertRaises(ValueError):
            give_bmi(height, weight)
        print_success("✅ ValueError détectée avec tailles différentes")

    def test_invalid_input(self):
        height = ["two", 1.15]
        weight = [165.3, 38.4]

        print_info("Test ➜ Invalid input types")
        with self.assertRaises(ValueError):
            give_bmi(height, weight)
        print_success("✅ ValueError détectée avec entrée invalide")

    def test_apply_limit_no_limit_exceeded(self):
        bmi = [20.0, 22.5]
        limit = 26
        expected = [False, False]

        print_info("Test ➜ apply_limit sans dépassement")
        result = apply_limit(bmi, limit)

        self.assertEqual(result, expected)
        print_success(f"✅ apply_limit OK : {result}")

    def test_apply_limit_all_above(self):
        bmi = [30.0, 35.5]
        limit = 26
        expected = [True, True]

        print_info("Test ➜ apply_limit tous dépassent")
        result = apply_limit(bmi, limit)

        self.assertEqual(result, expected)
        print_success(f"✅ apply_limit OK : {result}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
