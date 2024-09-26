from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_zoom(path: str) -> np.ndarray:
    """
    Charge une image, imprime ses dimensions, effectue un zoom et affiche
    l'image avec les axes X et Y.
    """
    # Charger l'image en utilisant ft_load de load_image.py
    img_array = ft_load(path)
    if img_array is None:
        print("Échec du chargement de l'image.")
        return None

    # Afficher les dimensions de l'image chargée
    print(f"Taille de l'image : {img_array.shape[1]}x{img_array.shape[0]}")
    print(f"Nombre de canaux : {img_array.shape[2]}")

    # Définir une zone de zoom (par exemple un carré de 200x200 au centre)
    center_x, center_y = img_array.shape[1] // 2, img_array.shape[0] // 2
    zoom_size = 200
    zoomed_img_array = img_array[
        center_y - zoom_size//2: center_y + zoom_size//2,
        center_x - zoom_size//2: center_x + zoom_size//2]

    # Afficher les dimensions de l'image zoomée et les pixels
    print(f"Nouvelle taille après zoom : {zoomed_img_array.shape}")

    # Créer une figure avec matplotlib
    fig, ax = plt.subplots()
    ax.imshow(zoomed_img_array)
    ax.set_title("Image zoomée")
    ax.set_xlabel("Axe X")
    ax.set_ylabel("Axe Y")
    plt.grid(True)
    plt.colorbar(ax.imshow(zoomed_img_array))

    # Sauvegarder la figure avec les axes et échelles
    fig.savefig("zoomed_image_with_axes.png")

    # Utiliser PIL pour ouvrir et afficher l'image sauvegardée
    zoomed_img_with_axes = Image.open("zoomed_image_with_axes.png")
    zoomed_img_with_axes.show()

    return zoomed_img_array


if __name__ == "__main__":
    image_path = "animal.jpeg"
    ft_zoom(image_path)
