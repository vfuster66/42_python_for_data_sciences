import unittest
from ex01.array2D import slice_me
from printer import print_title, print_info, print_success


class TestSliceMe(unittest.TestCase):

    def setUp(self):
        print_info(f"\n🔎 {self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin du test")

    def test_slice_normal(self):
        print_title("Test ➜ Découpage normal")
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        expected_result = [
            [1.80, 78.4],
            [2.15, 102.7]
        ]
        result = slice_me(family, 0, 2)
        print_success(f"✅ Résultat obtenu : {result}")
        self.assertEqual(result, expected_result)

    def test_slice_negative_index(self):
        print_title("Test ➜ Découpage avec index négatif")
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        expected_result = [
            [2.15, 102.7]
        ]
        result = slice_me(family, 1, -2)
        print_success(f"✅ Résultat obtenu : {result}")
        self.assertEqual(result, expected_result)

    def test_slice_out_of_bounds(self):
        print_title("Test ➜ Découpage out of bounds")
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        expected_result = [
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        result = slice_me(family, 1, 10)
        print_success(f"✅ Résultat obtenu : {result}")
        self.assertEqual(result, expected_result)

    def test_invalid_structure(self):
        print_title("Test ➜ Structure invalide")
        family = [
            [1.80, 78.4],
            2.15,  # Élément non valide
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        with self.assertRaises(ValueError):
            slice_me(family, 0, 2)
            print_success("✅ ValueError détectée sur structure invalide")


if __name__ == "__main__":
    unittest.main(verbosity=2)
