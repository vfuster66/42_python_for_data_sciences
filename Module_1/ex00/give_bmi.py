import numpy as np
from typing import Union


def give_bmi(height: list[Union[int, float]],
             weight: list[Union[int, float]]) -> list[Union[int, float]]:
    if len(height) != len(weight):
        raise ValueError("Lists must be of same length")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height list contains non-numeric value")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight list contains non-numeric value")

    h_arr = np.array(height, dtype=float)
    w_arr = np.array(weight, dtype=float)
    return (w_arr / (h_arr ** 2)).tolist()


def apply_limit(bmi: list[Union[int, float]], limit: int) -> list[bool]:
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list contains non-numeric value")

    return (np.array(bmi) > limit).tolist()

