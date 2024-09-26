import numpy as np


# Inversion des couleurs
def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverse les couleurs de l'image (filtre de négatif).
    """
    return 255 - array


# Garder uniquement le canal rouge
def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre rouge à l'image.
    """
    red_filter = np.zeros_like(array)
    red_filter[:, :, 0] = array[:, :, 0]
    return red_filter


# Garder uniquement le canal vert
def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre vert à l'image.
    """
    green_filter = np.zeros_like(array)
    green_filter[:, :, 1] = array[:, :, 1]
    return green_filter


# Garder uniquement le canal bleu
def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre bleu à l'image.
    """
    blue_filter = np.zeros_like(array)
    blue_filter[:, :, 2] = array[:, :, 2]
    return blue_filter


# Moyenne des trois canaux
# Répéter la valeur pour les trois canaux
def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applique un filtre gris (niveaux de gris) à l'image.
    """
    grey_filter = np.mean(array, axis=2, keepdims=True)
    grey_filter = np.repeat(grey_filter, 3, axis=2)
    return grey_filter.astype(np.uint8)
