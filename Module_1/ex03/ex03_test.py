# test_ex03.py

import unittest
import os
from zoom import ft_zoom


class TestFtZoom(unittest.TestCase):

    def test_01_zoom_image_success(self):
        """Test de zoom sur une image valide"""
        image_path = "animal.jpeg"
        print("\nTest 1: Zoom sur une image valide")
        zoomed_img = ft_zoom(image_path)
        self.assertIsNotNone(zoomed_img, "L'image \
                             n'a pas été zoomée correctement.")
        self.assertEqual(zoomed_img.shape, (200, 200, 3), "La \
                         taille de l'image zoomée est incorrecte.")

    def test_02_image_not_found(self):
        """Test avec un chemin d'image invalide"""
        invalid_image_path = "nonexistent_image.jpeg"
        print("\nTest 2: Zoom sur une image inexistante")
        zoomed_img = ft_zoom(invalid_image_path)
        self.assertIsNone(zoomed_img, "L'image \
                          inexistante ne devrait pas être zoomée.")

    def test_03_invalid_image_format(self):
        """Test avec un fichier qui n'est pas une image"""
        print("\nTest 3: Zoom sur un fichier au format invalide")
        # Création d'un fichier texte temp pour simuler un format non image
        with open("invalid_image.txt", "w") as f:
            f.write("Ceci est un fichier texte, pas une image.")

        zoomed_img = ft_zoom("invalid_image.txt")
        self.assertIsNone(zoomed_img, "Le fichier \
                          texte ne devrait pas être zoomé comme une image.")

        # Suppression du fichier texte temporaire
        os.remove("invalid_image.txt")


if __name__ == "__main__":
    unittest.main()
