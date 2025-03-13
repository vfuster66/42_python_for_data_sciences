from ex02.load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str) -> np.ndarray:
    """
    Charge une image, imprime ses dimensions, effectue un zoom et sauvegarde
    l'image zoomée avec les axes X et Y.
    """
    # Charger l'image en utilisant ft_load de load_image.py
    img_array = ft_load(path)
    if img_array is None:
        print("Échec du chargement de l'image.")
        return None

    print(f"Taille de l'image : {img_array.shape[1]}x{img_array.shape[0]}")
    print(f"Nombre de canaux : {img_array.shape[2]}")

    center_x, center_y = img_array.shape[1] // 2, img_array.shape[0] // 2
    zoom_size = 200
    zoomed_img_array = img_array[
        center_y - zoom_size // 2: center_y + zoom_size // 2,
        center_x - zoom_size // 2: center_x + zoom_size // 2]

    print(f"Nouvelle taille après zoom : {zoomed_img_array.shape}")

    fig, ax = plt.subplots()
    im = ax.imshow(zoomed_img_array)
    ax.set_title("Image zoomée")
    ax.set_xlabel("Axe X")
    ax.set_ylabel("Axe Y")
    plt.grid(True)
    plt.colorbar(im)

    output_file = "zoomed_image_with_axes.png"
    fig.savefig(output_file)
    print(f"Image zoomée sauvegardée dans '{output_file}'")

    plt.close(fig)

    return zoomed_img_array
