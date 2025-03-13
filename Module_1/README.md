
# Python for Data Science - Module 1

## Description

Ce module est dédié à l'apprentissage des **manipulations de tableaux (arrays)** et **d'images** en Python. Il s'agit du premier contact avec la **manipulation de données en 2D**, l'usage de **Numpy**, et l'application de **filtres d'image basiques**, en respectant des contraintes d'implémentation.

**Version Python :** `3.10`

---

## Table des matières

1. [Règles générales](#règles-générales)
2. [Exécution des exercices](#exécution-des-exercices)
3. [Détails des exercices](#détails-des-exercices)
4. [Exemple d'utilisation](#exemple-dutilisation)

---

## Règles générales

- **Pas de code global** : tout est dans des fonctions, avec une entrée par `main()`.
- **Python 3.10** uniquement.
- Respect de la **norme flake8** :
  ```bash
  pip install flake8
  flake8 fichier.py
  ```
- **Docstring** pour toutes les fonctions.
- Gestion obligatoire des **exceptions** :
  - Vérification des types.
  - Vérification des tailles de listes ou arrays.
  - Messages d'erreur clairs.

---

## Exécution des exercices

Chaque exo est indépendant. Pour **tester une fonctionnalité**, lance le `tester.py` associé :

```bash
cd ex00
python3 tester.py
```

Pour **tester avec unittest** (si disponible) :

```bash
cd ex00
python3 ex00_test.py
```

---

## Détails des exercices

### 🟦 EX00 - Give my BMI

📄 **Fichiers :** `give_bmi.py`, `tester.py`, `ex00_test.py`

➡️ **Fonctions :**
- `give_bmi()` : calcule l'IMC à partir de listes de tailles et poids.
- `apply_limit()` : renvoie True si l'IMC dépasse une limite.

➡️ **Validation :**
- Contrôle de la taille des listes.
- Contrôle du type des données.

---

### 🟦 EX01 - 2D Array

📄 **Fichiers :** `array2D.py`, `tester.py`, `ex01_test.py`

➡️ **Fonction :**
- `slice_me()` : découpe une liste 2D selon des indices `start` et `end`.

➡️ **Validation :**
- Vérifie que tous les sous-éléments sont des listes.
- Affiche la `shape` avant/après découpage.

---

### 🟦 EX02 - Load my image

📄 **Fichiers :** `load_image.py`, `tester.py`, `ex02_test.py`  
🖼️ Images : `landscape.jpg`, `animal.jpeg`

➡️ **Fonction :**
- `ft_load()` : charge une image JPEG/JPG et affiche la forme et les pixels RGB.

➡️ **Validation :**
- Contrôle du chemin et du format.
- Affichage des dimensions et échantillon des pixels.

---

### 🟦 EX03 - Zoom on me

📄 **Fichiers :** `zoom.py`, `tester.py`, `ex03_test.py`  
🖼️ Image : `animal.jpeg`

➡️ **Fonction :**
- `ft_zoom()` : effectue un zoom (slicing) centré et sauvegarde l'image zoomée avec axes.

➡️ **Validation :**
- Sauvegarde de l'image `zoomed_image_with_axes.png` pour Docker.
- Affiche la forme de l'image avant/après.

---

### 🟦 EX04 - Rotate me

📄 **Fichiers :** `rotate.py`, `tester.py`, `ex04_test.py`  
🖼️ Image : `animal.jpeg`

➡️ **Fonction :**
- `ft_rotate()` : transpose une zone carrée de l'image et sauvegarde l'image transposée avec axes.

➡️ **Validation :**
- Sauvegarde de l'image `transposed_image_with_axes.png`.
- Vérifie et affiche les formes avant/après.

---

### 🟦 EX05 - Pimp my image

📄 **Fichiers :** `pimp_image.py`, `tester.py`, `ex05_test.py`  
🖼️ Image : `landscape.jpg`

➡️ **Fonctions :**
- `ft_invert()`
- `ft_red()`
- `ft_green()`
- `ft_blue()`
- `ft_grey()`

➡️ **Validation :**
- Pas de fonctions Numpy toutes faites pour les modifications des pixels.
- Sauvegarde d'images transformées avec leurs axes (utile en Docker).
- Tests sur la transformation des canaux RGB.

---

## Exemple d'utilisation

```bash
cd ex05
python3 tester.py
```

Résultat :  
- Les images filtrées sont sauvegardées dans le dossier courant :
  - `inverted_image_with_axes.png`
  - `red_image_with_axes.png`
  - `green_image_with_axes.png`
  - `blue_image_with_axes.png`
  - `grey_image_with_axes.png`

---

## Conseils & astuces

### Docker
- Sauvegarde des images dans des `.png` pour vérifier hors-container.
- Pas de `show()` en environnement sans interface graphique !

### Respect des conventions
- `flake8` avant tout push/commit.
- Type hinting, docstrings et exceptions bien gérés.

---
