import unittest
from S1E9 import Stark, Character


class TestStark(unittest.TestCase):

    def test_01_instance_creation(self):
        """Test de la création d'une instance de Stark"""
        print("Test de la création d'une instance de Stark...")
        ned = Stark("Ned")
        print(f"Attendu: Ned, Obtenu: {ned.first_name}")
        print(f"Attendu: True (is_alive), Obtenu: {ned.is_alive}")
        self.assertEqual(ned.first_name, "Ned")
        self.assertTrue(ned.is_alive)

    def test_02_is_alive_default(self):
        """Test de l'état de vie par défaut"""
        print("Test de l'état de vie par défaut...")
        ned = Stark("Ned")
        print(f"Attendu: True, Obtenu: {ned.is_alive}")
        self.assertTrue(ned.is_alive)

    def test_03_custom_is_alive(self):
        """Test de la création d'un Stark avec un état de vie personnalisé"""
        print("Test de la création d'un Stark avec un état de vie "
              "personnalisé...")
        lyanna = Stark("Lyanna", False)
        print(f"Attendu: False, Obtenu: {lyanna.is_alive}")
        self.assertFalse(lyanna.is_alive)

    def test_04_die_method(self):
        """Test de la méthode die"""
        print("Test de la méthode die...")
        ned = Stark("Ned")
        ned.die()
        print(f"Attendu après die(): False, Obtenu: {ned.is_alive}")
        self.assertFalse(ned.is_alive)

    def test_05_docstrings(self):
        """Test des docstrings pour s'assurer qu'ils sont présents"""
        print("Test des docstrings...")
        self.assertIsNotNone(Stark.__doc__)
        self.assertIsNotNone(Stark.__init__.__doc__)
        self.assertIsNotNone(Stark.die.__doc__)

    def test_06_abstract_class_instantiation(self):
        """Test pour s'assurer que l'on ne peut pas instancier la classe
        abstraite"""
        print("Test d'instanciation d'une classe abstraite...")
        with self.assertRaises(TypeError):
            _ = Character("hodor")


if __name__ == "__main__":
    print("Début des tests pour l'exercice 00\n")
    unittest.main(verbosity=2)
