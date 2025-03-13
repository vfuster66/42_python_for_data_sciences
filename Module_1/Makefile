.PHONY: all ex00 ex01 ex02 ex03 ex04 ex05 test build clean

# Nom de l'image docker
IMAGE_NAME=module1-python
DOCKER_RUN=docker run -t --rm -v $(PWD):/Module_1 -w /Module_1 -e PYTHONPATH=/Module_1 $(IMAGE_NAME)

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Exécuter les scripts principaux
ex00:
	@$(DOCKER_RUN) python3 ex00/tester.py

ex01:
	@$(DOCKER_RUN) python3 ex01/tester.py

ex02:
	@$(DOCKER_RUN) python3 ex02/tester.py image=${image}

ex03:
	@$(DOCKER_RUN) python3 ex03/tester.py image=$(image)

ex04:
	@$(DOCKER_RUN) python3 ex04/tester.py image=$(image)

ex05:
	@$(DOCKER_RUN) python3 ex05/tester.py image=$(image)

# Tests pytest
test: test_00 test_01 test_02 test_03 test_04 test_05

test_00:
	@$(DOCKER_RUN) pytest -s tests/test_00.py --maxfail=1 --disable-warnings -q

test_01:
	@$(DOCKER_RUN) pytest -s tests/test_01.py --maxfail=1 --disable-warnings -q

test_02:
	@$(DOCKER_RUN) pytest -s tests/test_02.py --maxfail=1 --disable-warnings -q

test_03:
	@$(DOCKER_RUN) pytest -s tests/test_03.py --maxfail=1 --disable-warnings -q

test_04:
	@$(DOCKER_RUN) pytest -s tests/test_04.py --maxfail=1 --disable-warnings -q

test_05:
	@$(DOCKER_RUN) pytest -s tests/test_05.py --maxfail=1 --disable-warnings -q

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -exec rm -r {} +
