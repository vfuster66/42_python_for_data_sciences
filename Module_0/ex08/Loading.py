import time
import sys
import shutil
from typing import Generator


def format_time(seconds):
    """
    Formate le temps donné en secondes au format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """
    Simule une barre de progression pour itérer sur une range.

    Args:
        lst (range): La plage sur laquelle itérer.

    Yields:
        Tout élément de la plage.
    """
    total = len(lst)
    start_time = time.time()

    # Obtenir la largeur du terminal pour ajuster dynamiquement la barre de progression
    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        # Calcul de la progression
        progress = int(i / total * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed

        # Formater les temps écoulé et estimé
        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)

        # Construire la barre de progression
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        # Afficher la barre de progression
        print(f"\r{progress_info} {time_info}", end="", flush=True)

        yield item  # Utilisation de yield pour renvoyer l'élément tout en mettant à jour la progression

    # Fin de la barre de progression
    print()


def main():
    """
    Fonction principale pour tester la barre de progression avec une plage de valeurs.
    """
    for _ in ft_tqdm(range(0, 333)):
        time.sleep(0.005)


if __name__ == "__main__":
    main()
