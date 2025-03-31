import argparse
from ex02.aff_stats import plot_population
from ex00.load_csv import load


def main():
    parser = argparse.ArgumentParser(
        description="Comparer la population de deux pays au fil du temps."
    )
    parser.add_argument("country1", help="Premier pays (ex: France)")
    parser.add_argument("country2", help="Deuxième pays (ex: Germany)")
    args = parser.parse_args()

    data = load("ex02/population_total.csv")
    if data is not None:
        plot_population(args.country1, args.country2, data)


if __name__ == "__main__":
    main()
