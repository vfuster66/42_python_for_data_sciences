import unittest
from DiamondTrap import King
from S1E7 import Baratheon, Lannister


class TestKing(unittest.TestCase):

    def setUp(self):
        """Affiche un message avant chaque test."""
        print(f"{self._testMethodName} - Début du test")

    def tearDown(self):
        """Affiche un message après chaque test."""
        print(f"{self._testMethodName} - Test terminé")

    def test_01_initialization(self):
        """Test de l'initialisation de la classe King"""
        print("Test de l'initialisation de la classe King...")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.first_name, "Joffrey")
        self.assertEqual(joffrey.family_name, "Baratheon")
        self.assertEqual(joffrey.eyes, "brown")
        self.assertEqual(joffrey.hairs, "dark")
        self.assertTrue(joffrey.is_alive)

    def test_02_set_eyes(self):
        """Test de la méthode set_eyes pour changer la couleur des yeux"""
        print("Test de la méthode set_eyes...")
        joffrey = King("Joffrey")
        joffrey.set_eyes("blue")
        self.assertEqual(joffrey.get_eyes(), "blue")

    def test_03_set_hairs(self):
        """Test de la méthode set_hairs pour changer la couleur des cheveux"""
        print("Test de la méthode set_hairs...")
        joffrey = King("Joffrey")
        joffrey.set_hairs("light")
        self.assertEqual(joffrey.get_hairs(), "light")

    def test_04_get_eyes(self):
        """Test de la méthode get_eyes pour vérifier la couleur des yeux"""
        print("Test de la méthode get_eyes...")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.get_eyes(), "brown")  # Valeur par défaut

    def test_05_get_hairs(self):
        """Test de la méthode get_hairs pour vérifier la couleur des cheveux"""
        print("Test de la méthode get_hairs...")
        joffrey = King("Joffrey")
        self.assertEqual(joffrey.get_hairs(), "dark")  # Valeur par défaut

    def test_06_die_method(self):
        """Test de la méthode die héritée pour
        marquer le personnage comme mort"""
        print("Test de la méthode die...")
        joffrey = King("Joffrey")
        joffrey.die()
        self.assertFalse(joffrey.is_alive)

    def test_07_king_inheritance(self):
        """Test de la cohérence de l'héritage
        multiple (Baratheon et Lannister)"""
        print("Test de l'héritage multiple...")
        joffrey = King("Joffrey")
        self.assertTrue(isinstance(joffrey, King))
        self.assertTrue(isinstance(joffrey, Baratheon))
        self.assertTrue(isinstance(joffrey, Lannister))


if __name__ == "__main__":
    print("Début des tests pour l'exercice 02\n")
    unittest.main(verbosity=2)
