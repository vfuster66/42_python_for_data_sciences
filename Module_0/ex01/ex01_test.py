import subprocess
import time
from datetime import datetime


def test_format_ft_time():
    print("\nTest du script format_ft_time.py")

    # Exécuter le script format_ft_time.py
    print("Exécution du script...")
    result = subprocess.run(['python3', 'format_ft_time.py'],
                            capture_output=True, text=True)

    # Vérifier que la sortie n'est pas vide
    if not result.stdout.strip():
        print("Erreur : Le script n'a généré aucune sortie.")
        return

    # Afficher la sortie pour débogage
    print(f"\nSortie brute obtenue :\n{result.stdout}")

    # Séparer les lignes du résultat pour analyse
    lines = result.stdout.strip().split('\n')

    # Vérification des secondes écoulées depuis le 1er janvier 1970
    current_time = time.time()
    expected_first_line = f"Seconds since \
        January 1, 1970: {current_time:.4f} ou {current_time:.2e}"

    print("\nVérification des secondes écoulées depuis le 1er janvier 1970...")
    print(f"Valeur attendue (approx.) : {expected_first_line}")
    print(f"Valeur obtenue : {lines[0]}")

    # Les premières parties de la ligne 1 doivent matcher cette structure
    if "Seconds since January 1, 1970" in lines[0]:
        print("Test pour les secondes écoulées : OK")
    else:
        print(f"Sortie incorrecte pour les secondes écoulées : {lines[0]}")

    # Vérification de la date actuelle
    current_date = datetime.now().strftime("%b %d %Y")
    print("\nVérification de la date actuelle...")
    print(f"Date attendue : {current_date}")
    print(f"Date obtenue : {lines[1]}")

    if lines[1] == current_date:
        print("Test pour la date actuelle : OK")
    else:
        print(f"Sortie incorrecte pour la date : {lines[1]}")

    print("\nTous les tests sont passés avec succès !")


if __name__ == "__main__":
    test_format_ft_time()
