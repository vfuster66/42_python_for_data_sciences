.PHONY: all ex00 ex01 ex02 ex03 test build clean

# Nom de l'image docker
IMAGE_NAME=module4-python
DOCKER_RUN=docker run -t --rm -v $(PWD):/Module_4 -w /Module_4 -e PYTHONPATH=/Module_4 $(IMAGE_NAME)

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Exécuter les scripts principaux
ex00:
	@$(DOCKER_RUN) python3 ex00/tester.py

ex01:
	@$(DOCKER_RUN) python3 ex01/tester.py

ex02:
	@$(DOCKER_RUN) python3 ex02/tester.py

ex03:
	@$(DOCKER_RUN) python3 ex03/tester.py

# Tests pytest
test: test_00 test_01 test_02 test_03

test_00:
	@$(DOCKER_RUN) pytest -s tests/test_00.py --maxfail=1 --disable-warnings -q

test_01:
	@$(DOCKER_RUN) pytest -s tests/test_01.py --maxfail=1 --disable-warnings -q

test_02:
	@$(DOCKER_RUN) pytest -s tests/test_02.py --maxfail=1 --disable-warnings -q

test_03:
	@$(DOCKER_RUN) pytest -s tests/test_03.py --maxfail=1 --disable-warnings -q

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -exec rm -r {} +
