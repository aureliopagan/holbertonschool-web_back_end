#!/usr/bin/env python3
"""Returns a function that multiplies a float by a given multiplier."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a multiplier and returns a function that multiplies a float by it."""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
