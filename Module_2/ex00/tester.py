from ex00.load_csv import load
from printer import print_title, print_success


def main():
    print_title("Ex00 ➜ Tester load_csv")

    dataset = load("ex00/life_expectancy_years.csv")
    if dataset is not None:
        print_success("Chargement réussi ✅")
        print(dataset.head())


if __name__ == "__main__":
    main()
