import unittest
import io
import sys
from ex03.NULL_not_found import NULL_not_found
from printer import print_title, print_success


class TestNULLNotFound(unittest.TestCase):

    def setUp(self):
        print_title("=== Test ➜ Ex03 NULL_not_found ===")

    def capture_output(self, func, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_none(self):
        output = self.capture_output(NULL_not_found, None)
        self.assertIn("Nothing", output)
        print_success("✅ ✅ None OK")

    def test_nan(self):
        output = self.capture_output(NULL_not_found, float('NaN'))
        self.assertIn("Cheese", output)
        print_success("✅ ✅ NaN OK")

    def test_zero(self):
        output = self.capture_output(NULL_not_found, 0)
        self.assertIn("Zero", output)
        print_success("✅ ✅ Zero OK")

    def test_empty_string(self):
        output = self.capture_output(NULL_not_found, '')
        self.assertIn("Empty", output)
        print_success("✅ ✅ Empty String OK")

    def test_false(self):
        output = self.capture_output(NULL_not_found, False)
        self.assertIn("Fake", output)
        print_success("✅ ✅ False OK")

    def test_unknown_type(self):
        output = self.capture_output(NULL_not_found, "Brian")
        self.assertIn("Type not Found", output)
        print_success("✅ ✅ Unknown Type OK")

    def test_return_value(self):
        ret = NULL_not_found("Brian")
        self.assertEqual(ret, 1)
        ret = NULL_not_found(None)
        self.assertEqual(ret, 0)
        print_success("✅ ✅ Return Values OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
