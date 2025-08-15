#!/usr/bin/env python3
"""
Simple helper function for pagination.

This module provides a utility function to calculate index ranges
for pagination purposes in datasets.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.
    
    Given a page number and page size, this function returns a tuple
    containing the start index and end index corresponding to the range
    of indexes to return in a list for those pagination parameters.
    
    Page numbers are 1-indexed, meaning the first page is page 1.
    
    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page
        
    Returns:
        Tuple[int, int]: A tuple containing (start_index, end_index)
        
    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
