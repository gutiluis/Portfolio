# Pre-commit Hooks

This document explains how to run and manage pre-commit hooks for this project. And describes the hooks configured in `.pre-commit-config.yaml`.

---

## 1. Install hooks

Before committing using your python venv, install the hooks locally:

```bash
pre-commit install
```

### manually run al hooks on all files:
```bash
- pre-commit run --all-files
- pre-commit run --all-files --show-diff-on-failure # what would be changed
```
### preauthorize black changes # black will not refactor. # see: git diff
```bash
black --check .
black --diff . # preview changes across whole repo
pre-commit run --all-files --show-diff-on-failure
```
### update hooks
```bash
pre-commit autoupdate
```
### clean pre-commit caches # for errors
```bash
pre-commit clean
```
### check vulnerabilities using venv with a separate python security tool:
```bash
python3 -m safety check -r requirements.txt
```

---

## External hooks fetched from other repos automatically and managed by pre-commit

| Hook ID                   | Purpose |
|----------------------------|---------|
| trailing-whitespace        | Removes trailing spaces at the end of lines |
| end-of-file-fixer          | Ensures files end with a newline |
| check-yaml                 | Validates YAML syntax |
| check-added-large-files    | Prevents committing very large files |

## Repository local hooks / custom hooks under .pre-commit-config.yaml

| Hook ID        | Purpose |
|----------------|---------|
| safety | Checks dependencies for known security vulnerabilities |

---


# Pre-commit Hooks & CI Notes

- `name:` in `.yml` files is just a **label** for a workflow or step.
- `run:` executes commands in a **shell** (Bash on Ubuntu runners, PowerShell on Windows).
- Jobs are independent tasks inside a workflow; the job name can be anything.
- `pre-commit run --all-files` checks all files against hooks in `.pre-commit-config.yaml`.
- The workflow reads `.yml` and runs each `run:` command in a shell automatically.



## footnotes:
### configure hooks per language
### not every tool provides a pre-commit hook repo. ### see pre-commit mirrors
### pre-commit mirror: A mirror repository exists so a tool can be used with pre-commit, even if the original tool does not provide a pre-commit hook. ### a git repo containing pre-commit plugins must contain a .pre-commit-hooks.yaml
### References:
[Pre-Commit framework](https://pre-commit.com/#hook-configuration)
[Hook IDs for the pre-commit-hooks repo](https://github.com/pre-commit/pre-commit-hooks/blob/main/.pre-commit-hooks.yaml)
[Dependency Vulnerability](https://github.com/pyupio/safety?utm_source=chatgpt.com)
