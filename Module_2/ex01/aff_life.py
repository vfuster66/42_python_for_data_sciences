import matplotlib.pyplot as plt
import pandas as pd
import os
import webbrowser
from printer import print_info, print_failure, print_success


def display_life_expectancy(country: str, data: pd.DataFrame):
    """
    Affiche un graphique de l'espérance de vie d'un pays donné
    à travers les années.
    Affiche uniquement les années tous les 40 ans sur l'axe des abscisses.
    """
    if country not in data['country'].values:
        print_failure(f"Le pays '{country}' n'est pas dans le dataset.")
        return

    # Extraire les données pour le pays donné
    country_data = data[data['country'] == country].T
    country_data = country_data.iloc[1:]  # Retirer le nom du pays
    country_data.columns = ['Life Expectancy']

    years = country_data.index.astype(int)

    plt.figure(figsize=(10, 6))
    plt.plot(years, country_data['Life Expectancy'], marker='o', color='b')
    plt.title(f"Espérance de vie au fil des ans pour {country}")
    plt.xlabel("Année")
    plt.ylabel("Espérance de vie")
    plt.grid(True)

    plt.xticks(years[::40], rotation=45)
    plt.tight_layout()

    filename = f"life_expectancy_{country}.png"
    plt.savefig(filename)

    if os.path.exists(filename):
        print_success(f"Fichier '{filename}' créé avec succès.")
        # Désactiver webbrowser.open() dans Docker/headless
        try:
            webbrowser.open(filename)
        except Exception:
            print_info(f"Ouvre le fichier manuellement : {filename}")
    else:
        print_failure(
            f"Erreur : Le fichier '{filename}' n'a pas pu être créé.")
