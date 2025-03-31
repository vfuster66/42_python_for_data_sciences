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
        print_title("Test ➜ Ex04 Image valide")
        result = ft_rotate()
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, (400, 400)) # image transposée = 2D
        print_success(f"✅ Rotation OK : {result.shape}")
        
        # Vérifier l'existence du fichier avec un chemin relatif simple
        output_file = "ex04/transposed_image.png"
        self.assertTrue(os.path.exists(output_file), f"Le fichier {output_file} n'existe pas")

            
    def test_image_not_found(self):
        """Test ➜ Image non trouvée"""
        print_title("Test ➜ Ex04 Image inexistante")
        print_info("⚠️ Test ignoré car l'image est hardcodée.")
        self.skipTest("Le chemin d'image est fixe (ex04/animal.jpeg)")
        
    def test_invalid_file(self):
        """Test ➜ Fichier invalide"""
        print_title("Test ➜ Ex04 Fichier invalide")
        
        # Utiliser un chemin relatif simple
        fake_file = "ex04/animal.jpeg"
        backup = None
        
        if os.path.exists(fake_file):
            backup = fake_file + ".bak"
            os.rename(fake_file, backup)
            
        try:
            with open(fake_file, "w") as f:
                f.write("ceci n'est pas une image")
            result = ft_rotate()
            self.assertIsNone(result)
            print_success("✅ Fichier non image géré correctement")
        finally:
            if os.path.exists(fake_file):
                os.remove(fake_file)
            if backup and os.path.exists(backup):
                os.rename(backup, fake_file)
                
if __name__ == "__main__":
    unittest.main(verbosity=2)