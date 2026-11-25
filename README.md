# credit-card-default-prediction

Predicting credit card default of clients in Taiwan using the UCI "Default of Credit Card Clients" dataset.

## Dataset

The project uses the [Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) dataset from the UCI Machine Learning Repository (30,000 clients, 23 features and a binary target).

The raw data is not tracked in this repository. It is downloaded automatically (see Setup below).

See [docs/dataset.md](docs/dataset.md) for the variable descriptions, value codes and findings about the data.

## Setup

Requirements: Python 3.12 and GNU Make.

From the project root, run:

```bash
make all
```

This single command:

1. creates the virtual environment `.venv` (if it does not exist),
2. installs the pinned packages from `requirements.txt` (if they are not installed or `requirements.txt` changed),
3. downloads the dataset into `data/raw/` and verifies its SHA-256 checksum (if it is not already there).

It is safe to run repeatedly: steps that are already done are skipped.

Other targets:

| Command      | Description                                  |
| ------------ | -------------------------------------------- |
| `make help`  | List the available targets                   |
| `make setup` | Create the virtual environment and install packages only |
| `make data`  | Download the dataset only                    |

If Python 3.12 is installed under another name, pass it explicitly, for example `make all PYTHON=/path/to/python3.12`.

## Usage

Activate the environment and open the notebooks:

```bash
source .venv/bin/activate
jupyter notebook
```

In VS Code, select `.venv/bin/python` as the notebook kernel.

## License

The code in this repository is released under the [MIT License](LICENSE).

The dataset is provided by the UCI Machine Learning Repository under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license and is not included in this repository.

## Status

Work in progress.
