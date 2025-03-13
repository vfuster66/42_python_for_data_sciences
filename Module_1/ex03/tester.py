import sys
from zoom import ft_zoom
from printer import print_title, print_info, print_success, print_failure


def main():
    print_title("Ex03 ➜ Tester ft_zoom")

    # Récupérer le chemin de l'image depuis les arguments
    image_path = None
    for arg in sys.argv[1:]:
        if arg.startswith("image="):
            image_path = arg.split("=", 1)[1]

    if not image_path:
        print_failure("❌ Aucun chemin d'image fourni !\n")
        print_info("👉 Exemple : make ex03 image=ex03/animal.jpeg\n")
        return

    print_info(f"Chargement de l'image : {image_path}\n")

    zoomed_img = ft_zoom(image_path)

    if zoomed_img is not None:
        print_success(f"✅ Zoom effectué avec succès : {zoomed_img.shape}\n")
    else:
        print_failure("❌ Échec du zoom sur l'image.\n")


if __name__ == "__main__":
    main()
