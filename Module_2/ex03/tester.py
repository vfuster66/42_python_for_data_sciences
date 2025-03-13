import argparse
import pandas as pd
from ex00.load_csv import load
from ex03.aff_multi_stats import display_graph
from printer import print_title, print_info, print_failure


def main(country1: str = "France", country2: str = "Belgium") -> None:
    """Main function to load data and display graph."""
    print_title("Ex03 ➜ Projection Life Expectancy vs GDP")

    income_file = (
        "ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_file = "ex03/life_expectancy_years.csv"

    income_data = load(income_file)
    life_expectancy_data = load(life_expectancy_file)

    if income_data is None or life_expectancy_data is None:
        print_failure("❌ Impossible de charger les fichiers de données.")
        return

    year_1900_column = '1900'

    if year_1900_column not in income_data.columns:
        print_failure(
            f"❌ La colonne '{year_1900_column}' est manquante dans "
            f"{income_file}."
        )
        return

    if year_1900_column not in life_expectancy_data.columns:
        print_failure(
            f"❌ La colonne '{year_1900_column}' est manquante dans "
            f"{life_expectancy_file}."
        )
        return

    # Merge data on country
    income_1900 = income_data[['country', year_1900_column]].dropna()
    life_expectancy_1900 = life_expectancy_data[
        ['country', year_1900_column]
    ].dropna()

    merged_data = pd.merge(income_1900, life_expectancy_1900, on='country',
                           how='inner')
    merged_data.columns = ['country', 'gnp_1900', 'life_expectancy_1900']

    if merged_data.empty:
        print_failure("❌ Pas de données disponibles après la fusion !")
        return

    print_info(f"🔎 Données fusionnées : {len(merged_data)} pays disponibles.")

    # Afficher et sauvegarder le graphique
    display_graph(merged_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Projection Life Expectancy vs GDP (1900)"
    )
    args = parser.parse_args()

    main()
