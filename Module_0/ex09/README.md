# ft_package

## Description

`ft_package` est un package Python simple qui contient une fonction appelée `count_in_list`, laquelle permet de compter le nombre d'occurrences d'un élément dans une liste donnée.

## Installation et Utilisation

### Pré-requis

- Python 3.10 ou supérieur
- `pip` pour l'installation des packages
- `build` pour générer le package (si non installé, exécutez `pip install build`)

### Étapes pour créer et installer le package

#### 1. Créer le package

Assurez-vous que les fichiers suivants existent dans votre répertoire de projet :

- `ft_package/__init__.py` : ce fichier contient la fonction count_in_list
- `pyproject.toml` : fichier de configuration pour construire le package.
- `LICENSE` : fichier de licence (par exemple, MIT).
- `README.md` : fichier de description (ce fichier).

#### 2. Générer le package

Pour créer le package, exécutez la commande suivante dans votre terminal :
```
python3 -m build
```

Cela va générer deux fichiers dans le dossier dist/ :

- ft_package-0.0.1.tar.gz
- ft_package-0.0.1-py3-none-any.whl


#### 3. Installer le package

Installez le package en utilisant l'une des deux commandes suivantes :
```
pip install ./dist/ft_package-0.0.1.tar.gz
```

ou

```
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

#### 4. Vérifier l'installation

Vous devriez voir les informations concernant le package.
```
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: 
Author: 
Author-email: eagle <eagle@42.fr>
License: MIT
Location: /home/vfuster-/Documents/python_for_data_sciences/venv/lib/python3.10/site-packages
Requires: 
Required-by: 
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Programming Language :: Python :: 3
  License :: OSI Approved :: MIT License
Entry-points:
```

#### 5. Tester le package
Vous pouvez créer un fichier tester.py pour vérifier le bon fonctionnement de votre package :
```
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Doit afficher : 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Doit afficher : 0
```