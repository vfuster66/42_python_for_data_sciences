import unittest
from ex01.S1E7 import Baratheon, Lannister
from ex00.S1E9 import Character
from printer import print_title, print_info, print_success


class TestGameOfThrones(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé")

    def test_01_baratheon_instance_creation(self):
        print_title("Test ➜ Baratheon Instance")
        robert = Baratheon("Robert")
        self.assertEqual(robert.first_name, "Robert")
        self.assertEqual(robert.family_name, "Baratheon")
        self.assertEqual(robert.eyes, "brown")
        self.assertEqual(robert.hairs, "dark")
        self.assertTrue(robert.is_alive)
        print_success("Baratheon instance creation OK")

    def test_02_lannister_instance_creation(self):
        print_title("Test ➜ Lannister Instance")
        cersei = Lannister("Cersei")
        self.assertEqual(cersei.first_name, "Cersei")
        self.assertEqual(cersei.family_name, "Lannister")
        self.assertEqual(cersei.eyes, "blue")
        self.assertEqual(cersei.hairs, "light")
        self.assertTrue(cersei.is_alive)
        print_success("Lannister instance creation OK")

    def test_03_die_method(self):
        print_title("Test ➜ Die Method")
        robert = Baratheon("Robert")
        robert.die()
        self.assertFalse(robert.is_alive)

        cersei = Lannister("Cersei")
        cersei.die()
        self.assertFalse(cersei.is_alive)
        print_success("Die method OK for both families")

    def test_04_create_lannister(self):
        print_title("Test ➜ create_lannister() Method")
        jaine = Lannister.create_lannister("Jaine", True)
        self.assertEqual(jaine.first_name, "Jaine")
        self.assertEqual(jaine.family_name, "Lannister")
        self.assertTrue(jaine.is_alive)
        print_success("create_lannister OK")

    def test_05_docstrings(self):
        print_title("Test ➜ Docstrings")
        self.assertIsNotNone(Baratheon.__doc__)
        self.assertIsNotNone(Baratheon.__init__.__doc__)
        self.assertIsNotNone(Baratheon.die.__doc__)
        self.assertIsNotNone(Lannister.__doc__)
        self.assertIsNotNone(Lannister.create_lannister.__doc__)
        print_success("Docstrings exist for all tested methods/classes")

    def test_06_abstract_class_instantiation(self):
        print_title("Test ➜ Abstract Class Character Instantiation")
        with self.assertRaises(TypeError):
            _ = Character("Hodor")
        print_success("Abstract class instantiation correctly fails")

    def test_07_str_and_repr_methods(self):
        print_title("Test ➜ __str__ and __repr__ Methods")
        robert = Baratheon("Robert")
        cersei = Lannister("Cersei")

        self.assertEqual(str(robert), "Vector: ('Baratheon', 'brown', 'dark')")
        self.assertEqual(
            repr(robert), "Vector: ('Baratheon', 'brown', 'dark')"
        )

        self.assertEqual(str(cersei), "Vector: ('Lannister', 'blue', 'light')")
        self.assertEqual(
            repr(cersei), "Vector: ('Lannister', 'blue', 'light')"
        )

        print_success("__str__ and __repr__ OK for both families")


if __name__ == "__main__":
    unittest.main(verbosity=2)
