
# 📚 Python for Data Science - Module 3 : Oriented Object Programming

## Description

Ce module est une introduction à la **programmation orientée objet (OOP)** avec Python 3.  
Il propose la création de classes, l'héritage simple et multiple, la surcharge des opérateurs, ainsi que l'utilisation de décorateurs pour améliorer la lisibilité et la traçabilité du code.

Version Python : **3.10**

---

## 📝 Règles générales

- **Python 3.10** obligatoire.
- Aucune variable globale autorisée.
- Chaque script doit contenir :

```python
if __name__ == "__main__":
    main()
```

- Respect des normes **flake8**.
- Gestion des exceptions obligatoire.

---

## 📂 Contenu du Module

### ✅ EX00 - GOT S1E9
- 📄 **Fichier** : `S1E9.py`
- ➡️ **Classes** :
  - `Character` (classe abstraite avec `die()`)
  - `Stark` (hérite de `Character`)
- ✔️ Méthode `die()` ➔ rend `is_alive` à `False`.
- ✔️ Tests de la classe `Stark` avec `tester.py` et `ex00_test.py`.

---

### ✅ EX01 - GOT S1E7
- 📄 **Fichier** : `S1E7.py`
- ➡️ **Classes** :
  - `Baratheon` (hérite de `Character`)
  - `Lannister` (hérite de `Character`)
- ✔️ `__str__` / `__repr__` surchargés.
- ✔️ Méthode de classe `create_lannister()`.
- ✔️ Tests dans `tester.py` et `ex01_test.py`.

---

### ✅ EX02 - Now it’s weird!
- 📄 **Fichier** : `DiamondTrap.py`
- ➡️ **Classe** :
  - `King` (hérite de `Baratheon` et `Lannister`)
- ✔️ Propriétés `eyes` et `hairs`.
- ✔️ Résolution du diamond problem avec `super()`.
- ✔️ Tests dans `tester.py` et `ex02_test.py`.

---

### ✅ EX03 - Calculate my vector
- 📄 **Fichier** : `ft_calculator.py`
- ➡️ **Classe** :
  - `Calculator`
- ✔️ Surcharge des opérateurs `+`, `-`, `*`, `/`.
- ✔️ Supporte les opérations avec des scalaires et des `Calculator`.
- ✔️ Tests dans `tester.py` et `ex03_test.py`.

---

### ✅ EX04 - Calculate my dot product
- 📄 **Fichier** : `ft_calculator.py` (complété avec EX04)
- ➡️ **Fonctions** :
  - `dot_product()`
  - `add_vec()`
  - `sous_vec()`
- ✔️ Chaque fonction utilise un **décorateur** pour la traçabilité (`debug`).
- ✔️ Tests unitaires dans `ex04_test.py`.

---

## ⚙️ Installation et Exécution

### 🔹 Installation des dépendances
Aucune dépendance externe requise.

### 🔹 Exécution des scripts

```bash
python3 tester.py
python3 ex00_test.py
python3 ex01_test.py
python3 ex02_test.py
python3 ex03_test.py
python3 ex04_test.py
```

### 🔹 Remarques

- Les classes et méthodes respectent les principes de l'OOP.
- L'approche des décorateurs améliore la traçabilité des appels de fonctions.

---
