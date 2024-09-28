import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
import webbrowser
import os


def preprocess_population(pop_str):
    """
    Préprocessus une chaîne de population
    pour la convertir en valeur numérique.

    Args:
        pop_str (str): Chaîne de population avec ou sans le suffixe 'M' ou 'k'.

    Returns:
        float: Valeur numérique de la population.
    """
    if isinstance(pop_str, str):
        if pop_str.endswith("M"):
            return float(pop_str[:-1]) * 1e6
        elif pop_str.endswith("k"):
            return float(pop_str[:-1]) * 1e3
        else:
            return float(pop_str)
    return pop_str


def plot_population(country1: str, country2: str, data: pd.DataFrame):
    """
    Affiche un graphique comparant la population des deux pays au fil du temps.
    L'axe des ordonnées représente la population en millions avec des lignes
    de référence (ex. 20M, 40M), et l'axe des abscisses affiche les années
    entre 1800 et 2040, avec des marques tous les 40 ans.
    """
    if country1 not in data['country'].values:
        print(f"Erreur : Le pays '{country1}' n'est pas dans le dataset.")
        return
    if country2 not in data['country'].values:
        print(f"Erreur : Le pays '{country2}' n'est pas dans le dataset.")
        return

    # Récupération des données pour chaque pays
    country1_data = data[data['country'] == country1].iloc[:, 1:]
    country2_data = data[data['country'] == country2].iloc[:, 1:]

    # Conversion des données de population
    country1_pop = [
        preprocess_population(pop) for pop in country1_data.values.flatten()]
    country2_pop = [
        preprocess_population(pop) for pop in country2_data.values.flatten()]
    years = country1_data.columns.astype(int)

    # Tracer les données pour les deux pays
    plt.plot(years, country1_pop, label=country1)
    plt.plot(years, country2_pop, label=country2)

    # Configuration des axes
    plt.title(f"Comparaison de la population entre {country1} et {country2}")
    plt.xlabel("Année")
    plt.ylabel("Population (en millions)")

    # Limites et ticks sur l'axe des abscisses
    # (de 1800 à 2040 avec un intervalle de 40 ans)
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    # Limites et ticks sur l'axe des ordonnées
    # (afficher la population en millions)
    max_pop = max(max(country1_pop), max(country2_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarder le graphique dans un fichier
    filename = f"population_{country1}_{country2}.png"
    plt.savefig(filename)

    # Ouvrir l'image dans le visualiseur d'image par défaut du système
    if os.path.exists(filename):
        webbrowser.open(filename)
    else:
        print(f"Erreur : Le fichier '{filename}' n'a pas pu être créé.")


def main():
    # Charger les données
    data = load("population_total.csv")
    if data is None:
        print("Erreur lors du chargement des données.")
        return

    # Demander à l'utilisateur de saisir les noms de deux pays
    country1 = input("Veuillez entrer le nom du premier pays : ")
    country2 = input("Veuillez entrer le nom du deuxième pays : ")

    # Afficher le graphique comparant la population des deux pays
    plot_population(country1, country2, data)


if __name__ == "__main__":
    main()
