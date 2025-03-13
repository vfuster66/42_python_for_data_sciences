import argparse
from ex00.load_csv import load
from aff_stats import plot_population
from printer import print_title, print_info, print_failure


def main():
    print_title("Ex02 ➜ Comparaison de population entre deux pays")

    parser = argparse.ArgumentParser(
        description="Comparer la population entre deux pays"
    )
    parser.add_argument("country1", help="Premier pays (ex: France)")
    parser.add_argument("country2", help="Deuxième pays (ex: Belgium)")
    args = parser.parse_args()

    data = load("ex02/population_total.csv")
    if data is None:
        print_failure("Erreur lors du chargement du fichier CSV.")
        return

    print_info(f"Comparaison entre {args.country1} et {args.country2}")
    plot_population(args.country1, args.country2, data)


if __name__ == "__main__":
    main()
