#!/usr/bin/env python3
"""sum up a list containg integers and floats"""
from typing import List, Union
"""import list and unions"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes in a list of integers and floats"""
    result = sum(mxd_lst)
    return result
