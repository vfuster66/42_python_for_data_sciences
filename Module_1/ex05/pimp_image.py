import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre négatif à l'image (inversion des couleurs).
    Utilise uniquement les opérateurs =, +, -, *
    """
    try:
        # Inverser les couleurs en utilisant l'opérateur - (255 - valeur)
        return 255 - array
    except Exception as e:
        print(f"Erreur dans ft_invert : {e}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre rouge à l'image en multipliant le canal rouge.
    Utilise uniquement les opérateurs =, *
    """
    try:
        red_filter = np.zeros_like(array)
        red_filter[:, :, 0] = array[:, :, 0]
        return red_filter
    except Exception as e:
        print(f"Erreur dans ft_red : {e}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre vert à l'image en soustrayant les autres canaux.
    Utilise uniquement les opérateurs =, -
    """
    try:
        green_filter = np.zeros_like(array)
        green_filter[:, :, 1] = array[:, :, 1]
        return green_filter
    except Exception as e:
        print(f"Erreur dans ft_green : {e}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre bleu à l'image en gardant uniquement le canal bleu.
    Utilise uniquement l'opérateur =
    """
    try:
        blue_filter = np.zeros_like(array)
        blue_filter[:, :, 2] = array[:, :, 2]
        return blue_filter
    except Exception as e:
        print(f"Erreur dans ft_blue : {e}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre gris en calculant la moyenne des trois canaux
    (niveaux de gris). Utilise uniquement les opérateurs =, /
    """
    try:
        # Calculer la moyenne des trois canaux et
        # répéter cette valeur pour chaque canal
        grey_filter = np.mean(array, axis=2, keepdims=True)
        grey_filter = np.repeat(grey_filter, 3, axis=2)
        return grey_filter.astype(np.uint8)
    except Exception as e:
        print(f"Erreur dans ft_grey : {e}")
        return None
