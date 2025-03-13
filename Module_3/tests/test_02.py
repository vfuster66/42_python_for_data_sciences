import unittest
from ex02.DiamondTrap import King
from ex01.S1E7 import Baratheon, Lannister
from printer import print_title, print_info, print_success


class TestKing(unittest.TestCase):

    def setUp(self):
        print_info(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"{self._testMethodName} - Test terminé")

    def test_01_initialization(self):
        print_title("Test ➜ King Initialization")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.first_name, "Joffrey")
        self.assertEqual(joffrey.family_name, "Baratheon")  # From MRO!
        self.assertEqual(joffrey.eyes, "brown")
        self.assertEqual(joffrey.hairs, "dark")
        self.assertTrue(joffrey.is_alive)
        print_success("King initialized correctly")

    def test_02_set_eyes(self):
        print_title("Test ➜ set_eyes() Method")
        joffrey = King("Joffrey")
        joffrey.set_eyes("blue")
        self.assertEqual(joffrey.get_eyes(), "blue")
        print_success("set_eyes OK")

    def test_03_set_hairs(self):
        print_title("Test ➜ set_hairs() Method")
        joffrey = King("Joffrey")
        joffrey.set_hairs("light")
        self.assertEqual(joffrey.get_hairs(), "light")
        print_success("set_hairs OK")

    def test_04_get_eyes(self):
        print_title("Test ➜ get_eyes() Default Value")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.get_eyes(), "brown")
        print_success("get_eyes default OK")

    def test_05_get_hairs(self):
        print_title("Test ➜ get_hairs() Default Value")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.get_hairs(), "dark")
        print_success("get_hairs default OK")

    def test_06_die_method(self):
        print_title("Test ➜ die() Method")
        joffrey = King("Joffrey")
        joffrey.die()
        self.assertFalse(joffrey.is_alive)
        print_success("die() OK")

    def test_07_inheritance(self):
        print_title("Test ➜ King Inheritance Check")
        joffrey = King("Joffrey")
        self.assertTrue(isinstance(joffrey, King))
        self.assertTrue(isinstance(joffrey, Baratheon))
        self.assertTrue(isinstance(joffrey, Lannister))
        print_success("Inheritance OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
