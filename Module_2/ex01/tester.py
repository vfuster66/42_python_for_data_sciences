import argparse
from aff_life import display_life_expectancy
from ex00.load_csv import load
from printer import print_title, print_failure


def main():
    print_title("Ex01 ➜ Afficher l'espérance de vie par pays")

    parser = argparse.ArgumentParser(
        description="Afficher la life expectancy d'un pays"
    )
    parser.add_argument("country", help="Nom du pays à afficher (ex: France)")
    args = parser.parse_args()

    data = load("ex01/life_expectancy_years.csv")
    if data is None:
        print_failure("Erreur lors du chargement des données.")
        return

    display_life_expectancy(args.country, data)


if __name__ == "__main__":
    main()
