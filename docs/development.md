## Linting

This project uses `pre-commit` hooks to enforce code style and quality locally.
When you commit, the hooks automatically run linters like Black and Flake8.

**Note:** GitHub Actions also runs the same linters in CI.
It is normal for linting to run again on GitHub even if it passed locally.
This ensures all code in the repo meets the required standards.
