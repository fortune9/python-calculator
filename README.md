# Python Calculator

A simple calculator package with UI capabilities built using Python.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division, power)
- Expression evaluation
- Streamlit-based web UI
- Dash-based web UI
- Comprehensive test suite
- CI/CD with GitHub Actions

## Installation

### Basic installation (core functionality only):
```bash
pip install git+https://github.com/fortune9/python-calculator.git
```

### To install from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps python-calculator-fortune9
```

### With UI dependencies (not working yet):

```bash

# For Streamlit UI
pip install "python-calculator[streamlit]"

# For Dash UI
pip install "python-calculator[dash]"

# For all features
pip install "python-calculator[all]"

# For development
pip install "python-calculator[dev]"
```

## Usage

### As a Python package:

```python
from python_calculator import Calculator

calc = Calculator()
result = calc.calculate("2 + 3 * 4")  # Returns 14.0
result = calc.calculate("2 ^ 3")      # Returns 8.0 (power operator)
```

### Streamlit UI:

```bash
pip install "python-calculator[streamlit]"
python -c "from python_calculator.ui import StreamlitUI; import streamlit as st; ui = StreamlitUI(); ui.render()"
```

### Dash UI:

```bash
pip install "python-calculator[dash]"
python -c "from python_calculator.ui import DashUI; ui = DashUI(); ui.run()"
```

## Development

### Running tests:

```bash
pip install "python-calculator[dev]"
pytest
```

### Running tests with coverage:

```bash
pip install "python-calculator[dev]"
pytest --cov=python_calculator tests/
```

## License

MIT License
