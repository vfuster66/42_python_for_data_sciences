# tester.py

from load_image import ft_load


def main():
    # Chemin vers l'image de test
    # (assure-toi qu'elle soit présente dans le répertoire)
    image_path = "landscape.jpg"

    # Charger l'image
    img_array = ft_load(image_path)

    if img_array is not None:
        print(f"Image loaded successfully: Shape = {img_array.shape}")


if __name__ == "__main__":
    main()
