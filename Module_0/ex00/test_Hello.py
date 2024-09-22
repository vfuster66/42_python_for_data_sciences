import unittest
import subprocess
import os
from termcolor import colored

class TestHelloScript(unittest.TestCase):
    def test_hello_script(self):
        # Afficher le titre de l'exercice
        print("\nExercice 00 : First python script")
        print("Objectif : Modifier les objets de données pour afficher les salutations correctes")

        # Déterminer le chemin absolu de Hello.py
        script_path = os.path.join(os.path.dirname(__file__), 'Hello.py')

        if not os.path.exists(script_path):
            self.fail(f"Le fichier {script_path} n'existe pas.")

        # Exécuter le script Hello.py et capturer la sortie
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)

        # Résultat attendu
        expected_output = (
            "['Hello', 'World!']\n"
            "('Hello', 'France!')\n"
            "['Hello', 'Perpignan!']\n"
            "{'Hello': '42Perpignan!'}\n"
        )

        # Afficher l'exécution et les résultats
        print("\nExecution du script : Hello.py")
        print("Résultat attendu :")
        print(expected_output)

        print("\nRésultat obtenu :")
        print(result.stdout)

        # Vérifier si la sortie correspond à ce qui est attendu
        if result.stdout == expected_output:
            print(colored("\nOK", "green"))
        else:
            print(colored("\nFAILED", "red"))
            self.assertEqual(result.stdout, expected_output)

if __name__ == "__main__":
    unittest.main()
