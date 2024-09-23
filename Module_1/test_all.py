# test_all.py

import sys
import os

# Ajouter les dossiers ex00, ex01, ... au PATH pour les imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex00'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex01'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex02'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex03'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex04'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex05'))

# Import des tests pour chaque exercice
from give_bmi import give_bmi, apply_limit
from array2D import slice_me
from load_image import ft_load
from zoom import ft_zoom
from rotate import ft_rotate
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def test_ex00():
    print("Testing Exercise 00 - BMI")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print("BMI:", bmi)
    print("Apply Limit:", apply_limit(bmi, 26))
    print()

def test_ex01():
    print("Testing Exercise 01 - 2D Array")
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print()

def test_ex02():
    print("Testing Exercise 02 - Load Image")
    print(ft_load("landscape.jpg"))
    print()

def test_ex03():
    print("Testing Exercise 03 - Zoom Image")
    ft_zoom("animal.jpeg")
    print()

def test_ex04():
    print("Testing Exercise 04 - Rotate Image")
    ft_rotate("animal.jpeg")
    print()

def test_ex05():
    print("Testing Exercise 05 - Pimp My Image")
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print("Image processing completed.")
    print()

if __name__ == "__main__":
    print("Running all tests...")
    test_ex00()
    test_ex01()
    test_ex02()
    test_ex03()
    test_ex04()
    test_ex05()
    print("All tests completed.")
