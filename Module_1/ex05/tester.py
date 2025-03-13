import sys
import numpy as np
from PIL import Image
from ex02.load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from printer import print_title, print_info, print_success, print_failure


def save_image(array: np.ndarray, filename: str):
    """Sauvegarde une image à partir d'un array"""
    try:
        img = Image.fromarray(array.astype(np.uint8))
        img.save(filename)
        print_success(f"✅ ✅ Image sauvegardée : {filename}")
    except Exception as e:
        print_failure(
            f"❌ ❌ Impossible de sauvegarder l'image {filename} : {e}"
        )


def main():
    args = sys.argv[1:]
    image_path = None

    for arg in args:
        if arg.startswith("image="):
            image_path = arg.split("=", 1)[1]

    if not image_path:
        print_failure("❌ ❌ Aucun chemin d'image fourni !")
        print_info("🔎 👉 Exemple : make ex05 image=ex05/landscape.jpg")
        return

    print_title("=== Ex05 ➜ Tester pimp_image ===")
    print_info(f"🔎 Chargement de l'image : {image_path}")

    array = ft_load(image_path)
    if array is None:
        print_failure("❌ ❌ Impossible de charger l'image.")
        return

    print_success(f"✅ ✅ Image chargée avec succès : {array.shape}")

    filters = {
        "inverted": ft_invert(array),
        "red": ft_red(array),
        "green": ft_green(array),
        "blue": ft_blue(array),
        "grey": ft_grey(array)
    }

    for name, result in filters.items():
        if result is None:
            print_failure(f"❌ ❌ Filtre {name} échoué !")
        else:
            save_image(result, f"{name}_image.png")

    print_info("🔎 Tests de pimp_image terminés.\n")


if __name__ == "__main__":
    main()
