import unittest
import os
from ex03.zoom import ft_zoom
from printer import print_title, print_info, print_success


class TestFtZoom(unittest.TestCase):

    def setUp(self):
        print_info(f"\n🔎 {self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin du test\n")

    def test_zoom_image_success(self):
        print_title("Test ➜ Ex03 Zoom image valide")

        image_path = "ex03/animal.jpeg"
        zoomed_img = ft_zoom(image_path)

        self.assertIsNotNone(zoomed_img)
        self.assertEqual(zoomed_img.shape, (400, 400, 1))
        print_success("✅ Image zoomée avec succès !")

    def test_image_not_found(self):
        print_title("Test ➜ Ex03 Image inexistante")

        image_path = "ex03/nonexistent.jpeg"
        zoomed_img = ft_zoom(image_path)

        self.assertIsNone(zoomed_img)
        print_success("✅ Image inexistante gérée correctement")

    def test_invalid_image_format(self):
        print_title("Test ➜ Ex03 Format de fichier non image")

        fake_file = "ex03/fake.txt"
        with open(fake_file, "w") as f:
            f.write("Ce n'est pas une image")

        zoomed_img = ft_zoom(fake_file)

        self.assertIsNone(zoomed_img)
        print_success("✅ Fichier non image géré correctement")

        os.remove(fake_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
