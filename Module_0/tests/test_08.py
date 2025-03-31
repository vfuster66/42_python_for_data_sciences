from time import sleep
from tqdm import tqdm
from ex08.Loading import ft_tqdm
from printer import print_title, print_info, print_success


# Fonctions auxiliaires - ne seront pas exécutées comme tests indépendants
def _run_ft_tqdm_test():
    """Implémentation du test ft_tqdm"""
    total_iterations = 100
    print_info(f"Cas 1 - ft_tqdm sur {total_iterations} itérations.")
    try:
        for _ in ft_tqdm(range(total_iterations)):
            sleep(0.01)
        print_success("✅ ✅ ✅ Cas 1 OK : ft_tqdm a fonctionné sans erreur !")
    except Exception as e:
        raise AssertionError(f"Erreur inattendue sur ft_tqdm : {e}")


def _run_original_tqdm_test():
    """Implémentation du test tqdm original"""
    total_iterations = 100
    print_info(f"Cas 2 - tqdm sur {total_iterations} itérations.")
    try:
        for _ in tqdm(range(total_iterations)):
            sleep(0.01)
        print_success("✅ ✅ ✅ Cas 2 OK : tqdm a fonctionné sans erreur !")
    except Exception as e:
        raise AssertionError(f"Erreur inattendue sur tqdm : {e}")


# Test principal - le seul qui sera découvert par le framework de test
def test_ft_tqdm_vs_tqdm():
    """
    Seul test de la barre de progression - teste à la fois ft_tqdm et tqdm.
    Ce test combine toutes les vérifications nécessaires.
    """
    print_title("=== Test ➜ Ex08 Comparatif ft_tqdm VS tqdm ===")

    # Test de ft_tqdm
    print_title("=== Test ➜ ft_tqdm (EX08) ===")
    _run_ft_tqdm_test()

    # Test de tqdm original
    print_title("=== Test ➜ tqdm officiel (comparaison) ===")
    _run_original_tqdm_test()

    print_success("✅ ✅ ✅ ✅ Comparatif réussi : les deux barres fonctionnent !")


# Pour exécution manuelle
if __name__ == "__main__":
    test_ft_tqdm_vs_tqdm()
