#!/usr/bin/env python3
"""Returns a tuple with a string and the square of a number."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and a number, returns a tuple with the string and the square of the number."""
    return (k, v * v)
