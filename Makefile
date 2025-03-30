PYTHON := python3
VENV := venv
VENV_BIN := $(VENV)/bin
SRC_DIR := src
TEST_DIR := tests

.PHONY: help
help: 
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV_BIN)/pip install -U pip
	$(VENV_BIN)/pip install .
	$(VENV_BIN)/pip install .[dev]
	$(VENV_BIN)/$(PYTHON) -m pip install -e .

.PHONY:lint
lint:
	$(VENV_BIN)/pylint $(SRC_DIR)
	$(VENV_BIN)/pylint $(TEST_DIR)

.PHONY:typecheck
typecheck:
	$(VENV_BIN)/mypy --strict $(SRC_DIR)
	$(VENV_BIN)/mypy --strict $(TEST_DIR)

.PHONY:format
format:
	$(VENV_BIN)/isort $(SRC_DIR)
	$(VENV_BIN)/black $(SRC_DIR)
	$(VENV_BIN)/isort $(TEST_DIR)
	$(VENV_BIN)/black $(TEST_DIR)

.PHONY:format-check
format-check:
	$(VENV_BIN)/black --check $(SRC_DIR)
	$(VENV_BIN)/isort --check-only $(SRC_DIR)
	$(VENV_BIN)/black --check $(TEST_DIR)
	$(VENV_BIN)/isort --check-only $(TEST_DIR)

.PHONY:test
test:  
	$(VENV_BIN)/$(PYTHON) -m unittest discover -p '*tests.py' -v

.PHONY:all
all: lint typecheck format-check test

.PHONY:clean
clean:  
	rm -rf $(VENV) __pycache__ .pytest_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Default target
.DEFAULT_GOAL := help