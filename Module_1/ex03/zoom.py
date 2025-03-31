import numpy as np
import matplotlib.pyplot as plt
from ex02.load_image import ft_load


def ft_zoom(path: str) -> np.ndarray:
    """
    Charge une image, affiche sa shape, effectue un zoom 400x400 sur un canal,
    affiche la nouvelle shape et les données de pixels.
    Sauvegarde l'image zoomée avec des axes.
    """
    img = ft_load(path)
    if img is None:
        print("❌ Échec du chargement de l'image.")
        return None

    # Affichage de la forme initiale
    print(f"The shape of image is: {img.shape}")
    print(img)

    try:
        # Zoom centré, 400x400 sur le canal R (canal 0)
        center_y, center_x = img.shape[0] // 2, img.shape[1] // 2
        zoom = img[
            center_y - 200:center_y + 200,
            center_x - 200:center_x + 200,
            0:1  # on garde la 3e dimension
        ]

        # Affichage de la forme après slicing
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)

        # Affichage graphique (sauvegarde dans un fichier)
        fig, ax = plt.subplots()
        im = ax.imshow(zoom, cmap="gray")
        ax.set_title("Zoom sur l'image")
        ax.set_xlabel("Axe X")
        ax.set_ylabel("Axe Y")
        plt.colorbar(im)
        plt.grid(True)

        fig.savefig("ex03/zoomed_image.png")
        plt.close(fig)

        return zoom

    except Exception as e:
        print(f"❌ Erreur pendant le zoom : {e}")
        return None


def main():
    image_path = "ex03/animal.jpeg"
    ft_zoom(image_path)


if __name__ == "__main__":
    main()
