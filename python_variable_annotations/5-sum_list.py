#!/usr/bin/env python3
"""Returns the sum of a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Adds up all the numbers in the list."""
    return sum(input_list)


if __name__ == "__main__":
    # Test the function
    my_list = [1.5, 2.5, 3.5]
    print(sum_list(my_list))  # Output: 7.5
