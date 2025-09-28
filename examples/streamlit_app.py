"""Example Streamlit application."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.python_calculator.ui import StreamlitUI

if __name__ == "__main__":
    ui = StreamlitUI()
    ui.render()