# Testing Instructions ### authentication, not library notes

This document explains how to run tests for the Flask project.

## Requirements
- Python 3.11+
- `pytest` (installed via `requirements.txt`)
- `pytest-cov` (optional, for coverage)
- `.env` file with test database credentials (if tests involve DB)

### Install dependencies:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

### Run verbose test:
- pytest -v # from main project working dir/

### Run all tests:
- pytest

### Run a single test file:
- pytest tests/test_app.py

### Run a single test function
pytest tests/test_app.py::test_function_name

---

### Fixtures:
conftest.py defines reusable fixtures such as: flask app, db session for tests, HTTP client for testing routes.
Define fixtures for static data used by tests. This data can be accessed by all tests in the suite unless specified otherwise. This could be data as well as helpers of modules which will be passed to all tests.

### External plugin loading:
conftest.py is used to import external plugins or modules. By defining the following global variable, pytest will load the module and make it available for its test. Plugins are generally files defined in your project or other modules which might be needed in your tests. You can also load a set of predefined plugins

### Hooks:
You can specify hooks such as setup and teardown methods and much more to improve your tests.


### Test root path:
This is a bit of a hidden feature. By defining conftest.py in your root path, you will have pytest recognizing your application modules without specifying PYTHONPATH. In the background, py.test modifies your sys.path by including all submodules which are found from the root path.


### testing http basicauthentication extension from flask with pytest


### there can be more than one conftest.py file
https://stackoverflow.com/questions/34466027/what-is-conftest-py-for-in-pytest
