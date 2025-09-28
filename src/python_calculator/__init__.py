"""A simple calculator package with UI capabilities."""

__version__ = "0.1.0"
__author__ = "Zhenguo Zhang"
__email__ = "zhangz.sci@gmail.com"

from .calculator import Calculator
from .ui import DashUI, StreamlitUI

__all__ = ["Calculator", "StreamlitUI", "DashUI"]
