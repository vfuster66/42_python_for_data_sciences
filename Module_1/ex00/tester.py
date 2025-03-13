from ex00.give_bmi import give_bmi, apply_limit
from printer import print_title, print_success


def main():
    print_title("Ex00 ➜ Tester give_bmi et apply_limit")

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print_success(f"✅ BMI calculé : {bmi}")

    result = apply_limit(bmi, 26)
    print_success(f"✅ Résultat apply_limit : {result}")


if __name__ == "__main__":
    main()
