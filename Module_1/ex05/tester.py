from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_red, ft_grey
from PIL import Image
import numpy as np
import os
import webbrowser

# Charger l'image
array = ft_load("landscape.jpg")

# Appliquer les filtres
inverted = ft_invert(array)
red_filtered = ft_red(array)
green_filtered = ft_green(array)
blue_filtered = ft_blue(array)
grey_filtered = ft_grey(array)


# Fonction pour sauvegarder l'image
def save_and_open_image(image_array, filename):
    # Sauvegarder l'image en fichier PNG
    img = Image.fromarray(image_array.astype(np.uint8))
    img.save(filename)

    # Ouvrir l'image avec le viewer d'image par défaut du système
    if os.name == 'nt':  # Pour Windows
        os.system(f'start {filename}')
    elif os.name == 'posix':  # Pour macOS et Linux
        webbrowser.open(f'file://{os.path.abspath(filename)}')


# Sauvegarder et afficher chaque image filtrée
save_and_open_image(inverted, "inverted_image.png")
save_and_open_image(red_filtered, "red_image.png")
save_and_open_image(green_filtered, "green_image.png")
save_and_open_image(blue_filtered, "blue_image.png")
save_and_open_image(grey_filtered, "grey_image.png")
