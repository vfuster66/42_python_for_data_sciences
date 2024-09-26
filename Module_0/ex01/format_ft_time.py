import time
from datetime import datetime

# Obtenir le temps actuel en secondes depuis Epoch
current_time = time.time()

# Afficher les secondes depuis le 1er janvier 1970
print(f"Seconds since January 1, \
      1970: {current_time:.4f} ou {current_time:.2e}")

# Obtenir la date actuelle et l'afficher au format souhaité
# (par ex. Oct 21 2022)
current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")
print(formatted_date)
