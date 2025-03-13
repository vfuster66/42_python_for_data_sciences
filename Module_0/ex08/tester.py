from time import sleep
from tqdm import tqdm
from ex08.Loading import ft_tqdm
from printer import print_title, print_info, print_success


def run_ft_tqdm_test():
    print_title("=== EX08 ➜ Tester ft_tqdm() ===")
    print_info("🔎 Lancement de la barre de progression ft_tqdm sur "
               "100 itérations.")

    for _ in ft_tqdm(range(100)):
        sleep(0.01)

    print_success("✅ ✅ ✅ Progression terminée avec succès !")


def run_tqdm_test():
    print_title("=== EX08 ➜ Tester tqdm (version originale) ===")
    print_info("🔎 Lancement de la barre de progression tqdm sur "
               "100 itérations.")

    for _ in tqdm(range(100)):
        sleep(0.01)

    print_success("✅ ✅ ✅ Progression originale tqdm terminée !")


def main():
    print_title("=== EX08 ➜ Comparaison ft_tqdm() VS tqdm() ===")

    run_ft_tqdm_test()
    print()  # pour séparer proprement
    run_tqdm_test()


if __name__ == "__main__":
    main()
