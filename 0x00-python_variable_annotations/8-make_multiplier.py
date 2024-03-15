#!/usr/bin/env python3
"""Sum up a list containing integers and floats."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function for multiplying a number."""
    def multiply(number: float) -> float:
        """Multiply the number and the multiplier."""
        return number * multiplier

    return multiply
