# ex04/rotate.py

import numpy as np
import matplotlib.pyplot as plt
from PIL import UnidentifiedImageError
from ex02.load_image import ft_load
from printer import print_title, print_info, print_success, print_failure


def ft_rotate(path: str) -> np.ndarray | None:
    """
    Charge une image, effectue un découpage carré, transpose et sauvegarde.
    """
    print_title(f"Rotation de l'image : {path}")

    try:
        img_array = ft_load(path)
        if img_array is None:
            print_failure("❌ Impossible de charger l'image.")
            return None

        print_info(f"Image chargée : {img_array.shape}")

        # Découpage carré
        center_x, center_y = img_array.shape[1] // 2, img_array.shape[0] // 2
        square_size = 400
        square_img_array = img_array[
            center_y - square_size // 2:center_y + square_size // 2,
            center_x - square_size // 2:center_x + square_size // 2]

        print_info(f"Zone découpée : {square_img_array.shape}")

        # Transposer manuellement
        transposed_img_array = np.transpose(square_img_array, axes=(1, 0, 2))
        print_info(f"Après transposition : {transposed_img_array.shape}")

        # Sauvegarder l'image
        fig, ax = plt.subplots()
        im = ax.imshow(transposed_img_array)
        ax.set_title("Image transposée")
        ax.set_xlabel("Axe X")
        ax.set_ylabel("Axe Y")
        plt.grid(True)
        plt.colorbar(im)

        output_file = "transposed_image_with_axes.png"
        fig.savefig(output_file)
        plt.close(fig)

        print_success(f"✅ Image transposée sauvegardée sous : {output_file}")

        return transposed_img_array

    except FileNotFoundError:
        print_failure(f"❌ Le fichier '{path}' n'a pas été trouvé.")
    except UnidentifiedImageError:
        print_failure(
            f"❌ Le fichier '{path}' n'est pas un format d'image valide.")
    except Exception as e:
        print_failure(f"❌ Erreur inattendue : {e}")

    return None
