import unittest
import os
from ex02.load_image import ft_load
from printer import print_title, print_info, print_success


class TestFtLoad(unittest.TestCase):

    def setUp(self):
        print_info(f"\n🔎 {self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin du test\n")

    def test_load_image_success(self):
        print_title("Test ➜ Ex02 Chargement image valide")
        image_path = "ex02/landscape.jpg"

        img_array = ft_load(image_path)

        self.assertIsNotNone(
            img_array, "❌ L'image n'a pas été chargée correctement."
        )
        self.assertEqual(
            img_array.shape, (257, 450, 3),
            "❌ La forme de l'image est incorrecte."
        )
        print_success(f"✅ Image chargée avec succès : {img_array.shape}")

    def test_image_not_found(self):
        print_title("Test ➜ Ex02 Image inexistante")

        invalid_image_path = "ex02/nonexistent.jpg"
        img_array = ft_load(invalid_image_path)

        self.assertIsNone(
            img_array, "❌ Une image inexistante ne devrait pas être chargée."
        )
        print_success("✅ Image inexistante gérée correctement.")

    def test_invalid_image_format(self):
        print_title("Test ➜ Ex02 Fichier format invalide")

        invalid_file = "ex02/invalid_image.txt"

        with open(invalid_file, "w") as f:
            f.write("Ceci est un fichier texte, pas une image.")

        img_array = ft_load(invalid_file)

        self.assertIsNone(
            img_array,
            "❌ Le fichier texte ne devrait pas être chargé comme image."
        )
        print_success("✅ Fichier non image géré correctement.")

        os.remove(invalid_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
