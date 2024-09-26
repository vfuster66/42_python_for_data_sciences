# test_ex00.py

import unittest
from give_bmi import give_bmi, apply_limit


class TestEx00(unittest.TestCase):

    def test_01_bmi_normal(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        expected_bmi = [22.507863455018317, 29.0359168241966]
        print("\nTest 1: Normal BMI calculation")
        print(f"Height: {height}, Weight: {weight}")
        print(f"Expected BMI: {expected_bmi}")
        result = give_bmi(height, weight)
        print(f"Obtained BMI: {result}")
        self.assertAlmostEqual(result, expected_bmi, places=5)

    def test_02_apply_limit(self):
        bmi = [22.507863455018317, 29.0359168241966]
        limit = 26
        expected = [False, True]
        print("\nTest 2: Applying limit to BMI")
        print(f"BMI: {bmi}, Limit: {limit}")
        print(f"Expected Result: {expected}")
        result = apply_limit(bmi, limit)
        print(f"Obtained Result: {result}")
        self.assertEqual(result, expected)

    def test_03_different_list_lengths(self):
        height = [2.71, 1.15]
        weight = [165.3]
        print("\nTest 3: Error when lists have different lengths")
        print(f"Height: {height}, Weight: {weight}")
        print("Expected: ValueError")
        try:
            give_bmi(height, weight)
        except ValueError as e:
            print(f"Obtained: ValueError - {str(e)}")
            self.assertTrue(True)

    def test_04_invalid_input(self):
        height = ["two", 1.15]
        weight = [165.3, 38.4]
        print("\nTest 4: Error with invalid input types")
        print(f"Height: {height}, Weight: {weight}")
        print("Expected: TypeError")
        try:
            give_bmi(height, weight)
        except TypeError as e:
            print(f"Obtained: TypeError - {str(e)}")
            self.assertTrue(True)

    def test_05_apply_limit_no_limit_exceeded(self):
        bmi = [20.0, 22.5]
        limit = 26
        expected = [False, False]
        print("\nTest 5: Applying limit - No BMI exceeds limit")
        print(f"BMI: {bmi}, Limit: {limit}")
        print(f"Expected Result: {expected}")
        result = apply_limit(bmi, limit)
        print(f"Obtained Result: {result}")
        self.assertEqual(result, expected)

    def test_06_apply_limit_all_above(self):
        bmi = [30.0, 35.5]
        limit = 26
        expected = [True, True]
        print("\nTest 6: Applying limit - All BMI exceed limit")
        print(f"BMI: {bmi}, Limit: {limit}")
        print(f"Expected Result: {expected}")
        result = apply_limit(bmi, limit)
        print(f"Obtained Result: {result}")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
