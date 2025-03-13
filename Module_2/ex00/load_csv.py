import pandas as pd
from printer import print_info, print_failure


def load(path: str):
    """
    Charge un fichier CSV, affiche ses dimensions, et retourne le dataset.

    Args:
        path (str): Chemin vers le fichier CSV.

    Returns:
        pd.DataFrame | None
    """
    try:
        df = pd.read_csv(path)
        print_info(f"Le dataset contient {df.shape[0]} lignes "
                   f"et {df.shape[1]} colonnes.")
        return df
    except FileNotFoundError:
        print_failure(f"Erreur : Le fichier '{path}' est introuvable.")
        return None
    except pd.errors.EmptyDataError:
        print_failure(f"Erreur : Le fichier '{path}' est vide ou mal formaté.")
        return None
    except Exception as e:
        print_failure(f"Une erreur est survenue : {e}")
        return None
