
# 📚 Python for Data Science - Module 4 : Data Oriented Design

## Description

Ce module se concentre sur la **manipulation de données** et la **conception orientée données**. Il introduit la notion de fonctions statistiques personnalisées, closures, décorateurs et dataclasses.

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

### ✅ EX00 - Calculate my statistics
- 📄 **Fichier** : `ft_statistics.py`
- ➡️ **Fonction** :
  - `ft_statistics(*args, **kwargs)`
- ✔️ Calculs possibles :
  - mean, median, quartile, variance, standard deviation
- ✔️ Gestion d’erreur :
  - Pas d’arguments ➔ ERROR
  - Fonction non reconnue ➔ ERROR
- ✔️ Tests dans `ex00_test.py`

---

### ✅ EX01 - Outer_inner
- 📄 **Fichier** : `in_out.py`
- ➡️ **Fonctions** :
  - `outer()` ➔ retourne une closure `inner()`
- ✔️ `inner()` utilise les variables de `outer()`.
- ✔️ Tests dans `ex01_test.py`

---

### ✅ EX02 - My first decorating
- 📄 **Fichier** : `call_limit.py`
- ➡️ **Décorateur** :
  - `callLimit(limit: int)`
- ✔️ Limite le nombre d’appels d’une fonction.
- ✔️ Affiche un message `Error: function call limit reached` si limite dépassée.
- ✔️ Tests dans `ex02_test.py`

---

### ✅ EX03 - Data class
- 📄 **Fichier** : `student.py`
- ➡️ **Dataclass** :
  - `Student`
- ✔️ Attributs :
  - `first_name`, `last_name`
  - `id` ➔ auto-incrémenté
  - `login` ➔ généré à partir du `first_name` en lowercase + id
- ✔️ Tests dans `ex03_test.py`

---

## ⚙️ Installation et Exécution

### 🔹 Exécution des scripts

```bash
python3 ft_statistics.py
python3 in_out.py
python3 call_limit.py
python3 tester.py  # Pour ex03
```

### 🔹 Exécution des tests unitaires

```bash
python3 ex00_test.py
python3 ex01_test.py
python3 ex02_test.py
python3 ex03_test.py
```

---
