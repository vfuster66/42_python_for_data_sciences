import numpy as np
from printer import print_title, print_info, print_success, print_failure


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    Calcule l'IMC (Indice de Masse Corporelle)
    pour une liste de tailles (mètres) et de poids (kg).
    Retourne une liste d'IMC.
    """
    print_title("Calcul BMI")
    print_info(f"Tailles : {height}")
    print_info(f"Poids : {weight}")

    if len(height) != len(weight):
        msg = "Les listes 'height' et 'weight' doivent avoir la même taille."
        print_failure(msg)
        raise ValueError(msg)

    try:
        height_arr = np.array(height, dtype=float)
        weight_arr = np.array(weight, dtype=float)
    except ValueError as e:
        print_failure(f"Erreur de conversion des entrées : {e}")
        raise

    bmi = weight_arr / (height_arr ** 2)
    print_success(f"BMI calculé : {bmi.tolist()}")
    return bmi.tolist()


def apply_limit(bmi: list[float], limit: float) -> list[bool]:
    """
    Retourne une liste de booléens où True
    signifie que l'IMC est supérieur à la limite.
    """
    print_title(f"Application de la limite : {limit}")
    print_info(f"Liste des BMI : {bmi}")

    bmi_arr = np.array(bmi)
    result = (bmi_arr > limit).tolist()

    print_success(f"Résultat après application de la limite : {result}")
    return result
