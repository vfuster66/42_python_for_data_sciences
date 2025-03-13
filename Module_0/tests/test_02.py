import unittest
import io
import sys
from ex02.find_ft_type import all_thing_is_obj
from printer import print_title, print_success


class TestFindFtType(unittest.TestCase):

    def setUp(self):
        print_title("=== Test ➜ Ex02 all_thing_is_obj ===")

    def capture_output(self, func, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_list_type(self):
        output = self.capture_output(all_thing_is_obj, ["Hello", "tata!"])
        self.assertIn("List", output)
        print_success("✅ ✅ List OK")

    def test_tuple_type(self):
        output = self.capture_output(all_thing_is_obj, ("Hello", "toto!"))
        self.assertIn("Tuple", output)
        print_success("✅ ✅ Tuple OK")

    def test_set_type(self):
        output = self.capture_output(all_thing_is_obj, {"Hello", "tutu!"})
        self.assertIn("Set", output)
        print_success("✅ ✅ Set OK")

    def test_dict_type(self):
        output = self.capture_output(all_thing_is_obj, {"Hello": "titi!"})
        self.assertIn("Dict", output)
        print_success("✅ ✅ Dict OK")

    def test_str_type(self):
        output = self.capture_output(all_thing_is_obj, "Brian")
        self.assertIn("Brian is in the kitchen", output)
        print_success("✅ ✅ String OK")

    def test_unknown_type(self):
        output = self.capture_output(all_thing_is_obj, 10)
        self.assertIn("Type not found", output)
        print_success("✅ ✅ Unknown type OK")

    def test_return_value(self):
        ret = all_thing_is_obj(10)
        self.assertEqual(ret, 42)
        print_success("✅ ✅ Return value OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
