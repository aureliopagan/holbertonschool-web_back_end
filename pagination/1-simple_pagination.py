#!/usr/bin/env python3
"""
Simple pagination module for paginating a database of popular baby names.

This module provides functionality to paginate through a CSV dataset
using simple page and page_size parameters.
"""
import csv
import math
from typing import List, Tuple


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
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.
        
        Returns the cached dataset, excluding the header row.
        The dataset is loaded only once and cached for subsequent calls.
        
        Returns:
            List[List]: The dataset as a list of rows (excluding header)
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset based on pagination parameters.
        
        Retrieves a specific page from the dataset using the provided
        page number and page size. Validates input parameters and
        returns an empty list if the requested page is out of range.
        
        Args:
            page (int): The page number (must be positive integer, default 1)
            page_size (int): Number of items per page (must be positive integer, default 10)
            
        Returns:
            List[List]: The requested page of data, or empty list if out of range
            
        Raises:
            AssertionError: If page or page_size are not positive integers
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []
            
        return dataset[start_index:end_index]
