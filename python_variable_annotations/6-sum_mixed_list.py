#!/usr/bin/env python3
"""sum_mixed_list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all the elements in mxd_lst
    """
    return sum(mxd_lst)