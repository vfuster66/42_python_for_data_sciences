# test_ex02.py

import unittest
import os
from load_image import ft_load

class TestFtLoad(unittest.TestCase):

    def test_01_load_image_success(self):
        """Test de chargement d'une image valide"""
        image_path = "landscape.jpg"  # Assurez-vous que l'image est dans le répertoire
        print("\nTest 1: Chargement d'une image valide")
        img_array = ft_load(image_path)
        self.assertIsNotNone(img_array, "L'image n'a pas été chargée correctement.")
        self.assertEqual(img_array.shape, (257, 450, 3), "La forme de l'image est incorrecte.")
    
    def test_02_image_not_found(self):
        """Test avec un chemin d'image invalide"""
        invalid_image_path = "nonexistent.jpg"
        print("\nTest 2: Chargement d'une image inexistante")
        img_array = ft_load(invalid_image_path)
        self.assertIsNone(img_array, "Une image inexistante ne devrait pas être chargée.")
    
    def test_03_invalid_image_format(self):
        """Test avec un fichier non image"""
        print("\nTest 3: Chargement d'un fichier au format invalide")
        # Création d'un fichier texte temporaire pour simuler un format non image
        with open("invalid_image.txt", "w") as f:
            f.write("Ceci est un fichier texte, pas une image.")
        
        img_array = ft_load("invalid_image.txt")
        self.assertIsNone(img_array, "Le fichier texte ne devrait pas être chargé comme image.")
        
        # Suppression du fichier texte temporaire
        os.remove("invalid_image.txt")

if __name__ == "__main__":
    unittest.main()
