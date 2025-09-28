"""Example Dash application."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.python_calculator.ui import DashUI

if __name__ == "__main__":
    ui = DashUI()
    ui.run(debug=True, port=8050)