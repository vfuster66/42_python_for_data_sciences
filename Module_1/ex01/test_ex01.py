# test_ex01.py

import unittest
from array2D import slice_me

class TestSliceMe(unittest.TestCase):

    def test_01_slice_normal(self):
        """Test d'un découpage simple dans les limites"""
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
        print("\nTest 1: Découpage normal")
        result = slice_me(family, 0, 2)
        print(f"Expected: {expected_result}")
        print(f"Obtained: {result}")
        self.assertEqual(result, expected_result)

    def test_02_slice_negative_index(self):
        """Test avec un index de fin négatif"""
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        expected_result = [
            [2.15, 102.7]
        ]
        print("\nTest 2: Découpage avec un index négatif")
        result = slice_me(family, 1, -2)
        print(f"Expected: {expected_result}")
        print(f"Obtained: {result}")
        self.assertEqual(result, expected_result)

    def test_03_slice_out_of_bounds(self):
        """Test avec un index de fin hors des limites"""
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
        print("\nTest 3: Découpage hors des limites")
        result = slice_me(family, 1, 10)
        print(f"Expected: {expected_result}")
        print(f"Obtained: {result}")
        self.assertEqual(result, expected_result)

    def test_04_invalid_structure(self):
        """Test avec une structure invalide (éléments non-liste)"""
        family = [
            [1.80, 78.4],
            2.15,  # Élément non valide
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        print("\nTest 4: Structure invalide")
        with self.assertRaises(ValueError):
            slice_me(family, 0, 2)

if __name__ == "__main__":
    unittest.main()
