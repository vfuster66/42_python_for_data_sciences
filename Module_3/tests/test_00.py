import unittest
from ex00.S1E9 import Stark, Character
from printer import print_title, print_success, print_failure


class TestStark(unittest.TestCase):

    def test_01_instance_creation(self):
        print_title("Test de la création d'une instance de Stark")
        ned = Stark("Ned")
        if ned.first_name == "Ned" and ned.is_alive:
            print_success(f"Création OK : {ned.first_name}, "
                          f"is_alive={ned.is_alive}")
        else:
            print_failure("Échec création")
        self.assertEqual(ned.first_name, "Ned")
        self.assertTrue(ned.is_alive)

    def test_02_is_alive_default(self):
        print_title("Test de l'état de vie par défaut")
        ned = Stark("Ned")
        if ned.is_alive:
            print_success("is_alive par défaut OK")
        else:
            print_failure("is_alive KO")
        self.assertTrue(ned.is_alive)

    def test_03_custom_is_alive(self):
        print_title("Test avec un état de vie personnalisé")
        lyanna = Stark("Lyanna", False)
        if not lyanna.is_alive:
            print_success("is_alive personnalisé OK")
        else:
            print_failure("is_alive KO")
        self.assertFalse(lyanna.is_alive)

    def test_04_die_method(self):
        print_title("Test de la méthode die()")
        ned = Stark("Ned")
        ned.die()
        if not ned.is_alive:
            print_success("die() OK")
        else:
            print_failure("die() KO")
        self.assertFalse(ned.is_alive)

    def test_05_docstrings(self):
        print_title("Test des docstrings")
        if Stark.__doc__ and Stark.__init__.__doc__ and Stark.die.__doc__:
            print_success("Docstrings présents")
        else:
            print_failure("Docstrings manquants")
        self.assertIsNotNone(Stark.__doc__)
        self.assertIsNotNone(Stark.__init__.__doc__)
        self.assertIsNotNone(Stark.die.__doc__)

    def test_06_abstract_class_instantiation(self):
        print_title("Test de la non-instantiation de Character")
        with self.assertRaises(TypeError):
            _ = Character("hodor")
        print_success("Instanciation interdite validée")


if __name__ == "__main__":
    unittest.main(verbosity=2)
