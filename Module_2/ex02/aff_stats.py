import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import os
from printer import print_success, print_failure, print_info


def preprocess_population(pop_str):
    """
    Préprocessus une chaîne de population
    pour la convertir en valeur numérique.
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
    """
    print_info(
        f"Vérification de la présence de '{country1}' et '{country2}' "
        f"dans le dataset..."
    )

    if country1 not in data['country'].values:
        print_failure(f"Le pays '{country1}' n'est pas dans le dataset.")
        return
    if country2 not in data['country'].values:
        print_failure(f"Le pays '{country2}' n'est pas dans le dataset.")
        return

    # Extraction des données
    country1_data = data[data['country'] == country1].iloc[:, 1:]
    country2_data = data[data['country'] == country2].iloc[:, 1:]

    # Conversion
    country1_pop = [
        preprocess_population(pop) for pop in country1_data.values.flatten()
    ]
    country2_pop = [
        preprocess_population(pop) for pop in country2_data.values.flatten()
    ]
    years = country1_data.columns.astype(int)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, country1_pop, label=country1)
    plt.plot(years, country2_pop, label=country2)

    # Axes config
    plt.title(f"Comparaison de la population entre {country1} et {country2}")
    plt.xlabel("Année")
    plt.ylabel("Population (en millions)")

    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    max_pop = max(max(country1_pop), max(country2_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, [f"{pop / 1e6:.0f}M" for pop in y_ticks])

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"population_{country1}_{country2}.png"
    plt.savefig(filename)
    print_success(f"Graphique sauvegardé : {filename}")

    if os.path.exists(filename):
        print_success(f"Ouverture de {filename} dans le navigateur")
        webbrowser.open(filename)
    else:
        print_failure(f"Le fichier '{filename}' n'a pas pu être créé.")
