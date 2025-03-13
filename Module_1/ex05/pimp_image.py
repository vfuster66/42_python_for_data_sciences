import numpy as np
from printer import print_info, print_success, print_failure


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Applique un filtre négatif à l'image (inversion des couleurs)."""
    try:
        print_info("🔎 Application du filtre : Invert")
        result = 255 - array
        print_success("✅ ✅ Filtre invert appliqué avec succès !")
        return result
    except Exception as e:
        print_failure(f"❌ ❌ Erreur dans ft_invert : {e}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applique un filtre rouge à l'image."""
    try:
        print_info("🔎 Application du filtre : Red")
        red_filter = np.zeros_like(array)
        red_filter[:, :, 0] = array[:, :, 0]
        print_success("✅ ✅ Filtre red appliqué avec succès !")
        return red_filter
    except Exception as e:
        print_failure(f"❌ ❌ Erreur dans ft_red : {e}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applique un filtre vert à l'image."""
    try:
        print_info("🔎 Application du filtre : Green")
        green_filter = np.zeros_like(array)
        green_filter[:, :, 1] = array[:, :, 1]
        print_success("✅ ✅ Filtre green appliqué avec succès !")
        return green_filter
    except Exception as e:
        print_failure(f"❌ ❌ Erreur dans ft_green : {e}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applique un filtre bleu à l'image."""
    try:
        print_info("🔎 Application du filtre : Blue")
        blue_filter = np.zeros_like(array)
        blue_filter[:, :, 2] = array[:, :, 2]
        print_success("✅ ✅ Filtre blue appliqué avec succès !")
        return blue_filter
    except Exception as e:
        print_failure(f"❌ ❌ Erreur dans ft_blue : {e}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Applique un filtre gris à l'image."""
    try:
        print_info("🔎 Application du filtre : Grey")
        grey_filter = np.mean(array, axis=2, keepdims=True)
        grey_filter = np.repeat(grey_filter, 3, axis=2)
        print_success("✅ ✅ Filtre grey appliqué avec succès !")
        return grey_filter.astype(np.uint8)
    except Exception as e:
        print_failure(f"❌ ❌ Erreur dans ft_grey : {e}")
        return None
