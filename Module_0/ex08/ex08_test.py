import subprocess
import sys


def test_ft_tqdm():
    """
    Teste la barre de progression ft_tqdm en s'assurant que la progression
    atteint 100%.
    """
    try:
        # Tester ta version de ft_tqdm et rediriger stdout/stderr en temps réel
        result = subprocess.run(['python3', 'tester.py'],
                                stdout=sys.stdout, stderr=sys.stderr)

        # Vérifie si le processus s'est terminé avec succès (code retour 0)
        if result.returncode == 0:
            print("Tous les tests de ft_tqdm sont passés avec succès !")
        else:
            print(f"Les tests de ft_tqdm ont échoué avec \
                  le code de retour : {result.returncode}")

    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


def main():
    """
    Fonction principale pour exécuter les tests de ft_tqdm.
    """
    test_ft_tqdm()


if __name__ == "__main__":
    main()
