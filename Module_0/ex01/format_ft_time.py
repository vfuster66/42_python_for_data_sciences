from datetime import datetime
import time
from printer import print_title, print_info, print_success


def display_current_time():
    """
    Affiche le timestamp actuel et la date au format demandé.
    """
    print_title("=== EX01 ➜ Timestamp & Date Format ===")

    # Obtenir le temps actuel en secondes depuis Epoch
    current_time = time.time()

    # Afficher le timestamp brut et en notation scientifique
    print_info(f"Seconds since January 1, 1970: {current_time:.4f} "
               f"or {current_time:.2e}")

    # Obtenir la date actuelle et l'afficher au format souhaité
    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")
    print_success(f"✅ {formatted_date}")

    return current_time, formatted_date
