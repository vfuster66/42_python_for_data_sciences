# ex04/tester.py

import sys
from rotate import ft_rotate
from printer import print_title, print_info, print_failure, print_success


def main():
    # Vérification argument image
    image_path = None
    for arg in sys.argv:
        if arg.startswith("image="):
            image_path = arg.split("=", 1)[1]

    if not image_path:
        print_failure("❌ Aucun chemin d'image fourni !")
        print_info("👉 Exemple : make ex04 image=ex04/animal.jpeg")
        return

    print_title("Ex04 ➜ Tester ft_rotate()")
    print_info(f"Chargement de l'image : {image_path}\n")

    transposed = ft_rotate(image_path)

    if transposed is not None:
        print_success(f"✅ Rotation réussie : {transposed.shape}")
    else:
        print_failure("❌ Échec de la rotation")


if __name__ == "__main__":
    main()
