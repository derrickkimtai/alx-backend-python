#!/usr/bin/env python3

from typing import Tuple, Any
"""imports the above"""


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
        Zooms in on the given tuple

    Args:
        lst: The input tuple to be zoomed in.
        factor: The zoom factor. Default is 2.

    Returns:
        A new tuple containing elements of the input
    """
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: Tuple[int, ...] = zoom_array(array)

zoom_3x: Tuple[int, ...] = zoom_array(array, 3)
