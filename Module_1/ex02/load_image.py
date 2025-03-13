from PIL import Image
import numpy as np
from printer import print_title, print_info, print_success, print_failure


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis un chemin donné,
    imprime son format et retourne son contenu en RGB.
    Gère les erreurs si le fichier n'est pas trouvable
    ou si le format n'est pas supporté.
    """
    print_title(f"Chargement de l'image : {path}")

    try:
        img = Image.open(path)
        print_info(f"Format de l'image : {img.format}")

        img = img.convert("RGB")
        img_array = np.array(img)

        print_success("✅ Image convertie en RGB avec succès")
        print_info(f"Dimensions de l'image : {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print_failure(f"❌ Erreur : L'image '{path}' n'a pas été trouvée.")
        return None
    except IOError as e:
        print_failure(f"❌ Erreur : Impossible de lire le fichier '{path}'. "
                      f"{e}")
        return None
