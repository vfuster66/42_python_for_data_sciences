import unittest
import subprocess
from printer import print_title, print_info, print_success


class TestEx04(unittest.TestCase):

    def run_script(self, *args):
        """Helper pour exécuter tester.py avec arguments"""
        cmd = ['python3', 'ex04/whatis.py'] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def test_even_number(self):
        print_title("Test ➜ Nombre pair")
        output = self.run_script('14')

        print_info(f"🔎 Résultat obtenu : {output}")
        self.assertIn("I'm Even.", output)
        print_success("✅ ✅ Nombre pair OK")

    def test_odd_number(self):
        print_title("Test ➜ Nombre impair")
        output = self.run_script('-5')

        print_info(f"🔎 Résultat obtenu : {output}")
        self.assertIn("I'm Odd.", output)
        print_success("✅ ✅ Nombre impair OK")

    def test_zero(self):
        print_title("Test ➜ Nombre zéro")
        output = self.run_script('0')

        print_info(f"🔎 Résultat obtenu : {output}")
        self.assertIn("I'm Even.", output)
        print_success("✅ ✅ Zéro pair OK")

    def test_no_argument(self):
        print_title("Test ➜ Aucun argument fourni")
        output = self.run_script()
        print_info(f"🔎 Résultat obtenu : {output!r}")
        self.assertEqual(output.strip(), "")
        print_success("✅ ✅ Aucun argument OK (aucune sortie attendue)")

    def test_multiple_arguments(self):
        print_title("Test ➜ Trop d'arguments fournis")
        output = self.run_script('13', '5')

        print_info(f"🔎 Résultat obtenu : {output}")
        self.assertIn("more than one argument is provided", output)
        print_success("✅ ✅ Trop d'arguments OK")

    def test_not_an_integer(self):
        print_title("Test ➜ Argument non entier")
        output = self.run_script('hello')

        print_info(f"🔎 Résultat obtenu : {output}")
        self.assertIn("argument is not an integer", output)
        print_success("✅ ✅ Argument non entier OK")


if __name__ == "__main__":
    unittest.main(verbosity=2)
