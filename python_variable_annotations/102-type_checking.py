#!/usr/bin/env python3
"""Module for type checking with mypy."""

import typing
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of a tuple by repeating each element.

    Args:
        lst: A tuple containing elements to be zoomed
        factor: Number of times to repeat each element (default: 2)

    Returns:
        A list with each element from the tuple repeated factor times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
