#!/usr/bin/env python3
"""Module with duck-typed function for safe first element access"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Optional[typing.Any]:
    """Return the first element of a sequence or None if empty"""
    if lst:
        return lst[0]
    else:
        return None
