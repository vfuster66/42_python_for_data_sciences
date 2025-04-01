import argparse
from aff_life import display_life_expectancy
from ex00.load_csv import load


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Afficher l'espérance de vie d'un pays à partir d'un fichier CSV."
        )
    )
    parser.add_argument("country", help="Nom du pays à afficher (ex: France)")
    args = parser.parse_args()

    data = load("ex01/life_expectancy_years.csv")
    if data is not None:
        display_life_expectancy(args.country, data)
    else:
        print("❌ Erreur de chargement des données.")


if __name__ == "__main__":
    main()
