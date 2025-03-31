import matplotlib.pyplot as plt
import pandas as pd
import os


def display_life_expectancy(country: str, data: pd.DataFrame):
    """
    Affiche un graphique de l'espérance de vie d'un pays donné
    à travers les années, et sauvegarde l'image dans ex01/.
    """
    if country not in data['country'].values:
        print(f"❌ Le pays '{country}' n'est pas présent dans le dataset.")
        return

    country_data = data[data['country'] == country].T
    country_data = country_data.iloc[1:]  # on enlève le nom du pays
    country_data.columns = ['Life Expectancy']
    years = country_data.index.astype(int)

    plt.figure(figsize=(10, 6))
    plt.plot(years, country_data['Life Expectancy'], marker='o', color='b')
    plt.title(f"Espérance de vie pour {country}")
    plt.xlabel("Année")
    plt.ylabel("Espérance de vie")
    plt.grid(True)
    plt.xticks(years[::40], rotation=45)
    plt.tight_layout()

    # 📌 Chemin vers le dossier ex01
    output_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(output_dir, f"life_expectancy_{country}.png")

    plt.savefig(filename)
    plt.close()
    print(f"✅ Graphique sauvegardé sous : {filename}")
