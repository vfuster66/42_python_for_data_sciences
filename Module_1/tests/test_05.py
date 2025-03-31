import unittest
import os
import numpy as np
from ex05.pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from ex02.load_image import ft_load
from printer import print_title, print_info, print_success


class TestPimpImage(unittest.TestCase):

    def setUp(self):
        print_info(f"\n🔎 {self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin du test\n")

    def test_image_not_found(self):
        print_title("Test ➜ Ex05 Image inexistante")
        array = ft_load("ex05/does_not_exist.jpg")
        self.assertIsNone(array)
        print_success("✅ ✅ Image inexistante gérée correctement")

    def test_invalid_file(self):
        print_title("Test ➜ Ex05 Fichier non image")

        fake_file = "ex05/fake.txt"
        with open(fake_file, "w") as f:
            f.write("Pas une image")

        array = ft_load(fake_file)
        self.assertIsNone(array)
        print_success("✅ ✅ Fichier non image géré correctement")

        os.remove(fake_file)

    def test_valid_filters(self):
        print_title("Test ➜ Ex05 Filtres sur image valide")

        image_path = "ex05/landscape.jpg"
        array = ft_load(image_path)
        self.assertIsNotNone(array)

        inv = ft_invert(array)
        self.assertIsInstance(inv, np.ndarray)
        print_success("✅ ✅ ft_invert OK")

        red = ft_red(array)
        self.assertIsInstance(red, np.ndarray)
        print_success("✅ ✅ ft_red OK")

        green = ft_green(array)
        self.assertIsInstance(green, np.ndarray)
        print_success("✅ ✅ ft_green OK")

        blue = ft_blue(array)
        self.assertIsInstance(blue, np.ndarray)
        print_success("✅ ✅ ft_blue OK")

        grey = ft_grey(array)
        self.assertIsInstance(grey, np.ndarray)
        print_success("✅ ✅ ft_grey OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
