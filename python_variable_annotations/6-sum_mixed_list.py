#!/usr/bin/env python3
"""Returns the sum of a list of mixed integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adds up all the numbers in the mixed list and returns a float."""
    return sum(mxd_lst)


if __name__ == "__main__":
    # Test the function
    my_list = [1, 2.5, 3, 4.5]
    print(sum_mixed_list(my_list))  # Output: 11.0
