"""Core calculator functionality."""

import operator


class Calculator:
    """A simple arithmetic calculator."""

    def __init__(self) -> None:
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow,
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluate a mathematical expression.

        Args:
            expression: Mathematical expression as string

        Returns:
            float: Result of the calculation

        Raises:
            ValueError: If expression is invalid
        """
        try:
            # Basic safety check - only allow numbers and operators
            allowed_chars = set("0123456789.+-*/^() ")
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")

            # Use eval for simplicity (with safety restrictions)
            # In production, consider using a proper parser like ast.literal_eval
            # or implementing a shunting-yard algorithm
            result = eval(expression, {"__builtins__": {}}, self.operations)
            return float(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Raise a to the power of b."""
        return a**b  # type: ignore[no-any-return]
