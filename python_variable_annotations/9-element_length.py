#!/usr/bin/env python3
"""Returns a function that multiplies a float by a given multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a multiplier and returns a function that multiplies
    a float by it.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func


if __name__ == "__main__":
    # Test the function
    times_2_5 = make_multiplier(2.5)
    print(times_2_5(3))  # Output: 7.5

    times_10 = make_multiplier(10)
    print(times_10(5))  # Output: 50
