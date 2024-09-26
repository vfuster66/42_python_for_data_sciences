from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_rotate(path: str) -> np.ndarray:
    """
    Charge une image, découpe une zone carrée, effectue
    une transposition et affiche l'image transposée.
    """
    # Charger l'image en utilisant ft_load de load_image.py
    img_array = ft_load(path)
    if img_array is None:
        print("Échec du chargement de l'image.")
        return None

    # Définir une zone de découpe carrée\
    # (par exemple un carré de 400x400 au centre)
    center_x, center_y = img_array.shape[1] // 2, img_array.shape[0] // 2
    square_size = 400
    square_img_array = img_array[
        center_y - square_size//2: center_y + square_size//2,
        center_x - square_size//2: center_x + square_size//2]

    # Afficher les dimensions de l'image découpée
    print(f"La forme de l'image est : {square_img_array.shape}")

    # Transposer l'image découpée (échanger les lignes et colonnes)
    transposed_img_array = np.transpose(square_img_array, axes=(1, 0, 2))

    # Afficher les dimensions après transposition
    print(f"Forme après la transposition :{transposed_img_array.shape}")

    # Créer une figure avec matplotlib
    fig, ax = plt.subplots()
    ax.imshow(transposed_img_array)
    ax.set_title("Image transposée")
    ax.set_xlabel("Axe X")
    ax.set_ylabel("Axe Y")
    plt.grid(True)
    plt.colorbar(ax.imshow(transposed_img_array))

    # Sauvegarder la figure avec les axes et échelles
    fig.savefig("transposed_image_with_axes.png")

    # Utiliser PIL pour ouvrir et afficher l'image sauvegardée
    transposed_img_with_axes = Image.open("transposed_image_with_axes.png")
    transposed_img_with_axes.show()

    return transposed_img_array


if __name__ == "__main__":
    image_path = "animal.jpeg"
    ft_rotate(image_path)
