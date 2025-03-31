from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis un chemin donné,
    imprime son format et retourne son contenu en RGB.
    Gère les erreurs si le fichier n'est pas trouvable
    ou si le format n'est pas supporté.
    """

    try:
        img = Image.open(path)

        img = img.convert("RGB")
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print(f"❌ Erreur : L'image '{path}' n'a pas été trouvée.")
        return None
    except IOError as e:
        print(f"❌ Erreur : Impossible de lire le fichier '{path}'. {e}")
        return None

