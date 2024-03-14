#!/usr/bin/env python3
"""sum up a list containg integers and floats"""
from collections.abc import Callable
"""imports Callable"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function for multipliying a number"""
    def multiply(number: float) -> float:
        """multiplies"""
        return number * multiplier
    return multiply
