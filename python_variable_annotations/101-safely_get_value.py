#!/usr/bin/env python3
"""Module for safely getting values from dictionaries with type annotations."""

import typing

T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping,
                    key: typing.Any,
                    default: typing.Union[T, None] = None
                    ) -> typing.Union[typing.Any, T]:
    """
    Safely get a value from a dictionary-like object.
    
    Args:
        dct: A mapping object (dict-like)
        key: The key to look up
        default: Default value to return if key not found
        
    Returns:
        The value from the mapping if key exists, otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
