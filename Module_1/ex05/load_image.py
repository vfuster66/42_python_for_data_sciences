from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis un chemin donné,
    imprime son format et retourne son contenu en RGB.
    Gère les erreurs si le fichier n'est pas trouvable
    ou si le format n'est pas supporté.
    """
    try:
        # Ouvrir l'image
        img = Image.open(path)
        print(f"Format de l'image : {img.format}")

        # Convertir l'image en RGB si nécessaire
        img = img.convert("RGB")

        # Obtenir le contenu de l'image en tant que tableau numpy
        img_array = np.array(img)
        print(f"Contenu de l'image (pixels en RGB) :\n{img_array}")

        return img_array

    except FileNotFoundError:
        print(f"Erreur : L'image '{path}' n'a pas été trouvée.")
        return None
    except UnidentifiedImageError:
        print(f"Erreur : Le fichier '{path}' n'est pas un format d'image "
              f"valide.")
        return None
    except IOError:
        print(f"Erreur : Impossible de lire le fichier '{path}'.")
        return None
