import unittest
from ex00.Hello import display_hello
from printer import print_title, print_success, print_failure


class TestHello(unittest.TestCase):

    def setUp(self):
        print_title("=== Test ➜ Ex00 First Python Script ===")

    def test_display_hello(self):
        """Test les modifications de données dans Hello.py"""

        expected_list = ['Hello', 'World!']
        expected_tuple = ('Hello', 'France!')
        expected_set = ['Hello', 'Perpignan!']
        expected_dict = {'Hello': '42Perpignan!'}

        result_list, result_tuple, result_set, result_dict = display_hello()

        try:
            self.assertEqual(result_list, expected_list)
            self.assertEqual(result_tuple, expected_tuple)
            self.assertEqual(result_set, expected_set)
            self.assertEqual(result_dict, expected_dict)
            print_success("✅ ✅ Données modifiées correctement")
        except AssertionError as e:
            print_failure(f"❌ ❌ Test échoué : {e}")
            raise


if __name__ == "__main__":
    unittest.main(verbosity=2)
