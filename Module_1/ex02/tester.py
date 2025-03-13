import sys
from load_image import ft_load
from printer import print_title, print_info, print_success, print_failure


def main():
    print_title("Ex02 ➜ Tester ft_load")

    # Valeur par défaut si aucun argument n'est passé
    image_path = "ex02/landscape.jpg"

    # Parcours des arguments (image=...)
    for arg in sys.argv[1:]:
        if arg.startswith("image="):
            image_path = arg.split("=", 1)[1]

    # Si le chemin est vide ou None, on affiche l'erreur et le help
    if not image_path:
        print_failure("❌ Aucun chemin d'image spécifié.\n")
        print_info("👉 Exemple de commande :")
        print_info("make ex02 image=ex02/landscape.jpg\n")
        return

    print_info(f"Chargement de l'image : {image_path}\n")

    # Chargement de l'image
    img_array = ft_load(image_path)

    if img_array is not None:
        print_success(f"✅ Image chargée avec succès : {img_array.shape}\n")
    else:
        print_failure(f"❌ Échec du chargement de l'image : {image_path}\n")
        print_info("👉 Vérifiez le chemin fourni ou utilisez :")
        print_info("make ex02 image=ex02/landscape.jpg\n")


if __name__ == "__main__":
    main()
