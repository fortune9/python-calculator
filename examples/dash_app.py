"""Example Dash application."""

from python_calculator.ui import DashUI

if __name__ == "__main__":
    ui = DashUI()
    ui.run(debug=True, port=8050)
