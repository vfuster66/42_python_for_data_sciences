# Nom du projet
PROJECT_NAME=module_1
IMAGE_NAME=$(PROJECT_NAME):latest

# Commande pour build l'image Docker
build:
	docker build -t $(IMAGE_NAME) .

# Commande pour lancer un shell dans le conteneur Docker
run:
	docker run -it --rm -v $(PWD):/app $(IMAGE_NAME) bash

# Lancer flake8 sur les exos
lint:
	docker run --rm -v $(PWD):/app $(IMAGE_NAME) flake8 .

# Clean Docker
clean:
	docker rmi $(IMAGE_NAME)
