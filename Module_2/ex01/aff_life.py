import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import os
import webbrowser


def display_life_expectancy(country: str, data: pd.DataFrame):
    """
    Affiche un graphique de l'espérance de vie d'un pays donné
    à travers les années.
    Affiche uniquement les années tous les 40 ans sur l'axe des abscisses.
    """
    if country not in data['country'].values:
        print(f"Erreur : Le pays '{country}' n'est pas dans le dataset.")
        return

    # Extraire les données pour le pays donné
    country_data = data[data['country'] == country].T
    country_data = country_data.iloc[1:]  # Retirer le nom du pays
    country_data.columns = ['Life Expectancy']

    # Convertir les index en entier pour les années
    years = country_data.index.astype(int)

    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(years, country_data['Life Expectancy'], marker='o', color='b')
    plt.title(f"Espérance de vie au fil des ans pour {country}")
    plt.xlabel("Année")
    plt.ylabel("Espérance de vie")
    plt.grid(True)

    # Afficher les années tous les 40 ans
    plt.xticks(years[::40], rotation=45)

    plt.tight_layout()

    # Sauvegarder le graphique
    filename = f"life_expectancy_{country}.png"
    plt.savefig(filename)

    # Ouvrir le fichier avec le visualiseur d'image par défaut
    if os.path.exists(filename):
        webbrowser.open(filename)
    else:
        print(f"Erreur : Le fichier '{filename}' n'a pas pu être créé.")


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        print("Erreur lors du chargement des données.")
        return

    country = input("Veuillez entrer le nom du pays : ")
    display_life_expectancy(country, data)


if __name__ == "__main__":
    main()
