.PHONY: all ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09 test build clean

# Nom de l'image docker
IMAGE_NAME=module0-python
DOCKER_RUN=docker run -t --rm -v $(PWD):/Module_0 -w /Module_0 -e PYTHONPATH=/Module_0 $(IMAGE_NAME)

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

bash:
	@docker run -it --rm -v $(PWD):/Module_0 -w /Module_0 -e PYTHONPATH=/Module_0 $(IMAGE_NAME) /bin/bash

# Exécuter les scripts principaux
ex00:
	@echo "Running: python3 ex00/tester.py | cat -e"
	@$(DOCKER_RUN) python3 ex00/tester.py | sed 's/\r//g' | cat -e

ex01:
	@echo "Running: python3 ex01/tester.py | cat -e"
	@$(DOCKER_RUN) python3 ex01/tester.py | sed 's/\r//g' | cat -e

ex02:
	@echo "Running: python3 ex02/tester.py | cat -e"
	@$(DOCKER_RUN) python3 ex02/tester.py | sed 's/\r//g' | cat -e

ex02_empty:
	@echo "Running: python3 ex02/find_ft_type.py | cat -e"
	@$(DOCKER_RUN) python3 ex02/find_ft_type.py | sed 's/\r//g' | cat -e

ex03:
	@echo "Running: python3 ex03/tester.py | cat -e"
	@$(DOCKER_RUN) python3 ex03/tester.py | sed 's/\r//g' | cat -e

ex03_empty:
	@echo "Running: python3 ex03/NULL_not_found.py | cat -e"
	@$(DOCKER_RUN) python3 ex03/NULL_not_found.py | sed 's/\r//g' | cat -e

ex04:
	@$(DOCKER_RUN) python3 ex04/whatis.py $(number);

ex05:
	@if [ -z "$(text)" ]; then \
		echo "❌ ❌ Aucun texte fourni !"; \
		echo "🔎 👉 Exemple : make ex05 text='Hello World!'"; \
	else \
		$(DOCKER_RUN) python3 ex05/tester.py text="$(text)"; \
	fi

ex06:
	@if [ -z "$(s)" ] || [ -z "$(n)" ]; then \
		echo "❌ ❌ Arguments manquants !"; \
		echo "🔎 👉 Exemple : make ex06 s='Hello world' n=3"; \
	else \
		$(DOCKER_RUN) python3 ex06/tester.py "$(s)" $(n); \
	fi

ex07:
	@if [ -z "$(text)" ]; then \
		echo "❌ ❌ Argument manquant !"; \
		echo "🔎 👉 Exemple : make ex07 text='SOS'"; \
	else \
		$(DOCKER_RUN) python3 ex07/tester.py "$(text)"; \
	fi

ex08:
	@$(DOCKER_RUN) python3 ex08/tester.py

ex09_build:
	@$(DOCKER_RUN) sh -c "pip install build && cd ex09 && python3 -m build && pip install ./dist/ft_package-0.0.1.tar.gz"

ex09:
	@$(DOCKER_RUN) python3 ex09/tester.py

# Tests pytest
test: test_00 test_01 test_02 test_03 test_04 test_05 test_06 test_07 test_08 test_09

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

test_06:
	@$(DOCKER_RUN) pytest -s tests/test_06.py --maxfail=1 --disable-warnings -q

test_07:
	@$(DOCKER_RUN) pytest -s tests/test_07.py --maxfail=1 --disable-warnings -q

test_08:
	@$(DOCKER_RUN) pytest -s tests/test_08.py --maxfail=1 --disable-warnings -q

test_09:
	@$(DOCKER_RUN) pytest -s tests/test_09.py --maxfail=1 --disable-warnings -q

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -exec rm -r {} +
