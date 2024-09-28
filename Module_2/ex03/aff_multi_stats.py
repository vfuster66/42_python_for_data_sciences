import matplotlib.pyplot as plt
import pandas as pd
import os
import webbrowser
from load_csv import load

def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files. It focuses on data from
    the year 1900 and visualizes the correlation between GNP and life
    expectancy through a scatter plot.
    """
    # Charger les fichiers CSV pour le GNP et l'espérance de vie
    income_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_file = "life_expectancy_years.csv"

    income_data = load(income_file)
    life_expectancy_data = load(life_expectancy_file)

    if income_data is None or life_expectancy_data is None:
        print("Erreur lors du chargement des fichiers.")
        return

    year_1900_column = '1900'

    if year_1900_column not in income_data.columns or year_1900_column not in life_expectancy_data.columns:
        print(f"Erreur : La colonne '{year_1900_column}' n'existe pas dans l'un des fichiers.")
        return

    # Sélectionner les données pour l'année 1900
    income_1900 = income_data[['country', year_1900_column]].dropna()
    life_expectancy_1900 = life_expectancy_data[['country', year_1900_column]].dropna()

    # Fusionner les deux datasets sur la colonne 'country'
    merged_data = pd.merge(income_1900, life_expectancy_1900, on='country', how='inner')
    merged_data.columns = ['country', 'gnp_1900', 'life_expectancy_1900']

    # Créer le graphique de projection
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['gnp_1900'], merged_data['life_expectancy_1900'], alpha=0.6)
    plt.title("Life expectancy vs Gross domestic product (Year 1900)")
    plt.xlabel("Gross domestic product (GNP per capita)")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarder le graphique dans un fichier PNG
    file_name = "projection_life_expectancy_1900.png"
    plt.savefig(file_name)
    print(f"Graphique sauvegardé sous {file_name}")

    # Ouvrir l'image dans un viewer externe
    if os.path.exists(file_name):
        webbrowser.open(file_name)
    else:
        print(f"Erreur : Le fichier {file_name} n'a pas pu être créé.")

if __name__ == "__main__":
    main()
