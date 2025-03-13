# Python for Data Science - Module 0

## Description

Ce projet est une introduction aux fondamentaux de Python 3, avec des exercices progressifs allant de la manipulation de structures de données simples, à la création de packages Python réutilisables. Ce module fait partie de la formation **Piscine Python for Data Science**.

Version Python utilisée : **3.10**

---

## Table des matières

1. [Règles générales](#règles-générales)
2. [Exécution des exercices](#exécution-des-exercices)
3. [Précautions avec le terminal Bash](#précautions-avec-le-terminal-bash)
4. [Liste des exercices](#liste-des-exercices)
5. [Installation et utilisation du package `ft_package`](#installation-et-utilisation-du-package-ft_package)

---

## Règles générales

- Aucune variable globale.
- Utilisation obligatoire de Python **3.10**.
- Imports explicites : `import numpy as np` ✅, `from pandas import *` ❌.
- Chaque script doit contenir :
  ```python
  if __name__ == "__main__":
      main()
  ```
- Respect de la norme flake8 :
  ```bash
  pip install flake8
  flake8 fichier.py
  ```

---

## Exécution des exercices

Chaque script se lance depuis le terminal avec :
```bash
python3 fichier.py [arguments]
```

### **⚠️ Attention aux caractères spéciaux**

Sous **Bash**, certains caractères comme `!` ou `$` sont interprétés par le shell :
- Utilisez **des quotes simples** `'...'` pour éviter des erreurs :
  ```bash
  python3 sos.py 'H$llo'
  ```
- Ou échappez les caractères :
  ```bash
  python3 sos.py "H\!llo"
  ```

---

## Liste des exercices

### Exercice 00 : `Hello.py`
- Manipulation de structures (`list`, `tuple`, `set`, `dict`).
- Objectif : afficher des valeurs précises.

### Exercice 01 : `format_ft_time.py`
- Récupérer et afficher le temps depuis Epoch.

### Exercice 02 : `find_ft_type.py`
- Fonction qui affiche le type d'objet passé en paramètre.

### Exercice 03 : `NULL_not_found.py`
- Identifier les différentes formes de "null" en Python (None, nan, etc.).

### Exercice 04 : `whatis.py`
- Vérifier si un nombre est pair ou impair avec gestion d'erreurs sur les arguments.

### Exercice 05 : `building.py`
- Analyse de texte : compter majuscules, minuscules, espaces, ponctuations et chiffres.

### Exercice 06 : `ft_filter.py` et `filterstring.py`
- Recode de la fonction `filter()`.
- Sélection de mots dans une string selon leur longueur.

### Exercice 07 : `sos.py`
- Encodeur Morse via un dictionnaire.
- Gestion des caractères spéciaux et précaution avec Bash : utiliser `'...'` si besoin.

### Exercice 08 : `Loading.py`
- Simulation de la librairie `tqdm`.
- Affiche une barre de progression avec ETA et vitesse.

### Exercice 09 : `ft_package`
- Création d’un package Python contenant la fonction `count_in_list()`.

---

## Installation et utilisation du package `ft_package`

### 1. Structure du projet
```
ft_package/
  __init__.py
  count.py
LICENSE
README.md
pyproject.toml
```

### 2. Générer le package
```bash
python3 -m build
```
Les fichiers créés dans `dist/` :
```
ft_package-0.0.1.tar.gz
ft_package-0.0.1-py3-none-any.whl
```

### 3. Installer le package
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

### 4. Vérifier l'installation
```bash
pip show -v ft_package
```

### 5. Tester le package avec `tester.py`
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # ➜ 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # ➜ 0
```

---

## Conseils et astuces

### Bash
- Éviter les `"..."` si vous passez des caractères spéciaux.
- Préférez `'...'` ou échappez avec `\`.
- Commande utile pour désactiver temporairement l’interprétation des `!` :
  ```bash
  set +H
  ```

### Norme de code
- Respecter flake8 :
  ```bash
  flake8 fichier.py
  ```
- Ajouter des docstrings aux fonctions :
  ```python
  def ma_fonction():
      """Description"""
      pass
  ```

---
