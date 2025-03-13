# tests/test_04.py

import unittest
import os
from ex04.rotate import ft_rotate
from printer import print_title, print_info, print_success


class TestFtRotate(unittest.TestCase):

    def setUp(self):
        print_info(f"\n🔎 {self._testMethodName} - Début du test")

    def tearDown(self):
        print_info(f"🔎 {self._testMethodName} - Fin du test\n")

    def test_valid_image(self):
        """Test ➜ Rotation image valide"""
        print_title("Test ➜ Image valide")

        image = "ex04/animal.jpeg"
        result = ft_rotate(image)

        self.assertIsNotNone(result)
        self.assertEqual(result.shape, (400, 400, 3))
        print_success(f"✅ Rotation OK : {result.shape}")

        output_file = "transposed_image_with_axes.png"
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_image_not_found(self):
        """Test ➜ Image non trouvée"""
        print_title("Test ➜ Image inexistante")

        image = "ex04/does_not_exist.jpeg"
        result = ft_rotate(image)

        self.assertIsNone(result)
        print_success("✅ Image inexistante gérée correctement")

    def test_invalid_file(self):
        """Test ➜ Fichier invalide"""
        print_title("Test ➜ Fichier invalide")

        fake_file = "ex04/fake.txt"
        with open(fake_file, "w") as f:
            f.write("Je ne suis pas une image")

        result = ft_rotate(fake_file)
        self.assertIsNone(result)
        print_success("✅ Fichier non image géré correctement")

        os.remove(fake_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
