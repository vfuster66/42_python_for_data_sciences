import unittest
from S1E7 import Baratheon, Lannister, Character


class TestGameOfThrones(unittest.TestCase):

    def setUp(self):
        """Affiche un message avant chaque test."""
        print(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        """Affiche un message après chaque test."""
        print(f"{self._testMethodName} - Test terminé")

    def test_01_baratheon_instance_creation(self):
        """Test de la création d'une instance de Baratheon."""
        print("Test de la création d'une instance de Baratheon...")
        robert = Baratheon("Robert")
        self.assertEqual(robert.first_name, "Robert")
        self.assertEqual(robert.family_name, "Baratheon")
        self.assertEqual(robert.eyes, "brown")
        self.assertEqual(robert.hairs, "dark")
        self.assertTrue(robert.is_alive)

    def test_02_lannister_instance_creation(self):
        """Test de la création d'une instance de Lannister."""
        print("Test de la création d'une instance de Lannister...")
        cersei = Lannister("Cersei")
        self.assertEqual(cersei.first_name, "Cersei")
        self.assertEqual(cersei.family_name, "Lannister")
        self.assertEqual(cersei.eyes, "blue")
        self.assertEqual(cersei.hairs, "light")
        self.assertTrue(cersei.is_alive)

    def test_03_die_method(self):
        """Test de la méthode die pour les deux familles."""
        print("Test de la méthode die...")
        robert = Baratheon("Robert")
        robert.die()
        self.assertFalse(robert.is_alive)

        cersei = Lannister("Cersei")
        cersei.die()
        self.assertFalse(cersei.is_alive)

    def test_04_lannister_create_lannister(self):
        """Test de la méthode create_lannister pour créer un personnage."""
        print("Test de la méthode create_lannister...")
        jaine = Lannister.create_lannister("Jaine", True)
        self.assertEqual(jaine.first_name, "Jaine")
        self.assertEqual(jaine.family_name, "Lannister")
        self.assertTrue(jaine.is_alive)

    def test_05_docstrings(self):
        """Test pour vérifier la présence des docstrings."""
        print("Test des docstrings...")
        self.assertIsNotNone(Baratheon.__doc__)
        self.assertIsNotNone(Baratheon.__init__.__doc__)
        self.assertIsNotNone(Baratheon.die.__doc__)
        self.assertIsNotNone(Lannister.__doc__)
        self.assertIsNotNone(Lannister.create_lannister.__doc__)

    def test_06_abstract_class_instantiation(self):
        """Test pour s'assurer que l'on ne peut pas
        instancier la classe Character."""
        print("Test de l'instanciation de la classe abstraite Character...")
        with self.assertRaises(TypeError):
            _ = Character("Hodor")

    def test_07_str_and_repr_methods(self):
        """Test des méthodes __str__ et __repr__."""
        print("Test des méthodes __str__ et __repr__...")
        robert = Baratheon("Robert")
        cersei = Lannister("Cersei")

        self.assertEqual(
            str(robert), "Vector: ('Baratheon', 'brown', 'dark')"
        )
        self.assertEqual(
            repr(robert), "Vector: ('Baratheon', 'brown', 'dark')"
        )

        self.assertEqual(
            str(cersei), "Vector: ('Lannister', 'blue', 'light')"
        )
        self.assertEqual(
            repr(cersei), "Vector: ('Lannister', 'blue', 'light')"
        )


if __name__ == "__main__":
    print("Début des tests pour l'exercice 01\n")
    unittest.main(verbosity=2)
