import time


def format_time(seconds: float) -> str:
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst):
    """
    Reproduction de la fonction tqdm avec un yield.
    Affiche une barre de progression lors de l'itération.
    """
    total = len(lst)
    start_time = time.time()

    for index, item in enumerate(lst, 1):
        progress = index / total
        bar_length = 50
        filled_length = int(bar_length * progress)

        bar = '=' * filled_length + ' ' * (bar_length - filled_length)

        elapsed_time = time.time() - start_time
        speed = index / elapsed_time if elapsed_time > 0 else 0

        print(
            f"\r{int(progress * 100):3}%|[{bar}]| {index}/{total} "
            f"[{elapsed_time:0.2f}s<"
            f"{(elapsed_time / index) * (total - index):0.2f}s, "
            f"{speed:0.2f}it/s]",
            end='',
            flush=True
        )
        yield item

    print()


def main():
    try:
        for _ in ft_tqdm(range(333)):
            time.sleep(0.005)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()
