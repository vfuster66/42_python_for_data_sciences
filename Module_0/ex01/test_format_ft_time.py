import subprocess
import time
from datetime import datetime

def test_format_ft_time():
    # Exécuter le script format_ft_time.py
    result = subprocess.run(['python3', 'format_ft_time.py'], capture_output=True, text=True)
    
    # Vérifier que la sortie n'est pas vide
    if not result.stdout.strip():
        print("Erreur : Le script n'a généré aucune sortie.")
        return

    # Afficher la sortie pour débogage
    print(f"Sortie brute obtenue :\n{result.stdout}")

    # Séparer les lignes du résultat pour analyse
    lines = result.stdout.strip().split('\n')

    # Vérification des secondes écoulées depuis le 1er janvier 1970
    current_time = time.time()
    first_line = f"Seconds since January 1, 1970: {current_time:.4f} ou {current_time:.2e}"

    # Les premières parties de la ligne 1 doivent matcher cette structure
    assert "Seconds since January 1, 1970" in lines[0], f"Sortie incorrecte pour les secondes écoulées : {lines[0]}"
    
    # Vérification de la date actuelle
    current_date = datetime.now().strftime("%b %d %Y")
    assert lines[1] == current_date, f"Sortie incorrecte pour la date : {lines[1]}"

    print("Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    test_format_ft_time()
