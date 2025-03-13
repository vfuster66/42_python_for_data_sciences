import time
from datetime import datetime


def main():
    """
    Affiche le timestamp actuel et la date au format demandé.
    """
    # Obtenir le temps actuel en secondes depuis Epoch
    current_time = time.time()

    # Afficher les secondes depuis le 1er janvier 1970
    print(f"Seconds since January 1, 1970: {current_time:.4f} "
          f"or {current_time:.2e}")

    # Obtenir la date actuelle et l'afficher au format souhaité
    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")
    print(formatted_date)


if __name__ == "__main__":
    main()
