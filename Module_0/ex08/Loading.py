import time
import sys


def ft_tqdm(lst):
    """
    Reproduction de la fonction tqdm avec un yield.
    Affiche une barre de progression lors de l'itération.
    """
    total = len(lst)
    start_time = time.time()
    first_item = True
    bar_length = 6

    sys.stdout.flush()

    for index, item in enumerate(lst, 1):
        # Calculer le pourcentage de progression
        progress = index / total * 100

        elapsed_time = time.time() - start_time
        speed = index / elapsed_time if elapsed_time > 0 else 0

        # Calculer le temps restant estimé
        remaining_time = (total - index) / speed if speed > 0 else 0

        # Formater le temps écoulé
        elapsed_min, elapsed_sec = divmod(int(elapsed_time), 60)
        elapsed_hour, elapsed_min = divmod(elapsed_min, 60)

        if elapsed_hour > 0:
            elapsed_str = (
                f"{elapsed_hour:d}:{elapsed_min:02d}:{elapsed_sec:02d}"
            )
        else:
            elapsed_str = f"{elapsed_min:02d}:{elapsed_sec:02d}"

        # Formater le temps restant
        remain_min, remain_sec = divmod(int(remaining_time), 60)
        remain_hour, remain_min = divmod(remain_min, 60)

        if remain_hour > 0:
            remain_str = f"{remain_hour:d}:{remain_min:02d}:{remain_sec:02d}"
        else:
            remain_str = f"{remain_min:02d}:{remain_sec:02d}"

        # Créer la barre de progression avec 6 caractères de bloc plein à 100%
        filled_length = int(bar_length * progress / 100)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        if first_item:
            first_item = False
            # Sauter la première impression
            pass
        else:
            # Construire la chaîne complète
            line = (
                f"{progress:3.0f}%|{bar}| {index}/{total} "
                f"[{elapsed_str}<{remain_str}, {speed:.2f}it/s]"
            )
            # Effacer la ligne précédente et afficher la nouvelle
            print(f"\r{line}", end="", flush=True)

        yield item

    # Mise à jour finale à 100%
    elapsed_time = time.time() - start_time
    speed = total / elapsed_time if elapsed_time > 0 else 0

    # Formater le temps écoulé final
    elapsed_min, elapsed_sec = divmod(int(elapsed_time), 60)
    elapsed_hour, elapsed_min = divmod(elapsed_min, 60)

    if elapsed_hour > 0:
        elapsed_str = f"{elapsed_hour:d}:{elapsed_min:02d}:{elapsed_sec:02d}"
    else:
        elapsed_str = f"{elapsed_min:02d}:{elapsed_sec:02d}"

    final_line = (
        f"100%|{'█' * bar_length}| {total}/{total} "
        f"[{elapsed_str}<00:00, {speed:.2f}it/s]"
    )
    print(f"\r{final_line}", end="\n", flush=True)
