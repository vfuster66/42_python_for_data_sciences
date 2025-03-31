import numpy as np
import matplotlib.pyplot as plt


def save_image(image: np.ndarray, filename: str):
    """Sauvegarde l'image filtrée dans le dossier ex05."""
    try:
        plt.imsave(f"ex05/{filename}", image.astype(np.uint8))
        print(f"💾 Image enregistrée : ex05/{filename}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de {filename} : {e}")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    try:
        print("🔎 Application du filtre : Invert")
        result = 255 - array
        save_image(result, "filtered_invert.jpg")
        print("✅ Filtre invert appliqué avec succès !")
        return result
    except Exception as e:
        print(f"❌ Erreur dans ft_invert : {e}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel."""
    try:
        print("🔎 Application du filtre : Red")
        red_filter = np.zeros_like(array)
        red_filter[:, :, 0] = array[:, :, 0]
        save_image(red_filter, "filtered_red.jpg")
        print("✅ Filtre red appliqué avec succès !")
        return red_filter
    except Exception as e:
        print(f"❌ Erreur dans ft_red : {e}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel."""
    try:
        print("🔎 Application du filtre : Green")
        green_filter = np.zeros_like(array)
        green_filter[:, :, 1] = array[:, :, 1]
        save_image(green_filter, "filtered_green.jpg")
        print("✅ Filtre green appliqué avec succès !")
        return green_filter
    except Exception as e:
        print(f"❌ Erreur dans ft_green : {e}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel."""
    try:
        print("🔎 Application du filtre : Blue")
        blue_filter = np.zeros_like(array)
        blue_filter[:, :, 2] = array[:, :, 2]
        save_image(blue_filter, "filtered_blue.jpg")
        print("✅ Filtre blue appliqué avec succès !")
        return blue_filter
    except Exception as e:
        print(f"❌ Erreur dans ft_blue : {e}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    try:
        print("🔎 Application du filtre : Grey")
        grey = np.mean(array, axis=2, keepdims=True)
        grey_filter = np.repeat(grey, 3, axis=2)
        grey_filter = grey_filter.astype(np.uint8)
        save_image(grey_filter, "filtered_grey.jpg")
        print("✅ Filtre grey appliqué avec succès !")
        return grey_filter
    except Exception as e:
        print(f"❌ Erreur dans ft_grey : {e}")
        return None
