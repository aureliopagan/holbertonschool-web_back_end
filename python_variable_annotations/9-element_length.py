#!/usr/bin/env python3
"""Returns a list of tuples containing sequences and their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    with each sequence and its length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    # Test the function
    my_list = ["hello", "world", "python"]
    print(element_length(my_list))  # Output: [('hello', 5), ('world', 5), ('python', 6)]
