FROM python:3.10-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Installer les dépendances de base
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier de travail
WORKDIR /app

# Copier les requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier les sources dans le container
COPY . .

CMD ["bash"]
