import pandas as pd


def load(path: str):
    """
    Charge un fichier CSV, affiche ses dimensions, et retourne le dataset.
    Gère les erreurs en cas de fichier inexistant ou format incorrect.

    Args:
        path (str): Chemin vers le fichier CSV.

    Returns:
        pd.DataFrame | None: Dataset sous forme de DataFrame
        ou None en cas d'erreur.
    """
    try:
        # Charger le fichier CSV avec pandas
        df = pd.read_csv(path)

        # Afficher les dimensions du dataset
        print(f"Le dataset contient {df.shape[0]} lignes "
              f"et {df.shape[1]} colonnes.")

        return df
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' est introuvable.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Erreur : Le fichier '{path}' est vide ou mal formaté.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None


# Exemple d'utilisation
if __name__ == "__main__":
    dataset = load("path/to/your/dataset.csv")
