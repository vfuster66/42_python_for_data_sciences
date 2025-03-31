import pandas as pd
from typing import Optional


def load(path: str) -> Optional[pd.DataFrame]:
    """
    Charge un fichier CSV, affiche ses dimensions, et retourne le dataset.

    Args:
        path (str): Chemin vers le fichier CSV.

    Returns:
        Optional[pd.DataFrame]: Le DataFrame chargé ou None en cas d'erreur.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{path}' est introuvable.")
    except pd.errors.EmptyDataError:
        print(f"❌ Erreur : Le fichier '{path}' est vide ou mal formaté.")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")
    return None
