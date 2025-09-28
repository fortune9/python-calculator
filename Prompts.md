# Prompts

The prompts used to generate code using DeepSeek.

## Generate the first version of the code

### Prompt
You are a software engineer. Now I need you to create a python package (called python-calculator) which has the following functions: (1) allow users to do arithmetic calculation, (2) offers a UI for users using Streamlit, Dash, or alternatives, (3) add tests for the package, (4) when having a pull request or push to main, start all tests using git actions.

### Actions

Based on the answer from the LLM, I did the following:

- created the package structure
- created the calculator module
- created the UI module
- created the tests
- created the GitHub actions workflow
- replace placeholders in the code with my name and email
- created the README file
- created the setup.py file
- created the requirements.txt file
- created pyproject.toml file
- created .gitignore file

## Ask how to test the code

### Prompt

How to test this package locally, including install required dependencies?

### Actions

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Run tests

```bash
pytest --cov=src.python_calculator --cov-report=html
```

## Found errors in testing, ask how to fix

### Prompt

When I run the tests, I got the following error:

```
Got error when run pytest --cov=src.python_calculator --cov-report=html: ImportError while importing test module 'E:\github\python-calculator\tests\test_calculator.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\zhang\.pyenv\pyenv-win\versions\3.13.7\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\test_calculator.py:4: in <module>
    from src.python_calculator.calculator import Calculator
E   ModuleNotFoundError: No module named 'src'
```

### Actions

The response did not directly address the issue, but the answers gave me some hints.

The error indicates that the `src` module is not found. This is likely because the `src` directory is not in the Python path. To fix this, you can modify the `PYTHONPATH` environment variable to include the `src` directory before running the tests.

To this end, I add `pythonpath = ["src"]` to the `pytest` section of `pyproject.toml` file,
and then removed `src.` prefix in the import statements in the test files.

## Publish the package

### Prompt

How can I package this package and published to test.pypi for a test installation?

### Actions

#### Install required tools

```bash
pip install build twine
```

#### Build the package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build source distribution and wheel
python -m build
```

#### Test the build locally

```bash
# install
pip install dist/python_calculator-0.1.0-py3-none-any.whl
## and one can find where the package is installed
pip show python-calculator

# Test the package
python -c "
from python_calculator import Calculator
calc = Calculator()
print('2 + 3 =', calc.calculate('2 + 3'))
print('2 ^ 3 =', calc.calculate('2 ^ 3'))
"

# uninstall
pip uninstall python-calculator
```

#### Create a TestPyPI account 

Do it at https://test.pypi.org/account/register/
and get your API token at https://test.pypi.org/manage/account/token/.

One can put the API token in `~/.pypirc` file as follows to avoid
typing the token every time when uploading the package.:

```
[distutils]
index-servers = testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your-api-token-here
```

For more details check https://packaging.python.org/en/latest/specifications/pypirc/.

#### Upload the package to TestPyPI

```bash
twine upload --repository testpypi dist/*

# If you have API token set as environment variable:
# export TWINE_USERNAME=__token__
# export TWINE_PASSWORD=your-api-token-here
# python -m twine upload --repository testpypi dist/*
```

Actually when I upload the package, I got the error that I was
not allowed to upload the package `python-calculator` to TestPyPI,
and point me to https://test.pypi.org/help/#project-name.

This turned out that the package name `python-calculator` is already taken.

One quick way to check whether a package name is available is to
run the following command:

```bash
curl https://test.pypi.org/pypi/python-calculator/json
```

It will return 404 not found if the package name is available, otherwise
it will return the package information.

So I changed the package name to `python-calculator-fortune9` in `pyproject.toml` file,
and then rebuilt and uploaded the package again, which worked.


Test installing the package from TestPyPI

```bash
# create a new virtual environment
python -m venv test-env
source test-env/bin/activate  # On Windows use `test-env\Scripts\activate`
pip install --index-url https://test.pypi.org/simple/ --no-deps python-calculator-fortune9

# test the package
python -c "
from python_calculator import Calculator
calc = Calculator()
print('2 + 3 =', calc.calculate('2 + 3'))
print('2 ** 3 =', calc.calculate('2 ** 3'))
"

# use here document string to avoid escaping issues in Windows
python << 'EOF'
from python_calculator import Calculator
calc = Calculator()
print('Testing core calculator:')
print('2 + 3 =', calc.add(2, 3))
print('2 ^ 3 =', calc.calculate('2 ^ 3'))
print('(1+2)*3 =', calc.calculate('(1+2)*3'))
EOF

# deactivate the virtual environment
deactivate # on Windows use `test-env\Scripts\deactivate.bat`
```

#### Now push the code to GitHub main branch

```bash
git add .
git commit -m "Release version 0.1.0"
git tag v0.1.0
git push origin main --tags
```

