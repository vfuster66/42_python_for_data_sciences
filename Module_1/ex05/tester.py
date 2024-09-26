from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from PIL import Image
import numpy as np

# Charger l'image
image_array = ft_load("landscape.jpg")

# Appliquer les filtres et sauvegarder les résultats
filters = {
    "inverted": ft_invert(image_array),
    "red_filter": ft_red(image_array),
    "green_filter": ft_green(image_array),
    "blue_filter": ft_blue(image_array),
    "grey_filter": ft_grey(image_array)
}

for filter_name, filtered_image in filters.items():
    # Convertir l'image filtrée en image PIL
    img_with_filter = Image.fromarray(filtered_image.astype(np.uint8))

    # Sauvegarder l'image filtrée
    filename = f"{filter_name}.png"
    img_with_filter.save(filename)

    # Afficher l'image filtrée dans le viewer externe
    img_with_filter.show()
