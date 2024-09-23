# zoom.py

from PIL import Image
import numpy as np

def ft_zoom(path: str) -> np.ndarray:
    """
    Charge une image, imprime ses dimensions et effectue un zoom sur une partie de l'image.
    Affiche les pixels de la partie zoomée.
    """
    try:
        # Charger l'image
        img = Image.open(path)
        print(f"Taille de l'image : {img.size}")  # (width, height)
        print(f"Nombre de canaux : {len(img.getbands())}")

        # Convertir l'image en tableau numpy
        img_array = np.array(img)

        # Définir une zone de zoom (par exemple un carré de 200x200 au centre)
        center_x, center_y = img_array.shape[1] // 2, img_array.shape[0] // 2
        zoom_size = 200
        zoomed_img_array = img_array[center_y - zoom_size//2 : center_y + zoom_size//2,
                                     center_x - zoom_size//2 : center_x + zoom_size//2]

        # Afficher les dimensions de l'image zoomée et les pixels
        print(f"Nouvelle taille après zoom : {zoomed_img_array.shape}")
        print(f"Pixels après zoom :\n{zoomed_img_array}")

        return zoomed_img_array

    except FileNotFoundError:
        print(f"Erreur : L'image '{path}' n'a pas été trouvée.")
        return None
    except IOError:
        print(f"Erreur : Impossible de lire le fichier '{path}'.")
        return None
