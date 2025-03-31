import pandas as pd
import matplotlib.pyplot as plt
import os


def preprocess_population(pop_str):
    """Convertit une population (ex: '1.2M') en valeur numérique."""
    if isinstance(pop_str, str):
        if pop_str.endswith("M"):
            return float(pop_str[:-1]) * 1e6
        elif pop_str.endswith("k"):
            return float(pop_str[:-1]) * 1e3
        else:
            return float(pop_str)
    return pop_str


def plot_population(country1: str, country2: str, data: pd.DataFrame):
    """Affiche un graphique comparant la population de deux pays dans le temps."""
    if country1 not in data['country'].values:
        print(f"❌ Le pays '{country1}' n'est pas présent dans le dataset.")
        return
    if country2 not in data['country'].values:
        print(f"❌ Le pays '{country2}' n'est pas présent dans le dataset.")
        return

    # Données brutes
    country1_data = data[data['country'] == country1].iloc[:, 1:]
    country2_data = data[data['country'] == country2].iloc[:, 1:]

    # Conversion en float
    country1_pop = [preprocess_population(p) for p in country1_data.values.flatten()]
    country2_pop = [preprocess_population(p) for p in country2_data.values.flatten()]
    years = country1_data.columns.astype(int)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, country1_pop, label=country1, marker='o')
    plt.plot(years, country2_pop, label=country2, marker='x')

    plt.title(f"Comparaison de la population : {country1} vs {country2}")
    plt.xlabel("Année")
    plt.ylabel("Population (en millions)")
    plt.legend()
    plt.grid(True)

    plt.xticks(range(1800, 2051, 40), rotation=45)
    plt.xlim(1800, 2050)

    # Ajustement des ticks Y
    max_pop = max(max(country1_pop), max(country2_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, [f"{val/1e6:.0f}M" for val in y_ticks])

    plt.tight_layout()

    # Sauvegarde dans le dossier ex02/
    filename = os.path.join("ex02", f"population_{country1}_{country2}.png")
    plt.savefig(filename)
    print(f"✅ Graphique sauvegardé dans : {filename}")
    plt.close()
