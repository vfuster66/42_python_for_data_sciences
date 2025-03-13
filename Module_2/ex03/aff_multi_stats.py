import matplotlib.pyplot as plt
import pandas as pd
import os
import webbrowser
from ex00.load_csv import load
from printer import print_title, print_info, print_success, print_failure


def display_graph(data, show_browser=True):
    """
    Affiche le graphique de l'espérance de vie vs PIB par habitant en 1900.

    Args:
        data (pd.DataFrame): Dataset contenant les colonnes gnp_1900
            et life_expectancy_1900.
        show_browser (bool): Si True, ouvre l'image dans le navigateur.
            False pour les tests.
    """
    print_title("Affichage du graphique : Life expectancy vs GDP (1900)")

    plt.figure(figsize=(10, 6))
    plt.scatter(data['gnp_1900'], data['life_expectancy_1900'], alpha=0.6)

    plt.title("Life expectancy vs Gross domestic product (Year 1900)")
    plt.xlabel("Gross domestic product (GNP per capita)")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.grid(True)
    plt.tight_layout()

    filename = "projection_life_expectancy_1900.png"
    plt.savefig(filename)
    print_success(f"✅ Graphique sauvegardé : {filename}")

    if show_browser:
        if os.path.exists(filename):
            webbrowser.open(filename)
            print_info("🔎 Ouverture du graphique dans le navigateur.")
        else:
            print_failure(f"❌ Erreur : Le fichier {filename} n'existe pas.")


def main():
    """
    Charge les datasets et affiche le graphique pour l'année 1900.
    """
    print_title("Ex03 ➜ Afficher life expectancy vs GDP (1900)")

    income_file = (
        "ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_file = "ex03/life_expectancy_years.csv"

    print_info(
        f"🔎 Chargement des fichiers :\n - {income_file}\n - {life_file}")

    income_data = load(income_file)
    life_data = load(life_file)

    if income_data is None or life_data is None:
        print_failure("❌ Erreur lors du chargement des fichiers CSV.")
        return

    year = "1900"

    if year not in income_data.columns or year not in life_data.columns:
        print_failure(f"❌ Colonne {year} manquante dans les fichiers CSV.")
        return

    income_1900 = income_data[['country', year]].dropna()
    life_exp_1900 = life_data[['country', year]].dropna()

    merged = pd.merge(income_1900, life_exp_1900, on="country", how="inner")
    merged.columns = ["country", "gnp_1900", "life_expectancy_1900"]

    print_success(f"✅ {len(merged)} pays fusionnés avec succès.")
    display_graph(merged)


if __name__ == "__main__":
    main()
