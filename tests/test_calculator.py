"""Tests for the calculator module."""

import pytest
from python_calculator.calculator import Calculator

class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Setup before each test."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 5) == 5
    
    def test_subtraction(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiplication(self):
        """Test multiplication operation."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
    
    def test_division(self):
        """Test division operation."""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-6, 3) == -2
    
    def test_division_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(4, 0.5) == 2
    
    def test_calculate_expression(self):
        """Test expression calculation."""
        assert self.calc.calculate("2 + 3") == 5
        assert self.calc.calculate("10 - 4") == 6
        assert self.calc.calculate("3 * 4") == 12
        assert self.calc.calculate("15 / 3") == 5
        assert self.calc.calculate("2 ** 3") == 8
        assert self.calc.calculate("(2 + 3) * 4") == 20
    
    def test_calculate_invalid_expression(self):
        """Test invalid expression handling."""
        with pytest.raises(ValueError):
            self.calc.calculate("2 + abc")
        
        with pytest.raises(ValueError):
            self.calc.calculate("import os")
    
    def test_calculate_empty_expression(self):
        """Test empty expression handling."""
        with pytest.raises(ValueError):
            self.calc.calculate("")