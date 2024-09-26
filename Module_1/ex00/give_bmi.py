# give_bmi.py

import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    Calcule l'IMC (Indice de Masse Corporelle)
    pour une liste de tailles (mètres) et de poids (kg).
    Retourne une liste d'IMC.
    """
    if len(height) != len(weight):
        raise ValueError("Les listes 'height' \
                         et 'weight' doivent avoir la même taille.")

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    # Calcul de l'IMC : poids / (taille ^ 2)
    bmi = weight_arr / (height_arr ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[float], limit: float) -> list[bool]:
    """
    Retourne une liste de booléens où True \
        signifie que l'IMC est supérieur à la limite.
    """
    bmi_arr = np.array(bmi)
    return (bmi_arr > limit).tolist()
