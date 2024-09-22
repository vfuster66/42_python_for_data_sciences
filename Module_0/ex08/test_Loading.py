import subprocess
from time import sleep

def test_ft_tqdm():
    # Tester ta version de ft_tqdm
    print("Testing ft_tqdm:")
    result = subprocess.run(['python3', 'tester.py'], capture_output=True, text=True)
    assert "100%" in result.stdout, "Erreur : La progression n'a pas atteint 100% avec ft_tqdm."

    print("Tous les tests de ft_tqdm sont passés avec succès !")


if __name__ == "__main__":
    test_ft_tqdm()
