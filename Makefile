# Project automation. Run `make help` to list the targets.
# Requires Python 3.12 (see PYTHON_VERSION) on macOS or Linux.

PYTHON_VERSION := 3.12
PYTHON ?= python$(PYTHON_VERSION)
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
REQUIREMENTS_STAMP := $(VENV)/.requirements-installed
DATASET := data/raw/default_of_credit_card_clients.xls

.DEFAULT_GOAL := help
.PHONY: help all setup data

help:
	@echo "Targets:"
	@echo "  make setup  - create the virtual environment if missing and install the requirements if needed"
	@echo "  make data   - download and extract the dataset if missing"
	@echo "  make all    - setup and data"

all: setup data

setup: $(REQUIREMENTS_STAMP)

data: $(DATASET)

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

$(REQUIREMENTS_STAMP): requirements.txt | $(VENV_PYTHON)
	@$(VENV_PYTHON) -c "import sys; sys.exit(0 if sys.version_info[:2] == tuple(map(int, '$(PYTHON_VERSION)'.split('.'))) else 1)" || (echo "Error: $(VENV) does not use Python $(PYTHON_VERSION). Run 'rm -rf $(VENV)' and then 'make setup'." && exit 1)
	$(VENV_PYTHON) -m pip install -r requirements.txt
	touch $(REQUIREMENTS_STAMP)

$(DATASET): | $(VENV_PYTHON)
	$(VENV_PYTHON) src/download_data.py
