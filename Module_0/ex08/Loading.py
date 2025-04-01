import time
import shutil

def format_time(seconds):
    """
    Formate le temps donné en secondes au format MM:SS.
    Args:
        seconds (float): Temps en secondes.
    Returns:
        str: Temps formaté au format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"

def ft_tqdm(lst: range) -> None: # type: ignore
    """
    Simule une barre de progression pour l'itération à travers une plage.
    Args:
        lst (range): La plage à parcourir.
    Yields:
        Any: L'élément actuel de la plage.
    
    yield est un mot-clé en Python utilisé dans le contexte de création de générateurs.
    Les générateurs sont un moyen de créer des itérateurs, qui sont des objets utilisés pour
    itérer sur une séquence de valeurs sans avoir à stocker toutes ces
    valeurs en mémoire à la fois. Au lieu de générer toutes les valeurs et de les renvoyer
    en une seule fois, un générateur produit une valeur à la fois chaque fois que
    l'instruction yield est rencontrée.
    """
    total = len(lst)
    start_time = time.time()
    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10
    
    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed
        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"
        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item

def main():
    for _ in ft_tqdm(range(0, 333)):
        pass

if __name__ == "__main__":
    main()