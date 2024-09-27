import subprocess
import os
import webbrowser


def test_exercice_04():
    print("\n--- Test du script rotate.py avec l'image 'animal.jpeg' ---")

    # Test 1: Vérification que l'image existe et peut être ouverte
    if not os.path.exists("animal.jpeg"):
        print("Erreur : Le fichier 'animal.jpeg' est manquant.")
        return

    # Exécuter le script rotate.py avec une bonne image
    print("\nExécution du script rotate.py...")
    result = subprocess.run(
        ['python3', 'rotate.py', 'animal.jpeg', 'True'],
        capture_output=True, text=True
    )

    # Vérifier que l'image a bien été transposée
    output = result.stdout.strip().split('\n')

    # Affichage complet de la sortie pour inspection
    print("\n--- Sortie complète de rotate.py ---")
    for line in output:
        print(line)

    # Vérification de la sauvegarde de l'image transposée
    if os.path.exists("transposed_image_with_axes.png"):
        print("\nL'image transposée a été sauvegardée avec succès sous "
              "'transposed_image_with_axes.png'.")

        # Ouvrir l'image dans le visualiseur par défaut du système
        webbrowser.open("transposed_image_with_axes.png")
    else:
        print("Erreur : L'image transposée n'a pas été trouvée.")

    # Test 2: Comportement avec une image inexistante (ne pas ouvrir l'image)
    print("\n--- Test avec une image inexistante ---")
    result = subprocess.run(
        ['python3', 'rotate.py', 'fichier_inexistant.jpeg', 'False'],
        capture_output=True, text=True
    )

    # Vérifier si le bon message d'erreur est capturé
    if ("Erreur : L'image 'fichier_inexistant.jpeg' n'a pas été trouvée."
            in result.stdout or "Erreur : Impossible de charger l'image."
            in result.stdout):
        print("Test réussi : L'erreur pour un fichier inexistant a été "
              "correctement capturée.")
    else:
        print(f"Erreur : L'image inexistante n'a pas déclenché le bon "
              f"message d'erreur.\nSortie obtenue : {result.stdout}")

    # Test 3: Comportement avec un mauvais format (par ex. un fichier texte)
    print("\n--- Test avec un fichier au mauvais format (texte) ---")
    with open("fichier_texte.txt", "w") as f:
        f.write("Ceci est un fichier texte, pas une image.")

    result = subprocess.run(
        ['python3', 'rotate.py', 'fichier_texte.txt', 'False'],
        capture_output=True, text=True
    )

    if ("Erreur : Le fichier 'fichier_texte.txt' n'est pas un format d'image "
            "valide." in result.stdout):
        print("Test réussi : L'erreur pour un mauvais format a été "
              "correctement capturée.")
    else:
        print("Erreur : Le fichier au mauvais format n'a pas déclenché le "
              "bon message d'erreur.")

    # Nettoyage
    if os.path.exists("fichier_texte.txt"):
        os.remove("fichier_texte.txt")


if __name__ == "__main__":
    test_exercice_04()
