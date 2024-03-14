#!/usr/bin/env python3
"""imported those """
from typing import Iterable, Sequence, List, Tuple
"""imported thi all for the answer"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """elements in the function"""
    return [(i, len(i)) for i in lst]
