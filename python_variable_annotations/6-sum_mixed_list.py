#!/usr/bin/env python3
"""Returns the sum of a list of mixed integers and floats."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adds up all the numbers in the mixed list and returns a float."""
    return sum(mxd_lst)
