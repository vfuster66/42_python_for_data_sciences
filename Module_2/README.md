
# 📚 Python for Data Science - Module 2 : DataTable

## Description

Ce module porte sur la manipulation de **données tabulaires** à l’aide de **pandas** et **matplotlib**. Il s’agit d’importer, filtrer, comparer et visualiser des datasets réels (CSV). Ce module fait partie de la **Piscine Python for Data Science**.

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
- Gestion des exceptions obligatoire sur les fichiers et données.

---

## 📂 Contenu du Module

### ✅ Ex00 - Load my Dataset
- 📄 **Fichier** : `load_csv.py`
- ➡️ **Fonction** : `load(path: str) -> pd.DataFrame`
- 🔧 **Description** : Charge un fichier CSV et affiche la dimension.
- ⚠️ **Gestion des erreurs** :
  - Fichier inexistant.
  - Mauvais format.

---

### ✅ Ex01 - Draw my country
- 📄 **Fichier** : `aff_life.py`
- ➡️ **Données** : `life_expectancy_years.csv`
- 🔧 **Description** : Affiche l’évolution de l’espérance de vie de ton pays (campus) sur plusieurs années.
- 📈 **Visualisation** : Graphique `matplotlib` de la life expectancy.

---

### ✅ Ex02 - Compare my country
- 📄 **Fichier** : `aff_stats.py`
- ➡️ **Données** : `population_total.csv`
- 🔧 **Description** : Compare l’évolution de la population de ton pays avec un autre.
- 📈 **Visualisation** : Graphique `matplotlib` des populations comparées sur les années.
- **Lancement** :
```bash
make ex02 country1=France country2=Germany
```

---

### ✅ Ex03 - Draw my year
- 📄 **Fichier** : `aff_multi_stats.py`
- ➡️ **Données** :
  - `income_per_person_gdppercapita_ppp_inflation_adjusted.csv`
  - `life_expectancy_years.csv`
- 🔧 **Description** : Compare le GDP per capita et la life expectancy en 1900 pour tous les pays.
- 📈 **Visualisation** : Scatter plot (`matplotlib`) :
  - Axe X : GDP per capita.
  - Axe Y : Life expectancy.

---

## ⚙️ Installation et Exécution

### 🔹 Installation des dépendances

```bash
pip install pandas matplotlib
```

### 🔹 Exécution des scripts

```bash
python3 load_csv.py path/to/file.csv
python3 aff_life.py
python3 aff_stats.py
python3 aff_multi_stats.py
```

### 🔹 Remarques

- Adapter les chemins des fichiers CSV si nécessaire.
- En environnement Docker :
  - Utiliser `plt.savefig()` pour enregistrer les graphiques.
  - Ouverture des figures avec `Image.open()` si besoin.

---
