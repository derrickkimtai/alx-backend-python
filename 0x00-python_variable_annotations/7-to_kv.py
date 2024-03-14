#!/usr/bin/env python3
"""returns tupel"""
from typing import Union, Tuple
"""returns tupel"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """retruns a tupel"""
    square = (v ** 2)
    result = (k, square)

    return result
