import subprocess
import os

# Pour colorer les messages OK en vert, FAILED en rouge, et les titres en jaune
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'


def run_test(test_script_path, description):
    """
    Fonction qui exécute un script de test Python et affiche si le test est OK ou FAILED.
    
    :param test_script_path: Chemin du script de test à exécuter.
    :param description: Description courte de ce que fait l'exercice.
    """
    original_dir = os.getcwd()  # Sauvegarde du répertoire de travail actuel
    test_dir = os.path.dirname(test_script_path)  # Répertoire du script de test
    os.chdir(test_dir)  # Changer temporairement le répertoire de travail

    try:
        # Exécution du script de test et récupération de la sortie
        result = subprocess.run(['python3', os.path.basename(test_script_path)], capture_output=True, text=True)

        # Extraire le numéro de l'exercice à partir du nom du dossier (ex: ex00)
        exercise_number = os.path.basename(test_dir)

        # Afficher les détails du test
        print(f"\n{bcolors.YELLOW}Exercice {exercise_number[-2:]}: \n{bcolors.ENDC}{description}{bcolors.ENDC}")
        print(f"{os.path.basename(test_script_path)}")

        # Affichage des résultats
        if result.returncode == 0:
            print(f"\n{bcolors.OKGREEN}OK{bcolors.ENDC}\n")
        else:
            print(f"\n{bcolors.FAIL}FAILED{bcolors.ENDC}\n")
            print(f"Erreur:\n{result.stderr}")
            print(f"Sortie standard:\n{result.stdout}")

    finally:
        os.chdir(original_dir)  # Retour au répertoire de travail d'origine


def main():
    # Liste des scripts de tests à exécuter avec une description
    test_scripts = [
        (os.path.join('ex00', 'test_Hello.py'), "Modifier des objets de données pour afficher les salutations."),
        (os.path.join('ex01', 'test_format_ft_time.py'), "Afficher le temps écoulé depuis Epoch et la date actuelle formatée."),
        (os.path.join('ex02', 'test_find_ft_type.py'), "Vérifier le type d'un objet et retourner 42."),
        (os.path.join('ex03', 'test_NULL_not_found.py'), "Vérifier et afficher les types null comme None et NaN."),
        (os.path.join('ex04', 'test_whatis.py'), "Vérifier si un nombre est pair ou impair."),
        (os.path.join('ex05', 'test_building.py'), "Compter les types de caractères dans une chaîne (majuscules, minuscules, etc.)."),
        (os.path.join('ex06', 'test_filterstring.py'), "Filtrer une chaîne de caractères selon un nombre donné."),
        (os.path.join('ex07', 'test_sos.py'), "Convertir un texte en code Morse."),
        (os.path.join('ex08', 'test_Loading.py'), "Créer une barre de progression personnalisée."),
        (os.path.join('ex09', 'test_ft_package.py'), "Vérifier l'installation d'un package Python.")
    ]
    
    # Exécuter chaque script de test
    for test_script, description in test_scripts:
        if os.path.exists(test_script):
            run_test(test_script, description)
        else:
            print(f"{bcolors.FAIL}Test script {test_script} non trouvé !{bcolors.ENDC}")


if __name__ == "__main__":
    main()
