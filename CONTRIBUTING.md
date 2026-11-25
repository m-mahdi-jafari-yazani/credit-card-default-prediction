# Contributing

## Commit Message Format

Each commit message has a type, an optional scope, and a short description:

```
type(scope): short description
```

### Rules

- Use English and the imperative present tense ("add", not "added").
- One logical change per commit.

### Types

| Type | Use for |
|------|---------|
| `feat` | New feature, analysis step, or model |
| `fix` | Bug fix |
| `refactor` | Code restructuring without behavior change |
| `docs` | Documentation |
| `test` | Tests |
| `chore` | Config, dependencies, tooling |

### Examples

```
feat(preprocessing): impute missing income values with median
feat(model): add logistic regression baseline
fix(eval): correct ROC AUC computation
docs: add project structure to README
chore: add data files to .gitignore
```

## Workflow

The `main` branch is protected: changes reach it only through pull requests.

### Branches

- Create one branch per task, starting from an up-to-date `main`.
- Name it `type/short-description`, using the same types as commit messages (for example `feat/data-cleaning`, `docs/readme-update`).

```bash
git switch main
git pull
git switch -c feat/data-cleaning
```

### Pull requests

- Open a pull request into `main` when the work is ready for review.
- Write the pull request title in the commit message format, because it becomes the commit message on `main` (squash merge).
- Keep each pull request focused on one logical change.
- The other author reviews and approves it before it is merged.
- After merging, update your local `main` and delete the branch.

```bash
git switch main
git pull
git branch -d feat/data-cleaning
```

### Notebooks

- Jupyter notebooks are JSON files and are hard to merge.
- Only one person edits a given notebook at a time. Agree on who works on which notebook before starting.
- Run the notebook from top to bottom before committing, so the saved outputs are up to date.

### Before opening a pull request

- `make all` runs without errors on a clean checkout.
- Commit messages and the pull request title follow the format above.
- Everything in the repository is in English.
