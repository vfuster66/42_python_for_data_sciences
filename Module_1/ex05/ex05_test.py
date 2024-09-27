import os
import numpy as np
from PIL import Image
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


# Charger l'image de test
def test_load_image(image_path):
    array = ft_load(image_path)
    if array is None:
        print(f"Erreur : L'image '{image_path}' n'a pas pu être chargée.")
        return None
    return array


# Appliquer les filtres et sauvegarder les images
def test_apply_filters(array):
    filters = {
        "inverted": ft_invert(array),
        "red_filter": ft_red(array),
        "green_filter": ft_green(array),
        "blue_filter": ft_blue(array),
        "grey_filter": ft_grey(array),
    }

    for filter_name, filtered_image in filters.items():
        # Sauvegarder l'image filtrée
        filename = f"{filter_name}.png"
        img = Image.fromarray(filtered_image.astype(np.uint8))
        img.save(filename)
        print(f"L'image avec le filtre '{filter_name}' a été "
              f"sauvegardée sous '{filename}'.")

        # Vérifier que le fichier a bien été créé
        if not os.path.exists(filename):
            print(f"Erreur : Le fichier '{filename}' n'a pas été créé.")
        else:
            print(f"Le fichier '{filename}' a été vérifié avec succès.")


# Tester les comportements pour des fichiers inexistants ou mauvais format
def test_invalid_files():
    # Test avec une image inexistante
    print("\n--- Test avec une image inexistante ---")
    non_existent_image = "image_inexistante.jpg"
    result = ft_load(non_existent_image)
    if result is None:
        print(f"Test réussi : Le fichier inexistant '{non_existent_image}' "
              f"a déclenché l'erreur correcte.")
    else:
        print("Erreur : Le fichier inexistant n'a pas déclenché "
              "le bon message d'erreur.")

    # Test avec un fichier texte
    print("\n--- Test avec un fichier au mauvais format (texte) ---")
    with open("fichier_texte.txt", "w") as f:
        f.write("Ceci est un fichier texte, pas une image.")

    result = ft_load("fichier_texte.txt")
    if result is None:
        print("Test réussi : Le fichier au mauvais format "
              "'fichier_texte.txt' a déclenché l'erreur correcte.")
    else:
        print("Erreur : Le fichier au mauvais format n'a pas déclenché "
              "le bon message d'erreur.")

    # Nettoyage
    if os.path.exists("fichier_texte.txt"):
        os.remove("fichier_texte.txt")


# Nettoyer les fichiers générés après le test
def cleanup_files():
    filters = ["inverted", "red_filter", "green_filter", "blue_filter",
               "grey_filter"]
    for filter_name in filters:
        filename = f"{filter_name}.png"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Fichier '{filename}' supprimé après le test.")


# Fonction principale pour exécuter tous les tests
def run_tests():
    image_path = "landscape.jpg"

    # Test du chargement de l'image
    print("\n--- Test du chargement de l'image ---")
    array = test_load_image(image_path)

    if array is not None:
        # Appliquer les filtres et sauvegarder les images
        print("\n--- Test des filtres et de la sauvegarde des images ---")
        test_apply_filters(array)

    # Tester les fichiers inexistants ou mauvais formats
    test_invalid_files()

    # Nettoyer les fichiers générés après les tests
    # cleanup_files()


if __name__ == "__main__":
    run_tests()
